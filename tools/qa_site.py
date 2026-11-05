#!/usr/bin/env python3
"""Static QA over the built site (run after tools/build.py)."""
import os, re, sys, json, glob, html as H
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
pages = [p for p in glob.glob(ROOT + "/**/index.html", recursive=True) if "/tools/" not in p] + [ROOT + "/404.html"]
errs = []; titles = {}
def e(p, m): errs.append(f"{os.path.relpath(p, ROOT)}: {m}")
def exists(url):
    u = url.split("#")[0].split("?")[0]
    if not u.startswith("/"): return True
    f = ROOT + u
    return os.path.isfile(f) or os.path.isfile(f.rstrip("/") + "/index.html") or (u.endswith("/") and os.path.isfile(f + "index.html"))
for p in pages:
    s = open(p, encoding="utf-8").read()
    t = re.search(r"<title>(.*?)</title>", s, re.S); d = re.search(r'<meta name="description" content="(.*?)"', s)
    if not t: e(p, "no title"); continue
    tt = H.unescape(t.group(1)); titles.setdefault(tt, []).append(p)
    if len(tt) > 66: e(p, f"title {len(tt)} chars")
    if d and len(H.unescape(d.group(1))) > 160: e(p, f"description {len(H.unescape(d.group(1)))} chars")
    if s.count("<h1") != 1: e(p, f"{s.count('<h1')} h1")
    for bad in ("&lt;em", "&lt;a ", "&amp;lt;", "&amp;amp;", "None", "{", "@@PUB@@", "@@MOD@@"):
        if bad in re.sub(r"<script.*?</script>|<style.*?</style>", "", s, flags=re.S): e(p, f"found {bad!r}")
    for m in re.finditer(r'(?:href|src)="(/[^"]*)"', s):
        if not exists(m.group(1)): e(p, f"broken link {m.group(1)}")
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        try: json.loads(m.group(1))
        except Exception as x: e(p, f"bad JSON-LD {x}")
    if "/verse-" in p and "sri-yantra" not in p:
        n_f = s.count('class="fcard'); n_k = len(re.findall(r'<li><span class="ic ic\d">', s))
        if n_f != n_k: e(p, f"form cards {n_f} vs highlights {n_k}")
        if "ov-sketch" not in s: e(p, "no sketch card")
        if 'class="hh vh2"' not in s: e(p, "no hero")
        if "verse.js" not in s: e(p, "no verse.js")
for t, ps in titles.items():
    if len(ps) > 1: errs.append(f"duplicate title {t!r}: {[os.path.relpath(x, ROOT) for x in ps]}")
sm = open(ROOT + "/sitemap.xml", encoding="utf-8").read()
for u in re.findall(r"<loc>https://lakshmistuti.com(/[^<]*)</loc>", sm):
    if not exists(u): errs.append(f"sitemap URL missing page {u}")
print(f"{len(pages)} pages, {len(errs)} problems")
for x in errs: print(" -", x)
sys.exit(1 if errs else 0)
