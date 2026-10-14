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

A1.1 Practice: 6 units, 1918 scored items (U1 381, U2 324, U3 305, U4 320, U5 312, U6 276), 58 level-review items, 52 Arabic lines, 0.79 MB; reading words {1: 53, 2: 61, 3: 77, 4: 87, 5: 91, 6: 95}; places mix Damascus 46% / Syria 20% / world 34% ({'damascus': 252, 'syria': 107, 'world': 189})
A1.2 Practice: 6 units, 1707 scored items (U7 325, U8 316, U9 338, U10 240, U11 224, U12 264), 60 level-review items, 47 Arabic lines, 0.75 MB; reading words {7: 110, 8: 119, 9: 107, 10: 107, 11: 110, 12: 118}; places mix Damascus 34% / Syria 30% / world 35% ({'damascus': 60, 'syria': 53, 'world': 62})
A2.1 Practice: 7 units, 2073 scored items (U1 302, U2 294, U3 298, U4 288, U5 254, U6 300, U7 337), 56 level-review items, 67 Arabic lines, 0.84 MB; reading words {1: 107, 2: 116, 3: 124, 4: 124, 5: 124, 6: 121, 7: 128}; places mix Damascus 54% / Syria 15% / world 32% ({'damascus': 129, 'syria': 35, 'world': 77})
A2.2 Practice: 7 units, 2147 scored items (U8 310, U9 322, U10 319, U11 291, U12 340, U13 275, U14 290), 56 level-review items, 76 Arabic lines, 0.90 MB; reading words {8: 147, 9: 158, 10: 141, 11: 157, 12: 152, 13: 138, 14: 207}; places mix Damascus 46% / Syria 28% / world 25% ({'damascus': 118, 'syria': 72, 'world': 64})
ok  [browser] A1.1 Practice.html: B1 full sentence "Are you a student?", B3 pile, B4 single count, B8/B9 Escape finished, B7 24 Falling Words frames at 360px
ok  [browser] A1.1 Practice.html: 126 views at 375×812 + 72 views at 1920×1080 (class mode, zoom 1.75), parity 13 cases, scoring on 6 sets + unit test, reload kept 6 set scores, storage-blocked run clean
ok  [browser] A1.2 Practice.html: B1 full sentence "I always go to bed at eleven.", B3 pile, B4 single count, B8/B9 Escape finished, B7 22 Falling Words frames at 360px
ok  [browser] A1.2 Practice.html: 127 views at 375×812 + 72 views at 1920×1080 (class mode, zoom 1.75), parity 13 cases, scoring on 6 sets + unit test, reload kept 6 set scores, storage-blocked run clean
ok  [browser] A2.1 Practice.html: B1 full sentence "I am a police officer.", B3 pile, B4 single count, B8/B9 Escape finished, B7 30 Falling Words frames at 360px
ok  [browser] A2.1 Practice.html: 145 views at 375×812 + 84 views at 1920×1080 (class mode, zoom 1.75), parity 13 cases, scoring on 6 sets + unit test, reload kept 6 set scores, storage-blocked run clean
ok  [browser] A2.2 Practice.html: B1 full sentence "I didn't go to the party.", B3 pile, B4 single count, B8/B9 Escape finished, B7 22 Falling Words frames at 360px
ok  [browser] A2.2 Practice.html: 145 views at 375×812 + 84 views at 1920×1080 (class mode, zoom 1.75), parity 13 cases, scoring on 5 sets + unit test, reload kept 5 set scores, storage-blocked run clean
browser smoke test: passed

RESULT: ALL GATES PASSED
```
<!-- /AUTO:gates -->

## (a) Every Arabic line, by app and unit

Each line is shown with the grammar card it belongs to. Please correct anything that
doesn't sound like a friendly Damascus teacher; edit it in `content/<level>/uNN.py`
(the `ar=[...]` list of that grammar card) and rebuild.

<!-- AUTO:arabic -->

### A1.1 Practice


**Unit 1**

- *I'm / you're · my / your*: بالإنكليزي ما فينا نحذف الفعل: لازم نقول I am، مو بس I.
- *I'm / you're · my / your*: منستعمل am مع I بس، و are مع you.
- *I'm / you're · my / your*: my يعني تبعي، و your يعني تبعك: my name = اسمي.
- *I'm / you're · my / your*: بالسؤال منقدّم الفعل: Are you…?
- *a / an with jobs*: قبل الوظيفة لازم نحط a أو an: I'm a teacher، مو I'm teacher.
- *a / an with jobs*: منحط an قبل الكلمة اللي بتبلش بصوت a, e, i, o, u: an actor, an engineer.
- *a / an with jobs*: وباقي الكلمات بتاخد a: a student, a shop assistant.
- *The alphabet · How do you spell …?*: لما بدك تسأل كيف بتنكتب الكلمة منقول: How do you spell …?
- *The alphabet · How do you spell …?*: منلفظ الأحرف حرف حرف: K-A-R-E-E-M.
- *The alphabet · How do you spell …?*: انتبه: E متل 'إي'، و I متل 'آي'، و A متل 'إيه'.
- *The alphabet · How do you spell …?*: إذا في حرفين متل بعض منقول double: double L.

**Unit 2**

- *be: he / she / it*: مع he و she و it منستعمل is: He is، She is، It is.
- *be: he / she / it*: بالعربي منقول 'هي أستاذة' بلا فعل، بس بالإنكليزي لازم: She's a teacher.
- *be: he / she / it*: للنفي منحط not: He isn't Italian. وللسؤال منقدّم is: Is she Syrian?
- *be: he / she / it*: والعمر بالإنكليزي مع be: I'm 20، مو I have 20 years.
- *his / her / their / our*: بالعربي منقول 'سيارته' و'سيارتها'، بس بالإنكليزي منحط كلمة قبل الاسم: his car، her car.
- *his / her / their / our*: his للرجّال و her للمرا، حتى لو الشي نفسه مذكّر أو مؤنث بالعربي.
- *his / her / their / our*: their يعني تبعهن، و our يعني تبعنا: our teacher = أستاذنا.

**Unit 3**

- *this / that / these / those*: this و these للشي القريب (هاد، هدول)، و that و those للشي البعيد (هداك، هدوليك).
- *this / that / these / those*: this و that لشي واحد مع is، و these و those لأكتر من شي مع are.
- *this / that / these / those*: بالسؤال: What's this? → It's… و What are these? → They're…
- *be: we / they*: مع we و they منستعمل are: We are، They are.
- *be: we / they*: we يعني نحنا، و they يعني هنّن. You كمان بتنفع لأكتر من شخص.
- *be: we / they*: للنفي: aren't، وللسؤال منقدّم are: Are they Syrian?

**Unit 4**

- *Prepositions of place*: هي كلمات بتقول وين الشي: in (جوّا)، on (فوق ع)، under (تحت).
- *Prepositions of place*: next to (جنب)، near (قريب من)، behind (ورا)، in front of (قدّام).
- *Prepositions of place*: between (بين شيئين)، opposite (مقابل، بالجهة التانية من الشارع).
- *Prepositions of place*: انتبه: منقول next to مو next the، و in front of بثلاث كلمات.
- *there is / there are*: There is (There's) يعني 'في' لشي واحد، و There are يعني 'في' لأكتر من شي.
- *there is / there are*: للنفي: There isn't / There aren't. وللسؤال منقدّم is و are: Is there…? Are there…?
- *there is / there are*: انتبه: بالعربي 'في محلّين' بس بالإنكليزي There are two shops، مو There is two shops.
- *a / an, some, any, a lot of*: a و an لشي واحد، و some لعدد قليل (شوية)، و a lot of لعدد كبير (كتير).
- *a / an, some, any, a lot of*: بالنفي وبالسؤال منستعمل any مو some: There aren't any…, Are there any…?
- *a / an, some, any, a lot of*: ما منحط a قبل الجمع: There are a lot of shops، مو There are a shops.

**Unit 5**

- *possessive 's*: بالإنكليزي ما منقول 'زوج رنا' متل العربي، منقول Rana's husband: صاحب الشي أول، بعدين 's.
- *possessive 's*: يعني الترتيب معكوس: بيت أبو فراس = Abu Firas's house.
- *possessive 's*: انتبه: 's بتجي كمان بمعنى is: Rana's a teacher = Rana is a teacher.
- *possessive 's*: إذا الصاحب جمع بـ s منحط بس ': my parents' car.
- *Present simple: I / you / we / they*: المضارع البسيط منستعملو للأشياء اللي دايماً صحيحة أو للعادات: I live in Damascus.
- *Present simple: I / you / we / they*: مع I و you و we و they الفعل بيضل متل ما هو: I work, we work, they work.
- *Present simple: I / you / we / they*: للنفي منحط don't قبل الفعل: I don't live alone.
- *Present simple: I / you / we / they*: انتبه: ما منحط am مع الفعل: I go، مو I am go.
- *Questions: Do you…? / Do they…?*: لنسأل بالمضارع البسيط منحط Do بالأول: Do you live…?
- *Questions: Do you…? / Do they…?*: الجواب القصير: Yes, I do. أو No, I don't. ما منكرر الفعل.
- *Questions: Do you…? / Do they…?*: انتبه: ما منقول Are you live…? منقول Do you live…?

**Unit 6**

- *Present simple: he / she / it*: مع he و she و it منزيد s ع الفعل: he works, she lives.
- *Present simple: he / she / it*: بعض الأفعال بتاخد es: goes, watches. و study بتصير studies، و have بتصير has.
- *Present simple: he / she / it*: للنفي: doesn't + الفعل بلا s: She doesn't work، مو She doesn't works.
- *Present simple: he / she / it*: انتبه: أكتر غلطة عنا 'He go' — صحّها: He goes.
- *Questions: Does he / she…?*: لنسأل عن he و she و it منحط Does بالأول، والفعل بيرجع بلا s: Does she like…?
- *Questions: Does he / she…?*: الجواب القصير: Yes, she does. / No, he doesn't.
- *Questions: Does he / she…?*: انتبه: Does she likes? غلط — الـ s بتروح لـ does.

### A1.2 Practice


**Unit 7**

- *How often? Frequency adverbs*: هي الكلمات بتقول قدّيش منعمل الشي: always (دايماً) لـ never (أبداً).
- *How often? Frequency adverbs*: منحطها قبل الفعل: I always get up early. بس بعد am / is / are: He's never late.
- *How often? Frequency adverbs*: never بتكون لحالها نفي، ما منحط معها don't: I never drink coffee.
- *How often? Frequency adverbs*: لنسأل: How often do you…? (قدّيش بتعمل…؟)
- *Wh- questions: What time do you…?*: السؤال بيبلش بكلمة السؤال: What, Where, When, What time، بعدين do أو does.
- *Wh- questions: What time do you…?*: does مع he و she و it، و do مع الباقي، والفعل بيرجع لأصله بلا s.
- *Wh- questions: What time do you…?*: What do you do? يعني شو شغلتك؟ مو شو عم تعمل هلق.
- *Times and at / on / in*: at للساعة: at five o'clock، on لليوم: on Monday، in لقسم من النهار: in the morning.
- *Times and at / on / in*: بس منقول at night و at the weekend و at midday.
- *Times and at / on / in*: الوقت منقولو بالأرقام: 2:15 = two fifteen، 5:30 = five thirty.

**Unit 8**

- *can / can't*: can يعني بقدر / بعرف، و can't يعني ما بقدر.
- *can / can't*: can ما بتتغيّر: I can, she can — بلا s أبداً.
- *can / can't*: بعد can الفعل بيجي لحالو بلا to: I can swim، مو I can to swim.
- *Questions with can*: لنسأل بـ can منقدّم can: Can you swim?
- *Questions with can*: الجواب القصير: Yes, I can. / No, I can't. ما منكرر الفعل.
- *Questions with can*: ما منستعمل do مع can: Do you can…? غلط.
- *Review of questions*: إذا الجملة فيها am / is / are منقدّمو بالسؤال: Is he Syrian?
- *Review of questions*: إذا فيها فعل عادي منحط do أو does: Does he live here?
- *Review of questions*: وإذا فيها can منقدّم can: Can he swim?

**Unit 9**

- *was / were*: was و were هني ماضي am و is و are: كان / كانوا.
- *was / were*: was مع I و he و she و it، و were مع you و we و they.
- *was / were*: للنفي: wasn't / weren't.
- *Questions with was / were*: لنسأل بالماضي منقدّم was أو were: Were you at home?
- *Questions with was / were*: الجواب: Yes, I was. / No, I wasn't.
- *Questions with was / were*: مع كلمات السؤال: Where were you? What was your job?
- *Dates: the first of January*: التاريخ منقولو بالرقم الترتيبي: the first, the second, the third of May.
- *Dates: the first of January*: منقول on مع التاريخ: on the 5th of May، و in مع الشهر أو السنة: in May, in 2012.
- *Dates: the first of January*: السنين منقسمها: 1984 = nineteen eighty-four، 2012 = twenty twelve.

**Unit 10**

- *Past simple: regular verbs*: الماضي البسيط للأشياء اللي خلصت بوقت معروف: yesterday, in 2010.
- *Past simple: regular verbs*: الأفعال النظامية منزيدلها ed: worked, played. وstudy بتصير studied.
- *Past simple: regular verbs*: الماضي نفسه مع كل الأشخاص: I worked, she worked — بلا s.
- *Past simple: regular verbs*: للنفي: didn't + الفعل بلا ed: I didn't work، مو I didn't worked.
- *Past simple: irregular verbs*: في أفعال ما بتاخد ed، إلها شكل خاص بالماضي: go → went, have → had.
- *Past simple: irregular verbs*: هي الأفعال لازم نحفظها، شوف قائمة Irregular Verbs بالصفحة الرئيسية.
- *Past simple: irregular verbs*: بالنفي منرجع للفعل الأصلي: I didn't go، مو I didn't went.

**Unit 11**

- *Past simple: Yes / No questions*: لنسأل بالماضي منحط Did بالأول، والفعل بيرجع لأصله: Did you go?
- *Past simple: Yes / No questions*: الجواب: Yes, I did. / No, I didn't.
- *Past simple: Yes / No questions*: انتبه: مع was / were ما منستعمل did: Were you tired? مو Did you tired?
- *Past simple: Wh- questions*: بالماضي: كلمة السؤال + did + الشخص + الفعل بأصلو: Where did you go?
- *Past simple: Wh- questions*: ago بتجي بعد المدة: two days ago = من يومين.
- *Past simple: Wh- questions*: last week / last year بلا the: last week، مو the last week.

**Unit 12**

- *want and want to*: want يعني بدّي: I want a cat (بدي بسة).
- *want and want to*: إذا بعدها فعل منحط to: I want to travel، مو I want travel.
- *want and want to*: مع he و she: wants. وبالنفي والسؤال منستعمل do / does: She doesn't want to go.
- *going to*: going to منستعملها للخطط بالمستقبل: رح + فعل: I'm going to travel = رح سافر.
- *going to*: الشكل: am / is / are + going to + الفعل.
- *going to*: للنفي: I'm not going to…، وللسؤال: Are you going to…?

### A2.1 Practice


**Unit 1**

- *be: am / is / are*: بالعربي منقول 'أنا محامي' بلا فعل، بس بالإنكليزي لازم am / is / are.
- *be: am / is / are*: am مع I، و is مع he / she / it، و are مع you / we / they.
- *be: am / is / are*: للنفي: I'm not، isn't، aren't.
- *a / an with jobs*: قبل الوظيفة منحط a أو an: She's a doctor، مو She's doctor.
- *a / an with jobs*: an قبل الصوت a, e, i, o, u: an engineer, an actor.
- *a / an with jobs*: بالجمع ما منحط a: They're doctors.
- *Questions with be*: بالسؤال منقدّم am / is / are قبل الشخص: Are you married?
- *Questions with be*: مع كلمات السؤال: Where are you from? What's your job? How old is she?
- *Questions with be*: بالجواب القصير ما منختصر الإيجاب: Yes, I am، مو Yes, I'm.

**Unit 2**

- *this / that / these / those*: this (هاد) و these (هدول) للقريب، that (هداك) و those (هدوليك) للبعيد.
- *this / that / these / those*: this و that لشي واحد مع is، و these و those لأكتر من شي مع are.
- *this / that / these / those*: منستعمل This is… لنعرّف شخص: This is my cousin, Tala.
- *possessive 's*: للملكية منحط 's بعد صاحب الشي: Maya's camera = كاميرا مايا.
- *possessive 's*: إذا الصاحب جمع منتهي بـ s منحط بس ': my parents' house.
- *possessive 's*: Whose…? يعني لمين؟ Whose keys are these?
- *have got / has got*: have got يعني 'عندي': I've got a car = عندي سيارة.
- *have got / has got*: مع he / she / it منقول has got: She's got a camera.
- *have got / has got*: للنفي: haven't got / hasn't got، وللسؤال: Have you got…? Has she got…?
- *have got / has got*: انتبه: She's got = She has got، مو She is got.

**Unit 3**

- *Present simple: I / you / we / they*: المضارع البسيط للعادات والأشياء الثابتة: I get up at six.
- *Present simple: I / you / we / they*: للنفي don't + الفعل، وللسؤال Do + you + الفعل: Do you work?
- *Present simple: I / you / we / they*: انتبه: ما منحط am مع الفعل: I go، مو I am go.
- *Telling the time*: past يعني 'وْ' (بعد): twenty past ten = عشرة وتلت.
- *Telling the time*: to يعني 'إلا': five to nine = تسعة إلا خمسة.
- *Telling the time*: quarter = ربع، half = نص: half past one = وحدة ونص.
- *Places in a town*: أسماء الأماكن بالمدينة: shopping centre (مول)، street market (سوق شعبي)، block of flats (بناية).
- *Places in a town*: منستعمل There's / There are لنقول شو في بالمدينة.
- *Places in a town*: village أصغر من town، و town أصغر من city.

**Unit 4**

- *Present simple: he / she / it*: مع he / she / it الفعل بياخد s: she likes, he goes, she studies.
- *Present simple: he / she / it*: للنفي doesn't + الفعل بلا s، وللسؤال Does + الشخص + الفعل بلا s.
- *Present simple: he / she / it*: انتبه للغلطة المشهورة: He go → He goes.
- *like / love / hate + -ing*: بعد love / like / don't mind / hate منحط الفعل مع ing: I love dancing.
- *like / love / hate + -ing*: don't mind يعني ما عندي مشكلة، مو كتير حلو ومو كتير عاطل.
- *like / love / hate + -ing*: تهجئة ing: dance → dancing، swim → swimming، go → going.
- *How often? Frequency*: كلمات التكرار بتجي قبل الفعل العادي: I usually walk.
- *How often? Frequency*: وبعد am / is / are: She's always happy.
- *How often? Frequency*: How often…? منجاوب: once a week (مرة بالأسبوع)، twice a week (مرتين)، every day.

**Unit 5**

- *can / can't*: can يعني 'بقدر / بعرف'، وكمان 'مسموح': You can sit here.
- *can / can't*: can't يعني 'ما بقدر' أو 'ممنوع': You can't smoke here.
- *can / can't*: بعد can الفعل بلا to وبلا s: She can drive.
- *a / an, the, no article*: a / an لشي واحد لأول مرة منحكي عنو: I've got a car.
- *a / an, the, no article*: the لشي معروف أو حكينا عنو قبل: The car is red. وكمان the airport, the sun.
- *a / an, the, no article*: ما منحط شي بالعموميات وبـ by bus, at home, go to work: I love trains.
- *Transport and travel*: منقول by bus، by car بلا a أو the، بس on foot (مشي).
- *Transport and travel*: get on = نطلع ع الباص، get off = ننزل من الباص.
- *Transport and travel*: بالمطار: check-in desk ← security ← immigration ← gate.

**Unit 6**

- *there is / there are*: There's (في) لشي واحد أو شي ما بينعد، و There are لأكتر من شي.
- *there is / there are*: للنفي: There isn't / There aren't، وللسؤال: Is there…? Are there…?
- *there is / there are*: انتبه: There are two apples، مو There is two apples.
- *some / any · countable and uncountable*: في أشياء منعدّها (apple → apples) وأشياء ما منعدّها (rice, water, bread).
- *some / any · countable and uncountable*: اللي ما بينعد ما بياخد a ولا s: some bread، مو a bread أو breads.
- *some / any · countable and uncountable*: some بالإيجاب، و any بالنفي والسؤال.
- *How much? How many?*: How many للأشياء اللي منعدها (eggs, apples)، و How much للي ما منعدها (milk, rice).
- *How much? How many?*: How much is it? كمان منسأل فيها عن السعر: قدّيش حقها؟
- *How much? How many?*: بعد How many الاسم جمع: How many apples? مو How many apple?

**Unit 7**

- *was / were*: was و were هني الماضي تبع am / is / are.
- *was / were*: was مع I / he / she / it، و were مع you / we / they.
- *was / were*: منقول I was born (انولدت) — مو I born.
- *Past simple: regular verbs*: الماضي البسيط للأشياء اللي صارت وخلصت بوقت معروف: in 2015, last summer.
- *Past simple: regular verbs*: الأفعال النظامية بتاخد ed: worked, moved، و study بتصير studied.
- *Past simple: regular verbs*: نفس الشكل مع كل الأشخاص: I worked, she worked.
- *Past simple: irregular verbs*: في أفعال إلها شكل خاص بالماضي: go → went, get → got, meet → met.
- *Past simple: irregular verbs*: ما منزيدلها ed: went، مو goed.
- *Past simple: irregular verbs*: احفظها مع الصفحة Irregular Verbs بالتطبيق.
- *Past time phrases*: ago بتجي بعد المدة: two years ago (من سنتين).
- *Past time phrases*: last بلا the: last week، last summer.
- *Past time phrases*: When I was… يعني لما كنت: When I was ten (لما كان عمري عشر سنين).

### A2.2 Practice


**Unit 8**

- *Past simple: negative*: بالماضي للنفي منحط didn't + الفعل بأصلو: I didn't go، مو I didn't went.
- *Past simple: negative*: didn't نفسها مع كل الأشخاص: I / she / they didn't.
- *Past simple: negative*: بس مع was / were منقول wasn't / weren't بلا didn't.
- *Past simple: questions*: لنسأل بالماضي: Did + الشخص + الفعل بأصلو: Did you see it?
- *Past simple: questions*: مع كلمة السؤال: What did you do? Where did you go?
- *Past simple: questions*: مع was / were ما منستعمل did: How was the film?
- *Stories and entertainment*: أنواع الأفلام: comedy (كوميدي)، romance (رومانسي)، sci-fi (خيال علمي).
- *Stories and entertainment*: صفات: funny (مضحك)، boring (ممل)، frightening (بيخوّف)، fast-moving (أحداثو سريعة).
- *Stories and entertainment*: audience يعني الجمهور، و get good reviews يعني ياخد آراء منيحة.

**Unit 9**

- *Comparatives*: للمقارنة بين شيئين: الصفة + er + than: cheaper than (أرخص من).
- *Comparatives*: الصفات الطويلة منحط قبلها more: more expensive than (أغلى من).
- *Comparatives*: big → bigger (منضاعف الحرف)، easy → easier، و good → better، bad → worse.
- *Comparatives*: انتبه: ما منقول more cheaper — بس cheaper.
- *Superlatives*: لنقول 'الأكتر' من مجموعة: the + الصفة + est: the cheapest (الأرخص).
- *Superlatives*: الصفات الطويلة: the most + الصفة: the most expensive (الأغلى).
- *Superlatives*: good → the best، و bad → the worst.
- *Superlatives*: لا تنسَ the: the biggest، مو biggest لحالها.
- *Describing objects*: الصفة بتجي قبل الاسم بالإنكليزي: a stylish bag (شنتاية أنيقة)، مو a bag stylish.
- *Describing objects*: الصفة ما بتاخد s بالجمع: expensive shoes، مو expensives shoes.
- *Describing objects*: economical يعني ما بيصرف كتير، و second-hand يعني مستعمل.
- *Shops*: كتير من أسماء المحلات بتنتهي بـ 's: the baker's (الفرن)، the butcher's (اللحام).
- *Shops*: optician's = محل النظارات، estate agent's = مكتب عقاري، dry-cleaner's = دراي كلين.
- *Shops*: منقول at the baker's: I buy bread at the baker's.

**Unit 10**

- *Present continuous*: المضارع المستمر لشي عم يصير هلق: I'm wearing a jacket (عم ألبس جاكيت).
- *Present continuous*: الشكل: am / is / are + الفعل مع ing.
- *Present continuous*: للنفي: isn't / aren't + ing، وللسؤال: Are you…ing?
- *Present continuous*: انتبه: لا تنسى am / is / are: She's wearing، مو She wearing.
- *Present simple or present continuous?*: البسيط للعادة والشي الدايم: I usually wear jeans.
- *Present simple or present continuous?*: المستمر للشي اللي عم يصير هلق أو هالفترة: Today I'm wearing a suit.
- *Present simple or present continuous?*: أفعال متل like / know / want / need ما بتاخد ing: I want, مو I'm wanting.
- *Clothes*: smart clothes = لبس رسمي، casual clothes = لبس عادي ومريح.
- *Clothes*: try something on = نجرّب اللبسة بالمحل، و It suits you = لابقلك.
- *Clothes*: trousers و jeans و shorts دايماً جمع: My jeans are new.
- *Personality*: صفات الشخصية: cheerful (مبسوط دايماً)، shy (خجول)، bossy (بيحب يأمر).
- *Personality*: determined = مصمّم، easy-going = هادي ومو معقّد، hard-working = مجتهد.
- *Personality*: What's he like? يعني كيف شخصيتو؟ — مو شو بيحب!

**Unit 11**

- *Question words*: What وWhich بيسألوا عن شي (Which لما في خيارات محدودة).
- *Question words*: How + صفة: How fast (قدّيش سريع)، How long (قدّيش طويل)، How far (قدّيش بعيد).
- *Question words*: إذا Who هو الفاعل ما منحط did: Who took the photo?، مو Who did take…?
- *a lot of, a few, a little, not much, not many*: a lot of = كتير، مع العدود والما بينعد.
- *a lot of, a few, a little, not much, not many*: a few و not many للأشياء اللي منعدها (trees)، و a little و not much للي ما منعدها (water).
- *a lot of, a few, a little, not much, not many*: a few = شوية (كفاية)، not many = مو كتير.
- *Big numbers*: بالإنكليزي منقول and بعد hundred: five hundred and five.
- *Big numbers*: الفاصلة العشرية منقولها point: 5.5 = five point five.
- *Big numbers*: million و thousand و billion ما بياخدوا s بعد الرقم: five million.

**Unit 12**

- *going to: plans*: going to للخطط اللي قررناها قبل: We're going to hire a band (رح نجيب فرقة).
- *going to: plans*: الشكل: am / is / are + going to + الفعل.
- *going to: plans*: Look at the clouds! It's going to rain. — كمان لشي رح يصير وعم نشوف إشاراتو.
- *would like to / want to*: would like to يعني 'حابب' بطريقة مؤدبة: I'd like to come.
- *would like to / want to*: Would you like to…? منستعملها للدعوة: Would you like to come? — Yes, I'd love to!
- *would like to / want to*: انتبه: I'd like to go، مو I'd like go، ومو I like to go (هي بتعني بحب عادةً).
- *Celebrations*: كلمات الاحتفالات: decorate (نزيّن)، hire a band (نجيب فرقة)، dress up (نلبس أحلى شي).
- *Celebrations*: take part in = نشارك بـ: take part in a parade.
- *Celebrations*: religious holiday = عيد ديني، national holiday = عطلة وطنية.
- *Weather and seasons*: لنسأل عن الطقس: What's the weather like? — It's sunny.
- *Weather and seasons*: sunny, cloudy, windy صفات، بس raining و snowing منستعملهن مع ing: It's raining.
- *Weather and seasons*: الفصول: spring (ربيع)، summer (صيف)، autumn (خريف)، winter (شتي).

**Unit 13**

- *have to / don't have to*: have to يعني لازم / مضطر: I have to study.
- *have to / don't have to*: don't have to يعني مو لازم (مو ضروري)، مو 'ممنوع': You don't have to come.
- *have to / don't have to*: مع he / she: has to، وبالنفي doesn't have to.
- *might and will*: will (رح) لما نكون متأكدين من المستقبل: She'll pass.
- *might and will*: might (يمكن / ممكن) لما ما نكون متأكدين: I might study law.
- *might and will*: won't = will not، و might not = يمكن لأ.
- *might and will*: بعد will و might الفعل بلا to وبلا s: She might come.
- *School and careers*: أسماء المواد: maths (رياضيات)، science (علوم)، history (تاريخ)، geography (جغرافيا)، literature (أدب).
- *School and careers*: get into university = نفوت ع الجامعة، get a degree = ناخد شهادة.
- *School and careers*: apply for a job = نقدّم ع شغل، be unemployed = بلا شغل.

**Unit 14**

- *Present perfect: so far today*: المضارع التام (present perfect) لشي صار بفترة لسّا ما خلصت، متل اليوم: I've sent 10 emails so far today.
- *Present perfect: so far today*: الشكل: have / has + التصريف التالت (past participle): sent, made, been, done.
- *Present perfect: so far today*: الأفعال النظامية: worked → worked. والشاذة شوفها بصفحة Irregular Verbs (العامود التالت).
- *Present perfect with ever / never*: Have you ever…? يعني 'هل سبق و…؟' بأي وقت بحياتك.
- *Present perfect with ever / never*: never يعني 'أبداً ما…': I've never been to London.
- *Present perfect with ever / never*: إذا ذكرنا وقت محدد بالماضي منرجع للماضي البسيط: I went to London in 2019.
- *Technology*: upload = نرفع ع الإنترنت، download = ننزّل من الإنترنت.
- *Technology*: landline = تلفون أرضي، smartphone = موبايل ذكي.
- *Technology*: be on hold = ننطر ع الخط، leave a voice message = نترك رسالة صوتية.

### Learn Smarter (same in all four apps)

- *Arabic can help — and trick you — No 'is' in Arabic*: In Arabic we say 'أنا طالب' with no verb. In English you need it: 'I am a student.'
- *Arabic can help — and trick you — Age*: In Arabic: 'عمري 20 سنة'. In English: 'I'm 20', not 'I have 20 years'.
<!-- /AUTO:arabic -->
