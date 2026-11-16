#!/usr/bin/env python3
"""Plain-text Devanagari PDFs of the hymns (text only, no commentary).
Run: NODE_PATH=$(npm root -g) python3 tools/make_pdfs.py
Reads the verses straight from tools/build.py so the PDFs always match the site."""
import os, sys, re, json, subprocess, html
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import build

DIG = str.maketrans("0123456789", "०१२३४५६७८९")
def dn(n): return str(n).translate(DIG)

def lines_of(v): return [l.strip() for l in v["deva"].split("<br>") if l.strip()]

def verse_block(lines, num=None):
    ls = [l for l in lines]
    last = ls[-1].rstrip("॥").rstrip()
    tail = f" ॥{dn(num)}॥" if num is not None else " ॥"
    ls[-1] = last + tail
    return '<div class="v">' + "".join(f"<div>{html.escape(l)}</div>" for l in ls) + "</div>"

def sri_body():
    out = []
    for v in build.VERSES:
        if v["n"] == build.TOTAL_SRI:
            out.append('<div class="sub">फलश्रुतिः</div>' + verse_block(lines_of(v), None))
        else:
            out.append(verse_block(lines_of(v), v["n"]))
    return "".join(out)

def kana_body():
    return "".join(verse_block(lines_of(v), v["n"]) for v in build.KVERSES)

def mla_body():
    out = []
    for v in build.MVERSES:
        ls = lines_of(v)
        if v["n"] == 9:   # phalashruti: verses 9, 10, 11 are one couplet each
            out.append('<div class="sub">फलश्रुतिः</div>')
            for k in range(0, len(ls), 2):
                out.append(verse_block(ls[k:k+2], 9 + k // 2))
        else:
            out.append(verse_block(ls, v["n"]))
    return "".join(out)

DOCS = [
 dict(slug="sri-suktam-devanagari", deva="श्री सूक्तम्", roman="Śrī Sūktam", sub="ऋग्वेदखिलसूक्तम्", body=sri_body, count=len(build.VERSES), page="sri-suktam/"),
 dict(slug="kanakadhara-stotram-devanagari", deva="कनकधारा स्तोत्रम्", roman="Kanakadhāra Stotram", sub="श्रीमच्छङ्कराचार्यविरचितम्", body=kana_body, count=len(build.KVERSES), page="kanakadhara/"),
 dict(slug="mahalakshmi-ashtakam-devanagari", deva="महालक्ष्म्यष्टकम्", roman="Mahālakṣmī Aṣṭakam", sub="", body=mla_body, count=11, page="mahalakshmi-ashtakam/"),
]

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+Devanagari:wght@400;600;700&family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&display=swap');
@page{size:A4;margin:22mm 20mm 24mm}
*{box-sizing:border-box;margin:0}
body{font-family:'Noto Serif Devanagari',serif;color:#1d1410;font-size:19pt;line-height:1.95;text-align:center}
.top{padding-bottom:10mm;margin-bottom:9mm;border-bottom:1.2pt solid #b98a2e}
.shri{font-size:26pt;color:#8c1d2a;font-weight:600;line-height:1.9}
h1{font-size:30pt;font-weight:700;color:#5a1522;line-height:1.5;margin-top:2mm}
.roman{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:16pt;color:#7a5a3a;margin-top:1mm;line-height:1.3}
.src{font-size:13pt;color:#7a5a3a;margin-top:3mm;line-height:1.5}
.v{break-inside:avoid;margin:0 0 9mm}
.v div{white-space:nowrap}
.sub{break-after:avoid;font-size:17pt;font-weight:700;color:#8c1d2a;margin:2mm 0 4mm}
"""

def doc_html(d):
    src = f'<div class="src">{html.escape(d["sub"])}</div>' if d["sub"] else ""
    return f'''<!doctype html><html lang="sa"><head><meta charset="utf-8"><title>{d["roman"]} – Devanagari text</title><style>{CSS}</style></head><body>
<div class="top"><div class="shri">श्री</div><h1>{d["deva"]}</h1><div class="roman">{d["roman"]}</div>{src}</div>
{d["body"]()}
</body></html>'''

JS = r"""
const {chromium}=require('playwright');
(async()=>{const [,, inp, out, label]=process.argv;
const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+inp);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(1500);
const tpl=`<div style="width:100%;font-size:8.5px;color:#8a6d3b;font-family:Georgia,serif;text-align:center;padding:0 20mm">${label} &nbsp;·&nbsp; lakshmistuti.com &nbsp;·&nbsp; page <span class="pageNumber"></span> of <span class="totalPages"></span></div>`;
await p.pdf({path:out,format:'A4',printBackground:true,displayHeaderFooter:true,headerTemplate:'<span></span>',footerTemplate:tpl,margin:{top:'22mm',bottom:'24mm',left:'20mm',right:'20mm'}});
await b.close();})();
"""

if __name__ == "__main__":
    tmp = os.environ.get("PDF_TMP", "/tmp"); os.makedirs(tmp, exist_ok=True)
    js = os.path.join(tmp, "pdf_render.js"); open(js, "w").write(JS)
    outdir = os.path.join(ROOT, "assets", "downloads"); os.makedirs(outdir, exist_ok=True)
    for d in DOCS:
        h = os.path.join(tmp, d["slug"] + ".html"); open(h, "w", encoding="utf-8").write(doc_html(d))
        o = os.path.join(outdir, d["slug"] + ".pdf")
        subprocess.run(["node", js, h, o, d["roman"]], check=True)
        print(d["slug"], os.path.getsize(o))
