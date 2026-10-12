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
  closing="This first verse isn’t merely a chant. It is an invitation to the Divine, an invitation to nurture a gentle yet radiant heart that attracts true prosperity effortlessly. May your journey today become profoundly meaningful, peaceful, and enriching!",
 ),
 dict(
  n=2, slug="verse-2",
  deva="तां म आवह जातवेदो लक्ष्मीमनपगामिनीम्।<br>यस्यां हिरण्यं विन्देयं गामश्वं पुरुषानहम्॥",
  iast="Tāṁ ma āvaha jāta-vedo lakṣmīm anapagāminīm,<br>Yasyāṁ hiraṇyaṁ vindeyaṁ gāmaśvaṁ puruṣān aham.",
  title="Śrī Sūktam Verse 2 Meaning – Tāṁ Ma Āvaha Jātavedo Explained",
  desc="Śrī Sūktam Verse 2 (Tāṁ Ma Āvaha) with Devanāgarī, transliteration, word-by-word meaning, the idea of Lakshmi as the one who never leaves, and a short meditation.",
  h1="Śrī Sūktam – Verse 2",
  sub="Tāṁ Ma Āvaha – the Goddess who never leaves",
  words=[
   ("तां","Tāṁ","That Goddess","Referring to Lakshmi."),
   ("म आवह","Ma āvaha","Please bring (to me)","A request made to Agni, as in the first verse."),
   ("जातवेदः","Jātavedaḥ","O Fire God (Agni), the knower of all beings","As in the first verse, Agni is invoked as the divine messenger who carries prayers to higher realms."),
   ("लक्ष्मीम्","Lakṣmīm","Goddess Lakshmi","The embodiment of prosperity, grace and well-being."),
   ("अनपगामिनीम्","Anapagāminīm","One who never leaves, who is always present","Symbolising unwavering, enduring prosperity: not just material wealth but lasting spiritual and emotional well-being."),
   ("यस्याम्","Yasyāṁ","By whose presence",""),
   ("हिरण्यं विन्देयं","Hiraṇyaṁ vindeyaṁ","I may obtain gold (divine wealth)","<em>Hiraṇyaṁ</em> here is not just physical gold but symbolises abundance in all aspects: health, wisdom, dharma and joy."),
   ("गामश्वम्","Gām aśvam","Cattle and horses","Cattle represent nourishment (food, sustenance), and horses symbolise energy, movement and progress."),
   ("पुरुषानहम्","Puruṣān aham","And worthy, noble people","The blessing of good companionship, wise people around you, or even progeny and lineage."),
  ],
  meaning="O Jātaveda (sacred fire, divine messenger), please bring to me that ever-present, unwavering Goddess Lakshmi, whose presence bestows prosperity and grace. May I, through her blessings, attain divine wealth, nourishment, strength and the company of noble souls.",
  insights=[
   ("Lakshmi as Anapagāminī, the one who never leaves","True prosperity is not temporary or fleeting. It is steady, ever-present and deeply rooted in righteousness (dharma). Material wealth can come and go, but spiritual wealth, meaning wisdom, peace, gratitude and inner contentment, stays forever."),
   ("Requesting abundance beyond just money","Gold (<em>Hiraṇyaṁ</em>) symbolises not just money but also wisdom, divine grace and clarity. Cattle (<em>Gāṁ</em>) represent sustenance and nourishment, enough to share with others. Horses (<em>Aśvam</em>) represent movement, progress, energy and success in one’s pursuits. Good company (<em>Puruṣān</em>) represents the importance of being surrounded by wise, ethical and noble people who uplift us. True wealth is holistic: financial, emotional, mental and social well-being."),
   ("Why invoke Agni (Jātaveda) again?","Fire symbolises purification and transformation. Just as fire transforms raw food into nourishment, it is also believed to transform prayers into divine blessings. Here, we ask Agni to connect us with the divine abundance of Lakshmi, not just for material wealth but for holistic, righteous prosperity."),
  ],
  meditation=["Sit quietly after chanting.",
              "Visualise Goddess Lakshmi seated on a lotus, golden radiance surrounding her, blessing you.",
              "Feel her grace as an unshakable presence in your life, not just today but always.",
              "Picture yourself abundantly blessed, not just with money but with wisdom, peace, health and noble companions.",
              "Whisper gently in your heart: “May true abundance, spiritual and material, flow into my life, and may I share it with others.”"],
  reflection="Today, focus on what true abundance means to you. Ask yourself: is my prosperity steady and rooted in righteousness, or is it fleeting? Cultivate gratitude for the abundance already present in your life, however small or great.",
  closing="This verse reminds us that Lakshmi is not just about gold coins. She is the inner wealth that stays with us forever. Prosperity without peace is meaningless; abundance without wisdom is dangerous. By understanding this verse, we shift from simply seeking wealth to seeking holistic well-being, progress and good company, things that enrich life beyond measure.",
 ),
 dict(
  n=3, slug="verse-3",
  deva="अश्वपूर्वां रथमध्यां हस्तिनादप्रबोधिनीम्।<br>श्रियं देवीमुपह्वये श्रीर्मा देवी जुषताम्॥",
  iast="Aśva-pūrvāṁ ratha-madhyāṁ hastināda-prabodhinīm,<br>Śriyaṁ devīm upahvaye śrīr mā devī juṣatām.",
  title="Śrī Sūktam Verse 3 Meaning – Aśvapūrvāṁ Rathamadhyāṁ Explained",
  desc="Śrī Sūktam Verse 3 (Aśvapūrvāṁ Rathamadhyāṁ) with Devanāgarī, transliteration, word-by-word meaning, the symbolism of horses, chariot and elephants, and a short meditation.",
  h1="Śrī Sūktam – Verse 3",
  sub="Aśvapūrvāṁ Rathamadhyāṁ – the grand arrival of Lakshmi",
  words=[
   ("अश्वपूर्वां","Aśva-pūrvāṁ","One who is preceded by horses","Horses symbolise speed, energy, progress and power, the dynamic force that moves life forward. In ancient Vedic times, a grand chariot led by horses signified royalty and divine strength."),
   ("रथमध्यां","Ratha-madhyāṁ","One who is seated at the center of a chariot","Represents Lakshmi’s royal, majestic presence, signifying that prosperity moves with strength and direction."),
   ("हस्तिनादप्रबोधिनीम्","Hastināda-prabodhinīm","One awakened by the trumpeting of elephants","Elephants symbolise power, royalty, dignity and wisdom. Their majestic call is seen as a herald of prosperity and abundance. This line portrays Goddess Lakshmi arriving in grandeur, with horses leading the way and elephants trumpeting her arrival, symbolising immense, unstoppable prosperity."),
   ("श्रियं देवीमुपह्वये","Śriyaṁ devīm upahvaye","I invoke the divine Goddess Lakshmi","A heartfelt invocation, calling upon Lakshmi’s presence with reverence and devotion."),
   ("श्रीर्मा देवी जुषताम्","Śrīr mā devī juṣatām","May the divine Goddess Śrī bless me and reside with me","Not just visit, but stay permanently, bringing lasting prosperity and well-being."),
  ],
  meaning="I invoke the divine Goddess Lakshmi, who arrives in majesty, preceded by swift horses, seated in a grand chariot, and awakened by the mighty trumpet of elephants. May this supreme Goddess of prosperity bless me and reside in my life forever.",
  insights=[
   ("The grand arrival of Lakshmi: dynamic, unstoppable prosperity","This verse paints a majestic picture of Goddess Lakshmi’s arrival, not as a mere deity but as a powerful force of abundance. True prosperity comes with energy, movement and direction, just like a chariot powered by strong horses. Question to reflect on: is my life moving with direction and energy toward prosperity, or am I stagnant?"),
   ("The symbolism of horses, chariot and elephants","Horses (<em>Aśva-pūrvāṁ</em>) stand for speed, enthusiasm and energy: progress requires effort. The chariot (<em>Ratha-madhyāṁ</em>) stands for the structured path of life: prosperity follows discipline. Elephants (<em>Hastināda-prabodhinīm</em>) stand for strength, stability and wisdom: true prosperity is not temporary, and must be grounded in wisdom and righteousness. Reflection: do I balance energy (horses) with wisdom (elephants) in my pursuit of prosperity?"),
   ("Requesting not just wealth but a permanent divine presence","The last line, <em>Śrīr mā devī juṣatām</em>, is very special. It means “May the divine Goddess not just visit, but reside with me.” We are asking for lasting prosperity: not fleeting gains, but wealth rooted in virtue, gratitude and wisdom. Reflection: am I cultivating a mindset and actions that invite lasting prosperity into my life?"),
  ],
  meditation=["After chanting, visualise Goddess Lakshmi’s grand arrival.",
              "A golden chariot, led by white horses, approaches with grace.",
              "Mighty elephants trumpet, signalling unstoppable abundance.",
              "Lakshmi, glowing with divine radiance, blesses you with prosperity that is powerful, stable and enduring.",
              "Whisper gently in your heart: “May my prosperity be powerful yet wise, fast yet steady, and may it stay with me forever.”"],
  reflection="Where in your life do you need speed and energy (horses)? Where do you need wisdom and stability (elephants)? How can you ensure prosperity stays permanently, not just visits briefly? For example, by cultivating gratitude, ethical wealth practices, giving back and continuous learning.",
  closing="This verse teaches that prosperity isn’t just about financial gain. It is about momentum, stability, wisdom and divine grace. True abundance is a balance of enthusiasm (horses), structure (chariot) and wisdom (elephants). When these forces are aligned, Lakshmi doesn’t just visit; she stays.",
 ),
]
TOTAL_SRI = 15  # core verses of the Śrī Sūktam (a closing phalaśruti follows)

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
 ("अनपगामिनी","Anapagāminī","One who never leaves; ever-present, enduring.","sri-suktam/verse-2/"),
 ("विन्देयम्","Vindeyam","May I obtain.","sri-suktam/verse-2/"),
 ("गो","Go","Cow, cattle; nourishment and sustenance.","sri-suktam/verse-2/"),
 ("अश्व","Aśva","Horse; energy, movement and progress.","sri-suktam/verse-2/"),
 ("रथ","Ratha","Chariot; the structured path of life.","sri-suktam/verse-3/"),
 ("हस्ती","Hastin","Elephant; strength, dignity, stability and wisdom.","sri-suktam/verse-3/"),
 ("नाद","Nāda","Sound, trumpeting call.","sri-suktam/verse-3/"),
 ("उपह्वये","Upahvaye","I call upon, I invoke.","sri-suktam/verse-3/"),
 ("जुषताम्","Juṣatām","May she favour, be pleased with, and stay with.","sri-suktam/verse-3/"),
 ("श्री","Śrī","Lakshmi; prosperity, grace and auspiciousness.","sri-suktam/verse-3/"),
 ("पुरुष","Puruṣa","Person, man; here the noble people, companions and lineage one is blessed with.","sri-suktam/verse-2/"),
]

YANTRA = '''<svg class="yantra" viewBox="0 0 300 300" aria-hidden="true" focusable="false"><g fill="none" stroke="currentColor" stroke-width=".7" stroke-linejoin="round">
<rect x="2" y="2" width="296" height="296"/><rect x="9" y="9" width="282" height="282"/><rect x="137" y="2" width="26" height="20"/><rect x="137" y="278" width="26" height="20"/><rect x="2" y="137" width="20" height="26"/><rect x="278" y="137" width="20" height="26"/><circle cx="150" cy="150" r="138"/><circle cx="150" cy="150" r="134"/><circle cx="150" cy="150" r="130"/><g><path d="M150,40.0 Q164.0,29.5 150,19.0 Q136.0,29.5 150,40.0Z" transform="rotate(0.00 150 150)"/><path d="M150,40.0 Q164.0,29.5 150,19.0 Q136.0,29.5 150,40.0Z" transform="rotate(22.50 150 150)"/><path d="M150,40.0 Q164.0,29.5 150,19.0 Q136.0,29.5 150,40.0Z" transform="rotate(45.00 150 150)"/><path d="M150,40.0 Q164.0,29.5 150,19.0 Q136.0,29.5 150,40.0Z" transform="rotate(67.50 150 150)"/><path d="M150,40.0 Q164.0,29.5 150,19.0 Q136.0,29.5 150,40.0Z" transform="rotate(90.00 150 150)"/><path d="M150,40.0 Q164.0,29.5 150,19.0 Q136.0,29.5 150,40.0Z" transform="rotate(112.50 150 150)"/><path d="M150,40.0 Q164.0,29.5 150,19.0 Q136.0,29.5 150,40.0Z" transform="rotate(135.00 150 150)"/><path d="M150,40.0 Q164.0,29.5 150,19.0 Q136.0,29.5 150,40.0Z" transform="rotate(157.50 150 150)"/><path d="M150,40.0 Q164.0,29.5 150,19.0 Q136.0,29.5 150,40.0Z" transform="rotate(180.00 150 150)"/><path d="M150,40.0 Q164.0,29.5 150,19.0 Q136.0,29.5 150,40.0Z" transform="rotate(202.50 150 150)"/><path d="M150,40.0 Q164.0,29.5 150,19.0 Q136.0,29.5 150,40.0Z" transform="rotate(225.00 150 150)"/><path d="M150,40.0 Q164.0,29.5 150,19.0 Q136.0,29.5 150,40.0Z" transform="rotate(247.50 150 150)"/><path d="M150,40.0 Q164.0,29.5 150,19.0 Q136.0,29.5 150,40.0Z" transform="rotate(270.00 150 150)"/><path d="M150,40.0 Q164.0,29.5 150,19.0 Q136.0,29.5 150,40.0Z" transform="rotate(292.50 150 150)"/><path d="M150,40.0 Q164.0,29.5 150,19.0 Q136.0,29.5 150,40.0Z" transform="rotate(315.00 150 150)"/><path d="M150,40.0 Q164.0,29.5 150,19.0 Q136.0,29.5 150,40.0Z" transform="rotate(337.50 150 150)"/></g><g><path d="M150,66.0 Q176.0,53.5 150,41.0 Q124.0,53.5 150,66.0Z" transform="rotate(0.00 150 150)"/><path d="M150,66.0 Q176.0,53.5 150,41.0 Q124.0,53.5 150,66.0Z" transform="rotate(45.00 150 150)"/><path d="M150,66.0 Q176.0,53.5 150,41.0 Q124.0,53.5 150,66.0Z" transform="rotate(90.00 150 150)"/><path d="M150,66.0 Q176.0,53.5 150,41.0 Q124.0,53.5 150,66.0Z" transform="rotate(135.00 150 150)"/><path d="M150,66.0 Q176.0,53.5 150,41.0 Q124.0,53.5 150,66.0Z" transform="rotate(180.00 150 150)"/><path d="M150,66.0 Q176.0,53.5 150,41.0 Q124.0,53.5 150,66.0Z" transform="rotate(225.00 150 150)"/><path d="M150,66.0 Q176.0,53.5 150,41.0 Q124.0,53.5 150,66.0Z" transform="rotate(270.00 150 150)"/><path d="M150,66.0 Q176.0,53.5 150,41.0 Q124.0,53.5 150,66.0Z" transform="rotate(315.00 150 150)"/></g>
<circle cx="150" cy="150" r="82"/><circle cx="150" cy="150" r="80"/>
<g transform="translate(150 150) scale(.8) translate(-150 -150)"><polygon points="53.7,123.2 246.3,123.2 150,250.0"/><polygon points="53.0,174.2 247.0,174.2 150,50.0"/><polygon points="98.7,220.0 201.3,220.0 150,123.2"/><polygon points="78.3,197.9 221.7,197.9 150,78.1"/><polygon points="90.5,78.1 209.5,78.1 150,160.7"/><polygon points="81.0,103.1 219.0,103.1 150,220.0"/><polygon points="114.9,160.7 185.1,160.7 150,103.1"/><polygon points="116.4,134.3 183.6,134.3 150,197.9"/><polygon points="124.6,144.8 175.4,144.8 150,174.2"/><circle cx="150" cy="150" r="1.6" fill="currentColor"/></g></g></svg>'''
INTRO_HTML = '''<div class="intro-overlay" id="intro" role="dialog" aria-label="Welcome">
<svg viewBox="-120 -120 240 240" class="lotus" aria-hidden="true"><g fill="none" stroke="#b8860b" stroke-width="1.4"><path class="p" d="M0,0 C-26,-30 -22,-76 0,-104 C22,-76 26,-30 0,0Z" transform="rotate(0)"/><path class="p" d="M0,0 C-26,-30 -22,-76 0,-104 C22,-76 26,-30 0,0Z" transform="rotate(45)"/><path class="p" d="M0,0 C-26,-30 -22,-76 0,-104 C22,-76 26,-30 0,0Z" transform="rotate(90)"/><path class="p" d="M0,0 C-26,-30 -22,-76 0,-104 C22,-76 26,-30 0,0Z" transform="rotate(135)"/><path class="p" d="M0,0 C-26,-30 -22,-76 0,-104 C22,-76 26,-30 0,0Z" transform="rotate(180)"/><path class="p" d="M0,0 C-26,-30 -22,-76 0,-104 C22,-76 26,-30 0,0Z" transform="rotate(225)"/><path class="p" d="M0,0 C-26,-30 -22,-76 0,-104 C22,-76 26,-30 0,0Z" transform="rotate(270)"/><path class="p" d="M0,0 C-26,-30 -22,-76 0,-104 C22,-76 26,-30 0,0Z" transform="rotate(315)"/><circle r="108" class="ring"/></g></svg>
<p class="in-deva">ॐ श्रीं महालक्ष्म्यै नमः</p>
<p class="in-name">Lakshmi Stuti</p>
<button type="button" class="skip" id="skip">Skip intro</button>
</div>'''
INTRO_SCRIPT = '''<script>(function(){var o=document.getElementById("intro");if(!o)return;function done(){document.documentElement.classList.remove("intro");try{sessionStorage.setItem("ls_intro","1")}catch(e){}}document.getElementById("skip").addEventListener("click",done);o.addEventListener("click",done);setTimeout(done,3600);})();</script>'''

# ---------------------------------------------------------------- templates
INTRO_JS = '<script>try{if(location.pathname==="/"&&!sessionStorage.getItem("ls_intro")&&!matchMedia("(prefers-reduced-motion:reduce)").matches){document.documentElement.className+=" intro"}}catch(e){}</script>'

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
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Inter:wght@400;500;600&family=Noto+Serif+Devanagari:wght@500;700&display=swap">
<link rel="stylesheet" href="/assets/style.css">
{ldh}{ga}{ads}
{INTRO_JS if path=="" else ""}
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
<p class="shri foot" lang="sa">श्री</p>
<p><a href="/sri-yantra/">Śrī Yantra</a><a href="/about/">About</a><a href="/contact/">Contact</a><a href="/privacy/">Privacy Policy</a></p>
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
    v = VERSES[-1]
    t = "Lakshmi Stuti – Śrī Sūktam & Kanakadhāra Stotram Meaning in English"
    d = "Verse-by-verse English commentary on the Śrī Sūktam and Kanakadhāra Stotram to Goddess Lakshmi (Laxmi): Devanāgarī, transliteration, word meanings and practice."
    ld = {"@context":"https://schema.org","@type":"WebSite","name":NAME,"url":SITE+"/","inGroup":None,"author":{"@type":"Person","name":AUTHOR},"inLanguage":"en"}
    ld.pop("inGroup")
    body = head(t,d,"",ld) + INTRO_HTML + nav("home") + f'''
<main class="wrap">
<section class="hero">
{YANTRA}
<p class="shri" lang="sa">श्री</p>
<p class="eyebrow">Śrī Sūktam · Kanakadhāra Stotram</p>
<h1>Śrī Sūktam &amp; Kanakadhāra Stotram, understood gently</h1>
<p class="lede">A slow, verse-by-verse commentary on the hymns to Goddess Lakshmi (also written Laxmi): the original text, simple word meanings, and a short practice for each verse.</p>
<p><a class="btn" href="/sri-suktam/verse-1/">Start with Verse 1</a><a class="btn ghost" href="/sri-suktam/">Śrī Sūktam index</a></p>
</section>
<section class="garden">
<h2>A sacred garden, one seed at a time</h2>
<p>Think of your journey into the Śrī Sūktam like planting seeds in a sacred garden. Each verse is a seed. By carefully understanding and meditating upon one verse daily, you gently plant and nurture it within your heart. Slowly but surely, this practice blossoms into an abundant, radiant inner garden of clarity, devotion and wisdom.</p>
<p>Here is a practical and poetic approach you can follow each day.</p>
<ol class="steps">
<li><h3>Choose your verse</h3><p>Begin with the first verse. Take your time. There is no hurry; it is depth, not speed, that matters here.</p></li>
<li><h3>Understand the meaning</h3><p>Read an authentic translation. Reflect deeply: what qualities of the divine are highlighted, and how do they resonate with you personally?</p></li>
<li><h3>Chant and meditate</h3><p>Recite the verse slowly, attentively and lovingly. After chanting, sit quietly and let the vibration and meaning settle into your heart. Visualise the essence of the verse and feel it within you.</p></li>
<li><h3>Take it into your heart</h3><p>Through the day, recall the meaning and let the verse echo silently. Allow its wisdom to gently influence your interactions and decisions.</p></li>
<li><h3>Gratitude and reflection</h3><p>Before sleep, reflect on how the verse subtly influenced your day. Express sincere gratitude to the divine for the insights gained.</p></li>
</ol>
<p>This mindful approach turns spiritual practice into an enriching daily ritual. Each verse becomes an intimate friend, illuminating your inner space and your life.</p>
<p>Stay gently sceptical, too. Allow yourself curiosity and questions; explore, feel, understand, and trust the ancient wisdom at your own rhythm. No rush, only mindful growth.</p>
<p class="amen">You are on a beautiful path. Enjoy every step.</p>
</section>
<div class="grid">
<a class="tile" href="/sri-suktam/"><h3>Śrī Sūktam</h3><p>The Vedic hymn to Lakshmi. {len(VERSES)} verses are live; more are added one at a time.</p></a>
<a class="tile" href="/kanakadhara/"><h3>Kanakadhāra Stotram <span class="soon">coming soon</span></h3><p>Śrī Śaṅkarācārya’s hymn to Lakshmi, to follow the Śrī Sūktam.</p></a>
<a class="tile" href="/sri-yantra/"><h3>Śrī Yantra</h3><p>The sacred diagram of Lakshmi, and what each of its five layers means.</p></a>
<a class="tile" href="/glossary/"><h3>Glossary</h3><p>Sanskrit words used across the commentary, with simple meanings.</p></a>
</div>
<h2>Today’s verse</h2>
<div class="verse"><p class="label">Śrī Sūktam · Verse {v["n"]}</p><p class="deva">{v["deva"]}</p><p class="iast">{v["iast"]}</p></div>
<p>{E(v["closing"])} <a href="/sri-suktam/{v["slug"]}/">Read the full commentary →</a></p>
{ad("home")}
</main>''' + INTRO_SCRIPT + foot()
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
    ins = "".join(f'<div class="card"><h3>{E(a)}</h3><p>{b}</p></div>' for a,b in v["insights"])
    med = "".join(f"<li>{E(x)}</li>" for x in v["meditation"])
    p = f'<a href="/sri-suktam/{prev["slug"]}/">← Verse {prev["n"]}</a>' if prev else '<span class="off">← Previous</span>'
    n = f'<a href="/sri-suktam/{nxt["slug"]}/">Verse {nxt["n"]} →</a>' if nxt else f'<span class="off">Verse {v["n"]+1} coming soon →</span>'
    body = head(v["title"],v["desc"],path+"/",art,"article") + f'<script type="application/ld+json">{json.dumps(bc_ld(parts),ensure_ascii=False)}</script>' + nav("sri") + f'''
<main class="wrap"><article>
{crumbs([("Śrī Sūktam","sri-suktam/"),(f"Verse {v['n']}",None)])}
<p class="shri small" lang="sa">श्री</p>
<h1>{v["h1"]}</h1>
<p class="lede">{E(v["sub"])}</p>
<p class="crumbs">By {AUTHOR}</p>
<div class="verse">{YANTRA}<p class="label">Devanāgarī</p><p class="deva" lang="sa">{v["deva"]}</p><p class="iast" lang="sa-Latn">{v["iast"]}</p></div>
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
<p><em>{E(v["closing"])}</em></p>
<p class="crumbs">Terms used here are explained in the <a href="/glossary/">glossary</a>. This commentary was prepared with AI assistance; <a href="/about/">read more</a>.</p>
{ad("end")}
<div class="pager">{p}{n}</div>
</article></main>''' + foot()
    write(path, body, "0.9")

def page_yantra():
    t = "Śrī Yantra Meaning – Layers and Symbolism of the Lakshmi Yantra"
    d = "What the Śrī Yantra is and what each layer means: the enclosure, circle, lotus petals, nine triangles and the central point."
    parts = [("Śrī Yantra","sri-yantra/")]
    body = head(t,d,"sri-yantra/",bc_ld(parts)) + nav("") + f'''
<main class="wrap">{crumbs([("Śrī Yantra",None)])}
<p class="shri small" lang="sa">श्री</p>
<h1>The Śrī Yantra</h1>
<p class="lede">The Śrī Yantra is the sacred diagram associated with Goddess Lakshmi (Śrī): nine interlocking triangles around a central point, held inside circles, lotus petals and a gated square.</p>
<div class="verse yantra-big">{YANTRA}<p class="shri" lang="sa" style="font-size:2.4rem;margin:70px 0">श्रीं</p></div>
<h2>What is a yantra?</h2>
<p>A yantra is a geometric design made of shapes and patterns, used in early India as the basis on which major temples were planned. The word <em>yantra</em> means “machinery”. Like a machine, it has one task: to turn one form of energy into another and put it to use. Yantras are made for different purposes, such as prosperity or peace in the home.</p>
<h2>The layers, from the outside in</h2>
<div class="card"><h3>1. The enclosure (the Sun layer)</h3><p>The outermost square, with its four gateways. It is the first layer and creates a protected, enclosed space in the yantra. According to the source below, a yantra is drawn starting from this layer and energised last.</p></div>
<div class="card"><h3>2. The circle (the Moon layer)</h3><p>The circle stands for the continuous flow of energy. Where the square regulates energy at its corners and junctions, the circle lets it flow evenly. The Moon layer also keeps the strong energy of the Sun in balance.</p></div>
<div class="card"><h3>3. The lotus petals (the filter)</h3><p>Two rings of petals clean the energy, letting the steady, flowing part pass and holding back the disturbed part. The two rings stand in a ratio of 1:2 or 1:1. In the Śrī Yantra there are eight inner petals and sixteen outer petals, a ratio of 1:2.</p></div>
<div class="card"><h3>4. The triangles (the converters)</h3><p>Triangles take energy of one form and send it in one direction with full force. The Śrī Yantra has nine: four pointing upward and five pointing downward, interlocked so that together they form forty-three smaller triangles.</p></div>
<div class="card"><h3>5. The central point (bindu)</h3><p>All the energy finally reaches the centre, which becomes the point of reception. The bindu is the heart of the yantra.</p></div>
<h2>The seed sound</h2>
<p>A yantra is written in a language of its own, built from seed sounds (<em>bīja mantras</em>). The seed sound associated with Lakshmi is <em>Śrīṁ</em> (श्रीं), the sound shown in the yantra above. The same Śrī gives its name to the Śrī Sūktam, the hymn this site studies.</p>
<p>Begin with the <a href="/sri-suktam/verse-1/">first verse of the Śrī Sūktam</a>.</p>
<h2>Sources and credits</h2>
<p>The layer descriptions are adapted from the presentation <em>Universal Energy: Geometry of the Universe – Basics of Yantras</em> by Deepanshu Giri. The drawing uses the nine-triangle geometry published by Bhaskar Tripathi at <a href="https://texample.net/sri-yantra/" rel="noopener">texample.net</a> (CC BY-SA 4.0).</p>
</main>''' + foot()
    write("sri-yantra", body, "0.7")

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
<h2>Credits</h2>
<p>The Śrī Yantra drawn in the background uses the nine-triangle geometry published by Bhaskar Tripathi at <a href="https://texample.net/sri-yantra/" rel="noopener">texample.net</a> (CC BY-SA 4.0).</p>
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
    page_yantra(); page_gl(); page_about(); page_contact(); page_privacy(); page_404(); assets(); sitemap()
    print("built", len(PAGES), "pages")
