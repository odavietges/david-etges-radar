import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('estado', Path(__file__).resolve().parents[1] / 'operacao/estado_publicacao.py')
estado = importlib.util.module_from_spec(spec)
spec.loader.exec_module(estado)
SHA = 'a' * 40

def run(name, sha=SHA, conclusion='success'):
    return dict(name=name, head_sha=sha, status='completed', conclusion=conclusion)

class PublicationTests(unittest.TestCase):
    def check(self, date='2026-10-23', runs=None, publisher=None):
        return estado.monitor_result('2026-10-23', date, SHA, runs or [], publisher or {})[0]

    def test_old_edition_during_research_is_late(self):
        self.assertFalse(self.check('2026-10-22', publisher={'status':'in_progress'}))

    def test_no_publication_detected(self):
        self.assertFalse(self.check('2026-10-22'))

    def test_commit_alone_is_insufficient(self):
        self.assertFalse(self.check())

    def test_deploy_alone_is_insufficient(self):
        self.assertFalse(self.check(runs=[run('pages build and deployment')]))

    def test_success_from_other_sha_rejected(self):
        self.assertFalse(self.check(runs=[run('pages build and deployment'), run('Validar publicação pública', sha='b'*40)]))

    def test_cancelled_deploy_does_not_hide_successful_deploy(self):
        self.assertTrue(self.check(runs=[run('pages build and deployment', conclusion='cancelled'), run('pages build and deployment'), run('Validar publicação pública')]))

    def test_validation_run_name_can_include_publication_id(self):
        validation = run('Validar publicação pública · 123-1')
        validation['path'] = '.github/workflows/validar-publicacao.yml'
        self.assertTrue(self.check(runs=[run('pages build and deployment'), validation]))

    def test_failed_validation_never_confirms(self):
        self.assertFalse(self.check(runs=[run('pages build and deployment'), run('Validar publicação pública', conclusion='failure')]))

    def test_dispatch_sha_mismatch_fails_before_api(self):
        with patch.dict('os.environ', {'EXPECTED_SHA':SHA, 'GITHUB_SHA':'b'*40}), patch.object(estado, 'api') as api:
            with self.assertRaises(AssertionError):
                estado.await_pages()
            api.assert_not_called()

    def test_deploy_timeout_fails(self):
        with patch.dict('os.environ', {'EXPECTED_SHA':SHA, 'GITHUB_SHA':SHA}), patch.object(estado.subprocess, 'check_output', return_value=SHA), patch.object(estado, 'pages_run', return_value=None), patch.object(estado.time, 'monotonic', side_effect=[0, 601]):
            with self.assertRaises(RuntimeError):
                estado.await_pages()


class PublicBytesTests(unittest.TestCase):
    def invoke(self, divergent=False, expected_date='2026-10-23'):
        import contextlib
        import io
        import runpy
        root = Path(__file__).resolve().parents[1]
        def fetch(request, timeout):
            path = request.full_url.split('/david-etges-radar/', 1)[1]
            data = (root / path).read_bytes()
            return io.BytesIO(data + b'changed' if divergent else data)
        import json
        count = len(json.loads((root / 'arquivo/edicoes.json').read_text())['editions']) + 3
        ticks = iter([0] + [1]*count + [601]*(count + 100))
        env = {'GITHUB_SHA':SHA, 'EXPECTED_SHA':SHA, 'EXPECTED_DATE':expected_date, 'GITHUB_STEP_SUMMARY':''}
        with patch.dict('os.environ', env), patch('sys.argv', ['verificar_publicacao.py']), patch('urllib.request.urlopen', side_effect=fetch), patch('time.monotonic', side_effect=lambda:next(ticks)), contextlib.redirect_stdout(io.StringIO()):
            runpy.run_path(str(root / 'operacao/verificar_publicacao.py'), run_name='__main__')

    def test_public_bytes_and_full_history_match(self):
        import json
        root = Path(__file__).resolve().parents[1]
        date = json.loads((root/'arquivo/edicoes.json').read_text())['editions'][0]['date']
        self.invoke(expected_date=date)

    def test_divergent_public_bytes_fail(self):
        import json
        root = Path(__file__).resolve().parents[1]
        date = json.loads((root/'arquivo/edicoes.json').read_text())['editions'][0]['date']
        with self.assertRaises(RuntimeError):
            self.invoke(divergent=True, expected_date=date)

    def test_wrong_expected_date_fails(self):
        with self.assertRaises(AssertionError):
            self.invoke(expected_date='2000-01-01')

if __name__ == '__main__':
    unittest.main()
