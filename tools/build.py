#!/usr/bin/env python3
"""Static site generator for lakshmistuti.com
Run:  python3 tools/build.py      (from the repo root)
Add a verse by appending to VERSES below, then rebuild.
"""
import os, re, json, html, hashlib, unicodedata, subprocess
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://lakshmistuti.com"
NAME = "Lakshmi Stuti"
AUTHOR = "Amit N. Lakhtariya"
TODAY = date.today().isoformat()
GSC_TOKEN = "ydCk8z62OzpGbv6EnLvQAu8VoJl7T40cv6htu9_FsWs"  # Google Search Console site verification
GA_ID = "G-X1Y34J30ST"   # Google Analytics 4 measurement ID
ADSENSE_CLIENT = "" # e.g. "ca-pub-1234567890123456" -> switches AdSense on after approval
CONTACT_EMAIL = "shreelakshmistuti@gmail.com"
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
   ("हरिणीं","Hariṇīṁ","Resembling a deer (doe)","Gentle and graceful: it points to gentleness, beauty, purity and swiftness. This commentary follows the deer reading. Other commentators read <em>hariṇī</em> as “golden-yellow” (from <em>hari</em>, tawny gold), or as “she who takes away” sorrow and poverty. The three readings sit comfortably together."),
   ("सुवर्णरजतस्रजाम्","Suvarṇa-rajata-srajām","Wearing garlands of gold and silver","<em>Suvarṇa</em> = gold, <em>rajata</em> = silver, <em>sraj</em> = a garland or wreath. It speaks of richness, prosperity, brilliance, divine radiance and cosmic abundance. Gold is the colour of the sun and silver of the moon, which prepares the way for <em>Chandrāṁ</em> in the next word."),
   ("चन्द्रां","Chandrāṁ","Shining and gladdening, moon-like","The root of <em>candra</em> means both “to shine” and “to delight”, and the moon is called <em>candra</em> because it gladdens the heart. So the word carries coolness, soothing grace, serenity, beauty and balanced emotions, together with the joy she brings."),
   ("हिरण्मयीं लक्ष्मीं","Hiraṇmayīṁ Lakṣmīṁ","The golden form of Goddess Lakshmi","Divine abundance, prosperity and spiritual richness. Note the difference from the first word: <em>hiraṇya-varṇā</em> is golden in colour, in appearance, while <em>hiraṇmayī</em> is golden in substance, made of gold. She is golden both in how she appears and in what she is."),
   ("जातवेदो म आवह","Jātavedo ma āvaha","O Jātaveda (Fire, Agni), please invite or bring her to me","<em>Jātaveda</em> means “one who knows all births”. Agni is the mediator who carries our prayers to the Divine."),
  ],
  meaning="O Jātaveda (sacred fire, knower of all births), I humbly request you to invite into my life the golden-hued, graceful, gentle Goddess Lakshmi, who is adorned with garlands of gold and silver, who radiates serenity like the soft glow of the moon. May she gracefully enter my life, bestowing purity, peace, prosperity and spiritual harmony.",
  insights=[
   ("Gentleness (Hariṇīṁ)","True abundance and fulfilment are drawn not through harsh pursuit but through gentleness, grace and purity of heart."),
   ("The gold and silver garland","Balanced material and spiritual prosperity: gold stands for worldly success, silver for emotional and spiritual wisdom."),
   ("Moon-like radiance (Chandrāṁ)","Real prosperity is serene, calm and balanced. It cools the mind, relieves stress and brings peace."),
   ("The role of Agni (Jātaveda)","You are not alone on the journey. You ask the divine forces, with Agni as messenger, to guide you and connect you with universal abundance."),
   ("Where this hymn comes from","The Śrī Sūktam is a <em>khila</em>, a supplement to the Ṛgveda. In the Vedic tradition Agni is the one who carries offerings from the sacrificial fire to the gods, which is why the hymn begins by addressing him as <em>Jātavedas</em>. In the traditional worship of Lakshmi this first verse is commonly used as the invocation, the moment of inviting the Goddess to be present. Reading it that way, the verse is not a request for a distant favour but a formal welcome."),
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
   ("A note on the Sanskrit","Two small points for readers who like the text close up. First, <em>juṣatām</em> literally means “may she be pleased with me” or “may she favour me”. The sense of her staying with us is a devotional extension of that favour, and it is how this commentary reads the line. Second, <em>ratha-madhyāṁ</em> is also read as the order of a royal procession: horses in front, chariots in the middle and elephants behind. Either way, the picture is one of a queen arriving with her full retinue."),
  ],
  meditation=["After chanting, visualise Goddess Lakshmi’s grand arrival.",
              "A golden chariot, led by white horses, approaches with grace.",
              "Mighty elephants trumpet, signalling unstoppable abundance.",
              "Lakshmi, glowing with divine radiance, blesses you with prosperity that is powerful, stable and enduring.",
              "Whisper gently in your heart: “May my prosperity be powerful yet wise, fast yet steady, and may it stay with me forever.”"],
  reflection="Where in your life do you need speed and energy (horses)? Where do you need wisdom and stability (elephants)? How can you ensure prosperity stays permanently, not just visits briefly? For example, by cultivating gratitude, ethical wealth practices, giving back and continuous learning.",
  closing="This verse teaches that prosperity isn’t just about financial gain. It is about momentum, stability, wisdom and divine grace. True abundance is a balance of enthusiasm (horses), structure (chariot) and wisdom (elephants). When these forces are aligned, Lakshmi doesn’t just visit; she stays.",
 ),
 dict(
  n=4, slug="verse-4",
  deva="कां सोस्मितां हिरण्यप्राकारामार्द्रां ज्वलन्तीं तृप्तां तर्पयन्तीम्।<br>पद्मे स्थितां पद्मवर्णां तामिहोपह्वये श्रियम्॥",
  iast="Kāṁ sosmitāṁ hiraṇya-prākārām ārdrāṁ jvalantīṁ tṛptāṁ tarpayantīm,<br>Padme sthitāṁ padma-varṇāṁ tām ihopahvaye śriyam.",
  title="Śrī Sūktam Verse 4 Meaning – Kāṁ Sosmitāṁ Hiraṇyaprākārām Explained",
  desc="Śrī Sūktam Verse 4 (Kāṁ Sosmitāṁ) with Devanāgarī, transliteration, word-by-word meaning, the golden fortress, compassion and contentment of Lakshmi, and a short meditation.",
  h1="Śrī Sūktam – Verse 4",
  sub="Kāṁ Sosmitāṁ – Lakshmi, golden-walled, compassionate and radiant",
  words=[
   ("कां सोस्मितां","Kāṁ sosmitāṁ","Her whom I long for, the blissful one with a gentle smile","A poetic emphasis on the yearning of the seeker: that Lakshmi whom I desire and call upon with reverence. Many commentators read <em>kāṁ</em> as “who, that is, the blissful, the indescribable one” and <em>sosmitā</em> as <em>sa-smitā</em>, “with a gentle smile”."),
   ("हिरण्यप्राकाराम्","Hiraṇya-prākārām","One who is surrounded by walls of gold","Symbolising the supreme protection of divine abundance, and that true prosperity is fortified and safe."),
   ("आर्द्राम्","Ārdrām","Compassionate, moist, tender","A symbol of softness, nurturing and kindness. True prosperity is not dry or harsh: it nourishes all beings."),
   ("ज्वलन्तीम्","Jvalantīm","Radiant, shining like fire","Prosperity is not dull; it is luminous, energetic and dynamic."),
   ("तृप्ताम्","Tṛptāṁ","Fully satisfied","Lakshmi is herself complete, fulfilled and brimming with contentment."),
   ("तर्पयन्तीम्","Tarpayantīm","One who satisfies and nourishes others","True wealth nourishes and uplifts others, not just oneself."),
   ("पद्मे स्थिताम्","Padme sthitāṁ","Seated on a lotus","The lotus symbolises purity, beauty, detachment and divine perfection."),
   ("पद्मवर्णाम्","Padma-varṇāṁ","Lotus-hued, lotus-coloured","Her radiance and complexion are compared to the soft, soothing colours of a lotus."),
   ("तामिहोपह्वये श्रियम्","Tām ihopahvaye śriyam","I invoke that Śrī (Lakshmi) here and now, in my life",""),
  ],
  meaning="I call upon that Goddess Śrī (Lakshmi), who is surrounded by walls of gold, symbolising supreme abundance, whose presence is tender and compassionate, yet radiantly brilliant. She is fully satisfied and satisfies others, seated on a lotus with a lotus-like radiance. I invoke that divine prosperity to come and dwell here, in my life.",
  insights=[
   ("The golden fortress (Hiraṇya-prākārām)","Prosperity is not fragile. True wealth, both material and spiritual, is well protected, stable and enduring. Reflection: am I building prosperity on strong, ethical foundations or on weak ground?"),
   ("Compassion and nourishment (Ārdrām and Tarpayantīm)","Abundance should flow outward, nourishing others. Selfish prosperity dries up; shared abundance multiplies. Reflection: how am I using my wealth, for self-indulgence or to nourish and support others?"),
   ("Radiance and contentment (Jvalantīm and Tṛptāṁ)","True wealth glows. It brings inner confidence, light and satisfaction. Lakshmi does not represent restless greed; she represents calm fulfilment and peaceful joy. Reflection: am I chasing endlessly, or am I cultivating contentment and peace with what I have?"),
   ("Lotus symbolism (Padme sthitāṁ, Padma-varṇāṁ)","The lotus grows in mud but remains untouched, a reminder that prosperity should be pure and detached from ego or corruption. Reflection: am I cultivating purity in my wealth, staying detached from arrogance and impurity?"),
  ],
  meditation=["Visualise Goddess Lakshmi seated on a beautiful lotus, glowing with radiant light, surrounded by golden walls of protection.",
              "See her eyes full of compassion, her aura warm and nourishing, her presence deeply calming yet brilliant.",
              "Whisper in your heart: “May the abundance that enters my life be pure, luminous, compassionate and protected. May I find joy in sharing and nourishing others.”"],
  reflection="Where am I building golden walls, meaning strong foundations, in my life, and where am I leaving cracks? Am I radiating contentment, or restless dissatisfaction? How can I share more, give more and nourish others from my abundance?",
  closing="This verse is a gentle reminder that true wealth is radiant, compassionate, stable and deeply fulfilling. It uplifts not only us but everyone we touch.",
 ),
 dict(
  n=5, slug="verse-5",
  deva="चन्द्रां प्रभासां यशसा ज्वलन्तीं श्रियं लोके देवजुष्टामुदाराम्।<br>तां पद्मिनीमीं शरणमहं प्रपद्येऽलक्ष्मीर्मे नश्यतां त्वां वृणे॥",
  iast="Chandrāṁ prabhāsāṁ yaśasā jvalantīṁ śriyaṁ loke devajuṣṭām udārām,<br>Tāṁ padminīm īṁ śaraṇam ahaṁ prapadye alakṣmīr me naśyatāṁ tvāṁ vṛṇe.",
  title="Śrī Sūktam Verse 5 Meaning – Chandrāṁ Prabhāsāṁ Explained",
  desc="Śrī Sūktam Verse 5 (Chandrāṁ Prabhāsāṁ) with Devanāgarī, transliteration, word-by-word meaning, surrender to Lakshmi, the removal of Alakṣmī and a short meditation.",
  h1="Śrī Sūktam – Verse 5",
  sub="Chandrāṁ Prabhāsāṁ – surrender, and the choice of Lakshmi",
  words=[
   ("चन्द्राम्","Chandrāṁ","Shining and gladdening, moon-like","Symbolises coolness, beauty, purity, emotional calm and grace."),
   ("प्रभासाम्","Prabhāsāṁ","Full of brilliant light","Refers to divine brightness, an inner spiritual glow."),
   ("यशसा ज्वलन्तीम्","Yaśasā jvalantīm","Glowing with fame, success and honour","True prosperity brings not just wealth, but respect and renown earned through good deeds."),
   ("श्रियं लोके देवजुष्टाम्","Śriyaṁ loke devajuṣṭām","That Śrī (Lakshmi), adored in the world and favoured by the gods themselves",""),
   ("उदाराम्","Udārām","Generous, magnanimous","True abundance is never stingy; it is generous, open-hearted and sharing."),
   ("तां पद्मिनीम्","Tāṁ padminīm","That lotus-bearing Goddess","The small word <em>īṁ</em> that follows is a Vedic particle of emphasis, usually left untranslated."),
   ("शरणमहं प्रपद्ये","Śaraṇam ahaṁ prapadye","I take refuge in her; I surrender myself at her feet","This is the deepest gesture of trust and humility, acknowledging that divine grace guides prosperity."),
   ("अलक्ष्मीर्मे नश्यताम्","Alakṣmīr me naśyatām","May all forms of misfortune (Alakṣmī) disappear from my life","<em>Alakṣmī</em> is the opposite of Lakshmi: poverty, scarcity, misfortune and negativity."),
   ("त्वां वृणे","Tvāṁ vṛṇe","I choose you (O Lakshmi); I seek you alone","A conscious choice to align with prosperity, grace and righteousness, rejecting all that is inauspicious."),
  ],
  meaning="I surrender myself to that radiant, moon-like, luminous Goddess Lakshmi, who shines with fame, grace and generosity, adored by the gods and revered by all. I take refuge in this lotus-bearing Goddess. May all misfortune vanish from my life; O Divine Lakshmi, I choose you and your grace alone.",
  insights=[
   ("Choosing prosperity consciously (Tvāṁ vṛṇe)","The verse teaches us that prosperity and misfortune are both energies we choose to invite or reject. Reflection: am I consciously choosing prosperity in thought, word and action every day?"),
   ("The removal of Alakṣmī (misfortune)","Prosperity is not just about attracting good; it is about cleansing negativity: scarcity mindsets, bad habits, laziness or unethical actions that block abundance. Reflection: what “Alakṣmī” habits or energies do I need to consciously let go of today?"),
   ("Magnanimity and generosity (Udārām)","True wealth radiates and uplifts others. Generosity amplifies prosperity. Reflection: where can I be more giving and open-hearted in my life?"),
   ("Surrender (Śaraṇam ahaṁ prapadye)","We do our part, but then we surrender the outcome to divine grace. Prosperity flows best when action meets surrender."),
  ],
  meditation=["Close your eyes and visualise the radiant form of Goddess Lakshmi, soft as moonlight yet brilliantly glowing.",
              "See her holding a lotus, smiling with compassion and generosity.",
              "Whisper softly in your heart: “O Divine Mother, I surrender at your feet. May all misfortune dissolve. May I embody light, grace, generosity and abundance. I choose you and your path.”"],
  reflection="What negative patterns (Alakṣmī) am I willing to consciously let go of? Where can I express more generosity (Udārām)? How can I trust and surrender more, while still taking inspired action?",
  closing="This verse is a powerful turning point. You are not just calling prosperity; you are declaring your conscious alignment with it, and rejecting scarcity, fear and negativity.",
 ),
 dict(
  n=6, slug="verse-6",
  deva="आदित्यवर्णे तपसोऽधिजातो वनस्पतिस्तव वृक्षोऽथ बिल्वः।<br>तस्य फलानि तपसानुदन्तु मायान्तरायाश्च बाह्या अलक्ष्मीः॥",
  iast="Āditya-varṇe tapaso ’dhijāto vanaspatis tava vṛkṣo ’tha bilvaḥ,<br>Tasya phalāni tapasā nudantu māyāntarāyāś ca bāhyā alakṣmīḥ.",
  title="Śrī Sūktam Verse 6 Meaning – Ādityavarṇe Tapaso ’dhijāto Bilvaḥ Explained",
  desc="Śrī Sūktam Verse 6 (Ādityavarṇe, the bilva tree) with Devanāgarī, transliteration, word-by-word meaning, prosperity born of tapas, and a short meditation on removing inner and outer obstacles.",
  h1="Śrī Sūktam – Verse 6",
  sub="Ādityavarṇe – the sun-like Goddess, tapas and the bilva tree",
  words=[
   ("आदित्यवर्णे","Āditya-varṇe","O one shining with the colour and brilliance of the sun (Āditya)","A praise of Lakshmi’s radiant, golden, life-giving energy, like the sun that nurtures and gives light to all."),
   ("तपसोऽधिजातः","Tapaso ’dhijāto","Born of austerity (tapas), effort and discipline","True abundance comes from inner discipline, effort and purity. Nothing is random; prosperity is the fruit of sustained, righteous effort. In the traditional reading, it is the tree that is said to have sprung from the Goddess’s own austerity."),
   ("वनस्पतिस्तव वृक्षोऽथ बिल्वः","Vanaspatis tava vṛkṣo ’tha bilvaḥ","The bilva, the lord of the forest, is your tree","The bilva tree represents sacred, deeply rooted blessings, and is often associated with Lord Shiva and used in pure offerings. Symbolically, this is a blessing for deeply rooted, steady and sacred prosperity."),
   ("तस्य फलानि तपसा नुदन्तु","Tasya phalāni tapasā nudantu","May the fruits of that tree (the fruits of my efforts) drive away all obstacles through the power of my discipline","The verse is saying: may the rewards of my effort remove every barrier between me and divine prosperity."),
   ("मायान्तरायाश्च बाह्या अलक्ष्मीः","Māyāntarāyāś ca bāhyā alakṣmīḥ","May all illusions (Māyā), inner obstacles (antarāya) and external misfortunes (bāhyā alakṣmīḥ) be destroyed","A direct prayer for the removal of confusion, mental blocks, self-sabotage and outer negativity."),
  ],
  meaning="O Goddess, radiant like the sun, born of divine effort and discipline: just as the sacred bilva tree bears blessed fruits, may the results of my sincere efforts remove all obstacles. May all illusions, inner barriers and external misfortunes dissolve away.",
  insights=[
   ("Sun-like radiance (Āditya-varṇe)","Prosperity is radiant, life-giving, nourishing and unwavering, like the sun. Reflection: am I radiating positivity and life-giving energy in my actions, or am I clouded?"),
   ("Prosperity rooted in tapas (effort)","Lakshmi rewards those who strive with discipline and purity. Reflection: am I relying on effort and sincerity, or hoping for shortcuts?"),
   ("The bilva tree as a symbol","The bilva tree is steady, sacred and fruitful. It grows slowly, but its fruits are considered divine. Reflection: am I planting deep, sacred efforts that will bear lasting fruits?"),
   ("Removing inner and outer obstacles","Often, inner confusion (<em>Māyā</em>) and self-imposed blocks (<em>Antarāya</em>) stop abundance. This verse is a powerful prayer to remove these blockages, both inside and around you."),
  ],
  meditation=["Visualise a grand, sacred bilva tree, strong and unshakable, filled with golden fruits.",
              "See each fruit as the result of your effort, discipline and pure intention.",
              "Imagine those fruits falling gently to the earth, dissolving every obstacle: inner fears, doubts and outer blockages.",
              "Whisper softly inside: “May the fruits of my righteous efforts remove every block. May all illusions and negativity fall away. May I shine, steady and bright, like the sun.”"],
  reflection="What are the “bilva seeds” I am planting in my life, efforts that are sacred, slow-growing, but deeply rewarding? What inner blocks (Māyā or confusion) do I need to dissolve? Am I truly shining like the sun in my words, actions and presence, or hiding behind clouds?",
  closing="This verse teaches us that prosperity is not an accident. It is the divine fruit of effort, discipline and clarity. Obstacles are natural, but with steady, righteous action and inner purity, they dissolve like mist before the morning sun.",
 ),
 dict(
  n=7, slug="verse-7",
  deva="उपैतु मां देवसखः कीर्तिश्च मणिना सह।<br>प्रादुर्भूतोऽस्मि राष्ट्रेऽस्मिन्कीर्तिमृद्धिं ददातु मे॥",
  iast="Upaitu māṁ deva-sakhaḥ kīrtiś ca maṇinā saha,<br>Prādurbhūto ’smi rāṣṭre ’smin kīrtim ṛddhiṁ dadātu me.",
  title="Śrī Sūktam Verse 7 Meaning – Upaitu Māṁ Devasakhaḥ Explained",
  desc="Śrī Sūktam Verse 7 (Upaitu Māṁ Devasakhaḥ) with Devanāgarī, transliteration, word-by-word meaning, Kubera, honour and prosperity in society, and a short meditation.",
  h1="Śrī Sūktam – Verse 7",
  sub="Upaitu Māṁ Devasakhaḥ – honour and prosperity in society",
  words=[
   ("उपैतु","Upaitu","May he (that divine force) approach me, come near me",""),
   ("मां","Māṁ","Me; in my life",""),
   ("देवसखः","Deva-sakhaḥ","The friend of the gods","This is often interpreted as Kubera, the divine treasurer, one who manages wealth with righteousness and wisdom."),
   ("कीर्तिः च","Kīrtiś ca","And fame, honour, good reputation","Some commentators also see <em>Kīrti</em> as the goddess of fame who comes with Kubera."),
   ("मणिना सह","Maṇinā saha","Along with brilliance (like a jewel)","Accompanied by splendour and brilliance. Some commentators read <em>maṇi</em> as Maṇibhadra, the companion of Kubera."),
   ("प्रादुर्भूतः अस्मि","Prādurbhūto ’smi","I have arisen; I have become manifest","In essence, a declaration of stepping into one’s rightful place, presence and responsibility."),
   ("राष्ट्रे अस्मिन्","Rāṣṭre ’smin","In this kingdom, in this land, in this society","It signifies prosperity and recognition not in isolation, but within the community, society or nation."),
   ("कीर्तिम्","Kīrtim","Honour, fame, good repute",""),
   ("ऋद्धिम्","Ṛddhiṁ","Growth, prosperity, success; spiritual and material advancement",""),
   ("ददातु मे","Dadātu me","May it be granted to me",""),
  ],
  meaning="May the friend of the gods (the divine treasurer Kubera), along with honour and shining brilliance, approach me. Having manifested in this society and this life, may I be blessed with both good reputation and steady prosperity.",
  insights=[
   ("“The friend of the gods” (Deva-sakhaḥ)","This is not just about material wealth; it is about divine companionship and guidance. True abundance does not come from selfish accumulation. It comes from aligning oneself with dharma (divine order) and being a friend to divine energies."),
   ("Honour and splendour (Kīrti and Maṇinā saha)","Prosperity without honour is hollow. The verse asks not just for wealth, but for respect, dignity and brilliance. Reflection: is my pursuit of prosperity guided by values that will earn respect in my community and family?"),
   ("Living in society (Rāṣṭre ’smin)","Prosperity is not for isolation, but for uplifting the world around you. Reflection: how am I contributing to my family, my society and my country through the prosperity I am blessed with?"),
   ("Good reputation (Kīrtim) and growth (Ṛddhim)","These are the two wings of true abundance: honour and steady advancement. Reflection: am I balancing growth with integrity?"),
  ],
  meditation=["Visualise yourself standing in a beautiful, radiant space, with golden light around you.",
              "See yourself surrounded by Kubera, the divine treasurer, Goddess Lakshmi and wise elders, all smiling at you as if blessing your actions.",
              "Feel honour, respect and growth radiating from you, blessing your family, your community and beyond.",
              "Meditate on this affirmation: “May divine companionship, honour and splendour walk beside me. In this world and community where I live and act, may I earn respect and steady, righteous prosperity.”"],
  reflection="How do I define prosperity beyond wealth? Am I building a life where people will respect me long after I have left the room? What contribution can I make to my surroundings to make my success meaningful?",
  closing="This verse teaches us that prosperity is not just about gold in the vault. It is about honour in the heart, respect in the community and righteousness in action.",
 ),
 dict(
  n=8, slug="verse-8",
  deva="क्षुत्पिपासामलां ज्येष्ठामलक्ष्मीं नाशयाम्यहम्।<br>अभूतिमसमृद्धिं च सर्वां निर्णुद मे गृहात्॥",
  iast="Kṣut-pipāsā-malāṁ jyeṣṭhām alakṣmīṁ nāśayāmy aham,<br>Abhūtim asamṛddhiṁ ca sarvāṁ nirṇuda me gṛhāt.",
  title="Śrī Sūktam Verse 8 Meaning – Kṣutpipāsāmalāṁ Jyeṣṭhām Alakṣmīṁ Explained",
  desc="Śrī Sūktam Verse 8 (Kṣutpipāsāmalāṁ Jyeṣṭhām) with Devanāgarī, transliteration, word-by-word meaning, the removal of Alakṣmī, scarcity and stagnation from home and heart, and a short practice.",
  h1="Śrī Sūktam – Verse 8",
  sub="Kṣut-pipāsā-malāṁ – clearing scarcity and negativity from home and heart",
  words=[
   ("क्षुत्पिपासामलाम्","Kṣut-pipāsā-malāṁ","That which is impure due to hunger (kṣut) and thirst (pipāsā)","It also symbolises constant want, craving and dissatisfaction."),
   ("ज्येष्ठाम्","Jyeṣṭhām","The elder sister (of Lakshmi)","Jyeṣṭhā is the elder sister of Lakshmi. In symbolism, she represents poverty, misfortune and quarrelsomeness: Alakṣmī’s form."),
   ("अलक्ष्मीम्","Alakṣmīṁ","Misfortune","All forms of misfortune, scarcity, poverty and negativity."),
   ("नाशयाम्यहम्","Nāśayāmy aham","I destroy, remove and eliminate","Through this prayer and intention."),
   ("अभूतिम्","Abhūtim","Absence of prosperity; poverty",""),
   ("असमृद्धिं च","Asamṛddhiṁ ca","And lack of growth","Stagnation and failure."),
   ("सर्वाम्","Sarvāṁ","All of it, without exception",""),
   ("निर्णुद","Nirṇuda","Drive out, banish, remove forcefully",""),
   ("मे गृहात्","Me gṛhāt","From my home","My life, my household, my heart."),
  ],
  meaning="I remove and destroy all impurity born of hunger, thirst, craving and dissatisfaction, the misfortune represented by Jyeṣṭhā and Alakṣmī. I drive out all poverty, stagnation and failure from my home and my life, completely.",
  insights=[
   ("Kṣut-pipāsā: the root of lack","Hunger and thirst here are not just physical. They symbolise greed, dissatisfaction and endless wanting. Prosperity never stays in a place of constant craving and restlessness. If the mind is forever saying “I want this, I want that, it is not enough”, then no matter how much Lakshmi comes, she will not stay. Lakshmi loves peaceful, content spaces; a heart with a hole of dissatisfaction can never stay full. Reflection: am I living in contentment, or constantly feeling “not enough”?"),
   ("Jyeṣṭhā and Alakṣmī: energies of negativity","The verse teaches that misfortune and scarcity are energies. They can take root and spread if not consciously removed. Jyeṣṭhā Devī is considered the embodiment of quarrels, scarcity, dirt and negativity, the opposite of Lakshmi. Where there is constant complaining, fighting, discontent, laziness or carelessness, that energy takes over. Reflection: are there negative patterns, complaints or toxic habits in my home or mind that I need to drive out?"),
   ("Nāśayāmy aham: “I destroy”, not “I hope”","Notice the force of the words. It is a personal decision. You are not asking someone else to clean your space; you stand up and say, I will remove these energies from my mind, heart and home."),
   ("Abhūtim and Asamṛddhiṁ: poverty in every form","Not just poverty of money, but poverty of thought, love, creativity and possibility: poverty of wealth, of ideas, of relationships and of courage, and stagnation, being stuck in one place with no growth. Reflection: where am I tolerating “lack” in my thinking or surroundings?"),
   ("Nirṇuda: a forceful command","This is not a meek request. It is a command to banish. It is like saying, “Enough! I will not allow scarcity and negativity to live here any more,” and sweeping out the dust and shutting the door behind it. Sometimes prosperity comes when we stop tolerating scarcity-thinking and firmly remove doubt, fear and negativity."),
  ],
  meditation=["Close your eyes and visualise your home as a bright, clean space.",
              "Imagine all the dark clouds of fear, scarcity, complaints, laziness and negativity being swept out, like dust being thrown out of a sacred temple.",
              "Whisper with authority and conviction: “May all misfortune, stagnation and negativity leave my life now. My home and heart are sanctuaries of light, growth and abundance.”",
              "A simple practice: light a lamp in your home, in silence. Say aloud, “All scarcity, all doubt, all negativity, I ask you to leave. My home is now pure, blessed and filled with light.” Feel the shift in energy."],
  reflection="What patterns of scarcity, complaining or doubt do I need to stop tolerating? What clutter, mental, emotional or physical, do I need to clean from my home and mind? How can I cultivate a home environment that attracts divine abundance? In real life: if there is clutter in the house, clear it, because Lakshmi loves cleanliness and order. If there are negative conversations, gossip or complaints every day, stop them. If your mind has fear-based thoughts about money, replace them with faith-based affirmations. If you have been procrastinating, take a small, clear action.",
  closing="This verse teaches that before prosperity can truly reside, scarcity and negativity must be firmly removed. It is a cleansing, not just of home and surroundings but of mindset, attitude and heart-space. Before asking Lakshmi to enter, clean the inner temple. Remove restlessness, negativity, poverty-thinking, laziness and complaints. Then abundance flows like a river that never dries.",
 ),
 dict(
  n=9, slug="verse-9",
  deva="गन्धद्वारां दुराधर्षां नित्यपुष्टां करीषिणीम्।<br>ईश्वरीं सर्वभूतानां तामिहोपह्वये श्रियम्॥",
  iast="Gandha-dvārāṁ durādharṣāṁ nitya-puṣṭāṁ karīṣiṇīm,<br>Īśvarīṁ sarva-bhūtānāṁ tām ihopahvaye śriyam.",
  title="Śrī Sūktam Verse 9 Meaning – Gandhadvārāṁ Durādharṣāṁ Explained",
  desc="Śrī Sūktam Verse 9 (Gandhadvārāṁ Durādharṣāṁ) with Devanāgarī, transliteration, word-by-word meaning, the fragrance, invincibility and fruitfulness of Lakshmi, and a short meditation.",
  h1="Śrī Sūktam – Verse 9",
  sub="Gandha-dvārāṁ – the fragrant, invincible, ever-nourishing Goddess",
  words=[
   ("गन्धद्वाराम्","Gandha-dvārām","One whose presence is sensed by divine fragrance","One who is fragrant and subtle. This represents subtle presence, purity and auspiciousness. Wherever Lakshmi resides, there is a feeling of freshness and sacredness, like divine perfume."),
   ("दुराधर्षाम्","Durādharṣām","One who cannot be challenged or overcome; invincible","True abundance and divine grace are unshakeable by external negativity."),
   ("नित्यपुष्टाम्","Nitya-puṣṭām","Ever-nourishing and ever-flourishing","Real prosperity is continuous, self-renewing and never depleting."),
   ("करीषिणीम्","Karīṣiṇīm","The one who causes fertility, productivity and abundance","Especially connected with fertile land and cattle manure, symbols of nourishment in Vedic culture. It represents fruitfulness, growth and productivity."),
   ("ईश्वरीम्","Īśvarīm","The supreme ruler, the sovereign goddess","This line reminds us that Lakshmi is not just gentle and beautiful; she is supreme authority and power."),
   ("सर्वभूतानाम्","Sarva-bhūtānām","Of all beings","Belonging to and protecting all living creatures."),
   ("ताम्","Tām","Her",""),
   ("इह उपह्वये","Iha upahvaye","Here and now I invoke and call upon",""),
   ("श्रियम्","Śriyam","Goddess Lakshmi","The embodiment of prosperity and grace."),
  ],
  meaning="I invoke here and now that Goddess Śrī, whose presence is known by divine fragrance, who is invincible, ever-nourishing and ever-growing. She is the sovereign queen, protector of all beings, and the source of continuous abundance and fruitfulness.",
  insights=[
   ("Fragrance (Gandha-dvārām)","Lakshmi’s presence is not loud or ostentatious. It is sensed subtly, like fragrance in the air. Reflection: am I cultivating a quiet, fragrant presence in my actions and thoughts?"),
   ("Invincibility (Durādharṣām)","True wealth and grace cannot be shaken by challenges. Reflection: is my sense of abundance strong and rooted, or dependent on external conditions?"),
   ("Continuous nourishment (Nitya-puṣṭām)","Prosperity should not be a peak-and-valley game. Reflection: am I nurturing my resources, relationships and health consistently?"),
   ("Fruitfulness (Karīṣiṇīm)","True abundance is not stagnant. It grows, multiplies and benefits others."),
   ("Universal protector (Sarva-bhūtānām Īśvarīm)","The Goddess protects all. Prosperity that is good for everyone is blessed and sustained."),
  ],
  meditation=["Imagine a soft, divine fragrance filling your space.",
              "See Goddess Lakshmi seated on a radiant throne, unshakeable, powerful, gently smiling.",
              "Around her is flourishing greenery, fruits and flowing rivers, symbols of endless growth and productivity.",
              "Whisper softly within: “I invite you, O invincible, ever-nourishing, sovereign Goddess. May your presence fill my life with peace, fragrance, abundance and protection.”"],
  reflection="How can I make my prosperity “fragrant”: subtle, graceful and uplifting to those around me? Where in my life do I need to cultivate consistency (nitya-puṣṭām) rather than sporadic effort? Am I making my wealth and blessings fruitful for others too?",
  closing="This verse teaches that true prosperity is fragrant, unshakeable, ever-growing and protective. It is not flashy but felt quietly, a presence that nourishes all who come near.",
 ),
 dict(
  n=10, slug="verse-10",
  deva="मनसः काममाकूतिं वाचः सत्यमशीमहि।<br>पशूनां रूपमन्नस्य मयि श्रीः श्रयतां यशः॥",
  iast="Manasaḥ kāmam ākūtiṁ vācaḥ satyam aśīmahi,<br>Paśūnāṁ rūpam annasya mayi śrīḥ śrayatāṁ yaśaḥ.",
  title="Śrī Sūktam Verse 10 Meaning – Manasaḥ Kāmam Ākūtiṁ Explained",
  desc="Śrī Sūktam Verse 10 (Manasaḥ Kāmam Ākūtiṁ) with Devanāgarī, transliteration, word-by-word meaning, pure desires, truthful speech, nourishment and honour, and a short meditation.",
  h1="Śrī Sūktam – Verse 10",
  sub="Manasaḥ Kāmam – pure desires, truthful speech, enduring honour",
  words=[
   ("मनसः कामम्","Manasaḥ kāmam","The desires of the mind","Heartfelt wishes."),
   ("आकूतिम्","Ākūtiṁ","Intentions, noble aspirations and prayers",""),
   ("वाचः सत्यम्","Vācaḥ satyam","Truth in speech","The ability to speak with integrity and sincerity."),
   ("अशीमहि","Aśīmahi","May we possess, may we attain",""),
   ("पशूनां रूपम्","Paśūnāṁ rūpam","The beauty, health and abundance of cattle","Symbolising wealth, nourishment and sustenance in Vedic times."),
   ("अन्नस्य","Annasya","Of food, nourishment and sustenance",""),
   ("मयि","Mayi","In me, within me, in my life",""),
   ("श्रीः श्रयताम्","Śrīḥ śrayatāṁ","May Goddess Lakshmi reside; may prosperity dwell",""),
   ("यशः","Yaśaḥ","Honour, good reputation and glory",""),
  ],
  meaning="May the sincere desires and noble intentions of my heart be fulfilled; may my words always be truthful. May I possess the abundance of cattle, the beauty of nourishment, and may prosperity and honour permanently reside in my life.",
  insights=[
   ("Desire and intention (Manasaḥ kāmam ākūtiṁ)","The verse acknowledges that desires and intentions are natural, but they must be pure and noble. Reflection: are my desires aligned with good, or are they born of ego and restlessness?"),
   ("Truth in speech (Vācaḥ satyam)","True prosperity stands on the foundation of truthfulness and integrity. Reflection: do I honour my words? Is my speech gentle and truthful?"),
   ("Cattle and food (Paśūnāṁ rūpam annasya)","Symbolising abundance in nourishment, wealth and wellbeing. It also hints at prosperity that provides sustenance for oneself and others."),
   ("May prosperity and honour reside (Mayi śrīḥ śrayatāṁ yaśaḥ)","The prayer is for Lakshmi and honour to dwell within us, not fleetingly but permanently."),
  ],
  meditation=["Visualise sitting before Goddess Lakshmi.",
              "See her gently placing a lotus in your heart, representing truthful words, noble desires and fulfilled intentions.",
              "Visualise flowing streams of milk and grains around you, symbolising nourishment and plenty.",
              "Whisper inwardly: “May my desires be pure, my speech be truthful, and may prosperity and honour take shelter in my life always.”"],
  reflection="Are my daily intentions aligned with goodness and higher purpose? Do I consistently speak truthfully and with kindness? How can I make my abundance nourishing for myself and others?",
  closing="Prosperity is not just wealth. It is truth in speech, nobility in intention, fulfilment of righteous desires, good nourishment and enduring honour. This verse teaches us that prosperity is inseparable from pure desires, truthful speech, sincere effort, nourishment and honour.",
 ),
 dict(
  n=11, slug="verse-11",
  deva="कर्दमेन प्रजाभूता मयि सम्भव कर्दम।<br>श्रियं वासय मे कुले मातरं पद्ममालिनीम्॥",
  iast="Kardamena prajā-bhūtā mayi sambhava kardama,<br>Śriyaṁ vāsaya me kule mātaraṁ padma-mālinīm.",
  title="Śrī Sūktam Verse 11 Meaning – Kardamena Prajābhūtā Explained",
  desc="Śrī Sūktam Verse 11 (Kardamena Prajābhūtā) with Devanāgarī, transliteration, word-by-word meaning, Kardama, Lakshmi as the nurturing mother, and a short meditation.",
  h1="Śrī Sūktam – Verse 11",
  sub="Kardamena Prajābhūtā – Lakshmi as the nurturing mother",
  words=[
   ("कर्दमेन","Kardamena","By Kardama (symbolic of sacred fertility and abundance)","In Vedic lore, Kardama is associated with fertile earth and the nourishing power of creation. The word literally means mud or fertile soil. Many commentators also take Kardama as a sage, regarded as a son of Lakshmi, whom the verse asks to bring his mother to dwell in the family."),
   ("प्रजाभूता","Prajābhūtā","Having given rise to progeny, creation, abundance, flourishing life",""),
   ("मयि सम्भव","Mayi sambhava","Be present within me; arise in my life",""),
   ("कर्दम","Kardama","O divine force of fertility and abundance!",""),
   ("श्रियं वासय मे कुले","Śriyaṁ vāsaya me kule","May Goddess Lakshmi reside in my family, lineage and home",""),
   ("मातरं पद्ममालिनीम्","Mātaraṁ padma-mālinīm","The motherly form of Lakshmi, adorned with a garland of lotuses","Lotuses here represent beauty, purity and divine presence."),
  ],
  meaning="By the power of Kardama, the force of fertility and creation, may abundance arise within me. May Goddess Lakshmi, adorned with a garland of lotuses, take permanent residence in my family, my home and my lineage as a nurturing mother.",
  insights=[
   ("Kardama: the sacred, fertile force","It symbolises the pure, nourishing soil of effort, intention and divine grace. Reflection: am I cultivating the right “soil” in my actions and thoughts so that prosperity can take root and flourish?"),
   ("Prajābhūtā: creation and continuity","Prosperity is not just for oneself. It creates, multiplies and nourishes future generations."),
   ("Mayi sambhava: let abundance arise within me","Not from outside only, but from within, in character, conduct, intention and effort."),
   ("Lakshmi as the mother with a lotus garland","The image of Lakshmi here is soft, maternal, ever-nurturing and permanently present. This is not fleeting fortune, but motherly abundance that stays, protects and blesses."),
  ],
  meditation=["Imagine fertile, rich earth beneath you, full of life and nourishment.",
              "Visualise Goddess Lakshmi, radiant and gentle, adorned with a garland of fresh pink lotuses, entering your home with grace and serenity.",
              "Feel her presence settling in, as a protective, loving mother who will never leave.",
              "Whisper: “May the seeds I plant bear divine fruit. May abundance and beauty take residence in my home and heart.”"],
  reflection="Is my daily effort like rich, fertile soil, prepared for abundance to grow? How am I ensuring that my success and prosperity are nurturing those around me? Do I welcome beauty, grace and order in my surroundings, making my home a place where abundance wants to stay?",
  closing="This verse teaches that prosperity comes when we cultivate fertile conditions (effort, clarity and generosity) and invite abundance not as a guest, but as a motherly presence who stays and nurtures.",
 ),
 dict(
  n=12, slug="verse-12",
  deva="आपः सृजन्तु स्निग्धानि चिक्लीत वस मे गृहे।<br>नि च देवीं मातरं श्रियं वासय मे कुले॥",
  iast="Āpaḥ sṛjantu snigdhāni ciklīta vasa me gṛhe,<br>Ni ca devīṁ mātaraṁ śriyaṁ vāsaya me kule.",
  title="Śrī Sūktam Verse 12 Meaning – Āpaḥ Sṛjantu Snigdhāni Explained",
  desc="Śrī Sūktam Verse 12 (Āpaḥ Sṛjantu Snigdhāni) with Devanāgarī, transliteration, word-by-word meaning, the symbolism of water and softness, and a short meditation on a humble, settled presence.",
  h1="Śrī Sūktam – Verse 12",
  sub="Āpaḥ Sṛjantu – softness, sacred waters and a settled presence",
  words=[
   ("आपः","Āpaḥ","Waters, sacred waters","In Vedic thought, water is purity, life-force and flow."),
   ("सृजन्तु","Sṛjantu","May they create, bring forth, generate",""),
   ("स्निग्धानि","Snigdhāni","Soft, smooth, harmonious, full of affection and cohesion","It represents sweetness in relationships, softness in the heart, and kindness in speech and action."),
   ("चिक्लीत","Ciklīta","An ancient word for fertility, fragrance and richness","It also suggests stickiness or cohesion, everything that makes prosperity “cling” or stay with you. Many commentators take <em>Ciklīta</em> as a name, another son of Lakshmi after Kardama in the previous verse, who is addressed directly: “O Ciklīta, dwell in my home.”"),
   ("वस मे गृहे","Vasa me gṛhe","Dwell in my home","May abundance and sweetness live here."),
   ("नि च देवीम्","Ni ca devīṁ","And settle the Goddess firmly","<em>Ni</em> carries the sense of settling down firmly. The humble, close, divine presence in daily life is the Goddess we ask to be settled in the home."),
   ("मातरं श्रियम्","Mātaraṁ śriyaṁ","The motherly form of Śrī (Lakshmi)","Nurturing, compassionate and permanently present."),
   ("वासय मे कुले","Vāsaya me kule","Make her reside in my lineage; bless my family",""),
  ],
  meaning="May the sacred waters bring softness, harmony and sweetness into my life and home. O divine Mother Lakshmi, humble yet ever-present, adorned with grace and nurturing energy, dwell permanently in my family and bless my lineage with abundance and peace.",
  insights=[
   ("Water’s symbolism (Āpaḥ)","Flow, purity and cleansing. True prosperity flows gently. It is never rigid or forced."),
   ("Softness (Snigdhāni)","Wealth without gentleness becomes arrogance. This verse asks for abundance that comes with sweetness in behaviour, harmony in the home and kindness in interactions."),
   ("Ciklīta: the quality that makes prosperity “stick”","What makes prosperity stay? Contentment, humility, gratitude and righteous conduct. Without these, abundance comes but slips away."),
   ("A settled, humble presence (Ni ca devīṁ)","We ask not for loud displays of wealth, but for a humble, nourishing, constant divine presence that subtly blesses every corner of life."),
  ],
  meditation=["Close your eyes and imagine pure, crystal-clear water flowing through your home, washing away rigidity, cleansing old energy, and leaving behind softness, warmth and harmony.",
              "Visualise Goddess Lakshmi sitting quietly, like a gentle mother, in the heart of your home: calm, smiling, silently nurturing.",
              "Whisper within: “May abundance flow softly and sweetly. May it remain with me, humble and nourishing, blessing my family for generations.”"],
  reflection="Am I cultivating softness and kindness along with abundance? What qualities in me make prosperity “stick”: gratitude, humility, sharing? Does my home feel like a place where divine energy would love to stay?",
  closing="This verse teaches that prosperity is not a sudden guest. It is a quiet, gentle, nourishing presence that stays only where there is purity, softness, humility and care.",
 ),
 dict(
  n=13, slug="verse-13",
  deva="आर्द्रां पुष्करिणीं पुष्टिं पिङ्गलां पद्ममालिनीम्।<br>चन्द्रां हिरण्मयीं लक्ष्मीं जातवेदो म आवह॥",
  iast="Ārdrāṁ puṣkariṇīṁ puṣṭiṁ piṅgalāṁ padma-mālinīm,<br>Chandrāṁ hiraṇmayīṁ lakṣmīṁ jāta-vedo ma āvaha.",
  title="Śrī Sūktam Verse 13 Meaning – Ārdrāṁ Puṣkariṇīṁ Puṣṭiṁ Explained",
  desc="Śrī Sūktam Verse 13 (Ārdrāṁ Puṣkariṇīṁ) with Devanāgarī, transliteration, word-by-word meaning, the tender, nourishing, golden Lakshmi of the lotus lake, and a short meditation.",
  h1="Śrī Sūktam – Verse 13",
  sub="Ārdrāṁ Puṣkariṇīṁ – tender, nourishing, golden",
  words=[
   ("आर्द्राम्","Ārdrām","Moist, tender, compassionate, nurturing","Lakshmi’s presence is soft and nourishing, never dry or harsh."),
   ("पुष्करिणीम्","Puṣkariṇīṁ","One who dwells in lotus-filled lakes","A source of purity and beauty."),
   ("पुष्टिम्","Puṣṭiṁ","Fullness, nourishment, flourishing health and prosperity",""),
   ("पिङ्गलाम्","Piṅgalām","Golden-hued, shining with warmth and radiance",""),
   ("पद्ममालिनीम्","Padma-mālinīm","Adorned with a garland of lotuses","Symbolising divine beauty and purity."),
   ("चन्द्राम्","Chandrāṁ","Shining and gladdening, moon-like","Radiant and soothing like the moon."),
   ("हिरण्मयीम्","Hiraṇmayīṁ","Golden, lustrous, and filled with divine glow",""),
   ("लक्ष्मीम्","Lakṣmīṁ","Goddess of prosperity, beauty, grace and abundance",""),
   ("जातवेदो म आवह","Jātavedo ma āvaha","O Agni (Jātaveda, divine fire), please bring her to me","Invite this divine presence into my life."),
  ],
  meaning="O Jātaveda (sacred fire), please bring into my life that tender, nurturing, lotus-dwelling Goddess Lakshmi, who is full of nourishment, golden-hued, adorned with lotuses, radiant like the moon, and glowing with divine brilliance.",
  insights=[
   ("Ārdrām: softness and compassion","Prosperity is beautiful only when it is tender, caring and filled with empathy."),
   ("Puṣkariṇīṁ: a lake filled with lotuses","It symbolises purity, serenity and peace. True abundance is as peaceful and beautiful as a still lake filled with flowers."),
   ("Puṣṭiṁ: nourishment","Without nourishment of body, mind and soul, wealth is hollow."),
   ("Piṅgalām and Hiraṇmayīṁ: golden glow","Prosperity should make life warm, bright and inviting, like the warm glow of gold or the soft light of the moon."),
   ("Agni as the messenger (Jātaveda)","We once again ask the sacred fire, the purifier and messenger, to invite this divine presence into our lives."),
  ],
  meditation=["Close your eyes and visualise a serene lake, covered in soft pink lotuses, glowing under moonlight.",
              "See Goddess Lakshmi rising from this lake: golden, radiant, wearing a lotus garland, her eyes filled with compassion and warmth.",
              "Whisper inwardly: “May this tenderness, nourishment and brilliance flow into my home and heart, and dwell here always.”"],
  reflection="Am I cultivating softness and grace along with strength and ambition? Does my abundance radiate beauty and nourish others? Can I bring more calm, peaceful energy into my home and work, like the stillness of a lotus lake?",
  closing="This verse teaches that prosperity is not only power. It is gentle, radiant, nourishing beauty that brings peace and fulfilment.",
 ),
 dict(
  n=14, slug="verse-14",
  deva="आर्द्रां यः करिणीं यष्टिं सुवर्णां हेममालिनीम्।<br>सूर्यां हिरण्मयीं लक्ष्मीं जातवेदो म आवह॥",
  iast="Ārdrāṁ yaḥ kariṇīṁ yaṣṭiṁ suvarṇāṁ hema-mālinīm,<br>Sūryāṁ hiraṇmayīṁ lakṣmīṁ jāta-vedo ma āvaha.",
  title="Śrī Sūktam Verse 14 Meaning – Ārdrāṁ Yaḥ Kariṇīṁ Yaṣṭiṁ Explained",
  desc="Śrī Sūktam Verse 14 (Ārdrāṁ Yaḥ Kariṇīṁ Yaṣṭiṁ) with Devanāgarī, transliteration, word-by-word meaning, the tender, active, sun-bright Lakshmi, and reflection questions.",
  h1="Śrī Sūktam – Verse 14",
  sub="Ārdrāṁ Yaḥ Kariṇīṁ – tender, active and sun-bright",
  words=[
   ("आर्द्राम्","Ārdrām","Tender, compassionate, soft","She who keeps life moist and nourished, like rain on dry ground."),
   ("यः करिणीम्","Yaḥ kariṇīm","She who gives the strength to accomplish every kind of work","She is the source of activity and movement in life. This is one of the harder phrases of the hymn, and commentators differ; another traditional reading takes <em>kariṇī</em> as “attended by elephants”."),
   ("यष्टिम्","Yaṣṭiṁ","The power joined with resolve, worship and austerity","The strength that comes as the lasting fruit of sustained practice and gives stability in life. The word also means a staff, a support."),
   ("सुवर्णाम्","Suvarṇām","Golden, shining with a pure, bright glow",""),
   ("हेममालिनीम्","Hema-mālinīm","Adorned with a garland of gold","A symbol of splendour, grace and dignity."),
   ("सूर्याम्","Sūryām","Radiant like the sun, life-giving","The sun’s brilliance never fails; it gives energy and strength continuously. In Verse 13 she was moon-like (<em>Chandrā</em>); here she is sun-like. Together they bring coolness and fire, gentleness and power."),
   ("हिरण्मयीम्","Hiraṇmayīṁ","Golden in brilliance, filled with divine radiance",""),
   ("लक्ष्मीम्","Lakṣmīṁ","Mother Lakshmi","The Goddess of prosperity, beauty, grace and splendour."),
   ("जातवेदो म आवह","Jātavedo ma āvaha","O Agni, knower of all births, please bring this divine Lakshmi into my life",""),
  ],
  meaning="O Agni, please invite into my life that Goddess Lakshmi who is tender and compassionate, the power that brings every undertaking to fulfilment, who shines like gold, wears a garland of gold, is radiant like the sun, and is filled with divine brilliance.",
  insights=[
   ("Tenderness and compassion (Ārdrām)","Wealth is not only hard power; it should carry gentleness, kindness and love as well. Only then does it last."),
   ("Action and resolve (Yaḥ kariṇīm, Yaṣṭiṁ)","Lakshmi dwells where there is action and resolve: where there is no laziness, but steady effort and practice."),
   ("Beauty and radiance (Suvarṇām, Hema-mālinīm, Sūryām, Hiraṇmayīṁ)","Prosperity is not only material wealth. It is the beauty of life, a touch of the divine and an inner light that shines by itself and lights up others too."),
   ("The invitation (Jātavedo ma āvaha)","Through Agni, the power of the self, we call Goddess Lakshmi. Calling her is not just reciting a mantra; it is an inner preparation."),
  ],
  meditation=["Close your eyes and imagine the first light of dawn, soft and warm, spreading slowly across a still sky.",
              "See Mother Lakshmi in that light: gentle eyes full of compassion, a garland of gold on her shoulders, her whole form shining like the rising sun.",
              "Feel her radiance reach your heart and wake up your own resolve, steady and unhurried, ready to act.",
              "Whisper inwardly: “O Mother, let tenderness and strength, compassion and effort, shine together in me, and may your light stay in my life.”"],
  reflection="Is the radiance of Lakshmi in my life only outside, or inside as well? Am I making my action and resolve pure and strong enough for Lakshmi to stay in my life? Do I have the compassion and beauty within that can make wealth sacred?",
  closing="This verse teaches that prosperity is tender and active at once. It shines like the sun, but it stays only where there is compassion in the heart and steady, sincere effort in the hands.",
 ),
 dict(
  n=15, slug="verse-15",
  deva="तां म आवह जातवेदो लक्ष्मीमनपगामिनीम्।<br>यस्यां हिरण्यं प्रभूतं गावो दास्यो अश्वान्विन्देयं पुरुषानहम्॥",
  iast="Tāṁ ma āvaha jāta-vedo lakṣmīm anapagāminīm,<br>Yasyāṁ hiraṇyaṁ prabhūtaṁ gāvo dāsyo aśvān vindeyaṁ puruṣān aham.",
  title="Śrī Sūktam Verse 15 Meaning – Tāṁ Ma Āvaha Prabhūtaṁ Explained",
  desc="Śrī Sūktam Verse 15 (Tāṁ Ma Āvaha, the closing verse) with Devanāgarī, transliteration, word-by-word meaning, lasting prosperity, support and good company, and a short meditation.",
  h1="Śrī Sūktam – Verse 15",
  sub="Tāṁ Ma Āvaha – the closing invocation of lasting prosperity",
  words=[
   ("तां","Tāṁ","Her (that Goddess Lakshmi)",""),
   ("म आवह","Ma āvaha","Invite her for me; bring her",""),
   ("जातवेदः","Jātavedo","O Agni, knower of all births",""),
   ("लक्ष्मीम्","Lakṣmīm","Goddess Lakshmi","The Goddess of prosperity and beauty."),
   ("अनपगामिनीम्","Anapagāminīm","One who never goes away; one who stays always",""),
   ("यस्याम्","Yasyāṁ","With whom; in whose presence",""),
   ("हिरण्यं प्रभूतम्","Hiraṇyaṁ prabhūtam","Gold and splendour in abundance",""),
   ("गावः","Gāvaḥ","Cows","A symbol of prosperity and nourishment."),
   ("दास्यः","Dāsyaḥ","Attendants, those who help","Meaning cooperation and support."),
   ("अश्वान्","Aśvān","Horses","Symbols of strength, speed and progress."),
   ("विन्देयम्","Vindeyaṁ","May I obtain",""),
   ("पुरुषान् अहम्","Puruṣān aham","Good, excellent, virtuous people","Good people and good company."),
  ],
  meaning="O Jātaveda (Agni), please invite into my life Mother Lakshmi, who never goes away and always stays with me. In her presence may I obtain gold and splendour in abundance, cows (nourishment), attendants (support), horses (strength and progress), and the company of excellent people. This closing verse returns to the invocation of Verse 2.",
  insights=[
   ("Lasting Lakshmi (Anapagāminīm)","This is a very important word. We are not asking for temporary pleasure, but inviting lasting prosperity and inner peace."),
   ("Gold in abundance (Hiraṇyaṁ prabhūtam)","But this gold is not only outer wealth. It is also a symbol of knowledge, brightness, good judgement and divine radiance."),
   ("Cows, helpers and horses (Gāvaḥ, Dāsyaḥ, Aśvān): nourishment, support and strength","Prosperity lasts only when we have nourishment, cooperation and the means of progress."),
   ("Good company (Puruṣān aham)","This is very important. Lakshmi stays only when our company is excellent, positive and uplifting."),
  ],
  meditation=["Close your eyes and imagine a golden radiance coming towards you, as the lasting presence of Mother Lakshmi.",
              "With her come abundance, help, strength, and excellent guides and companions in life.",
              "Slowly say within your heart: “O Mother Lakshmi, may you remain in my life, and give me auspiciousness, strength, cooperation and right guidance.”"],
  reflection="Do I want only wealth, or wealth that lasts and brings growth? Is my life limited to material prosperity, or do I also pay attention to cooperation, strength and good company? Am I removing instability from my life and bringing steadiness and balance?",
  closing="",
 ),
 dict(
  n=16, slug="verse-16",
  deva="यः शुचिः प्रयतो भूत्वा जुहुयादाज्यमन्वहम्।<br>श्रियः पञ्चदशर्चं च श्रीकामः सततं जपेत्॥",
  iast="Yaḥ śuciḥ prayato bhūtvā juhuyād ājyam anvaham,<br>Śriyaḥ pañcadaśarcaṁ ca śrīkāmaḥ satataṁ japet.",
  title="Śrī Sūktam Verse 16 (Phalaśruti) Meaning – Yaḥ Śuciḥ Prayato Bhūtvā Explained",
  desc="Śrī Sūktam Verse 16, the phalaśruti (Yaḥ Śuciḥ Prayato Bhūtvā) with Devanāgarī, transliteration, word-by-word meaning, the fruit of reciting the fifteen verses, and a closing meditation.",
  h1="Śrī Sūktam – Verse 16",
  sub="Yaḥ Śuciḥ Prayato Bhūtvā – the phalaśruti, the fruit of reciting the hymn",
  words=[
   ("यः शुचिः प्रयतः भूत्वा","Yaḥ śuciḥ prayataḥ bhūtvā","One who, becoming pure, with a clean mind and self-restraint",""),
   ("जुहुयात् आज्यम् अन्वहम्","Juhuyāt ājyam anvaham","Should offer ghee into the sacred fire every day","The daily fire offering (<em>agnihotra</em>)."),
   ("श्रियः पञ्चदशर्चं च","Śriyaḥ pañcadaśarcaṁ ca","And the fifteen verses of the Śrī Sūktam","Recited every day."),
   ("श्रीकामः सततं जपेत्","Śrīkāmaḥ satataṁ japet","One who desires Lakshmi should keep reciting it continuously",""),
  ],
  meaning="The person who becomes pure and self-restrained, offers ghee into the sacred fire every day, and recites the fifteen verses of the Śrī Sūktam with faith, receives the special grace of Śrī Lakshmi. Such a person gains both material and spiritual prosperity.",
  insights=[
   ("More than asking","This closing part does not teach us only to ask. It tells us that discipline, self-restraint and pure conduct are what make Mother Lakshmi’s grace lasting."),
   ("A daily practice","It says that for Lakshmi there must be a daily practice: a pure heart, regular recitation, the offering of one’s own duty and work, and true faith."),
  ],
  meditation=["Close your eyes.",
              "Imagine Mother Lakshmi, calm and gentle, surrounded by a golden glow, seated in the temple of your heart.",
              "At her feet are lotuses, and from her hands a steady stream of gold, knowledge and peace flows into your life.",
              "Say softly: “O Mother Lakshmi, make me worthy of pure conduct, self-restraint, good deeds and your continuous grace.”"],
  reflection="",
  closing="Mother Lakshmi is not called by words alone. To call her we need clean conduct, a disciplined life, service, good company and daily practice. Then she not only comes; she stays.",
 ),
]
TOTAL_SRI = 16  # 15 verses of the hymn plus the closing phalaśruti, numbered Verse 16 here

KANA_TOTAL = 22  # popular edition; the verse count is confirmed on the Kanakadhāra page once the edition is settled

KVERSES = [
 dict(
  n=1, slug="verse-1",
  deva="अङ्गं हरेः पुलकभूषणमाश्रयन्ती<br>भृङ्गाङ्गनेव मुकुलाभरणं तमालम्।<br>अङ्गीकृताखिलविभूतिरपाङ्गलीला<br>माङ्गल्यदास्तु मम मङ्गलदेवतायाः॥",
  iast="Aṅgaṁ hareḥ pulaka-bhūṣaṇam āśrayantī,<br>Bhṛṅgāṅganeva mukulābharaṇaṁ tamālam;<br>Aṅgīkṛtākhila-vibhūtir apāṅga-līlā,<br>Māṅgalya-dāstu mama maṅgala-devatāyāḥ.",
  title="Kanakadhāra Stotram Verse 1 Meaning – Aṅgaṁ Hareḥ Pulaka-Bhūṣaṇam Explained",
  desc="Kanakadhāra Stotram Verse 1 (Aṅgaṁ Hareḥ Pulaka-Bhūṣaṇam) with Devanāgarī, transliteration, word-by-word meaning, the sidelong glance of Mahalakshmi, the bee and the tamāla tree, and a short meditation.",
  h1="Kanakadhāra Stotram – Verse 1",
  sub="Aṅgaṁ Hareḥ – the divine glance of Mahālakṣmī",
  words=[
   ("अङ्गं हरेः","Aṅgaṁ hareḥ","The body of Hari (Lord Vishnu)","<em>Aṅga</em> means body or limb; <em>hareḥ</em> is “of Hari”, a name of Vishnu."),
   ("पुलकभूषणम्","Pulaka-bhūṣaṇam","Having goosebumps as its ornament","<em>Pulaka</em> is the goosebumps that rise from intense emotion; <em>bhūṣaṇa</em> is an ornament. Together: goosebumps that become ornaments."),
   ("आश्रयन्ती","Āśrayantī","Resting upon, taking refuge in","The glance rests upon the body of the Lord."),
   ("भृङ्गाङ्गना इव","Bhṛṅgāṅganā iva","Like a female bee","<em>Bhṛṅga</em> is a bee and <em>aṅganā</em> a woman or female figure; <em>iva</em> means “like” or “as”."),
   ("मुकुलाभरणं तमालम्","Mukulābharaṇaṁ tamālam","A tamāla tree adorned with flower buds","<em>Mukula</em> is a flower bud and <em>ābharaṇa</em> an ornament. The <em>tamāla</em> is a tree traditionally associated with a dark complexion."),
   ("अङ्गीकृताखिलविभूतिः","Aṅgīkṛtākhila-vibhūtiḥ","That which has embraced all glories and powers","<em>Aṅgīkṛta</em> is accepted or embraced as one’s own; <em>akhila</em> is all; <em>vibhūti</em> is glory, power, excellence."),
   ("अपाङ्गलीला","Apāṅga-līlā","The graceful play of a sidelong glance","<em>Apāṅga</em> is the corner of the eye, a sidelong glance; <em>līlā</em> is play or graceful action."),
   ("माङ्गल्यदा अस्तु मम","Māṅgalyadā astu mama","May it bestow auspiciousness on me","<em>Māṅgalyadā</em> is “giver of auspiciousness”; <em>astu</em> is “may it be”; <em>mama</em> is “for me”."),
   ("मङ्गलदेवतायाः","Maṅgala-devatāyāḥ","Of the Goddess of auspiciousness","Lakshmi, whose glance is the subject of the prayer."),
  ],
  meaning="May the graceful sidelong glance of Goddess Mahalakshmi, which lovingly rests upon the dark, beautiful form of Lord Vishnu and makes His body thrill with divine joy; which moves like a bee among the flower buds adorning a tamāla tree; and which embraces every form of divine glory and prosperity: may that sacred glance of the Goddess of Auspiciousness bless my life with good fortune and well-being.",
  insights=[
   ("In simple words","“O Mother Mahalakshmi, your glance is filled with such love and grace that even Lord Vishnu’s body thrills with joy when you look upon Him. Your beauty is like a bee moving among flower buds on a dark tree, and you embody every form of divine glory. May your compassionate glance fall upon me and bring auspiciousness into my life.” The central prayer is not simply for gold. It is for the grace of the Goddess who embodies auspiciousness."),
   ("The poetry hidden in the first line","Ādi Śaṅkarācārya could have simply written, “Lakshmi looked at Vishnu.” Instead he paints a whole picture. Imagine it: Vishnu stands serene, dark as a monsoon cloud. Lakshmi turns toward Him. She does not stare; she gives only a gentle glance from the corner of her eye. That glance is filled with so much love that His body is covered in goosebumps of divine bliss, sparkling like jewels. A poet sees what ordinary eyes miss."),
   ("Goosebumps as ornaments (Pulaka-bhūṣaṇam)","Ordinarily we adorn the body with gold, pearls and precious stones. Here the poet imagines something more beautiful: divine love itself becomes the ornament. Vishnu needs no jewellery to be magnificent; the joy awakened by Lakshmi’s glance adorns Him. The phrase turns an invisible feeling into a visible image. There is a gentle lesson in it for us too: the deepest forms of beauty are not always things we can purchase or possess. Sometimes they are the traces of love, devotion and joy that show in a person."),
   ("The bee and the tamāla tree","The second line extends the painting. Imagine a dark tamāla tree, its branches adorned with delicate flower buds, and a bee moving gracefully among them. The poet compares Lakshmi’s glance to this bee and Vishnu’s dark form to the tamāla tree. A bee is drawn to flowers; its movement is delicate and graceful. In the same way her glance brings movement and tenderness to the picture of Vishnu’s serene form. Traditionally Lakshmi and Vishnu are also seen as inseparable, their relationship expressing divine harmony. It helps to keep the layers apart: the bee and the tree are the verse’s own imagery, while inseparability and harmony are spiritual interpretations we draw from it."),
   ("The most important word: Apāṅga","<em>Apāṅga</em> is the corner of the eye, a sidelong glance. Why not simply say that Lakshmi looks at Vishnu? Because the sidelong glance adds delicacy, intimacy and grace. In classical Indian aesthetics the eyes are powerful instruments of expression: a glance can carry affection, shyness, compassion, longing or delight without a word. In devotional language a deity’s <em>kaṭākṣa</em>, a gracious glance, is a symbol of divine favour. The devotee is not merely asking to be seen. The devotee longs to receive compassionate attention."),
   ("Seek the giver, not merely the gift","The verse ends with a prayer for auspiciousness, not for a specific quantity of gold. The poet turns our attention to the Goddess herself. We may ask for material prosperity, but we can also seek the wisdom, integrity and grace that make prosperity meaningful."),
   ("Prosperity is broader than money","The word <em>vibhūti</em> evokes glory, power and excellence. We can think of prosperity as including material resources along with knowledge, good judgement, courage, generosity and contentment. These wider applications are philosophical reflections inspired by the verse, not a literal list contained in it."),
   ("Love is itself an adornment","<em>Pulaka-bhūṣaṇam</em> reminds us that emotion changes how we see beauty. A person adorned with jewels may be impressive; a person whose face shines with love, joy and compassion has a different kind of beauty. The verse invites us to appreciate both."),
   ("Grace and effort belong together","The prayer asks for divine auspiciousness. In a practical reading, prayer need not replace effort; it can guide it. We may pray for prosperity while working honestly, managing resources prudently, learning continuously and helping others where we can. Devotion gives direction to effort; effort gives practical expression to our intentions."),
   ("How to pronounce the key words","Aṅgam: ang-gam. Hareḥ: ha-reh, ending in a soft breath. Pulaka: pu-la-ka. Bhūṣaṇam: bhoo-sha-nam. Bhṛṅgāṅganeva: bhring-gaan-ga-ne-va. Apāṅgalīlā: a-paan-ga-lee-laa. Māṅgalyadāstu: maang-gal-yaa-stu. Do not worry about mastering every sound at once; confidence grows gradually."),
  ],
  meditation=["Minute 1, become still: sit comfortably and breathe naturally. Let your attention settle without forcing the mind to become completely silent.",
              "Minutes 2–3, visualise the poetry: imagine Lakshmi’s gentle glance resting upon Vishnu, and His joy shown as a natural radiance, as though His body were adorned by bliss. Recite the verse slowly, resting on <em>apāṅgalīlā</em>.".replace("<em>","").replace("</em>",""),
              "Minute 4, offer a prayer. Say silently: “O Mahalakshmi, may I recognise the blessings already present in my life. May I gain the wisdom to use my resources well and the generosity to share what I can.”",
              "Minute 5, carry the prayer into life: choose one action for today. Help someone, share knowledge, express gratitude, or make a thoughtful financial decision."],
  reflection="What adorns my life: is it merely what I possess, or also my conduct, relationships and inner qualities? Where does my attention rest: am I noticing opportunities for gratitude and goodness, or am I consumed by fear and comparison? What does auspiciousness mean to me: if prosperity came into my life tomorrow, what would make me use it wisely? Do not rush to answer; let one question stay with you through the day.",
  closing="The first verse joins the grace of Lakshmi, the joy of Vishnu and the beauty of nature in a single poetic moment. The bee, the flower buds, the dark tree, the goosebumps and the sidelong glance are not isolated decorations; they form one living picture of divine beauty and auspiciousness. And the prayer brings that image close to us: may that auspicious glance bless me. Prosperity is worth seeking, but also worth understanding. Wealth can fill a treasury; wisdom helps us use it. Possessions can adorn the body; love and goodness adorn the life. This meditation is a devotional practice for attention and reflection; it does not promise a supernatural result or guarantee material wealth.",
 ),
 dict(
  n=2, slug="verse-2",
  deva="मुग्धा मुहुर्विदधती वदने मुरारेः<br>प्रेमत्रपाप्रणिहितानि गतागतानि।<br>माला दृशोर्मधुकरीव महोत्पले या<br>सा मे श्रियं दिशतु सागरसम्भवायाः॥",
  iast="Mugdhā muhur vidadhatī vadane Murāreḥ,<br>Prema-trapā-praṇihitāni gatāgatāni;<br>Mālā dṛśor madhukarīva mahotpale yā,<br>Sā me śriyaṁ diśatu sāgara-sambhavāyāḥ.",
  title="Kanakadhāra Stotram Verse 2 Meaning – Mugdhā Muhur Vidadhatī Explained",
  desc="Kanakadhāra Stotram Verse 2 (Mugdhā Muhur Vidadhatī) with Devanāgarī, transliteration, word-by-word meaning, the garland of glances, the bee and the great lotus, Lakshmi born of the ocean, and a short meditation.",
  h1="Kanakadhāra Stotram – Verse 2",
  sub="Mugdhā Muhur – the garland of loving glances",
  words=[
   ("मुग्धा","Mugdhā","Charming, lovely, innocent, bashful","A description of the Goddess herself."),
   ("मुहुः विदधती","Muhuḥ vidadhatī","Again and again casting, directing","<em>Muhuḥ</em> is “again and again”; <em>vidadhatī</em> is making, performing or displaying."),
   ("वदने मुरारेः","Vadane Murāreḥ","Upon the face of Murāri (Vishnu)","<em>Murāri</em> means the foe of Mura, a name of Vishnu, who slew the demon Mura."),
   ("प्रेमत्रपाप्रणिहितानि","Prema-trapā-praṇihitāni","Glances directed with love and bashfulness","<em>Prema</em> is love; <em>trapā</em> is bashfulness or modesty; <em>praṇihita</em> is directed, placed, fixed upon."),
   ("गतागतानि","Gatāgatāni","Going and coming","Glances that go and return, repeated movements. The word gives movement to the poem."),
   ("माला दृशोः","Mālā dṛśoḥ","A garland of the eyes, of the glances","<em>Mālā</em> is a garland; <em>dṛśoḥ</em> is “of the two eyes”. The poetic centre of the verse: her repeated glances become a garland."),
   ("मधुकरी इव","Madhukarī iva","Like a female bee","<em>Madhukarī</em> is “she who makes honey”, a female bee."),
   ("महोत्पले","Mahotpale","On a great lotus","<em>Mahā</em> is great and <em>utpala</em> is a lotus, often a blue lotus."),
   ("या सा","Yā sā","She who… may she","<em>Yā</em> (“who”) and <em>sā</em> (“she”) hold the sentence together: the Goddess who is described, and the same Goddess who is asked."),
   ("मे श्रियं दिशतु","Me śriyaṁ diśatu","May she grant me Śrī","<em>Śrī</em> is prosperity, good fortune, beauty and auspiciousness; <em>diśatu</em> is “may she grant”."),
   ("सागरसम्भवायाः","Sāgara-sambhavāyāḥ","Of her who was born from the ocean","Lakshmi, who emerged at the churning of the ocean."),
  ],
  meaning="The lovely, bashful Goddess, born from the ocean, again and again directs towards the face of Murāri glances that come and go, full of love and modesty. Her glances move like a garland, like a female bee around a great lotus. May that Goddess Lakshmi grant me Śrī: prosperity, beauty, good fortune and auspiciousness.",
  insights=[
   ("In simple words","“O Mother Lakshmi, your eyes are full of love and gentle bashfulness as you look again and again towards Lord Vishnu’s face. Your glances move like bees drawn to a magnificent lotus. O Daughter of the Ocean, bless me with Śrī: with prosperity, grace and auspiciousness.” In Verse 1 we contemplated the power of a single sidelong glance. Verse 2 shows a repeated exchange of glances, full of love and modesty. The first verse presents the beauty of divine grace; the second brings us closer to the emotional intimacy of the Divine Couple."),
   ("The poetry hidden in Verse 2","Ādi Śaṅkarācārya could have written, “Lakshmi looks lovingly at Vishnu.” Instead he gives a whole scene of glances that come and go, each carrying a delicate emotion. Imagine Vishnu, calm and magnificent, with the serene beauty of a blue lotus. Lakshmi looks towards His face. Her eyes linger for a moment; then, out of modesty, they turn away; and then they return. Again and again. There is love in the glance, and also <em>trapā</em>, a beautiful reserve. The poet does not need to describe a conversation; their eyes speak for them. A poet sees what ordinary eyes miss."),
   ("The emotional genius of the verse","Look at the sequence. The lotus is the image of beauty, freshness and attraction. The bee is drawn to the flower again and again and moves around it. The glance returns again and again, carrying love and bashfulness. The bee’s repeated movement gives us a visual language for the movement of Lakshmi’s eyes. The lotus attracts the bee, and the face of Vishnu draws Lakshmi’s loving attention. The comparison is not merely decorative; it makes the feeling visible."),
   ("A subtle distinction from Verse 1","In the first verse the bee image evokes Lakshmi’s graceful movement around Vishnu’s dark, tamāla-like form. In the second, the great lotus becomes the focus: her glances are a garland, like a bee at that lotus. The imagery develops from one verse to the next, but its emotional centre stays the same: the beauty of the Divine Couple and the grace the poet seeks from Lakshmi."),
   ("Love and modesty can coexist","<em>Prema-trapā</em> is one of the most tender expressions in the verse. <em>Prema</em> is love and <em>trapā</em> is bashfulness. The Goddess is not portrayed as distant or impersonal: her glances express affection and still keep a graceful reserve. Love does not always need grand declarations; sometimes tenderness is expressed through restraint, attention and quiet presence. This is a poetic picture of divine love, not a rule that everyone must express affection through shyness."),
   ("The garland of glances","A garland is made by bringing individual flowers together. Here the poet imagines individual glances as a garland: each glance is a moment of affection, and together they become a continuous expression of love. Repeated acts of attention can form something beautiful. In everyday life a relationship is rarely sustained by one grand gesture; it is sustained by many small ones: listening, remembering, caring, forgiving and showing up."),
   ("Why the lotus?","The lotus holds a special place in Indian spiritual and literary traditions. It suggests beauty, purity, freshness and the possibility of flourishing even in muddy water, and it is deeply associated with Lakshmi herself. In this verse, however, the lotus is part of a specific comparison: the bee is drawn to the great lotus just as Lakshmi’s glances turn again and again towards Vishnu’s face. It helps to appreciate both layers, the immediate image and the wider symbolism, without confusing the two."),
   ("Why ask for Śrī?","The verse ends with a direct prayer: <em>Sā me śriyaṁ diśatu</em>, “May she grant me Śrī.” It is a beautiful progression from describing the Goddess to addressing her grace. <em>Śrī</em> can mean prosperity, splendour, beauty, good fortune and auspiciousness, so the prayer is broad enough to invite thought about prosperity in its many forms: material well-being, the discernment to use resources wisely, the character to act ethically and the contentment to recognise what is already good. That wider application is a reflection inspired by the verse, not a literal list of meanings in the Sanskrit."),
   ("Lakshmi as Sāgarasambhavā","<em>Sāgara-sambhavāyāḥ</em> refers to her who was born from the ocean. In Hindu tradition Lakshmi is associated with the Samudra Manthana, the churning of the cosmic ocean, when she emerged from the ocean of milk and was welcomed by the gods; the account appears in different forms across the Purāṇas. Why does Śaṅkara invoke this identity? He reminds us of her cosmic origin. She is not only a beautiful figure in an intimate scene with Vishnu; she is the revered Goddess born from the cosmic ocean, associated with auspiciousness and prosperity. There is a poetic contrast between the vastness of the ocean and the delicacy of a glance. From a cosmic event the poet brings us to a deeply personal prayer: may she grant me Śrī. The universe is vast, yet devotion makes the prayer intimate."),
   ("How to pronounce the key words","Mugdhā: mug-dhaa. Muhuḥ: muhur, “again and again”. Murāreḥ: mu-raa-reh. Prema-trapā: pre-ma-tra-paa. Gatāgatāni: ga-taa-ga-taa-ni. Madhukarī: ma-dhu-ka-ree. Mahotpale: ma-hot-pa-le. Sāgarasambhavāyāḥ: saa-ga-ra-sam-bha-vaa-yaah. One small lesson: when words are joined in a verse their sounds often change slightly. This is called <em>sandhi</em>. We will gradually learn to recognise these joins so that grammar never becomes a barrier to enjoying the poetry."),
  ],
  meditation=["Minute 1, become still: sit comfortably, breathe gently and let the day’s concerns settle. You do not need to empty your mind; simply allow yourself to be present.",
              "Minutes 2–3, recite the verse: read the Sanskrit slowly, resting on prematrapāpraṇihitāni gatāgatāni. Recall the meaning: glances directed with love and bashfulness, moving back and forth.",
              "Minute 4, visualise the scene: imagine a magnificent lotus with a bee gently moving around it. Then picture Lakshmi’s loving glance turning towards Vishnu and returning again. Let the image remind you of tenderness, attention and harmony.",
              "Minute 5, offer your prayer. Say silently: “O Mother Lakshmi, may my attention be loving, my conduct graceful and my understanding of prosperity wise. May I recognise and nurture the goodness already present in my life.”"],
  reflection="Where does my attention return, again and again? The bee returns to the lotus; Lakshmi’s glance returns to Vishnu. Our attention also returns to certain things: sometimes to worry, sometimes to ambition, sometimes to gratitude, sometimes to the people we love. Repeated attention gradually shapes our inner world. What occupies my thoughts most often: fear of losing what I have, desire for what I lack, or gratitude for what I possess? Do the people important to me receive my attention in small, consistent ways? If I seek prosperity, am I also cultivating the qualities that will let me use it wisely? I need not answer every question today; I can choose the one that speaks to me most deeply.",
  closing="Lakshmi looks towards Vishnu. Her eyes move away and return, carrying both love and modesty, and the poet sees these repeated glances as a garland of bees around a magnificent lotus. Then he makes his prayer: may the Goddess born from the ocean grant me Śrī. Verse 1 taught us to contemplate the power of the divine glance; Verse 2 invites us to contemplate its tenderness, the affection, the repeated attention and the beauty of a relationship expressed without words. What we return to, again and again, becomes an important part of our lives. May we return to wisdom when confused, gratitude when restless, integrity when tempted and compassion when dealing with others. This meditation is a devotional practice for attention and reflection; it does not promise a supernatural result or guarantee material wealth.",
 ),
]


MLA_D = "This meditation is a devotional practice for attention and reflection; it does not promise a supernatural result or guarantee material wealth."

MVERSES = [
 dict(n=1, slug="verse-1",
  deva="नमस्तेऽस्तु महामाये श्रीपीठे सुरपूजिते।<br>शङ्खचक्रगदाहस्ते महालक्ष्मि नमोऽस्तु ते॥",
  iast="Namas te 'stu mahāmāye śrīpīṭhe sura-pūjite,<br>Śaṅkha-cakra-gadā-haste mahālakṣmi namo 'stu te.",
  sub="Namas te ’stu Mahāmāye – the first bow",
  words=[
   ("नमः ते अस्तु","Namaḥ te astu","Salutation to you; may there be a bow to you","<em>Namaḥ</em> is a bow or salutation; <em>te</em> is “to you”; <em>astu</em> is “let it be”."),
   ("महामाये","Mahāmāye","O Great Māyā, great divine power","<em>Māyā</em> is the creative power by which the world appears. Here it is a title of honour, not a charge of deception."),
   ("श्रीपीठे","Śrīpīṭhe","O you who are seated at Śrīpīṭha, the seat of Śrī","<em>Pīṭha</em> is a seat or sacred centre. Tradition links this seat with Kolhapur; the phrase can also be read simply as “seat of prosperity”."),
   ("सुरपूजिते","Sura-pūjite","Worshipped by the gods","<em>Sura</em> is a god; <em>pūjita</em> is worshipped."),
   ("शङ्खचक्रगदाहस्ते","Śaṅkha-cakra-gadā-haste","Holding conch, discus and mace in her hands","<em>Śaṅkha</em> is the conch, <em>cakra</em> the discus, <em>gadā</em> the mace, <em>hasta</em> the hand."),
   ("महालक्ष्मि","Mahālakṣmi","O Mahalakshmi","The vocative of Mahālakṣmī, “the Great Lakshmi”."),
   ("नमः अस्तु ते","Namo ’stu te","My salutations to you","The refrain that closes every verse of the hymn."),
  ],
  meaning="Salutations to you, O Mahāmāyā, great divine power, seated at Śrīpīṭha and worshipped by the gods; you who hold the conch, discus and mace in your hands. O Mahalakshmi, I bow to you.",
  insights=[
   ("In simple words","The hymn opens with a plain bow. Before asking for anything, the poet greets the Goddess with three titles: the great creative power, the one seated at the sacred seat of Śrī, and the one whom even the gods worship. Reverence comes first; everything else follows from it."),
   ("Who is speaking","Tradition ascribes this hymn to Indra, king of the gods, and places it in the Padma Purāṇa. Accounts of the occasion differ, so it is safer to hold only the broad idea: even a king of the gods approaches Lakshmi with a bow."),
   ("Conch, discus and mace","These are the familiar emblems of Lord Vishnu. Here the Goddess carries them herself. The picture is of a Lakshmi who is not only gentle and generous but also powerful. That is a useful balance to keep in mind through the rest of the hymn."),
   ("Mahāmāyā is not “illusion” only","In popular speech <em>māyā</em> often means illusion. In devotional Sanskrit it also means the creative power through which the world is manifest. Read that way, <em>mahāmāyā</em> addresses Lakshmi as the great power behind creation."),
  ],
  meditation=["Minute 1: sit quietly and let the breath settle.","Minute 2: recite the first line slowly, feeling the bow in <em>namaḥ</em>.".replace("<em>","").replace("</em>",""),"Minute 3: picture the Goddess holding the conch, discus and mace, calm and capable.","Minute 4: offer one silent thanks for something you already have."],
  reflection="Before I ask for anything today, can I begin by acknowledging what I have already received? What would change in my day if I started with a bow instead of a request?",
  closing="The first verse is a salutation and nothing more, and that is its strength. A hymn that begins with reverence trains the mind to receive before it asks. "+MLA_D),

 dict(n=2, slug="verse-2",
  deva="नमस्ते गरुडारूढे कोलासुरभयङ्करि।<br>सर्वपापहरे देवि महालक्ष्मि नमोऽस्तु ते॥",
  iast="Namas te garuḍārūḍhe kolāsura-bhayaṅkari,<br>Sarva-pāpa-hare devi mahālakṣmi namo 'stu te.",
  sub="Garuḍārūḍhe – she who rides Garuḍa and removes fear and fault",
  words=[
   ("नमः ते","Namaḥ te","Salutation to you","As in the first verse."),
   ("गरुडारूढे","Garuḍārūḍhe","O you who are mounted on Garuḍa","<em>Garuḍa</em> is the eagle-like king of birds, the traditional mount of Lord Vishnu; <em>ārūḍha</em> is mounted or seated."),
   ("कोलासुरभयङ्करि","Kolāsura-bhayaṅkari","O terror of the demon Kolāsura","<em>Kolāsura</em> is the demon Kola of the Kolhapur tradition; <em>bhayaṅkari</em> is she who causes fear."),
   ("सर्वपापहरे","Sarva-pāpa-hare","O remover of all sins and faults","<em>Sarva</em> is all; <em>pāpa</em> is sin or fault; <em>harā</em> is one who takes away."),
   ("देवि","Devi","O Goddess","A respectful vocative."),
   ("महालक्ष्मि","Mahālakṣmi","O Mahalakshmi","The refrain name."),
  ],
  meaning="Salutations to you, O Goddess who ride on Garuḍa and are the terror of the demon Kolāsura, remover of all sins. O Mahalakshmi, I bow to you.",
  insights=[
   ("In simple words","The second verse shows two sides of the Goddess: she is mounted on Garuḍa and strikes fear into a demon, yet she is also the one who removes the faults of her devotees. Power and compassion are named in the same breath."),
   ("Kolāsura and Kolhapur","Local tradition tells that Mahalakshmi destroyed the demon Kolāsura at Kolhapur, and the city’s great Mahalakshmi temple is linked with this legend. Different tellings vary in detail, so treat the story as tradition rather than record."),
   ("A reflection on inner “demons”","Many readers take the demon as a symbol of whatever overwhelms us from inside: fear, greed or carelessness. That is a reading we bring to the verse, not something the verse states. It is a helpful way to make an old legend speak to daily life."),
  ],
  meditation=["Minute 1: breathe slowly and settle.","Minute 2: recite the verse once, paying attention to the rhythm of <em>garuḍārūḍhe</em>.".replace("<em>","").replace("</em>",""),"Minute 3: name one fear or fault you would like to be freed from, without judging yourself.","Minute 4: take one small, practical step toward it today."],
  reflection="What is the one fear or habit that most holds back my prosperity, in the widest sense of that word? What small step could I take toward it today?",
  closing="Fear and fault are two of the quiet drains on any life. This verse asks the Goddess to deal with both. "+MLA_D),

 dict(n=3, slug="verse-3",
  deva="सर्वज्ञे सर्ववरदे सर्वदुष्टभयङ्करि।<br>सर्वदुःखहरे देवि महालक्ष्मि नमोऽस्तु ते॥",
  iast="Sarvajñe sarva-varade sarva-duṣṭa-bhayaṅkari,<br>Sarva-duḥkha-hare devi mahālakṣmi namo 'stu te.",
  sub="Sarvajñe – the all-knowing, boon-giving mother",
  words=[
   ("सर्वज्ञे","Sarvajñe","O all-knowing one","<em>Sarva</em> is all; <em>jña</em> is one who knows."),
   ("सर्ववरदे","Sarva-varade","O giver of all boons","<em>Vara</em> is a boon or blessing; <em>da</em> is giver."),
   ("सर्वदुष्टभयङ्करि","Sarva-duṣṭa-bhayaṅkari","O terror of all wicked beings","<em>Duṣṭa</em> is one of evil intent; <em>bhayaṅkari</em> is one who causes fear."),
   ("सर्वदुःखहरे","Sarva-duḥkha-hare","O remover of all sorrows","<em>Duḥkha</em> is sorrow, pain, suffering."),
   ("देवि महालक्ष्मि","Devi mahālakṣmi","O Goddess Mahalakshmi","Vocatives."),
  ],
  meaning="Salutations to you, O all-knowing one, giver of all boons, terror of all wicked beings and remover of all sorrows. O Goddess Mahalakshmi, I bow to you.",
  insights=[
   ("In simple words","This verse is built on the word <em>sarva</em>, “all”, repeated four times. She knows all, gives all boons, frightens all evil and removes all sorrow. The poet is making the Goddess’s reach complete."),
   ("A chain of reasoning","Notice the order. Because she is all-knowing, she knows what we truly need. Because she grants boons, she can give it. Because she frightens the wicked, we are protected. Because she removes sorrow, we are comforted. The four titles can be read as one logical chain."),
   ("Why “all-knowing” comes first","We usually pray for outcomes. The verse begins with knowledge: that she knows. A reader may find rest in that: the prayer does not need to be perfectly worded, because it is addressed to someone who already understands."),
  ],
  meditation=["Minute 1: sit still and breathe.","Minute 2: recite the verse slowly; on each <em>sarva</em> pause for one breath.".replace("<em>","").replace("</em>",""),"Minute 3: bring to mind one worry and hand it over in your mind, without asking for a specific outcome.","Minute 4: rest in silence."],
  reflection="Is there a worry I keep rehearsing that I could simply place before the one who is said to know all? What would I do differently if I trusted that I had been understood?",
  closing="Four times the verse says “all”, and each time it widens the circle of care. It is a reminder that a prayer can be an act of letting go. "+MLA_D),

 dict(n=4, slug="verse-4",
  deva="सिद्धिबुद्धिप्रदे देवि भुक्तिमुक्तिप्रदायिनि।<br>मन्त्रमूर्ते सदा देवि महालक्ष्मि नमोऽस्तु ते॥",
  iast="Siddhi-buddhi-prade devi bhukti-mukti-pradāyini,<br>Mantra-mūrte sadā devi mahālakṣmi namo 'stu te.",
  sub="Siddhi, buddhi, bhukti, mukti – success and wisdom, enjoyment and freedom",
  words=[
   ("सिद्धिबुद्धिप्रदे","Siddhi-buddhi-prade","O giver of accomplishment and wisdom","<em>Siddhi</em> is accomplishment or success; <em>buddhi</em> is intellect, discernment; <em>prada</em> is giver."),
   ("देवि","Devi","O Goddess","Vocative."),
   ("भुक्तिमुक्तिप्रदायिनि","Bhukti-mukti-pradāyini","O giver of worldly enjoyment and liberation","<em>Bhukti</em> is enjoyment of the world, material well-being; <em>mukti</em> is liberation; <em>pradāyinī</em> is giver."),
   ("मन्त्रमूर्ते","Mantra-mūrte","O you whose form is mantra","<em>Mūrti</em> is form or embodiment. The Goddess is seen as present in sacred sound."),
   ("सदा","Sadā","Always","At all times."),
   ("महालक्ष्मि","Mahālakṣmi","O Mahalakshmi","The refrain."),
  ],
  meaning="Salutations to you, O Goddess, giver of accomplishment and wisdom, giver of worldly well-being and of liberation, whose very form is mantra. O Mahalakshmi, I bow to you.",
  insights=[
   ("In simple words","Two pairs of gifts are named: success with wisdom, and enjoyment with liberation. Notice that success is paired with wisdom, and enjoyment with freedom. The verse does not set one pair against the other."),
   ("Both aims of life","Indian thought speaks of <em>bhukti</em>, a good life in the world, and <em>mukti</em>, freedom from what binds us. Here the Goddess gives both. It is a quietly balanced view: material well-being is not despised, and it is not the final goal."),
   ("Mantra-mūrti: sound as presence","To call the Goddess “whose form is mantra” is to say that when her name or verse is recited, she is present in the sound. This is the devotional logic behind chanting, and it explains why many readers value pronouncing the verses with care."),
  ],
  meditation=["Minute 1: settle your posture and breath.","Minute 2: recite the verse once, slowly and clearly.","Minute 3: think of one area where you want success and ask what wisdom it needs.","Minute 4: sit quietly with the sound of the verse still in your mind."],
  reflection="Where am I asking for success without asking for wisdom? What would a good life, not only a successful one, look like for me?",
  closing="The verse pairs every gift with its companion. That is perhaps its best advice: look for success that comes with wisdom, and enjoyment that does not forget freedom. "+MLA_D),

 dict(n=5, slug="verse-5",
  deva="आद्यन्तरहिते देवि आद्यशक्तिमहेश्वरि।<br>योगजे योगसम्भूते महालक्ष्मि नमोऽस्तु ते॥",
  iast="Ādyanta-rahite devi ādya-śakti-maheśvari,<br>Yogaje yoga-sambhūte mahālakṣmi namo 'stu te.",
  sub="Ādyanta-rahite – without beginning and without end",
  words=[
   ("आद्यन्तरहिते","Ādyanta-rahite","O you who are without beginning or end","<em>Ādi</em> is beginning; <em>anta</em> is end; <em>rahita</em> is without."),
   ("आद्यशक्ति","Ādya-śakti","Primal power","<em>Ādya</em> is first, primal; <em>śakti</em> is power or energy."),
   ("महेश्वरि","Maheśvari","O great sovereign","<em>Īśvarī</em> is a female ruler; <em>mahā</em> is great."),
   ("योगजे","Yogaje","O you who are born of yoga","Born of, or known through, yoga: union and disciplined contemplation. Some editions vary this word."),
   ("योगसम्भूते","Yoga-sambhūte","O you who arise from yoga","<em>Sambhūta</em> is arisen, come into being."),
   ("महालक्ष्मि","Mahālakṣmi","O Mahalakshmi","The refrain."),
  ],
  meaning="Salutations to you, O Goddess without beginning or end, primal power and great sovereign, born of and arising from yoga. O Mahalakshmi, I bow to you.",
  insights=[
   ("In simple words","With this verse the hymn moves from stories to philosophy. The Goddess is without beginning or end, the first power, the supreme sovereign, and she is known in the depths of yoga."),
   ("Lakshmi beyond wealth","Many people meet Lakshmi only as the goddess of money. This verse shows a larger picture: Mahalakshmi as the primal power behind all that exists. Wealth is one of her gifts; it is not her whole nature."),
   ("Yoga as a way of knowing","The verse says she arises from yoga. Readers differ on exactly how to read this; one natural way is that she is realised through steady, disciplined inner attention rather than through argument. It invites quieter forms of worship."),
  ],
  meditation=["Minute 1: close your eyes and breathe.","Minute 2: recite the verse and let “without beginning or end” stay with you.","Minute 3: imagine a presence larger than your worries.","Minute 4: bring that wider view back to one thing you are concerned about today."],
  reflection="When I think of Lakshmi, do I think only of money? What changes if I think of her as the source of all well-being?",
  closing="A hymn that begins with a bow and ends with the supreme power has travelled a long way in five verses. It asks us to widen our idea of what we are praying to. "+MLA_D),

 dict(n=6, slug="verse-6",
  deva="स्थूलसूक्ष्ममहारौद्रे महाशक्तिमहोदरे।<br>महापापहरे देवि महालक्ष्मि नमोऽस्तु ते॥",
  iast="Sthūla-sūkṣma-mahā-raudre mahā-śakti-mahodare,<br>Mahā-pāpa-hare devi mahālakṣmi namo 'stu te.",
  sub="Sthūla-sūkṣma – gross and subtle, fierce and all-containing",
  words=[
   ("स्थूलसूक्ष्ममहारौद्रे","Sthūla-sūkṣma-mahā-raudre","O you who are gross, subtle and greatly fierce","<em>Sthūla</em> is gross or visible; <em>sūkṣma</em> is subtle; <em>raudra</em> is fierce, terrible."),
   ("महाशक्ति","Mahā-śakti","Great power","<em>Śakti</em> is power or energy."),
   ("महोदरे","Mahodare","O you of great womb, who contain all","Literally “of the great belly”: she holds the whole universe within her. Some editions read <em>mahodaye</em>, “of great rise or prosperity”."),
   ("महापापहरे","Mahā-pāpa-hare","O remover of great sins","<em>Mahā</em> is great; <em>pāpa</em> is sin or fault; <em>hara</em> is remover."),
   ("देवि महालक्ष्मि","Devi mahālakṣmi","O Goddess Mahalakshmi","Vocatives."),
  ],
  meaning="Salutations to you, O Goddess who are both gross and subtle and also greatly fierce, great power who contain all within you, remover of the greatest sins. O Mahalakshmi, I bow to you.",
  insights=[
   ("In simple words","The verse piles up contrasts: visible and invisible, and fierce as well as nurturing. The point is that the Goddess is not one thing. She is the whole range, from the form we can see to the energy we cannot."),
   ("Gentle and fierce","Lakshmi is usually shown smiling, with coins falling from her hand. This verse reminds us that the same power can be fierce toward what harms. Taking both seriously keeps devotion from becoming sentimental."),
   ("A note on the variant reading","Editions differ on the third pāda: <em>mahodare</em> (of great belly, containing all) and <em>mahodaye</em> (of great prosperity or rise). Either way the idea is greatness and fullness. We follow the more widely printed <em>mahodare</em>."),
  ],
  meditation=["Minute 1: still the body.","Minute 2: recite the verse slowly.","Minute 3: notice both the visible and the unseen in your day: what you can count, and what you cannot.","Minute 4: sit with the thought that both are part of one life."],
  reflection="What in my life is measurable, and what matters just as much but cannot be measured? Am I giving the second kind its share of attention?",
  closing="Gross and subtle, gentle and fierce: the verse refuses to shrink the Goddess to one picture. That is a good habit for a reader, too. "+MLA_D),

 dict(n=7, slug="verse-7",
  deva="पद्मासनस्थिते देवि परब्रह्मस्वरूपिणि।<br>परमेशि जगन्मातर्महालक्ष्मि नमोऽस्तु ते॥",
  iast="Padmāsana-sthite devi para-brahma-svarūpiṇi,<br>Parameśi jagan-mātar mahālakṣmi namo 'stu te.",
  sub="Padmāsana-sthite – seated on the lotus, mother of the world",
  words=[
   ("पद्मासनस्थिते","Padmāsana-sthite","O you who are seated on a lotus seat","<em>Padma</em> is lotus; <em>āsana</em> is seat; <em>sthita</em> is seated."),
   ("परब्रह्मस्वरूपिणि","Para-brahma-svarūpiṇi","O you whose nature is the Supreme Brahman","<em>Para-brahma</em> is the Supreme Reality; <em>svarūpa</em> is own form or nature."),
   ("परमेशि","Parameśi","O Supreme Sovereign","<em>Parama</em> is supreme; <em>īśī</em> is a ruler, a feminine form."),
   ("जगन्मातः","Jagan-mātaḥ","O Mother of the world","<em>Jagat</em> is the world; <em>mātṛ</em> is mother."),
   ("महालक्ष्मि","Mahālakṣmi","O Mahalakshmi","The refrain."),
  ],
  meaning="Salutations to you, O Goddess seated on the lotus, whose very nature is the Supreme Brahman, supreme sovereign and mother of the world. O Mahalakshmi, I bow to you.",
  insights=[
   ("In simple words","Two images come together: the Goddess on her lotus seat, and the Goddess as the Supreme Reality itself. Lakshmi is not only a figure in a story; here she is named as the ultimate."),
   ("The lotus seat","The lotus grows in mud yet stays clean, which is why it has long stood for purity and for being at ease in the world. To place the Goddess on a lotus is to say that prosperity and purity belong together."),
   ("Mother of the world","<em>Jagan-mātā</em> is a warm title. It means that the Supreme is also a mother: someone from whom we are not separate and to whom we can speak directly. Many devotees find this the most approachable image in the hymn."),
  ],
  meditation=["Minute 1: sit and settle.","Minute 2: picture a lotus resting on still water.","Minute 3: recite the verse and let the word “mother” soften the recitation.","Minute 4: rest quietly."],
  reflection="What would it mean to approach prosperity the way a lotus approaches water: at home in it, but not stained by it?",
  closing="The seventh verse joins the highest philosophy with the warmest title: Supreme Brahman, and mother. Both are meant to be held together. "+MLA_D),

 dict(n=8, slug="verse-8",
  deva="श्वेताम्बरधरे देवि नानालङ्कारभूषिते।<br>जगत्स्थिते जगन्मातर्महालक्ष्मि नमोऽस्तु ते॥",
  iast="Śvetāmbara-dhare devi nānālaṅkāra-bhūṣite,<br>Jagat-sthite jagan-mātar mahālakṣmi namo 'stu te.",
  sub="Śvetāmbara-dhare – in white garments, adorned with many ornaments",
  words=[
   ("श्वेताम्बरधरे","Śvetāmbara-dhare","O you who wear white garments","<em>Śveta</em> is white; <em>ambara</em> is cloth or garment; <em>dhara</em> is wearing."),
   ("नानालङ्कारभूषिते","Nānālaṅkāra-bhūṣite","O you adorned with many ornaments","<em>Nānā</em> is various; <em>alaṅkāra</em> is ornament; <em>bhūṣita</em> is adorned."),
   ("जगत्स्थिते","Jagat-sthite","O you who abide in the world","<em>Sthita</em> is standing, abiding, established. She is present in the world and sustains it."),
   ("जगन्मातः","Jagan-mātaḥ","O Mother of the world","Repeated from the seventh verse."),
   ("महालक्ष्मि","Mahālakṣmi","O Mahalakshmi","The refrain."),
  ],
  meaning="Salutations to you, O Goddess clad in white garments and adorned with many ornaments, who abide in the world and are its mother. O Mahalakshmi, I bow to you.",
  insights=[
   ("In simple words","The eighth verse paints a final picture: white garments, rich ornaments, the world as her place and the whole world as her child. It closes the hymn with an image of simplicity and abundance together."),
   ("White and ornaments","White suggests purity and simplicity; ornaments suggest richness. The verse gives both without any sense of conflict. That is a gentle idea of prosperity: abundance that stays clean."),
   ("A note on colour","This hymn describes the Goddess in white. Popular images of Lakshmi, especially at Diwali, often show her in red or pink. The tradition has many forms of the Goddess, and different texts and temples describe different ones."),
  ],
  meditation=["Minute 1: breathe and settle.","Minute 2: recite the whole eight-verse hymn in your mind, one image per verse.","Minute 3: choose the image that stayed with you most.","Minute 4: carry it into the next hour."],
  reflection="Which image in this hymn spoke to me most: the bow, the fear removed, the all-knowing mother, the lotus, the white garment? What does that say about what I am looking for?",
  closing="The eight verses end as they began, with a bow. In between they have shown the Goddess as protector, giver, primal power, supreme mother. "+MLA_D),

 dict(n=9, slug="verse-9",
  deva="महालक्ष्म्यष्टकं स्तोत्रं यः पठेद्भक्तिमान्नरः।<br>सर्वसिद्धिमवाप्नोति राज्यं प्राप्नोति सर्वदा॥<br>एककाले पठेन्नित्यं महापापविनाशनम्।<br>द्विकालं यः पठेन्नित्यं धनधान्यसमन्वितः॥<br>त्रिकालं यः पठेन्नित्यं महाशत्रुविनाशनम्।<br>महालक्ष्मीर्भवेन्नित्यं प्रसन्ना वरदा शुभा॥",
  iast="Mahālakṣmy-aṣṭakaṁ stotraṁ yaḥ paṭhed bhaktimān naraḥ,<br>Sarva-siddhim avāpnoti rājyaṁ prāpnoti sarvadā.<br>Eka-kāle paṭhen nityaṁ mahā-pāpa-vināśanam,<br>Dvi-kālaṁ yaḥ paṭhen nityaṁ dhana-dhānya-samanvitaḥ.<br>Tri-kālaṁ yaḥ paṭhen nityaṁ mahā-śatru-vināśanam,<br>Mahālakṣmīr bhaven nityaṁ prasannā varadā śubhā.",
  sub="Phalaśruti – the fruit of reciting the hymn",
  words=[
   ("महालक्ष्म्यष्टकं स्तोत्रम्","Mahālakṣmy-aṣṭakaṁ stotram","The eight-verse hymn to Mahalakshmi","<em>Aṣṭaka</em> is a set of eight; <em>stotra</em> is a hymn of praise."),
   ("यः पठेत् भक्तिमान् नरः","Yaḥ paṭhet bhaktimān naraḥ","The person who recites it with devotion","<em>Bhaktimān</em> is one who has devotion."),
   ("सर्वसिद्धिम् अवाप्नोति","Sarva-siddhim avāpnoti","Attains all accomplishments","<em>Siddhi</em> is accomplishment; <em>avāpnoti</em> is attains."),
   ("राज्यं प्राप्नोति","Rājyaṁ prāpnoti","Obtains sovereignty or a kingdom","Classical language for authority and prosperity; many readers take it figuratively."),
   ("एककाले","Eka-kāle","Once a day","<em>Kāla</em> is time or period."),
   ("द्विकालम् / त्रिकालम्","Dvi-kālam / Tri-kālam","Twice a day / three times a day","Morning and evening, or morning, noon and evening."),
   ("धनधान्यसमन्वितः","Dhana-dhānya-samanvitaḥ","Endowed with wealth and grain","<em>Dhana</em> is wealth; <em>dhānya</em> is grain; <em>samanvita</em> is endowed with."),
   ("प्रसन्ना वरदा शुभा","Prasannā varadā śubhā","Pleased, boon-giving and auspicious","Three words describing Mahalakshmi as she becomes favourable."),
  ],
  meaning="Whoever recites this eight-verse hymn to Mahalakshmi with devotion is said to attain every accomplishment and lasting authority. Recited once daily, it destroys great sins; twice daily, it brings wealth and grain; three times daily, it destroys great enemies, and Mahalakshmi becomes ever pleased, boon-giving and auspicious.",
  insights=[
   ("In simple words","Like many Sanskrit hymns, this one ends with a <em>phalaśruti</em>, a statement of the fruit that tradition associates with reciting it. Three more verses are added to the eight, so the hymn is often printed with eleven verses. Here the three are taken together as the ninth entry."),
   ("Once, twice, three times","The verses raise the benefit as the practice grows: once a day for forgiveness of faults, twice for prosperity, three times for strength against what opposes us. The pattern encourages regularity rather than a single grand effort."),
   ("How to read these promises","A phalaśruti states what tradition says, not what anyone can guarantee. Readers differ: some take the fruits literally, others as inner growth such as steadiness, clarity and courage. This site reads it as encouragement to practise, and does not promise an outcome."),
  ],
  meditation=["Minute 1: sit and breathe.","Minute 2: recite one verse of the hymn that you remember.","Minute 3: choose a realistic rhythm for yourself: once a day, or once a week.","Minute 4: end with a bow."],
  reflection="What would a gentle, sustainable practice look like for me: a few minutes once a day, rather than a promise I cannot keep?",
  closing="The hymn closes by turning from praise to practice. Whatever fruit one expects, the steady habit of attention is the part within our own hands. "+MLA_D),
]

MLA_TOTAL = 9  # eight verses plus the closing phalaśruti (three verses, shown together as the ninth entry)
for _v in MVERSES:
    _v["h1"] = f"Mahālakṣmī Aṣṭakam – Verse {_v['n']}"
    _v["title"] = _v["desc"] = ""
MVERSES[8]["label"] = "Phalaśruti (9–11)"
MVERSES[8]["h1"] = "Mahālakṣmī Aṣṭakam – Phalaśruti (Verses 9–11)"
MVERSES[8]["ttl"] = "Mahalakshmi Ashtakam Phalashruti Meaning (Verses 9-11)"
MVERSES[8]["dsc"] = "Mahalakshmi Ashtakam phalashruti (verses 9-11): the fruit of reciting the hymn once, twice or three times a day. Word-by-word meaning and English translation."

GLOSSARY = [
 ("महामाया","Mahāmāyā","The “great Māyā”: the divine creative power by which the world appears; a title of the Goddess.","mahalakshmi-ashtakam/verse-1/"),
 ("श्रीपीठ","Śrīpīṭha","The seat of Śrī (Lakshmi); tradition links it with the Mahalakshmi temple at Kolhapur.","mahalakshmi-ashtakam/verse-1/"),
 ("कोलासुर","Kolāsura","The demon Kola of the Kolhapur tradition, said to have been destroyed by Mahalakshmi.","mahalakshmi-ashtakam/verse-2/"),
 ("गरुड","Garuḍa","The king of birds and the traditional mount of Lord Vishnu.","mahalakshmi-ashtakam/verse-2/"),
 ("सिद्धि","Siddhi","Accomplishment, success; in a spiritual sense, attainment.","mahalakshmi-ashtakam/verse-4/"),
 ("भुक्ति","Bhukti","Worldly enjoyment and well-being, as the companion aim to mukti.","mahalakshmi-ashtakam/verse-4/"),
 ("मुक्ति","Mukti","Liberation from what binds us.","mahalakshmi-ashtakam/verse-4/"),
 ("मन्त्रमूर्ति","Mantra-mūrti","One whose form is mantra: the Goddess present in sacred sound.","mahalakshmi-ashtakam/verse-4/"),
 ("अष्टक","Aṣṭaka","A hymn or set of eight verses.","mahalakshmi-ashtakam/verse-9/"),
 ("मुरारि","Murāri","“Foe of Mura”: a name of Vishnu, who slew the demon Mura.","kanakadhara/verse-2/"),
 ("प्रेम","Prema","Love, affection.","kanakadhara/verse-2/"),
 ("त्रपा","Trapā","Bashfulness, modesty; a graceful reserve.","kanakadhara/verse-2/"),
 ("मधुकरी","Madhukarī","A female bee; literally “she who makes honey”.","kanakadhara/verse-2/"),
 ("सागरसम्भवा","Sāgarasambhavā","“Born from the ocean”: a name of Lakshmi, who emerged at the churning of the ocean.","kanakadhara/verse-2/"),
 ("सन्धि","Sandhi","The joining of sounds when Sanskrit words meet, which is why words in a verse often look run together.","kanakadhara/verse-2/"),
 ("पुलक","Pulaka","Goosebumps that rise from intense emotion; the visible thrill of joy.","kanakadhara/verse-1/"),
 ("अपाङ्ग","Apāṅga","The corner of the eye; a sidelong glance.","kanakadhara/verse-1/"),
 ("कटाक्ष","Kaṭākṣa","A gracious glance; in devotion, a sign of divine favour.","kanakadhara/verse-1/"),
 ("लीला","Līlā","Play; graceful, effortless action.","kanakadhara/verse-1/"),
 ("विभूति","Vibhūti","Glory, power, excellence, magnificence.","kanakadhara/verse-1/"),
 ("माङ्गल्य","Māṅgalya","Auspiciousness; blessing and good fortune.","kanakadhara/verse-1/"),
 ("तमाल","Tamāla","A tree traditionally associated with a dark complexion, often used as an image of Vishnu’s dark form.","kanakadhara/verse-1/"),
 ("भृङ्ग","Bhṛṅga","A bee.","kanakadhara/verse-1/"),
 ("हिरण्यवर्णा","Hiraṇyavarṇā","Golden-colored; the golden hue of Lakshmi.","sri-suktam/verse-1/"),
 ("हरिणी","Hariṇī","Deer-like, gentle and graceful. Also read as golden-yellow, or as the one who removes sorrow and poverty.","sri-suktam/verse-1/"),
 ("सुवर्ण","Suvarṇa","Gold.","sri-suktam/verse-1/"),
 ("रजत","Rajata","Silver.","sri-suktam/verse-1/"),
 ("स्रज्","Sraj","A garland or wreath; by extension, an adornment.","sri-suktam/verse-1/"),
 ("चन्द्रा","Chandrā","Shining and gladdening; moon-like, radiant and cooling.","sri-suktam/verse-1/"),
 ("हिरण्मयी","Hiraṇmayī","Made of gold; golden in substance, not only in colour.","sri-suktam/verse-1/"),
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
 ("सोस्मिता","Sosmitā","With a gentle smile (sa-smitā); also read as the blissful one.","sri-suktam/verse-4/"),
 ("हिरण्यप्राकार","Hiraṇya-prākāra","Surrounded by walls or ramparts of gold; prosperity that is protected and secure.","sri-suktam/verse-4/"),
 ("आर्द्रा","Ārdrā","Moist, tender, compassionate.","sri-suktam/verse-4/"),
 ("ज्वलन्ती","Jvalantī","Blazing, radiant, shining like fire.","sri-suktam/verse-4/"),
 ("तृप्ता","Tṛptā","Satisfied, contented, complete.","sri-suktam/verse-4/"),
 ("तर्पयन्ती","Tarpayantī","One who satisfies and nourishes others.","sri-suktam/verse-4/"),
 ("पद्म","Padma","Lotus; purity, beauty and detachment.","sri-suktam/verse-4/"),
 ("पद्मवर्णा","Padma-varṇā","Lotus-coloured, with the soft hue of a lotus.","sri-suktam/verse-4/"),
 ("प्रभासा","Prabhāsā","Brilliant, full of light.","sri-suktam/verse-5/"),
 ("यशस्","Yaśas","Fame, glory, honour earned by good deeds.","sri-suktam/verse-5/"),
 ("देवजुष्टा","Devajuṣṭā","Favoured, loved and served by the gods.","sri-suktam/verse-5/"),
 ("उदारा","Udārā","Generous, magnanimous, open-hearted.","sri-suktam/verse-5/"),
 ("पद्मिनी","Padminī","She who holds or is associated with the lotus; a name of Lakshmi.","sri-suktam/verse-5/"),
 ("शरण","Śaraṇa","Refuge, shelter, protection.","sri-suktam/verse-5/"),
 ("प्रपद्ये","Prapadye","I take refuge, I surrender.","sri-suktam/verse-5/"),
 ("अलक्ष्मी","Alakṣmī","The opposite of Lakshmi: poverty, scarcity, misfortune and negativity.","sri-suktam/verse-5/"),
 ("वृणे","Vṛṇe","I choose, I select.","sri-suktam/verse-5/"),
 ("आदित्यवर्णा","Āditya-varṇā","Sun-coloured; shining with the brilliance of the sun.","sri-suktam/verse-6/"),
 ("तपस्","Tapas","Austerity, discipline and sustained effort; the inner heat that refines.","sri-suktam/verse-6/"),
 ("वनस्पति","Vanaspati","Lord of the forest; a large tree.","sri-suktam/verse-6/"),
 ("बिल्व","Bilva","The bael tree, sacred to Lord Shiva and used in pure offerings; a symbol of deeply rooted, fruitful blessings.","sri-suktam/verse-6/"),
 ("माया","Māyā","Illusion, confusion; here the inner delusion that blocks abundance.","sri-suktam/verse-6/"),
 ("अन्तराय","Antarāya","An obstacle or hindrance, especially an inner one.","sri-suktam/verse-6/"),
 ("बाह्य","Bāhya","External, outer.","sri-suktam/verse-6/"),
 ("देवसख","Deva-sakha","Friend of the gods; understood as Kubera, the divine treasurer.","sri-suktam/verse-7/"),
 ("कुबेर","Kubera","The divine treasurer, guardian of wealth, who holds it with righteousness.","sri-suktam/verse-7/"),
 ("कीर्ति","Kīrti","Fame, honour, good reputation.","sri-suktam/verse-7/"),
 ("मणि","Maṇi","A jewel; brilliance and splendour. Some commentators read it as Maṇibhadra, Kubera’s companion.","sri-suktam/verse-7/"),
 ("राष्ट्र","Rāṣṭra","Kingdom, land, nation; here one’s society and community.","sri-suktam/verse-7/"),
 ("ऋद्धि","Ṛddhi","Growth, prosperity, success.","sri-suktam/verse-7/"),
 ("प्रादुर्भूत","Prādurbhūta","Manifested, arisen, come into being.","sri-suktam/verse-7/"),
 ("क्षुत्","Kṣut","Hunger; also craving and dissatisfaction.","sri-suktam/verse-8/"),
 ("पिपासा","Pipāsā","Thirst; also endless wanting.","sri-suktam/verse-8/"),
 ("मल","Mala","Impurity, dirt, stain.","sri-suktam/verse-8/"),
 ("ज्येष्ठा","Jyeṣṭhā","The elder sister of Lakshmi; the figure who stands for poverty, misfortune and quarrelsomeness.","sri-suktam/verse-8/"),
 ("नाशयामि","Nāśayāmi","I destroy, I remove.","sri-suktam/verse-8/"),
 ("अभूति","Abhūti","Absence of prosperity; poverty.","sri-suktam/verse-8/"),
 ("असमृद्धि","Asamṛddhi","Lack of growth; stagnation and failure.","sri-suktam/verse-8/"),
 ("निर्णुद","Nirṇuda","Drive out, banish, push away forcefully.","sri-suktam/verse-8/"),
 ("गृह","Gṛha","Home, household.","sri-suktam/verse-8/"),
 ("गन्धद्वारा","Gandha-dvārā","One whose presence is known through fragrance; subtle, pure and auspicious.","sri-suktam/verse-9/"),
 ("दुराधर्षा","Durādharṣā","Invincible; one who cannot be overcome.","sri-suktam/verse-9/"),
 ("नित्यपुष्टा","Nitya-puṣṭā","Ever-nourished and ever-nourishing.","sri-suktam/verse-9/"),
 ("करीषिणी","Karīṣiṇī","One connected with fertility and productivity, especially of the land and cattle.","sri-suktam/verse-9/"),
 ("ईश्वरी","Īśvarī","Sovereign goddess; supreme ruler.","sri-suktam/verse-9/"),
 ("सर्वभूत","Sarva-bhūta","All beings.","sri-suktam/verse-9/"),
 ("मनस्","Manas","The mind.","sri-suktam/verse-10/"),
 ("काम","Kāma","Desire, wish.","sri-suktam/verse-10/"),
 ("आकूति","Ākūti","Intention, resolve, noble aspiration.","sri-suktam/verse-10/"),
 ("सत्य","Satya","Truth; truthfulness.","sri-suktam/verse-10/"),
 ("अशीमहि","Aśīmahi","May we obtain, may we attain.","sri-suktam/verse-10/"),
 ("पशु","Paśu","Cattle, livestock; a symbol of wealth and nourishment in Vedic times.","sri-suktam/verse-10/"),
 ("अन्न","Anna","Food, nourishment, sustenance.","sri-suktam/verse-10/"),
 ("श्रयताम्","Śrayatām","May she take shelter, may she dwell.","sri-suktam/verse-10/"),
 ("कर्दम","Kardama","Mud or fertile soil; also a sage, regarded as a son of Lakshmi.","sri-suktam/verse-11/"),
 ("प्रजा","Prajā","Offspring, progeny, living creation.","sri-suktam/verse-11/"),
 ("सम्भव","Sambhava","Arise, come into being.","sri-suktam/verse-11/"),
 ("कुल","Kula","Family, lineage, household.","sri-suktam/verse-11/"),
 ("मातृ","Mātṛ","Mother.","sri-suktam/verse-11/"),
 ("पद्ममालिनी","Padma-mālinī","One wearing a garland of lotuses; a name of Lakshmi.","sri-suktam/verse-11/"),
 ("आपः","Āpaḥ","Waters; purity, life-force and flow.","sri-suktam/verse-12/"),
 ("स्निग्ध","Snigdha","Soft, smooth, gentle and affectionate.","sri-suktam/verse-12/"),
 ("चिक्लीत","Ciklīta","Moisture, richness and fertility; also read as the name of a son of Lakshmi.","sri-suktam/verse-12/"),
 ("वासय","Vāsaya","Cause to dwell, settle.","sri-suktam/verse-12/"),
 ("पुष्करिणी","Puṣkariṇī","A lotus pond; one who dwells among lotuses.","sri-suktam/verse-13/"),
 ("पुष्टि","Puṣṭi","Nourishment, fullness, thriving.","sri-suktam/verse-13/"),
 ("पिङ्गला","Piṅgalā","Golden-hued, tawny and warm.","sri-suktam/verse-13/"),
 ("करिणी","Kariṇī","She who brings action to fulfilment; also read as one attended by elephants.","sri-suktam/verse-14/"),
 ("यष्टि","Yaṣṭi","A staff or support; the strength that comes from sustained practice.","sri-suktam/verse-14/"),
 ("सुवर्णा","Suvarṇā","Golden, of a fine bright colour.","sri-suktam/verse-14/"),
 ("हेममालिनी","Hema-mālinī","One wearing a garland of gold.","sri-suktam/verse-14/"),
 ("सूर्या","Sūryā","Sun-like; radiant and life-giving.","sri-suktam/verse-14/"),
 ("प्रभूत","Prabhūta","Abundant, plentiful.","sri-suktam/verse-15/"),
 ("दासी","Dāsī","An attendant or helper; here, cooperation and support.","sri-suktam/verse-15/"),
 ("फलश्रुति","Phalaśruti","The “hearing of the fruits”: the closing verse that describes the benefit of reciting a hymn.","sri-suktam/verse-16/"),
 ("शुचि","Śuci","Pure, clean.","sri-suktam/verse-16/"),
 ("प्रयत","Prayata","Self-restrained, disciplined, composed.","sri-suktam/verse-16/"),
 ("आज्य","Ājya","Clarified butter (ghee) used in fire offerings.","sri-suktam/verse-16/"),
 ("अग्निहोत्र","Agnihotra","The daily fire offering made at sunrise and sunset.","sri-suktam/verse-16/"),
 ("पञ्चदशर्च","Pañcadaśarca","Of fifteen verses (ṛc); the fifteen verses of the Śrī Sūktam.","sri-suktam/verse-16/"),
 ("श्रीकाम","Śrīkāma","One who desires Śrī, prosperity.","sri-suktam/verse-16/"),
 ("जप","Japa","Quiet, repeated recitation of a mantra.","sri-suktam/verse-16/"),
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
<meta name="google-site-verification" content="{GSC_TOKEN}">
<meta name="theme-color" content="#7a1f2b">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Lakshmi Stuti: Śrī Sūktam and Kanakadhāra Stotram commentary">
<meta property="og:locale" content="en_IN">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{E(title)}">
<meta name="twitter:description" content="{E(desc)}">
<meta name="twitter:image" content="{SITE}/assets/og.png">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Inter:wght@400;500;600&family=Noto+Serif+Devanagari:wght@500;700&display=swap">
<link rel="stylesheet" href="/assets/style.css">
{ldh}{ga}{ads}
{INTRO_JS if path=="" else ""}
</head>'''

def nav(cur):
    items = [("Home","", "home"),("Śrī Sūktam","sri-suktam/","sri"),("Kanakadhāra","kanakadhara/","kana"),("Mahālakṣmī Aṣṭakam","mahalakshmi-ashtakam/","mla"),("Glossary","glossary/","gl"),("About","about/","about")]
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

PAGES = []  # (path, priority, lastmod)
MANIFEST_PATH = os.path.join(ROOT, "tools", "pagedates.json")
try: MANIFEST = json.load(open(MANIFEST_PATH, encoding="utf-8"))
except Exception: MANIFEST = {}
def write(path, content, prio="0.6"):
    # published / modified dates come from a manifest: the modified date moves only when the page's own content changes
    m = content[content.find("<main"):content.rfind("</main>")]
    h = hashlib.sha1(m.encode("utf-8")).hexdigest()[:12]
    e = MANIFEST.get(path or "home")
    if not e:
        # first time a page is seen: use the date it was first committed, if it already existed
        rel = (path + "/index.html") if path else "index.html"
        try:
            dts = subprocess.run(["git","log","--format=%cs","--",rel],cwd=ROOT,capture_output=True,text=True).stdout.split()
        except Exception: dts = []
        e = {"published": dts[-1] if dts else TODAY, "modified": dts[0] if dts else TODAY, "hash": h}
    elif e["hash"] != h: e = {"published": e["published"], "modified": TODAY, "hash": h}
    MANIFEST[path or "home"] = e
    content = content.replace("@@PUB@@", e["published"]).replace("@@MOD@@", e["modified"])
    d = os.path.join(ROOT, path)
    os.makedirs(d, exist_ok=True) if path else None
    with open(os.path.join(d, "index.html") if path else os.path.join(ROOT,"index.html"), "w", encoding="utf-8") as f:
        f.write(content)
    PAGES.append((path, prio, e["modified"]))

def plain(t):
    """Diacritics-free spelling, because most people search without them (Sri Suktam, not Śrī Sūktam)."""
    t = unicodedata.normalize("NFD", t.replace("ṁ","m").replace("ṃ","m"))
    return "".join(c for c in t if not unicodedata.combining(c))

def opening(v, n=4):
    first = re.sub(r"(?<=\s)['’]", "a", v["iast"]).replace("<br>"," ").replace("-"," ").replace(","," ").replace(";"," ").replace("."," ")
    return " ".join(plain(first).split()[:n]).title()

# ---------------------------------------------------------------- pages
def lab(v): return v.get("label") or f"Verse {v['n']}"
def page_home():
    v = KVERSES[-1]
    t = "Lakshmi Stuti: Sri Suktam & Kanakadhara Stotram Meaning"
    d = "Verse-by-verse English meaning of the Sri Suktam and Kanakadhara Stotram to Goddess Lakshmi (Laxmi): Sanskrit text, word meanings and reflection."
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
<p><a class="btn" href="/sri-suktam/verse-1/">Start with Śrī Sūktam Verse 1</a><a class="btn ghost" href="/sri-suktam/">Śrī Sūktam index</a><a class="btn ghost" href="/kanakadhara/">Kanakadhāra Stotram</a></p>
</section>
<h2>Latest verse</h2>
<div class="verse"><p class="label">Kanakadhāra Stotram · {lab(v)}</p><p class="deva">{v["deva"]}</p><p class="iast">{v["iast"]}</p></div>
<p>{E(v["closing"] or v["meaning"])} <a href="/kanakadhara/{v["slug"]}/">Read the full commentary →</a></p>
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
<a class="tile" href="/kanakadhara/"><h3>Kanakadhāra Stotram</h3><p>Śrī Śaṅkarācārya’s hymn to Lakshmi. The story and {len(KVERSES)} verse{"s" if len(KVERSES)!=1 else ""} are live; more follow one at a time.</p></a>
<a class="tile" href="/mahalakshmi-ashtakam/"><h3>Mahālakṣmī Aṣṭakam</h3><p>Indra’s eight-verse hymn to Mahalakshmi. The full text to chant, with the meaning of every verse.</p></a>
<a class="tile" href="/ashtalakshmi/"><h3>Aṣṭalakṣmī</h3><p>The eight forms of Lakshmi, and what each one stands for.</p></a>
<a class="tile" href="/sri-yantra/"><h3>Śrī Yantra</h3><p>The sacred diagram of Lakshmi, and what each of its five layers means.</p></a>
<a class="tile" href="/glossary/"><h3>Glossary</h3><p>Sanskrit words used across the commentary, with simple meanings.</p></a>
</div>
{ad("home")}
</main>''' + INTRO_SCRIPT + foot()
    write("", body, "1.0")

def page_sri():
    t = "Sri Suktam Meaning in English – Verse by Verse"
    d = "Sri Suktam (Shri Suktam) meaning in English: all 16 verses of the Vedic hymn to Goddess Lakshmi with Sanskrit text and word-by-word explanation."
    parts = [("Śrī Sūktam","sri-suktam/")]
    rows = ""
    for v in VERSES:
        rows += f'<a class="tile" href="/sri-suktam/{v["slug"]}/"><h3>{lab(v)}</h3><p>{E(v["sub"])}</p></a>'
    for n in range(len(VERSES)+1, TOTAL_SRI+1):
        rows += f'<div class="tile" style="opacity:.55"><h3>Verse {n} <span class="soon">coming soon</span></h3></div>'
    body = head(t,d,"sri-suktam/",bc_ld(parts)) + nav("sri") + f'''
<main class="wrap">{crumbs([("Śrī Sūktam",None)])}
<h1>Śrī Sūktam – verse by verse</h1>
<p class="lede">The Śrī Sūktam (also written Sri Suktam, Shri Suktam or Shree Suktam) is a Vedic hymn praising Goddess Lakshmi (Śrī) as the source of prosperity, grace and auspiciousness. Each verse here has the Sanskrit text, a word-by-word meaning, deeper insights and a short practice.</p>
<p>Verses are published one at a time, so that each can be read and absorbed slowly before the next appears.</p>
<p><small>A note on the count: the hymn proper has 15 verses. Here the closing verse on the fruit of reciting it (the <em>phalaśruti</em>) is numbered Verse 16, so the series is complete at sixteen. Editions differ: some print more phalaśruti verses, and some do not number this one at all.</small></p>
<div class="grid">{rows}</div>
{ad("index")}
</main>''' + foot()
    write("sri-suktam", body, "0.9")

def page_kana():
    t = "Kanakadhara Stotram Meaning, Story and Verses in English"
    d = "Kanakadhara Stotram by Adi Shankaracharya: the story of the poor woman’s gooseberry, what “stream of gold” means, and verse-by-verse meaning in English."
    parts = [("Kanakadhāra Stotram","kanakadhara/")]
    ld = {"@context":"https://schema.org","@type":"Article","headline":"Kanakadhāra Stotram – The Story Before the First Verse","author":{"@type":"Person","name":AUTHOR},"datePublished":"@@PUB@@","dateModified":"@@MOD@@","inLanguage":"en","image":SITE+"/assets/og.png","isAccessibleForFree":True,"mainEntityOfPage":SITE+"/kanakadhara/","publisher":{"@type":"Person","name":AUTHOR,"url":SITE+"/about/"}}
    krows = "".join(f'<a class="tile" href="/kanakadhara/{v["slug"]}/"><h3>{lab(v)}</h3><p>{E(v["sub"])}</p></a>' for v in KVERSES)
    body = head(t,d,"kanakadhara/",ld,"article") + f'<script type="application/ld+json">{json.dumps(bc_ld(parts),ensure_ascii=False)}</script>' + nav("kana") + f'''
<main class="wrap">{crumbs([("Kanakadhāra Stotram",None)])}
<h1>Kanakadhāra Stotram</h1>
<p class="lede">Śrī Śaṅkarācārya’s hymn to Goddess Lakshmi (the Kanakadhara Stotram, also written Kanakdhara or Kanaka Dhara Stotra), read slowly, verse by verse.</p>
<p class="crumbs">By {AUTHOR}</p>
<p><a class="btn" href="/kanakadhara/verse-1/">Start with Verse 1</a><a class="btn ghost" href="#story">Read the story first</a></p>
<h2 id="verses">Verses</h2>
<div class="grid">{krows}</div>
<p><small>{len(KVERSES)} of {KANA_TOTAL} verses published so far. The next ones are added one at a time.</small></p>
<h2 id="story">The story before the first verse</h2>

<p>Every great hymn has a story. The Kanakadhāra Stotram is no exception.</p>
<p>More than 1,200 years ago, the young Ādi Śaṅkarācārya, still a boy of about eight in most tellings, went from house to house seeking <em>bhikṣā</em> (alms), as a student and renunciate does. The custom is not about need. Accepting whatever is freely offered cultivates humility in both the giver and the receiver.</p>
<p>One day he arrived at the home of a poor Brahmin family. The lady of the house searched every corner of her kitchen. She had nothing to offer. Nothing, except one small <em>āmalakī</em> (Indian gooseberry): the last edible thing in the house.</p>
<p>She faced a dilemma. Should she keep it for herself and her family, or honour the sacred duty of offering food to a seeker? Her heart chose generosity. She offered that lone gooseberry with complete sincerity.</p>
<p>The young Śaṅkara saw her poverty at once and, more importantly, her boundless generosity. Deeply moved, he composed a spontaneous hymn in praise of Mahālakṣmī, praying that her compassionate glance fall upon this noble woman.</p>
<p>Tradition says that the Goddess first replied that, by the law of karma, the woman had not yet earned enough merit to receive wealth. Śaṅkara, it is said, then appealed not to justice but to compassion. The story is often read as carrying this unspoken argument: if a person who possesses nothing can still give everything, has she not created merit at this very moment?</p>
<p>The Goddess smiled. A shower of golden gooseberries fell upon the humble home. Thus the Kanakadhāra Stotram was born. <em>Kanaka</em> means gold and <em>dhārā</em> means a stream or continuous flow, so <em>Kanakadhārā</em> is “the stream of gold”.</p>

<h2>The first lesson, even before verse one</h2>
<p>Many people take this hymn to be about becoming rich. The story points to something subtler. The miracle did not begin with Lakshmi. It began with the generosity of the poor woman. She gave before she received.</p>
<p>Prosperity does not begin in the wallet. It begins in the heart. Lakshmi is not merely the Goddess of money; she is the Goddess of abundance in every form:</p>
<ul>
<li>Wealth</li><li>Health</li><li>Knowledge</li><li>Virtue</li><li>Beauty</li><li>Courage</li><li>Harmony</li><li>Opportunity</li><li>Contentment</li>
</ul>
<p>Money is only one expression of Śrī.</p>

<h2>A Sanskrit jewel</h2>
<div class="verse">{YANTRA}<p class="deva" lang="sa">श्री</p><p class="iast" lang="sa-Latn">Śrī</p></div>
<p>This is one of the most beautiful words in Sanskrit, and no single English word carries it. <em>Śrī</em> means prosperity, auspiciousness, grace, beauty, radiance, excellence and divine abundance. That is why we say Śrī Rāma, Śrī Kṛṣṇa and Śrī Mahālakṣmī: the word carries the sense of something blessed, noble and flourishing.</p>

<h2>Reflection for today</h2>
<p>Rather than rushing to the first verse, pause with this question:</p>
<p><em>If I had only one gooseberry left, would I have the faith and generosity to offer it?</em></p>
<p>This question is the doorway to the Kanakadhāra Stotram. Śaṅkarācārya invites us to reflect not only on receiving Lakshmi’s blessings, but also on becoming worthy of them.</p>

<h2>Today’s takeaway</h2>
<div class="grid">
<div class="card"><h3>Three Sanskrit words</h3><p><strong>Śrī</strong> (श्री): divine abundance and auspiciousness.<br><strong>Kanaka</strong> (कनक): gold.<br><strong>Dhārā</strong> (धारा): stream or continuous flow.</p></div>
<div class="card"><h3>Philosophical insight</h3><p>True prosperity begins with a generous heart, not a full treasury.</p></div>
<div class="card"><h3>Practice for today</h3><p>Perform one act of giving, whether of time, kindness, knowledge or material help, without expecting anything in return.</p></div>
</div>

<h2>About the text and this commentary</h2>
<p>The number of verses differs between editions: many printed and online versions carry 21 or 22 stanzas, while some scholarly editions of Śaṅkarācārya’s works give a shorter core text. This commentary will follow one clear edition and will say which, so that you can read along with the text you chant from. Each verse will have its Devanāgarī and transliteration, a word-by-word meaning, the full meaning in plain English, deeper insights, a short meditation and a reflection, as in the <a href="/sri-suktam/">Śrī Sūktam</a> series. Verses will be published one at a time.</p>
<p><small>The story is the traditional account; details vary between tellings.</small></p>
</main>''' + foot()
    write("kanakadhara", body, "0.7")

def page_mla():
    t = "Mahalakshmi Ashtakam Lyrics and Meaning in English"
    d = "Mahalakshmi Ashtakam (Mahalaxmi Ashtak) in Sanskrit with transliteration and English meaning: chant the full text, then read each verse word by word."
    parts = [("Mahālakṣmī Aṣṭakam","mahalakshmi-ashtakam/")]
    ld = {"@context":"https://schema.org","@type":"Article","headline":"Mahalakshmi Ashtakam – Lyrics, Transliteration and Meaning in English","author":{"@type":"Person","name":AUTHOR,"url":SITE+"/about/"},"datePublished":"@@PUB@@","dateModified":"@@MOD@@","inLanguage":"en","image":SITE+"/assets/og.png","isAccessibleForFree":True,"mainEntityOfPage":SITE+"/mahalakshmi-ashtakam/","publisher":{"@type":"Person","name":AUTHOR,"url":SITE+"/about/"}}
    dn = str.maketrans("0123456789","०१२३४५६७८९")
    chant = [(v["n"], v["deva"], v["iast"]) for v in MVERSES[:8]]
    dd = MVERSES[8]["deva"].split("<br>"); ii = MVERSES[8]["iast"].split("<br>")
    for k in range(3): chant.append((9+k, dd[2*k]+"<br>"+dd[2*k+1], ii[2*k]+"<br>"+ii[2*k+1]))
    dev = '<p class="ch-dv" lang="sa">इन्द्र उवाच</p>' + "".join(f'<p class="ch-dv" lang="sa">{c[1]}<br><span class="ch-n">॥ {str(c[0]).translate(dn)} ॥</span></p>' for c in chant)
    ias = '<p class="ch-ia"><em>Indra uvāca</em></p>' + "".join(f'<p class="ch-ia" lang="sa-Latn">{c[2]}<br><span class="ch-n">({c[0]})</span></p>' for c in chant)
    rows = "".join(f'<a class="tile" href="/mahalakshmi-ashtakam/{v["slug"]}/"><h3>{lab(v)}</h3><p>{E(v["sub"])}</p></a>' for v in MVERSES)
    copyjs = '<script>try{var b=document.getElementById("copy-deva");b.addEventListener("click",function(){var t=document.getElementById("deva-text").innerText;navigator.clipboard.writeText(t).then(function(){b.textContent="Copied"},function(){b.textContent="Copy not available"})})}catch(e){}</script>'
    body = head(t,d,"mahalakshmi-ashtakam/",ld,"article") + f'<script type="application/ld+json">{json.dumps(bc_ld(parts),ensure_ascii=False)}</script>' + nav("mla") + f'''
<main class="wrap">{crumbs([("Mahālakṣmī Aṣṭakam",None)])}
<h1>Mahālakṣmī Aṣṭakam</h1>
<p class="lede">The Mahalakshmi Ashtakam (also written Mahalaxmi Ashtak or Mahalakshmyashtakam) is an eight-verse hymn to Goddess Mahalakshmi, traditionally ascribed to Indra. Chant the full text below, then read the meaning of each verse.</p>
<p class="crumbs">By {AUTHOR}</p>
<p><a class="btn" href="#chant">Chant the Ashtakam</a><a class="btn ghost" href="/mahalakshmi-ashtakam/verse-1/">Meaning, verse by verse</a></p>
<h2 id="chant">Chant the Ashtakam</h2>
<p>The full hymn in one place, for daily practice. Devanāgarī first, then the same text in Roman transliteration. The meaning of each verse follows further down.</p>
<p><button class="btn ghost" id="copy-deva" type="button">Copy Devanāgarī text</button></p>
<div class="chant"><h3>देवनागरी</h3><div id="deva-text">{dev}</div></div>
<div class="chant"><h3>Transliteration (IAST)</h3>{ias}</div>
<p><small>Verses 9–11 are the phalaśruti, the closing verses on the fruit of reciting the hymn. Many people chant only the first eight. Editions differ in the wording of a few words; where they do, the verse page says so.</small></p>
<h2 id="verses">Meaning, verse by verse</h2>
<div class="grid">{rows}</div>
<h2>About the hymn</h2>
<p>An <em>aṣṭaka</em> is a hymn of eight verses. In the Mahālakṣmī Aṣṭakam each verse ends with the same line, <em>Mahālakṣmi namo ’stu te</em>, “O Mahalakshmi, I bow to you”, so the refrain gives the hymn a steady rhythm for chanting. Tradition ascribes it to Indra, king of the gods, and places it in the Padma Purāṇa; accounts of the occasion differ.</p>
<p>The verses move from the Goddess seated at her sacred seat and worshipped by the gods, to her protection and her gifts, to her nature as the primal power and the mother of the world. The closing three verses describe the fruit of reciting the hymn, as tradition tells it. This commentary reads those as encouragement to practise, and does not promise any outcome.</p>
<p>There is no single rule for how to chant it. Many people recite after a bath, before a lamp and an image of the Goddess, and Fridays and Diwali are popular times. Follow your own family tradition or teacher where they differ from what is written here.</p>
<p><small>This commentary was prepared with AI assistance and reviewed by the author. <a href="/about/">Read more</a>.</small></p>
{ad("index")}
</main>{copyjs}''' + foot()
    write("mahalakshmi-ashtakam", body, "0.9")

def page_verse(i, lst=None, base="sri-suktam", sname="Śrī Sūktam", navkey="sri", total=None, spname=None):
    lst = lst or VERSES
    total = total or len(lst)
    v = lst[i]
    prev = lst[i-1] if i>0 else None
    nxt = lst[i+1] if i+1 < len(lst) else None
    path = f'{base}/{v["slug"]}'
    parts = [(sname,base+"/"),(lab(v),None)]
    sp = spname or plain(sname)
    tail = v["sub"].split(" – ")[1] if " – " in v["sub"] else ""
    v = dict(v)
    v["title"] = f"{sp} Verse {v['n']} Meaning – {opening(v,3)}"
    d1 = f"{sp} Verse {v['n']} ({opening(v,4)}): {plain(tail)}."
    for extra in (" Word-by-word meaning, English translation and a short meditation."," Word-by-word meaning and English translation."," Meaning in English."):
        if len(d1 + extra) <= 158: d1 += extra; break
    v["desc"] = d1
    if v.get("ttl"): v["title"], v["desc"] = v["ttl"], v["dsc"]
    art = {"@context":"https://schema.org","@type":"Article","headline":v["title"],"description":v["desc"],
           "author":{"@type":"Person","name":AUTHOR,"url":SITE+"/about/"},"datePublished":"@@PUB@@","dateModified":"@@MOD@@","inLanguage":"en","image":SITE+"/assets/og.png","isAccessibleForFree":True,
           "mainEntityOfPage":SITE+"/"+path+"/","publisher":{"@type":"Person","name":AUTHOR,"url":SITE+"/about/"}}
    words = "".join(f'<div class="word"><div class="w">{a}<i>{E(b)}</i></div><p class="m">{E(c)}</p><p>{d}</p></div>' for a,b,c,d in v["words"])
    ins = "".join(f'<div class="card"><h3>{E(a)}</h3><p>{b}</p></div>' for a,b in v["insights"])
    med = "".join(f"<li>{E(x)}</li>" for x in v["meditation"])
    medlink = '<a href="#meditation">Meditation</a>' if v["meditation"] else ''
    medsec = f'<h2 id="meditation">Practical meditation</h2>\n<ol>{med}</ol>' if v["meditation"] else ''
    reflink = '<a href="#reflection">Reflection</a>' if v["reflection"] else ''
    refsec = f'<h2 id="reflection">Reflection for today</h2>\n<p>{E(v["reflection"])}</p>' if v["reflection"] else ''
    closesec = f'<p><em>{E(v["closing"])}</em></p>' if v["closing"] else ''
    p = f'<a href="/{base}/{prev["slug"]}/">← {lab(prev)}</a>' if prev else '<span class="off">← Previous</span>'
    n = f'<a href="/{base}/{nxt["slug"]}/">{lab(nxt)} →</a>' if nxt else (f'<a href="/{base}/">All verses →</a>' if v["n"]>=total else f'<span class="off">Verse {v["n"]+1} coming soon →</span>')
    other = ("Kanakadhāra Stotram","kanakadhara") if base=="sri-suktam" else ("Śrī Sūktam","sri-suktam")
    items = "".join(f'<li><a href="/{base}/{x["slug"]}/"{" class=\"on\" aria-current=\"page\"" if x["slug"]==v["slug"] else ""}><b>{x["n"]}</b><span class="t">{E(x["sub"].split(" – ")[0])}</span></a></li>' for x in lst)
    vnav = f'<aside class="vnav" aria-label="Verses"><p class="vn-title"><a href="/{base}/">{sname}</a></p><ol>{items}</ol><p class="vn-other"><a href="/{other[1]}/">{other[0]} →</a></p></aside>'
    vscript = '<script>try{var a=document.querySelector(".vnav a.on");if(a&&a.scrollIntoView&&innerWidth<1100){var o=a.parentNode.parentNode;o.scrollLeft=a.offsetLeft-o.offsetWidth/2+a.offsetWidth/2}}catch(e){}</script>'
    body = head(v["title"],v["desc"],path+"/",art,"article") + f'<script type="application/ld+json">{json.dumps(bc_ld(parts),ensure_ascii=False)}</script>' + nav(navkey) + f'''
<main class="wrap has-vnav">{vnav}<article>
{crumbs([(sname,base+"/"),(lab(v),None)])}
<p class="shri small" lang="sa">श्री</p>
<h1>{v["h1"]}</h1>
<p class="lede">{E(v["sub"])}</p>
<p class="crumbs">By {AUTHOR}</p>
<div class="verse">{YANTRA}<p class="label">Devanāgarī</p><p class="deva" lang="sa">{v["deva"]}</p><p class="iast" lang="sa-Latn">{v["iast"]}</p></div>
{ad("below-verse")}
<nav class="toc" aria-label="On this page"><a href="#words">Word by word</a><a href="#meaning">Meaning</a><a href="#insights">Deeper insights</a>{medlink}{reflink}</nav>
<h2 id="words">Word-by-word meaning</h2>
{words}
<h2 id="meaning">Full meaning</h2>
<blockquote><p>{E(v["meaning"])}</p></blockquote>
<h2 id="insights">Deeper spiritual insights</h2>
{ins}
{medsec}
{refsec}
{closesec}
<p class="crumbs">Terms used here are explained in the <a href="/glossary/">glossary</a>. This commentary was prepared with AI assistance; <a href="/about/">read more</a>.</p>
{ad("end")}
<div class="pager">{p}{n}</div>
</article></main>{vscript}''' + foot()
    write(path, body, "0.9")

ASHTA = [
 ("Ādi Lakshmi","आदिलक्ष्मी","The first, primal Lakshmi",
  "<em>Ādi</em> means first or original. This is Lakshmi as the source from whom the other seven forms flow, often identified with Mahālakṣmī and with Vishnu’s eternal abode. She stands for what is steady beneath all changes of fortune: the sense that prosperity has a source and is not only a matter of luck.",
  "Often shown with a lotus and a flag in two hands, and the other two hands raised in reassurance and in giving."),
 ("Dhana Lakshmi","धनलक्ष्मी","Lakshmi of wealth",
  "<em>Dhana</em> is wealth in the plainest sense: money, gold, savings and the means to live well. In the images this form is the one most clearly linked with coins. The tradition around her is not only “may I have wealth” but also how wealth is earned, held and shared.",
  "Often shown with a pot from which gold coins pour, together with Vishnu’s emblems (discus and conch), a bow and arrow, and a lotus."),
 ("Dhānya Lakshmi","धान्यलक्ष्मी","Lakshmi of grain and food",
  "<em>Dhānya</em> is grain. This form stands for food, good harvests and the quiet abundance of a well-fed home. It is the oldest sense of prosperity: enough to eat, and something to share. It is also a reminder of the farmers and workers behind every meal.",
  "Often shown in green, holding sheaves of crops, fruits, sugarcane and bananas."),
 ("Gaja Lakshmi","गजलक्ष्मी","Lakshmi with the elephants",
  "<em>Gaja</em> is an elephant. Two elephants pouring water over the Goddess is one of the oldest images of Lakshmi in Indian art, found in early sculpture and on ancient coins. It stands for royal grandeur, strength, dignity and the rain that makes the land fertile. Tradition links this form with the recovery of lost glory and standing.",
  "Seated on a lotus, with two elephants lifting water pots over her."),
 ("Santāna Lakshmi","सन्तानलक्ष्मी","Lakshmi of children and lineage",
  "<em>Santāna</em> means offspring and the continuity of a family. This form stands for children, the next generation, and what is handed down: values, skills and a good name along with property. Many families pray to her for the wellbeing of their children.",
  "Often shown with a child on her lap, and pots, a sword and a shield in her hands."),
 ("Dhairya Lakshmi","धैर्यलक्ष्मी","Lakshmi of courage and steadiness",
  "<em>Dhairya</em> is courage, patience and steadiness under pressure. Some lists call this form <em>Vīra</em> Lakshmi, “the heroic”. It stands for the inner strength that keeps a person working through a hard period. Prosperity needs it too: a business or a household often gets through bad years on nerve.",
  "Often shown with weapons and emblems in several hands, in red or orange."),
 ("Vijaya Lakshmi","विजयलक्ष्मी","Lakshmi of victory",
  "<em>Vijaya</em> is victory. Some lists name her <em>Jaya</em> Lakshmi. She stands for success after effort, and for overcoming obstacles, including the inner ones such as fear, laziness and doubt. Victory here is not only winning over others.",
  "Often shown on a lotus with a sword, shield, discus and conch, and a hand raised in reassurance."),
 ("Vidyā Lakshmi","विद्यालक्ष्मी","Lakshmi of knowledge",
  "<em>Vidyā</em> is knowledge and learning. This is the form where Lakshmi and Sarasvatī meet, since knowledge is counted here as a kind of wealth, one that cannot be divided or easily lost. She is remembered by students, teachers, artists and professionals.",
  "Often shown in white, with a book, a lotus and a hand raised in blessing."),
]

def page_ashta():
    t = "Ashtalakshmi Meaning – The Eight Forms of Goddess Lakshmi"
    d = "The Ashtalakshmi, the eight forms of Goddess Lakshmi: Adi, Dhana, Dhanya, Gaja, Santana, Dhairya, Vijaya and Vidya, and what each one stands for."
    parts = [("Aṣṭalakṣmī","ashtalakshmi/")]
    ld = {"@context":"https://schema.org","@type":"Article","headline":t,"author":{"@type":"Person","name":AUTHOR,"url":SITE+"/about/"},"datePublished":"@@PUB@@","dateModified":"@@MOD@@","inLanguage":"en","image":SITE+"/assets/og.png","isAccessibleForFree":True,"mainEntityOfPage":SITE+"/ashtalakshmi/","publisher":{"@type":"Person","name":AUTHOR,"url":SITE+"/about/"}}
    cards = "".join(f'<div class="card"><h3>{i}. {E(n)} <span lang="sa" style="font-family:var(--deva);font-weight:400;color:var(--muted)">· {dv}</span></h3><p class="m" style="font-weight:700;margin:.1em 0 .4em">{E(sub)}</p><p>{body}</p><p><small>{E(img)}</small></p></div>' for i,(n,dv,sub,body,img) in enumerate(ASHTA,1))
    body = head(t,d,"ashtalakshmi/",ld,"article") + f'<script type="application/ld+json">{json.dumps(bc_ld(parts),ensure_ascii=False)}</script>' + nav("") + f'''
<main class="wrap">{crumbs([("Aṣṭalakṣmī",None)])}
<p class="shri small" lang="sa">श्री</p>
<h1>Aṣṭalakṣmī – the eight forms of Lakshmi</h1>
<p class="lede">The Ashtalakshmi (also written Ashta Lakshmi or Ashtalaxmi) are eight forms of Goddess Lakshmi, each standing for a different kind of prosperity. Wealth is one of the eight; the others are a source, food, standing, family, courage, success and knowledge.</p>
<p class="crumbs">By {AUTHOR}</p>
<h2>Why eight?</h2>
<p><em>Aṣṭa</em> means eight. The idea behind the eight forms is that prosperity is not one thing. A person can have money and no peace, or a good family and a struggling business, or learning without a livelihood. Tradition therefore pictures Lakshmi in eight forms, and a worshipper may turn to one or to all of them.</p>
<p>Lists differ a little from one tradition to another. Some name Vīra Lakshmi in place of Dhairya, or Jaya in place of Vijaya, and some lists include Aiśvarya (grandeur) or Saubhāgya (good fortune). The eight below are the most common set. The pictures described are typical ones; temples and paintings differ in the details, and the number of hands varies.</p>
<h2>The eight forms</h2>
{cards}
{ad("below-verse")}
<h2>A way to use the eight</h2>
<p>Read the eight names slowly and ask which one is most present in your life, and which is least. Many people find they have put effort into one or two, usually wealth and knowledge, while courage, family or simple gratitude for food went unattended. This is a reflection inspired by the tradition, and does not promise any outcome.</p>
<p>The Ashtalakshmi are also worshipped together in temples and in the Ashtalakshmi Stotram, a hymn that praises each form in turn. Prosperity in its wider sense is also the theme of the <a href="/sri-suktam/">Śrī Sūktam</a>, the <a href="/kanakadhara/">Kanakadhāra Stotram</a> and the <a href="/mahalakshmi-ashtakam/">Mahālakṣmī Aṣṭakam</a> on this site.</p>
<p><small>This page was prepared with AI assistance and reviewed by the author. <a href="/about/">Read more</a>.</small></p>
{ad("end")}
</main>''' + foot()
    write("ashtalakshmi", body, "0.8")

def page_yantra():
    t = "Sri Yantra Meaning – Layers and Symbolism"
    d = "What the Sri Yantra (Lakshmi Yantra) is and what each layer means: the square enclosure, circle, lotus petals, nine triangles and the central point."
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
    t = "Sanskrit Glossary – Sri Suktam & Lakshmi Stotras"
    d = "Simple meanings of Sanskrit words in the Sri Suktam and Kanakadhara Stotram: Hiranya, Harini, Lakshmi, Jatavedas, Apanga and more."
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
<p>This site uses Google Analytics to understand which pages are read, so the content can be improved. Google Analytics uses cookies and collects data in aggregate, such as pages viewed, approximate location and device type. It is not used to identify individual readers. You can opt out with the <a href="https://tools.google.com/dlpage/gaoptout">Google Analytics opt-out browser add-on</a>, or by blocking cookies in your browser settings.</p>
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
    u = "".join(f'<url><loc>{SITE}/{p + "/" if p else ""}</loc><lastmod>{lm}</lastmod><priority>{pr}</priority></url>' for p,pr,lm in PAGES)
    open(os.path.join(ROOT,"sitemap.xml"),"w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{u}</urlset>\n')

if __name__ == "__main__":
    page_home(); page_sri(); page_kana(); page_mla()
    for i in range(len(VERSES)): page_verse(i)
    for i in range(len(KVERSES)): page_verse(i, KVERSES, "kanakadhara", "Kanakadhāra Stotram", "kana", KANA_TOTAL)
    for i in range(len(MVERSES)): page_verse(i, MVERSES, "mahalakshmi-ashtakam", "Mahālakṣmī Aṣṭakam", "mla", MLA_TOTAL, "Mahalakshmi Ashtakam")
    page_ashta(); page_yantra(); page_gl(); page_about(); page_contact(); page_privacy(); page_404(); assets(); sitemap()
    json.dump(MANIFEST, open(MANIFEST_PATH,"w",encoding="utf-8"), indent=1, ensure_ascii=False)
    print("built", len(PAGES), "pages")
