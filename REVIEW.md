# REVIEW — things for Eid to check

This file is partly written by hand and partly filled in by `python3 build.py`
(the parts between the `AUTO` markers are regenerated on every full build).

## (b) Questions for Eid

_(written at the end of the build — see below)_

## (d) Things I wasn't sure about

_(written at the end of the build — see below)_

## (c) Gate results (last full build)

<!-- AUTO:gates -->
```
Font: Nunito downloaded from Google Fonts at build time
A1.2 Practice: no content yet
A2.1 Practice: no content yet
A2.2 Practice: no content yet

A1.1 Practice: 6 units, 1918 scored items (U1 381, U2 324, U3 305, U4 320, U5 312, U6 276), 58 level-review items, 52 Arabic lines, 0.78 MB; reading words {1: 53, 2: 61, 3: 77, 4: 87, 5: 91, 6: 95}; places mix Damascus 46% / Syria 19% / world 35% ({'damascus': 250, 'syria': 105, 'world': 188})
ok  [browser] A1.1 Practice.html: 126 views at 375×812 + 72 views at 1920×1080 (class mode, zoom 1.75), parity 10 cases, scoring on 6 sets + unit test, reload kept 6 set scores, storage-blocked run clean
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
<!-- /AUTO:arabic -->
