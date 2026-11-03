# Redesign extras for Śrī Sūktam (verses 1-16): key ideas, forms cards, sketch-note sheet.
# Every statement follows the verse's own words and the existing commentary on its page.

def _alt(n, desc):
    return (f"Sketch note for Śrī Sūktam Verse {n}: the Sanskrit verse and transliteration, its meaning, {desc}, "
            "key words and a life takeaway, around a picture of Goddess Lakshmi seated on a lotus.")

EXTRAS = {
1: dict(
  icons=["sun", "leaf", "gem", "moon"],
  keypoints=[("Hiraṇyavarṇā", "Golden: the glow of purity and auspiciousness"),
             ("Hariṇī", "Gentle: grace and softness, like a deer"),
             ("Garland", "Adorned: gold and silver, sun and moon together"),
             ("Chandrā", "Moon-like: shining, gladdening and serene")],
  tagline="Before asking for anything, the hymn describes her: golden, gentle, garlanded and moon-bright.",
  forms_title="Explore the four glimpses",
  formnotes=[
   ("Hiraṇyavarṇā means golden-coloured. In the commentary the gold stands for spiritual light, purity and auspiciousness more than for metal. The hymn begins with how she looks, not with what we want.", "Do I begin my day by noticing what is good, or what is missing?"),
   ("Hariṇī is read here as “deer-like”: gentle, graceful and swift. Other commentators hear “golden-yellow” or “she who takes away sorrow”. The three readings sit comfortably together.", "Where in my life could a gentler way work better than force?"),
   ("The garland of gold and silver pairs the colour of the sun with the colour of the moon. In the commentary it speaks of material and spiritual prosperity held together.", "Can I hold ambition and calm together in the same day?"),
   ("Chandrā means shining and gladdening, like the moon. The commentary reads her radiance as serene and balanced: it cools the mind and relieves stress instead of dazzling.", "Do the people around me feel calmer in my company?")],
  sheet=dict(
   salut_title="Four Glimpses", centre_title="Her Radiant Form", centre="Golden Grace",
   essence="Before asking for anything, the hymn paints her: golden, gentle, garlanded and moon-bright, and then invites her through Agni.",
   short="I ask Agni, the knower of all births, to bring to me Lakshmi: golden-hued, gentle as a doe, wearing garlands of gold and silver, moon-bright and golden in form.",
   salut=["Golden in colour: purity, light and auspiciousness.", "Gentle and graceful, like a deer.", "Wears garlands of gold and silver.", "Shining and gladdening like the moon."],
   words=[("हिरण्यवर्णां", "Hiraṇyavarṇāṁ", "Golden-coloured one"), ("हरिणीं", "Hariṇīṁ", "Deer-like, gentle"), ("चन्द्रां", "Chandrāṁ", "Moon-like, gladdening"), ("जातवेदो", "Jātavedo", "O Agni, knower of all births")],
   take=["Begin with gratitude for what is good.", "Choose gentleness before force.", "Let ambition and calm sit together.", "Be a comforting presence to others."]),
  sketchalt=_alt(1, "four glimpses of Lakshmi as Hiraṇyavarṇā (golden), Hariṇī (gentle), the wearer of the gold and silver garland, and Chandrā (moon-like)")),

2: dict(
  icons=["home", "coin", "leaf", "hands"],
  keypoints=[("Anapagāminī", "Constant: the one who never goes away"),
             ("Hiraṇya", "Gold: read as divine wealth, beyond money alone"),
             ("Gām aśvam", "Nourishment: cattle and horses, food and strength"),
             ("Puruṣān", "Good company: worthy, noble people")],
  tagline="She is asked to stay, and the wish widens from gold to nourishment, strength and good company.",
  forms_title="Explore the four ideas",
  formnotes=[
   ("Anapagāminī means “one who does not go away”. The verse asks not for a visit but for a lasting presence, which the commentary links to prosperity rooted in dharma: wisdom, peace, gratitude and contentment stay.", "What do I want to last, more than I want it to arrive?"),
   ("Hiraṇya is gold. The commentary reads it as more than money: wisdom, divine grace and clarity. It is the first item on the list, but not the only one.", "What does wealth mean for me beyond the number in my account?"),
   ("Gām aśvam is cattle and horses. Read as symbols, cattle are sustenance, enough to share, and horses are movement, energy and progress in one’s pursuits.", "Do I have the nourishment and energy to carry out what I intend?"),
   ("Puruṣān are worthy, noble people. The list ends with company, since the commentary counts being surrounded by wise and ethical people as part of true prosperity.", "Who are the people I am glad to have around me, and do they know it?")],
  sheet=dict(
   salut_title="Four Key Ideas", centre_title="More Than Money", centre="Lasting Abundance",
   essence="She is invited to stay for good, and the wish widens from gold to nourishment, strength and the company of good people.",
   short="O Jātaveda, bring to me Lakshmi, who never leaves, through whom I may obtain gold, cattle, horses and worthy people.",
   salut=["She who does not go away: a lasting presence.", "Gold, read as wisdom, grace and clarity.", "Cattle and horses: food, energy and progress.", "Worthy, noble people as part of true wealth."],
   words=[("अनपगामिनीम्", "Anapagāminīm", "One who never leaves"), ("हिरण्यं", "Hiraṇyaṁ", "Gold, divine wealth"), ("गामश्वम्", "Gām aśvam", "Cattle and horses"), ("पुरुषान्", "Puruṣān", "Good, noble people")],
   take=["Ask for lasting things, not passing ones.", "Count nourishment and energy as wealth.", "Keep good people close.", "Let wealth widen your life, not narrow it."]),
  sketchalt=_alt(2, "four key ideas: Anapagāminī (she who never leaves), Hiraṇya (gold as divine wealth), Gām aśvam (cattle and horses, nourishment and progress) and Puruṣān (good company)")),

3: dict(
  icons=["bolt", "path", "mountain"],
  keypoints=[("Aśva-pūrvā", "Energy: horses go ahead, speed and effort"),
             ("Ratha-madhyā", "Direction: the chariot, a structured path"),
             ("Hastināda", "Stability: elephants, strength and wisdom")],
  tagline="Horses, chariot and elephants: a picture of prosperity that arrives with energy, direction and steadiness.",
  forms_title="Explore the three images",
  formnotes=[
   ("Aśva-pūrvā: horses go ahead of her. In the commentary horses stand for speed, enthusiasm and energy, a reminder that progress asks for effort.", "Where could a little more energy move something forward this week?"),
   ("Ratha-madhyā: she sits in the middle of a chariot. The chariot is read as the structured path of life, so prosperity follows discipline and direction. Some readers also take it as the order of a royal procession.", "Is my daily effort pointed in a direction I would choose?"),
   ("Hastināda-prabodhinī: she is awakened by the trumpeting of elephants. Elephants stand for strength, stability and wisdom, so the prosperity she brings is meant to be grounded, not fleeting.", "What in my life needs a firmer, steadier foundation?")],
  sheet=dict(
   salut_title="Three Images", centre_title="Her Arrival", centre="Majestic Arrival",
   essence="Horses lead, a chariot carries and elephants announce her. Prosperity is pictured as energy, direction and steadiness together.",
   short="I call the divine Śrī, who comes preceded by horses, seated in a chariot and awakened by the trumpeting of elephants. May she favour me and stay.",
   salut=["Horses ahead of her: speed, enthusiasm, effort.", "The chariot: a structured path and direction.", "Elephants: strength, stability and wisdom."],
   words=[("अश्वपूर्वां", "Aśva-pūrvāṁ", "Preceded by horses"), ("रथमध्यां", "Ratha-madhyāṁ", "Seated in the chariot"), ("हस्तिनादप्रबोधिनीम्", "Hastināda-prabodhinīm", "Awakened by elephant trumpets"), ("उपह्वये", "Upahvaye", "I invoke, I call upon")],
   take=["Bring energy to your work.", "Walk a path with direction.", "Build on steady, wise foundations.", "Ask for prosperity that stays."]),
  sketchalt=_alt(3, "three images of her arrival: horses (energy), the chariot (direction) and elephants (stability and wisdom)")),

4: dict(
  icons=["shield", "drop", "flame", "lotus"],
  keypoints=[("Prākāra", "Protected: walls of gold, stable and enduring"),
             ("Ārdrā", "Tender: compassion that nourishes others"),
             ("Tṛptā", "Content: radiant, yet fully satisfied"),
             ("Padma", "Lotus: pure, untouched by the mud")],
  tagline="Walled in gold yet tender, radiant yet content: prosperity that is protected, shared and pure.",
  forms_title="Explore the four qualities",
  formnotes=[
   ("Hiraṇya-prākārā: she is surrounded by walls of gold. Read as a symbol, prosperity is meant to be well protected, stable and enduring.", "Is what I am building resting on strong, honest foundations?"),
   ("Ārdrā means tender, moist with compassion, and tarpayantī means she who satisfies others. The commentary reads this as abundance that flows outward, since selfish prosperity tends to dry up.", "How am I using what I have to support someone else?"),
   ("Jvalantī (radiant like fire) and tṛptā (fully satisfied) sit side by side. She glows, yet she is not restless: the picture is calm fulfilment rather than endless chasing.", "Where could I pause and feel that I have enough?"),
   ("Padme sthitā, padma-varṇā: seated on a lotus, lotus-coloured. The lotus grows in mud and stays untouched, a symbol of prosperity that remains pure and free of ego.", "What helps me stay clean and humble when things go well?")],
  sheet=dict(
   salut_title="Four Qualities", centre_title="Radiant and Content", centre="Calm Fulfilment",
   essence="She is walled in gold, tender, radiant and content, seated on a lotus: prosperity that is secure, shared and pure.",
   short="I call here and now upon that Śrī: surrounded by walls of gold, tender, radiant, fully satisfied and satisfying others, seated on a lotus and lotus-hued.",
   salut=["Golden walls: well protected and enduring.", "Tender and compassionate; she nourishes others.", "Radiant like fire, yet fully satisfied.", "On a lotus: pure, untouched by the mud."],
   words=[("हिरण्यप्राकाराम्", "Hiraṇya-prākārām", "Surrounded by walls of gold"), ("आर्द्राम्", "Ārdrām", "Tender, compassionate"), ("तृप्ताम्", "Tṛptāṁ", "Fully satisfied"), ("पद्मवर्णाम्", "Padma-varṇāṁ", "Lotus-coloured")],
   take=["Build on strong, honest foundations.", "Let what you have nourish others.", "Practise contentment while you strive.", "Stay pure and humble, like the lotus."]),
  sketchalt=_alt(4, "four qualities: golden walls (protected), Ārdrā (tender and nourishing), Tṛptā (radiant yet content) and the lotus (pure and untouched)")),

5: dict(
  icons=["hands", "shield", "cloud", "key"],
  keypoints=[("Udārā", "Generous: glory that lifts others too"),
             ("Śaraṇam", "Refuge: do your part, then surrender the result"),
             ("Alakṣmī", "Let go: misfortune and the habits that feed it"),
             ("Tvāṁ vṛṇe", "Choose: I choose you, a conscious daily choice")],
  tagline="After praising her glory and generosity, the verse turns personal: I take refuge, let go and choose.",
  forms_title="Explore the four steps",
  formnotes=[
   ("Udārā means generous and magnanimous. The commentary reads her glory as the kind that radiates and uplifts others, so generosity is part of prosperity, not a subtraction from it.", "Where could I be more open-handed this week?"),
   ("Śaraṇam ahaṁ prapadye: I take refuge in her. We do our part, the commentary says, and then surrender the outcome to grace. Effort and surrender are held together.", "What can I do my best on, and then let go of?"),
   ("Alakṣmī is misfortune, the opposite of Śrī. The commentary reads it as scarcity thinking, bad habits, laziness and unethical actions that block abundance, and the prayer is for these to vanish.", "Which one habit would I most like to let go of?"),
   ("Tvāṁ vṛṇe: I choose you. The verse ends in a conscious choice. In the commentary’s reading, prosperity and misfortune are both energies that we can invite or turn away.", "What am I choosing in my thoughts, words and actions today?")],
  sheet=dict(
   salut_title="Four Steps", centre_title="From Praise to Choice", centre="Conscious Choice",
   essence="After praising her moon-like glory and generosity, the verse becomes personal: I take refuge, let misfortune go and choose her.",
   short="I take refuge in that radiant, generous Śrī, adored by the gods and bearing the lotus. May misfortune vanish from me; O Lakshmi, I choose you.",
   salut=["Generous and glorious: she lifts others too.", "Refuge: do your part, then surrender the result.", "Alakṣmī, misfortune: may it vanish.", "I choose you: a conscious, daily choice."],
   words=[("उदाराम्", "Udārām", "Generous, magnanimous"), ("शरणम्", "Śaraṇam", "Refuge, shelter"), ("अलक्ष्मीर्", "Alakṣmīr", "Misfortune, the opposite of Śrī"), ("वृणे", "Vṛṇe", "I choose")],
   take=["Be generous as you grow.", "Do your best, then release the result.", "Let go of one blocking habit.", "Choose well, every day."]),
  sketchalt=_alt(5, "four steps: Udārā (generous), Śaraṇam (refuge and surrender), Alakṣmī (letting go of misfortune) and Tvāṁ vṛṇe (I choose you)")),

6: dict(
  icons=["sun", "flame", "leaf", "cloud"],
  keypoints=[("Āditya-varṇā", "Radiant: bright and life-giving like the sun"),
             ("Tapas", "Effort: discipline is the root of her blessing"),
             ("Bilva", "Fruitful: a sacred tree, slow-growing, divine fruit"),
             ("Antarāya", "Clearing: inner confusion and outer misfortune")],
  tagline="Sun-bright and born of effort: the bilva tree is the picture of slow, sacred fruit that clears obstacles.",
  forms_title="Explore the four images",
  formnotes=[
   ("Āditya-varṇā: she has the colour and brilliance of the sun. The commentary reads prosperity as radiant, life-giving and steady, like the sun.", "Am I giving light to others, or am I clouded today?"),
   ("Tapas is effort and discipline, and the verse says she is born of it. In the commentary, Lakshmi rewards those who strive with discipline and sincerity, not those who hope for shortcuts.", "Where am I relying on shortcuts instead of steady effort?"),
   ("The bilva is a sacred tree, called here the lord of the forest and her own tree. It grows slowly, but its fruit is held to be divine.", "What slow, sincere effort am I planting that will bear fruit later?"),
   ("Māyā and antarāya are inner confusion and self-made blocks; bāhyā alakṣmī is outer misfortune. The prayer is that the fruits of our effort dissolve all three, inside and around us.", "Which inner block could I name honestly today?")],
  sheet=dict(
   salut_title="Four Images", centre_title="Effort Bears Fruit", centre="Earned Fruit",
   essence="Born of effort and bright as the sun, her sacred bilva tree stands for slow, steady fruit that clears obstacles within and without.",
   short="O Goddess bright as the sun, born of tapas: the bilva is your tree. May its fruits, through my effort, drive away illusion, inner obstacles and outer misfortune.",
   salut=["Bright as the sun: radiant, life-giving, steady.", "Tapas: effort and discipline are the root.", "The bilva tree: slow growth, sacred fruit.", "Inner and outer obstacles dissolve."],
   words=[("आदित्यवर्णे", "Āditya-varṇe", "Sun-coloured one"), ("तपसो", "Tapaso", "By effort and discipline"), ("बिल्वः", "Bilvaḥ", "The bilva tree"), ("अलक्ष्मीः", "Alakṣmīḥ", "Misfortune")],
   take=["Choose steady effort over shortcuts.", "Plant slow, sincere work.", "Name the inner block, then clear it.", "Shine for others, like the sun."]),
  sketchalt=_alt(6, "four images: Āditya-varṇā (sun-bright), Tapas (effort), the bilva tree (slow sacred fruit) and the clearing of inner and outer obstacles")),

7: dict(
  icons=["hands", "crown", "home", "sprout"],
  keypoints=[("Deva-sakhaḥ", "Companion: the friend of the gods, in line with dharma"),
             ("Kīrti", "Honour: a good name, with jewel-like brilliance"),
             ("Rāṣṭra", "Society: prosperity that lifts the people around"),
             ("Ṛddhi", "Growth: steady advancement with integrity")],
  tagline="Prosperity is asked for with honour: a companion of the gods, a good name and steady growth in society.",
  forms_title="Explore the four ideas",
  formnotes=[
   ("Deva-sakhaḥ means friend of the gods, here understood as Kubera, the divine treasurer. The commentary reads it as divine companionship: abundance that comes from living in line with dharma, not from selfish accumulation.", "Would I be at ease explaining how I earn to someone I respect?"),
   ("Kīrti is honour and good reputation, and the verse pairs it with maṇi, the brilliance of a jewel. The commentary says prosperity without honour is hollow.", "Will my pursuit of prosperity earn respect in my family and community?"),
   ("Rāṣṭre ’smin: in this society, in this land. The verse places the speaker among others. Prosperity here is not for isolation but for lifting the world around us.", "How is what I have helping my family and community?"),
   ("Ṛddhi is growth and steady advancement. With kīrti it forms the two wings of abundance: a good name and real progress.", "Am I growing in a way that keeps my integrity intact?")],
  sheet=dict(
   salut_title="Four Ideas", centre_title="Prosperity with Honour", centre="Honoured Prosperity",
   essence="She is asked for with honour: divine companionship, a good name, a place in society and steady growth.",
   short="May the friend of the gods approach me, with honour and brilliance. Having arisen in this society, may I be granted good repute and growth.",
   salut=["Companion of the gods: abundance in line with dharma.", "Honour and a good name, with jewel-like brilliance.", "In this society: prosperity that lifts others.", "Steady growth that keeps integrity."],
   words=[("देवसखः", "Deva-sakhaḥ", "Friend of the gods"), ("कीर्तिः", "Kīrtiś", "Honour, good reputation"), ("मणिना", "Maṇinā", "With jewel-like brilliance"), ("ऋद्धिं", "Ṛddhiṁ", "Growth, prosperity")],
   take=["Earn in a way you can speak of openly.", "Guard your good name.", "Let your prosperity lift others.", "Grow without losing your integrity."]),
  sketchalt=_alt(7, "four ideas: Deva-sakhaḥ (friend of the gods), Kīrti (honour), Rāṣṭra (society) and Ṛddhi (growth)")),

8: dict(
  icons=["drop", "cloud", "flame", "home"],
  keypoints=[("Kṣut-pipāsā", "Craving: hunger and thirst of restless wanting"),
             ("Alakṣmī", "Misfortune: scarcity and quarrel, the opposite of Śrī"),
             ("Nāśayāmi", "Resolve: “I destroy”, a firm personal decision"),
             ("Nirṇuda", "Clearing: drive it out of home and life")],
  tagline="A verse of clearing: name craving and scarcity, then decide firmly to sweep them out of home and heart.",
  forms_title="Explore the four steps",
  formnotes=[
   ("Kṣut-pipāsā is hunger and thirst. The commentary reads them as more than physical: greed, dissatisfaction and endless wanting. Where the mind keeps saying “not enough”, prosperity is said not to stay.", "Where does “not enough” keep speaking in my mind?"),
   ("Jyeṣṭhā, the elder sister, and Alakṣmī stand for scarcity, quarrels, dirt and negativity, the opposite of Lakshmi. The commentary says they take root where there is constant complaint, discontent or carelessness.", "What habit of complaint or carelessness could I stop feeding?"),
   ("Nāśayāmy aham means “I destroy”. It is first person and firm, not “I hope”. You are not asking someone else to clean your space; the decision is your own.", "What am I ready to decide today, rather than hope for?"),
   ("Nirṇuda is a command to drive out, and me gṛhāt means from my home. Abhūti and asamṛddhi, lack and stagnation, are included. The commentary reads it as no longer tolerating scarcity thinking, doubt and fear.", "Which corner of my home or mind needs clearing first?")],
  sheet=dict(
   salut_title="Four Steps", centre_title="A Cleared Home", centre="Clear Space",
   essence="A verse of clearing: name craving and scarcity, then decide firmly to sweep lack and stagnation out of the home and the heart.",
   short="I destroy the impurity of hunger and thirst, the misfortune called Jyeṣṭhā and Alakṣmī. Drive out all lack and stagnation from my home.",
   salut=["Hunger and thirst: restless craving, not only food.", "Jyeṣṭhā and Alakṣmī: scarcity, quarrel, negativity.", "“I destroy”: a firm, personal decision.", "Drive it out of my home, completely."],
   words=[("क्षुत्पिपासामलां", "Kṣut-pipāsā-malāṁ", "Impurity of hunger and thirst"), ("ज्येष्ठाम्", "Jyeṣṭhām", "The elder sister of Lakshmi"), ("नाशयाम्यहम्", "Nāśayāmy aham", "I destroy"), ("निर्णुद", "Nirṇuda", "Drive out, banish")],
   take=["Notice where craving takes over.", "Decide, don’t just hope.", "Clear one corner of home or mind today.", "Stop feeding complaint and carelessness."]),
  sketchalt=_alt(8, "four steps of clearing: Kṣut-pipāsā (craving), Alakṣmī (misfortune), Nāśayāmi (I destroy, a firm resolve) and Nirṇuda (drive it out of the home)")),

9: dict(
  icons=["leaf", "shield", "sprout", "crown"],
  keypoints=[("Gandha-dvārā", "Fragrance: a quiet presence, sensed not announced"),
             ("Durādharṣā", "Unshaken: grace that challenges cannot overcome"),
             ("Nitya-puṣṭā", "Nourished: steady, not peaks and valleys"),
             ("Īśvarī", "Sovereign: protector of all beings")],
  tagline="Quiet as fragrance, unshakeable, ever nourished and sovereign: the Goddess as a steady, protective presence.",
  forms_title="Explore the four qualities",
  formnotes=[
   ("Gandha-dvārā: her presence is known by fragrance, as through a door. The commentary notes it is not loud or ostentatious but sensed subtly, like scent in the air.", "What quiet presence am I leaving through my actions and words?"),
   ("Durādharṣā means one who cannot be overcome. The commentary reads it as wealth and grace that challenges cannot shake, rooted in more than outside conditions.", "Does my sense of having enough depend on how things look today?"),
   ("Nitya-puṣṭā is ever nourished and ever flourishing. The commentary says prosperity should not be a game of peaks and valleys, but a steady nurturing of resources, relationships and health.", "What small habit could keep my health and relationships nourished?"),
   ("Īśvarī sarva-bhūtānām: sovereign of all beings. The commentary reads her as protector of everyone, so prosperity that is good for all is the kind said to be blessed and sustained.", "Is what I am pursuing good for others as well as for me?")],
  sheet=dict(
   salut_title="Four Qualities", centre_title="Quiet Strength", centre="Steady Abundance",
   essence="She is sensed like fragrance, cannot be overcome, is ever nourished and rules as protector of all beings.",
   short="Here and now I invoke Śrī: known by fragrance, invincible, ever nourishing and fruitful, the sovereign of all beings.",
   salut=["Fragrance: a quiet presence, sensed not announced.", "Invincible: grace that challenges do not shake.", "Ever nourished: steady, not peaks and valleys.", "Sovereign of all beings and their protector."],
   words=[("गन्धद्वाराम्", "Gandha-dvārām", "Known by fragrance"), ("दुराधर्षाम्", "Durādharṣām", "Invincible"), ("नित्यपुष्टाम्", "Nitya-puṣṭām", "Ever nourishing"), ("ईश्वरीम्", "Īśvarīm", "Sovereign goddess")],
   take=["Be quietly useful, not loud.", "Build steadiness that outlasts bad days.", "Nourish health and relationships daily.", "Seek prosperity that is good for all."]),
  sketchalt=_alt(9, "four qualities: Gandha-dvārā (fragrance), Durādharṣā (unshaken), Nitya-puṣṭā (ever nourished) and Īśvarī (sovereign protector of all beings)")),

10: dict(
  icons=["heart", "sound", "pot", "crown"],
  keypoints=[("Kāmam", "Wishes: pure, noble intentions of the mind"),
             ("Satyam", "Truth: honest speech is the foundation"),
             ("Annam", "Nourishment: cattle and food, for self and others"),
             ("Yaśaḥ", "Honour: prosperity and a good name that stay")],
  tagline="Honest wishes, truthful words, enough to eat and a good name: a grounded, modest prayer.",
  forms_title="Explore the four wishes",
  formnotes=[
   ("Manasaḥ kāmam ākūti: the wishes and intentions of the mind. The verse accepts that we have desires but asks that they be pure and noble, aligned with good rather than ego.", "Which of my wishes are born of care, and which of restlessness?"),
   ("Vācaḥ satyam: truth in speech. The commentary says prosperity stands on truthfulness and integrity, and asks whether we honour our own words.", "Do my words match what I do?"),
   ("Paśūnāṁ rūpam annasya: the beauty or abundance of cattle and of food. Read as nourishment, it hints at prosperity that sustains oneself and others.", "Does what I have feed others as well as me?"),
   ("Mayi śrīḥ śrayatāṁ yaśaḥ: may prosperity and honour rest in me. The prayer is for them to dwell within us, not to visit briefly.", "What would help a good name and steady fortune settle in my life?")],
  sheet=dict(
   salut_title="Four Wishes", centre_title="A Grounded Prayer", centre="Truthful Prosperity",
   essence="A grounded prayer: pure wishes, truthful speech, enough to eat and honour that stays.",
   short="May the wishes and intentions of my mind be fulfilled and my speech be true. May cattle and food be mine, and may prosperity and honour dwell in me.",
   salut=["The mind’s wishes: pure, noble intentions.", "Truth in speech: honesty is the foundation.", "Cattle and food: nourishment for self and others.", "Prosperity and honour that stay within."],
   words=[("मनसः", "Manasaḥ", "Of the mind"), ("सत्यम्", "Satyam", "Truth"), ("अन्नस्य", "Annasya", "Of food, nourishment"), ("यशः", "Yaśaḥ", "Honour, good name")],
   take=["Check your wishes for care, not ego.", "Keep your word.", "Share what nourishes you.", "Let a good name grow slowly."]),
  sketchalt=_alt(10, "four wishes: Kāmam (pure intentions), Satyam (truthful speech), Annam (nourishment) and Yaśaḥ (honour that stays)")),

11: dict(
  icons=["sprout", "home", "heart", "lotus"],
  keypoints=[("Kardama", "Soil: the fertile ground of effort and grace"),
             ("Prajābhūtā", "Continuity: creating for future generations"),
             ("Mayi sambhava", "From within: abundance rising from character"),
             ("Mātā", "Mother: Lakshmi with a lotus garland, ever present")],
  tagline="Prosperity as fertile soil: it rises from within, continues through the family and rests with a motherly Lakshmi.",
  forms_title="Explore the four ideas",
  formnotes=[
   ("Kardama is the sacred, fertile force, read as the nourishing soil of effort, intention and grace. Good things grow only in prepared ground.", "What kind of soil am I preparing with my thoughts and actions?"),
   ("Prajābhūtā: having given rise to progeny and creation. In the commentary, prosperity is not only for oneself; it creates, multiplies and nourishes future generations.", "What am I building that others will still benefit from?"),
   ("Mayi sambhava: arise within me. The commentary reads abundance as coming not only from outside but from character, conduct, intention and effort.", "Which quality in myself would most help abundance take root?"),
   ("Mātaraṁ padma-mālinīm: the mother, wearing a garland of lotuses. She is soft, nurturing and permanently present, and the verse asks her to dwell in family and lineage.", "How can I make my home a place where care can settle?")],
  sheet=dict(
   salut_title="Four Ideas", centre_title="Roots and Lineage", centre="Motherly Abundance",
   essence="Prosperity as fertile soil: it rises from within, continues through the family and rests with Lakshmi as a lotus-garlanded mother.",
   short="By Kardama, the fertile force, may abundance arise in me. May Lakshmi, the mother who wears lotus garlands, dwell in my family and lineage.",
   salut=["Kardama: the fertile, nourishing ground.", "Creation and continuity across generations.", "Abundance rising from character and effort.", "The mother with lotus garlands, always present."],
   words=[("कर्दमेन", "Kardamena", "By Kardama, the fertile force"), ("प्रजाभूता", "Prajābhūtā", "Giving rise to creation"), ("सम्भव", "Sambhava", "Arise, come into being"), ("मातरं", "Mātaraṁ", "Mother")],
   take=["Prepare good soil: habits and intentions.", "Build what will outlast you.", "Grow from within first.", "Make home a place of care."]),
  sketchalt=_alt(11, "four ideas: Kardama (fertile soil), Prajābhūtā (continuity), Mayi sambhava (abundance from within) and Mātā (the motherly Lakshmi with a lotus garland)")),

12: dict(
  icons=["drop", "heart", "key", "home"],
  keypoints=[("Āpaḥ", "Water: flow, purity and cleansing"),
             ("Snigdha", "Softness: sweet behaviour, harmony at home"),
             ("Ciklīta", "Staying: what helps prosperity settle"),
             ("Vāsaya", "Settled: a humble, constant presence")],
  tagline="Water, softness and humility: a prosperity that flows gently and settles in the home.",
  forms_title="Explore the four ideas",
  formnotes=[
   ("Āpaḥ are the sacred waters. Water stands for flow, purity and cleansing, and the commentary reads true prosperity as flowing gently, never rigid or forced.", "Where am I forcing something that could flow?"),
   ("Snigdhāni means soft, smooth and full of affection. Wealth without gentleness, the commentary says, turns into arrogance, so the verse asks for sweetness in behaviour and harmony in the home.", "Is my home gentler because of how I act?"),
   ("Ciklīta is an ancient word linked with fertility, fragrance and richness. The commentary reads it as the quality that makes prosperity stay: contentment, humility, gratitude and right conduct.", "Which of these four could I practise a little more?"),
   ("Vāsaya me kule: make her dwell in my family. The prayer is not for loud displays but for a humble, nourishing, constant presence that blesses every corner of life.", "What does a settled, calm home feel like to me?")],
  sheet=dict(
   salut_title="Four Ideas", centre_title="A Settled Home", centre="Gentle Flow",
   essence="The sacred waters bring softness, and the verse asks Lakshmi to dwell, humble and constant, in the family.",
   short="May the sacred waters bring forth softness and richness. Dwell in my home; O Mother Śrī, make the Goddess live in my family.",
   salut=["Sacred waters: flow, purity, cleansing.", "Softness: sweet behaviour, harmony at home.", "Ciklīta: what helps prosperity stay.", "A humble, constant presence in the family."],
   words=[("आपः", "Āpaḥ", "Sacred waters"), ("स्निग्धानि", "Snigdhāni", "Soft, smooth, affectionate"), ("चिक्लीत", "Ciklīta", "Richness, fertility"), ("वासय", "Vāsaya", "Make her dwell")],
   take=["Let things flow, don’t force them.", "Be gentle at home.", "Practise contentment and gratitude.", "Welcome a calm, constant presence."]),
  sketchalt=_alt(12, "four ideas: Āpaḥ (sacred waters), Snigdha (softness), Ciklīta (what helps prosperity stay) and Vāsaya (a settled, humble presence in the family)")),

13: dict(
  icons=["heart", "wave", "sprout", "sun"],
  keypoints=[("Ārdrā", "Tender: wealth with empathy and care"),
             ("Puṣkariṇī", "Lotus lake: purity, serenity and peace"),
             ("Puṣṭi", "Nourishment: body, mind and soul"),
             ("Piṅgalā", "Golden: a warm, bright, inviting glow")],
  tagline="Tender, lotus-lake calm, nourishing and golden: four soft qualities invited through Agni.",
  forms_title="Explore the four qualities",
  formnotes=[
   ("Ārdrā: moist, tender and compassionate. The commentary says prosperity is beautiful only when it is caring and full of empathy.", "Where could more empathy change a decision I am facing?"),
   ("Puṣkariṇī: she who dwells in a lake of lotuses. The picture is purity, serenity and peace, a still lake filled with flowers.", "Where in my day can I find stillness like a quiet lake?"),
   ("Puṣṭi is fullness and nourishment. The commentary says that without nourishment of body, mind and soul, wealth is hollow.", "Which of body, mind or soul is least nourished right now?"),
   ("Piṅgalā is golden-hued and hiraṇmayī is filled with a golden glow. Prosperity, the commentary says, should make life warm, bright and inviting, like gold or the soft light of the moon.", "Does my home or work feel warm and inviting to others?")],
  sheet=dict(
   salut_title="Four Qualities", centre_title="Warm and Nourishing", centre="Golden Tenderness",
   essence="Four soft qualities, tender, lotus-calm, nourishing and golden, are asked for through Agni, the messenger.",
   short="O Jātaveda, bring to me Lakshmi: tender, dwelling among lotuses, full of nourishment, golden-hued, wearing lotus garlands, moon-bright and golden in form.",
   salut=["Tender and compassionate: wealth with empathy.", "A lotus lake: purity, serenity and peace.", "Nourishment of body, mind and soul.", "Golden and warm: a bright, inviting glow."],
   words=[("आर्द्राम्", "Ārdrām", "Tender, compassionate"), ("पुष्करिणीं", "Puṣkariṇīṁ", "Dweller among lotuses"), ("पुष्टिं", "Puṣṭiṁ", "Nourishment, fullness"), ("पिङ्गलाम्", "Piṅgalām", "Golden-hued")],
   take=["Let empathy shape your decisions.", "Make room for stillness.", "Nourish body, mind and soul.", "Be warm and inviting to others."]),
  sketchalt=_alt(13, "four qualities: Ārdrā (tender), Puṣkariṇī (lotus lake), Puṣṭi (nourishment) and Piṅgalā (golden glow)")),

14: dict(
  icons=["heart", "flag", "gem", "sun"],
  keypoints=[("Ārdrā", "Tender: wealth with kindness and love"),
             ("Kariṇī", "Action: the power that brings work to fulfilment"),
             ("Suvarṇā", "Golden: the beauty of life, a touch of the divine"),
             ("Sūryā", "Sun-bright: an inner light that lights others")],
  tagline="Tenderness and action, gold and sunlight: wealth that is kind, hard-working and bright from within.",
  forms_title="Explore the four qualities",
  formnotes=[
   ("Ārdrā is tender and compassionate. The commentary says wealth is not only hard power: it should carry gentleness, kindness and love, and then it lasts.", "Is there room for kindness in how I handle money and work?"),
   ("Kariṇī is the power that brings work to completion, joined with yaṣṭi, resolve and discipline. The commentary says Lakshmi dwells where there is steady effort and practice, not laziness.", "What one task would steady effort finish this week?"),
   ("Suvarṇā and hema-mālinī: golden, and wearing a garland of gold. Prosperity, the commentary says, is not only material: it is the beauty of life and a touch of the divine.", "What makes my life beautiful besides what I own?"),
   ("Sūryā is sun-bright and life-giving, and hiraṇmayī is filled with golden light. The picture is an inner light that shines by itself and lights up others too.", "Who feels brighter after time with me?")],
  sheet=dict(
   salut_title="Four Qualities", centre_title="Kind and Bright", centre="Radiant Action",
   essence="Tender and hard-working, golden and sun-bright: wealth that is kind, active and radiant from within.",
   short="O Agni, bring to me Lakshmi: tender, the power that fulfils every work, golden, garlanded with gold, sun-bright and filled with golden light.",
   salut=["Tender: wealth with kindness and love.", "Action and resolve: steady, disciplined effort.", "Golden and garlanded: the beauty of life.", "Sun-bright: an inner light that lights others."],
   words=[("आर्द्राम्", "Ārdrām", "Tender, compassionate"), ("करिणीं", "Kariṇīṁ", "Power to complete work"), ("सुवर्णाम्", "Suvarṇām", "Golden, pure and bright"), ("सूर्याम्", "Sūryām", "Sun-bright, life-giving")],
   take=["Keep kindness inside your work.", "Finish what you begin.", "Notice beauty beyond possessions.", "Be a source of light for others."]),
  sketchalt=_alt(14, "four qualities: Ārdrā (tender), Kariṇī (action and resolve), Suvarṇā (golden beauty) and Sūryā (sun-bright inner light)")),

15: dict(
  icons=["home", "gem", "pot", "hands"],
  keypoints=[("Anapagāminī", "Lasting: she who never goes away"),
             ("Hiraṇya", "Brightness: gold, also knowledge and judgement"),
             ("Gāvaḥ, Aśvān", "Support: nourishment, helpers and strength"),
             ("Puruṣān", "Company: excellent, uplifting people")],
  tagline="The closing verse returns to the opening request: a Lakshmi who stays, with brightness, support and good company.",
  forms_title="Explore the four ideas",
  formnotes=[
   ("Anapagāminī means one who does not go away. The commentary calls this a very important word: the verse asks for lasting prosperity and inner peace, not temporary pleasure.", "What do I hope will still be with me in ten years?"),
   ("Hiraṇyaṁ prabhūtam: gold in abundance. The commentary adds that this gold is also a symbol of knowledge, brightness and good judgement.", "Which kind of brightness, wisdom or judgement, do I most want to grow?"),
   ("Gāvaḥ, dāsyaḥ, aśvān: cows, attendants and horses. Read as nourishment, support and the means of progress, they say that prosperity lasts only with cooperation and sustenance.", "Who supports me, and have I thanked them lately?"),
   ("Puruṣān aham: excellent people. The commentary says Lakshmi stays where company is positive and uplifting, so the closing line asks for good people around us.", "Does my company lift me up, and do I lift theirs?")],
  sheet=dict(
   salut_title="Four Ideas", centre_title="The Closing Invocation", centre="Lasting Prosperity",
   essence="The hymn returns to its first request: a Lakshmi who stays, with brightness, nourishment, support and good company.",
   short="O Jātaveda, bring to me Lakshmi who never leaves, in whose presence may I obtain gold in abundance, cows, helpers, horses and excellent people.",
   salut=["She who never leaves: lasting prosperity and peace.", "Gold in abundance, also knowledge and judgement.", "Nourishment, helpers and horses: support and progress.", "Excellent people: positive, uplifting company."],
   words=[("अनपगामिनीम्", "Anapagāminīm", "One who never goes away"), ("प्रभूतं", "Prabhūtam", "In abundance"), ("गावो", "Gāvo", "Cows, nourishment"), ("पुरुषान्", "Puruṣān", "Excellent people")],
   take=["Ask for what lasts.", "Value knowledge and good judgement.", "Thank those who support you.", "Keep company that lifts you."]),
  sketchalt=_alt(15, "four ideas: Anapagāminī (she who never leaves), Hiraṇya (gold and brightness), Gāvaḥ and Aśvān (nourishment, helpers and strength) and Puruṣān (good company)")),

16: dict(
  icons=["drop", "shield", "flame", "sound"],
  keypoints=[("Śuciḥ", "Pure: a clean mind and clean conduct"),
             ("Prayataḥ", "Restraint: self-control and discipline"),
             ("Juhuyāt", "Offering: ghee into the fire, every day"),
             ("Japet", "Recitation: the fifteen verses, steadily")],
  tagline="The closing verse is about practice: purity, restraint, daily offering and steady recitation, as the tradition describes it.",
  forms_title="Explore the four practices",
  formnotes=[
   ("Śuci means pure. The verse begins with the person, not the request: a clean mind and clean conduct come first, according to the closing verse.", "What small thing would make my mind feel cleaner today?"),
   ("Prayata is self-restrained. The commentary says discipline, self-restraint and pure conduct are what make Lakshmi’s grace lasting, more than asking alone.", "Where would a little restraint serve me better than more effort?"),
   ("Juhuyāt ājyam anvaham: offer ghee into the sacred fire every day. The commentary reads it as a daily practice that includes offering one’s own duty and work with true faith.", "What is my daily offering, in work or in care for others?"),
   ("Japet means one should recite, and satataṁ means continuously. The fifteen verses are to be recited steadily, so the emphasis is on regularity.", "What rhythm of practice could I keep up for a month?")],
  sheet=dict(
   salut_title="Four Practices", centre_title="The Fruit of Practice", centre="Daily Practice",
   essence="The closing verse is about practice: purity, restraint, a daily offering and steady recitation of the fifteen verses.",
   short="One who becomes pure and self-restrained, offers ghee into the fire daily and steadily recites the fifteen verses of Śrī, desiring Śrī.",
   salut=["Śuci: a pure, clean mind.", "Prayata: self-restraint and discipline.", "A daily offering of ghee, and of one’s work.", "Steady recitation of the fifteen verses."],
   words=[("शुचिः", "Śuciḥ", "Pure"), ("प्रयतः", "Prayataḥ", "Self-restrained"), ("आज्यम्", "Ājyam", "Ghee, clarified butter"), ("जपेत्", "Japet", "One should recite")],
   take=["Begin with a clean mind.", "Practise restraint.", "Keep a small daily offering.", "Recite steadily, with faith."]),
  sketchalt=_alt(16, "four practices: Śuci (purity), Prayata (restraint), Juhuyāt (the daily offering) and Japet (steady recitation of the fifteen verses)")),
}
