#!/usr/bin/env python3
"""Static site generator for lakshmistuti.com
Run:  python3 tools/build.py      (from the repo root)
Add a verse by appending to VERSES below, then rebuild.
"""
import os, json, html
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://lakshmistuti.com"
NAME = "Lakshmi Stuti"
AUTHOR = "Amit N. Lakhtariya"
TODAY = "2026-10-11"
GA_ID = ""          # e.g. "G-XXXXXXXXXX"  -> switches Google Analytics on
ADSENSE_CLIENT = "" # e.g. "ca-pub-1234567890123456" -> switches AdSense on after approval
CONTACT_EMAIL = "contact@lakshmistuti.com"  # placeholder: replace with the address you want to show publicly
E = html.escape

# ---------------------------------------------------------------- content
VERSES = [
 dict(
  n=1, slug="verse-1",
  deva="हिरण्यवर्णां हरिणीं सुवर्णरजतस्रजाम्।<br>चन्द्रां हिरण्मयीं लक्ष्मीं जातवेदो म आवह॥",
  iast="Hiraṇyavarṇāṁ hariṇīṁ suvarṇa-rajata-srajām,<br>Chandrāṁ hiraṇmayīṁ Lakṣmīṁ jāta-vedo ma āvaha.",
  title="Śrī Sūktam Verse 1 Meaning – Hiraṇyavarṇāṁ Hariṇīṁ Explained",
  desc="Śrī Sūktam Verse 1 (Hiraṇyavarṇāṁ Hariṇīṁ) with Devanāgarī, transliteration, word-by-word meaning, deeper insights and a short Lakshmi meditation.",
  h1="Śrī Sūktam – Verse 1",
  sub="Hiraṇyavarṇāṁ Hariṇīṁ – the invitation to Goddess Lakshmi",
  words=[
   ("हिरण्यवर्णां","Hiraṇyavarṇāṁ","Golden-colored one","The golden glow stands for spiritual illumination, purity and auspiciousness."),
   ("हरिणीं","Hariṇīṁ","Resembling a deer","Gentle and graceful: it points to gentleness, beauty, purity and swiftness."),
   ("सुवर्णरजतस्रजाम्","Suvarṇa-rajata-srajām","Wearing garlands (adornments) of gold and silver","<em>Suvarṇa</em> = gold, <em>rajata</em> = silver, <em>srajām</em> = garlanded or adorned. It speaks of richness, prosperity, brilliance, divine radiance and cosmic abundance."),
   ("चन्द्रां","Chandrāṁ","Radiant like the moon","Coolness, soothing grace, serenity, beauty and balanced emotions."),
   ("हिरण्मयीं लक्ष्मीं","Hiraṇmayīṁ Lakṣmīṁ","The golden form of Goddess Lakshmi","Divine abundance, prosperity and spiritual richness."),
   ("जातवेदो म आवह","Jātavedo ma āvaha","O Jātaveda (Fire, Agni), please invite or bring her to me","<em>Jātaveda</em> means “one who knows all births”. Agni is the mediator who carries our prayers to the Divine."),
  ],
  meaning="O Jātaveda (sacred fire, knower of all births), I humbly request you to invite into my life the golden-hued, graceful, gentle Goddess Lakshmi, who is adorned with garlands of gold and silver, who radiates serenity like the soft glow of the moon. May she gracefully enter my life, bestowing purity, peace, prosperity and spiritual harmony.",
  insights=[
   ("Gentleness (Hariṇīṁ)","True abundance and fulfilment are drawn not through harsh pursuit but through gentleness, grace and purity of heart."),
   ("The gold and silver garland","Balanced material and spiritual prosperity: gold stands for worldly success, silver for emotional and spiritual wisdom."),
   ("Moon-like radiance (Chandrāṁ)","Real prosperity is serene, calm and balanced. It cools the mind, relieves stress and brings peace."),
   ("The role of Agni (Jātaveda)","You are not alone on the journey. You ask the divine forces, with Agni as messenger, to guide you and connect you with universal abundance."),
  ],
  meditation=["After chanting, visualise Goddess Lakshmi vividly.",
              "Imagine her radiant form, golden like sunrise, her eyes full of compassionate gentleness, like those of a deer.",
              "Feel the serenity of moonlight radiating from her presence into your heart.",
              "Allow the image to settle gently, gradually replacing anxieties or fears with calmness and confidence."],
  reflection="Through the day, quietly remind yourself of gentleness, grace, clarity and balance, the qualities symbolised by Lakshmi. Notice how these qualities subtly influence your interactions, choices and responses.",
  closing="This first verse isn’t merely a chant. It is an invitation to the Divine, an invitation to nurture a gentle yet radiant heart that attracts true prosperity effortlessly.",
 ),
]
TOTAL_SRI = 16  # verses planned in the Śrī Sūktam (core Rigvedic Khila text)

GLOSSARY = [
 ("हिरण्यवर्णा","Hiraṇyavarṇā","Golden-colored; the golden hue of Lakshmi.","sri-suktam/verse-1/"),
 ("हरिणी","Hariṇī","Deer-like; gentle and graceful.","sri-suktam/verse-1/"),
 ("सुवर्ण","Suvarṇa","Gold.","sri-suktam/verse-1/"),
 ("रजत","Rajata","Silver.","sri-suktam/verse-1/"),
 ("स्रज्","Sraj","Garland; adornment.","sri-suktam/verse-1/"),
 ("चन्द्रा","Chandrā","Moon-like; radiant and cooling.","sri-suktam/verse-1/"),
 ("हिरण्मयी","Hiraṇmayī","Made of gold; golden.","sri-suktam/verse-1/"),
 ("लक्ष्मी","Lakṣmī (Lakshmi, Laxmi)","Goddess of prosperity, grace and auspiciousness.","sri-suktam/verse-1/"),
 ("जातवेदस्","Jātavedas","Agni, the sacred fire; “one who knows all births”.","sri-suktam/verse-1/"),
 ("आवह","Āvaha","Invite, bring forth.","sri-suktam/verse-1/"),
]

# ---------------------------------------------------------------- templates
def head(title, desc, path, extra_ld=None, og_type="website"):
    url = SITE + "/" + path
    ld = []
    if extra_ld: ld.append(extra_ld)
    ga = ""
    if GA_ID:
        ga = ('<script async src="https://www.googletagmanager.com/gtag/js?id=%s"></script>'
              '<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}gtag("js",new Date());gtag("config","%s");</script>' % (GA_ID, GA_ID))
    ads = ""
    if ADSENSE_CLIENT:
        ads = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=%s" crossorigin="anonymous"></script>' % ADSENSE_CLIENT
    ldh = "".join('<script type="application/ld+json">%s</script>' % json.dumps(x, ensure_ascii=False) for x in ld)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{url}">
<meta name="author" content="{AUTHOR}">
<meta name="theme-color" content="#7a1f2b">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/og.svg">
<meta name="twitter:card" content="summary">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/style.css">
{ldh}{ga}{ads}
</head>'''

def nav(cur):
    items = [("Home","", "home"),("Śrī Sūktam","sri-suktam/","sri"),("Kanakadhāra","kanakadhara/","kana"),("Glossary","glossary/","gl"),("About","about/","about")]
    out = "".join('<a href="/%s"%s>%s</a>' % (p, ' aria-current="page"' if k==cur else "", l) for l,p,k in items)
    return f'''<body>
<header class="site"><div class="wrap">
<a class="brand" href="/">श्री लक्ष्मी स्तुति<small>LAKSHMI STUTI · A COMMENTARY</small></a>
<nav class="main" aria-label="Main">{out}</nav>
</div></header>'''

def foot():
    return f'''
<footer class="site"><div class="wrap">
<p><a href="/about/">About</a><a href="/contact/">Contact</a><a href="/privacy/">Privacy Policy</a></p>
<p>© 2026 {AUTHOR}. Commentary prepared with AI assistance and reviewed by the author.</p>
</div></footer>
</body></html>'''

def ad(slot):
    # Empty until AdSense is approved. Hidden when empty (see .ad-slot:empty in CSS).
    if not ADSENSE_CLIENT: return '<div class="ad-slot" data-slot="%s"></div>' % slot
    return ('<div class="ad-slot"><ins class="adsbygoogle" style="display:block" data-ad-client="%s" data-ad-slot="REPLACE_%s" data-ad-format="auto" data-full-width-responsive="true"></ins>'
            '<script>(adsbygoogle=window.adsbygoogle||[]).push({});</script></div>') % (ADSENSE_CLIENT, slot.upper())

def crumbs(parts):
    s = ['<a href="/">Home</a>'] + [('<a href="/%s">%s</a>' % (p,l)) if p else E(l) for l,p in parts]
    return '<p class="crumbs" aria-label="Breadcrumb">' + " › ".join(s) + "</p>"

def bc_ld(parts):
    items = [("Home", SITE + "/")] + [(l, SITE + "/" + p if p else None) for l,p in parts]
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":i+1,"name":l, **({"item":u} if u else {})} for i,(l,u) in enumerate(items)]}

PAGES = []  # (path, priority)
def write(path, content, prio="0.6"):
    d = os.path.join(ROOT, path)
    os.makedirs(d, exist_ok=True) if path else None
    with open(os.path.join(d, "index.html") if path else os.path.join(ROOT,"index.html"), "w", encoding="utf-8") as f:
        f.write(content)
    PAGES.append((path, prio))

# ---------------------------------------------------------------- pages
def page_home():
    v = VERSES[0]
    t = "Lakshmi Stuti – Śrī Sūktam & Kanakadhāra Stotram Meaning in English"
    d = "Verse-by-verse English commentary on the Śrī Sūktam and Kanakadhāra Stotram to Goddess Lakshmi (Laxmi): Devanāgarī, transliteration, word meanings and practice."
    ld = {"@context":"https://schema.org","@type":"WebSite","name":NAME,"url":SITE+"/","inGroup":None,"author":{"@type":"Person","name":AUTHOR},"inLanguage":"en"}
    ld.pop("inGroup")
    body = head(t,d,"",ld) + nav("home") + f'''
<main class="wrap">
<section class="hero">
<p class="deva">श्री लक्ष्मी स्तुति</p>
<h1>Śrī Sūktam &amp; Kanakadhāra Stotram, understood gently</h1>
<p class="lede">A slow, verse-by-verse commentary on the hymns to Goddess Lakshmi (also written Laxmi): the original text, simple word meanings, and a short practice for each verse.</p>
<p><a class="btn" href="/sri-suktam/verse-1/">Start with Verse 1</a><a class="btn ghost" href="/sri-suktam/">Śrī Sūktam index</a></p>
</section>
<div class="grid">
<a class="tile" href="/sri-suktam/"><h3>Śrī Sūktam</h3><p>The Vedic hymn to Lakshmi. Verse 1 is live; more verses are added one at a time.</p></a>
<a class="tile" href="/kanakadhara/"><h3>Kanakadhāra Stotram <span class="soon">coming soon</span></h3><p>Śrī Śaṅkarācārya’s hymn to Lakshmi, to follow the Śrī Sūktam.</p></a>
<a class="tile" href="/glossary/"><h3>Glossary</h3><p>Sanskrit words used across the commentary, with simple meanings.</p></a>
</div>
<h2>Today’s verse</h2>
<div class="verse"><p class="label">Śrī Sūktam · Verse 1</p><p class="deva">{v["deva"]}</p><p class="iast">{v["iast"]}</p></div>
<p>{E(v["closing"])} <a href="/sri-suktam/verse-1/">Read the full commentary →</a></p>
{ad("home")}
</main>''' + foot()
    write("", body, "1.0")

def page_sri():
    t = "Śrī Sūktam Meaning in English – Verse by Verse Commentary"
    d = "Verse-by-verse English meaning of the Śrī Sūktam, the Vedic hymn to Goddess Lakshmi, with Devanāgarī, transliteration and word-by-word explanation."
    parts = [("Śrī Sūktam","sri-suktam/")]
    rows = ""
    for v in VERSES:
        rows += f'<a class="tile" href="/sri-suktam/{v["slug"]}/"><h3>Verse {v["n"]}</h3><p>{E(v["sub"])}</p></a>'
    for n in range(len(VERSES)+1, TOTAL_SRI+1):
        rows += f'<div class="tile" style="opacity:.55"><h3>Verse {n} <span class="soon">coming soon</span></h3></div>'
    body = head(t,d,"sri-suktam/",bc_ld(parts)) + nav("sri") + f'''
<main class="wrap">{crumbs([("Śrī Sūktam",None)])}
<h1>Śrī Sūktam – verse by verse</h1>
<p class="lede">The Śrī Sūktam is a Vedic hymn praising Goddess Lakshmi (Śrī) as the source of prosperity, grace and auspiciousness. Each verse here has the Sanskrit text, a word-by-word meaning, deeper insights and a short practice.</p>
<p>Verses are published one at a time, so that each can be read and absorbed slowly before the next appears.</p>
<div class="grid">{rows}</div>
{ad("index")}
</main>''' + foot()
    write("sri-suktam", body, "0.9")

def page_kana():
    t = "Kanakadhāra Stotram Meaning in English – Commentary (Coming Soon)"
    d = "Commentary on the Kanakadhāra Stotram, Śrī Śaṅkarācārya’s hymn to Goddess Lakshmi. Verse-by-verse meaning is coming soon."
    parts = [("Kanakadhāra Stotram","kanakadhara/")]
    body = head(t,d,"kanakadhara/",bc_ld(parts)) + nav("kana") + f'''
<main class="wrap">{crumbs([("Kanakadhāra Stotram",None)])}
<h1>Kanakadhāra Stotram</h1>
<p class="lede">The Kanakadhāra Stotram is the hymn traditionally attributed to Śrī Śaṅkarācārya, composed in praise of Goddess Lakshmi.</p>
<p>The verse-by-verse commentary will begin after the Śrī Sūktam series is well under way. Meanwhile, you can begin with the <a href="/sri-suktam/">Śrī Sūktam</a>.</p>
</main>''' + foot()
    write("kanakadhara", body, "0.5")

def page_verse(i):
    v = VERSES[i]
    prev = VERSES[i-1] if i>0 else None
    nxt = VERSES[i+1] if i+1 < len(VERSES) else None
    path = f'sri-suktam/{v["slug"]}'
    parts = [("Śrī Sūktam","sri-suktam/"),(f'Verse {v["n"]}',None)]
    art = {"@context":"https://schema.org","@type":"Article","headline":v["title"],"description":v["desc"],
           "author":{"@type":"Person","name":AUTHOR},"datePublished":TODAY,"dateModified":TODAY,"inLanguage":"en",
           "mainEntityOfPage":SITE+"/"+path+"/","publisher":{"@type":"Person","name":AUTHOR}}
    words = "".join(f'<div class="word"><div class="w">{a}<i>{E(b)}</i></div><p class="m">{E(c)}</p><p>{d}</p></div>' for a,b,c,d in v["words"])
    ins = "".join(f'<div class="card"><h3>{E(a)}</h3><p>{E(b)}</p></div>' for a,b in v["insights"])
    med = "".join(f"<li>{E(x)}</li>" for x in v["meditation"])
    p = f'<a href="/sri-suktam/{prev["slug"]}/">← Verse {prev["n"]}</a>' if prev else '<span class="off">← Previous</span>'
    n = f'<a href="/sri-suktam/{nxt["slug"]}/">Verse {nxt["n"]} →</a>' if nxt else '<span class="off">Verse 2 coming soon →</span>'
    body = head(v["title"],v["desc"],path+"/",art,"article") + f'<script type="application/ld+json">{json.dumps(bc_ld(parts),ensure_ascii=False)}</script>' + nav("sri") + f'''
<main class="wrap"><article>
{crumbs([("Śrī Sūktam","sri-suktam/"),(f"Verse {v['n']}",None)])}
<h1>{v["h1"]}</h1>
<p class="lede">{E(v["sub"])}</p>
<p class="crumbs">By {AUTHOR}</p>
<div class="verse"><p class="label">Devanāgarī</p><p class="deva" lang="sa">{v["deva"]}</p><p class="iast" lang="sa-Latn">{v["iast"]}</p></div>
{ad("below-verse")}
<nav class="toc" aria-label="On this page"><a href="#words">Word by word</a><a href="#meaning">Meaning</a><a href="#insights">Deeper insights</a><a href="#meditation">Meditation</a><a href="#reflection">Reflection</a></nav>
<h2 id="words">Word-by-word meaning</h2>
{words}
<h2 id="meaning">Full meaning</h2>
<blockquote><p>{E(v["meaning"])}</p></blockquote>
<h2 id="insights">Deeper spiritual insights</h2>
{ins}
<h2 id="meditation">Practical meditation</h2>
<ol>{med}</ol>
<h2 id="reflection">Reflection for today</h2>
<p>{E(v["reflection"])}</p>
<p><em>{E(v["closing"])} May your journey today become meaningful, peaceful and enriching.</em></p>
<p class="crumbs">Terms used here are explained in the <a href="/glossary/">glossary</a>. This commentary was prepared with AI assistance; <a href="/about/">read more</a>.</p>
{ad("end")}
<div class="pager">{p}{n}</div>
</article></main>''' + foot()
    write(path, body, "0.9")

def page_gl():
    t = "Glossary of Sanskrit Terms – Śrī Sūktam & Lakshmi Stotras"
    d = "Simple meanings of Sanskrit words used in the Śrī Sūktam and Kanakadhāra Stotram commentary: Hiraṇya, Hariṇī, Lakshmi, Jātavedas and more."
    parts = [("Glossary","glossary/")]
    dl = "".join(f'<dt>{a} <span style="font-family:var(--serif);font-weight:400;color:var(--muted)">· {E(b)}</span></dt><dd>{E(c)} <a href="/{u}">See verse →</a></dd>' for a,b,c,u in GLOSSARY)
    body = head(t,d,"glossary/",bc_ld(parts)) + nav("gl") + f'''
<main class="wrap">{crumbs([("Glossary",None)])}
<h1>Glossary</h1>
<p class="lede">Sanskrit words met in the commentary. New entries are added with every verse.</p>
<dl class="gl">{dl}</dl>
</main>''' + foot()
    write("glossary", body, "0.6")

def page_about():
    t = f"About – {NAME} by {AUTHOR}"
    d = "About this commentary on the Śrī Sūktam and Kanakadhāra Stotram by Amit N. Lakhtariya, and how AI assistance is used in preparing it."
    parts = [("About","about/")]
    ld = {"@context":"https://schema.org","@type":"AboutPage","name":"About","url":SITE+"/about/","author":{"@type":"Person","name":AUTHOR}}
    body = head(t,d,"about/",ld) + nav("about") + f'''
<main class="wrap">{crumbs([("About",None)])}
<h1>About this site</h1>
<p>This site is a slow, verse-by-verse reading of the Śrī Sūktam and the Kanakadhāra Stotram, the well-loved hymns to Goddess Lakshmi. It began on the first day of Sharad Navratri, 2026, as a personal study and is shared here for anyone who wants to understand what they are chanting.</p>
<h2>About the author</h2>
<p><strong>{AUTHOR}</strong> is a Chartered Accountant based in Ahmedabad, India, and a lifelong student of the devotional tradition. The commentary reflects his own reading and reflections on each verse.</p>
<h2>AI assistance</h2>
<p>This commentary is prepared collaboratively with an AI assistant (Claude, by Anthropic). The AI helps with drafting, structuring and cross-checking the word-by-word explanations. The author directs the interpretation, reviews every verse and decides what is published. Because AI can make mistakes, and because Sanskrit admits more than one reading, this is a study aid and not a substitute for a teacher or the traditional commentaries. Corrections are welcome through the <a href="/contact/">contact page</a>.</p>
<h2>How the content is organised</h2>
<p>Every verse page has the Devanāgarī text, a transliteration, a word-by-word meaning, the full meaning, deeper insights, a short meditation and a reflection for the day. Verses are released one at a time.</p>
<h2>Spellings</h2>
<p>The Goddess’s name is written <em>Lakshmi</em> (Sanskrit <em>Lakṣmī</em>), and is also commonly spelled <em>Laxmi</em>. Both refer to the same Goddess.</p>
</main>''' + foot()
    write("about", body, "0.5")

def page_contact():
    t = f"Contact – {NAME}"
    d = "Contact the author of the Lakshmi Stuti commentary for corrections, suggestions or questions."
    body = head(t,d,"contact/") + nav("") + f'''
<main class="wrap">{crumbs([("Contact",None)])}
<h1>Contact</h1>
<p>Corrections, suggestions and questions about the commentary are welcome.</p>
<p>Email: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></p>
<p>Please mention the verse number so that it can be checked quickly.</p>
</main>''' + foot()
    write("contact", body, "0.3")

def page_privacy():
    t = f"Privacy Policy – {NAME}"
    d = "Privacy policy for lakshmistuti.com: what data is collected, cookies, analytics and advertising."
    body = head(t,d,"privacy/") + nav("") + f'''
<main class="wrap">{crumbs([("Privacy Policy",None)])}
<h1>Privacy Policy</h1>
<p><em>Last updated: 11 October 2026</em></p>
<p>This website (lakshmistuti.com) is operated by {AUTHOR}. It is a reading site and does not ask visitors to create accounts or submit personal information.</p>
<h2>Information collected</h2>
<p>When you visit, standard technical information (such as your IP address, browser type and the pages viewed) may be recorded by the hosting provider and by analytics tools. If you email the author, your email address and message are used only to reply.</p>
<h2>Analytics</h2>
<p>The site may use Google Analytics to understand which pages are read, so the content can be improved. Google Analytics uses cookies and collects data in aggregate.</p>
<h2>Advertising</h2>
<p>The site may in future display advertisements, including Google AdSense. Third-party vendors, including Google, may use cookies to serve ads based on a visitor’s prior visits to this and other websites. You can opt out of personalised advertising at <a href="https://www.google.com/settings/ads" rel="noopener">Google Ads Settings</a>.</p>
<h2>External links</h2>
<p>Pages may link to other websites. The author is not responsible for their privacy practices.</p>
<h2>Changes</h2>
<p>This policy may be updated from time to time; the date above shows the latest revision.</p>
<p>Questions: <a href="/contact/">contact page</a>.</p>
</main>''' + foot()
    write("privacy", body, "0.2")

def page_404():
    body = head("Page not found – "+NAME,"The page you were looking for could not be found.","404.html") + nav("") + '''
<main class="wrap"><h1>Page not found</h1><p>Please go to the <a href="/">home page</a> or the <a href="/sri-suktam/">Śrī Sūktam index</a>.</p></main>''' + foot()
    body = body.replace('<meta name="description"','<meta name="robots" content="noindex"><meta name="description"',1)
    open(os.path.join(ROOT,"404.html"),"w",encoding="utf-8").write(body)

def assets():
    os.makedirs(os.path.join(ROOT,"assets"),exist_ok=True)
    open(os.path.join(ROOT,"assets/favicon.svg"),"w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><circle cx="32" cy="32" r="30" fill="#7a1f2b"/><circle cx="32" cy="32" r="22" fill="none" stroke="#e5b94a" stroke-width="3"/><text x="32" y="43" font-size="30" text-anchor="middle" fill="#e5b94a" font-family="serif">श्री</text></svg>')
    open(os.path.join(ROOT,"assets/og.svg"),"w").write('<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630"><rect width="1200" height="630" fill="#7a1f2b"/><circle cx="600" cy="250" r="120" fill="none" stroke="#e5b94a" stroke-width="6"/><text x="600" y="290" font-size="110" text-anchor="middle" fill="#e5b94a" font-family="serif">श्री</text><text x="600" y="480" font-size="64" text-anchor="middle" fill="#fff" font-family="serif">Lakshmi Stuti</text><text x="600" y="545" font-size="32" text-anchor="middle" fill="#f3e8d6" font-family="serif">Śrī Sūktam and Kanakadhāra Stotram commentary</text></svg>')
    open(os.path.join(ROOT,"CNAME"),"w").write("lakshmistuti.com\n")
    open(os.path.join(ROOT,".nojekyll"),"w").write("")
    open(os.path.join(ROOT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    open(os.path.join(ROOT,"ads.txt"),"w").write("# Add the AdSense line here after approval, e.g.\n# google.com, pub-XXXXXXXXXXXXXXXX, DIRECT, f08c47fec0942fa0\n")

def sitemap():
    u = "".join(f'<url><loc>{SITE}/{p + "/" if p else ""}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>' for p,pr in PAGES)
    open(os.path.join(ROOT,"sitemap.xml"),"w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{u}</urlset>\n')

if __name__ == "__main__":
    page_home(); page_sri(); page_kana()
    for i in range(len(VERSES)): page_verse(i)
    page_gl(); page_about(); page_contact(); page_privacy(); page_404(); assets(); sitemap()
    print("built", len(PAGES), "pages")
