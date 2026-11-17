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

def lotus():
    petal = "M0,0 C-30,-34 -28,-100 0,-146 C28,-100 30,-34 0,0 Z"
    rings = [(1.0, [-90,-60,-30,0,30,60,90], "#8e1c63", "#c0457f"), (0.8, [-75,-45,-15,15,45,75], "#d9435f", "#f0766f"), (0.58, [-60,-30,0,30,60], "#ffa63d", "#ffd079")]
    g = []
    for k, (sc, angs, c1, c2) in enumerate(rings):
        for a in angs:
            g.append(f'<path d="{petal}" transform="rotate({a}) scale({sc})" fill="url(#pg{k})" stroke="#f2c4b2" stroke-width="1.2"/>')
    defs = "".join(f'<linearGradient id="pg{k}" x1="0" y1="0" x2="0" y2="-1" gradientUnits="objectBoundingBox"><stop offset="0" stop-color="{c2}"/><stop offset="1" stop-color="{c1}"/></linearGradient>' for k,(sc,an,c1,c2) in enumerate(rings))
    return f'<svg viewBox="-190 -160 380 230" class="lot" style="overflow:visible"><defs>{defs}<radialGradient id="gold"><stop offset="0" stop-color="#ffe9a0"/><stop offset="1" stop-color="#d89a22"/></radialGradient></defs>{"".join(g)}<circle r="26" cy="-6" fill="url(#gold)"/><text y="4" text-anchor="middle" font-size="28" font-weight="700" fill="#7a1f2b" font-family="Noto Serif Devanagari">श्री</text></svg>'

def stars():
    import random; r = random.Random(11); o = []
    while len(o) < 34:
        x, y, z = r.uniform(12, 198), r.uniform(10, 205), r.choice([.35, .4, .5, .6, .8, 1.0])
        if 20 < x < 190 and 24 < y < 150: continue      # keep the title area clear
        if 25 < x < 185 and 150 <= y < 205 and abs(x - 105) < 60: continue   # keep the lotus area clear
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{z:.2f}" fill="#ffe9a8"/>')
    return "".join(o)

def backdrop():
    return ('<svg class="bg" viewBox="0 0 210 297" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">'
            '<stop offset="0" stop-color="#1a1240"/><stop offset=".28" stop-color="#3d2278"/><stop offset=".52" stop-color="#7a2f7a"/><stop offset=".76" stop-color="#c4476a"/><stop offset="1" stop-color="#f08a5d"/></linearGradient></defs>'
            '<rect width="210" height="297" fill="url(#sky)"/>' + stars() +
            '<rect x="9" y="9" width="192" height="279" rx="7" fill="none" stroke="#f0cf8a" stroke-width=".8"/>'
            '<rect x="13" y="13" width="184" height="271" rx="5" fill="none" stroke="#d9b47c" stroke-width=".3"/></svg>')

COVER_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+Devanagari:wght@400;600;700&family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=Inter:wght@400;500&display=swap');
@page{size:A4;margin:0}
*{box-sizing:border-box;margin:0}
html,body{width:210mm;height:297mm}
body{position:relative;overflow:hidden;color:#fbf1de;text-align:center;background:#1a1240}
.bg{position:absolute;left:0;top:0;width:210mm;height:297mm}
.in{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;padding:34mm 26mm 30mm}
.kick{font-family:Inter,sans-serif;font-size:11pt;letter-spacing:.42em;text-transform:uppercase;color:#f4cf7a}
.om{font-family:'Noto Serif Devanagari',serif;font-size:20pt;color:#ffe08a;margin-top:10mm;font-weight:600}
h1{font-family:'Noto Serif Devanagari',serif;font-size:56pt;font-weight:700;line-height:1.45;color:#fff8e8;margin-top:8mm}
.roman{font-family:'Cormorant Garamond',serif;font-style:italic;font-weight:600;font-size:34pt;color:#ffe08a;line-height:1.1;margin-top:2mm}
.rule{width:60mm;height:.5mm;margin:9mm 0 7mm;background:#e3bf72}
.src{font-family:'Noto Serif Devanagari',serif;font-size:15pt;color:#ead9bd;line-height:1.6}
.line{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:17pt;color:#f6e9d1;margin-top:5mm}
.lot{position:absolute;left:50%;bottom:26mm;width:150mm;transform:translateX(-50%)}
.foot{position:absolute;left:0;right:0;bottom:21mm;font-family:Inter,sans-serif;font-size:9.5pt;letter-spacing:.28em;text-transform:uppercase;color:#fff3c9}
"""

def cover_html(d):
    src = f'<div class="src">{html.escape(d["sub"])}</div>' if d["sub"] else ""
    return f'''<!doctype html><html lang="sa"><head><meta charset="utf-8"><title>{d["roman"]}</title><style>{COVER_CSS}</style></head><body>
{backdrop()}
<div class="in"><div class="kick">Lakshmi Stuti</div><div class="om">॥ श्रीः ॥</div><h1>{d["deva"]}</h1><div class="roman">{d["roman"]}</div><div class="rule"></div>{src}<div class="line">The Devanāgarī text, for chanting and recitation</div></div>
{lotus()}<div class="foot">lakshmistuti.com</div></body></html>'''

COVER_JS = r"""
const {chromium}=require('playwright');
(async()=>{const [,, inp, out]=process.argv;
const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+inp);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(1500);
await p.pdf({path:out,format:'A4',printBackground:true,margin:{top:'0',bottom:'0',left:'0',right:'0'},pageRanges:'1'});
await b.close();})();
"""

if __name__ == "__main__":
    tmp = os.environ.get("PDF_TMP", "/tmp"); os.makedirs(tmp, exist_ok=True)
    js = os.path.join(tmp, "pdf_render.js"); open(js, "w").write(JS)
    outdir = os.path.join(ROOT, "assets", "downloads"); os.makedirs(outdir, exist_ok=True)
    for d in DOCS:
        h = os.path.join(tmp, d["slug"] + ".html"); open(h, "w", encoding="utf-8").write(doc_html(d))
        o = os.path.join(outdir, d["slug"] + ".pdf")
        body_pdf = os.path.join(tmp, d["slug"] + "_body.pdf")
        subprocess.run(["node", js, h, body_pdf, d["roman"]], check=True)
        ch = os.path.join(tmp, d["slug"] + "_cover.html"); open(ch, "w", encoding="utf-8").write(cover_html(d))
        cjs = os.path.join(tmp, "cover_render.js"); open(cjs, "w").write(COVER_JS)
        cov_pdf = os.path.join(tmp, d["slug"] + "_cover.pdf")
        subprocess.run(["node", cjs, ch, cov_pdf], check=True)
        from pypdf import PdfWriter, PdfReader
        w = PdfWriter()
        for f in (cov_pdf, body_pdf):
            for pg in PdfReader(f).pages: w.add_page(pg)
        w.add_metadata({"/Title": d["roman"] + " (Devanagari text)", "/Author": "lakshmistuti.com", "/Subject": "Plain Devanagari text for chanting"})
        w.write(o)
        print(d["slug"], os.path.getsize(o), len(w.pages), "pages")
