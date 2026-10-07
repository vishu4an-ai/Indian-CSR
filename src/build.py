"""Builds ../index.html from page.html (template) and companies.json (data)."""
import json, pathlib
here = pathlib.Path(__file__).resolve().parent
data = json.loads((here / "companies.json").read_text(encoding="utf-8"))
js = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
tpl = (here / "page.html").read_text(encoding="utf-8")
assert tpl.count("/*__DATA__*/[]") == 1
(here.parent / "index.html").write_text(tpl.replace("/*__DATA__*/[]", js), encoding="utf-8")
print("built", here.parent / "index.html")
