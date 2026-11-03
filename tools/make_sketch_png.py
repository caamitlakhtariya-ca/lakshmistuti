#!/usr/bin/env python3
"""One-page sketch note for a verse -> assets/sketch/<file>.png
Usage: python3 tools/make_sketch_png.py kana 11 [plain|lotus|art:/path/to/lakshmi.png]  (plain = use assets/sketch/lakshmi-art.png if present; lotus = my drawn lotus)
Text comes from the verified verse data in build.py (verse['sheet']), never typed by hand.
"""
import sys, os, html
sys.path.insert(0, os.path.dirname(__file__))
import build as B
from playwright.sync_api import sync_playwright

# series key -> (verse list, display name, url base)
SERIES = {"kana": (B.KVERSES, "Kanakadhāra Stotram", "kanakadhara"),
          "sri": (B.VERSES, "Śrī Sūktam", "sri-suktam"),
          "mla": (B.MVERSES, "Mahālakṣmī Aṣṭakam", "mahalakshmi-ashtakam")}
def esc(x): return html.escape(x, quote=False)

def lotus(art=None):
    if art:
        return f'<img class="art" src="file://{art}" alt="">'
    petals = ""
    for a, r, c in [(-72,1,"#f6b9c8"),(-48,1,"#f4a6ba"),(-24,1,"#f6b9c8"),(0,1,"#f2a0b6"),(24,1,"#f6b9c8"),(48,1,"#f4a6ba"),(72,1,"#f6b9c8")]:
        petals += f'<ellipse cx="200" cy="205" rx="34" ry="104" transform="rotate({a} 200 300)" fill="{c}" stroke="#c8506f" stroke-width="2.4" stroke-linejoin="round"/>'
    inner = "".join(f'<ellipse cx="200" cy="228" rx="26" ry="78" transform="rotate({a} 200 300)" fill="#fbd3dd" stroke="#c8506f" stroke-width="2"/>' for a in (-36,0,36))
    rays = "".join(f'<line x1="200" y1="150" x2="{200+190*__import__("math").sin(__import__("math").radians(a)):.1f}" y2="{150-190*__import__("math").cos(__import__("math").radians(a)):.1f}" stroke="#e5b94a" stroke-width="3" stroke-linecap="round" stroke-dasharray="2 14"/>' for a in range(-70,71,14))
    return f'''<svg class="lotus" viewBox="0 0 400 340"><circle cx="200" cy="140" r="118" fill="#fff3c9" fill-opacity=".8" stroke="#e5b94a" stroke-width="2.5" stroke-dasharray="7 6"/>{rays}
{petals}{inner}<ellipse cx="200" cy="318" rx="118" ry="12" fill="#f4a6ba" fill-opacity=".5"/>
<circle cx="200" cy="205" r="34" fill="#fff3c9" stroke="#c9972b" stroke-width="2.4"/><text x="200" y="217" text-anchor="middle" font-family="Noto Serif Devanagari" font-weight="700" font-size="34" fill="#8a2c3c">श्री</text></svg>'''

def sheet(v, art=None, sname="Kanakadhāra Stotram"):
    d = v["sheet"]; kp = v["keypoints"]; ic = v["icons"]; N = len(kp)
    cols = ["#8e5bb5", "#d04a6c", "#c98a12", "#4f8a3f"]
    tints = ["#efe6f8", "#fbe3ea", "#fcefc9", "#e6f0dc"]
    sal = "".join(f'''<div class="srow"><div class="sname" style="background:{tints[i]};border-color:{cols[i]};color:{cols[i]}"><b>{esc(kp[i][0])}</b><small>({esc(kp[i][1].split(":")[0])})</small></div>
<div class="sico" style="color:{cols[i]}">{B.icon(ic[i],46)}</div><p>{esc(d["salut"][i])}</p></div>''' for i in range(N))
    words = "".join(f'<div class="krow"><span class="kd" lang="sa">{a}</span><span class="ki">{esc(b)}</span><span class="kg">{esc(c)}</span></div>' for a, b, c in d["words"])
    take = "".join(f'<li>{esc(t)}</li>' for t in d["take"])
    centre = B.sketch_note(kp, ic, d.get("centre", "Whole Picture")).replace('viewBox="0 0 640 410"','viewBox="40 36 560 340"')
    return f'''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&family=Patrick+Hand&family=Cormorant+Garamond:ital,wght@0,600;1,500;1,600&family=Noto+Serif+Devanagari:wght@500;700&display=swap">
<style>
*{{box-sizing:border-box;margin:0}}
body{{width:1344px;height:896px;background:radial-gradient(circle at 20% 10%,#fffaf0,#fdf3dc 70%);font-family:"Patrick Hand","Cormorant Garamond",serif;color:#3b2a1e;position:relative;overflow:hidden}}
.g{{position:absolute;inset:18px 22px 34px;display:grid;grid-template-columns:396px minmax(0,1fr) 396px;gap:16px 20px;grid-template-rows:auto 1fr}}
.title{{grid-column:2;grid-row:1;justify-self:center;align-self:start;white-space:nowrap;background:linear-gradient(#fbe7b5,#f6d48a);border:3px solid #b9801c;border-radius:10px 14px 10px 14px;padding:8px 30px;font:700 32px Caveat,cursive;color:#5a2d0c;letter-spacing:.5px;position:relative}}
.panel{{position:relative;border:2.5px solid;border-radius:20px 26px 18px 24px/24px 18px 26px 20px;padding:22px 16px 12px}}
.lab{{position:absolute;top:-17px;left:14px;font:700 26px Caveat,cursive;padding:0 16px;border-radius:999px;border:2px solid;line-height:1.35}}
.col{{display:flex;flex-direction:column;gap:22px;height:100%}}.col>.panel{{flex:1 1 auto;display:flex;flex-direction:column;justify-content:center}}.p-sa,.p-tr{{flex:0 0 auto!important}}.p-fs{{justify-content:space-around!important}}.p-cp{{flex:0 0 auto!important}}
.p-sa{{background:#fff4d6;border-color:#c9972b}}.p-sa .lab{{background:#fbd6df;border-color:#d04a6c;color:#8a2c3c}}
.deva{{font:500 calc(25px*var(--s,1))/1.55 "Noto Serif Devanagari";color:#4a2410;text-align:center}}
.p-tr{{background:#fffaf0;border-color:#cdbb92}}.p-tr .lab{{background:#e3d6f5;border-color:#8e5bb5;color:#4a2a78}}
.iast{{font:italic 500 calc(18px*var(--s,1))/1.45 "Cormorant Garamond";text-align:center}}
.p-me{{background:#fff3c8;border-color:#d9a92b}}.p-me .lab{{background:#fde9a8;border-color:#c98a12;color:#7a4a05}}
.p-me p{{font-size:calc(19.5px*var(--s,1));line-height:1.3}}
.p-kw{{background:#f1ebfa;border-color:#9a78c4}}.p-kw .lab{{background:#d9c8f0;border-color:#8e5bb5;color:#4a2a78}}
.krow{{display:grid;grid-template-columns:78px 62px 1fr;align-items:baseline;padding:4px 0;border-bottom:1.5px dashed #c8b6e2;font-size:calc(18px*var(--s,1))}}
.krow:last-child{{border:0}}.kd{{font:500 calc(21px*var(--s,1)) "Noto Serif Devanagari";color:#8a2c3c}}.ki{{font:italic 600 calc(18px*var(--s,1)) "Cormorant Garamond"}}.kg{{font-size:calc(17px*var(--s,1))}}
.mid{{display:flex;flex-direction:column;align-items:center;justify-content:space-between;gap:14px;height:100%}}
.art{{height:calc(380px*var(--s,1));object-fit:contain}}
.lotus{{width:calc(430px*var(--s,1));height:calc(366px*var(--s,1));margin-top:6px}}
.p-es{{background:#fff3c8;border-color:#d9a92b;width:100%}}.p-es .lab{{background:#fde9a8;border-color:#c98a12;color:#7a4a05;left:50%;transform:translateX(-50%)}}
.p-es p{{font-size:calc(20px*var(--s,1));line-height:1.3;text-align:center}}
.p-lt{{background:#e6f3dc;border-color:#7fb06a;width:100%}}.p-lt .lab{{background:#cfe8bf;border-color:#4f8a3f;color:#2e5a22;left:50%;transform:translateX(-50%)}}
.p-lt ul{{list-style:none;padding:0}}.p-lt li{{font-size:calc(19px*var(--s,1));padding:3px 0 3px 30px;position:relative}}
.p-lt li::before{{content:"✔";position:absolute;left:2px;color:#4f8a3f;font-weight:700}}
.p-fs{{background:#fffaf0;border-color:#cdbb92}}.p-fs .lab{{background:#fbe9a0;border-color:#c98a12;color:#7a4a05}}
.srow{{display:grid;grid-template-columns:128px 50px 1fr;gap:8px;align-items:center;padding:4px 0}}
.sname{{border:2px solid;border-radius:16px 22px 16px 22px;text-align:center;padding:6px 4px;line-height:1.05}}
.sname b{{display:block;font:italic 700 27px "Cormorant Garamond";white-space:nowrap}}.sname small{{font-size:16px;display:block}}
.srow p{{font-size:calc(17.5px*var(--s,1));line-height:1.25}}
.p-cp{{background:#fdeef2;border-color:#e28aa0;flex:1;padding-bottom:6px}}.p-cp .lab{{background:#f8c9d5;border-color:#d04a6c;color:#8a2c3c}}
.p-cp svg.sketch{{width:100%;height:auto;margin:auto 0}}
.sk-a{{font-family:"Cormorant Garamond";font-size:34px;font-weight:700;font-style:italic}}.sk-b{{font-family:"Patrick Hand";font-size:20px;fill:#3b2a1e}}.sk-c{{font-family:Caveat;font-size:25px;font-weight:700;fill:#3a2208}}
.foot{{position:absolute;bottom:8px;left:0;right:0;text-align:center;font:600 15px Caveat;color:#8a7a62}}
</style></head><body><div class="g">
<div class="col" style="grid-column:1;grid-row:1/3">
 <div class="panel p-sa"><span class="lab">Sanskrit</span><p class="deva" lang="sa">{v["deva"]}</p></div>
 <div class="panel p-tr"><span class="lab">Transliteration</span><p class="iast">{v["iast"]}</p></div>
 <div class="panel p-me"><span class="lab">Meaning (in short)</span><p>{esc(d["short"])}</p></div>
 <div class="panel p-kw"><span class="lab">Key Words</span>{words}</div>
</div>
<div class="title" style="font-size:{30 if len(sname)+len(B.lab(v))<34 else 25}px">{esc(sname)} – {esc(B.lab(v))}</div>
<div class="col" style="grid-column:3;grid-row:1/3"><div class="panel p-fs"><span class="lab">{esc(d.get("salut_title","Key Ideas"))}</span>{sal}</div>
 <div class="panel p-cp"><span class="lab">{esc(d.get("centre_title","The Whole Picture"))}</span>{centre}</div></div>
<div class="mid" style="grid-column:2;grid-row:2">{lotus(art)}
 <div class="panel p-es"><span class="lab">The Essence</span><p>{esc(d["essence"])}</p></div>
 <div class="panel p-lt"><span class="lab">Life Takeaway</span><ul>{take}</ul></div></div>
</div><script>
document.fonts.ready.then(()=>{{
 document.querySelectorAll('.sname').forEach(n=>{{const b=n.querySelector('b');b.style.display='inline-block';let f=27;while(b.getBoundingClientRect().width>n.clientWidth-14&&f>13){{f-=1;b.style.fontSize=f+'px'}}b.style.display='block'}});
 document.querySelectorAll('.col,.mid').forEach(c=>{{let k=1;const over=()=>c.scrollHeight>c.clientHeight+1||[...c.children].some(x=>x.scrollWidth>x.clientWidth+1);while(over()&&k>0.5){{k-=0.03;c.style.setProperty('--s',k.toFixed(2))}}}});
 document.body.dataset.fit='done';
}});
</script><div class="foot">lakshmistuti.com  ·  Amit N. Lakhtariya</div></body></html>'''

def render(series, n, mode="plain", out=None, pw=None):
    lst, sname, base = SERIES[series]
    v = next(x for x in lst if x["n"] == n)
    default_art = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets", "sketch", "lakshmi-art.png"))
    art = mode[4:] if mode.startswith("art:") else (default_art if mode == "plain" and os.path.exists(default_art) else None)
    sketchfile = v.get("sketchfile") or f"{base}-{v['slug']}-sketch-note.png"
    out = out or os.path.join(os.path.dirname(__file__), "..", "assets", "sketch", sketchfile)
    tmp = os.path.join(os.path.dirname(os.path.abspath(out)), f"_sheet_{series}{n}.html")
    open(tmp, "w").write(sheet(v, art, sname))
    pg = pw.new_page(viewport={"width": 1344, "height": 896}, device_scale_factor=2)
    pg.goto("file://" + os.path.abspath(tmp)); pg.wait_for_selector("body[data-fit=done]", timeout=20000); pg.wait_for_timeout(600)
    pg.screenshot(path=out); pg.close()
    from PIL import Image
    im = Image.open(out).convert("RGB")
    im.resize((1344, 896), Image.LANCZOS).save(out.replace(".png", "-1344.webp"), quality=88, method=6)
    im.quantize(colors=128, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.FLOYDSTEINBERG).save(out, optimize=True)
    os.remove(tmp)
    return out

if __name__ == "__main__":
    # usage: make_sketch_png.py <series> <n|all> [plain|lotus|art:/path]
    series, which = sys.argv[1], sys.argv[2]; mode = sys.argv[3] if len(sys.argv) > 3 else "plain"
    ns = [x["n"] for x in SERIES[series][0] if x.get("sheet")] if which == "all" else [int(which)]
    with sync_playwright() as p:
        b = p.chromium.launch()
        for n in ns: print(render(series, n, mode, pw=b))
        b.close()
