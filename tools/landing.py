# Landing-page components (home + the two hymn hubs): scroll-driven lotus, hymn tabs, verse paths.
# Imported by build.py. Pure functions that return HTML strings.
import random

def _petal(scale):
    s = scale
    return (f"M0,0 C{-44*s:.1f},{-50*s:.1f} {-38*s:.1f},{-128*s:.1f} 0,{-176*s:.1f} "
            f"C{38*s:.1f},{-128*s:.1f} {44*s:.1f},{-50*s:.1f} 0,0Z")

def lotus_svg():
    rings = [
        ("r1", "g1", 1.0, list(range(-120, 121, 30))),
        ("r2", "g2", 0.80, [-105, -75, -45, -15, 15, 45, 75, 105]),
        ("r3", "g3", 0.58, [-60, -30, 0, 30, 60]),
    ]
    g = []
    for cls, grad, sc, angles in rings:
        d = _petal(sc)
        ps = "".join(f'<g class="pt" style="--a:{a}deg"><path d="{d}" fill="url(#{grad})"/></g>' for a in angles)
        g.append(f'<g class="ring {cls}">{ps}</g>')
    return ('<svg class="lotus" viewBox="-200 -200 400 400" aria-hidden="true" focusable="false">'
            '<defs>'
            '<linearGradient id="g1" x1="0" y1="0" x2="0" y2="-1"><stop offset="0" stop-color="#8f1d63"/><stop offset=".55" stop-color="#e0366b"/><stop offset="1" stop-color="#ff9ab4"/></linearGradient>'
            '<linearGradient id="g2" x1="0" y1="0" x2="0" y2="-1"><stop offset="0" stop-color="#d9435e"/><stop offset=".6" stop-color="#ff8a3d"/><stop offset="1" stop-color="#ffd27a"/></linearGradient>'
            '<linearGradient id="g3" x1="0" y1="0" x2="0" y2="-1"><stop offset="0" stop-color="#ffa63d"/><stop offset=".6" stop-color="#ffd35c"/><stop offset="1" stop-color="#fff3c4"/></linearGradient>'
            '<radialGradient id="gc"><stop offset="0" stop-color="#fff6d6"/><stop offset=".6" stop-color="#f6c34a"/><stop offset="1" stop-color="#c98a12"/></radialGradient>'
            '</defs>'
            + "".join(g) +
            '<circle class="core" r="26" fill="url(#gc)"/>'
            '<text class="coret" y="9" text-anchor="middle" lang="sa">श्री</text></svg>')

def sparkles(n=26, seed=7):
    r = random.Random(seed)
    out = []
    for i in range(n):
        x = r.uniform(2, 98); y = r.uniform(4, 88); s = r.choice([2, 2, 3, 3, 4, 5]); d = r.uniform(0, 6); t = r.uniform(3.2, 7)
        out.append(f'<i style="left:{x:.1f}%;top:{y:.1f}%;--s:{s}px;--dl:{d:.1f}s;--du:{t:.1f}s"></i>')
    return '<div class="spk" aria-hidden="true">' + "".join(out) + "</div>"

def first_line(v):
    return v["deva"].split("<br>")[0]

def chips(lst, base):
    return "".join(f'<a class="cn k{(i)%4}" href="/{base}/{v["slug"]}/" title="{v.get("label") or "Verse "+str(v["n"])}">{v["n"]}</a>' for i, v in enumerate(lst))

def hymn_tabs(sri, kana, kana_total, sri_total, kappx):
    s1, k1 = first_line(sri[0]), first_line(kana[0])
    sri_n, kana_n = len(sri), len(kana)
    sri_panel = f'''<div class="tp" role="tabpanel" id="tp-sri" aria-labelledby="tb-sri">
<div class="tp-art k-sri"><p class="tp-k">Vedic hymn · {sri_n} verses</p><p class="tp-d" lang="sa">{s1}</p><p class="tp-s">Verse 1 · the invitation</p></div>
<div class="tp-body"><h3>Śrī Sūktam</h3>
<p>The Vedic hymn that calls Goddess Lakshmi (Śrī) into the home and the heart: her golden radiance, her steady presence, and the fruit of reciting it. Each of the {sri_n} verses has the Sanskrit text, a word-by-word meaning, deeper insights and a short practice.</p>
<p class="tp-cta"><a class="btn" href="/sri-suktam/verse-1/">Start with Verse 1</a><a class="btn ghost" href="/sri-suktam/">All {sri_n} verses</a></p>
<div class="cns" aria-label="Śrī Sūktam verses">{chips(sri, "sri-suktam")}</div></div></div>'''
    kana_panel = f'''<div class="tp" role="tabpanel" id="tp-kana" aria-labelledby="tb-kana">
<div class="tp-art k-kana"><p class="tp-k">Śrī Śaṅkarācārya · {kana_n} verses</p><p class="tp-d" lang="sa">{k1}</p><p class="tp-s">Verse 1 · a glance of grace</p></div>
<div class="tp-body"><h3>Kanakadhāra Stotram</h3>
<p>Śrī Śaṅkarācārya’s hymn of the “stream of gold”, born from the story of a poor woman’s single gooseberry. Read verse by verse, from the first glance of grace to the closing benediction, with a meditation and a reflection for each.</p>
<p class="tp-cta"><a class="btn" href="/kanakadhara/verse-1/">Start with Verse 1</a><a class="btn ghost" href="/kanakadhara/">All {kana_n} verses</a></p>
<div class="cns" aria-label="Kanakadhāra Stotram verses">{chips(kana, "kanakadhara")}</div></div></div>'''
    return f'''<section class="hymns" id="hymns"><div class="hy-in">
<p class="kick rv">Two hymns, one Mother</p>
<h2 class="rv">Choose your hymn</h2>
<div class="tabs" role="tablist" aria-label="Choose a hymn">
<button type="button" role="tab" class="tb on" id="tb-sri" aria-controls="tp-sri" aria-selected="true"><span class="tb-t">Śrī Sūktam</span><span class="tb-s">Vedic · {sri_n} verses</span></button>
<button type="button" role="tab" class="tb" id="tb-kana" aria-controls="tp-kana" aria-selected="false" tabindex="-1"><span class="tb-t">Kanakadhāra Stotram</span><span class="tb-s">Śaṅkarācārya · {kana_n} verses</span></button>
</div>
<div class="tpanels rv">{sri_panel}{kana_panel}</div>
</div></section>'''

def verse_card(v, base, i, sub):
    lab = v.get("label") or f"Verse {v['n']}"
    return (f'<a class="vc k{i%4} rv" style="--d:{(i%2)*0.08:.2f}s" href="/{base}/{v["slug"]}/"><span class="vc-n">{v["n"]}</span>'
            f'<span class="vc-t"><b>{lab}</b><small>{sub}</small></span></a>')

def hub_hero(kick, h1, lede, byline, ctas, stat):
    return f'''<header class="hh"><div class="hh-sky">{sparkles(18, 11)}<span class="hh-shri" lang="sa" aria-hidden="true">श्री</span></div>
<div class="hh-in"><p class="hh-k">{kick}</p><h1>{h1}</h1><p class="hh-l">{lede}</p>{byline}<p class="hh-c">{ctas}</p>
<p class="hh-stat">{stat}</p></div></header>'''

def rain(n=20, seed=4):
    r = random.Random(seed)
    out = []
    for i in range(n):
        x = r.uniform(2, 98); s = r.choice([6, 8, 9, 11]); d = r.uniform(0, 7); t = r.uniform(5, 9)
        out.append(f'<i style="left:{x:.1f}%;--s:{s}px;--dl:{d:.1f}s;--du:{t:.1f}s"></i>')
    return "".join(out)
