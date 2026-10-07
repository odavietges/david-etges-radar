"""Verifica os arquivos públicos do THE PULSE sem escrever no repositório."""
import hashlib
import json
import re
import time
from datetime import datetime
from pathlib import Path
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://odavietges.github.io/david-etges-radar/"
registry = json.loads((ROOT / "arquivo/edicoes.json").read_text(encoding="utf-8"))
editions = registry["editions"]
dates = [entry["date"] for entry in editions]
assert dates and dates == sorted(set(dates), reverse=True), "Datas ausentes, fora de ordem ou duplicadas"
date = dates[0]
assert re.fullmatch(r"\d{4}-\d{2}-\d{2}", date), "Data inválida"
html = (ROOT / "index.html").read_text(encoding="utf-8")
assert f'content="{date}"' in html and 'name="pulse-edition-date"' in html
assert 'name="pulse-edition-status" content="complete"' in html
assert f'data-edition-date="{date}"' in html
assert "America/Cuiaba" in html, "Aviso de data não encontrado"
assert f"{date}.html" in (ROOT / "arquivo/index.html").read_text(encoding="utf-8")
targets = ["index.html", f"arquivo/{date}.html", "arquivo/edicoes.json", "arquivo/index.html"]
for entry in editions:
    assert re.fullmatch(r"\d{4}-\d{2}-\d{2}\.html", entry["path"])
    assert entry["path"] == entry["date"] + ".html"
    path = "arquivo/" + entry["path"]
    assert (ROOT / path).is_file(), f"Arquivo ausente: {path}"
    if path not in targets:
        targets.append(path)
expected = {path: (ROOT / path).read_bytes() for path in targets}
deadline = time.monotonic() + 600
while True:
    failures = []
    for path, wanted in expected.items():
        try:
            req = Request(BASE + path, headers={"Cache-Control": "no-cache", "User-Agent": "THE-PULSE-public-validation"})
            with urlopen(req, timeout=25) as response:
                actual = response.read()
            if actual != wanted:
                failures.append(path + ": conteúdo público difere do commit")
        except Exception as error:
            failures.append(path + ": " + str(error))
    if not failures:
        break
    if time.monotonic() >= deadline:
        raise RuntimeError("\n".join(failures))
    print("Aguardando Pages: " + "; ".join(failures), flush=True)
    time.sleep(20)
now = datetime.now(ZoneInfo("America/Cuiaba"))
lines = [f"Edição pública verificada: {date}", f"Verificada em: {now.isoformat()}",
         f"Data corrente no fuso: {now.date().isoformat()}",
         f"Edição corresponde à data corrente: {date == now.date().isoformat()}"]
for path, data in expected.items():
    lines.append(f"OK {BASE}{path} SHA256={hashlib.sha256(data).hexdigest()}")
print("\n".join(lines))
import os
summary = os.environ.get("GITHUB_STEP_SUMMARY")
if summary:
    with open(summary, "a", encoding="utf-8") as file:
        file.write("## Verificação pública do THE PULSE\n\n" + "\n\n".join(lines) + "\n")
