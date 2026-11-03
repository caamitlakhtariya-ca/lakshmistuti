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
 dict(
  n=3, slug="verse-3",
  deva="विश्वामरेन्द्रपदविभ्रमदानदक्षम्<br>आनन्दहेतुरधिकं मुरविद्विषोऽपि।<br>ईषन्निषीदतु मयि क्षणमीक्षणार्धम्<br>इन्दीवरोदरसहोदरमिन्दिरायाः॥",
  iast="Viśvāmarendra-pada-vibhrama-dāna-dakṣam,<br>Ānanda-hetur adhikaṁ mura-vidviṣo 'pi;<br>Īṣan niṣīdatu mayi kṣaṇam īkṣaṇārdham,<br>Indīvarodara-sahodaram Indirāyāḥ.",
  ttl="Kanakadhara Stotram Verse 3 Meaning – Visvamarendra Pada",
  dsc="Kanakadhara Stotram Verse 3 (Visvamarendra Pada Vibhrama): Lakshmi’s half-glance, Indra’s splendour and Vishnu’s joy. Word-by-word meaning in English.",
  h1="Kanakadhāra Stotram – Verse 3",
  sub="Viśvāmarendra – half a glance, humbly asked",
  words=[
   ("विश्वामरेन्द्रपदविभ्रमदानदक्षम्","Viśvāmarendra-pada-vibhrama-dāna-dakṣam","Skilled in bestowing the splendour of Indra’s station as lord of all the gods","<em>Viśva</em> is all; <em>amara</em> is an immortal, a god; <em>indra</em> is lord, so <em>viśvāmarendra</em> is Indra, king of all the gods. <em>Pada</em> is station or rank; <em>vibhrama</em> is splendour, charm and the glamour of high office; <em>dāna</em> is giving; <em>dakṣa</em> is skilled or able. The final <em>m</em> of <em>dakṣam</em> joins the next word when the verse is recited without a pause (<em>dakṣam</em> + <em>ānanda</em> sounds as <em>dakṣamānanda</em>)."),
   ("आनन्दहेतुः","Ānanda-hetuḥ","A cause of joy","<em>Ānanda</em> is joy, bliss; <em>hetu</em> is cause or source."),
   ("अधिकम्","Adhikam","Abundantly, exceedingly","Read with <em>ānanda</em>: a source of abundant joy. Translators also render it “even more”, but the sense is the same: the joy is great."),
   ("मुरविद्विषः अपि","Mura-vidviṣaḥ api","Even to the foe of Mura (Vishnu)","<em>Mura</em> is the demon of that name; <em>vidviṣ</em> is an enemy, one opposed to. So “the enemy of Mura” is Vishnu, the same Murāri we met in Verse 2. <em>Api</em> is “even” or “also”."),
   ("ईषत् निषीदतु","Īṣat niṣīdatu","May it settle lightly","<em>Īṣat</em> is slightly, a little; <em>niṣīdatu</em> is “may it sit down, may it rest”. The two join as <em>īṣan niṣīdatu</em>. The picture is of something landing gently, as a bird alights."),
   ("मयि क्षणम्","Mayi kṣaṇam","Upon me, for a moment","<em>Mayi</em> is “on me”; <em>kṣaṇa</em> is an instant or a moment."),
   ("ईक्षणार्धम्","Īkṣaṇārdham","Half a glance; a fraction of a look","<em>Īkṣaṇa</em> is a look or glance (from the root <em>īkṣ</em>, to see); <em>ardha</em> is half. This is the thing the poet asks to settle on him."),
   ("इन्दीवरोदरसहोदरम्","Indīvarodara-sahodaram","Akin to the inside of a blue lotus","<em>Indīvara</em> is the blue lotus; <em>udara</em> is the interior (it also means belly); <em>sahodara</em> is literally “born of the same womb”, a sibling, and so “closely resembling”. The word <em>udara</em> appears twice inside this one compound."),
   ("इन्दिरायाः","Indirāyāḥ","Of Indirā (Lakshmi)","<em>Indirā</em> is a name of Lakshmi; the ending marks “of”."),
  ],
  meaning="May even half a glance of Indirā (Lakshmi), a glance able to bestow the splendour of Indra’s station as lord of all the gods, an abundant source of joy even to Vishnu, the foe of Mura, and as soft as the inside of a blue lotus, settle lightly upon me, if only for a moment.",
  insights=[
   ("In simple words","“O Mother Lakshmi, your glance is so powerful that it can give the glory of a heavenly throne, and it brings joy even to Lord Vishnu. I ask for so little in comparison: may a fraction of that glance rest on me for one brief moment and bless my life.” The verse praises the greatness of the glance and then makes the smallest possible request."),
   ("The poetry hidden in the verse","Śaṅkara could have written, “Lakshmi is powerful. Please bless me.” Instead he moves our eyes from the grandeur of a heavenly throne to the delicacy of a single glance. First we picture Indra in the magnificence of his heaven. Then the poet turns to Vishnu, for whom her glance is a source of joy. Finally the grandeur becomes intimate: <em>īṣan niṣīdatu mayi</em>, “may it settle lightly on me”. From the throne of Indra to the humble devotee, from cosmic power to a moment of grace. A poet sees what ordinary eyes miss."),
   ("Three images, one prayer","The verse holds three pictures side by side: the grandeur of Indra, the joy of Vishnu and the soft blue lotus. Power, love and beauty are set around a single glance. The lotus is what softens the majesty of the first lines; it gives the glance something we can see, rather than merely telling us it is beautiful."),
   ("The greatness of the blessing, the humility of the request","The first line speaks of the power to grant Indra’s exalted position. Yet the poet asks for neither a kingdom nor a throne nor riches. He asks for half a glance, resting on him for a moment. The contrast suggests a devotional attitude: the devotee recognises the greatness of the Divine without treating grace as something to be bought or commanded. A useful lesson to carry: approach what you revere with humility, even when your aspirations are large."),
   ("Even the powerful look to grace","In this imagery Indra stands for the highest authority among the gods, and Vishnu for divine majesty and bliss. The verse says her glance can confer Indra’s station and is a joy to Vishnu. The poetic message is that status and power are not the whole story. In everyday life this can remind us that professional success, wealth or authority should not make us forget gratitude, relationships and the sources of our good fortune."),
   ("The meaning of “just a moment”","<em>Kṣaṇam</em> means “for a moment”. The poet’s request is modest in duration but large in aspiration. We often imagine that change must arrive through some grand event, yet a moment of insight, a word of wisdom or an act of compassion can turn the direction of a life. This is a reflection inspired by the verse, not a promise that a brief prayer will automatically change one’s circumstances."),
   ("The blue lotus, and a play on a word","The blue lotus (<em>indīvara</em>) is deeply rooted in Indian devotional and poetic imagery, where it evokes beauty, freshness and quiet colour. Here the comparison is to its inside: the glance is as soft and deep as the inner blue of the flower. There is also a small piece of sound-play. The compound <em>indīvarodara-sahodaram</em> carries <em>udara</em> twice, and it sits next to <em>Indirāyāḥ</em>, so the line opens and closes on a similar sound: <em>Indīvara… Indirā</em>. Reading the verse aloud, one hears how the lotus and the Goddess are tied together."),
   ("How this verse follows Verses 1 and 2","The first two verses showed the glance moving towards Vishnu: a sidelong glance in Verse 1 and a garland of repeated glances in Verse 2. Verse 3 spends most of its lines on how great that glance is, then makes the poet’s request in the shortest form possible, half a glance for a moment. The verses open out gradually: first we see the glance, then we learn its power, and then the devotee dares to ask."),
   ("Grace and effort","The verse asks for divine blessing. It does not prescribe a practical programme for success. We can still carry its spirit into daily life: pray with sincerity, work with integrity, manage resources prudently, and stay humble when circumstances favour us. Grace may inspire our efforts; it should not become an excuse to abandon them."),
   ("Three Sanskrit words to keep","<em>Ānanda</em> is bliss, a deep joy that goes beyond ordinary pleasure. <em>Īkṣaṇa</em> is a glance, the act of seeing, and here it is the very thing the devotee prays for. <em>Dakṣa</em> is capable or skilful; in this verse it describes the Goddess’s ability to bestow great glory."),
   ("How to pronounce the key words","Viśvāmarendra: vish-vaa-ma-ren-dra. Vibhrama: vi-bhra-ma. Dakṣam: dak-sham. Mura-vidviṣaḥ: mu-ra-vid-vi-shah. Īṣan niṣīdatu: ee-shan ni-shee-da-tu. Īkṣaṇārdham: eek-sha-naar-dham. Indīvarodara: in-dee-va-ro-da-ra. Read the verse slowly and give each line time to settle; the aim is understanding, not speed."),
  ],
  meditation=["Minute 1, become still: sit comfortably and breathe naturally. Let the day’s concerns settle; do not force the mind to become empty.",
              "Minutes 2–3, recite the verse: read the Sanskrit slowly, resting on īṣan niṣīdatu mayi kṣaṇam īkṣaṇārdham. Let its meaning settle: may even a fraction of the glance rest upon me for a moment.",
              "Minute 4, visualise the lotus: imagine a blue lotus on still water and let it stand for the beauty and calm of the Goddess’s glance. You need not force a vision; simply hold the image.",
              "Minute 5, offer a prayer. Say silently: “O Mother Lakshmi, may I receive the wisdom to recognise my blessings, the humility to remain grounded and the discernment to use my resources for good.”"],
  reflection="Ambition: am I pursuing success while also building the character needed to handle it? Humility: when things go well, do I remember the people, opportunities and circumstances that helped me? Grace: can I be grateful for what I already have while continuing to work towards what I hope to achieve? I need not answer all three today; I can choose one and let it stay with me through the day.",
  closing="A heavenly throne stands for extraordinary power. Vishnu stands for divine majesty and joy. The blue lotus gives the Goddess’s glance a soft, vivid beauty. Then Śaṅkara turns to his own prayer: may even half a glance rest upon me for a moment. The heart of the verse is not only how much Lakshmi can bestow; it is the humility with which her grace is sought. Aspire greatly, remain humble, and remember that prosperity is most meaningful when it comes with wisdom and gratitude. This meditation is a devotional practice for attention and reflection; it does not promise a supernatural result or guarantee material wealth.",
 ),

 dict(
  n=4, slug="verse-4",
  deva="आमीलिताक्षमधिगम्य मुदा मुकुन्दम्<br>आनन्दकन्दमनिमेषमनङ्गतन्त्रम्।<br>आकेकरस्थितकनीनिकपक्ष्मनेत्रम्<br>भूत्यै भवेन्मम भुजङ्गशयाङ्गनायाः॥",
  iast="Āmīlitākṣam adhigamya mudā Mukundam,<br>Ānanda-kandam animeṣam anaṅga-tantram;<br>Ākekara-sthita-kanīnika-pakṣma-netram,<br>Bhūtyai bhaven mama bhujaṅga-śayāṅganāyāḥ.",
  ttl="Kanakadhara Stotram Verse 4 Meaning – Amilitaksham",
  dsc="Kanakadhara Stotram Verse 4 (Amilitaksham Adhigamya Muda Mukundam): Lakshmi’s loving, unblinking gaze at Vishnu. Word-by-word meaning in English.",
  h1="Kanakadhāra Stotram – Verse 4",
  sub="Āmīlitākṣam – the gaze that rests on Mukunda",
  words=[
   ("आमीलिताक्षम्","Āmīlita-akṣam","With half-closed eyes","<em>Mīlita</em> is closed; the prefix <em>ā</em> softens it to “a little, partly”, so <em>āmīlita</em> is half-shut. <em>Akṣa</em> is the eye. The lids are lowered but not closed: the look of someone taking in something dear."),
   ("अधिगम्य","Adhigamya","Having come to; having come upon","From <em>adhi</em> (towards) and <em>gam</em> (to go): to approach, to reach, to come upon. The ending <em>-ya</em> means “having done”, so the arrival is complete before the next thing happens."),
   ("मुदा","Mudā","With joy, gladly","<em>Mud</em> is delight. The ending means “by, with”, so the coming upon is done with gladness."),
   ("मुकुन्दम्","Mukundam","Mukunda, the one who is looked upon","A name of Vishnu. Tradition explains it as “giver of <em>mukti</em>” (liberation). The final <em>m</em> marks him as the one the glance goes towards."),
   ("आनन्दकन्दम्","Ānanda-kandam","The root, or bulb, of bliss","<em>Ānanda</em> is bliss; <em>kanda</em> is a bulb or tuber, the underground root from which a plant springs. So Mukunda is not simply happy: he is the source from which bliss grows."),
   ("अनिमेषम्","Animeṣam","Unblinking, without a pause","<em>Nimeṣa</em> is a blink, a closing of the eyes; <em>a-</em> negates it. The word sits in the same case as <em>Mukundam</em>, so strictly it goes with him, but translators commonly carry it over to her gaze, which does not turn away. Both readings give the same scene: one steady, absorbed look."),
   ("अनङ्गतन्त्रम्","Anaṅga-tantram","Ruled by Anaṅga (Kāma, Love)","<em>Anaṅga</em> means “without a body”, the name of Kāma, the god of love, who lives on without form after Shiva burned his body. <em>Tantra</em> here is rule or sway, so the compound reads “governed by Love”. Commentators handle this compound in slightly different ways; the plain sense is the look of someone held by love."),
   ("आकेकरस्थितकनीनिकपक्ष्मनेत्रम्","Ākekara-sthita-kanīnika-pakṣma-netram","The eye whose pupil and lashes rest in a narrowed, sidelong look","<em>Ākekara</em> means slightly squinting, a narrowed and sidelong glance (from <em>kekara</em>, squinting); some translators render it as “at the corner of the eye”, and the picture is much the same. <em>Sthita</em> is standing, staying; <em>kanīnikā</em> is the pupil; <em>pakṣma</em> is the eyelash; <em>netra</em> is the eye. The long compound is one picture: the eye in which pupil and lashes stay held in that soft, narrowed pose."),
   ("भूत्यै","Bhūtyai","For prosperity, for flourishing","<em>Bhūti</em> comes from <em>bhū</em>, to be or to become: growth, well-being, prosperity. The ending means “for the sake of”."),
   ("भवेत् मम","Bhavet mama","May it be; for me","<em>Bhavet</em> is the wishing form of <em>bhū</em>: “may it be, may it become”. <em>Mama</em> is “of me, mine”. Together with <em>bhūtyai</em>: “may it become, for my prosperity”. The two join as <em>bhūtyai bhaven mama</em>."),
   ("भुजङ्गशयाङ्गनायाः","Bhujaṅga-śayāṅganāyāḥ","Of the consort of him who rests on the serpent","<em>Bhujaṅga</em> is a serpent; <em>śaya</em> is resting or lying, so “he who rests on the serpent” is Vishnu on Śeṣa. <em>Aṅganā</em> is a woman, a lady, here his consort, Lakshmi. When the two words join, <em>śaya</em> and <em>aṅganā</em> become <em>śayāṅganā</em>. The ending marks “of”."),
  ],
  meaning="May the eye of the consort of Vishnu, who rests on the serpent, become a source of prosperity for me: the eye that, having come upon Mukunda with joy, the root of bliss, gazes at him unblinking and ruled by love, half-closed, with its pupil and lashes held in a narrowed, sidelong look.",
  insights=[
   ("In simple words","“O Mother, I see how you look at Vishnu: with a joy so deep that your eyes are half-closed and your gaze does not move away from him. May that same loving look turn towards me and help my life flourish.” The first three lines paint a picture of love. The last line is the quiet request."),
   ("What the verse actually says","The subject of the verse is her eye. Everything before the last line describes it: the half-closed lids, the steady look, the pupil and lashes in their narrowed pose. Only in the last line does the wish arrive: <em>bhūtyai bhavet mama</em>, “may it be for my prosperity”. The poet never says she looks at <em>him</em>; the glance of her eye is what he hopes will come to him."),
   ("The poetry hidden in the verse","Look at what the poet chooses to show. Not Vishnu’s crown, not the splendour of his heaven, not the ornaments she wears. He shows the smallest movement of her eye: the lowered lids, the lashes, the pupil held to one side. Deep affection is often shown this way, not in words but in how we look at someone. <em>Animeṣam</em>, “unblinking”, makes the look feel continuous; <em>mudā</em>, “with joy”, gives it warmth. A tiny physical detail carries a whole world of feeling."),
   ("Reading the compounds","The first two lines are a chain of describing words in one case: <em>āmīlitākṣam</em>, <em>ānanda-kandam</em>, <em>animeṣam</em>, <em>anaṅga-tantram</em>. Sanskrit can pile up such words so that they flavour one another without a single verb between them. Translators differ on which word describes her and which describes him, and I have noted the difference in the word list. The picture is the same either way: a gaze that rests, steady and glad, on the source of joy."),
   ("The beauty of attention","The verse says she looks at Mukunda with joy and without turning away. What we may reflect on, beyond the verse, is how rarely we give anything that kind of attention. We divide ourselves between work, worry and the next task. This is a reflection inspired by the verse, not a line in it: could our work, or a conversation with someone we love, be better for even five minutes of whole attention?"),
   ("Bliss as a source, not a prize","Mukunda is <em>ānanda-kanda</em>, the root of bliss. The poet turns our eyes towards the source of joy, not towards the things we hope will make us happy. We often think, “When I earn more or solve this problem, then I will be happy.” The verse suggests a different question: while I work for what I need, can I also notice the sources of peace already in my life? This does not ask us to give up ambition. It asks us not to hang all our happiness on the next achievement."),
   ("What bhūti can mean","The verse asks for <em>bhūti</em>: prosperity, flourishing, well-being. For a householder this certainly includes a steady income, the means to support a family and freedom from want. As a wider reflection it may also include sound judgement, healthy relationships, peace of mind and the wisdom to use what we have. These wider meanings are reflections on the word; the Sanskrit itself says only prosperity and flourishing."),
   ("Why ask after describing love?","The poet does not first call her a giver of wealth. He first shows her in a moment of loving absorption, and only then asks. One way to read the order is that prosperity is sought in the presence of grace and joy, not as a possession cut off from them. The verse does not promise that reciting it brings wealth. It offers a devotional ideal: ask for well-being while keeping the heart turned towards something deeper than possessions."),
   ("How this verse follows Verses 1 to 3","The first three verses followed the glance: its sidelong approach in Verse 1, its repeated going and returning in Verse 2, its great power in Verse 3. Verse 4 comes close and looks at the eye itself: the lids, the lashes, the pupil, and the love behind them. After the power of the glance, we see its tenderness."),
   ("Three Sanskrit words to keep","<em>Mudā</em> is joy, doing a thing with a glad heart. <em>Ānanda-kanda</em> is the root of bliss, the source from which joy springs. <em>Bhūti</em> is flourishing: life that grows and prospers."),
   ("How to pronounce the key words","Āmīlitākṣam: aa-mee-li-taak-sham. Adhigamya: a-dhi-gam-ya. Mudā: mu-daa. Mukundam: mu-kun-dam. Ānanda-kandam: aa-nan-da-kan-dam. Animeṣam: a-ni-me-sham. Anaṅga-tantram: a-nang-ga-tan-tram. Ākekara: aa-ke-ka-ra. Kanīnika: ka-nee-ni-ka. Pakṣma: paksh-ma. Bhūtyai: bhoot-yai. Bhujaṅga: bhu-jan-ga. Read slowly and let each line settle."),
  ],
  meditation=["Minute 1, recite: say the verse gently and without hurry, giving each line its own breath.",
              "Minute 2, picture the scene: imagine Vishnu resting on the great serpent and Lakshmi beside him, looking at him with quiet delight. You need not force a vision; let it come as it will.",
              "Minute 3, look at the eyes: rest your attention on her lowered lids and the stillness of her look. Notice how still a loving attention can be.",
              "Minute 4, reflect: ask yourself, “What deserves my whole attention today? What am I pursuing, and why?”",
              "Minute 5, offer a prayer. Say silently: “O Mother Lakshmi, may my life flourish. Give me the wisdom to recognise true happiness, the discernment to use prosperity well and the steadiness to stay grateful as I work for my goals.”"],
  reflection="Attention: when someone I love speaks to me, am I listening, or already busy with something else? Ambition: am I seeking prosperity as a way of living well, or have I made it the only measure of whether my life is going well? Gratitude: what is already valuable in my life that I may be overlooking while I chase the next thing? One honest answer is enough for today.",
  closing="The verse opens with Lakshmi’s eye resting lovingly on Mukunda, the root of bliss, and ends with a humble prayer that her grace may bring flourishing to the devotee. Its beauty is in the contrast: something large is asked for, well-being and prosperity, by drawing our eyes to something very small, a loving look. Perhaps the lesson is to seek not prosperity alone but a life in which prosperity, joy, attention and gratitude can live together. " + "This meditation is a devotional practice for attention and reflection; it does not promise a supernatural result or guarantee material wealth.",
 ),

 dict(
  n=5, slug="verse-5",
  deva="बाह्वन्तरे मधुजितः श्रितकौस्तुभे या<br>हारावलीव हरिनीलमयी विभाति।<br>कामप्रदा भगवतोऽपि कटाक्षमाला<br>कल्याणमावहतु मे कमलालयायाः॥",
  iast="Bāhvantare madhujitaḥ śrita-kaustubhe yā,<br>Hārāvalīva harinīlamayī vibhāti;<br>Kāmapradā bhagavato 'pi kaṭākṣa-mālā,<br>Kalyāṇam āvahatu me kamalālayāyāḥ.",
  ttl="Kanakadhara Stotram Verse 5 Meaning – Bahvantare Madhujitah",
  dsc="Kanakadhara Stotram Verse 5 (Bahvantare Madhujitah): Lakshmi’s garland of glances shining like sapphires on Vishnu’s chest. Word-by-word meaning in English.",
  h1="Kanakadhāra Stotram – Verse 5",
  sub="Bāhvantare – the garland of glances",
  words=[
   ("बाह्वन्तरे","Bāhv-antare","In the space between the arms; on the chest","<em>Bāhu</em> is the arm; <em>antara</em> is the space within or between. The space between the arms is the chest. When <em>bāhu</em> meets <em>antare</em>, the <em>u</em> turns into <em>v</em>: <em>bāhv-antare</em>. The ending means “in, on”."),
   ("मधुजितः","Madhu-jitaḥ","Of the conqueror of Madhu (Vishnu)","<em>Madhu</em> is a demon, who in tradition was slain by Vishnu together with Kaiṭabha. <em>Jit</em> is one who conquers. So <em>Madhujit</em> is “the conqueror of Madhu”, a name of Vishnu. The ending marks “of”."),
   ("श्रितकौस्तुभे","Śrita-kaustubhe","Where the Kaustubha jewel rests","<em>Śrita</em> is one who has taken shelter or settled; <em>Kaustubha</em> is the famous jewel of Vishnu, which tradition says rose from the churning of the ocean and rests on his chest. The word describes the chest: the chest on which the Kaustubha has settled."),
   ("या","Yā","Which (she who, that which)","A feminine “which”. It looks ahead to <em>kaṭākṣa-mālā</em>, the garland of glances, in the third line, and tells us the first two lines are describing that garland."),
   ("हारावलीव","Hārāvalī iva","Like a necklace","<em>Hāra</em> is a necklace or string; <em>āvalī</em> is a row or line; <em>iva</em> is “like”. The words run together as <em>hārāvalīva</em>. A row of jewels strung along the chest."),
   ("हरिनीलमयी","Hari-nīla-mayī","Made of sapphire; deep-blue gem","<em>Nīla</em> is blue; <em>harinīla</em> is the name of a blue gem, usually rendered sapphire. <em>-Mayī</em> means “made of, full of”, and its feminine ending agrees with the garland. So the glances are a necklace of deep-blue jewels."),
   ("विभाति","Vibhāti","Shines, gleams","<em>Bhā</em> is to shine; the prefix <em>vi</em> adds brilliance. This is a plain statement of how the garland looks: it shines. The wish does not come until the last line."),
   ("कामप्रदा","Kāma-pradā","Giver of wishes","<em>Kāma</em> is desire, wish (it can also mean love); <em>prada</em> is giver. The feminine ending agrees with the garland: the garland of glances is the giver."),
   ("भगवतः अपि","Bhagavato ’pi","Even to the Lord (Vishnu)","<em>Bhagavat</em> is the Blessed Lord, here Vishnu. <em>Api</em> is “even”. The two join as <em>bhagavato ’pi</em>. The surprise is in the word “even”: her glance is a giver of wishes to the Lord himself."),
   ("कटाक्षमाला","Kaṭākṣa-mālā","A garland of sidelong glances","<em>Kaṭākṣa</em> is a sidelong, gracious glance; <em>mālā</em> is a garland. This is not a physical necklace but a garland made of glances, the heart of the verse."),
   ("कल्याणम् आवहतु मे","Kalyāṇam āvahatu me","May it bring welfare to me","<em>Kalyāṇa</em> is what is good and auspicious: welfare, well-being. <em>Ā-vah</em> is to bring; <em>āvahatu</em> is “let it bring, may it bring”. <em>Me</em> is “to me”. The words join as <em>kalyāṇam āvahatu me</em>. This is the wish of the whole verse."),
   ("कमलालयायाः","Kamalālayāyāḥ","Of her whose home is the lotus (Lakshmi)","<em>Kamala</em> is the lotus; <em>ālaya</em> is a dwelling. So the one whose dwelling is the lotus is Lakshmi. The ending marks “of”: the garland of glances of Lakshmi."),
  ],
  meaning="May the garland of sidelong glances of Lakshmi, whose home is the lotus, bring welfare to me: the garland which shines like a necklace of sapphires on the chest of Madhujit (Vishnu), where the Kaustubha jewel rests, and which grants wishes even to the Lord himself.",
  insights=[
   ("In simple words","“O Mother, your loving glances shine on Vishnu’s chest like a string of blue sapphires beside the Kaustubha jewel, and they give joy even to the Lord himself. May that same garland of your glances bring goodness into my life.” The first three lines are a picture; only the last line is the prayer."),
   ("What the verse actually says","The grammar is simple once the long compound is unpacked. The subject is the garland of glances. The first two lines say where it shines and how it looks: on the chest of Madhujit, like a sapphire necklace. The third line says what it does: it grants wishes even to the Lord. The wish itself is only in the last line: <em>kalyāṇam āvahatu me</em>, “may it bring welfare to me”. The shining is a statement; the prayer is separate."),
   ("The poetry hidden in the verse","A less daring poet would have put a necklace on Lakshmi. Śaṅkara turns the picture around: her necklace is made of her own glances, and it is worn on Vishnu. Each loving look is a blue gem, and a row of looks becomes a string of jewels. The beauty is not in the ornament but in the affection that makes it. Blue stones lie beside the Kaustubha, and the dark chest and the glowing gem seem to answer one another."),
   ("A picture built across the verses","In <a href=\"/kanakadhara/verse-2/\">Verse 2</a> her repeated glances were a bee moving round a lotus: going, returning, going again. Verse 5 takes those same repeated glances and strings them together. The movement of Verse 2 becomes a lasting ornament. The poet keeps returning to the same few images and lets them grow."),
   ("Madhujit and the Kaustubha","<em>Madhujit</em> is a name of Vishnu from the tradition that he slew the demon Madhu. The Kaustubha is the jewel said to have risen at the churning of the ocean, the same churning in which Lakshmi herself arose. The verse places her glances beside the one jewel that came from the same waters."),
   ("Kāmapradā bhagavato ’pi","The line says her glance grants wishes even to the Lord. A devotional reading is that Lakshmi stands for grace and compassion, inseparable from Vishnu’s power to sustain the world: the divine pair is complete together. The word <em>kāma</em> can also mean love, which gives a second, gentler sense: a glance that brings delight even to him. This is a reading of the imagery, not a claim that the verse sets out a doctrine."),
   ("Grace as an ornament","A necklace is worn to add beauty. Here the ornament is affection itself. We can carry this as a reflection: our titles, possessions and achievements may decorate a life, but kindness, generosity and integrity are what make it beautiful. This is a reflection inspired by the verse, not a line in it."),
   ("What do we truly desire?","<em>Kāmapradā</em> means giver of wishes, and it is tempting to read the verse only as a prayer for wealth. But wishes are many: wealth and also security, success and also fulfilment, recognition and also respect, comfort and also peace. The verse invites us to lay our wishes before the Goddess with humility. It does not say that every wish will come exactly as we imagine; we can also pray for the wisdom to see which wishes are worth pursuing."),
   ("Kalyāṇa: more than money","The last word is not <em>dhana</em> (wealth) but <em>kalyāṇa</em>: goodness, auspiciousness, welfare. A life can have money and still lack <em>kalyāṇa</em>. The poet asks for the larger thing, well-being that includes right living and good relationships, though the Sanskrit itself says only welfare and auspiciousness."),
   ("How to pronounce the key words","Bāhvantare: baah-van-ta-re. Madhujitaḥ: ma-dhu-ji-tah. Śrita-kaustubhe: shri-ta-kaus-tu-bhe. Hārāvalīva: haa-raa-va-lee-va. Harinīlamayī: ha-ri-nee-la-ma-yee. Vibhāti: vi-bhaa-ti. Kāmapradā: kaa-ma-pra-daa. Kaṭākṣa-mālā: ka-taak-sha-maa-laa. Kalyāṇam: kal-yaa-nam. Āvahatu: aa-va-ha-tu. Kamalālayāyāḥ: ka-ma-laa-la-yaa-yaah."),
  ],
  meditation=["Minute 1, recite: say the verse slowly, resting on kāmapradā bhagavato ’pi kaṭākṣa-mālā.",
              "Minute 2, picture the scene: see the Kaustubha jewel shining on Vishnu’s chest, and a garland of Lakshmi’s glances lying beside it like a string of blue gems.",
              "Minute 3, remember kindness: think of the people whose affection, guidance and kindness have enriched your life.",
              "Minute 4, look at your wishes: ask yourself, “Are my ambitions leading me towards a better life, or only towards more possessions?”",
              "Minute 5, offer a prayer. Say silently: “O Mother Lakshmi, may my wishes be guided by wisdom. May my prosperity bring happiness not only to me but to those whose lives touch mine. May my life be filled with kalyāṇa.”"],
  reflection="If Lakshmi’s garland is made of loving glances and not of precious stones, what are the ornaments of my own life? Perhaps the blessings of parents, the affection of family, the trust of colleagues, the ability to help someone in need, the satisfaction of earning honestly. Building wealth is necessary and worthwhile; I can also build a life worthy of the wealth I earn.",
  closing="The verse turns Lakshmi’s loving glances into a necklace of blue gems shining beside the Kaustubha on Vishnu’s chest, and then asks that this garland of grace bring welfare to the devotee. The thought to carry is simple: the finest ornaments of a life are not always the things we own. Sometimes they are the love we receive, the grace we feel and the goodness we share. " + "This meditation is a devotional practice for attention and reflection; it does not promise a supernatural result or guarantee material wealth.",
 ),

 dict(
  n=6, slug="verse-6",
  deva="कालाम्बुदालिललितोरसि कैटभारेः<br>धाराधरे स्फुरति या तडिदङ्गनेव।<br>मातुः समस्तजगतां महनीयमूर्तिः<br>भद्राणि मे दिशतु भार्गवनन्दनायाः॥",
  iast="Kālāmbudāli-lalitorasi Kaiṭabhāreḥ,<br>Dhārādhare sphurati yā taḍid-aṅganeva;<br>Mātuḥ samasta-jagatāṁ mahanīya-mūrtiḥ,<br>Bhadrāṇi me diśatu Bhārgava-nandanāyāḥ.",
  ttl="Kanakadhara Stotram Verse 6 Meaning – Kalambudali Lalitorasi",
  dsc="Kanakadhara Stotram Verse 6 (Kalambudali Lalitorasi): Lakshmi as lightning on Vishnu’s dark cloud-like chest, the Mother of all worlds. Word-by-word meaning.",
  h1="Kanakadhāra Stotram – Verse 6",
  sub="Kālāmbudāli – lightning on the monsoon cloud",
  words=[
   ("कालाम्बुदालिललितोरसि","Kāla-ambuda-āli-lalita-urasi","On the chest, lovely as a bank of dark clouds","<em>Kāla</em> is black or dark; <em>ambuda</em> is a cloud, literally “giver of water” (<em>ambu</em>, water, and <em>da</em>, giving); <em>āli</em> is a row or bank; <em>lalita</em> is charming, graceful; <em>uras</em> is the chest, and the ending means “on”. Together: on the chest that is lovely like a bank of dark clouds. The sounds join as <em>kālāmbudāli-lalitorasi</em>."),
   ("कैटभारेः","Kaiṭabhāreḥ","Of the enemy of Kaiṭabha (Vishnu)","<em>Kaiṭabha</em> is the demon who, in tradition, was slain by Vishnu together with Madhu; <em>ari</em> is an enemy. So <em>Kaiṭabhāri</em> is Vishnu. In Verse 5 he was named by one of the pair, <em>Madhujit</em>; here by the other. The ending marks “of”."),
   ("धाराधरे","Dhārā-dhare","On the rain-bearing cloud","<em>Dhārā</em> is a stream, a falling line of rain; <em>dhara</em> is a bearer. So <em>dhārādhara</em> is “the bearer of streams”, a rain cloud. The ending means “on”: the place where the lightning flashes."),
   ("स्फुरति","Sphurati","Flashes, gleams","The root <em>sphur</em> is to flash, quiver, glint. Like <em>vibhāti</em> in Verse 5, this is a plain statement of how the form appears, not a wish."),
   ("या","Yā","She who; the one which","A feminine “which”. It points forward to the feminine <em>mahanīya-mūrtiḥ</em>, the revered form, in the third line: the form that flashes."),
   ("तडिदङ्गनेव","Taḍid-aṅganā iva","Like lightning pictured as a woman","<em>Taḍit</em> is lightning; <em>aṅganā</em> is a woman, a lady; <em>iva</em> is “like”. The words run together as <em>taḍid-aṅganeva</em>. Lightning is pictured as a lady, so the flash has a figure and a grace. Readers also take it as “a woman bright as lightning”; the picture is the same."),
   ("मातुः समस्तजगताम्","Mātuḥ samasta-jagatām","Of the Mother of all the worlds","<em>Mātṛ</em> is mother; the ending marks “of”. <em>Samasta</em> is all, entire; <em>jagat</em> is world, and <em>jagatām</em> is “of the worlds”. The text writes the last as <em>jagatāṁ</em> when it joins the next word."),
   ("महनीयमूर्तिः","Mahanīya-mūrtiḥ","The form worthy of reverence","<em>Mahanīya</em> is “to be honoured”, from <em>mah</em>, to honour and revere. <em>Mūrti</em> is a form, an embodied shape. This is the thing the poet addresses: her revered form, which shines on the cloud."),
   ("भद्राणि","Bhadrāṇi","Good things, blessings","<em>Bhadra</em> is good, auspicious, fortunate. The plural means “good things”, many kinds of well-being, not one gift."),
   ("मे दिशतु","Me diśatu","May she grant to me","The root <em>diś</em> is to point out, assign, grant. <em>Diśatu</em> is “let her grant, may she bestow”. <em>Me</em> is “to me”. This is the prayer of the verse."),
   ("भार्गवनन्दनायाः","Bhārgava-nandanāyāḥ","Of the daughter of Bhṛgu (Lakshmi)","<em>Bhārgava</em> means belonging to the sage Bhṛgu. <em>Nandanā</em> is a daughter (the masculine <em>nandana</em> is a son), literally one who gives delight. Tradition calls Lakshmi Bhārgavī, born as the daughter of Bhṛgu. The ending marks “of”."),
  ],
  meaning="May the revered form of the Mother of all the worlds, the daughter of Bhṛgu, grant me good things: the form that flashes like a lady of lightning on the rain-bearing cloud that is the chest of Vishnu, the enemy of Kaiṭabha, lovely as a bank of dark clouds.",
  insights=[
   ("In simple words","“O Mother, on Vishnu’s dark chest, which is as lovely as a monsoon cloud, you shine like a flash of lightning. You are the Mother of all the worlds and worthy of all reverence. May you grant me every kind of good.” The first two lines paint the sky. The third lifts the picture to the whole world. The last line is the prayer."),
   ("What the verse actually says","Two comparisons and one prayer. The chest of Vishnu is like a bank of dark rain clouds. Lakshmi’s form flashes on it like lightning. Then comes the wish: <em>bhadrāṇi me diśatu</em>, “may she grant me good things”. As in Verse 5, the shining is a statement, and only the last line is a request."),
   ("The poetry hidden in the verse","Picture a monsoon sky: deep blue, nearly black, heavy with rain. Then, a flash. For a moment the whole cloud is lit from inside, and its darkness shows its beauty. That is how the poet sees Vishnu and Lakshmi. He does not simply say she stands beside him. He turns her into <em>taḍid-aṅganā</em>, lightning pictured as a lady, so that a flash becomes a graceful figure moving across a dark sky. After a necklace of blue gems in Verse 5, the image grows from the chest to the sky."),
   ("From the chest to the whole world","Look at what happens in the third line. We have been looking at a close and tender picture of two divine figures. Then the poet says <em>mātuḥ samasta-jagatām</em>, “of the Mother of all the worlds”. The lightning on one cloud becomes the light of the Mother of the universe. The verse moves in one breath from the intimate to the cosmic."),
   ("Bhārgava-nandanā","Naming Lakshmi as the daughter of Bhṛgu links her to an old line of sages and gives the prayer a personal warmth. The poet is not addressing an abstract idea of wealth. He is calling to a revered Mother by one of the traditional names that people have called her by."),
   ("Light and dark are not enemies","The darkness in this verse is not evil. It is the majestic darkness of a cloud that carries rain. The cloud gives water; the lightning shows its beauty. As a reflection inspired by the image, not a line in the verse, we may notice that a hard season can carry the possibility of renewal. We need not praise suffering to see that a difficult time can sometimes teach patience, resilience and judgement."),
   ("More than the goddess of wealth","The verse calls her Mother of all the worlds, which is far larger than “goddess of money”. Tradition speaks of many forms of abundance that she gives: wealth, food, knowledge, courage, family, victory and more. The <a href=\"/ashtalakshmi/\">Aṣṭalakṣmī page</a> sets out the eight forms people most often name. Seen this way, a prayer to Lakshmi is a prayer for a nourished life, not just a full purse."),
   ("From beauty to blessing","The earlier verses dwelt on her eyes, her glances and her affection. Here the prayer grows. The poet no longer asks only for a moment of her look; he asks <em>bhadrāṇi</em>, the many good things that her presence brings. It reminds us that prayer is not only asking for things; it can also be making ourselves ready for a life of more goodness."),
   ("How this verse follows Verses 1 to 5","The glance, the bee, the power of the look, the eyes and the necklace of glances: the first five verses stayed close to Lakshmi’s eyes and their light. Verse 6 steps back and lets us see the whole figure against the sky. The poet lifts our gaze, one verse at a time, from eyes to chest to cloud and lightning."),
   ("Three Sanskrit words to keep","<em>Taḍit</em> is lightning, a flash of light that shows what was hidden. <em>Mūrti</em> is a form or embodied shape, the visible face of something sacred. <em>Bhadra</em> is good and auspicious, the well-being that makes a life flourish and not only a full one."),
   ("How to pronounce the key words","Kālāmbudāli: kaa-laam-bu-daa-li. Lalitorasi: la-li-to-ra-si. Kaiṭabhāreḥ: kai-ta-bhaa-reh. Dhārādhare: dhaa-raa-dha-re. Sphurati: sphu-ra-ti. Taḍid-aṅganā: ta-did-ang-ga-naa. Mahanīya: ma-ha-nee-ya. Mūrtiḥ: moor-tih. Bhadrāṇi: bha-draa-ni. Diśatu: di-sha-tu. Bhārgava: bhaar-ga-va. Nandanāyāḥ: nan-da-naa-yaah."),
  ],
  meditation=["Minute 1, recite: say the verse slowly, resting on bhadrāṇi me diśatu bhārgava-nandanāyāḥ.",
              "Minute 2, picture the sky: a vast, dark monsoon cloud, quiet and heavy with rain. Then a single flash of light that lights up the whole cloud.",
              "Minute 3, see the Mother: let the light stand for Lakshmi as the Mother of all worlds, a sign of nourishment, compassion and abundance. You need not force a vision.",
              "Minute 4, reflect: think of one difficult situation in your life and ask what patience, courage or wisdom would help you meet it.",
              "Minute 5, offer a prayer. Say silently: “O Mother of all worlds, may your light guide my decisions. May there be prosperity in my home, wisdom in my work, compassion in my heart and auspiciousness in all I undertake.”"],
  reflection="Clarity: where in my life do I most need a flash of clarity? Measure: am I judging prosperity only by financial growth? Rain: can I use what I have gained to nourish and support others, as rain nourishes the earth? Wealth is most meaningful when it creates something good beyond ourselves. One honest answer is enough for today.",
  closing="In one image Śaṅkara sets the dark cloud of Vishnu and the flash of Lakshmi side by side, and the sky becomes a picture of divine abundance. Then the picture opens out: she is the Mother of all the worlds, and the poet asks her for every kind of good. The thought to carry is that real prosperity is not only the growth of wealth; it is the arrival of light, wisdom, nourishment and goodness in a life. " + "This meditation is a devotional practice for attention and reflection; it does not promise a supernatural result or guarantee material wealth.",
 ),

 dict(
  n=7, slug="verse-7",
  deva="प्राप्तं पदं प्रथमतः खलु यत्प्रभावान्<br>माङ्गल्यभाजि मधुमाथिनि मन्मथेन।<br>मय्यापतेत्तदिह मन्थरमीक्षणार्धं<br>मन्दालसं च मकरालयकन्यकायाः॥",
  iast="Prāptaṁ padaṁ prathamataḥ khalu yat-prabhāvān<br>Māṅgalya-bhāji madhu-māthini manmathena;<br>Mayy āpatet tad iha mantharam īkṣaṇārdhaṁ<br>Mandālasaṁ ca makarālaya-kanyakāyāḥ.",
  ttl="Kanakadhara Stotram Verse 7 Meaning – Praptam Padam",
  dsc="Kanakadhara Stotram Verse 7 (Praptam Padam): the slow half-glance of Lakshmi that gave Manmatha a footing in Vishnu. Word-by-word meaning in English.",
  h1="Kanakadhāra Stotram – Verse 7",
  sub="Prāptaṁ padaṁ – the slow half-glance and its power",
  words=[
   ("प्राप्तम्","Prāptam","Has been obtained","From <em>pra</em> and <em>āp</em>, to reach or gain. It is a past participle: “has been gained”. It goes with the next word: a footing has been gained."),
   ("पदम्","Padam","A footing, a place","<em>Pada</em> is a foot, a step, and so a place to stand, a position. Here it is the footing that Manmatha gained."),
   ("प्रथमतः","Prathamataḥ","At first","<em>Prathama</em> is first; the ending <em>-taḥ</em> gives “from the first, at first”. It says that this was where it began."),
   ("खलु","Khalu","Indeed","A small word for emphasis: “indeed, surely”."),
   ("यत्प्रभावात्","Yat-prabhāvāt","By the power of which","<em>Yat</em> is “which” and points forward to <em>tad īkṣaṇārdham</em>, “that half-glance”, in the second line: it is the glance whose power is meant. <em>Prabhāva</em> is power, might, influence (from <em>pra</em> and <em>bhū</em>, to come forth). The ending means “by”. Before the next word, which begins with <em>m</em>, the final <em>t</em> becomes <em>n</em>: <em>prabhāvān māṅgalya-</em>."),
   ("माङ्गल्यभाजि","Māṅgalya-bhāji","In him who shares in auspiciousness","<em>Māṅgalya</em> is auspiciousness, good fortune; <em>bhāj</em> means sharing in, having a part of. So he is the auspicious one. The ending means “in”."),
   ("मधुमाथिनि","Madhu-māthini","In the crusher of Madhu","<em>Madhu</em> is the name of a demon in the Vishnu tradition; <em>māthin</em> is one who churns or crushes (from <em>math</em>). So this is Vishnu. The next word tells who found a footing in him. The ending means “in”."),
   ("मन्मथेन","Manmathena","By Manmatha, the god of love","<em>Manmatha</em> is a name of Kāma, the god of love and desire. A traditional explanation is that it means “one who churns the mind” (<em>manas</em>, mind, and <em>matha</em>, churning). The ending means “by”: he is the one who gained the footing."),
   ("मयि","Mayi","On me","“In me, on me”. Before <em>āpatet</em> it is written <em>mayy</em>."),
   ("आपतेत्","Āpatet","May it fall","From <em>ā</em> (towards) and <em>pat</em> (to fall): to alight, to come down upon. The ending makes it a wish: “may it fall”. The poet’s one request."),
   ("तत्","Tat","That","It points to the half-glance of the second line, whose power the first line has just described."),
   ("इह","Iha","Here","“Here, in this place”. He asks that it fall here, upon him as he stands."),
   ("मन्थरम्","Mantharam","Slow","<em>Manthara</em> describes a slow, unhurried movement; in Sanskrit it can also mean lingering or dull. Here it is the quality he asks of the glance: slow, not quick."),
   ("ईक्षणार्धम्","Īkṣaṇārdham","Half a glance","<em>Īkṣaṇa</em> is a look, a glance, from <em>īkṣ</em>, to see; <em>ardha</em> is half. The words join as <em>īkṣaṇārdham</em>. The same word was used in <a href=\"/kanakadhara/verse-3/\">Verse 3</a>."),
   ("मन्दालसम्","Mandālasam","Slow and languid","<em>Manda</em> is slow, gentle; <em>ālasa</em> is languid, unhurried, as though relaxed and half asleep. The words join as <em>mandālasam</em>. It adds a softer, more drowsy slowness to <em>mantharam</em>."),
   ("च","Ca","And","Joins the two descriptions of the glance."),
   ("मकरालयकन्यकायाः","Makarālaya-kanyakāyāḥ","Of the daughter of the ocean","<em>Makara</em> is a sea creature of Indian myth, often shown like a crocodile; <em>ālaya</em> is an abode. So <em>makarālaya</em> is “the home of the makara”: the ocean. <em>Kanyakā</em> is a girl, a daughter. The ending means “of”: she is Lakshmi, born from the ocean."),
  ],
  meaning="May that slow and languid half-glance of the ocean’s daughter, by whose power Manmatha first gained a footing in the auspicious Vishnu, the crusher of Madhu, fall upon me here.",
  insights=[
   ("In simple words","“O Mother, your glance once did something wonderful: through its power the god of love first found a footing in Vishnu himself. May that same glance, slow and soft and only half-given, fall on me.” The poet shows what her glance can do, and then asks for it in its smallest form."),
   ("What the verse actually says","The verse is one sentence in two parts. The first part says what the glance has done: by its power Manmatha first gained a footing in Vishnu. The second part is the wish: may that slow, languid half-glance of the ocean’s daughter fall on me here. The word <em>yat</em> (“by whose”) ties the two together: it is the glance itself, not only the Goddess, whose power is meant."),
   ("The poetry hidden in the verse","Picture the scene the verse describes. Vishnu sits serene and complete in his own abode, and Lakshmi is beside him. Somewhere in this world is Manmatha, the god of love, with his bow of sugarcane and his arrows of flowers, the picture tradition gives of desire and attraction. Then the poet makes a quiet claim: it was by the power of her glance that even Manmatha first gained a footing in Vishnu. \n\nNotice the turn. Verses 1 to 6 showed us the beauty of her glance; now we see its influence. And then comes the most delicate part of the verse. Having shown how great the power is, the poet asks for the smallest piece of it: <em>mantharam īkṣaṇārdham</em>, a slow half-glance. \n\nImagine standing before a great queen. She need not speak or make a grand gesture; a small movement of her eyes is enough to say that you have been seen and welcomed. That is the feeling of this verse. The scene is an imagined picture to help us enter the verse, not something the verse itself states in these words. The poet does not demand attention and does not claim a right. He asks that even a fraction of her loving attention fall on him, and in that there is both humility and a great confidence in grace."),
   ("Manmatha and Vishnu","<em>Manmatha</em> is the god of love, shown with a bow of sugarcane and arrows of flowers. The verse says that through the power of her glance he first gained a place in Vishnu. A common reading is that her look is what made love take hold in the Lord. The verse does not tell the story, and commentators read it a little differently, but the point is the same: if her glance can move even Vishnu, its power is beyond doubt. Note that the page says “a footing in Vishnu”, not “in his heart”: the verse says <em>padam</em>, a place or footing, and leaves the place unnamed."),
   ("The sound of the verse","Listen for the sound <em>m</em>. Eight words or word-parts begin with <em>ma-</em> or <em>mā-</em>: <em>māṅgalya</em>, <em>madhu</em>, <em>māthini</em>, <em>manmathena</em>, <em>mayy</em>, <em>mantharam</em>, <em>mandālasam</em>, <em>makarālaya</em>. There is also a small play on words: <em>madhu-māthin</em> and <em>manmatha</em> both contain the root <em>math</em>, to churn or crush. One is the crusher of Madhu, and the other, by the traditional explanation, churns the mind."),
   ("Three kinds of slowness","The glance is described three ways. <em>Mantharam</em> is slow, unhurried. <em>Mandālasam</em> is slow and languid, relaxed to the point of drowsiness. <em>Īkṣaṇārdham</em> is only half a glance. Nothing in these words is quick, strong or complete. The poet asks for a look that is gentle and small, and trusts that it is enough."),
   ("An echo of Verse 3","The half-glance <em>īkṣaṇārdham</em> is not new. In <a href=\"/kanakadhara/verse-3/\">Verse 3</a> the poet asked that it rest on him for a moment. Here the same half-glance returns with a reason: now we have been told what it can do. After hearing of its power, the request for just a little of it carries more weight."),
   ("Asking from what has been seen","The shape of the argument is simple. The glance gave Manmatha a place in Vishnu, so surely it can do something for me. That is how many prayers work: not by claiming a right, but by pointing to what grace has already done and asking for a share. As a reflection: humility can be strong in this way. It does not demand; it remembers."),
   ("The daughter of the ocean","<em>Makarālaya-kanyakā</em> is another name for Lakshmi as the ocean’s daughter, as in <a href=\"/kanakadhara/verse-2/\">Verse 2</a>. In the tradition she rose from the churning of the ocean. The ocean is a picture of depth and hidden treasure, and the verse, which began with the power of her glance, ends by naming where she came from. This is a mythological association, not a historical claim."),
   ("Desire and its direction","Manmatha stands for desire and attraction. The verse does not condemn him; it says her glance gave him a footing in Vishnu. As a reflection, and not a statement of the verse: desire is a strong force, and the question is what guides it. The wish to earn can become the wish to create something of value. The wish for recognition can become the wish to do work that matters."),
   ("Three Sanskrit words to keep","<em>Prabhāva</em> is power, influence. <em>Manmatha</em> is the god of love, “the mind-churner”. <em>Manthara</em> is slow, unhurried."),
   ("How to pronounce the key words","Prāptam: praap-tam. Padam: pa-dam. Prathamataḥ: pra-tha-ma-tah. Khalu: kha-lu. Yat-prabhāvāt: yat-pra-bhaa-vaat. Māṅgalya-bhāji: maang-gal-ya-bhaa-ji. Madhu-māthini: ma-dhu-maa-thi-ni. Manmathena: man-ma-the-na. Mayi: ma-yi. Āpatet: aa-pa-tet. Mantharam: man-tha-ram. Īkṣaṇārdham: ee-ksha-naar-dham. Mandālasam: man-daa-la-sam. Makarālaya-kanyakāyāḥ: ma-ka-raa-la-ya-kan-ya-kaa-yaah."),
  ],
  meditation=["Minute 1, recite: say slowly, mayy āpatet tad iha mantharam īkṣaṇārdham, and let the words settle.",
              "Minute 2, picture: Lakshmi seated beside Vishnu, and her gaze, slow and kind, turning gently.",
              "Minute 3, silence: sit quietly and ask for nothing yet. Simply stand before her in your mind.",
              "Minute 4, examine desire: ask yourself, “Which of my ambitions deserve my energy? Which need to be refined, or let go?”",
              "Minute 5, offer a prayer. Say silently: “O Mother Lakshmi, may your grace guide my wishes. May I work with care, stay humble in success and use whatever I gain for the good of others.”"],
  reflection="Influence: who has changed my course by a small, kind act, and have I done that for someone? Humility: when I ask for something, do I remember what I have already received? Desire: which of my wishes would I choose again if I looked at them slowly? One honest answer is enough for today.",
  closing="The poet first shows the power of her glance, powerful enough to give the god of love a footing in Vishnu. Then he asks only for the smallest, slowest portion of it. The thought to carry is that grace need not be loud to be strong, and that asking quietly is a way of trusting it. " + "This meditation is a devotional practice for attention and reflection; it does not promise a supernatural result or guarantee material wealth.",
 ),

 dict(
  n=8, slug="verse-8",
  deva="दद्याद्दयानुपवनो द्रविणाम्बुधाराम्<br>अस्मिन्नकिञ्चनविहङ्गशिशौ विषण्णे।<br>दुष्कर्मघर्ममपनीय चिराय दूरं<br>नारायणप्रणयिनीनयनाम्बुवाहः॥",
  iast="Dadyād dayānupavano draviṇāmbudhārām,<br>Asminn akiñcana-vihaṅga-śiśau viṣaṇṇe;<br>Duṣkarma-gharmam apanīya cirāya dūram,<br>Nārāyaṇa-praṇayinī-nayanāmbuvāhaḥ.",
  ttl="Kanakadhara Stotram Verse 8 Meaning – Dadyad Dayanupavano",
  dsc="Kanakadhara Stotram Verse 8 (Dadyad Dayanupavano): Lakshmi’s eyes as rain clouds and the devotee as a helpless young bird. Word-by-word meaning in English.",
  h1="Kanakadhāra Stotram – Verse 8",
  sub="Dadyād dayānupavano – the cloud and the fledgling",
  words=[
   ("दद्यात्","Dadyāt","May it give","From the root <em>dā</em>, to give. The ending makes it a wish: “may it give, let it give”. It is the main verb of the verse; everything else says who gives, what is given, to whom and what is driven away. Before the next word it is written <em>dadyād</em>."),
   ("दयानुपवनः","Dayā-anupavanaḥ","The one whose favouring breeze is compassion","<em>Dayā</em> is compassion; <em>anu</em> is “along, following”; <em>pavana</em> is wind. An <em>anupavana</em> is a wind that carries something along, a favourable breeze. A cloud goes where the wind sends it; the poet’s picture is a cloud that compassion itself drives towards the one who needs it. The words join as <em>dayānupavanaḥ</em>."),
   ("द्रविणाम्बुधाराम्","Draviṇa-ambu-dhārām","A stream of the water of wealth","<em>Draviṇa</em> is wealth, goods, riches; <em>ambu</em> is water; <em>dhārā</em> is a stream or a falling shower. So the shower is of water that is wealth: wealth falling like rain. The final <em>m</em> marks it as the thing given."),
   ("अस्मिन्","Asmin","On this one","The “on” form of <em>idam</em>, “this”. The poet points to himself: on this one, here."),
   ("अकिञ्चनविहङ्गशिशौ","Akiñcana-vihaṅga-śiśau","On the young bird that has nothing","<em>Kiñcana</em> is “anything”, so <em>akiñcana</em> is one who has not even a little, who has nothing. <em>Vihaṅga</em> is a bird, one who goes through the sky. <em>Śiśu</em> is a child, a young one, a fledgling. The ending means “on”. The devotee is pictured as a nestling with nothing of its own."),
   ("विषण्णे","Viṣaṇṇe","Dejected, in distress","From <em>vi</em> and <em>sad</em>, to sit: to sit sunk down in sorrow. The ending agrees with the fledgling: on the one who sits there, downcast."),
   ("दुष्कर्मघर्मम्","Duṣkarma-gharmam","The heat of evil deeds","<em>Duṣ-</em> is bad; <em>karma</em> is a deed or action, so <em>duṣkarma</em> is a wrong or harmful act. <em>Gharma</em> is heat, the scorching heat of the sun. The compound pictures the results of wrong action as a burning heat. The final <em>m</em> marks it as what is carried away."),
   ("अपनीय","Apanīya","Having carried away, having removed","From <em>apa</em> (away) and <em>nī</em> (to lead): to lead away, take off. The ending <em>-ya</em> means “having done”."),
   ("चिराय","Cirāya","For a long time","<em>Cira</em> is long (in time). It tells us the relief is hoped to last, not to pass at once."),
   ("दूरम्","Dūram","Far away","Used as an adverb: the heat is to be driven far off, not merely eased."),
   ("नारायणप्रणयिनीनयनाम्बुवाहः","Nārāyaṇa-praṇayinī-nayana-ambuvāhaḥ","The water-carrying cloud that is the eyes of Nārāyaṇa’s beloved","<em>Nārāyaṇa</em> is a name of Vishnu. <em>Praṇayinī</em> is a beloved, a woman who is loved (from <em>praṇaya</em>, affection). <em>Nayana</em> is the eye. <em>Ambu</em> is water and <em>vāha</em> carrying, so <em>ambuvāha</em> is “carrier of water”, a rain cloud. The poet does not say the eyes are <em>like</em> a cloud: they are the cloud. This is the grammatical subject, the giver. The words join as <em>nayanāmbuvāhaḥ</em>."),
  ],
  meaning="May the water-bearing cloud that is the eyes of Nārāyaṇa’s beloved, with compassion as its favouring breeze, having driven the heat of evil deeds far away for a long time, give a stream of wealth like falling rain to this distressed young bird who has nothing.",
  insights=[
   ("In simple words","“O Mother, your eyes are clouds heavy with water, and compassion is the wind that carries them. I am a helpless young bird with nothing, sitting in the heat of my own wrong deeds. Let the cloud come to me, take away the heat and send down a rain of wealth.” The poet does not praise himself. He shows himself exactly as he is: in need."),
   ("What the verse actually says","Five pictures stand side by side. Her eyes are the cloud. Compassion is the wind that drives it. Wealth is the rain. The devotee is a young bird with nothing. The results of wrong deeds are a scorching heat. The one wish is <em>dadyāt</em>, “may it give”, and the verse says what is given (a stream of wealth), to whom (the fledgling) and what goes away (the heat). Note that the heat of evil deeds is to be driven away, not denied: the verse names it."),
   ("The poetry hidden in the verse","Picture a nestling in the heat of the sun. It cannot fly far or find its own food. It has nothing. Then far away a cloud gathers and a wind begins to carry it nearer. The bird cannot make it rain; it can only wait. Śaṅkara turns this whole scene into a prayer, and the effect is unlike the earlier verses. We have been admiring a goddess of beauty and splendour; now we are with a very small creature waiting for rain. The hymn comes down from the heights of Vaikuṇṭha to a nest."),
   ("Why rain?","Rain is generous in a particular way. It falls on the dry field and the green field alike and does not first ask whether the ground has earned it. That is a reflection on the image, not a line in the verse, but it explains why the poet chose it. He longs for grace that gives freely, and he describes wealth not as something kept in a pot but as something that falls, spreads and gives life."),
   ("The young bird with nothing","<em>Akiñcana</em> is a strong word: one who has not even a little. The poet calls himself that, and a fledgling too. Sanskrit poets often picture the <em>cātaka</em>, the bird said to drink only raindrops, waiting for the cloud; this verse says only “young bird”, but the feeling is the same. As a reflection: there are moments when our knowledge, money and influence are simply not enough. To admit that is not weakness; it is honesty. We can work hard and plan well and still accept that we cannot control every result."),
   ("The heat of evil deeds","<em>Duṣkarma-gharma</em> pictures the results of wrong action as a burning heat. The prayer is not for the deeds to be forgotten or for responsibility to be waved away. A fair reading is that it asks for relief, a cooling, and the strength to live differently. Grace and personal responsibility need not be opposites; we may pray for relief and still set right what we have done."),
   ("Wealth as rain, not as a hoard","The verse gives us two ways to see wealth. One is to collect it and guard it. The other is to see it as rain: it falls, it feeds, it moves on. Rain is valuable for what it sustains, the plants, the animals and the people. Taking the picture as a reflection, not a rule in the verse, wealth has a larger purpose when it supports families, creates opportunities and helps those in need, and prosperity does best when it circulates, not when it stands in a closed vessel."),
   ("Compassion as the wind","The small phrase <em>dayā-anupavana</em> is easy to miss. The cloud needs the wind to reach us. The poet suggests that Lakshmi’s eyes hold the water, but it is compassion that carries it. This is also true among people: resources alone do not help anyone until kindness moves them to where they are needed."),
   ("How this verse follows the earlier ones","In <a href=\"/kanakadhara/verse-3/\">Verse 3</a> the poet asked, humbly, for only half a glance. Here the request grows in feeling, not in size: he wants the glance to become a shower. The earlier verses studied the beauty and power of her eyes. This one turns those same eyes into clouds that bring relief to a living creature."),
   ("Three Sanskrit words to keep","<em>Dayā</em> is compassion: the willingness to see suffering and answer it with kindness. <em>Akiñcana</em> is one who possesses nothing, a word for complete helplessness. <em>Ambuvāha</em> is a water-carrier, a cloud; here a picture of the Goddess’s eyes."),
   ("How to pronounce the key words","Dadyād: dad-yaad. Dayānupavanaḥ: da-yaa-nu-pa-va-nah. Draviṇāmbudhārām: dra-vi-naam-bu-dhaa-raam. Akiñcana: a-kin-cha-na. Vihaṅga: vi-hang-ga. Śiśau: shi-shau. Viṣaṇṇe: vi-shan-ne. Duṣkarma-gharmam: dush-kar-ma-ghar-mam. Apanīya: a-pa-nee-ya. Cirāya: chi-raa-ya. Nārāyaṇa-praṇayinī: naa-raa-ya-na-pra-na-yi-nee. Nayanāmbuvāhaḥ: na-ya-naam-bu-vaa-hah."),
  ],
  meditation=["Minute 1, recite: say the last line slowly, nārāyaṇa-praṇayinī-nayanāmbuvāhaḥ, and think of her eyes as clouds filled with compassion.",
              "Minute 2, picture the scene: a young bird waiting in the heat, and dark clouds gathering. Then a gentle rain begins to fall.",
              "Minute 3, look inward: name one area of your life where you feel uncertain, exposed or in need of support.",
              "Minute 4, look outward: ask yourself, “Is there someone near me who is waiting for a little help, as that bird waits for rain?”",
              "Minute 5, offer a prayer. Say silently: “O Mother Lakshmi, take away the heat of my past mistakes. Give me the strength to set my actions right, the wisdom to decide better and the generosity to become a source of relief for others.”"],
  reflection="Limits: where in my life do I need to accept that I cannot control everything? Past actions: are there mistakes whose consequences I should address and not merely regret? Relief: can I be a source of relief for someone who is struggling? Perhaps I cannot always make it rain, but I can often carry an umbrella for someone else. One honest answer is enough for today.",
  closing="Here the poet gives up every claim. He is a young bird with nothing, waiting under a hot sky, and he asks that the eyes of Lakshmi become clouds and send rain. The thought to carry is that humility opens the heart to compassion, and that whatever abundance reaches us is best treated as rain: something to receive gratefully and pass on to others who are thirsty. " + "This meditation is a devotional practice for attention and reflection; it does not promise a supernatural result or guarantee material wealth.",
 ),
 dict(
  n=9, slug="verse-9",
  deva="इष्टा विशिष्टमतयोऽपि यया दयार्द्र-<br>दृष्ट्या त्रिविष्टपपदं सुलभं लभन्ते।<br>दृष्टिः प्रहृष्टकमलोदरदीप्तिरिष्टां<br>पुष्टिं कृषीष्ट मम पुष्करविष्टरायाः॥",
  iast="Iṣṭā viśiṣṭa-matayo 'pi yayā dayārdra-<br>dṛṣṭyā triviṣṭapa-padaṁ sulabhaṁ labhante;<br>Dṛṣṭiḥ prahṛṣṭa-kamalodara-dīptir iṣṭāṁ<br>puṣṭiṁ kṛṣīṣṭa mama puṣkara-viṣṭarāyāḥ.",
  ttl="Kanakadhara Stotram Verse 9 Meaning – Ishta Vishishtamatayo",
  dsc="Kanakadhara Stotram Verse 9 (Ishta Vishishtamatayo): Lakshmi’s kind glance, bright as an open lotus, and a prayer for nourishment. Word-by-word meaning.",
  h1="Kanakadhāra Stotram – Verse 9",
  sub="Iṣṭā viśiṣṭa-matayaḥ – the glance and the prayer for puṣṭi",
  words=[
   ("इष्टाः","Iṣṭāḥ","The cherished ones; the devoted","<em>Iṣṭa</em> means desired, dear, cherished; it is also used for what is honoured by worship. Here it describes the people who are meant: those dear to her, or devoted to her. Readers differ on the exact shade. In the verse it appears as <em>iṣṭā</em>, because the final visarga falls away before the next word."),
   ("विशिष्टमतयः","Viśiṣṭa-matayaḥ","Those of distinguished understanding","<em>Viśiṣṭa</em> is distinguished, excellent, set apart; <em>mati</em> is mind, understanding, intelligence. So these are people of fine understanding. Note the beginning of the word: it is <em>viśiṣṭa</em>, not <em>aviśiṣṭa</em>. Run together with the next word it becomes <em>matayo ’pi</em>."),
   ("अपि","Api","Even; also","A small word that adds “even, too”. Here it is joined to the previous word as <em>-yo ’pi</em>, where the apostrophe marks a vowel that has merged."),
   ("यया","Yayā","By which","A feminine “by which”, agreeing with <em>dṛṣṭyā</em> (glance): by which glance."),
   ("दयार्द्रदृष्ट्या","Dayārdra-dṛṣṭyā","By the glance moist with compassion","<em>Dayā</em> is compassion; <em>ārdra</em> is moist, tender, softened; <em>dṛṣṭi</em> is a look or glance. The picture is of a look so full of compassion that it is wet with it. The ending means “by”: it is by this glance that the next thing happens."),
   ("त्रिविष्टपपदम्","Triviṣṭapa-padam","The station of heaven","<em>Triviṣṭapa</em> is heaven, the celestial world. <em>Pada</em> is a place, a station, a standing. The traditional meaning is the heavenly state or world."),
   ("सुलभम्","Sulabham","Easily","<em>Su-</em> is good or well; <em>labha</em> is getting. So <em>sulabha</em> is easy to obtain, easily had. Here it is used as an adverb: they get it with ease."),
   ("लभन्ते","Labhante","They obtain","From <em>labh</em>, to obtain. The plural subject is the devoted and the wise named at the start of the verse."),
   ("दृष्टिः","Dṛṣṭiḥ","The glance","The subject of the second half. From <em>dṛś</em>, to see. This is the same glance that the first half has described."),
   ("प्रहृष्टकमलोदरदीप्तिः","Prahṛṣṭa-kamala-udara-dīptiḥ","With the radiance of the interior of a fully open lotus","<em>Prahṛṣṭa</em> is thrilled, delighted; for a flower, it suggests fully open, as if bristling with joy. <em>Kamala</em> is lotus. <em>Udara</em> is the inside, the middle, the body of something; for a lotus, its centre. <em>Dīpti</em> is brightness, shining. The glance has the glow of the heart of an open lotus. The words join as <em>kamalodara</em>."),
   ("इष्टाम्","Iṣṭām","The desired","The same word <em>iṣṭa</em> as at the start of the verse, now in the singular, describing <em>puṣṭi</em>: the nourishment that is wished for."),
   ("पुष्टिम्","Puṣṭim","Nourishment, thriving","<em>Puṣṭi</em> is nourishment, fullness, growth, flourishing; it is the word for becoming well-fed and well-grown, in body, family and life. See <a href=\"/sri-suktam/verse-13/\">Śrī Sūktam Verse 13</a>, where the same word appears."),
   ("कृषीष्ट","Kṛṣīṣṭa","May it bring about","A form of <em>kṛ</em>, to do or make, used for a blessing or wish: “may it make, may it bring about”. It is the verb of the second half."),
   ("मम","Mama","For me; my","“Of me, mine”. It tells us who the prayer is for."),
   ("पुष्करविष्टरायाः","Puṣkara-viṣṭarāyāḥ","Of her whose seat is a lotus","<em>Puṣkara</em> is a lotus; <em>viṣṭara</em> is a seat. So she is the one who sits on a lotus: Lakshmi. The ending means “of”: the glance belongs to her."),
  ],
  meaning="Even people who are cherished and of distinguished understanding gain the station of heaven easily by her glance, moist with compassion. May that glance of the lotus-seated Goddess, bright as the interior of a fully open lotus, bring about for me the nourishment I desire.",
  insights=[
   ("In simple words","“O Mother, the wise and the devoted reach the highest places easily by your compassionate look. Let that same look, shining like the heart of an open lotus, give me the growth and nourishment I wish for.” After the picture of the helpless bird in Verse 8, the poet speaks of a goal he can name: <em>puṣṭi</em>."),
   ("What the verse actually says","The first half is a statement: those who are cherished and of excellent understanding obtain heaven easily through her glance. The second half is a wish: may her glance, radiant as an open lotus, bring about the <em>puṣṭi</em> I desire. Notice what is placed under her glance: even people of fine understanding. The verse does not say that the humble or the unlearned are favoured; it says that her look is what makes the way easy for everyone, including the wise."),
   ("The poetry hidden in the verse","Imagine a lotus pond at sunrise. The night has passed, the first light touches the water, and a lotus slowly opens its petals to show its bright centre. There is a quiet beauty in that moment. \n\nNow imagine Lakshmi seated on that lotus, and her eyes carrying the same soft light as the open flower. This is the picture the verse paints in <em>prahṛṣṭa-kamalodara-dīptiḥ</em>. Against it the poet sets a large claim: by her glance even the wise and devoted reach the highest places with ease. \n\nNotice the contrast. The lotus is delicate, yet it shines. The glance is gentle, yet its reach is great. Her compassion is quiet, yet it can change a life. The poet does not describe her power with weapons, thunder or command. He describes it through her eyes. That is much of the beauty of the verse: the greatest power is shown in the gentlest gesture. The pond and the sunrise are an imagined setting to help us see the lotus; the verse itself gives the comparison with the open lotus."),
   ("A note on the reading","The line is <em>iṣṭā viśiṣṭa-matayo ’pi</em>: the wise and devoted (<em>viśiṣṭa-matayaḥ</em>). Some summaries read it as <em>aviśiṣṭa</em>, “not distinguished”, and so take the verse to be about ordinary people being lifted. Standard editions have <em>viśiṣṭa</em>, and so does this page. Both readings can inspire a reflection, but the verse itself is about the wise."),
   ("The sound of the verse","Listen to the verse and one sound keeps returning: <em>ṣṭ</em>. It appears ten times in this one verse: <em>iṣṭā</em>, <em>viśiṣṭa</em>, <em>triviṣṭapa</em>, <em>dṛṣṭyā</em>, <em>dṛṣṭiḥ</em>, <em>prahṛṣṭa</em>, <em>iṣṭām</em>, <em>puṣṭim</em>, <em>kṛṣīṣṭa</em>, <em>viṣṭarāyāḥ</em>. Śaṅkara builds the whole verse on one repeating beat. It is a poet’s pleasure, and you can hear it best when the verse is read aloud."),
   ("The glance that is wet with compassion","<em>Dayārdra-dṛṣṭi</em> is one of the loveliest phrases in the hymn. <em>Ārdra</em> means moist, as soil after rain or as eyes that have filled. The poet has just spoken of clouds in Verse 8; here the same idea returns in a smaller form. Her look is not cold or merely graceful; it is softened by feeling."),
   ("The lotus opened","The second picture is a lotus in full bloom. <em>Prahṛṣṭa</em> comes from a root meaning to thrill with joy, and for a flower it suggests complete opening, with nothing held back. The glance is compared to the glowing centre of that flower. A closed bud does not show its inside; an open lotus does. The comparison suggests a look that is warm and fully given."),
   ("What puṣṭi can mean","<em>Puṣṭi</em> is a wider word than “wealth”. It means to be nourished, to grow, to thrive. As a reflection, not a definition in the verse, we may think of strength in the body, clarity in the mind, steadiness in the family, growth in one’s work and a sense of enough. Money may be one part of this, but the word itself looks to a life that is well fed in every sense."),
   ("Knowledge and grace","The first half sets wisdom beside grace. The wise are named, and the verse still says it is by her glance that the way becomes easy. As a reflection: skill, learning and good judgement matter, and the hymn does not dismiss them. But the poet places them under something larger. Many people find this a useful reminder when their own abilities have taken them a long way and they feel tempted to think they did it all alone."),
   ("Heaven and everyday life","<em>Triviṣṭapa</em> is the world of the gods in tradition, and that is what the verse means. A reader may also take heaven figuratively as a life that is lifted, calmer and better. The verse does not promise that every wish will be met. It praises a compassion that makes difficult things easier."),
   ("How this verse follows the last","Verse 8 ended with a young bird waiting for rain. Verse 9 turns from need to hope. It moves from “I have nothing” to “let me be nourished”, and the cloud of the eyes becomes the lotus of the eyes. The tone is quieter and more confident."),
   ("Three Sanskrit words to keep","<em>Dayārdra</em> is moist with compassion. <em>Puṣṭi</em> is nourishment and thriving. <em>Sulabha</em> is easily obtained."),
   ("How to pronounce the key words","Iṣṭā: ish-taa. Viśiṣṭa-matayaḥ: vi-shish-ta-ma-ta-yah. Dayārdra-dṛṣṭyā: da-yaar-dra-drish-tyaa. Triviṣṭapa-padam: tri-vish-ta-pa-pa-dam. Sulabham: su-la-bham. Labhante: la-bhan-te. Prahṛṣṭa-kamalodara-dīptiḥ: pra-hrish-ta-ka-ma-lo-da-ra-deep-tih. Puṣṭim: push-tim. Kṛṣīṣṭa: kri-sheesh-ta. Puṣkara-viṣṭarāyāḥ: push-ka-ra-vish-ta-raa-yaah."),
  ],
  meditation=["Minute 1, settle: sit comfortably, breathe slowly and imagine a lotus resting on still water at dawn.",
              "Minute 2, recite: say the phrase dayārdra-dṛṣṭi quietly, “the glance moist with compassion”. Picture a look that is kind and unhurried.",
              "Minute 3, think of a person or a responsibility in your life that needs that kind of patient attention.",
              "Minute 4, ask yourself: “Am I helping those around me to be nourished and to grow, or only trying to gain for myself?”",
              "Minute 5, offer a prayer. Say silently: “O Mother Lakshmi, may there be growth in my home, health in my body, clarity in my work and compassion in my heart. May what I gain nourish others as well.”"],
  reflection="Ability: when something has gone well for me, do I remember the help that came with my own effort? Nourishment: what would puṣṭi mean for me this year, beyond money? Compassion: whom could I look at today with a softer eye? One honest answer is enough for today.",
  closing="The poet who sat as a fledgling in Verse 8 now lifts his eyes to the lotus. He asks for puṣṭi, a life nourished and growing, and he places it in the hands of a glance. The thought to carry is that real growth is not only getting more; it is being fed in body, mind and heart, and being kind enough to feed others. " + "This meditation is a devotional practice for attention and reflection; it does not promise a supernatural result or guarantee material wealth.",
 ),

 dict(
  n=10, slug="verse-10",
  deva="गीर्देवतेति गरुडध्वजसुन्दरीति<br>शाकम्भरीति शशिशेखरवल्लभेति।<br>सृष्टिस्थितिप्रलयकेलिषु संस्थितायै<br>तस्यै नमस्त्रिभुवनैकगुरोस्तरुण्यै॥",
  iast="Gīrdevateti garuḍadhvaja-sundarīti<br>Śākambharīti śaśiśekhara-vallabheti;<br>Sṛṣṭi-sthiti-pralaya-keliṣu saṁsthitāyai<br>Tasyai namas tribhuvanaika-guros taruṇyai.",
  ttl="Kanakadhara Stotram Verse 10 Meaning – Girdevateti",
  dsc="Kanakadhara Stotram Verse 10 (Girdevateti): Lakshmi saluted as Sarasvati, Vishnu’s beloved, Shakambhari and Shiva’s beloved. Word-by-word meaning in English.",
  h1="Kanakadhāra Stotram – Verse 10",
  sub="Gīrdevateti – the Goddess of many names",
  words=[
   ("गीर्देवता इति","Gīr-devatā iti","“The goddess of speech”, thus called","<em>Gīr</em> is speech, voice, the spoken word; <em>devatā</em> is a deity. Tradition understands her as Sarasvatī. <em>Iti</em> means “thus”; it closes a name, as quotation marks do in English. Because <em>ā</em> and <em>i</em> meet, the two words are written together as <em>gīrdevateti</em>."),
   ("गरुडध्वजसुन्दरी इति","Garuḍadhvaja-sundarī iti","“The beautiful one of Garuḍa’s banner”, thus called","<em>Garuḍa</em> is the eagle, the mount of Vishnu; <em>dhvaja</em> is a banner, so <em>garuḍadhvaja</em> is the one whose banner bears Garuḍa: Vishnu. <em>Sundarī</em> is a beautiful woman. So she is Vishnu’s beautiful beloved: Lakshmi herself. The words join as <em>sundarīti</em>."),
   ("शाकम्भरी इति","Śākambharī iti","“She who bears vegetables”, thus called","<em>Śāka</em> is vegetable, leafy food; <em>bharī</em> is a bearer or supporter (from <em>bhṛ</em>, to carry, to sustain). So <em>śākambharī</em> is the one who sustains life with greens and plants. It is also the name of a form of the Goddess who is remembered for feeding the world (see below). The words join as <em>śākambharīti</em>."),
   ("शशिशेखरवल्लभा इति","Śaśiśekhara-vallabhā iti","“The beloved of the moon-crested one”, thus called","<em>Śaśin</em> is the moon (“the one with the hare mark”); <em>śekhara</em> is a crest or crown; <em>śaśiśekhara</em> is the one who wears the moon as a crest: Shiva. <em>Vallabhā</em> is a beloved, a wife. The words join as <em>vallabheti</em>, where <em>ā</em> and <em>i</em> become <em>e</em>."),
   ("सृष्टिस्थितिप्रलयकेलिषु","Sṛṣṭi-sthiti-pralaya-keliṣu","In the play of creation, preservation and dissolution","<em>Sṛṣṭi</em> is creation, letting go forth; <em>sthiti</em> is standing, staying, preservation; <em>pralaya</em> is dissolution, the melting away of the world at the end of a cycle. <em>Keli</em> is play, sport. The ending means “in”. The three great acts are called play: done freely and without strain."),
   ("संस्थितायै","Saṁsthitāyai","To her who abides","From <em>sam</em> (together, fully) and <em>sthā</em> (to stand): firmly established, present. The ending means “to”: this is the one being saluted."),
   ("तस्यै","Tasyai","To her","“To that one”. It gathers all the names and descriptions above into one person."),
   ("नमः","Namaḥ","A bow, salutation","Before the next word it is written <em>namas</em>. The same word that ends many Sanskrit prayers: “bowing”."),
   ("त्रिभुवनैकगुरोः","Tribhuvana-eka-guroḥ","Of the one teacher of the three worlds","<em>Tri</em> is three; <em>bhuvana</em> is a world; <em>eka</em> is one, sole; <em>guru</em> is a teacher, one who is weighty with knowledge. The three worlds are heaven, earth and the lower realm. Traditionally the one teacher or lord of the three worlds is Nārāyaṇa. <em>A</em> and <em>e</em> join as <em>ai</em>, giving <em>-bhuvanaika-</em>. The ending means “of”, and the final <em>ḥ</em> becomes <em>s</em> before <em>t</em>: <em>guros taruṇyai</em>."),
   ("तरुण्यै","Taruṇyai","To the young woman, the young wife","<em>Taruṇī</em> is a young woman, in the full bloom of youth. The ending means “to”. She is the youthful consort of the guru of the three worlds."),
  ],
  meaning="Salutations to her who is called the goddess of speech, the beautiful beloved of him whose banner bears Garuḍa, Śākambharī, and the beloved of the moon-crested one; who abides in the play of creation, preservation and dissolution; to that youthful wife of the one teacher of the three worlds.",
  insights=[
   ("In simple words","“O Mother, you are known as Sarasvatī, as Vishnu’s beloved, as Śākambharī and as the beloved of Shiva. You are present whenever the world is made, kept and dissolved. I bow to you, the ever-young wife of the one teacher of the three worlds.” After asking for puṣṭi in Verse 9, the poet stops to bow."),
   ("What the verse actually says","The verse is one long salutation. It names her four times, each name closed with <em>iti</em>: the goddess of speech, the beloved of Garuḍa’s banner, Śākambharī, the beloved of the moon-crested one. It says where she is found: in the play of creation, preservation and dissolution. And it bows to her as the young wife of the teacher of the three worlds."),
   ("The poetry hidden in the verse","Imagine a devotee standing before a great temple. At first he sees different forms. There is a Goddess with a <em>vīṇā</em>, the lute, who stands for speech, music and learning. There is a Goddess beside Vishnu, who stands for beauty, prosperity and keeping. There is a Mother surrounded by fruit, vegetables and green leaves, who feeds the world. And there is a Goddess beside Shiva. The names differ, the appearances differ, and so do their relationships. \n\nThen the poet invites us to look beyond the forms. By the traditional reading, the power that nourishes, creates, sustains and transforms the universe is one, and the verse bows to her under all these names. \n\nSee how the verse moves: it begins with the personal, the beloved of Vishnu, and widens to the universal, the one present in making, keeping and dissolving the world. The temple scene is a picture to help us read the verse; the verse itself gives only the names and the bow."),
   ("What iti is doing","Each name ends with <em>iti</em>, meaning “thus”. It works like an opening and closing quotation mark: she who is called <em>gīrdevatā</em>, she who is called <em>śākambharī</em>. The poet is repeating the names by which she is known, not defining her by any one."),
   ("The names","<em>Gīrdevatā</em> is the goddess of speech, usually taken as Sarasvatī. <em>Garuḍadhvaja-sundarī</em> is Vishnu’s beloved, Lakshmi. <em>Śākambharī</em> is a form of the Mother remembered for feeding the world. <em>Śaśiśekhara-vallabhā</em> is the beloved of Shiva, usually taken as Pārvatī. Traditional readers understand these as names of the one Goddess; others take the verse as a salutation to several goddesses together. This site follows the first, because the hymn is addressed to Lakshmi throughout."),
   ("Śākambharī","In the Devī Māhātmya, a major text of the Goddess tradition, she promises that in a time of drought she will sustain the world with life-giving vegetables from her own body, and she is then known as Śākambharī. The name <em>śāka-bhṛ</em> means exactly that: the bearer of greens. It is a good companion to the previous verse: after asking for <em>puṣṭi</em>, nourishment, the poet names the Goddess who feeds the world."),
   ("Creation, preservation, dissolution as play","<em>Keli</em> means play. Śaṅkara does not call the making, keeping and ending of the world her labour; he calls it her play. As a reflection, this does not make dissolution gentle or trivial; it says that nothing in the cycle lies outside her. Compare <a href=\"/glossary/\">līlā</a> in the glossary, the same idea of graceful, unforced action."),
   ("Who is the guru of the three worlds?","The verse says only <em>tribhuvanaika-guru</em>, the one teacher of the three worlds. Commentators usually understand this as Vishnu, Lakshmi’s husband, which suits the second name in the list. The poet ends by returning to the personal: after all the cosmic names, she is a young wife."),
   ("Youth","<em>Taruṇī</em> is a young woman. In Sanskrit poetry it often stands for freshness and bloom. The tradition does not say the Goddess has an age; it says she is ever fresh. A reflection: creation and ending may go on through ages, but the poet thinks of her as new."),
   ("The turn to salutation","From this verse the hymn moves from asking to bowing: <em>namas</em> is the heart of this verse, and a run of salutations begins here and carries on in the verses that follow. The poet has asked; now he honours."),
   ("Three Sanskrit words to keep","<em>Śākambharī</em> is the one who sustains with greens. <em>Pralaya</em> is dissolution, the end of a cycle. <em>Sthiti</em> is staying, keeping, preservation."),
   ("How to pronounce the key words","Gīrdevateti: geer-de-va-te-ti. Garuḍadhvaja-sundarīti: ga-ru-da-dhva-ja-sun-da-ree-ti. Śākambharīti: shaa-kam-ba-ree-ti. Śaśiśekhara-vallabheti: sha-shi-she-kha-ra-val-la-bhe-ti. Sṛṣṭi-sthiti-pralaya-keliṣu: sri-shti-sthi-ti-pra-la-ya-ke-li-shu. Saṁsthitāyai: sam-sthi-taa-yai. Tasyai namas: tas-yai na-mas. Tribhuvanaika-guros: tri-bhu-va-nai-ka-gu-ros. Taruṇyai: ta-run-yai."),
  ],
  meditation=["Minute 1, settle: sit quietly and recite the first line slowly, gīrdevateti garuḍadhvaja-sundarīti, once or twice.",
              "Minute 2, speech: think of the Goddess as the power of speech. Resolve to speak truthfully and kindly today.",
              "Minute 3, nourishment: picture a green field and a full plate. Give thanks, silently, for the food in front of you and for the people who grew it.",
              "Minute 4, endings: bring to mind one thing that is coming to an end in your life, a habit, a worry or a season. Let it go with respect.",
              "Minute 5, offer a prayer. Say silently: “O Mother, you are the word, the harvest and the turning of all things. May I speak well, be grateful for what feeds me, and meet change with trust.” If you wish, bow your head at the end."],
  reflection="Speech: have my words been truthful and kind today? Food: do I remember what sustains me and who made it? Change: what ending am I resisting that may be making room for something new? One honest answer is enough for today.",
  closing="The poet has looked into her eyes for nine verses. Now he steps back and bows to everything she is: speech, beauty, food, the beloved of two great gods and the play of the whole world. The thought to carry is that prosperity is not separate from knowledge, nourishment and change; the Mother who gives wealth is also the one who feeds, teaches and renews. " + "This meditation is a devotional practice for attention and reflection; it does not promise a supernatural result or guarantee material wealth.",
 ),

 dict(
  n=11, slug="verse-11",
  deva="श्रुत्यै नमोऽस्तु शुभकर्मफलप्रसूत्यै<br>रत्यै नमोऽस्तु रमणीयगुणार्णवायै।<br>शक्त्यै नमोऽस्तु शतपत्रनिकेतनायै<br>पुष्ट्यै नमोऽस्तु पुरुषोत्तमवल्लभायै॥",
  iast="Śrutyai namo ’stu śubha-karma-phala-prasūtyai<br>Ratyai namo ’stu ramaṇīya-guṇārṇavāyai;<br>Śaktyai namo ’stu śata-patra-niketanāyai<br>Puṣṭyai namo ’stu puruṣottama-vallabhāyai.",
  ttl="Kanakadhara Stotram Verse 11 Meaning – Shrutyai Namostu",
  icons=["book","heart","bolt","sprout"],
  keypoints=[("Śruti","Wisdom: the sacred knowledge that guides good action"),("Rati","Delight: love, beauty and lovely qualities"),("Śakti","Power: the energy that gives strength and the ability to act"),("Puṣṭi","Nourishment: growth, fullness and flourishing")],
  tagline="The Goddess is praised as wisdom, delight, power and nourishment: four strands of a flourishing life.",
  sketchfile="kanakadhara-verse-11-sketch-note.png", forms_title="Explore the four forms",
  sketchalt="Sketch note for Kanakadhāra Stotram Verse 11: the Sanskrit verse and transliteration, its meaning, the four salutations to Śruti (wisdom), Rati (delight), Śakti (power) and Puṣṭi (nourishment), key words and a life takeaway, around a picture of Goddess Lakshmi seated on a lotus.",
  sheet=dict(
   salut_title="The Four Salutations", centre_title="A Complete Prosperity", centre="Flourishing Life",
   essence="The Goddess is praised in four complementary forms: wisdom, delight, power and nourishment. Together they make a life prosperous and fulfilling.",
   short="Salutations to her as Śruti, source of the fruit of good deeds; as Rati, ocean of lovely qualities; as Śakti, dwelling in the hundred-petalled lotus; and as Puṣṭi, beloved of Puruṣottama.",
   salut=["The sacred knowledge that leads to good actions and their fruits.","Love, delight and kindness: an ocean of lovely qualities.","The energy that gives life, strength and the ability to act.","Growth, fullness and flourishing: the beloved of Viṣṇu (Puruṣottama)."],
   words=[("श्रुति","Śruti","Sacred wisdom, the Veda"),("रति","Rati","Love, delight, joy"),("शक्ति","Śakti","Divine power, energy"),("पुष्टि","Puṣṭi","Nourishment, growth")],
   take=["Seek wisdom to choose rightly.","Nurture love and lovely qualities.","Use your strength for a worthy purpose.","Make your life and work nourish others."],
  ),
  formnotes=[
   ("Śruti means “what is heard”, the Veda. The line calls her the source from which good deeds yield their fruit. Wisdom comes first because it tells us which deeds are worth doing.","Am I deciding with understanding, or only reacting?"),
   ("Rati is delight, love and the pleasure of lovely qualities. The poet calls her an ocean of them. After wisdom, the second bow is to warmth and beauty.","Do the people around me feel kindness from the way I act?"),
   ("Śakti is power, the energy that gives strength and the ability to act. The verse places her in the hundred-petalled lotus, Lakshmi’s own seat.","Am I using my abilities for something worthwhile?"),
   ("Puṣṭi is nourishment, fullness and thriving. The line ends by calling her the beloved of Puruṣottama, Vishnu, which brings us back to Lakshmi herself.","Are my family, my office and my community better fed because of what I do?"),
  ],
  grammar=dict(
   anvaya_note="The verse is one sentence pattern repeated four times: the name in the “to” form, a description in the same form, and the words namo ’stu. The lines already stand in prose order, so the sentence below is the verse itself, read line by line.",
   anvaya=[("Śrutyai","śubha-karma-phala-prasūtyai","namo ’stu"),("Ratyai","ramaṇīya-guṇārṇavāyai","namo ’stu"),("Śaktyai","śata-patra-niketanāyai","namo ’stu"),("Puṣṭyai","puruṣottama-vallabhāyai","namo ’stu")],
   vib_title="Why every name ends in -yai",
   vib_notes=["Śruti, rati, śakti and puṣṭi are feminine nouns ending in -i. Their “to” form is called the dative, the fourth case (caturthī). In Sanskrit the word namaḥ, “a bow”, is joined with the dative: “a bow to…” (Pāṇini 2.3.16). For a feminine word in -i the dative singular is -yai, so śruti becomes śrutyai, “to Śruti”, which the English renders as “to her”.",
              "The four descriptions must agree with the name they describe, so they take the same case, number and gender. A compound takes its ending on the last word: -prasūtyai (prasūti, a feminine word in -i), and -arṇavāyai, -niketanāyai and -vallabhāyai, which are feminine forms in -ā whose dative singular is -āyai."],
   vib_rows=[("श्रुति","śruti","श्रुत्यै","śrutyai","dative singular, feminine"),("रति","rati","रत्यै","ratyai","dative singular, feminine"),("शक्ति","śakti","शक्त्यै","śaktyai","dative singular, feminine"),("पुष्टि","puṣṭi","पुष्ट्यै","puṣṭyai","dative singular, feminine")],
   sam_note="Each long word in the verse is a compound (samāsa): several words joined into one. Reading the parts in order gives the meaning.",
   sam_rows=[("शुभकर्मफलप्रसूत्यै","śubha-karma-phala-prasūtyai","śubha + karma + phala + prasūti","tatpuruṣa: each part limits the next","to her who is the source of the fruit of good deeds"),
             ("रमणीयगुणार्णवायै","ramaṇīya-guṇārṇavāyai","ramaṇīya + guṇa + arṇava","tatpuruṣa: “ocean of delightful qualities”","to her who is an ocean of lovely qualities"),
             ("शतपत्रनिकेतनायै","śata-patra-niketanāyai","śata + patra + niketana","bahuvrīhi: “she whose dwelling is the hundred-petalled lotus”","to her whose dwelling is the lotus"),
             ("पुरुषोत्तमवल्लभायै","puruṣottama-vallabhāyai","puruṣa + uttama + vallabhā","tatpuruṣa: “beloved of the supreme person”","to the beloved of Puruṣottama")],
   sandhi=[("namaḥ + astu","namo ’stu","The visarga after -a becomes o before a, and the a of astu is dropped, shown by the apostrophe."),
           ("guṇa + arṇava","guṇārṇava","a + a join into ā."),
           ("puruṣa + uttama","puruṣottama","a + u join into o.")],
   foot="These notes follow standard Sanskrit grammar and explain the words themselves. They do not depend on any one commentary.",
  ),
  dsc="Kanakadhara Stotram Verse 11 (Shrutyai Namo ’stu): four salutations to Lakshmi as Shruti, Rati, Shakti and Pushti. Word-by-word meaning in English.",
  h1="Kanakadhāra Stotram – Verse 11",
  sub="Śrutyai namo ’stu – four bows",
  words=[
   ("श्रुत्यै","Śrutyai","To Śruti; to the Veda","<em>Śruti</em> comes from <em>śru</em>, to hear: “that which is heard”. It is the traditional name for the Vedas, the revealed scripture handed down by hearing. The ending <em>-yai</em> means “to” and shows that the Goddess herself is being addressed in this form."),
   ("नमः अस्तु","Namo ’stu","Let there be a bow","<em>Namaḥ</em> is a bow, a salutation; <em>astu</em> means “let it be”. So the phrase is “let there be a bow to…”. The two words meet as <em>namo ’stu</em>, where the apostrophe marks the lost <em>a</em> of <em>astu</em>. It is repeated four times, once in each line."),
   ("शुभकर्मफलप्रसूत्यै","Śubha-karma-phala-prasūtyai","To her who brings forth the fruit of good deeds","<em>Śubha</em> is auspicious, good; <em>karma</em> is action or deed; <em>phala</em> is fruit or result; <em>prasūti</em> is bringing forth, giving birth, a source. So she is the source from which good deeds yield their fruit. The ending means “to”."),
   ("रत्यै","Ratyai","To Rati; to delight","<em>Rati</em> means delight, pleasure, love. It is also the name of the goddess of love, wife of Kāma. Here the sense is usually taken to be delight itself, with Lakshmi as its giver."),
   ("रमणीयगुणार्णवायै","Ramaṇīya-guṇa-arṇavāyai","To her who is an ocean of lovely qualities","<em>Ramaṇīya</em> is delightful, charming, from <em>ram</em>, to please; <em>guṇa</em> is a quality, a virtue; <em>arṇava</em> is an ocean. The two <em>a</em> sounds of <em>guṇa</em> and <em>arṇava</em> join into <em>guṇārṇava-</em>. The picture is of virtues as vast and deep as the sea."),
   ("शक्त्यै","Śaktyai","To Śakti; to power","<em>Śakti</em> is power, energy, ability. In the Goddess tradition it is also the name of the divine power itself. The ending means “to”."),
   ("शतपत्रनिकेतनायै","Śata-patra-niketanāyai","To her whose dwelling is the hundred-petalled lotus","<em>Śata</em> is a hundred; <em>patra</em> is a petal or leaf; <em>śatapatra</em> is a common Sanskrit name for the lotus. <em>Niketana</em> is a dwelling, a home. So she is the one who lives in the lotus. The number need not be taken literally."),
   ("पुष्ट्यै","Puṣṭyai","To Puṣṭi; to nourishment","<em>Puṣṭi</em> is nourishment, fullness, thriving. It is the same word asked for in <a href=\"/kanakadhara/verse-9/\">Verse 9</a>. The ending means “to”."),
   ("पुरुषोत्तमवल्लभायै","Puruṣottama-vallabhāyai","To the beloved of Puruṣottama","<em>Puruṣa</em> is a person; <em>uttama</em> is the best, the highest; <em>puruṣottama</em> is “the supreme person”, a name of Vishnu. <em>Vallabhā</em> is a beloved, a wife, as in the last verse. The ending means “to”."),
  ],
  meaning="Let there be a bow to her as Śruti, who brings forth the fruit of good deeds. Let there be a bow to her as Rati, the ocean of lovely qualities. Let there be a bow to her as Śakti, whose dwelling is the hundred-petalled lotus. Let there be a bow to her as Puṣṭi, the beloved of Puruṣottama.",
  insights=[
   ("In simple words","“O Mother, I bow to you as the sacred word that gives good deeds their fruit. I bow to you as delight, an ocean of lovely qualities. I bow to you as power, who lives in the lotus. I bow to you as nourishment, the beloved of Vishnu.” Four bows, one in each line."),
   ("What the verse actually says","Each line has the same shape: a name in the “to” form, <em>namo ’stu</em>, and a description. The four names are Śruti, Rati, Śakti and Puṣṭi. The four descriptions are: she who brings forth the fruit of good deeds; she who is an ocean of lovely qualities; she whose dwelling is the lotus; she who is the beloved of Puruṣottama."),
   ("The poetry hidden in the verse","Imagine four offerings placed one after another at the Goddess’s feet. The first is <em>śruti</em>: wisdom, the sacred knowledge that guides us towards what is worth doing. The second is <em>rati</em>: delight, the beauty of love and the lovely qualities that make a life worth living. The third is <em>śakti</em>: power, the unseen energy that gives movement and strength to things. The fourth is <em>puṣṭi</em>: nourishment, the fullness that sustains body, mind and family. \n\nNotice how they follow one another. Wisdom gives direction. Delight gives sweetness. Power gives strength. Nourishment gives continuity. In four bows the poet has gathered a whole picture of a flourishing life. The four offerings are an image to help us read the verse, in which the four names and the four bows are what the poet gives us."),
   ("Śruti","<em>Śruti</em>, “what is heard”, is the Veda. The Goddess is honoured as the sacred knowledge itself, and the second part of the line says what that knowledge does: it brings the fruit of good deeds. This reading follows the traditional commentators, for whom the Veda teaches which deeds are good and what they lead to. As a reflection: the first bow is not to gold but to wisdom, and the line suggests that prosperity begins with knowing what is worth doing."),
   ("Rati","<em>Rati</em> is delight, and it is also the goddess of love. The poet calls her an ocean of lovely qualities. After wisdom, the second bow is to joy and beauty. As a reflection: a life can be successful and still feel empty, and warmth, kindness and joy are part of what the verse calls Lakshmi."),
   ("Śakti and the lotus","<em>Śakti</em> is power, and the line says where that power lives: in the lotus. A later yoga tradition speaks of a thousand-petalled lotus at the crown of the head, but this verse says hundred-petalled, and <em>śatapatra</em> is also simply a common word for a lotus. So the verse need not be read as pointing to that tradition. The central picture is of divine power seated in a lotus."),
   ("Puṣṭi","<em>Puṣṭi</em> returns here after <a href=\"/kanakadhara/verse-9/\">Verse 9</a>. There the poet asked for it; here he bows to it. It means nourishment, thriving, being well fed in every sense, and the line ends by calling her the beloved of Puruṣottama, which brings us back to Lakshmi’s own name and place."),
   ("From the abstract to the personal","Look at how the four lines are built. The first two descriptions are general: the fruit of good deeds, an ocean of qualities. The last two are about Lakshmi in particular: the lotus is her home and Vishnu is her beloved. As a reflection, the verse moves from ideas to a face."),
   ("How this verse follows the last","<a href=\"/kanakadhara/verse-10/\">Verse 10</a> bowed to the Goddess of many names. This verse goes on bowing and gives four more of her aspects. After the poet asked and described, the hymn has become a chain of salutations."),
   ("Three Sanskrit words to keep","<em>Śruti</em> is what is heard, the Veda. <em>Arṇava</em> is an ocean. <em>Puṣṭi</em> is nourishment and thriving."),
   ("How to pronounce the key words","Śrutyai: shrut-yai. Namo ’stu: na-mo-stu. Śubha-karma-phala-prasūtyai: shu-bha-kar-ma-pha-la-pra-soot-yai. Ratyai: rat-yai. Ramaṇīya-guṇārṇavāyai: ra-ma-nee-ya-gu-naar-na-vaa-yai. Śaktyai: shak-tyai. Śata-patra-niketanāyai: sha-ta-pat-ra-ni-ke-ta-naa-yai. Puṣṭyai: push-tyai. Puruṣottama-vallabhāyai: pu-ru-shot-ta-ma-val-la-bhaa-yai."),
  ],
  meditation=["Minute 1, wisdom: picture a lotus and say silently, śrutyai namaḥ. Ask that your understanding guide your actions.",
              "Minute 2, delight: say ratyai namaḥ. Think of someone close to you and wish that your dealings with them be warm.",
              "Minute 3, power: say śaktyai namaḥ. Ask for strength to fulfil your responsibilities.",
              "Minute 4, nourishment: say puṣṭyai namaḥ. Ask that your life, family and work be well nourished.",
              "Minute 5, gratitude: bring the four together and give thanks for the wisdom, joy, strength and nourishment already in your life."],
  reflection="Wisdom: am I deciding with understanding, or only reacting? Warmth: do people around me feel kindness from the way I act? Strength: am I using my abilities for something worthwhile? Nourishment: is my family, my office, my community better fed because of what I do? One honest answer is enough for today.",
  closing="Four bows give the poet’s picture of a full life: wisdom to choose well, delight to enjoy it, strength to act and nourishment to last. The thought to carry is that prosperity is measured not only by what we gather but by what we grow, in ourselves and in those around us. " + "This meditation is a devotional practice for attention and reflection; it does not promise a supernatural result or guarantee material wealth.",
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

def _load_extras():
    """Per-verse redesign content (icons, keypoints, formnotes, sheet ...) lives in tools/extras_<series>.py and is merged without overriding keys already on a verse."""
    import importlib.util
    here = os.path.dirname(os.path.abspath(__file__))
    for fn, lst in (("extras_sri.py", VERSES), ("extras_kana.py", KVERSES), ("extras_mla.py", MVERSES)):
        fp = os.path.join(here, fn)
        if not os.path.exists(fp): continue
        spec = importlib.util.spec_from_file_location(fn[:-3], fp); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        for v in lst:
            for k, val in m.EXTRAS.get(v["n"], {}).items():
                v.setdefault(k, val)
_load_extras()

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
 ("इन्दिरा","Indirā","A name of Lakshmi.","kanakadhara/verse-3/"),
 ("इन्दीवर","Indīvara","The blue lotus (blue water lily), a classical image of beauty and calm.","kanakadhara/verse-3/"),
 ("ईक्षण","Īkṣaṇa","A glance, a look; the act of seeing.","kanakadhara/verse-3/"),
 ("आनन्द","Ānanda","Joy, bliss; a deep happiness that goes beyond ordinary pleasure.","kanakadhara/verse-3/"),
 ("सहोदर","Sahodara","Literally “born of the same womb”: a sibling; by extension, closely resembling.","kanakadhara/verse-3/"),
 ("मुकुन्द","Mukunda","A name of Vishnu, traditionally explained as the giver of mukti (liberation).","kanakadhara/verse-4/"),
 ("अनङ्ग","Anaṅga","“Without a body”: a name of Kāma, the god of love, who lives on without form after Shiva burned his body.","kanakadhara/verse-4/"),
 ("अनिमेष","Animeṣa","Unblinking; without a pause.","kanakadhara/verse-4/"),
 ("कनीनिका","Kanīnikā","The pupil of the eye.","kanakadhara/verse-4/"),
 ("भूति","Bhūti","Prosperity, well-being, flourishing; from bhū, “to be, to become”.","kanakadhara/verse-4/"),
 ("कौस्तुभ","Kaustubha","The celebrated jewel of Vishnu, said in tradition to have risen at the churning of the ocean and to rest on his chest.","kanakadhara/verse-5/"),
 ("मधुजित्","Madhujit","“Conqueror of Madhu”: a name of Vishnu, from the tradition that he slew the demon Madhu.","kanakadhara/verse-5/"),
 ("कल्याण","Kalyāṇa","What is good and auspicious: welfare, well-being, flourishing.","kanakadhara/verse-5/"),
 ("कैटभ","Kaiṭabha","A demon who, with Madhu, was slain by Vishnu in tradition; Vishnu is therefore called Kaiṭabhāri, “enemy of Kaiṭabha”.","kanakadhara/verse-6/"),
 ("तडित्","Taḍit","Lightning; a flash of light.","kanakadhara/verse-6/"),
 ("भृगु","Bhṛgu","A great sage of tradition; Lakshmi is called Bhārgavī, “daughter of Bhṛgu”.","kanakadhara/verse-6/"),
 ("भद्र","Bhadra","Good, auspicious, fortunate; in the plural, good things and blessings.","kanakadhara/verse-6/"),
 ("मूर्ति","Mūrti","A form or embodied shape, especially the visible form of a deity.","kanakadhara/verse-6/"),
 ("प्रभाव","Prabhāva","Power, might, influence; the ability to bring about an effect.","kanakadhara/verse-7/"),
 ("मन्मथ","Manmatha","A name of Kāma, the god of love; traditionally explained as “the mind-churner”.","kanakadhara/verse-7/"),
 ("मन्थर","Manthara","Slow, unhurried, lingering.","kanakadhara/verse-7/"),
 ("मकर","Makara","A sea creature of Indian myth, often shown like a crocodile; the ocean is its abode.","kanakadhara/verse-7/"),
 ("दया","Dayā","Compassion: the willingness to see suffering and respond with kindness.","kanakadhara/verse-8/"),
 ("द्रविण","Draviṇa","Wealth, riches, goods.","kanakadhara/verse-8/"),
 ("अकिञ्चन","Akiñcana","One who has nothing, not even a little; utterly destitute.","kanakadhara/verse-8/"),
 ("दुष्कर्म","Duṣkarma","A bad or harmful deed; in the verse, the wrong actions whose results burn like heat.","kanakadhara/verse-8/"),
 ("अम्बुवाह","Ambuvāha","“Water-carrier”: a rain cloud.","kanakadhara/verse-8/"),
 ("इष्ट","Iṣṭa","Desired, dear, cherished; also what is honoured by worship.","kanakadhara/verse-9/"),
 ("त्रिविष्टप","Triviṣṭapa","Heaven; the celestial world.","kanakadhara/verse-9/"),
 ("पुष्कर","Puṣkara","A lotus; also a name for a lotus pond.","kanakadhara/verse-9/"),
 ("गीर्देवता","Gīrdevatā","The goddess of speech, usually taken as Sarasvatī.","kanakadhara/verse-10/"),
 ("शाकम्भरी","Śākambharī","“She who bears vegetables”: a form of the Mother remembered for feeding the world.","kanakadhara/verse-10/"),
 ("प्रलय","Pralaya","Dissolution; the melting away of the world at the end of a cycle.","kanakadhara/verse-10/"),
 ("स्थिति","Sthiti","Standing, staying; preservation and continuity.","kanakadhara/verse-10/"),
 ("श्रुति","Śruti","“What is heard”: the Veda, the revealed scripture.","kanakadhara/verse-11/"),
 ("रति","Rati","Delight, pleasure, love; also the name of the goddess of love.","kanakadhara/verse-11/"),
 ("शक्ति","Śakti","Power, energy; in the Goddess tradition, the divine power itself.","kanakadhara/verse-11/"),
 ("अर्णव","Arṇava","An ocean.","kanakadhara/verse-11/"),
 ("पुरुषोत्तम","Puruṣottama","“The supreme person”: a name of Vishnu.","kanakadhara/verse-11/"),
 ("प्रहृष्ट","Prahṛṣṭa","Thrilled, delighted; said of a flower, fully open.","kanakadhara/verse-9/"),
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
<a class="tile" href="/lakshmi-aarti/"><h3>Lakshmi Aarti</h3><p>How to perform the aarti at home on Diwali, and what each stanza means.</p></a>
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

INS_KINDS = [
 ("in simple words","simple",""),
 ("what the verse actually says","text","From the text"),
 ("the poetry hidden","scene","Picture it"),
 ("the sound of the verse","sound","Listen"),
 ("three sanskrit words","keep","Words to keep"),
 ("how to pronounce","say","Say it aloud"),
 ("how this verse follows","thread","The thread"),
 ("an echo of","thread","The thread"),
 ("a note on","note","A note"),
]
def ins_card(h, body):
    kind, chip = "", ""
    for key, k, c in INS_KINDS:
        if h.lower().startswith(key): kind, chip = k, c; break
    cls = "card ins" + (f" ins-{kind}" if kind else "")
    chip_html = f'<p class="chip">{chip}</p>' if chip else ""
    paras = "".join(f"<p>{q}</p>" for q in body.split("\n\n"))
    return f'<div class="{cls}">{chip_html}<h3>{E(h)}</h3>{paras}</div>'

import re as _re
def med_step(x):
    m = _re.match(r"^(Minutes? \d+(?:[–-]\d+)?)(?:,\s*([^:]{1,40}))?:\s*(.*)$", x)
    if not m: return f"<li><span class=\"mt\">{E(x)}</span></li>"
    lab_, what, rest = m.groups()
    what_html = f"<b>{E(what[0].upper()+what[1:])}</b>" if what else ""
    rest = rest[:1].upper()+rest[1:]
    return f'<li><span class="mn">{E(lab_)}</span><span class="mt">{what_html}{E(rest)}</span></li>'

def ref_block(t):
    tail = ""
    if t.rstrip().endswith("One honest answer is enough for today."):
        t = t.rstrip()[: -len("One honest answer is enough for today.")].rstrip(); tail = "One honest answer is enough for today."
    parts = _re.split(r"(?<=[.?!”]) (?=[A-Z][A-Za-z ]{2,25}: )", t)
    ok = len(parts) >= 2 and all(_re.match(r"^[A-Z][A-Za-z ]{2,25}: ", q) for q in parts)
    if ok:
        lis = "".join(f'<li><b>{E(q.split(": ",1)[0])}</b>{E(q.split(": ",1)[1][:1].upper()+q.split(": ",1)[1][1:])}</li>' for q in parts)
        body = f'<ul class="asks">{lis}</ul>'
    else:
        body = f"<p>{E(t)}</p>"
    foot = f'<p class="once">{E(tail)}</p>' if tail else ""
    return f'<div class="reflect">{body}{foot}</div>'

def close_block(t):
    disc = ""
    i = t.find("This meditation is a devotional practice")
    if i > 0: disc = t[i:].strip(); t = t[:i].strip()
    d = f'<p class="disc">{E(disc)}</p>' if disc else ""
    return f'<p class="closing">{E(t)}</p>{d}'

ICONS = {
 "book":'<path d="M3 5.5c3-1.5 6-1.2 9 .8 3-2 6-2.3 9-.8V19c-3-1.5-6-1.2-9 .8-3-2-6-2.3-9-.8z"/><path d="M12 6.3v13.5"/>',
 "heart":'<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.5A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>',
 "bolt":'<path d="M13 2 5 13.5h6L10 22l9-12h-6z"/>',
 "sprout":'<path d="M12 21v-9"/><path d="M12 12c0-4-3-6-7-6 0 4 3 6 7 6z"/><path d="M12 15c0-3 2.5-5 6-5 0 3.5-2.5 5-6 5z"/>',
 "sun":'<circle cx="12" cy="12" r="4"/><path d="M12 2.5v2.5M12 19v2.5M2.5 12H5M19 12h2.5M5.2 5.2 7 7M17 17l1.800 1.800M18.800 5.200 17 7M7 17l-1.800 1.800"/>',
 "moon":'<path d="M20 14.500A8.500 8.500 0 1 1 9.500 4a7 7 0 0 0 10.500 10.500z"/>',
 "drop":'<path d="M12 3C8.500 8 6 11 6 14.500a6 6 0 0 0 12 0C18 11 15.500 8 12 3z"/>',
 "flame":'<path d="M12 3c1 4 5 6 5 11a5 5 0 0 1-10 0c0-2 1-3 2-4 0 2 1 3 2 3 0-3-1-6 1-10z"/>',
 "coin":'<circle cx="12" cy="12" r="8.500"/><circle cx="12" cy="12" r="4.500"/>',
 "shield":'<path d="M12 3l7 3v5c0 5-3 8-7 10-4-2-7-5-7-10V6z"/>',
 "bud":'<path d="M12 21c-4-3-6-6-6-9l6-8 6 8c0 3-2 6-6 9z"/><path d="M12 8v13"/>',
 "eye":'<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
 "star":'<path d="m12 3 2.700 5.600 6.100.8-4.500 4.300 1.100 6.100L12 16.800 6.600 19.800l1.100-6.100L3.200 9.400l6.100-.8z"/>',
 "home":'<path d="M3 11l9-8 9 8"/><path d="M5 10v10h5v-6h4v6h5V10"/>',
 "mountain":'<path d="M2 19 9 7l4 7 3-4 6 9z"/>',
 "wave":'<path d="M2 9c2.500-2.500 5-2.500 7.500 0s5 2.500 7.500 0l5 0"/><path d="M2 15c2.500-2.500 5-2.500 7.500 0s5 2.500 7.500 0l5 0"/>',
 "key":'<circle cx="8" cy="12" r="4"/><path d="M12 12h9M18 12v4M21 12v3"/>',
 "bell":'<path d="M6 17v-6a6 6 0 0 1 12 0v6l2 2H4z"/><path d="M10 21a2 2 0 0 0 4 0"/>',
 "crown":'<path d="M3 8l4.500 4L12 5l4.500 7L21 8l-2 11H5z"/>',
 "sound":'<path d="M4 10v4M8 6.500v11M12 3v18M16 7v10M20 10v4"/>',
 "leaf":'<path d="M5 19C5 9.500 11 4 20 4c0 9-5.500 15-15 15z"/><path d="M5 19 14 10"/>',
 "flag":'<path d="M5 21V4"/><path d="M5 4h12l-2.500 4L17 12H5"/>',
 "gem":'<path d="M6 3h12l4 6-10 12L2 9z"/><path d="M2 9h20M9 3l-2 6 5 12 5-12-2-6"/>',
 "hands":'<path d="M12 20c-3-1-6-4-6-8 2 0 4 1 6 3 2-2 4-3 6-3 0 4-3 7-6 8z"/><path d="M12 15V6"/>',
 "pot":'<path d="M8 6h8M7 6c-2 2-3 4-3 7a8 8 0 0 0 16 0c0-3-1-5-3-7"/><path d="M9 3h6"/>',
 "path":'<path d="M5 21c0-6 14-5 14-12S8 7 12 3"/><circle cx="12" cy="3" r="1"/>',
 "scale":'<path d="M12 4v16M6 20h12M4 8h16"/><path d="M4 8l-2 6a3 3 0 0 0 6 0zM20 8l-2 6a3 3 0 0 0 6 0z"/>',
 "cloud":'<path d="M7 18a4.500 4.500 0 1 1 1-8.900A6 6 0 0 1 19.500 11 3.5 3.5 0 0 1 18 18z"/><path d="M9 21l1-2M13 21l1-2"/>',
 "lotus":'<path d="M12 20c-4 0-7-2.5-8-6 3 0 5 1 8 3 3-2 5-3 8-3-1 3.5-4 6-8 6z"/><path d="M12 17c-3-2-3.5-5 0-10 3.5 5 3 8 0 10z"/><path d="M8 15c-2-2-2.5-4-2-6 2 1 3.5 3 4 5.500"/><path d="M16 15c2-2 2.5-4 2-6-2 1-3.5 3-4 5.5"/>',
}
def icon(name, size=22, cls="", attrs=""):
    return f'<svg class="icn {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" {attrs}>{ICONS[name]}</svg>'

FA_POS = {3:[(92,92),(188,92),(140,186)], 4:[(88,88),(192,88),(88,192),(192,192)]}
FA_CENTRE = {3:(140,121), 4:(140,140)}
def four_art(kp, icons):
    n=len(kp)
    out='<svg class="fourart" viewBox="0 0 280 280" role="img" aria-label="The key ideas of the verse">'
    for (cx,cy),(a,b),ic in zip(FA_POS[n],kp,icons):
        out+=f'<circle cx="{cx}" cy="{cy}" r="62" fill="rgba(255,255,255,.07)" stroke="#e5b94a" stroke-opacity=".7"/>'
        out+=f'<svg x="{cx-13}" y="{cy-42}" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#e5b94a" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{ICONS[ic]}</svg>'
        out+=f'<text x="{cx}" y="{cy-2}" text-anchor="middle" class="fa-t">{E(a)}</text><text x="{cx}" y="{cy+16}" text-anchor="middle" class="fa-s">{E(b.split(":")[0])}</text>'
    ox,oy=FA_CENTRE[n]
    out+=f'<circle cx="{ox}" cy="{oy}" r="14" fill="#e5b94a"/></svg>'
    return out

SK_POS = {3:[(190,112),(450,112),(320,298)], 4:[(190,115),(450,115),(190,290),(450,290)]}
SK_CENTRE = {3:(320,193,54), 4:(320,203,66)}
def sketch_note(kp, icons, centre="Flourishing Life", label="Sketch note: the key ideas of the verse"):
    n=len(kp)
    cols=["#8e5bb5","#e0587a","#e8a22b","#5f9b4f"]
    o=f'<svg class="sketch" viewBox="0 0 640 410" role="img" aria-label="{E(label)}">'
    for (cx,cy),(a,b),ic,c,rot in zip(SK_POS[n],kp,icons,cols,(-4,3,3,-3)):
        w=b.split(":")[0]
        o+=f'<g transform="rotate({rot} {cx} {cy})"><ellipse cx="{cx}" cy="{cy}" rx="140" ry="76" fill="{c}" fill-opacity=".16" stroke="{c}" stroke-width="2.2" stroke-dasharray="7 4" stroke-linecap="round"/></g>'
        o+=f'<svg x="{cx-14}" y="{cy-60}" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{ICONS[ic]}</svg>'
        o+=f'<text x="{cx}" y="{cy-2}" text-anchor="middle" class="sk-a" fill="{c}">{E(a)}</text><text x="{cx}" y="{cy+22}" text-anchor="middle" class="sk-b">{E(w)}</text>'
    ox,oy,r=SK_CENTRE[n]
    w1,w2=(centre.split(" ",1)+[""])[:2]
    k=r/66
    o+=f'<g transform="translate({ox} {oy}) scale({k:.3f})"><circle r="66" fill="#fdf0c8" fill-opacity=".95" stroke-opacity="0"/><circle r="66" fill="#e5b94a" fill-opacity=".28" stroke="#c9972b" stroke-width="2.2" stroke-dasharray="3 5" stroke-linecap="round"/><svg x="-15" y="-50" width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#b9801c" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{ICONS["lotus"]}</svg><text y="6" text-anchor="middle" class="sk-c">{E(w1)}</text><text y="28" text-anchor="middle" class="sk-c">{E(w2)}</text></g>'
    o+='</svg>'
    return o

def grammar_section(g):
    def tbl(head, rows, cls=""):
        h="".join(f"<th>{E(x)}</th>" for x in head)
        r="".join("<tr>"+"".join(f"<td>{c}</td>" for c in row)+"</tr>" for row in rows)
        return f'<div class="gscroll"><table class="gtable {cls}"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'
    o='<h2 id="grammar">Sanskrit structure</h2>\n<p class="sect-note">How the verse is built. Grammar only, with no interpretation.</p>\n<div class="gram">'
    o+='<section class="gblock"><h3><span class="gk">Anvaya</span> The sentence in plain order</h3><p>'+E(g["anvaya_note"])+'</p>'
    o+=tbl(["Who is saluted","Her description (every line ends: namo ’stu)"],[[f'<span lang="sa-Latn"><i>{E(a)}</i></span>',f'<span lang="sa-Latn"><i>{E(b)}</i></span>'] for a,b,c in g["anvaya"]])+'</section>'
    o+='<section class="gblock"><h3><span class="gk">Vibhakti</span> '+E(g["vib_title"])+'</h3>'+"".join(f'<p>{x}</p>' for x in g["vib_notes"])
    o+=tbl(["Name","The word “to her”","Case"],[[f'<span lang="sa">{a}</span> <i>{E(b)}</i>',f'<span lang="sa">{c}</span> <i>{E(d)}</i>',E(e)] for a,b,c,d,e in g["vib_rows"]])+'</section>'
    o+='<section class="gblock"><h3><span class="gk">Samāsa</span> Compound analysis</h3><p>'+E(g["sam_note"])+'</p>'
    o+=tbl(["Compound","Parts","Type","Meaning"],[[f'<span lang="sa">{a}</span><i>{E(b)}</i>',E(c),E(d),E(e)] for a,b,c,d,e in g["sam_rows"]],"gcomp")+'</section>'
    o+='<section class="gblock"><h3><span class="gk">Sandhi</span> Where sounds join</h3>'
    o+=tbl(["Before","After","What happens"],[[f'<i>{E(a)}</i>',f'<i>{E(b)}</i>',E(c)] for a,b,c in g["sandhi"]])+'</section>'
    o+='<p class="gfoot">'+E(g["foot"])+'</p></div>'
    return o

def forms_block(v):
    o=f'<div class="ov-card ov-forms"><h2 class="ov-h">{E(v.get("forms_title","Explore the key ideas"))}</h2><p class="ov-sub">Tap a card to open its meaning and a question to carry with you.</p><div class="fgrid">'
    for n,((a,b),(body,ask)) in enumerate(zip(v["keypoints"],v["formnotes"])):
        o+=f'<details name="forms" class="fcard fc{n}"><summary><span class="ic ic{n}">{icon(v["icons"][n],26)}</span><span class="ft"><b>{E(a)}</b><small>{E(b.split(":")[0])}</small></span></summary><div class="fbody"><p>{E(body)}</p><p class="fask"><b>Pause and reflect:</b> {E(ask)}</p></div></details>'
    return o+'</div></div>'

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
    if v.get("sheet") and not v.get("sketchfile"): v["sketchfile"] = f"{base}-{v['slug']}-sketch-note.png"
    if v.get("sheet") and not v.get("sketchalt"): v["sketchalt"] = f"Sketch note for {sname} {lab(v)}: the Sanskrit verse, its meaning, the key ideas, key words and a life takeaway."
    v["title"] = f"{sp} Verse {v['n']} Meaning – {opening(v,3)}"
    d1 = f"{sp} Verse {v['n']} ({opening(v,4)}): {plain(tail)}."
    for extra in (" Word-by-word meaning, English translation and a short meditation."," Word-by-word meaning and English translation."," Meaning in English."):
        if len(d1 + extra) <= 158: d1 += extra; break
    v["desc"] = d1
    if v.get("ttl"): v["title"], v["desc"] = v["ttl"], v["dsc"]
    art = {"@context":"https://schema.org","@type":"Article","headline":v["title"],"description":v["desc"],
           "author":{"@type":"Person","name":AUTHOR,"url":SITE+"/about/"},"datePublished":"@@PUB@@","dateModified":"@@MOD@@","inLanguage":"en","image":SITE+"/assets/og.png","isAccessibleForFree":True,
           "mainEntityOfPage":SITE+"/"+path+"/","publisher":{"@type":"Person","name":AUTHOR,"url":SITE+"/about/"}}
    rows = "".join(f'<tr><td class="t-s" lang="sa">{a}<i>{E(b)}</i></td><td>{E(c)}</td></tr>' for a,b,c,d in v["words"])
    notes = "".join(f'<div class="word"><div class="w">{a}<i>{E(b)}</i></div><p>{d}</p></div>' for a,b,c,d in v["words"] if d)
    words = f'<table class="wtable"><thead><tr><th>Sanskrit</th><th>Meaning</th></tr></thead><tbody>{rows}</tbody></table>' + (f'<details class="wnotes" open><summary>Notes on each word</summary>{notes}</details>' if notes else "")
    gramsec = grammar_section(v["grammar"]) if v.get("grammar") else ""
    gramlink = '<a href="#grammar">Sanskrit structure</a>' if v.get("grammar") else ""
    ins = "".join(ins_card(a,b) for a,b in v["insights"])
    med = "".join(med_step(x) for x in v["meditation"])
    medlink = '<a href="#meditation">Meditation</a>' if v["meditation"] else ''
    medsec = f'<h2 id="meditation">Practical meditation</h2>\n<ol class="med">{med}</ol>' if v["meditation"] else ''
    reflink = '<a href="#reflection">Reflection</a>' if v["reflection"] else ''
    refsec = f'<h2 id="reflection">Reflection for today</h2>\n{ref_block(v["reflection"])}' if v["reflection"] else ''
    closesec = close_block(v["closing"]) if v["closing"] else ''
    p = f'<a href="/{base}/{prev["slug"]}/">← {lab(prev)}</a>' if prev else '<span class="off">← Previous</span>'
    n = f'<a href="/{base}/{nxt["slug"]}/">{lab(nxt)} →</a>' if nxt else (f'<a href="/{base}/">All verses →</a>' if v["n"]>=total else f'<span class="off">Verse {v["n"]+1} coming soon →</span>')
    other = ("Kanakadhāra Stotram","kanakadhara") if base=="sri-suktam" else ("Śrī Sūktam","sri-suktam")
    items = "".join(f'<li><a href="/{base}/{x["slug"]}/"{" class=\"on\" aria-current=\"page\"" if x["slug"]==v["slug"] else ""}><b>{x["n"]}</b><span class="t">{E(x["sub"].split(" – ")[0])}</span></a></li>' for x in lst)
    vnav = f'<aside class="vnav" aria-label="Verses"><p class="vn-title"><a href="/{base}/">{sname}</a></p><ol>{items}</ol><p class="vn-other"><a href="/{other[1]}/">{other[0]} →</a></p></aside>'
    vscript = '<script>try{var a=document.querySelector(".vnav a.on");if(a&&a.scrollIntoView&&innerWidth<1100){var o=a.parentNode.parentNode;o.scrollLeft=a.offsetLeft-o.offsetWidth/2+a.offsetWidth/2}}catch(e){}</script>'
    body = head(v["title"],v["desc"],path+"/",art,"article") + f'<script type="application/ld+json">{json.dumps(bc_ld(parts),ensure_ascii=False)}</script>' + nav(navkey) + f'''
<header class="vhero"><div class="vh-in"><div class="vh-text">
<p class="vh-kick" lang="sa">श्री</p>
<h1>{v["h1"]}</h1>
<p class="lede">{E(v["sub"])}</p>
<p class="vh-by">By {AUTHOR}</p></div>
<div class="vh-art">{four_art(v["keypoints"], v["icons"]) if v.get("keypoints") else YANTRA}</div></div></header>
<main class="wrap has-vnav">{vnav}<article>
{crumbs([(sname,base+"/"),(lab(v),None)])}
<nav class="vtabs" aria-label="On this page"><a href="#overview">Overview</a><a href="#words">Word by word</a>{gramlink}<a href="#insights">Deeper insights</a>{medlink}{reflink}</nav>
<section id="overview" class="ov"><div class="ov-card ov-verse"><h2 class="ov-h">The verse</h2><p class="deva" lang="sa">{v["deva"]}</p><p class="iast" lang="sa-Latn">{v["iast"]}</p></div>
<div class="ov-card ov-mean"><h2 class="ov-h">Meaning in short</h2><p>{E(v["meaning"])}</p>{('<p class="ov-quote">'+E(v["tagline"])+'</p>') if v.get("tagline") else ""}</div>
{('<div class="ov-card ov-high"><h2 class="ov-h">Key highlights</h2><ul>'+"".join('<li><span class="ic ic'+str(n)+'">'+icon(v["icons"][n],22)+'</span><span><b>'+E(a)+'</b> '+E(b)+'</span></li>' for n,(a,b) in enumerate(v["keypoints"]))+'</ul></div>') if v.get("keypoints") else ""}
{forms_block(v) if v.get("formnotes") else ""}
{('<div class="ov-card ov-sketch"><h2 class="ov-h">Sketch note</h2><div class="sk-wrap">'+(f'<img class="sk-img" src="/assets/sketch/{v["sketchfile"][:-4]}-1344.webp" width="1344" height="896" loading="lazy" alt="{E(v["sketchalt"])}">' if v.get("sketchfile") else sketch_note(v["keypoints"], v["icons"]))+'</div><p class="sk-cap">'+('A one-page summary of the verse: Sanskrit, meaning, key ideas, key words and a takeaway. On a phone, open it full screen.' if v.get("sketchfile") else 'The key ideas of the verse at a glance.')+'</p>'+('<p class="sk-act"><a class="btn-s" href="/assets/sketch/'+v["sketchfile"]+'" download>Download the sketch note (PNG)</a></p>' if v.get("sketchfile") else "")+'</div>') if v.get("keypoints") else ""}</section>
{ad("below-verse")}
<h2 id="words">Word-by-word meaning</h2>
<p class="sect-note">The literal meaning of each word.</p>
{words}
{gramsec}
<h2 id="insights">Deeper spiritual insights</h2>
<p class="sect-note">Interpretation and reflection: ideas that help us read the verse, not part of the text itself.</p>
{ins}
{medsec}
{refsec}
{closesec}
<p class="crumbs">Terms used here are explained in the <a href="/glossary/">glossary</a>. This commentary was prepared with AI assistance; <a href="/about/">read more</a>.</p>
{ad("end")}
<div class="pager">{p}{n}</div>
</article></main>{vscript}<script src="/assets/verse.js" defer></script>''' + foot()
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

ASTS = [
 ("The prayer behind every stanza","Each of the eight stanzas has the same shape: a string of titles praising the Goddess, then a closing prayer that names the form being honoured and asks her to protect the devotee always. She is addressed as the beloved of Vishnu, the slayer of the demon Madhu. The hymn is less a list of requests than a long act of praise that ends each time in one plain request for protection."),
 ("Stanza 1: Ādi Lakshmi","The first form is praised as the beautiful consort of Vishnu, the sister of the moon (both are said to have risen from the ocean of milk), golden in colour and a dweller in the lotus. Gods and sages honour her and the Vedas praise her; she speaks sweetly, gives peace and showers good qualities. The gift named here is liberation, so the source of prosperity is also pictured as a source of freedom."),
 ("Stanza 2: Dhānya Lakshmi","Dhānya Lakshmi is the Lakshmi of grain, but this stanza does not mention grain. It describes her as the destroyer of the faults of the Kali age, born of the milk ocean, of auspicious form and dwelling in mantras, served by the gods and praised by the Vedas. The link to food comes from the name in the closing prayer. One reading, which we bring to the stanza, is that nourishment is a blessing that rests on purity and auspiciousness."),
 ("Stanza 3: Dhairya Lakshmi","She is addressed by names tied to Vishnu and to the sage Bhṛgu (Bhārgavī, “daughter of Bhṛgu”), as mantra in form, quick to give results and an unfolder of knowledge. The gifts named are freedom from the fear of worldly life and release from sin, and the people who rely on her are the good. Courage is pictured here as freedom from fear, not as aggression."),
 ("Stanza 4: Gaja Lakshmi","The imagery turns royal. She is the destroyer of misfortune and the giver of every fruit, surrounded by the four divisions of a king’s army (chariots, elephants, horses and foot-soldiers) and by her attendants, and praised by the whole world. Vishnu, Shiva and Brahmā all worship her, and she removes distress. The picture is one of dignity and standing, the grandeur the elephants stand for in the older sculptures."),
 ("Stanza 5: Santāna Lakshmi","As with Dhānya, this stanza does not speak of children. It praises her as the rider of the divine bird, the enchantress who holds the discus, an increaser of love or devotion (the word <em>rāga</em> can also mean a musical mode) and a sea of virtues who wishes the world well. She is adorned by the seven notes of music and praised in song, and gods, demons, sages and humans alike honour her. The theme of family and continuity comes from the name in the closing prayer."),
 ("Stanza 6: Vijaya Lakshmi","She is seated on a lotus, gives a good destiny, unfolds knowledge and is full of song. The stanza pictures daily worship with kumkum, perfume and instruments. Then it names the <a href=\"/kanakadhara/\">Kanakadhāra hymn</a> and the teacher Śaṅkara, saying that her feet are honoured by him and that she is praised in the glory of that hymn. This is the stanza that links the Ashtalakshmi hymn with the Kanakadhāra Stotram, and it also shows that the Ashtalakshmi hymn is the later of the two."),
 ("Stanza 7: Vidyā Lakshmi","She is addressed as Bhāratī, a name of Sarasvatī, and as Bhārgavī, so learning and prosperity are named together in one breath. She destroys sorrow, is adorned with jewels and ear ornaments, smiles and is wrapped in peace. She gives the nine treasures of the god of wealth, removes the faults of the Kali age and fulfils wishes. Knowledge is pictured with jewels and a calm smile, not only with books."),
 ("Stanza 8: Dhana Lakshmi","The wealth stanza opens with sound instead of pictures: the beat of the kettledrum and the blare of conches, written out in drum syllables. Wealth here is a festival. Yet the stanza ends on a quiet note: she is worshipped through the Vedas, the Purāṇas and the epics, and she shows the Vedic path. Money is celebrated, and then tied to guidance on how to live."),
 ("The closing verse","After the eight stanzas comes a short closing salutation. It bows to the eight forms together: the giver of boons who takes any form at will, seated on Vishnu’s chest, a liberator of devotees, holding the conch, discus and mace (the same emblems as in <a href=\"/mahalakshmi-ashtakam/verse-1/\">Verse 1 of the Mahālakṣmī Aṣṭakam</a>), of universal form, the mother of the world; it ends with a wish for auspiciousness. Printed versions often label it a <em>phalaśruti</em>, but it states no fruit of reciting, so it is better read as a salutation and blessing."),
]

def page_asts():
    t = "Ashtalakshmi Stotram Meaning in English – Stanza by Stanza"
    d = "Ashtalakshmi Stotram meaning in English: what each of the eight stanzas says about Adi, Dhanya, Dhairya, Gaja, Santana, Vijaya, Vidya and Dhana Lakshmi."
    parts = [("Ashtalakshmi Stotram","ashtalakshmi-stotram/")]
    ld = {"@context":"https://schema.org","@type":"Article","headline":t,"author":{"@type":"Person","name":AUTHOR,"url":SITE+"/about/"},"datePublished":"@@PUB@@","dateModified":"@@MOD@@","inLanguage":"en","image":SITE+"/assets/og.png","isAccessibleForFree":True,"mainEntityOfPage":SITE+"/ashtalakshmi-stotram/","publisher":{"@type":"Person","name":AUTHOR,"url":SITE+"/about/"}}
    cards = "".join(f'<div class="card"><h3>{E(a)}</h3><p>{b}</p></div>' for a,b in ASTS)
    body = head(t,d,"ashtalakshmi-stotram/",ld,"article") + f'<script type="application/ld+json">{json.dumps(bc_ld(parts),ensure_ascii=False)}</script>' + nav("") + f'''
<main class="wrap">{crumbs([("Ashtalakshmi Stotram",None)])}
<p class="shri small" lang="sa">श्री</p>
<h1>Ashtalakshmi Stotram – meaning in English</h1>
<p class="lede">The Ashtalakshmi Stotram is a Sanskrit hymn of eight stanzas, one for each of the <a href="/ashtalakshmi/">eight forms of Lakshmi</a>, with a short closing salutation. This page explains what each stanza says.</p>
<p class="crumbs">By {AUTHOR}</p>
<p><small>A note on the words: this hymn is a modern composition, not an ancient scripture, so this page explains it and does not print the verses. Please use a trusted printed or recorded version for chanting; printed versions differ in small details.</small></p>
<h2>About the hymn</h2>
<p>According to Wikipedia, the hymn was composed in Chennai in the early 1970s by U. V. Srinivasa Varadachariyar, a scholar of the Sri Vaishnava tradition, and became widely known through recordings in the 1980s. I have not been able to confirm this from a second source, so please treat the attribution as provisional. The eight forms are taken in this order: Ādi, Dhānya, Dhairya, Gaja, Santāna, Vijaya, Vidyā and Dhana. (The <a href="/ashtalakshmi/">explainer page</a> lists Dhana second; the order differs between lists.)</p>
<h2>What the stanzas say</h2>
<p>These are my own explanations of the hymn’s ideas, and any practical lessons are reflections inspired by it, not literal lines in the text.</p>
{cards}
{ad("below-verse")}
<h2>A way to read it</h2>
<p>Some people read one stanza a day, or the stanza of the form they feel most in need of. A simple way to begin is to read the meaning of a stanza here, then listen to or chant it from your own book, and sit quietly for a minute with the form’s name. This is a devotional and reflective reading. It does not promise any outcome or guarantee wealth.</p>
<p>See also: <a href="/ashtalakshmi/">Aṣṭalakṣmī – the eight forms</a>, <a href="/kanakadhara/">Kanakadhāra Stotram</a> and <a href="/mahalakshmi-ashtakam/">Mahālakṣmī Aṣṭakam</a>.</p>
<p><small>This page was prepared with AI assistance and reviewed by the author. <a href="/about/">Read more</a>.</small></p>
{ad("end")}
</main>''' + foot()
    write("ashtalakshmi-stotram", body, "0.8")

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
<p>The Ashtalakshmi are also worshipped together in temples and in the <a href="/ashtalakshmi-stotram/">Ashtalakshmi Stotram</a>, a hymn that praises each form in turn. Prosperity in its wider sense is also the theme of the <a href="/sri-suktam/">Śrī Sūktam</a>, the <a href="/kanakadhara/">Kanakadhāra Stotram</a> and the <a href="/mahalakshmi-ashtakam/">Mahālakṣmī Aṣṭakam</a> on this site.</p>
<p><small>This page was prepared with AI assistance and reviewed by the author. <a href="/about/">Read more</a>.</small></p>
{ad("end")}
</main>''' + foot()
    write("ashtalakshmi", body, "0.8")

AARTI = [
 ("The refrain: gratitude","Every stanza returns to the same cry, <em>Om Jai Lakshmi Mata</em>, “Victory to Mother Lakshmi”. Repeating it is a way of saying thank you: for food on the table, for work, for family, for health and for the chance to be useful. Lakshmi is felt differently by different people: as honest profit by a trader, as a good harvest by a farmer, as understanding by a student, as a settled and happy household by a parent. Having wealth and understanding what wealth is for are two different things."),
 ("First stanza: served by Vishnu and the creator","The aarti opens by placing Lakshmi beside Hari Vishnu, the preserver of the world, and the creator, who serve her night and day. Tradition pairs Lakshmi, who stands for prosperity, with Vishnu, who stands for order and right conduct. The quiet lesson is that wealth and dharma should walk together. Earning money is an achievement; keeping it responsibly and using it for something worthwhile is the larger task."),
 ("Second stanza: one mother, many names","Here she is addressed as Umā, Ramā and Brahmāṇī, names usually linked with Pārvatī, Lakshmi and the power of Brahmā (often joined with Sarasvatī), and as the mother of the world. The sun and moon meditate on her and the sage Nārada sings of her. Readers take the stanza to say that the great goddesses are not rivals but many faces of one divine feminine."),
 ("Third stanza: the stainless Durgā","She is called Durgā in form, spotless, and the giver of comfort and wealth; whoever meditates on her receives success and prosperity. It is a reminder that Lakshmi is not only gentle. Prosperity also needs strength: the courage to face a bad year, the patience to wait through uncertainty and the character to stay honest under pressure. A person who keeps their calm and their integrity in a crisis holds a wealth that does not appear on a balance sheet."),
 ("Fourth stanza: from the unseen to the seen","The stanza names her as the one who dwells in the lower worlds, the giver of good, the one who lights up the working of karma, and the rescuer from the ocean of worldly life. One reading is that fortune and the results of our actions are not separate: effort and conduct matter, and grace works alongside them, not instead of them."),
 ("Fifth stanza: the true wealth of a home","Perhaps the most practical stanza. It says that where she lives, all good qualities come, everything becomes possible and the mind is no longer anxious. The emphasis is on virtues (<em>sadguṇa</em>), not on gold. A home with plenty of money but no trust is not a happy one, while a home where elders are respected, children learn good values, guests are welcomed and the family stands together has a deep kind of wealth. This does not mean good values remove every money problem; they give lasting prosperity a firmer base."),
 ("Sixth stanza: nothing happens without her","Without her, the stanza says, sacrifices would not be performed, no one would find clothing, and the plenty of food and drink would not exist. Behind a single meal stand farmers, nature, transporters and traders; behind a business stand employees, customers and suppliers. The stanza invites a question: if I have received prosperity, am I also adding something worthwhile to other people’s lives? Paying people fairly, dealing honestly and helping those in need are ways to keep worshipping after the aarti ends."),
 ("Seventh stanza: born of the milk ocean","She is praised as the home of good qualities, beautiful, and born of the ocean of milk. Without her, the stanza says, the fourteen jewels of that churning could not be had. It points to the old story of the churning of the ocean, in which Lakshmi rose from the waters. The same story lies behind her name Sāgarasambhavā in <a href=\"/kanakadhara/verse-2/\">Verse 2 of the Kanakadhāra Stotram</a>."),
 ("Final stanza: the fruit of singing","The closing stanza says that whoever sings this aarti to Mahālakṣmī finds joy filling the heart and sin falling away. Singing alone does not cancel the results of what we do, and devotion is not an exemption from responsibility. What it can do is help us see our own faults, such as greed, pride, resentment, fear and ingratitude, and find the strength to turn back to the right path. The deeper fruit of prayer is not always that life changes as we wish; it can be that we gain the wisdom to live rightly whatever comes."),
]

def page_aarti():
    t = "Lakshmi Aarti Meaning and How to Perform It on Diwali"
    d = "Lakshmi Aarti (Om Jai Lakshmi Mata): how to perform it at home on Diwali, and what each stanza means, explained in English."
    parts = [("Lakshmi Aarti","lakshmi-aarti/")]
    ld = {"@context":"https://schema.org","@type":"Article","headline":t,"author":{"@type":"Person","name":AUTHOR,"url":SITE+"/about/"},"datePublished":"@@PUB@@","dateModified":"@@MOD@@","inLanguage":"en","image":SITE+"/assets/og.png","isAccessibleForFree":True,"mainEntityOfPage":SITE+"/lakshmi-aarti/","publisher":{"@type":"Person","name":AUTHOR,"url":SITE+"/about/"}}
    cards = "".join(f'<div class="card"><h3>{E(a)}</h3><p>{b}</p></div>' for a,b in AARTI)
    body = head(t,d,"lakshmi-aarti/",ld,"article") + f'<script type="application/ld+json">{json.dumps(bc_ld(parts),ensure_ascii=False)}</script>' + nav("") + f'''
<main class="wrap">{crumbs([("Lakshmi Aarti",None)])}
<p class="shri small" lang="sa">श्री</p>
<h1>Lakshmi Aarti – meaning and how to perform it</h1>
<p class="lede">The Lakshmi Aarti, “Om Jai Lakshmi Mata”, is the song of light sung to Goddess Lakshmi at the end of worship, above all on the evening of Diwali. This page explains how the aarti is performed at home and what its stanzas say.</p>
<p class="crumbs">By {AUTHOR}</p>
<nav class="toc" aria-label="On this page"><a href="#how">How to perform it</a><a href="#meaning">What it says</a><a href="#prayer">A closing prayer</a></nav>
<p><small>A note on the words: the aarti is a sung folk hymn, and printed versions differ slightly from region to region and family to family. This page explains it and does not print the words, so please use the version your family or temple sings.</small></p>
<h2>What is an aarti?</h2>
<p>An aarti is a short act of worship in which a lit lamp is waved before the deity while a hymn is sung. The word is usually traced to the Sanskrit <em>ārātrika</em>, connected with the night and with the light that drives away darkness. At the end the flame is shared: people pass their hands over it and bring them to the eyes and forehead, taking the blessing of the light.</p>
<p>The Lakshmi Aarti is sung on Fridays in many homes, and above all during the Lakshmi Puja of Diwali. The date and the auspicious time (<em>muhūrta</em>) of the evening puja change every year, so check a local panchang or your temple for the exact time.</p>
<h2 id="how">How to perform it at home</h2>
<p>There is no single rule, and families differ. This is a common simple order.</p>
<ol>
<li><strong>Prepare the place.</strong> Clean the space and set an image or idol of the Goddess on a clean cloth. Many people draw a small rangoli at the entrance.</li>
<li><strong>Prepare the thali.</strong> A plate with a ghee lamp (<em>dīpa</em>), incense, flowers, kumkum, and a small piece of camphor or a second lamp for the aarti. Keep the sweets or fruit that will be offered close by.</li>
<li><strong>Complete the puja first.</strong> The aarti closes the worship. Offer the flowers, kumkum and sweets before you begin.</li>
<li><strong>Light the lamp.</strong> Hold the thali in your right hand, with the left hand free to ring a small bell if you have one.</li>
<li><strong>Wave the light.</strong> While the hymn is sung, move the thali slowly in a clockwise circle in front of the image. Some families make seven turns, some three, some wave it to the feet, the middle and the face in turn. Follow your own tradition.</li>
<li><strong>Take the aarti.</strong> When the hymn ends, pass your hands over the flame and touch them to your eyes and forehead. Then offer the prasad.</li>
<li><strong>Stay for a moment.</strong> A minute of quiet gratitude closes the aarti well.</li>
</ol>
<p><small>Safety: keep long sleeves, dupattas and curtains away from the flame, and keep children at a distance from the lit thali.</small></p>
<h2 id="meaning">What the aarti says, stanza by stanza</h2>
<p>The aarti has a refrain and eight short stanzas. Below, each is explained in simple words. These are my own explanations of the hymn’s ideas, and the practical lessons are reflections inspired by it, not literal lines in the text.</p>
{cards}
{ad("below-verse")}
<h2 id="prayer">A closing prayer</h2>
<p>After the aarti, many people add a few words of their own. Here is one, in plain English.</p>
<blockquote><p>O Mother Mahalakshmi, give us enough wealth to live with dignity and to meet our duties, and the wisdom never to let the pursuit of wealth make us forget our dharma. Give us courage in hard times and humility when success comes. Bless our homes with food, peace and understanding, and may we never waste the food you give. When we succeed, let us stay grateful; when we fail, let us keep our courage; when we receive, let us learn to share. Make us worthy keepers of the prosperity we ask for.</p></blockquote>
<h2>One thought to take away</h2>
<p>We often pray for Lakshmi to enter our homes. We might also ask whether we are building a home worthy of the qualities she stands for: gratitude in place of complaint, integrity in place of greed, love in place of ego, humility in place of pride, and a heart that remembers those who have less. Money can build a house, but values make it a home. Money can buy comfort but cannot guarantee contentment. May we receive prosperity with gratitude, keep it with wisdom, use it rightly and share it with compassion.</p>
<p>This page is a devotional and reflective reading. It does not promise any outcome or guarantee wealth.</p>
<p><strong>For the puja table:</strong> a <a href="/lakshmi-aarti-printable/">one-page printable guide</a> with the steps and a line on each stanza, to keep beside your aarti booklet.</p>
<p>See also: <a href="/mahalakshmi-ashtakam/">Mahālakṣmī Aṣṭakam</a> to chant, and the <a href="/sri-suktam/">Śrī Sūktam</a>.</p>
<p><small>This page was prepared with AI assistance and reviewed by the author. <a href="/about/">Read more</a>.</small></p>
{ad("end")}
</main>''' + foot()
    write("lakshmi-aarti", body, "0.8")

AARTI_ONE = [
 ("Refrain","“Victory to Mother Lakshmi”: a thank-you for food, work, family and health."),
 ("1st stanza","Lakshmi beside Vishnu: wealth should walk with right conduct."),
 ("2nd stanza","One Mother, many names: the goddesses are faces of one divine feminine."),
 ("3rd stanza","The stainless Durgā: prosperity needs courage and steady character."),
 ("4th stanza","From the unseen to the seen: effort and grace work together."),
 ("5th stanza","Where she dwells, good qualities come: virtues, not gold, make a home."),
 ("6th stanza","Nothing happens without her: behind every meal stand many hands, so give back."),
 ("7th stanza","Born of the milk ocean: the source of the jewels of the churning."),
 ("Final stanza","The fruit of singing: a glad heart and the strength to turn from our faults."),
]

def page_aarti_print():
    t = "Lakshmi Aarti at Home – Printable Guide for Diwali"
    d = "One-page printable guide to the Lakshmi Aarti: what to keep ready, the steps and a line on each stanza. Print it and keep it beside your aarti booklet."
    parts = [("Lakshmi Aarti","lakshmi-aarti/"),("Printable guide","lakshmi-aarti-printable/")]
    ld = {"@context":"https://schema.org","@type":"Article","headline":t,"author":{"@type":"Person","name":AUTHOR,"url":SITE+"/about/"},"datePublished":"@@PUB@@","dateModified":"@@MOD@@","inLanguage":"en","image":SITE+"/assets/og.png","isAccessibleForFree":True,"mainEntityOfPage":SITE+"/lakshmi-aarti-printable/","publisher":{"@type":"Person","name":AUTHOR,"url":SITE+"/about/"}}
    mean = "".join(f'<li><strong>{E(a)}.</strong> {E(b)}</li>' for a,b in AARTI_ONE)
    body = head(t,d,"lakshmi-aarti-printable/",ld,"article") + f'<script type="application/ld+json">{json.dumps(bc_ld(parts),ensure_ascii=False)}</script>' + nav("") + f"""
<main class="wrap">{crumbs([("Lakshmi Aarti","lakshmi-aarti/"),("Printable guide",None)])}
<div class="printpage">
<button type="button" class="btn noprint" onclick="window.print()">Print this page</button>
<p class="shri small" lang="sa">श्री</p>
<h1>Lakshmi Aarti at home</h1>
<p class="pp-sub">A one-page guide to keep beside your aarti booklet. It does not print the words of the aarti, so sing from the version your family or temple uses.</p>
<div class="pp-cols">
<section>
<h2>Keep ready</h2>
<ul class="pp-list">
<li>Image or idol of the Goddess on a clean cloth</li>
<li>A thali with a ghee lamp, incense, flowers and kumkum</li>
<li>Camphor or a second small lamp for the aarti</li>
<li>A small bell, if you have one</li>
<li>Sweets or fruit for the offering (prasad)</li>
<li>Your aarti booklet or printed words</li>
</ul>
<h2>The steps</h2>
<ol class="pp-list">
<li><strong>Finish the puja first.</strong> Offer flowers, kumkum and sweets before the aarti begins.</li>
<li><strong>Light the lamp.</strong> Hold the thali in your right hand and keep the left free for the bell.</li>
<li><strong>Wave the light.</strong> Move the thali slowly in a clockwise circle before the image while the hymn is sung. Follow your family’s number of turns.</li>
<li><strong>Take the aarti.</strong> When the hymn ends, pass your hands over the flame and touch them to your eyes and forehead.</li>
<li><strong>Offer the prasad</strong> and stay a minute in quiet gratitude.</li>
</ol>
<p class="pp-safe"><strong>Safety.</strong> Keep dupattas, long sleeves and curtains away from the flame, and keep children back from the lit thali.</p>
</section>
<section>
<h2>What each stanza says</h2>
<ul class="pp-list pp-mean">{mean}</ul>
<h2>A closing prayer</h2>
<p class="pp-prayer">O Mother Mahalakshmi, give us enough wealth to live with dignity and to meet our duties, and the wisdom never to let the pursuit of wealth make us forget our dharma. Give us courage in hard times and humility when success comes. Bless our homes with food, peace and understanding. Make us worthy keepers of the prosperity we ask for.</p>
</section>
</div>
<p class="pp-foot">Full explanation of each stanza: lakshmistuti.com/lakshmi-aarti/ · By {AUTHOR}</p>
</div>
<p class="noprint"><small>The full guide, with a longer explanation of every stanza, is at <a href="/lakshmi-aarti/">Lakshmi Aarti – meaning and how to perform it</a>. This page was prepared with AI assistance and reviewed by the author. <a href="/about/">Read more</a>.</small></p>
</main>""" + foot()
    write("lakshmi-aarti-printable", body, "0.6")

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
    page_ashta(); page_asts(); page_aarti(); page_aarti_print(); page_yantra(); page_gl(); page_about(); page_contact(); page_privacy(); page_404(); assets(); sitemap()
    json.dump(MANIFEST, open(MANIFEST_PATH,"w",encoding="utf-8"), indent=1, ensure_ascii=False)
    print("built", len(PAGES), "pages")
