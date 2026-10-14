# REVIEW — things for Eid to check

This file is partly written by hand and partly filled in by `python3 build.py`
(the parts between the `AUTO` markers are regenerated on every full build).

## (b) Questions for Eid

1. **Sections 14 and 15 were missing from the brief.** The brief refers to "section 14" (Learn
   Smarter) and "section 15" (Resources), but the text ends at section 13. I wrote my own:
   8 Learn Smarter tips (word cards, little and often, mistakes, chunks, Arabic traps, talking to
   yourself, easy reading, test week) and 8 resources (British Council LearnEnglish, BBC Learning
   English, Cambridge Dictionary, Oxford Learner's Dictionaries, Duolingo, Quizlet, Anki, ESL Video).
   They are in `content/common.py`. Please replace or approve them.
2. **Unit tests and the Level Review reuse practice items.** Each 25-item unit test is a seeded mix
   of items from that unit's grammar sets (+ word items); the ~60-item Level Review is a mix from all
   units. Would you like brand-new items for tests instead?
3. **Numbers in the book lists.** "Numbers 0–20" became 21 word cards; "Numbers 21–100 and How
   old…?" became twenty-one, the tens and a hundred; Starter U9 ordinals are one card each. OK?
4. **Family links between the cast are my invention** (for continuity inside a unit): e.g. Rana is
   married to Kareem with children Joud and Mais, Abu Firas and Hind are Rana's parents (A1.1 U5);
   Walid and Sana are Layla and Ziad's parents (A1.1 U5, A2.1 U2/U7). The trees are not identical
   across apps. Do you want one fixed family for the whole series?
5. **Classroom-English situations** (the short line under each phrase, e.g. "The teacher speaks
   very fast for you.") are mine. Like word definitions, I treated them as exempt from the level
   gate. OK?
6. **Arabic outside grammar cards:** one Learn Smarter tip ("Arabic can help — and trick you")
   contains two short Arabic examples. Keep it? And would you like short Arabic support on the
   Learn Smarter tips for A1 learners (they are in simple English now)?
7. **Elementary order:** in A2.1 Units 1–2 I avoided every *do/does* form (except fixed classroom
   chunks) but used present-simple statements like "She plays the oud", because Starter already
   teaches them. OK?
8. **"have got"** is not used in the Starter apps at all (Starter teaches *have*), and the present
   continuous is never used in Starter except *going to* in Unit 12. Correct?
9. **Games per unit:** A1 units offer Memory Match, Speed Round or Sentence Builder Race, Falling
   Words or Odd One Out, Balloon Spelling and Escape the Souq; A2 units offer Memory Match, Speed
   Round, Falling Words or Odd One Out, Sentence Builder Race and Escape the Souq. Any preferences?
10. **Real facts to check:** Nizar Qabbani's life (A1.2 U10 reading), Fairuz, Messi, Mozart, Harrods,
    the Bosra Roman theatre, camel and other animal numbers (A2.2 U11), distances (Damascus–Latakia
    ≈ 330 km). The Bosra festival (A2.2 U12) and the band "Jasmine" (A2.2 U8) are written as fiction.
11. **Cultural mix.** Counting place names, the apps are about: A1.1 46% Damascus / 19% Syria / 35%
    world; A1.2 34 / 31 / 35; A2.1 54 / 15 / 31; A2.2 47 / 29 / 24 (exact figures are in the gate
    report). International settings are below your 40% target in the A2 apps. Do you want me to add
    more international settings there?
12. **Zero article in typed gaps:** for "Write a, an or x (= nothing)" the learner types **x**
    (or "nothing") for no article. Is that clear enough for your students?

## (d) Things I wasn't sure about

* **Level gate limits.** The gate is a set of regex/keyword rules (`buildlib/levelgate.py`) plus my
  own reading. Exempt from it: classroom-English chunks and their situations, the book words of the
  unit and earlier units, word definitions, and the *wrong* side of Watch-out boxes (they show the
  typical Arabic-speaker mistake on purpose, e.g. "I have 20 years" in A1.1 U2). One- or two-word
  options (e.g. "are", "got") are checked without the rules that need the sentence around them.
* **Answer-position rule with small sets.** "No slot holds more than 50%" cannot pass for an odd
  number of 2-option items, so those sets are kept even. 3-item Quick checks use "not all keys in
  one slot" instead of 50%.
* **Distractors** were proofread by me, one by one. The adverb-position sets ("Choose the right
  sentence") use deliberately broken word orders as distractors.
* **"Sentence Builder" / word-order items** accept only the orders I listed; other correct orders
  may exist for a few longer sentences.
* **Team mode** in quiz games shows the right answer when someone taps an option; points are given
  only by the teacher bar (✅ Team A / ✅ Team B / ❌).
* **Progress keys:** item IDs are short hashes of the item text, so editing an item's text resets
  the saved progress for that one item only. Storage keys: `eid-practice-a11-v1`, `-a12-`, `-a21-`,
  `-a22-v1`.
* **Resources links** open outside the app and need the internet; I did not test them live.
* **Reading lengths** rise from 53 words (A1.1 U1) to about 200 (A2.2 U14).
* **Playwright** used the Chromium that is pre-installed in the build environment.
* To balance places, some sentences use international cities in place of Syrian ones (e.g. "We
  lived in Cairo in 2005"); these are invented examples, not facts about the cast.

## (c) Gate results (last full build)

<!-- AUTO:gates -->
```
Font: Nunito downloaded from Google Fonts at build time
warn a12u11: balloon has too little data; offered builder instead

A1.1 Practice: 6 units, 1918 scored items (U1 381, U2 324, U3 305, U4 320, U5 312, U6 276), 58 level-review items, 52 Arabic lines, 0.83 MB; reading words {1: 53, 2: 61, 3: 77, 4: 87, 5: 91, 6: 98}; places mix Damascus 46% / Syria 19% / world 34% ({'damascus': 254, 'syria': 107, 'world': 189})
A1.2 Practice: 6 units, 1707 scored items (U7 325, U8 316, U9 338, U10 240, U11 224, U12 264), 60 level-review items, 47 Arabic lines, 0.79 MB; reading words {7: 110, 8: 115, 9: 107, 10: 107, 11: 110, 12: 118}; places mix Damascus 34% / Syria 30% / world 35% ({'damascus': 60, 'syria': 53, 'world': 62})
A2.1 Practice: 7 units, 2073 scored items (U1 302, U2 294, U3 298, U4 288, U5 254, U6 300, U7 337), 56 level-review items, 67 Arabic lines, 0.88 MB; reading words {1: 107, 2: 116, 3: 124, 4: 124, 5: 123, 6: 126, 7: 128}; places mix Damascus 53% / Syria 15% / world 32% ({'damascus': 129, 'syria': 36, 'world': 77})
A2.2 Practice: 7 units, 2147 scored items (U8 310, U9 322, U10 319, U11 291, U12 340, U13 275, U14 290), 56 level-review items, 76 Arabic lines, 0.94 MB; reading words {8: 147, 9: 158, 10: 141, 11: 157, 12: 152, 13: 138, 14: 208}; places mix Damascus 46% / Syria 29% / world 25% ({'damascus': 119, 'syria': 74, 'world': 65})
ok  [browser] A1.1 Practice.html: 184 views at 390×844 (247 sets opened in the player), 174 views at 360×740, 108 views at 1920×1080 class mode (zoom 1.75); parity 13; scoring on 25 sets + unit test; B1 "Are you a student?"; B3 pile; B4 single count; B7 24 Falling Words frames; B8/B9 Escape finished; Arabic toggle; reload kept 25 set scores; v1 progress: 50 items, 4 sets, 2 words kept; storage-blocked run clean
ok  [browser] A1.2 Practice.html: 182 views at 390×844 (227 sets opened in the player), 170 views at 360×740, 108 views at 1920×1080 class mode (zoom 1.75); parity 13; scoring on 25 sets + unit test; B1 "I always go to bed at eleven."; B3 pile; B4 single count; B7 20 Falling Words frames; B8/B9 Escape finished; Arabic toggle; reload kept 25 set scores; v1 progress: 50 items, 4 sets, 2 words kept; storage-blocked run clean
ok  [browser] A2.1 Practice.html: 215 views at 390×844 (280 sets opened in the player), 205 views at 360×740, 126 views at 1920×1080 class mode (zoom 1.75); parity 13; scoring on 23 sets + unit test; B1 "I am a police officer."; B3 pile; B4 single count; B7 32 Falling Words frames; B8/B9 Escape finished; Arabic toggle; reload kept 23 set scores; v1 progress: 49 items, 4 sets, 2 words kept; storage-blocked run clean
ok  [browser] A2.2 Practice.html: 219 views at 390×844 (290 sets opened in the player), 209 views at 360×740, 126 views at 1920×1080 class mode (zoom 1.75); parity 13; scoring on 24 sets + unit test; B1 "I didn't go to the party."; B3 pile; B4 single count; B7 22 Falling Words frames; B8/B9 Escape finished; Arabic toggle; reload kept 24 set scores; v1 progress: 48 items, 4 sets, 2 words kept; storage-blocked run clean
browser smoke test: passed

RESULT: ALL GATES PASSED
```
<!-- /AUTO:gates -->

## (a) Every Arabic line, by app and unit

Each line is shown with the grammar card it belongs to. Please correct anything that
doesn't sound like a friendly Damascus teacher; edit it in `content/<level>/uNN.py`
(the `ar=[...]` list of that grammar card) and rebuild.

<!-- AUTO:arabic -->
English is shown first; the Arabic opens with the عربي pill or the global "Arabic help" switch.


### A1.1 Practice


**Unit 1**

| Grammar card | In simple words | عربي |
|---|---|---|
| I'm / you're · my / your | Say the verb: I'm Layla. (not: I Layla.)<br>I → am. You → are.<br>my = mine. your = yours. | بالإنكليزي ما فينا نحذف الفعل: لازم نقول I am، مو بس I.<br>منستعمل am مع I بس، و are مع you.<br>my يعني تبعي، و your يعني تبعك: my name = اسمي.<br>بالسؤال منقدّم الفعل: Are you…? |
| a / an with jobs | Before a job, say {a} or {an}: I'm {a} teacher.<br>First sound a, e, i, o, u → {an}: {an} actor.<br>Other jobs → {a}: {a} student, {a} shop assistant. | قبل الوظيفة لازم نحط a أو an: I'm a teacher، مو I'm teacher.<br>منحط an قبل الكلمة اللي بتبلش بصوت a, e, i, o, u: an actor, an engineer.<br>وباقي الكلمات بتاخد a: a student, a shop assistant. |
| The alphabet · How do you spell …? | Ask: How do you spell your name?<br>Say the letters one by one: K-A-R-E-E-M.<br>Careful: E = 'see', I = 'my', A = 'say'.<br>Two letters the same? Say double: double L. | لما بدك تسأل كيف بتنكتب الكلمة منقول: How do you spell …?<br>منلفظ الأحرف حرف حرف: K-A-R-E-E-M.<br>انتبه: E متل 'إي'، و I متل 'آي'، و A متل 'إيه'.<br>إذا في حرفين متل بعض منقول double: double L. |

**Unit 2**

| Grammar card | In simple words | عربي |
|---|---|---|
| be: he / she / it | He, she, it → {is}: He's Syrian. She's a teacher.<br>Say the verb: She's a teacher. (not: She teacher.)<br>Negative: {isn't}. Question: {Is} she Syrian?<br>Age: I'm 20, she's 30. Use be, not have. | مع he و she و it منستعمل is: He is، She is، It is.<br>بالعربي منقول 'هي أستاذة' بلا فعل، بس بالإنكليزي لازم: She's a teacher.<br>للنفي منحط not: He isn't Italian. وللسؤال منقدّم is: Is she Syrian?<br>والعمر بالإنكليزي مع be: I'm 20، مو I have 20 years. |
| his / her / their / our | A man → {his}: Hadi → {his} phone.<br>A woman → {her}: Layla → {her} car.<br>Rana + Kareem → {their}. Me + my family → {our}.<br>Say {his} car, {her} phone. Not: car his. | بالعربي منقول 'سيارته' و'سيارتها'، بس بالإنكليزي منحط كلمة قبل الاسم: his car، her car.<br>his للرجّال و her للمرا، حتى لو الشي نفسه مذكّر أو مؤنث بالعربي.<br>their يعني تبعهن، و our يعني تبعنا: our teacher = أستاذنا. |

**Unit 3**

| Grammar card | In simple words | عربي |
|---|---|---|
| this / that / these / those | Near → {this} (one), {these} (more than one).<br>Far → {that} (one), {those} (more than one).<br>{this} / {that} + is. {these} / {those} + are.<br>What's this? → It's… What are these? → They're… | this و these للشي القريب (هاد، هدول)، و that و those للشي البعيد (هداك، هدوليك).<br>this و that لشي واحد مع is، و these و those لأكتر من شي مع are.<br>بالسؤال: What's this? → It's… و What are these? → They're… |
| be: we / they | We, you, they → {are}: We're from Damascus.<br>{we} = me + other people. {they} = other people.<br>{you} = one person or more than one.<br>Negative: {aren't}. Question: {Are} they Syrian? | مع we و they منستعمل are: We are، They are.<br>we يعني نحنا، و they يعني هنّن. You كمان بتنفع لأكتر من شخص.<br>للنفي: aren't، وللسؤال منقدّم are: Are they Syrian? |

**Unit 4**

| Grammar card | In simple words | عربي |
|---|---|---|
| Prepositions of place | These words say where: {in}, {on}, {under}, {near}.<br>{in} the bag, {on} the table, {under} the chair.<br>{opposite} = on the other side of the street.<br>Say {next to} (not: next) and {in front of}. | هي كلمات بتقول وين الشي: in (جوّا)، on (فوق ع)، under (تحت).<br>next to (جنب)، near (قريب من)، behind (ورا)، in front of (قدّام).<br>between (بين شيئين)، opposite (مقابل، بالجهة التانية من الشارع).<br>انتبه: منقول next to مو next the، و in front of بثلاث كلمات. |
| there is / there are | One thing → {There's}: There's a bank in my street.<br>More than one → {There are}: There are two shops.<br>Negative: {There isn't} / {There aren't}.<br>Question: {Is there}…? / {Are there}…? | There is (There's) يعني 'في' لشي واحد، و There are يعني 'في' لأكتر من شي.<br>للنفي: There isn't / There aren't. وللسؤال منقدّم is و are: Is there…? Are there…?<br>انتبه: بالعربي 'في محلّين' بس بالإنكليزي There are two shops، مو There is two shops. |
| a / an, some, any, a lot of | One → {a} / {an}: There's {a} bank.<br>{some} = not many. {a lot of} = very many.<br>Negative and question → {any}: Are there {any} hotels?<br>No {a} with more than one: There are {some} shops. | a و an لشي واحد، و some لعدد قليل (شوية)، و a lot of لعدد كبير (كتير).<br>بالنفي وبالسؤال منستعمل any مو some: There aren't any…, Are there any…?<br>ما منحط a قبل الجمع: There are a lot of shops، مو There are a shops. |

**Unit 5**

| Grammar card | In simple words | عربي |
|---|---|---|
| possessive 's | Person first, then {'s}, then the thing: {Rana's} husband.<br>{Abu Firas's} house (not: the house of Abu Firas)<br>Careful: Rana's a teacher. Here {'s} = is.<br>More than one: my {parents'} car (two parents). | بالإنكليزي ما منقول 'زوج رنا' متل العربي، منقول Rana's husband: صاحب الشي أول، بعدين 's.<br>يعني الترتيب معكوس: بيت أبو فراس = Abu Firas's house.<br>انتبه: 's بتجي كمان بمعنى is: Rana's a teacher = Rana is a teacher.<br>إذا الصاحب جمع بـ s منحط بس ': my parents' car. |
| Present simple: I / you / we / they | For every day, again and again: I {live} in Damascus.<br>I, you, we, they + verb: I {work}, they {work}.<br>Negative: {don't} + verb: I {don't live} alone.<br>No am or are: I go. (not: I am go.) | المضارع البسيط منستعملو للأشياء اللي دايماً صحيحة أو للعادات: I live in Damascus.<br>مع I و you و we و they الفعل بيضل متل ما هو: I work, we work, they work.<br>للنفي منحط don't قبل الفعل: I don't live alone.<br>انتبه: ما منحط am مع الفعل: I go، مو I am go. |
| Questions: Do you…? / Do they…? | Question: {Do} first: {Do} you live in a flat?<br>Short answer: Yes, I {do}. / No, I {don't}.<br>Not: Are you live…? Say: {Do} you live…? | لنسأل بالمضارع البسيط منحط Do بالأول: Do you live…?<br>الجواب القصير: Yes, I do. أو No, I don't. ما منكرر الفعل.<br>انتبه: ما منقول Are you live…? منقول Do you live…? |

**Unit 6**

| Grammar card | In simple words | عربي |
|---|---|---|
| Present simple: he / she / it | He, she, it → verb + {s}: he {works}, she {lives}.<br>Some verbs + {es}: {goes}, {watches}. study → {studies}, have → {has}.<br>Negative: {doesn't} + verb, no s: She {doesn't work}.<br>Careful: He go ✗ → He {goes} ✓. | مع he و she و it منزيد s ع الفعل: he works, she lives.<br>بعض الأفعال بتاخد es: goes, watches. و study بتصير studies، و have بتصير has.<br>للنفي: doesn't + الفعل بلا s: She doesn't work، مو She doesn't works.<br>انتبه: أكتر غلطة عنا 'He go' — صحّها: He goes. |
| Questions: Does he / she…? | He, she, it → {Does} first: {Does} she like jazz?<br>After Does, no s: Does she {like}? (not: likes)<br>Short answer: Yes, she {does}. / No, he {doesn't}. | لنسأل عن he و she و it منحط Does بالأول، والفعل بيرجع بلا s: Does she like…?<br>الجواب القصير: Yes, she does. / No, he doesn't.<br>انتبه: Does she likes? غلط — الـ s بتروح لـ does. |

### A1.2 Practice


**Unit 7**

| Grammar card | In simple words | عربي |
|---|---|---|
| How often? Frequency adverbs | How often? {always} 100% → {usually} → {often} → {sometimes} → {hardly ever} → {never} 0%.<br>Put the word before the verb: I {always} get up early.<br>After am / is / are, put it after: He's {never} late.<br>{never} is already negative: I never drink coffee. (not: I don't never…) | هي الكلمات بتقول قدّيش منعمل الشي: always (دايماً) لـ never (أبداً).<br>منحطها قبل الفعل: I always get up early. بس بعد am / is / are: He's never late.<br>never بتكون لحالها نفي، ما منحط معها don't: I never drink coffee.<br>لنسأل: How often do you…? (قدّيش بتعمل…؟) |
| Wh- questions: What time do you…? | Question word + do / does + person + verb: Where {does} she work?<br>{does} with he / she / it. {do} with I / you / we / they.<br>After does, the verb has no s: Where does he {work}? (not: works)<br>What do you do? = What's your job? | السؤال بيبلش بكلمة السؤال: What, Where, When, What time، بعدين do أو does.<br>does مع he و she و it، و do مع الباقي، والفعل بيرجع لأصله بلا s.<br>What do you do? يعني شو شغلتك؟ مو شو عم تعمل هلق. |
| Times and at / on / in | {at} + clock time: at five o'clock. Also: at night, at the weekend.<br>{on} + day: on Monday, on weekdays.<br>{in} + part of the day: in the morning, in the evening.<br>Say times like this: 2:15 = two fifteen, 5:30 = five thirty. | at للساعة: at five o'clock، on لليوم: on Monday، in لقسم من النهار: in the morning.<br>بس منقول at night و at the weekend و at midday.<br>الوقت منقولو بالأرقام: 2:15 = two fifteen، 5:30 = five thirty. |

**Unit 8**

| Grammar card | In simple words | عربي |
|---|---|---|
| can / can't | {can} = I am able to. {can't} = I am not able to.<br>can is the same for all people: I can, she {can}. (not: she cans)<br>After can, the verb has no to: I can {swim}. (not: I can to swim) | can يعني بقدر / بعرف، و can't يعني ما بقدر.<br>can ما بتتغيّر: I can, she can — بلا s أبداً.<br>بعد can الفعل بيجي لحالو بلا to: I can swim، مو I can to swim. |
| Questions with can | For a question, put can first: {Can} you swim?<br>Short answers: Yes, I {can}. / No, I {can't}.<br>No do with can: Can you swim? (not: Do you can swim?) | لنسأل بـ can منقدّم can: Can you swim?<br>الجواب القصير: Yes, I can. / No, I can't. ما منكرر الفعل.<br>ما منستعمل do مع can: Do you can…? غلط. |
| Review of questions | With am / is / are, put it first: {Is} he Syrian?<br>With other verbs, use do / does: {Does} he live here?<br>With can, put can first: {Can} he swim? | إذا الجملة فيها am / is / are منقدّمو بالسؤال: Is he Syrian?<br>إذا فيها فعل عادي منحط do أو does: Does he live here?<br>وإذا فيها can منقدّم can: Can he swim? |

**Unit 9**

| Grammar card | In simple words | عربي |
|---|---|---|
| was / were | {was} / {were} = am / is / are in the past.<br>I / he / she / it → {was}. You / we / they → {were}.<br>Negative: {wasn't} / {weren't}. I wasn't at home. | was و were هني ماضي am و is و are: كان / كانوا.<br>was مع I و he و she و it، و were مع you و we و they.<br>للنفي: wasn't / weren't. |
| Questions with was / were | For a question, put was / were first: {Were} you at home?<br>Short answers: Yes, I {was}. / No, I {wasn't}.<br>With question words: {Where were} you? {What was} your job? | لنسأل بالماضي منقدّم was أو were: Were you at home?<br>الجواب: Yes, I was. / No, I wasn't.<br>مع كلمات السؤال: Where were you? What was your job? |
| Dates: the first of January | For dates, say first, second, third…: the {fifth} of May.<br>{on} + date: on the 5th of May. {in} + month or year: in May, in 2012.<br>Say years in two parts: 1984 = nineteen eighty-four, 2012 = twenty twelve. | التاريخ منقولو بالرقم الترتيبي: the first, the second, the third of May.<br>منقول on مع التاريخ: on the 5th of May، و in مع الشهر أو السنة: in May, in 2012.<br>السنين منقسمها: 1984 = nineteen eighty-four، 2012 = twenty twelve. |

**Unit 10**

| Grammar card | In simple words | عربي |
|---|---|---|
| Past simple: regular verbs | Use the past for finished times: yesterday, in 2010, last year.<br>Most verbs + ed: work → {worked}, play → {played}. study → {studied}.<br>The same for all people: I worked, she {worked}. (no s)<br>Negative: {didn't} + verb with no ed: I didn't {work}. | الماضي البسيط للأشياء اللي خلصت بوقت معروف: yesterday, in 2010.<br>الأفعال النظامية منزيدلها ed: worked, played. وstudy بتصير studied.<br>الماضي نفسه مع كل الأشخاص: I worked, she worked — بلا s.<br>للنفي: didn't + الفعل بلا ed: I didn't work، مو I didn't worked. |
| Past simple: irregular verbs | Some verbs have a new past form, with no ed: go → {went}.<br>Learn them one by one: have → {had}, buy → {bought}.<br>Negative: didn't + go, not went: I didn't {go}. | في أفعال ما بتاخد ed، إلها شكل خاص بالماضي: go → went, have → had.<br>هي الأفعال لازم نحفظها، شوف قائمة Irregular Verbs بالصفحة الرئيسية.<br>بالنفي منرجع للفعل الأصلي: I didn't go، مو I didn't went. |

**Unit 11**

| Grammar card | In simple words | عربي |
|---|---|---|
| Past simple: Yes / No questions | Past question: {Did} + person + verb: Did you {go}?<br>After Did, the verb has no ed: Did you go? (not: Did you went?)<br>Short answers: Yes, I {did}. / No, I {didn't}.<br>With was / were, no did: {Were} you tired? (not: Did you tired?) | لنسأل بالماضي منحط Did بالأول، والفعل بيرجع لأصله: Did you go?<br>الجواب: Yes, I did. / No, I didn't.<br>انتبه: مع was / were ما منستعمل did: Were you tired? مو Did you tired? |
| Past simple: Wh- questions | Question word + did + person + verb: Where {did} you go?<br>{ago} comes after the time: two days ago.<br>No 'the' before last: {last} week. (not: the last week) | بالماضي: كلمة السؤال + did + الشخص + الفعل بأصلو: Where did you go?<br>ago بتجي بعد المدة: two days ago = من يومين.<br>last week / last year بلا the: last week، مو the last week. |

**Unit 12**

| Grammar card | In simple words | عربي |
|---|---|---|
| want and want to | {want} + a thing: I want a cat.<br>want + {to} + verb: I want to travel. (not: I want travel)<br>He / she → {wants}: She wants a new jacket.<br>Negative and question: She {doesn't} want to go. {Does} she want a cat? | want يعني بدّي: I want a cat (بدي بسة).<br>إذا بعدها فعل منحط to: I want to travel، مو I want travel.<br>مع he و she: wants. وبالنفي والسؤال منستعمل do / does: She doesn't want to go. |
| going to | {going to} = a plan for the future: I'm going to travel.<br>am / is / are + going to + verb: She's {going to} buy a car.<br>Negative: I'm {not} going to… Question: {Are} you going to…? | going to منستعملها للخطط بالمستقبل: رح + فعل: I'm going to travel = رح سافر.<br>الشكل: am / is / are + going to + الفعل.<br>للنفي: I'm not going to…، وللسؤال: Are you going to…? |

### A2.1 Practice


**Unit 1**

| Grammar card | In simple words | عربي |
|---|---|---|
| be: am / is / are | Every sentence needs a verb: I'm a lawyer. (not: I a lawyer.)<br>I → am. He / she / it → is. You / we / they → are.<br>Negative: I'm not, isn't, aren't. | بالعربي منقول 'أنا محامي' بلا فعل، بس بالإنكليزي لازم am / is / are.<br>am مع I، و is مع he / she / it، و are مع you / we / they.<br>للنفي: I'm not، isn't، aren't. |
| a / an with jobs | Put a or an before a job: She's a doctor.<br>an before an a, e, i, o, u sound: an engineer, an actor.<br>More than one: no a / an. They're doctors. | قبل الوظيفة منحط a أو an: She's a doctor، مو She's doctor.<br>an قبل الصوت a, e, i, o, u: an engineer, an actor.<br>بالجمع ما منحط a: They're doctors. |
| Questions with be | Question: put am / is / are first: Are you married?<br>With question words: Where are you from? What's your job?<br>Short answers: Yes, I am. (not: Yes, I'm.) | بالسؤال منقدّم am / is / are قبل الشخص: Are you married?<br>مع كلمات السؤال: Where are you from? What's your job? How old is she?<br>بالجواب القصير ما منختصر الإيجاب: Yes, I am، مو Yes, I'm. |

**Unit 2**

| Grammar card | In simple words | عربي |
|---|---|---|
| this / that / these / those | this / these = here, near you. that / those = there.<br>One thing → this / that + is.<br>More than one → these / those + are.<br>This is… for people too: This is my cousin, Tala. | this (هاد) و these (هدول) للقريب، that (هداك) و those (هدوليك) للبعيد.<br>this و that لشي واحد مع is، و these و those لأكتر من شي مع are.<br>منستعمل This is… لنعرّف شخص: This is my cousin, Tala. |
| possessive 's | Name + 's = it is his or hers: Maya's camera.<br>More than one, with s at the end: add only ' → my parents' house.<br>Whose…? = which person's? Whose keys are these? — Kareem's. | للملكية منحط 's بعد صاحب الشي: Maya's camera = كاميرا مايا.<br>إذا الصاحب جمع منتهي بـ s منحط بس ': my parents' house.<br>Whose…? يعني لمين؟ Whose keys are these? |
| have got / has got | have got = have: I've got a car.<br>He / she / it → has got: She's got a camera.<br>Negative: haven't got / hasn't got. Question: Have you got…?<br>She's got = She has got. (not: She is got.) | have got يعني 'عندي': I've got a car = عندي سيارة.<br>مع he / she / it منقول has got: She's got a camera.<br>للنفي: haven't got / hasn't got، وللسؤال: Have you got…? Has she got…?<br>انتبه: She's got = She has got، مو She is got. |

**Unit 3**

| Grammar card | In simple words | عربي |
|---|---|---|
| Present simple: I / you / we / they | Use it for things you do every day: I get up at six.<br>Negative: don't + verb. Question: Do you + verb?<br>No am with the verb: I go. (not: I am go.) | المضارع البسيط للعادات والأشياء الثابتة: I get up at six.<br>للنفي don't + الفعل، وللسؤال Do + you + الفعل: Do you work?<br>انتبه: ما منحط am مع الفعل: I go، مو I am go. |
| Telling the time | past = after: twenty past ten = 10:20.<br>to = before: five to nine = 8:55.<br>quarter = 15 minutes. half = 30 minutes: half past one = 1:30. | past يعني 'وْ' (بعد): twenty past ten = عشرة وتلت.<br>to يعني 'إلا': five to nine = تسعة إلا خمسة.<br>quarter = ربع، half = نص: half past one = وحدة ونص. |
| Places in a town | Places in a town: shopping centre, street market, block of flats.<br>There's / There are = what is in your town.<br>village → town → city: small → big. | أسماء الأماكن بالمدينة: shopping centre (مول)، street market (سوق شعبي)، block of flats (بناية).<br>منستعمل There's / There are لنقول شو في بالمدينة.<br>village أصغر من town، و town أصغر من city. |

**Unit 4**

| Grammar card | In simple words | عربي |
|---|---|---|
| Present simple: he / she / it | He / she / it: add s to the verb → she likes, he goes, she studies.<br>Negative: doesn't + verb, no s. Question: Does she + verb?<br>Watch out: He go → He goes. | مع he / she / it الفعل بياخد s: she likes, he goes, she studies.<br>للنفي doesn't + الفعل بلا s، وللسؤال Does + الشخص + الفعل بلا s.<br>انتبه للغلطة المشهورة: He go → He goes. |
| like / love / hate + -ing | After love / like / don't mind / hate: verb + ing → I love dancing.<br>don't mind = it's OK, not good and not bad.<br>Spelling: dance → dancing, swim → swimming, go → going. | بعد love / like / don't mind / hate منحط الفعل مع ing: I love dancing.<br>don't mind يعني ما عندي مشكلة، مو كتير حلو ومو كتير عاطل.<br>تهجئة ing: dance → dancing، swim → swimming، go → going. |
| How often? Frequency | always / usually / often / never go before the verb: I usually walk.<br>But after am / is / are: She's always happy.<br>How often…? → once a week, twice a week, every day. | كلمات التكرار بتجي قبل الفعل العادي: I usually walk.<br>وبعد am / is / are: She's always happy.<br>How often…? منجاوب: once a week (مرة بالأسبوع)، twice a week (مرتين)، every day. |

**Unit 5**

| Grammar card | In simple words | عربي |
|---|---|---|
| can / can't | can = I know how to do it: I can swim.<br>can = it's OK: You can sit here. can't = no: You can't smoke here.<br>After can: the verb, no to, no s → She can drive. | can يعني 'بقدر / بعرف'، وكمان 'مسموح': You can sit here.<br>can't يعني 'ما بقدر' أو 'ممنوع': You can't smoke here.<br>بعد can الفعل بلا to وبلا s: She can drive. |
| a / an, the, no article | a / an = one thing, the first time: I've got a car.<br>the = we know which one: The car is red. the airport, the sun.<br>Nothing for things in general: I love trains. Also: by bus, at home. | a / an لشي واحد لأول مرة منحكي عنو: I've got a car.<br>the لشي معروف أو حكينا عنو قبل: The car is red. وكمان the airport, the sun.<br>ما منحط شي بالعموميات وبـ by bus, at home, go to work: I love trains. |
| Transport and travel | by bus, by car: no a / the. But walking = on foot.<br>get on = go into the bus. get off = leave the bus.<br>At the airport: check-in desk → security → immigration → gate. | منقول by bus، by car بلا a أو the، بس on foot (مشي).<br>get on = نطلع ع الباص، get off = ننزل من الباص.<br>بالمطار: check-in desk ← security ← immigration ← gate. |

**Unit 6**

| Grammar card | In simple words | عربي |
|---|---|---|
| there is / there are | There's = one thing, or things you can't count: There's some milk.<br>There are = more than one: There are two apples.<br>Negative: There isn't / There aren't. Question: Is there…? Are there…? | There's (في) لشي واحد أو شي ما بينعد، و There are لأكتر من شي.<br>للنفي: There isn't / There aren't، وللسؤال: Is there…? Are there…?<br>انتبه: There are two apples، مو There is two apples. |
| some / any · countable and uncountable | Things you can count: an apple → two apples.<br>Things you can't count: rice, water, bread → no a, no s.<br>some: There are some eggs. any: There aren't any eggs. Are there any eggs? | في أشياء منعدّها (apple → apples) وأشياء ما منعدّها (rice, water, bread).<br>اللي ما بينعد ما بياخد a ولا s: some bread، مو a bread أو breads.<br>some بالإيجاب، و any بالنفي والسؤال. |
| How much? How many? | How many + things you can count: How many eggs?<br>How much + things you can't count: How much milk?<br>How much is it? = What's the price?<br>After How many: more than one → How many apples? | How many للأشياء اللي منعدها (eggs, apples)، و How much للي ما منعدها (milk, rice).<br>How much is it? كمان منسأل فيها عن السعر: قدّيش حقها؟<br>بعد How many الاسم جمع: How many apples? مو How many apple? |

**Unit 7**

| Grammar card | In simple words | عربي |
|---|---|---|
| was / were | was / were = am / is / are in the past.<br>I / he / she / it → was. You / we / they → were.<br>Say: I was born in 1995. (not: I born in 1995.) | was و were هني الماضي تبع am / is / are.<br>was مع I / he / she / it، و were مع you / we / they.<br>منقول I was born (انولدت) — مو I born. |
| Past simple: regular verbs | Use the past for finished things: in 2015, last summer.<br>Add ed: work → worked, move → moved, study → studied.<br>The same for everyone: I worked, she worked, they worked. | الماضي البسيط للأشياء اللي صارت وخلصت بوقت معروف: in 2015, last summer.<br>الأفعال النظامية بتاخد ed: worked, moved، و study بتصير studied.<br>نفس الشكل مع كل الأشخاص: I worked, she worked. |
| Past simple: irregular verbs | Some verbs have a special past: go → went, get → got, meet → met.<br>No ed with them: went. (not: goed.)<br>Learn them on the Irregular Verbs page in the app. | في أفعال إلها شكل خاص بالماضي: go → went, get → got, meet → met.<br>ما منزيدلها ed: went، مو goed.<br>احفظها مع الصفحة Irregular Verbs بالتطبيق. |
| Past time phrases | ago comes after the time: two years ago.<br>last with no the: last week, last summer.<br>When I was… = at that time in my life: When I was ten. | ago بتجي بعد المدة: two years ago (من سنتين).<br>last بلا the: last week، last summer.<br>When I was… يعني لما كنت: When I was ten (لما كان عمري عشر سنين). |

### A2.2 Practice


**Unit 8**

| Grammar card | In simple words | عربي |
|---|---|---|
| Past simple: negative | Past negative: {didn't} + verb: I {didn't go}. (not: I didn't went.)<br>{didn't} is the same for I, you, he, she, we and they.<br>With was / were: {wasn't} / {weren't}. (not: I didn't was.) | بالماضي للنفي منحط didn't + الفعل بأصلو: I didn't go، مو I didn't went.<br>didn't نفسها مع كل الأشخاص: I / she / they didn't.<br>بس مع was / were منقول wasn't / weren't بلا didn't. |
| Past simple: questions | Past question: {Did} + person + verb? {Did} you see it?<br>With a question word: What {did} you do? Where {did} you go?<br>With was / were, no did: How {was} the film? | لنسأل بالماضي: Did + الشخص + الفعل بأصلو: Did you see it?<br>مع كلمة السؤال: What did you do? Where did you go?<br>مع was / were ما منستعمل did: How was the film? |
| Stories and entertainment | Types of film: comedy, romance, sci-fi film, action film.<br>{funny} = it makes you laugh. {boring} = not interesting.<br>{audience} = the people who watch. {get good reviews} = people say it's good. | أنواع الأفلام: comedy (كوميدي)، romance (رومانسي)، sci-fi (خيال علمي).<br>صفات: funny (مضحك)، boring (ممل)، frightening (بيخوّف)، fast-moving (أحداثو سريعة).<br>audience يعني الجمهور، و get good reviews يعني ياخد آراء منيحة. |

**Unit 9**

| Grammar card | In simple words | عربي |
|---|---|---|
| Comparatives | Two things: adjective + {-er} + {than}: {cheaper than}.<br>Long adjectives: {more} + adjective: {more expensive than}.<br>big → {bigger}, easy → {easier}, good → {better}, bad → {worse}.<br>Not {more cheaper} — only {cheaper}. | للمقارنة بين شيئين: الصفة + er + than: cheaper than (أرخص من).<br>الصفات الطويلة منحط قبلها more: more expensive than (أغلى من).<br>big → bigger (منضاعف الحرف)، easy → easier، و good → better، bad → worse.<br>انتبه: ما منقول more cheaper — بس cheaper. |
| Superlatives | More than two things: {the} + adjective + {-est}: {the cheapest}.<br>Long adjectives: {the most} + adjective: {the most expensive}.<br>good → {the best}, bad → {the worst}.<br>Don't forget {the}: {the biggest}, not biggest. | لنقول 'الأكتر' من مجموعة: the + الصفة + est: the cheapest (الأرخص).<br>الصفات الطويلة: the most + الصفة: the most expensive (الأغلى).<br>good → the best، و bad → the worst.<br>لا تنسَ the: the biggest، مو biggest لحالها. |
| Describing objects | The adjective comes before the thing: a {stylish} bag. (not: a bag stylish)<br>No -s on adjectives: {expensive} shoes. (not: expensives shoes)<br>{economical} = it doesn't use a lot. {second-hand} = not new. | الصفة بتجي قبل الاسم بالإنكليزي: a stylish bag (شنتاية أنيقة)، مو a bag stylish.<br>الصفة ما بتاخد s بالجمع: expensive shoes، مو expensives shoes.<br>economical يعني ما بيصرف كتير، و second-hand يعني مستعمل. |
| Shops | Many shop names end in {'s}: the {baker's}, the {butcher's}.<br>{optician's} = glasses. {estate agent's} = flats and houses.<br>Use {at}: I buy bread {at} the baker's. | كتير من أسماء المحلات بتنتهي بـ 's: the baker's (الفرن)، the butcher's (اللحام).<br>optician's = محل النظارات، estate agent's = مكتب عقاري، dry-cleaner's = دراي كلين.<br>منقول at the baker's: I buy bread at the baker's. |

**Unit 10**

| Grammar card | In simple words | عربي |
|---|---|---|
| Present continuous | Something happening now: am / is / are + verb + {-ing}.<br>I{'m wearing} a jacket. She{'s trying on} a dress.<br>Negative: {isn't} / {aren't} + -ing. Question: {Are} you listening?<br>Don't forget am / is / are: She{'s} wearing. (not: She wearing.) | المضارع المستمر لشي عم يصير هلق: I'm wearing a jacket (عم ألبس جاكيت).<br>الشكل: am / is / are + الفعل مع ing.<br>للنفي: isn't / aren't + ing، وللسؤال: Are you…ing?<br>انتبه: لا تنسى am / is / are: She's wearing، مو She wearing. |
| Present simple or present continuous? | Always or usually → He usually {wears} a suit.<br>Now or today → am / is / are + -ing: Today he{'s wearing} jeans.<br>{like}, {know}, {want}, {need}: no -ing. I {want}, not I'm wanting. | البسيط للعادة والشي الدايم: I usually wear jeans.<br>المستمر للشي اللي عم يصير هلق أو هالفترة: Today I'm wearing a suit.<br>أفعال متل like / know / want / need ما بتاخد ing: I want, مو I'm wanting. |
| Clothes | {smart clothes} = for work. {casual clothes} = for every day.<br>{try it on} = wear it in the shop. It {suits} you = it looks good.<br>Jeans, trousers and shorts are always more than one: My jeans {are} new. | smart clothes = لبس رسمي، casual clothes = لبس عادي ومريح.<br>try something on = نجرّب اللبسة بالمحل، و It suits you = لابقلك.<br>trousers و jeans و shorts دايماً جمع: My jeans are new. |
| Personality | {cheerful} = always happy. {shy} = quiet with new people.<br>{bossy} = tells people what to do. {easy-going} = relaxed.<br>{determined} = you don't stop. {hard-working} = you work a lot.<br>What's he {like}? = Tell me about him. (not: What does he like?) | صفات الشخصية: cheerful (مبسوط دايماً)، shy (خجول)، bossy (بيحب يأمر).<br>determined = مصمّم، easy-going = هادي ومو معقّد، hard-working = مجتهد.<br>What's he like? يعني كيف شخصيتو؟ — مو شو بيحب! |

**Unit 11**

| Grammar card | In simple words | عربي |
|---|---|---|
| Question words | {What} / {Which} ask about a thing. {Which} = from a few choices.<br>How + adjective: {How fast}? {How long}? {How far}? {How tall}?<br>{How many} legs? (you can count) {How much} water? (you can't count)<br>{Who took} this photo? (not: Who did take…?) | What وWhich بيسألوا عن شي (Which لما في خيارات محدودة).<br>How + صفة: How fast (قدّيش سريع)، How long (قدّيش طويل)، How far (قدّيش بعيد).<br>إذا Who هو الفاعل ما منحط did: Who took the photo?، مو Who did take…? |
| a lot of, a few, a little, not much, not many | {a lot of} = a big number or amount: {a lot of} fish / water.<br>Things you can count (trees): {a few}, {not many}.<br>Things you can't count (water): {a little}, {not much}.<br>{a few} = some, enough. {not many} = a small number. | a lot of = كتير، مع العدود والما بينعد.<br>a few و not many للأشياء اللي منعدها (trees)، و a little و not much للي ما منعدها (water).<br>a few = شوية (كفاية)، not many = مو كتير. |
| Big numbers | Say {and} after hundred: five hundred {and} five.<br>Say {point} for the dot: 5.5 = five {point} five.<br>No -s after a number: five {million}, two {thousand}. | بالإنكليزي منقول and بعد hundred: five hundred and five.<br>الفاصلة العشرية منقولها point: 5.5 = five point five.<br>million و thousand و billion ما بياخدوا s بعد الرقم: five million. |

**Unit 12**

| Grammar card | In simple words | عربي |
|---|---|---|
| going to: plans | Plans: am / is / are + {going to} + verb.<br>We{'re going to} hire a band. (We decided before.)<br>Look at the clouds! It{'s going to} rain. (You can see it coming.) | going to للخطط اللي قررناها قبل: We're going to hire a band (رح نجيب فرقة).<br>الشكل: am / is / are + going to + الفعل.<br>Look at the clouds! It's going to rain. — كمان لشي رح يصير وعم نشوف إشاراتو. |
| would like to / want to | {would like to} = want to, but more polite: I{'d like to} come.<br>Invite: {Would you like to} come? Answer: Yes, I'd love to!<br>I'd like {to} go. (not: I'd like go.) I like to go = usually.<br>With a thing, no to: I{'d like} a coffee, please. | would like to يعني 'حابب' بطريقة مؤدبة: I'd like to come.<br>Would you like to…? منستعملها للدعوة: Would you like to come? — Yes, I'd love to!<br>انتبه: I'd like to go، مو I'd like go، ومو I like to go (هي بتعني بحب عادةً). |
| Celebrations | Before a party: {decorate} the house, {hire} a band, {make} a cake.<br>{take part in} = be one of the people in it: take part in a parade.<br>{religious holiday}: Eid. {national holiday}: a day off for the whole country. | كلمات الاحتفالات: decorate (نزيّن)، hire a band (نجيب فرقة)، dress up (نلبس أحلى شي).<br>take part in = نشارك بـ: take part in a parade.<br>religious holiday = عيد ديني، national holiday = عطلة وطنية. |
| Weather and seasons | Ask: What's the weather {like}? — It's sunny.<br>It's + {sunny} / {cloudy} / {windy}. Rain or snow now: It's {raining}.<br>Seasons: {spring}, {summer}, {autumn}, {winter}. | لنسأل عن الطقس: What's the weather like? — It's sunny.<br>sunny, cloudy, windy صفات، بس raining و snowing منستعملهن مع ing: It's raining.<br>الفصول: spring (ربيع)، summer (صيف)، autumn (خريف)، winter (شتي). |

**Unit 13**

| Grammar card | In simple words | عربي |
|---|---|---|
| have to / don't have to | {have to} = it's necessary: I {have to} study.<br>{don't have to} = it isn't necessary. It doesn't mean 'you can't'.<br>He / she: {has to}, {doesn't have to}. | have to يعني لازم / مضطر: I have to study.<br>don't have to يعني مو لازم (مو ضروري)، مو 'ممنوع': You don't have to come.<br>مع he / she: has to، وبالنفي doesn't have to. |
| might and will | {will} = I'm sure: She{'ll} pass.<br>{might} = maybe: I {might} study law.<br>{won't} = will not. {might not} = maybe not.<br>After will and might: verb, no to, no -s: She might {come}. | will (رح) لما نكون متأكدين من المستقبل: She'll pass.<br>might (يمكن / ممكن) لما ما نكون متأكدين: I might study law.<br>won't = will not، و might not = يمكن لأ.<br>بعد will و might الفعل بلا to وبلا s: She might come. |
| School and careers | Subjects: maths, science, history, geography, literature.<br>{get into university} = start university. {get a degree} = finish it.<br>{apply for a job} = ask for a job. {be unemployed} = have no job. | أسماء المواد: maths (رياضيات)، science (علوم)، history (تاريخ)، geography (جغرافيا)، literature (أدب).<br>get into university = نفوت ع الجامعة، get a degree = ناخد شهادة.<br>apply for a job = نقدّم ع شغل، be unemployed = بلا شغل. |

**Unit 14**

| Grammar card | In simple words | عربي |
|---|---|---|
| Present perfect: so far today | Today isn't finished: I{'ve sent} ten emails so far today.<br>have / has + the third form of the verb: sent, made, been, done.<br>Regular verbs: worked → worked. Irregular: see the Irregular Verbs page. | المضارع التام (present perfect) لشي صار بفترة لسّا ما خلصت، متل اليوم: I've sent 10 emails so far today.<br>الشكل: have / has + التصريف التالت (past participle): sent, made, been, done.<br>الأفعال النظامية: worked → worked. والشاذة شوفها بصفحة Irregular Verbs (العامود التالت). |
| Present perfect with ever / never | Have you {ever}…? = at any time in your life.<br>{never} = not at any time: I{'ve never} been to London.<br>With a past time (yesterday, in 2019), use the past: I {went} in 2019. | Have you ever…? يعني 'هل سبق و…؟' بأي وقت بحياتك.<br>never يعني 'أبداً ما…': I've never been to London.<br>إذا ذكرنا وقت محدد بالماضي منرجع للماضي البسيط: I went to London in 2019. |
| Technology | {upload} = send to the internet. {download} = get from the internet.<br>{landline} = a phone at home. {smartphone} = a phone with the internet.<br>{be on hold} = wait on the phone. {leave a voice message} = speak after the beep. | upload = نرفع ع الإنترنت، download = ننزّل من الإنترنت.<br>landline = تلفون أرضي، smartphone = موبايل ذكي.<br>be on hold = ننطر ع الخط، leave a voice message = نترك رسالة صوتية. |

### Learn Smarter (same in all four apps)

| Slide | English | عربي |
|---|---|---|
| Arabic can help — and trick you — No 'is' in Arabic | In Arabic, 'I student' is a full sentence, with no verb. In English you need the verb: 'I am a student.' | بالعربي منقول «أنا طالب» بلا فعل. بالإنكليزي لازم الفعل: I am a student. |
| Arabic can help — and trick you — Age | In English we say 'I'm 20', not 'I have 20 years'. | بالعربي منقول «عمري 20 سنة». بالإنكليزي: I'm 20، مو I have 20 years. |
<!-- /AUTO:arabic -->
