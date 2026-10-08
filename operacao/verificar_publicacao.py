"""Verifica os arquivos públicos do THE PULSE sem escrever no repositório."""
import argparse
import hashlib
from html.parser import HTMLParser
import json
import re
import time
from datetime import datetime
from pathlib import Path
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo
import os

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--require-current", action="store_true",
                    help="Exigir edição da data corrente em America/Cuiaba")
args = parser.parse_args()
ROOT = Path(__file__).resolve().parents[1]
BASE = "https://odavietges.github.io/david-etges-radar/"
registry = json.loads((ROOT / "arquivo/edicoes.json").read_text(encoding="utf-8"))
editions = registry["editions"]
dates = [entry["date"] for entry in editions]
assert dates and dates == sorted(set(dates), reverse=True), "Datas ausentes, fora de ordem ou duplicadas"
date = dates[0]
assert re.fullmatch(r"\d{4}-\d{2}-\d{2}", date), "Data inválida"
html = (ROOT / "index.html").read_text(encoding="utf-8")
class PageInfo(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.metadata = {}
        self.body_date = None
        self.links = set()
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "meta" and attrs.get("name", "").startswith("pulse-edition-"):
            name = attrs["name"]
            if name in self.metadata:
                raise ValueError(f"Metadado duplicado: {name}")
            self.metadata[name] = attrs.get("content")
        if tag == "body":
            self.body_date = attrs.get("data-edition-date")
        if tag == "a" and "href" in attrs:
            self.links.add(attrs["href"])

def require_edition(text, label):
    info = PageInfo(text)
    assert info.metadata.get("pulse-edition-date") == date, f"Data divergente: {label}"
    assert info.metadata.get("pulse-edition-status") == "complete", f"Edição incompleta: {label}"
    assert info.body_date == date, f"Data do body divergente: {label}"
    return info

require_edition(html, "index.html")
archive_html = (ROOT / f"arquivo/{date}.html").read_text(encoding="utf-8")
require_edition(archive_html, f"arquivo/{date}.html")
assert "America/Cuiaba" in html, "Aviso de data não encontrado"
index_info = PageInfo((ROOT / "arquivo/index.html").read_text(encoding="utf-8"))
for entry in editions:
    assert entry["path"] in index_info.links, f"Link ausente do histórico: {entry['path']}"
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
lines = [f"Commit verificado: {os.environ.get('GITHUB_SHA', 'indisponivel')}",
         f"Edição pública verificada: {date}", f"Verificada em: {now.isoformat()}",
         f"Data corrente no fuso: {now.date().isoformat()}",
         f"Edição corresponde à data corrente: {date == now.date().isoformat()}"]
for path, data in expected.items():
    lines.append(f"OK {BASE}{path} SHA256={hashlib.sha256(data).hexdigest()}")
print("\n".join(lines))
summary = os.environ.get("GITHUB_STEP_SUMMARY")
if summary:
    with open(summary, "a", encoding="utf-8") as file:
        file.write("## Verificação pública do THE PULSE\n\n" + "\n\n".join(lines) + "\n")

if args.require_current and date != now.date().isoformat():
    raise RuntimeError(
        f"Edição de hoje ainda não confirmada: esperado {now.date().isoformat()}, "
        f"edição pública verificada {date}. A última edição válida foi preservada."
    )
