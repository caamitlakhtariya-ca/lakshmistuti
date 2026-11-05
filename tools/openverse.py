# Verse-page "openness": a wide dawn scene (open sky, cool mountains, deep ocean) behind the hero. Returns an HTML string.
import random

def stars(n=34, seed=11):
    r = random.Random(seed); out = []
    for _ in range(n):
        out.append(f'<i style="left:{r.uniform(1,99):.1f}%;top:{r.uniform(3,52):.1f}%;--s:{r.choice([2,2,3,3,4])}px;--dl:{r.uniform(0,6):.1f}s;--du:{r.uniform(3,7):.1f}s"></i>')
    return '<div class="spk vstars" aria-hidden="true">' + "".join(out) + '</div>'

def scene():
    far = "M0,330 L90,262 L150,300 L250,215 L330,285 L420,240 L520,310 L640,225 L730,300 L840,250 L940,320 L1060,235 L1160,300 L1270,255 L1360,305 L1440,270 L1440,420 L0,420Z"
    mid = "M0,360 L110,300 L200,340 L310,268 L400,330 L500,290 L610,345 L720,280 L830,338 L930,300 L1050,350 L1170,292 L1290,340 L1440,305 L1440,430 L0,430Z"
    near = "M0,392 L130,345 L240,380 L360,332 L470,378 L600,350 L720,392 L860,346 L980,384 L1100,352 L1230,390 L1340,360 L1440,386 L1440,450 L0,450Z"
    snow = "M640,225 L612,262 L632,254 L650,270 L668,252 L690,262Z M250,215 L226,248 L244,242 L258,256 L274,240 L292,248Z M1060,235 L1038,266 L1054,260 L1068,274 L1082,258 L1100,266Z"
    wave = "M0,12 Q90,0 180,12 T360,12 T540,12 T720,12 T900,12 T1080,12 T1260,12 T1440,12 T1620,12 T1800,12 T1980,12 T2160,12 T2340,12 T2520,12 T2700,12 T2880,12 L2880,60 L0,60Z"
    return ('<div class="vscene" aria-hidden="true">' + stars() +
        '<svg class="vsvg" viewBox="0 0 1440 470" preserveAspectRatio="xMidYMax slice" focusable="false">'
        '<defs>'
        '<radialGradient id="vsun" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#fff3c4"/><stop offset=".35" stop-color="#ffc766" stop-opacity=".85"/><stop offset="1" stop-color="#ff9a4d" stop-opacity="0"/></radialGradient>'
        '<linearGradient id="vsea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1a7f8e"/><stop offset=".5" stop-color="#0d5a73"/><stop offset="1" stop-color="#082f4d"/></linearGradient>'
        '<linearGradient id="vm1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8d7fd0"/><stop offset="1" stop-color="#5d5bb0"/></linearGradient>'
        '<linearGradient id="vm2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4a6fb8"/><stop offset="1" stop-color="#2f5a9a"/></linearGradient>'
        '<linearGradient id="vm3" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1f6f8c"/><stop offset="1" stop-color="#0f4a68"/></linearGradient>'
        '</defs>'
        '<circle class="vglow" cx="1010" cy="330" r="170" fill="url(#vsun)"/>'
        '<g class="ly l1"><path d="' + far + '" fill="url(#vm1)" opacity=".75"/><path d="' + snow + '" fill="#fff" opacity=".6"/></g>'
        '<g class="ly l2"><path d="' + mid + '" fill="url(#vm2)" opacity=".92"/></g>'
        '<g class="ly l3"><path d="' + near + '" fill="url(#vm3)"/></g>'
        '<rect x="0" y="410" width="1440" height="70" fill="url(#vsea)"/>'
        '<g class="vwv w1"><path transform="translate(0,398)" d="' + wave + '" fill="#127a8c" opacity=".55"/></g>'
        '<g class="vwv w2"><path transform="translate(0,420)" d="' + wave + '" fill="#0c5f7c" opacity=".7"/></g>'
        '<g class="vwv w3"><path transform="translate(0,442)" d="' + wave + '" fill="#09405f" opacity=".85"/></g>'
        '<path d="M960,432 H1060 M975,442 H1045 M990,452 H1030" stroke="#ffe39a" stroke-width="2" stroke-linecap="round" opacity=".6" class="vshim"/>'
        '</svg></div>')
