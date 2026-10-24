"""Estado do Pages e monitor de pontualidade; somente leitura, sem credenciais editoriais."""
import base64
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

REPO = 'odavietges/david-etges-radar'


def api(path):
    assert os.environ['GITHUB_REPOSITORY'] == REPO
    req = Request(f'https://api.github.com/repos/{REPO}/{path}', headers={
        'Authorization': 'Bearer ' + os.environ['GH_TOKEN'],
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28'})
    with urlopen(req, timeout=25) as response:
        return json.load(response)


def succeeded(runs, sha, name):
    return next((r for r in runs if r['head_sha'] == sha and (r['name'] == name or
                 (name == 'Validar publicação pública' and r.get('path') == '.github/workflows/validar-publicacao.yml'))
                 and r['status'] == 'completed' and r['conclusion'] == 'success'), None)


def pages_run(sha):
    return succeeded(api(f'actions/runs?head_sha={sha}&per_page=100')['workflow_runs'],
                     sha, 'pages build and deployment')


def await_pages():
    sha = os.environ['EXPECTED_SHA']
    assert re.fullmatch('[0-9a-f]{40}', sha), 'SHA inválido'
    assert os.environ['GITHUB_SHA'] == sha, 'SHA do disparo diverge do esperado'
    assert subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip() == sha
    deadline = time.monotonic() + 600
    while True:
        run = pages_run(sha)
        if run:
            print(f'Deploy confirmado: {run["html_url"]}; SHA {sha}', flush=True)
            return
        if time.monotonic() >= deadline:
            raise RuntimeError('Pages não confirmou deploy success para o SHA esperado no prazo')
        print('Aguardando deploy Pages do SHA ' + sha, flush=True)
        time.sleep(min(20, max(0, deadline - time.monotonic())))


def monitor_result(today, date, sha, runs, publisher):
    if date != today:
        state = publisher.get('status', 'ausente')
        conclusion = publisher.get('conclusion') or 'pendente'
        return False, f'ATRASO: edição de {today} ausente; última {date}. Publicador: {state}/{conclusion}.'
    if not succeeded(runs, sha, 'pages build and deployment'):
        return False, 'ATRASO: edição corrente no Git, mas deploy Pages do head ainda não confirmado.'
    if not succeeded(runs, sha, 'Validar publicação pública'):
        return False, 'ATRASO: edição corrente com deploy, mas validação pública do head ainda não confirmada.'
    return True, f'Edição {date}, Pages e validação pública confirmados para {sha}.'


def monitor():
    today = datetime.now(ZoneInfo('America/Cuiaba')).date().isoformat()
    # Consultar o head vivo: o SHA congelado do schedule não é prova de ausência da edição.
    sha = api('branches/main')['commit']['sha']
    contents = api(f'contents/arquivo/edicoes.json?ref={sha}')
    registry = json.loads(base64.b64decode(contents['content']))
    date = registry['editions'][0]['date']
    runs = api(f'actions/runs?head_sha={sha}&per_page=100')['workflow_runs']
    publishers = api('actions/workflows/publicar-codex.yml/runs?branch=main&per_page=20')['workflow_runs']
    publisher = next((r for r in publishers if datetime.fromisoformat(r['created_at'].replace('Z', '+00:00'))
                      .astimezone(ZoneInfo('America/Cuiaba')).date().isoformat() == today), {})
    ok, message = monitor_result(today, date, sha, runs, publisher)
    if api('branches/main')['commit']['sha'] != sha:
        ok, message = False, 'Publicação mudou durante o monitoramento; confirmação ainda pendente.'
    if publisher:
        message += '\nPublicador: ' + publisher['html_url']
    print(message, flush=True)
    summary = os.environ.get('GITHUB_STEP_SUMMARY')
    if summary:
        with open(summary, 'a', encoding='utf-8') as file:
            file.write('## Pontualidade do THE PULSE\n\n' + message + '\n')
    if not ok:
        raise RuntimeError(message)


if __name__ == '__main__':
    {'await-pages': await_pages, 'monitor': monitor}[sys.argv[1]]()
