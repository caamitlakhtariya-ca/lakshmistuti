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
TODAY = "2026-10-12"
GSC_TOKEN = "ydCk8z62OzpGbv6EnLvQAu8VoJl7T40cv6htu9_FsWs"  # Google Search Console site verification
GA_ID = ""          # e.g. "G-XXXXXXXXXX"  -> switches Google Analytics on
ADSENSE_CLIENT = "" # e.g. "ca-pub-1234567890123456" -> switches AdSense on after approval
CONTACT_EMAIL = "amitnlakhtariya@gmail.com"  # interim address; to be replaced by the dedicated site Gmail once created
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
   ("आर्द्राम्","Ārdrām","Tender, compassionate, soft","She who makes life moist and nourished."),
   ("यः करिणीम्","Yaḥ kariṇīm","She who gives the strength to accomplish every kind of work","She is the cause of activity and movement in life. This is one of the harder phrases of the hymn, and commentators differ. Another traditional reading takes <em>kariṇī</em> as “attended by elephants”."),
   ("यष्टिम्","Yaṣṭiṁ","The power joined with resolve, worship and austerity","The strength that comes as the lasting fruit of sustained practice, giving stability in life. The word also means a staff, a support."),
   ("सुवर्णाम्","Suvarṇām","Golden, shining with a pure, bright glow",""),
   ("हेममालिनीम्","Hema-mālinīm","Adorned with a garland of gold","A symbol of splendour, grace and dignity."),
   ("सूर्याम्","Sūryām","Radiant like the sun, life-giving","The sun’s brilliance never stops; it gives energy and strength continuously. In Verse 13 she was moon-like (<em>Chandrā</em>); here she is sun-like. Together they bring coolness and fire."),
   ("हिरण्मयीम्","Hiraṇmayīṁ","Gold-like in brilliance, divine and full of divine radiance",""),
   ("लक्ष्मीम्","Lakṣmīṁ","Mother Lakshmi","The Goddess of prosperity, beauty, grace and splendour."),
   ("जातवेदो म आवह","Jātavedo ma āvaha","O Agni, knower of all births, please bring this divine Lakshmi into my life",""),
  ],
  meaning="O Agni, please invite into my life that Goddess Lakshmi who is tender and compassionate, the power that brings every undertaking to fulfilment, who shines like gold, wears a garland of gold, is radiant like the sun, and is filled with divine brilliance.",
  insights=[
   ("Tenderness and compassion (Ārdrām)","Wealth is not only hard power; it should carry gentleness, kindness and love as well. Only then does it last."),
   ("Action and resolve (Yaḥ kariṇīm, Yaṣṭiṁ)","Lakshmi dwells where there is action and resolve, where there is no laziness but steady inspiration and practice."),
   ("Beauty and radiance (Suvarṇām, Hema-mālinīm, Sūryām, Hiraṇmayīṁ)","Prosperity is not only material wealth. It is the beauty of life, divinity and inner light, which shines itself and also lights up others."),
   ("The invitation (Jātavedo ma āvaha)","Through Agni, the power of the self, we call Goddess Lakshmi. Calling her is not just a mantra; it is an inner preparation."),
  ],
  meditation=[],
  reflection="Is the radiance of Lakshmi in my life only outside, or inside as well? Am I making my action and resolve pure and strong enough for Lakshmi to stay in my life? Do I have the compassion and beauty within that can make wealth sacred?",
  closing="",
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
  n=16, slug="phalashruti", label="Phalaśruti",
  deva="यः शुचिः प्रयतो भूत्वा जुहुयादाज्यमन्वहम्।<br>श्रियः पञ्चदशर्चं च श्रीकामः सततं जपेत्॥",
  iast="Yaḥ śuciḥ prayato bhūtvā juhuyād ājyam anvaham,<br>Śriyaḥ pañcadaśarcaṁ ca śrīkāmaḥ satataṁ japet.",
  title="Śrī Sūktam Phalaśruti Meaning – Yaḥ Śuciḥ Prayato Bhūtvā Explained",
  desc="The Śrī Sūktam phalaśruti (Yaḥ Śuciḥ Prayato Bhūtvā) with Devanāgarī, transliteration, word-by-word meaning, the fruit of reciting the fifteen verses, and a closing meditation.",
  h1="Śrī Sūktam – Phalaśruti",
  sub="Yaḥ Śuciḥ Prayato Bhūtvā – the fruit of reciting the hymn",
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
TOTAL_SRI = 15  # core verses of the Śrī Sūktam (a closing phalaśruti follows)

GLOSSARY = [
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
 ("फलश्रुति","Phalaśruti","The “hearing of the fruits”: the closing verses that describe the benefit of reciting a hymn.","sri-suktam/phalashruti/"),
 ("शुचि","Śuci","Pure, clean.","sri-suktam/phalashruti/"),
 ("प्रयत","Prayata","Self-restrained, disciplined, composed.","sri-suktam/phalashruti/"),
 ("आज्य","Ājya","Clarified butter (ghee) used in fire offerings.","sri-suktam/phalashruti/"),
 ("अग्निहोत्र","Agnihotra","The daily fire offering made at sunrise and sunset.","sri-suktam/phalashruti/"),
 ("पञ्चदशर्च","Pañcadaśarca","Of fifteen verses (ṛc); the fifteen verses of the Śrī Sūktam.","sri-suktam/phalashruti/"),
 ("श्रीकाम","Śrīkāma","One who desires Śrī, prosperity.","sri-suktam/phalashruti/"),
 ("जप","Japa","Quiet, repeated recitation of a mantra.","sri-suktam/phalashruti/"),
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
def lab(v): return v.get("label") or f"Verse {v['n']}"
def page_home():
    v = [x for x in VERSES if "label" not in x][-1]
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
<div class="verse"><p class="label">Śrī Sūktam · {lab(v)}</p><p class="deva">{v["deva"]}</p><p class="iast">{v["iast"]}</p></div>
<p>{E(v["closing"] or v["meaning"])} <a href="/sri-suktam/{v["slug"]}/">Read the full commentary →</a></p>
{ad("home")}
</main>''' + INTRO_SCRIPT + foot()
    write("", body, "1.0")

def page_sri():
    t = "Śrī Sūktam Meaning in English – Verse by Verse Commentary"
    d = "Verse-by-verse English meaning of the Śrī Sūktam, the Vedic hymn to Goddess Lakshmi, with Devanāgarī, transliteration and word-by-word explanation."
    parts = [("Śrī Sūktam","sri-suktam/")]
    rows = ""
    for v in VERSES:
        rows += f'<a class="tile" href="/sri-suktam/{v["slug"]}/"><h3>{lab(v)}</h3><p>{E(v["sub"])}</p></a>'
    for n in range(len(VERSES)+1, TOTAL_SRI+1):
        rows += f'<div class="tile" style="opacity:.55"><h3>Verse {n} <span class="soon">coming soon</span></h3></div>'
    body = head(t,d,"sri-suktam/",bc_ld(parts)) + nav("sri") + f'''
<main class="wrap">{crumbs([("Śrī Sūktam",None)])}
<h1>Śrī Sūktam – verse by verse</h1>
<p class="lede">The Śrī Sūktam is a Vedic hymn praising Goddess Lakshmi (Śrī) as the source of prosperity, grace and auspiciousness. Each verse here has the Sanskrit text, a word-by-word meaning, deeper insights and a short practice.</p>
<p>Verses are published one at a time, so that each can be read and absorbed slowly before the next appears.</p>
<p><small>A note on the count: the Śrī Sūktam is usually counted as 15 verses. A few closing verses on the fruits of reciting it (the <em>phalaśruti</em>) are chanted after them, and some editions number those too, so you may see a slightly higher total elsewhere.</small></p>
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
    parts = [("Śrī Sūktam","sri-suktam/"),(lab(v),None)]
    art = {"@context":"https://schema.org","@type":"Article","headline":v["title"],"description":v["desc"],
           "author":{"@type":"Person","name":AUTHOR},"datePublished":TODAY,"dateModified":TODAY,"inLanguage":"en",
           "mainEntityOfPage":SITE+"/"+path+"/","publisher":{"@type":"Person","name":AUTHOR}}
    words = "".join(f'<div class="word"><div class="w">{a}<i>{E(b)}</i></div><p class="m">{E(c)}</p><p>{d}</p></div>' for a,b,c,d in v["words"])
    ins = "".join(f'<div class="card"><h3>{E(a)}</h3><p>{b}</p></div>' for a,b in v["insights"])
    med = "".join(f"<li>{E(x)}</li>" for x in v["meditation"])
    medlink = '<a href="#meditation">Meditation</a>' if v["meditation"] else ''
    medsec = f'<h2 id="meditation">Practical meditation</h2>\n<ol>{med}</ol>' if v["meditation"] else ''
    reflink = '<a href="#reflection">Reflection</a>' if v["reflection"] else ''
    refsec = f'<h2 id="reflection">Reflection for today</h2>\n<p>{E(v["reflection"])}</p>' if v["reflection"] else ''
    closesec = f'<p><em>{E(v["closing"])}</em></p>' if v["closing"] else ''
    p = f'<a href="/sri-suktam/{prev["slug"]}/">← {lab(prev)}</a>' if prev else '<span class="off">← Previous</span>'
    n = f'<a href="/sri-suktam/{nxt["slug"]}/">{lab(nxt)} →</a>' if nxt else (f'<a href="/sri-suktam/">All verses →</a>' if v.get("label") else f'<span class="off">Verse {v["n"]+1} coming soon →</span>')
    n = n.replace('Verse 15 coming soon','Phalaśruti coming soon') if v["n"]==15 and not nxt else n
    body = head(v["title"],v["desc"],path+"/",art,"article") + f'<script type="application/ld+json">{json.dumps(bc_ld(parts),ensure_ascii=False)}</script>' + nav("sri") + f'''
<main class="wrap"><article>
{crumbs([("Śrī Sūktam","sri-suktam/"),(lab(v),None)])}
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
