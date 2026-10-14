# REVIEW — things for Eid to check (round 2)

This file is partly written by hand and partly filled in by `python3 build.py`
(the parts between the `AUTO` markers are regenerated on every full build).

Round 2 in one paragraph: the 14 bugs are fixed and each has a gate or a browser test; Eid's
language fixes are in, and every unit was proofread again by a native-speaker pass (change lists
in `docs/notes/`); every grammar card now explains the point **in simple English first** with the
Arabic behind a **عربي** pill and a global **Arabic help** switch; the apps were redesigned (one
question per screen, a 4-step unit path, quiet surfaces, one accent colour per screen); and every
unit has a **Puzzles** section with 4 puzzles. Saved progress from round 1 still loads: every v1
item, set and word ID is kept (the build checks it) and the state is migrated in place.

## (a) English beside Arabic, for every grammar card

Each row shows the "In simple words" lines (shown first) and the Arabic lines (behind the toggle).
Please correct anything; edit `en=[...]` or `ar=[...]` in `content/<level>/uNN.py` and rebuild.

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

## (b) Every puzzle, in full

Cases with their solutions, the crossword and word-search words, every escape-room lock with its
code, the riddles and the guess-the-word lists. The crossword, word search, escape locks and the
guess-the-word list are generated from the unit's words and grammar items; the cases, escape-room
texts and riddles are written in the unit files (`PUZZLES = dict(...)`).

<!-- AUTO:puzzles -->

### A1.1 Practice


#### Unit 1

**The case — Sami, what's your job?** You're new in an office building in Malki. Hello, Lana, Sami and Yara! Three jobs, three rooms: 7, 12 and 15.  
1. The engineer: "My workplace is room 12."
2. Yara: "I'm in room 15."
3. Yara: "I'm not an engineer." *(red herring: true, not needed)*
4. Lana: "I'm not in room 7."
5. Yara: "I'm not an accountant."
6. Sami: "I'm not in room 15." *(red herring: true, not needed)*

Question: Sami, what's your job? → **accountant**  
Solution: Lana — engineer, 12; Sami — accountant, 7; Yara — architect, 15  
Reveal: Sami: "I'm an accountant. My workplace is room 7." Lana: "I'm an engineer, in room 12." Yara: "And I'm an architect, in room 15!"

**Crossword:** 1A businessman (a man / a woman who buys and sells for a company); 5A teacher (a person who teaches students); 6A student (a person who studies at a school or university); 9A eleven (the number 11); 10A nine (the number 9); 11A eight (the number 8); 12A one (the number 1); 2D seventeen (the number 17); 3D eighteen (the number 18); 4D accountant (a person who works with money and numbers for a company); 7D twenty (the number 20); 8D hello (a word you say when you meet a person)  
**Word search:** actor, architect, engineer, student, teacher, zero, one, two, three, four

**Escape room — Locked in Bait Nizam.** You're in Bait Nizam, a beautiful old house in Damascus. But the big door? Not open! Open the locks, please. *Ending:* Fantastic — you're out! Goodbye, Bait Nizam. See you again!  
- Lock 1 (Find the correct sentences) — code **34**: You a student? / I'm a engineer. / Are you an accountant? / I'm an architect in Hama. / What's you surname?
- Lock 2 (The number lock) — code **132**: Same sound as M: (1 N / 2 H / 3 E) / ___ name's Hadi. (1 I / 2 I'm / 3 My) / Same sound as A: (1 Q / 2 J / 3 E)
- Lock 3 (Count the correct sentences) — code **4**: You're an student. / I'm not a teacher. / You're a businessman. / I'm an actor. / I'm not a shop assistant.

**What am I?** *teacher*: My workplace is a school, but I'm not a student. / Books, a board and twenty students: my day! / "Open your books, please!" — I'm the person at the board. · *architect*: I'm in an office with a pen and big paper. / My work: plans for new houses and buildings. / A new house in Mezzeh? My plan first! · *engineer*: I'm in an office, on a road or on a bridge. / Machines, roads and bridges: my work! / Hadi Saleh from Bab Touma and me: the same job! · *actor*: I'm a doctor today and a king tomorrow! / My workplace: the theatre, TV or a film. / Duraid Lahham — Ghawar! — and me: the same job. · *alphabet*: I'm a long line of letters. / My first letter: A. My last letter: Z. / A, B, C, D, E… I'm all the letters! · *surname*: I'm a name, but not your first name. / Haddad? Saleh? Nasser? Yes, me! / I'm your family name. · *email address*: I'm not a phone number, but I'm for messages. / My letters, a dot… and @! / hadi.fix@mail.com — me!  
**Guess the word (targets):** actor, student, teacher, zero, three, four, five, seven, eight, nine, eleven, twelve, fifteen, sixteen, twenty, name, surname, number, spell, town, school, hello, goodbye


#### Unit 2

**The case — Who is from Aleppo?** Hadi, Maya and Jad: new students in Rana's class. Each student is from a city in Syria. One is 20, one is 30 and one is 40.  
1. Hadi isn't from Homs. *(red herring: true, not needed)*
2. The student from Homs is 30.
3. Maya is 30.
4. The student from Latakia is 40.
5. Jad isn't 40.
6. Maya isn't from Latakia. *(red herring: true, not needed)*

Question: Who is from Aleppo? → **Jad**  
Solution: Hadi — Latakia, 40; Maya — Homs, 30; Jad — Aleppo, 20  
Reveal: Jad is from Aleppo. He's 20. Hadi is 40, and he's from Latakia.

**Crossword:** 1A person (one man, woman or child); 4A people (more than one person); 5A tortilla (Spanish food: eggs and potatoes, or flat Mexican bread); 8A ninety (90); 9A age (how old you are); 10A eighty (80); 1D pizza (Italian food: bread, cheese and tomato); 2D seventy (70); 3D company (a business: people work there and sell things); 6D thirty (30); 7D place (a town, a city, a country, a building…)  
**Word search:** thirty, forty, fifty, sixty, seventy, eighty, ninety, pizza, tortilla, company

**Escape room — Locked in Khan As'ad Pasha.** You're in Khan As'ad Pasha, an old khan in Damascus. The big door isn't open! Open the locks, please. *Ending:* The big door is open. Welcome to the souq!  
- Lock 1 (Find the correct sentences) — code **14**: How old is Reem? / Reem and Tala: her school is in Dummar. / Reem is seventeen. His school is in Dummar. / Maya is a barista. Her café is in Baramkeh. / Me and my family: their house is in Midan.
- Lock 2 (The number lock) — code **122**: He ___ an engineer. (1 's / 2 're / 3 'm) / Is Wei from Japan? — No, he ___. (1 aren't / 2 isn't / 3 not) / Salma is a nurse. ___ hospital is in Malki. (1 His / 2 Her / 3 Our)
- Lock 3 (Count the correct sentences) — code **2**: Tala isn't Lebanese. / He are from Egypt. / Kenji and Mei: her flat is in Tokyo. / She's a teacher. / Is Pierre French? — Yes, he are.

**What am I?** *pizza*: I'm Italian. / I'm round. / I'm food with cheese and tomato. · *samba music*: I'm from Brazil. / I'm loud and happy. / I'm Brazilian music for dancing! · *Egypt*: I'm a country. / My river is the Nile. / Cairo is my capital. · *China*: I'm a big country in Asia. / Beijing is my capital. / My food is famous: rice and noodles! · *winner*: I'm a person. / I'm number one. / I'm happy at the end of the race. · *best friend*: I'm not family, but I'm like family. / Your secret? Safe with me! / I'm your number one friend.  
**Guess the word (targets):** thirty, forty, fifty, sixty, seventy, eighty, ninety, pizza, company, place, person, people, river, winner


#### Unit 3

**The case — Who's the milk for?** Maya, Jad and Reem are on holiday in Tartus. It's breakfast time at the hotel: three cups and three plates. Each friend: one cup, one plate.  
1. These sandwiches are for Jad.
2. That milk isn't for Reem. *(red herring: true, not needed)*
3. The eggs aren't for Maya.
4. The tea and the eggs are for the same person.
5. Those apples aren't for Jad. *(red herring: true, not needed)*
6. The coffee isn't for Jad.

Question: Who's the milk for? → **Jad**  
Solution: Maya — coffee, apples; Jad — milk, sandwiches; Reem — tea, eggs  
Reveal: The milk and the sandwiches are for Jad. The coffee and the apples are for Maya. The tea and the eggs are for Reem — they're her favourite!

**Crossword:** 2A black (the colour of the night); 3A fish (an animal from the sea or a river; also food); 5A vegetables (potatoes, tomatoes, carrots…); 6A fruit (apples, oranges, grapes…); 7A red (the colour of tomatoes); 9A potatoes (brown or yellow vegetables; chips are made from them); 10A colours (black, white, red, yellow…); 1D cheese (white or yellow food made from milk); 2D breakfast (the first meal of the day); 3D favourite (you like it best); 4D delicious (it tastes very good); 8D pasta (Italian food, like spaghetti)  
**Word search:** tea, coffee, milk, water, meat, fish, chicken, fruit, apples, potatoes

**Escape room — Locked in the spice shop in Bzouriyah.** You're in a spice shop in Souq al-Bzouriyah. These spices are fantastic, but the door isn't open! *Ending:* The door is open! We're happy, and the spices are in our bags.  
- Lock 1 (Find the correct sentences) — code **45**: Are they Polish? — Yes, they is. / We isn't Italian. / They typical Syrian dishes. / Are they on holiday? / My friends are friendly.
- Lock 2 (The number lock) — code **111**: My parents ___ in Aleppo. (1 are / 2 is / 3 be) / ___ we late? (1 Are / 2 Am / 3 Is) / Kenji and Mei ___ Italian. Kenji is Japanese. (1 aren't / 2 not / 3 isn't)
- Lock 3 (Count the correct sentences) — code **1**: Those is my car. / We from Syria. / These is my friends. / These child are happy. / Those buses are new.

**What am I?** *coffee*: I'm hot and black, and I'm strong. / In Damascus, I'm with cardamom. / Espresso? Cappuccino? Yes, me! · *taxi*: I'm yellow in the streets of Damascus. / I'm a car, but I'm not your car. / Abu Salim? He's my driver! · *bread*: I'm hot from the oven. / Labneh, ful and hummus are with me at breakfast. / A sandwich? I'm the outside! · *apples*: We're from the orchards of Zabadani. / We're round fruit, red or green. / Isaac Newton? Bonk! One of us, on his head! · *fish*: I'm from the sea or a river. / I'm typical food in Latakia and Tartus. / I'm an animal, and I'm a good swimmer! · *yellow*: I'm a happy colour. / Lemons and the sun? That's me! / The taxis in Damascus? They're this colour. · *hotel*: On holiday? I'm your home for a week. / My rooms are cheap or expensive. / Beds, keys, breakfast and five stars! · *breakfast*: I'm the first of three. / Ful, labneh, bread and tea: I'm a typical Syrian one. / I'm the meal in the morning.  
**Guess the word (targets):** shop, shops, taxi, taxis, cars, student, buses, address, city, cities, country, woman, women, person, people, child, happy, cheap, awful, coffee, milk, water, meat, fish, chicken, fruit, apples, bread, rice, pasta, eggs, cheese, hotel, colours, black, white, yellow, typical


#### Unit 4

**The case — Where's Hadi?** Saturday in the city centre. There are three friends here — Rana, Kareem and Hadi — but where are they? One friend is in a café, one is at a bus stop and one is in a car park.  
1. The bus stop is opposite the cinema.
2. Hadi isn't in the car park. *(red herring: true, not needed)*
3. The car park is behind the hotel.
4. Kareem is behind the hotel.
5. There's a friend at the bus stop, but it isn't Rana.
6. Kareem isn't next to the bank. *(red herring: true, not needed)*

Question: Where's Hadi? → **bus stop**  
Solution: Rana — café, next to the bank; Kareem — car park, behind the hotel; Hadi — bus stop, opposite the cinema  
Reveal: Hadi is at the bus stop, opposite the cinema. Kareem is in the car park behind the hotel, and Rana is in the café next to the bank.

**Crossword:** 1A big (not small); 4A river (water that goes to the sea); 6A island (land with water all around it); 8A old (not new); 10A supermarket (a big shop for food and drink); 2D good (nice, not bad); 3D restaurant (a place where you eat a meal); 4D rainforest (a forest with a lot of rain and tall trees); 5D cathedral (a big, important church); 7D square (an open place in a town, with streets around it); 9D bank (a place for your money)  
**Word search:** bank, park, cinema, hotel, square, lake, island, mountain, beach, river

**Escape room — Locked in the Hejaz Railway Station.** You're in the Hejaz Railway Station. There's a big old door in front of you, but it isn't open! *Ending:* The door is open! There's a train to Zabadani next to you. Have a good trip!  
- Lock 1 (Find the correct sentences) — code **45**: The book is in front the computer. / The cat is under of the bed. / Are there a bank in Sarouja? / There is a big hotel in the square. / There isn't a bank in the village.
- Lock 2 (The number lock) — code **331**: There's ___ university in Baramkeh. (1 any / 2 an / 3 a) / ___ there any hotels in Bloudan? (1 Is / 2 They / 3 Are) / There are ___ people in Souq al-Hamidiyah! (a big number) (1 a lot of / 2 an / 3 any)
- Lock 3 (Count the correct sentences) — code **3**: There are a shops in my street. / There's an old cinema in the city centre. / There are two shops in my street. / There aren't any hotels here. / There aren't a beach in Damascus.

**What am I?** *cinema*: I'm dark inside, but the people are happy. / There are a lot of seats and a big screen in me. / Popcorn and a film? Come in! · *bank*: I'm a place for numbers, not letters. / There's a lot of money in me. / Your money? It's safe with me! · *island*: I'm in the sea or in a lake. / There's water all around me. / Arwad, near Tartus — that's me! · *mountain*: I'm very high, and there's snow on me in winter. / There are a lot of us in Syria. / Qasioun, behind Damascus, is one of us! · *supermarket*: There are a lot of things in me, from apples to soap. / I'm a big shop for food and drink. / Trolleys, baskets and a long queue — that's me! · *rainforest*: I'm green, wet and very big. / There are a lot of tall trees and animals in me. / The Amazon, in Brazil — that's me! · *café*: There's music, and there are a lot of people in me. / Tea, coffee and cake: that's my menu. / Al-Nofara, behind the Umayyad Mosque, is a famous one!  
**Guess the word (targets):** bank, park, cinema, hotel, square, lake, island, beach, river, hill, town, street, great, good, famous, small, nice, travel


#### Unit 5

**The case — Who's the medicine student?** Hiba, Omar and Nadia study at Damascus University. They live in three areas: Jaramana, Mezzeh and Dummar. Their subjects? Medicine, engineering and languages.  
1. Hiba: "I live in Jaramana."
2. Omar: "I don't live in Jaramana." *(red herring: true, not needed)*
3. The medicine student's flat is in Mezzeh.
4. Nadia: "I don't live in Mezzeh."
5. Hiba's subject isn't medicine. *(red herring: true, not needed)*
6. Nadia: "I don't study engineering."

Question: Who's the medicine student? → **Omar**  
Solution: Hiba — Jaramana, engineering; Omar — Mezzeh, medicine; Nadia — Dummar, languages  
Reveal: Omar is the medicine student, and his flat is in Mezzeh. Hiba's subject is engineering, and her home is in Jaramana. Nadia's subject is languages, and her family's flat is in Dummar.

**Crossword:** 2A husband (the man you are married to); 5A son (your male child); 8A children (sons and daughters); 9A engineering (the study of machines, roads and buildings); 11A grandparents (the parents of your mother or father); 12A grandfather (the father of your mother or father); 1D brother (a boy or man with the same parents as you); 3D business (buying and selling); 4D alone (with nobody); 6D grandmother (the mother of your mother or father); 7D magazine (a thin book with photos; there's a new one every week or month); 10D teach (to help people learn)  
**Word search:** husband, wife, parents, father, mother, children, son, daughter, brother, sister

**Escape room — Locked in the courtyard house.** You're in your grandparents' courtyard house in Sarouja. The jasmine is beautiful, but the big door isn't open! *Ending:* The door is open! Your grandparents are happy, and your grandmother's kibbeh is on the table.  
- Lock 1 (Find the correct sentences) — code **24**: You have children? / Do you live alone? — No, I don't. / We are go to work by bus. / Maya's café is in Baramkeh. / Kareem is the husband of Rana.
- Lock 2 (The number lock) — code **332**: I ___ medicine at university. (1 am study / 2 studying / 3 study) / They ___ for a big company. (1 are work / 2 working / 3 work) / Joud is Mais's ___. (1 mother / 2 sister / 3 brother)
- Lock 3 (Count the correct sentences) — code **2**: Have you study medicine? / You are speak English very well! / Do they work in an office? / My parents don't live alone. / They are work long hours.

**What am I?** *grandmother*: I have grandchildren, and I love them. / My kibbeh is famous in the family! / I'm your father's mother or your mother's mother. · *wife*: I'm a woman, and I'm married. / In the family photo, I'm next to my husband. / Rana is Kareem's … — that's me! · *magazine*: I'm thin, and I have a lot of photos. / A new me every week or every month! / National Geographic? Vogue? Read me on the bus. · *medicine*: I'm a long course at university: six years! / My students work in hospitals later. / Study me, and you're a doctor! · *alone*: No brothers, no sisters, no parents in my flat. / I'm the opposite of 'with my family'. / With nobody: just me! · *grandchildren*: We call you 'Teta' and 'Jiddo'. / We're the children of your son or your daughter. / Joud and Mais? We're Abu Firas and Hind's …! · *brother*: I'm a boy or a man in your family. / We have the same mother and the same father. / Ziad is Layla's … — that's me!  
**Guess the word (targets):** husband, wife, parents, father, mother, brother, sister, speak, teach, alone


#### Unit 6

**The case — Who has a dog?** Dima, Walid and Hala are neighbours in Midan. Each friend plays something after work, and each friend has a pet.  
1. The tennis player has a cat.
2. Walid doesn't play the piano.
3. Dima doesn't play computer games. *(red herring: true, not needed)*
4. Hala doesn't play tennis.
5. Hala doesn't play the piano.
6. Walid doesn't have a fish. *(red herring: true, not needed)*
7. Hala doesn't have a dog.

Question: Who has a dog? → **Dima**  
Solution: Dima — the piano, dog; Walid — tennis, cat; Hala — computer games, fish  
Reveal: Dima has a dog, and she plays the piano. Walid plays tennis, and he has a cat. Hala doesn't have a dog — she has a fish, and she plays computer games!

**Crossword:** 5A hate (to not like at all); 6A win (to be first in a competition / the person who is first); 8A competition (an event where people try to be the best); 11A football (a team sport with a ball you kick); 1D cricket (a sport with a bat and a ball, popular in England and India); 2D basketball (a team sport; you throw the ball into a high net); 3D pet (an animal in your home: a dog, a cat, a fish); 4D window (glass in a wall; you see out of it); 7D unusual (not normal; different); 9D dogs (animals that are often pets; they say "woof"); 10D jazz (a type of music with saxophones and piano)  
**Word search:** dinner, love, like, hate, jazz, dancing, football, running, dogs, horses

**Escape room — Locked in the old library.** You're in the old library. Reem studies here every day, but today the big door doesn't open! *Ending:* The door opens! Reem smiles, and she goes home with three new books.  
- Lock 1 (Find the correct sentences) — code **23**: Abu Omar have a shop in Kafr Sousa. / Maya doesn't play the guitar. / Do they live in Homs? / She likes dogs? / Hadi like rock music.
- Lock 2 (The number lock) — code **223**: Does Abu Omar ___ horses? (1 liking / 2 like / 3 likes) / ___ your parents live in Aleppo? (1 Does / 2 Do / 3 Are) / Does Kareem have a car? — No, he ___. (1 hasn't / 2 don't / 3 doesn't)
- Lock 3 (Count the correct sentences) — code **4**: Reem studies at the library. / Does Rana teach English? / Does Reem read magazines? / Rana teaches English. / Does she likes jazz?

**What am I?** *guitar*: Hadi plays me, and Maya plays me, too. / Rock music? Flamenco? I'm the star! / I'm a musical instrument with six strings. · *piano*: Reem plays me at home. / I'm big and heavy, and I'm black or brown. / I have 88 black and white keys. · *library*: Shh! Everybody is quiet in me. / Reem studies in me after school. / I have a lot of books, and you take them home for two weeks. · *window cleaner*: I work high up, on tall buildings. / Bassel from Homs does my job in Dubai. / Glass, water and a cloth: my work every day! · *hockey*: I'm popular in Canada and Russia. / Olga plays me on ice in winter. / I'm a sport with sticks and a small ball. · *pet*: I live in your home, and I'm part of the family. / Mais has one: a cat. / A dog, a cat or a fish in your house — that's me! · *fast food*: I'm quick and cheap, but not very healthy. / Fadi eats me in his car. / Burgers, chips and a big cola!  
**Guess the word (targets):** dinner, love, like, hate, jazz, dancing, running, dogs, horses, winner, piano, guitar, cricket, hockey, window, library, animal, unusual


### A1.2 Practice


#### Unit 7

**The case — Who has a day off on Wednesday?** Nour, Tareq and Walid: three friends in Mezzeh. Each friend gets up at a different time on weekdays, and each friend has a different day off work.  
1. Nour always gets up at seven fifteen.
2. Tareq never gets up at seven fifteen. *(red herring: true, not needed)*
3. Walid never gets up at six o'clock.
4. The friend with a day off on Saturday always gets up at six thirty.
5. Walid doesn't have a day off on Monday. *(red herring: true, not needed)*
6. The friend with a day off on Monday always gets up at seven fifteen.

Question: Who has a day off on Wednesday? → **Tareq**  
Solution: Nour — seven fifteen, Monday; Tareq — six o'clock, Wednesday; Walid — six thirty, Saturday  
Reveal: Tareq has a day off on Wednesday. He always gets up at six o'clock. Nour gets up at seven fifteen and relaxes on Monday, and Walid has a day off on Saturday.

**Crossword:** 1A lunch (to eat your morning / midday / evening meal); 4A festival (a big event with food or music, often for days); 5A month (all the days / weeks… again and again); 9A Wednesday (the day after Tuesday); 10A dinner (to eat your morning / midday / evening meal); 11A relax (to rest and feel calm); 2D celebrate (to do something special for a happy day); 3D exam (a test at school or university); 6D Tuesday (the day after Monday); 7D meeting (people come together to talk about work); 8D year (all the days / weeks… again and again)  
**Word search:** lunch, dinner, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, midday

**Escape room — Locked in the Hejaz Railway Station.** You're in the Hejaz Railway Station. It's midnight, and the big door isn't open! Open the locks — your train leaves at six fifteen. *Ending:* The door is open, and it's six o'clock. You're on time for your train!  
- Lock 1 (Find the correct sentences) — code **12**: He usually eats at home. / I get up at six o'clock. / She always is happy. / I sometimes am tired. / Salma works in night.
- Lock 2 (The number lock) — code **212**: Mei does Tai Chi every morning. She ___ does it. (1 hardly ever / 2 always / 3 never) / I have English ___ the afternoon. (1 in / 2 on / 3 at) / What time do you ___ work? (1 finishing / 2 finish / 3 finishes)
- Lock 3 (Count the correct sentences) — code **4**: Fadi hardly ever cooks. / The meeting is in three thirty. / The shop is closed on Friday. / I always go to bed at eleven. / She drinks coffee in the morning.

**What am I?** *Friday*: Families in Syria often have a big lunch on me. / A lot of people don't work on me. / I'm the day after Thursday. · *midnight*: I'm a time. / Most people are in bed at me. / I'm twelve o'clock at night. · *Tai Chi*: I'm very slow. / People often do me in the park in the morning. / I'm an exercise from China. · *exam*: Students don't usually like me. / I'm on paper, with a lot of questions. / I'm a test at school or university. · *tourists*: We usually have a camera and a map. / We visit Maaloula and the Umayyad Mosque. / We're people on holiday. · *go to bed*: I'm the last thing you do every day. / Children usually do this at eight or nine. / After this, you sleep. · *football match*: I'm ninety minutes long. / People often watch me on TV on Friday evening. / Two teams play me with one ball.  
**Guess the word (targets):** lunch, dinner, midday, week, weekend, month, year, busy, party, young, exam, relax, meeting, tourism


#### Unit 8

**The case — Who can play chess?** Ghada, Walid and Lama: three new people at a sports club in Mezzeh. One is a personal trainer, one is a dance teacher and one is a nanny for the children's room. Each person can do one special thing: swim, play chess or sing.  
1. The nanny can sing very well.
2. Ghada isn't the dance teacher.
3. Walid isn't the nanny. *(red herring: true, not needed)*
4. Lama can't swim.
5. The personal trainer can swim very well.
6. Ghada can't sing. *(red herring: true, not needed)*
7. Lama can't play chess.

Question: Who can play chess? → **Walid**  
Solution: Ghada — personal trainer, swim; Walid — dance teacher, play chess; Lama — nanny, sing  
Reveal: Walid can play chess. He's the dance teacher! Ghada is the personal trainer — she can swim very well — and Lama is the nanny. She can sing to the children.

**Crossword:** 6A abilities (things you can do); 8A babies (a very young child / very young children); 10A forget (not to remember); 12A nanny (a person who looks after children in their home); 1D thumb (the short, thick finger); 2D ear (you hear with them; you have two); 3D finger (one of five on your hand); 4D fit (strong and healthy); 5D remember (to keep in your head; not to forget); 7D sporty (you like sport and you're good at it); 9D baby (a very young child / very young children); 11D fast (quickly; not slow)  
**Word search:** walk, run, swim, dance, sing, remember, forget, head, nose, ear

**Escape room — Locked in the old hammam.** You're in an old hammam in the Old City. The door isn't open! Can you open the locks? *Ending:* The door is open. You can go home now — clean and happy!  
- Lock 1 (Find the correct sentences) — code **35**: Cans he ride a bike? / Do you are a teacher? / Do you like dancing? / Is she live in Midan? / They can't sing.
- Lock 2 (The number lock) — code **221**: How old ___ your son? (1 can / 2 is / 3 does) / Can he ___ the piano? (1 plays / 2 play / 3 to play) / What time ___ the bank open? (1 does / 2 are / 3 can)
- Lock 3 (Count the correct sentences) — code **4**: Where is she from? / I can drive. / Can you swim? / What can you cook? / Can she drives?

**What am I?** *nose*: I'm in the middle of your face. / I can smell coffee and jasmine. / You blow me with a tissue. · *thumb*: I'm short and thick. / I'm on your hand, but I'm not like the other four. / Put me up and it means 'Well done!' · *ear*: You have two of me. / I'm on the side of your head. / You can hear music with me. · *swim*: Fish can do it, but cats usually can't. / You can do it in the sea in Latakia. / You move in water. · *forget*: I'm a verb. / Your keys, your phone, a person's name — I'm the problem! / I'm the opposite of remember. · *nanny*: I work in a family's home. / I'm good with babies and small children. / Parents pay me to look after their children. · *play chess*: It's a game for two people. / The board is black and white. / There's a king and a queen.  
**Guess the word (targets):** walk, swim, dance, sing, forget, head, nose, mouth, hair, hand, finger, thumb, well, fast, sporty, skills, baby, babies, nanny


#### Unit 9

**The case — Who was in Bloudan?** Last year, Layla, Kareem and Dima were on holiday. Each friend was in a different place — Bloudan, Tartus or Aleppo — on a different date.  
1. Dima was on holiday on the fifth of April.
2. Layla wasn't in Bloudan. *(red herring: true, not needed)*
3. The friend in Tartus wasn't there on the fifth of April.
4. The friend in Bloudan was there on the twentieth of December.
5. Kareem wasn't in Aleppo. *(red herring: true, not needed)*
6. Layla wasn't on holiday on the twentieth of December.

Question: Who was in Bloudan? → **Kareem**  
Solution: Layla — Tartus, the second of August; Kareem — Bloudan, the twentieth of December; Dima — Aleppo, the fifth of April  
Reveal: Kareem was in Bloudan on the twentieth of December. It was cold and snowy! Dima was in Aleppo on the fifth of April, and Layla was in Tartus on the second of August.

**Crossword:** 1A clean (not dirty); 7A seventeenth (17th); 8A fifteenth (15th); 9A seventh (7th); 10A sixth (6th); 2D nineteenth (19th); 3D eleventh (11th); 4D eighteenth (18th); 5D President (the leader of a country); 6D twentieth (20th)  
**Word search:** January, February, March, April, May, June, July, August, September, October

**Escape room — Locked in the old cinema.** You're in an old cinema in Damascus. The film was very long, and now the door isn't open! Open the locks. *Ending:* The door is open. What a night! The film was fantastic, and the locks were fun.  
- Lock 1 (Find the correct sentences) — code **15**: Were they on holiday? / We wasn't late. / The threeth of March was cold. / The streets was quiet. / Was Reem at school?
- Lock 2 (The number lock) — code **232**: The exam was ___ April. (1 on / 2 in / 3 at) / The children ___ naughty today. (1 is / 2 was / 3 were) / We ___ in Istanbul in August. (1 are / 2 were / 3 was)
- Lock 3 (Count the correct sentences) — code **3**: Where were you on Friday? / You were at the party! / It weren't cold yesterday. / Today is the second of April. / My father were a postman.

**What am I?** *February*: I'm short. / I'm often cold and snowy in Bloudan. / I'm the second month of the year. · *yesterday*: I'm a day. / I was here, but now I'm not. / I'm the day before today. · *noisy*: I'm an adjective. / The souq on a Thursday evening is often like me. / I'm the opposite of quiet. · *naughty*: I'm a word for some children. / I never listen to Mum and Dad. / The teacher isn't happy with me! · *President*: I'm a very important person. / In the USA, my home is the White House. / I'm the leader of a country. · *record*: I'm round and black. / I'm old, but I'm cool again now. / Grandfathers play Fairuz on me. · *December*: I'm cold and wet in Damascus. / Christmas is in me. / I'm the last month of the year.  
**Guess the word (targets):** first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth, twelfth, record, quiet, noisy, clean, dirty, naughty


#### Unit 10

**The case — Who studied in Paris?** Ghada, Fadi and Rami left secondary school in Damascus in 2005. After that, each friend studied in a different city, and each friend got a different creative job.  
1. The musician studied in Cairo.
2. Ghada didn't work as an artist. *(red herring: true, not needed)*
3. Fadi didn't become an architect.
4. Rami didn't go to university in Cairo.
5. The artist went to university in Aleppo.
6. Fadi didn't study in Aleppo. *(red herring: true, not needed)*
7. Rami didn't study in Paris.

Question: Who studied in Paris? → **Ghada**  
Solution: Ghada — architect, Paris; Fadi — musician, Cairo; Rami — artist, Aleppo  
Reveal: Ghada studied in Paris, and she became an architect. Fadi went to university in Cairo and became a musician. Rami studied in Aleppo — he's an artist.

**Crossword:** 4A inventor (a person who makes something new for the first time); 5A singer (a person who sings as a job); 7A architect (a person who plans buildings); 8A plane (it flies in the sky and carries people); 1D musician (a person who plays music as a job); 2D jewellery (rings, necklaces, earrings); 3D bridge (it goes over a river or a road); 5D special (different and important); 6D artist (a person who paints or draws pictures)  
**Word search:** someone, artist, musician, singer, writer, architect, inventor, dancer, special, prize

**Escape room — Locked in the Azem Palace.** You're in the Azem Palace. You stayed late in the museum, and now the big door isn't open! Open the locks. *Ending:* You did it! You opened the door and walked out into the souq.  
- Lock 1 (Find the correct sentences) — code **35**: The bus stoped here. / We was live in Homs. / I didn't have breakfast. / Tareq maked a fantastic dinner. / She won the competition.
- Lock 2 (The number lock) — code **231**: We ___ to Istanbul last year. (1 travels / 2 travelled / 3 travel) / Tareq ___ a big kibbeh for the competition. (1 make / 2 maked / 3 made) / He ___ a famous singer. (1 became / 2 become / 3 becomed)
- Lock 3 (Count the correct sentences) — code **3**: We bought a new car. / I no watched TV yesterday. / She didn't worked yesterday. / They didn't like the film. / She didn't go to school.

**What am I?** *inventor*: I didn't buy my ideas — I made them. / Alexander Graham Bell was one. He made the first telephone. / I make something new for the first time. · *architect*: I don't build houses, but I plan them. / Zaha Hadid from Iraq was a famous one. / I design buildings. · *singer*: My voice is my job. / Fairuz and Umm Kulthum were very famous ones. / I make music with my voice on stage. · *bridge*: The Golden Gate in San Francisco is a famous one. / People walk or drive across me. / I go over a river or a road. · *plane*: The Wright brothers built the first one in 1903. / I carry a lot of people — to Dubai in three hours. / I fly in the sky. · *jewellery*: I'm small, but I'm often very expensive. / You find a lot of me in Souq al-Hamidiyah. / Rings, necklaces and earrings are me. · *get married*: Two people, one big party, a lot of music and food. / Rana and Kareem did this in 2012. / After this, two people are husband and wife.  
**Guess the word (targets):** someone, artist, singer, writer, dancer, special, prize, award, plane, bridge


#### Unit 11

**The case — Who went by train?** Tareq, Salma and Nour live in Damascus. Each friend went to Aleppo at a different time — last week, a month ago or last year — by bus, by train or by plane.  
1. The train trip was a month ago.
2. Tareq didn't go last week.
3. Salma didn't go by plane. *(red herring: true, not needed)*
4. The bus trip was last week.
5. Nour didn't go by bus.
6. Nour didn't go last year. *(red herring: true, not needed)*
7. Tareq didn't go a month ago.

Question: Who went to Aleppo by train? → **Nour**  
Solution: Tareq — by plane, last year; Salma — by bus, last week; Nour — by train, a month ago  
Reveal: Did Nour go by train? Yes, she did! She went a month ago. Salma went by bus last week, and Tareq went by plane last year.

**Crossword:** 3A eat out (to have a meal in a restaurant); 4A be late (to arrive after the right time); 5A go walking (to walk in the country for fun); 7A last week (the week / month / year before this one); 8A visit museums (to go to see museums); 9A tunnel (a road under the ground or through a mountain); 10A be on time (to arrive at the right time); 1D be early (to arrive before the right time); 2D dangerous (it can hurt you); 5D go skiing (to move on snow with skis); 6D passenger (a person who travels in a car, bus, train or plane)  
**Word search:** dangerous, tunnel, flight, airport, passenger, go by bus, be late, be early, be on time, two months

**Escape room — Locked in a train to Aleppo.** You're on an old train to Aleppo. You went to the café, and now the door of your carriage isn't open! Open the locks. *Ending:* The door is open, and you're back in your seat. Did you arrive in Aleppo on time? Yes, you did!  
- Lock 1 (Find the correct sentences) — code **25**: I went there two weeks before. / Did they go skiing? — Yes, they did. / Did she bought a ticket? / Did you tired? / Where did you go?
- Lock 2 (The number lock) — code **221**: Did you ___ a return ticket? (1 buys / 2 buy / 3 bought) / ___ Jad ride his bike to Latakia? (1 Were / 2 Did / 3 Was) / What did you ___ in Paris? (1 do / 2 does / 3 did)
- Lock 3 (Count the correct sentences) — code **1**: How did they travel? / You visited the museum? / We arrived the last week. / What did the weather like? / What did you did yesterday?

**What am I?** *passenger*: I don't drive. / I sit on a bus, a train or a plane and travel. / I need a ticket. · *tunnel*: I'm long and dark. / Trains and cars go through me. / I'm under a mountain or under the sea. · *airport*: I'm big and busy. / Planes arrive and leave here every day. / You go here for your flight. · *go skiing*: You need warm clothes and a lot of snow. / Last winter, a lot of people did this in Lebanon. / You go down a mountain on two long skis. · *dangerous*: I'm an adjective. / A mountain road at night is often like me. / I can hurt you! · *eat out*: You don't cook, and you don't wash the plates. / You choose from a menu and pay at the end. / You have dinner in a restaurant. · *go on a boat trip*: You need a sunny day and a calm sea. / Last summer, we did this from Tartus to Arwad. / You travel on the water for fun.  
**Guess the word (targets):** train, plane, month, year, tunnel, flight, airport


#### Unit 12

**The case — Who is going to buy the jacket?** Fadi, Hala and Jad are in a clothes shop in Sha'lan. Each friend wants one thing — a scarf, a jacket or a T-shirt — in a different colour: red, black or green.  
1. One friend wants a red scarf.
2. Fadi isn't going to buy anything green. *(red herring: true, not needed)*
3. Hala doesn't want a jacket.
4. Nobody wants a black T-shirt.
5. Jad doesn't want anything red.
6. Jad doesn't want a T-shirt. *(red herring: true, not needed)*
7. Hala isn't going to buy anything red.

Question: Who is going to buy the jacket? → **Jad**  
Solution: Fadi — scarf, red; Hala — T-shirt, green; Jad — jacket, black  
Reveal: Jad is going to buy the jacket. It's black! Fadi wants the red scarf — it's a present for his wife — and Hala is going to buy a green T-shirt.

**Crossword:** 1A jacket (a short coat); 5A scarf (a long piece of cloth for your neck); 8A jeans (trousers made of strong cotton, often blue); 9A grey (black + white); 10A frightening (it makes you afraid); 2D accessories (small things you wear: bags, belts, scarves); 3D technology (phones, computers and machines); 4D jewellery (rings, necklaces and earrings); 6D red (the colour of tomatoes); 7D earrings (jewellery for your ears)  
**Word search:** clothes, jeans, scarf, jacket, handbag, umbrella, jewellery, earrings, necklace, bracelet

**Escape room — Locked in the Citadel of Damascus.** You're in the Citadel of Damascus. You want to go home, but the big door isn't open! Open the locks. *Ending:* The door is open! What are you going to do now? You're going to have an ice cream in Souq al-Hamidiyah.  
- Lock 1 (Find the correct sentences) — code **25**: I going to buy a jacket. / I want a new phone. / Does you want to come? / We want to a new car. / He doesn't want to go.
- Lock 2 (The number lock) — code **332**: Jad is going to ___ a football team. (1 starts / 2 started / 3 start) / Hadi doesn't want ___ to the party. (1 go / 2 going / 3 to go) / ___ she going to do a course? (1 Are / 2 Is / 3 Does)
- Lock 3 (Count the correct sentences) — code **4**: I'm not going to eat out. / She's going to buy earrings. / Reem wants take part in a quiz show. / We're going to go to Bloudan. / Is she going to do a course?

**What am I?** *umbrella*: I open and close. / I'm usually in your bag in winter. / You hold me over your head in the rain. · *earrings*: You wear us in pairs. / We're gold or silver jewellery. / We're for your ears. · *see the Northern Lights*: A lot of travellers want to do this in Norway or Iceland. / You need a cold, dark night in winter. / Green and purple lights dance in the sky. · *boring*: I'm an adjective. / A long lesson with no pictures is often like me. / I'm the opposite of exciting. · *sociable*: I'm an adjective for a person. / I love parties and new people. / I'm never alone at a wedding! · *grey*: I'm a colour. / Elephants and clouds in winter are this colour. / I'm black and white together. · *go diving*: You're going to need special equipment. / In the Red Sea, you can see beautiful fish. / You swim under the sea.  
**Guess the word (targets):** clothes, jeans, scarf, jacket, handbag, orange, yellow, green, blue, purple, brown, white, black, grey, small, medium, large, boring, carry


### A2.1 Practice


#### Unit 1

**The case — Who is the lawyer?** Four new friends at the language café at Al-Nofara: Yara, Tareq, Nour and Samer. They're from four different cities in Syria. Their jobs and ages are all different, too.  
1. The musician is from Hama.
2. Nour is 24.
3. Samer isn't from Aleppo. *(red herring: true, not needed)*
4. The lawyer is from Latakia.
5. Tareq isn't a doctor.
6. The person from Homs is 32.
7. Yara is from Hama.
8. The engineer is 36.

Question: Who is the lawyer? → **Nour**  
Solution: Yara — Hama, musician, 28; Tareq — Aleppo, engineer, 36; Nour — Latakia, lawyer, 24; Samer — Homs, doctor, 32  
Reveal: Nour is the lawyer. She's 24, and she's from Latakia. Tareq is an engineer from Aleppo, and Samer is a doctor from Homs.

**Crossword:** 5A footballer (Messi is a famous ___.); 7A name (What's your ___?); 8A businessman (Kareem is a ___.); 9A Chinese (Mei is ___, and her husband is Japanese.); 1D actor (Is he an ___? He's very famous!); 2D Australian (Hannah's husband is ___. He's from Sydney.); 3D Japanese (Kenji is ___. He's an engineer in Tokyo.); 4D Vietnamese (Pho is a ___ soup.); 6D Spanish (Lucía isn't ___. She's from Argentina.)  
**Word search:** Japanese, Polish, Brazilian, Chinese, Russian, British, Spanish, Irish, American, Italian

**Escape room — Locked in the Hejaz Railway Station.** You're in the Hejaz Railway Station in Damascus. It's late, and the big door isn't open! Open the locks. *Ending:* The door is open! You're free, and you aren't late for your train.  
- Lock 1 (Find the correct sentences) — code **136**: Are you a student? / I'm an musician. / Is he an actor? / Are Hadi from Bab Touma? / My friends isn't here. / How old are your children?
- Lock 2 (The number lock) — code **232**: "I bring food to tables in a restaurant." (1 an engineer / 2 a waiter / 3 a lawyer) / James ___ British. (1 am / 2 are / 3 is) / ___ she a lawyer? (1 Am / 2 Is / 3 Are)
- Lock 3 (Count the correct sentences) — code **3**: I is a police officer. / Is they Brazilian? / He isn't married. / She's a waiter. / He's a lawyer.
- Lock 4 (Count the correct sentences) — code **4**: They are Brazilian. / What is your name? / She's a doctor. / Ziad are a lawyer. / My father is an architect.

**What am I?** *doctor*: My coat is white. / I'm at a hospital all day. / I help sick people. · *waiter*: I'm on my feet all day, and I'm very fast. / I'm in a café or a restaurant. / I bring food to your table. · *footballer*: I'm in a team of eleven. / My shoes are very important for my job. / Messi is a famous one. · *tourist*: I'm not on business. / I'm in a new city with a map and a camera. / I'm on holiday in a different country. · *singer*: I'm on a stage. / My voice is my job. / Fairuz is a famous one. · *Japanese*: I'm a nationality. / Sushi is my food. / I'm from Tokyo or Osaka. · *police officer*: My car is blue and white, and it's very loud. / I'm in the street, and I'm here for you. / I work for the police. · *address*: I'm a number, a street and a town. / I'm on letters and parcels. / What's your …? — 12 Baghdad Street, Damascus.  
**Guess the word (targets):** actor, lawyer, doctor, singer, waiter, address, friend, really, married, single, student, name, tourist


#### Unit 2

**The case — Whose is the camera?** Four grandparents are at Hala's café today. Each one has got a different number of grandchildren and a different thing in his or her bag. Their houses are in four different parts of Damascus.  
1. The grandparent with four grandchildren has got a bottle of water.
2. Um Ziad's house is in Bab Touma.
3. Abu Firas hasn't got three grandchildren.
4. Um Ziad hasn't got a camera. *(red herring: true, not needed)*
5. Abu Omar has got two grandchildren.
6. The grandparent with a house in Kafr Sousa has got a packet of chewing gum.
7. Abu Firas has got a dictionary in his bag.
8. The grandparent with three grandchildren has got a house in Sarouja.

Question: Who has got the camera? → **Um Khaled**  
Solution: Abu Firas — five, dictionary, Midan; Um Khaled — three, camera, Sarouja; Abu Omar — two, chewing gum, Kafr Sousa; Um Ziad — four, bottle of water, Bab Touma  
Reveal: The camera is Um Khaled's. She's got three grandchildren, and her house is in Sarouja. Abu Firas has got five grandchildren — and a dictionary!

**Crossword:** 2A bag (My ___ is really heavy today!); 5A dictionary (Is that your ___?); 8A grandmother (My ___'s kitchen is lovely.); 10A grandparents (My ___ have got a house in Sarouja.); 11A interview (My job ___ is tomorrow.); 12A boyfriend (Her ___ is a doctor.); 1D coin (money made of metal); 3D glasses (My grandfather's ___ are on the table.); 4D key (Have you got your house ___?); 6D information (The ___ is on the website.); 7D here (Your keys are ___, on the table.); 9D husband (Mei's ___ is Japanese.)  
**Word search:** bag, key, camera, coin, photo, tissue, glasses, wallet, watch, boyfriend

**Escape room — Locked in the Azem Palace.** You're in an old room in the Azem Palace. You've got a key, but it isn't the right key — and the door isn't open! Open the locks. *Ending:* The door is open! Have you got your bag and your camera? Great. The palace garden is lovely!  
- Lock 1 (Find the correct sentences) — code **346**: They has got two sons. / These is my nephew. / She has got a camera. / My uncle's name is Mazen. / The childrens' room is small. / This is Maya's camera.
- Lock 2 (The number lock) — code **311**: Abu Salim and Um Ziad are Tala's ___. (1 uncles / 2 parents / 3 grandparents) / ___ woman is my aunt. (there) (1 That / 2 These / 3 Those) / My phone ___ got a good camera. (1 's / 2 've / 3 have)
- Lock 3 (Count the correct sentences) — code **3**: Whose keys are these? / Have you got a tissue? — Yes, I've got. / These are my glasses. / That is my car. / They're Kareems coins.
- Lock 4 (Count the correct sentences) — code **4**: My parents' house is in Midan. (two parents) / Hadi's wallet is black. / Is this your wallet? / These are my glass. They're new. / These are my keys.

**What am I?** *key*: I've got teeth, but I haven't got a mouth. / I'm small, and I'm metal. / I open the door of your house. · *glasses*: I've got two eyes, but I haven't got a face. / I'm on your grandfather's nose. / You wear me, and then the words in your book are clear. · *wallet*: I'm brown or black. / I'm in your pocket or your bag. / I've got your money and your credit cards in me. · *camera*: I've got one big eye. / I'm with you on holiday. / I take photos. · *dictionary*: I'm a book, but I haven't got a story. / I've got thousands of words in me. / Look in me for the meaning of a word. · *uncle*: I'm a man in your family. / My children are your cousins. / I'm your father's brother — or your mother's. · *grandmother*: I'm a woman in your family. / My grandchildren are my favourite people. / I'm your mother's mother — or your father's. · *coin*: I'm round and flat. / I'm metal, and I'm in your pocket. / I'm money, but I'm not paper.  
**Guess the word (targets):** camera, coin, photo, tissue, glasses, wallet, watch, husband, brother, mother, cousin, nephew, parents, uncle, here, lovely, there


#### Unit 3

**The case — Who goes to the cinema?** Maya, Jad, Dima and Tareq are friends. On Friday, they go to four different places in town at four different times. They live in different parts of Damascus.  
1. The trip to the swimming pool is at quarter past two.
2. Tareq: "I live in Mezzeh."
3. Jad: "I don't go at twenty past ten."
4. The friend from Jaramana goes at five o'clock.
5. Maya: "I don't live in Jaramana." *(red herring: true, not needed)*
6. The trip to the shopping centre is at half past one.
7. Dima: "I go at quarter past two."
8. The friend from Dummar goes to the street market.

Question: Who goes to the cinema? → **Jad**  
Solution: Maya — street market, twenty past ten, Dummar; Jad — cinema, five o'clock, Jaramana; Dima — swimming pool, quarter past two, Kafr Sousa; Tareq — shopping centre, half past one, Mezzeh  
Reveal: Jad goes to the cinema at five o'clock. He lives in Jaramana. Maya goes to the street market at twenty past ten, and Tareq goes to the shopping centre at half past one.

**Crossword:** 1A weekdays (I work on ___.); 4A lunchtime (The café is busy at ___.); 5A supermarket (The ___ is open until midnight.); 7A weekend (What do you do at the ___?); 8A midnight (Hadi finishes work at ___.); 2D afternoon (I study in the ___.); 3D restaurant (We eat at a ___ in Qassaa on Thursdays.); 5D study (I ___ law at Damascus University.); 6D town (Bloudan is a small ___ in the mountains.)  
**Word search:** study, cinema, evening, lunchtime, morning, midday, weekdays, midnight, open, weekend

**Escape room — Locked in the old hammam.** You're in an old hammam in the Old City. It's quarter to ten at night, and the door isn't open! Open the locks. *Ending:* The door is open! It's five to ten. You go home, have a cup of tea and go to bed.  
- Lock 1 (Find the correct sentences) — code **236**: Where you work? / I live with my parents. / Lunch is at half past one. / What time you get up? / They doesn't work on Friday. / Do you like it? — Yes, I do.
- Lock 2 (The number lock) — code **233**: Do they work in an office? — Yes, they ___. (1 work / 2 do / 3 are) / I want to see a film. (1 the supermarket / 2 the swimming pool / 3 the cinema) / I want to eat a meal with my friends. (1 a block of flats / 2 a swimming pool / 3 a restaurant)
- Lock 3 (Count the correct sentences) — code **1**: Are you study at university? / We don't have a car. / I get up at six and half. / I doesn't have breakfast. / It's half to three. (3:30)
- Lock 4 (Count the correct sentences) — code **3**: It's quarter to eight. (7:45) / It's ten to four. (4:10) / It's fifteen past two. (2:15) / The film starts at five to nine. (8:55) / It's twenty past ten. (10:20)

**What am I?** *cinema*: It's dark inside me. / People eat popcorn and sit in me for two hours. / You watch films here. · *midnight*: I'm the end of one day and the start of the next. / Cinderella runs home at me. / I'm twelve o'clock at night. · *weekend*: I'm only two days long. / Children love me — no school! / In Syria, I'm Friday and Saturday. · *supermarket*: I'm a big shop. / People push trolleys around me. / You buy food and things for the house here. · *village*: I've got one small school and a lot of trees. / Grandparents live here, and everyone knows everyone. / I'm a very small place in the countryside. · *swimming pool*: I'm blue, and I'm full of water. / You wear special clothes here. / You swim in me. · *morning*: I come before the afternoon. / People have breakfast in me. / I'm the first part of the day.  
**Guess the word (targets):** study, cinema, evening, morning, midday, open, weekend, start, town, village


#### Unit 4

**The case — Who loves cooking?** Reem, Maya, Fadi and Salma talk about their free time. Each friend loves a different activity and has a different job. They all go to concerts at the Opera House — but how often?  
1. The student often goes to concerts.
2. Reem doesn't like swimming.
3. The nurse loves cooking.
4. Fadi never goes to concerts. *(red herring: true, not needed)*
5. Maya loves dancing.
6. The person who loves cooking always goes to concerts.
7. Fadi is a taxi driver.
8. Reem sometimes goes to concerts.

Question: Who loves cooking? → **Salma**  
Solution: Reem — reading, sometimes, artist; Maya — dancing, often, student; Fadi — swimming, never, taxi driver; Salma — cooking, always, nurse  
Reveal: Salma loves cooking. She's a nurse, and she always goes to concerts. Fadi loves swimming, but he never goes to concerts.

**Crossword:** 1A usually (We ___ have lunch at two.); 6A sometimes (I ___ go swimming on Fridays.); 7A cooking (Um Khaled loves ___ for her neighbours.); 9A album (a collection of songs from one singer or band); 10A never (Fadi ___ cooks.); 2D swimming (Jad hates ___. He doesn't like water!); 3D dancing (Lina loves ___ — she's a dance teacher!); 4D win (to be first in a game or a competition); 5D nervous (Reem is ___ before exams.); 8D often (Maya ___ goes to concerts.)  
**Word search:** reading, cooking, dancing, swimming, always, never, often, sometimes, usually, album

**Escape room — Locked in the old library.** You love reading, so you often spend Friday afternoon in the old library. Today it's late, and the door isn't open! Open the locks. *Ending:* The door is open! You always have fun in the library — but next time, check the time!  
- Lock 1 (Find the correct sentences) — code **134**: They love going to concerts. / Do you like shoping? / She loves dancing. / Abu Omar has a shop. / He doesn't mind makeing mistakes. / Does he plays football?
- Lock 2 (The number lock) — code **222**: She hates ___ her email on Friday. (1 check / 2 checking / 3 checks) / (never) We go dancing. (1 We go dancing never never. / 2 We never go dancing. / 3 We go never dancing.) / Kareem ___ a fabric shop. (1 haves / 2 has / 3 have)
- Lock 3 (The password) — code **DOOR**: I love ___. (dance) / She goes to concerts — a lot. She ___ goes. / They go swimming three or four times a month. They ___ go swimming. / Do you like ___? (read)
- Lock 4 (Count the correct sentences) — code **2**: We hate cooking. / Does Maya play the guitar? / I like swim. / She doesn't likes cooking. / She hates watch sport.

**What am I?** *reading*: Your eyes go from left to right — or right to left in Arabic! / Reem does it every night. / You need a book or a newspaper. · *swimming*: Jad hates it. / You need a pool or the sea. / You do it in water. · *cooking*: Fadi never does it. / Um Khaled loves it — her kibbeh is famous! / You do it in the kitchen. · *dancing*: You don't need your hands — only your feet! / People usually do it at weddings. / You move your body to music. · *concert*: People buy tickets for me. / A band or a singer is on the stage. / I'm an event with live music. · *album*: I've got ten or twelve songs. / A singer makes a new one every year or two. / Fairuz has got a lot of these. · *never*: I'm the opposite of 'always'. / I'm 0%. / Fadi ___ cooks. Not once! · *nervous*: Your hands are cold, and your heart is fast. / Reem feels like this before exams. / You're worried and a bit afraid.  
**Guess the word (targets):** reading, cooking, dancing, always, never, often, usually, album, concert, nervous


#### Unit 5

**The case — Who can speak Spanish?** Four passengers are at Damascus airport. Each one has got a different destination and a different gate number. Each one can speak a different language, too.  
1. Kareem's destination is Istanbul.
2. The passenger at Gate 1 can't speak Turkish.
3. Ghada can speak French.
4. You can board the plane to Cairo at Gate 2.
5. Hala can't speak Russian. *(red herring: true, not needed)*
6. Dima's gate number is 4.
7. The passenger to Dubai can speak Spanish.
8. Ghada's gate number is 3.

Question: Who can speak Spanish? → **Dima**  
Solution: Ghada — Doha, French, Gate 3; Kareem — Istanbul, Russian, Gate 1; Dima — Dubai, Spanish, Gate 4; Hala — Cairo, Turkish, Gate 2  
Reveal: Dima can speak Spanish. Her destination is Dubai, and she can board the plane at Gate 4. Hala can speak Turkish, and her plane goes to Cairo.

**Crossword:** 1A drive a car (Can you ___?); 7A boarding pass (Can I see your ___, please?); 8A get on (___ the bus at the university.); 9A once a week (We visit my grandmother ___.); 10A fly (We ___ to Dubai once a year.); 2D ride a scooter (In Rome, a lot of people ___ to work.); 3D ride a bicycle (Joud can ___.); 4D twice a week (Hadi plays football ___.); 5D luggage (You can't take a lot of ___ on small planes.); 6D destination (Our ___ is Istanbul.); 8D get off (___ the bus at Marjeh Square.)  
**Word search:** bicycle, fly, luggage, screens, smoke, terminal, drive a car, get off, get on, take a bus

**Escape room — Locked on a train to Aleppo.** You're on a train to Aleppo. The train is at the station, but the door isn't open, and you can't get off! Open the locks. *Ending:* The door is open, and you can get off the train. Welcome to Aleppo!  
- Lock 1 (Find the correct sentences) — code **156**: She's an engineer. / I go to work by the bus. / He can speaks French. / Can you drive? — Yes, I do. / You can't smoke here. / I can ride a scooter.
- Lock 2 (The number lock) — code **323**: ___ airport in Damascus is south-east of the city. (1 A / 2 An / 3 The) / My grandmother can't ___ a car. (1 drives / 2 drive / 3 to drive) / You ___ the bus at the front door. (1 go in on / 2 get up / 3 get on)
- Lock 3 (Count the correct sentences) — code **2**: Can I took this bag? / The gate number is on your boarding pass. / There's an underground train in Paris. / She cans drive a car. / We go to the work by scooter.
- Lock 4 (Count the correct sentences) — code **2**: I've got a new car. The car is blue. / I love trains. (all trains) / Do you can swim? / We not can board yet. / Where's airport?

**What am I?** *bicycle*: I've got two wheels, but I haven't got an engine. / You can ride me to university. / You move me with your feet. · *luggage*: I'm heavy. / You give me to the person at the check-in desk. / I'm your bags and suitcases. · *boarding pass*: I'm a small piece of paper, or a picture on your phone. / Your seat and gate number are on me. / You can't board the plane without me. · *destination*: I'm at the end of your journey. / On your ticket, I come after 'To:'. / I'm the place you travel to. · *underground train*: I'm under the city. / In London, people call me 'the Tube'. / I'm a train under the ground. · *public transport*: I'm for everyone. / I'm cheap in Damascus. / I'm buses, trains and service taxis. · *screens*: We're on the walls at the airport. / We show flight information. / Look at us for your gate number.  
**Guess the word (targets):** bicycle, luggage, screens, smoke


#### Unit 6

**The case — Whose basket is yellow?** Four friends are at a picnic in the Ghouta. Each one has got a basket of a different colour. In each basket, there's some food and a drink.  
1. There's some tea in Um Khaled's basket.
2. There are some olives in the yellow basket.
3. There isn't any water in Rana's basket.
4. There are some biscuits in Hadi's basket.
5. There aren't any sandwiches in the blue basket. *(red herring: true, not needed)*
6. There's some water in the basket with the grapes.
7. Um Khaled's basket is red.
8. There's some coffee in the blue basket.

Question: Whose basket is yellow? → **Rana**  
Solution: Abu Omar — grapes, water, green; Um Khaled — sandwiches, tea, red; Rana — olives, orange juice, yellow; Hadi — biscuits, coffee, blue  
Reveal: The yellow basket is Rana's. There are some olives and some orange juice in it. In Abu Omar's green basket, there are some grapes and some water.

**Crossword:** 2A sandwich (I have a cheese ___ for lunch.); 5A receipt (Can I have a ___, please?); 7A biscuit (Have a ___ with your tea!); 8A vegetarian (Raj is ___. He loves mujaddara.); 9A delicious (This muhammara is ___!); 1D water (How much ___ do you drink every day?); 3D cappuccino (A ___, please — medium.); 4D tomato (a red fruit, used as a vegetable in salads); 6D olive (a small green or black fruit; it gives oil)  
**Word search:** apple, grape, sandwich, banana, tomato, biscuit, salad, water, rice, olive

**Escape room — Locked in a spice shop in Bzouriyah.** You're in a spice shop in Bzouriyah. There are a lot of herbs and spices here, but there isn't a key — and the door isn't open! Open the locks. *Ending:* The door is open! The owner is back, and there's some hot tea and a biscuit for you.  
- Lock 1 (Find the correct sentences) — code **245**: There isn't any eggs. / Are there any grapes? / There are any grapes. / How many biscuits are in the box? / There's some bread on the table. / Have there a knife?
- Lock 2 (The number lock) — code **232**: Can I have ___ banana? (1 an / 2 a / 3 some) / ___ there a vegetarian dish? (1 Are / 2 Has / 3 Is) / ___ there any olives? (1 Is / 2 Are / 3 Have)
- Lock 3 (Count the correct sentences) — code **2**: How much are the sandwich? / How many milk do you want? / There aren't any milk. / How many people are there? / There aren't any eggs.
- Lock 4 (Count the correct sentences) — code **2**: There is a café in the station. / We need some water. / How many apple do you want? / How much water you drink? / Is there some milk?

**What am I?** *banana*: There's a soft white fruit inside me. / Monkeys love me. / I'm long and yellow. · *olive*: There's a stone inside me. / There are thousands of us on one tree. / I'm green or black, and I give oil. · *receipt*: There are prices and numbers on me. / I'm a small piece of paper from the shop. / The cashier gives me to you after you pay. · *vegetarian*: I love mujaddara and fattoush. / There isn't any meat on my plate. / I don't eat meat or chicken. · *picnic*: There isn't a table — there's a blanket on the grass. / Sometimes there are ants! / I'm a meal outside, in the Ghouta or in a park. · *cappuccino*: I'm from Italy. / There's some milk and some foam in me. / I'm a coffee. · *sandwich*: There's some cheese or some falafel inside me. / I'm good for lunch at school or at work. / I'm two pieces of bread with food inside. · *tomato*: I'm a fruit, but people use me as a vegetable. / There's a lot of me in fattoush. / I'm red and round.  
**Guess the word (targets):** apple, grape, banana, tomato, biscuit, salad, water, rice, olive, picnic, receipt, change, medium, healthy, snack


#### Unit 7

**The case — Who collected postcards?** Yesterday, four grandparents talked about their lives at Hala's café. When they were children, they lived in four different cities, and each one collected different things. They got married in four different years.  
1. The person from Latakia got married in 1975.
2. Um Khaled collected photos.
3. Abu Salim's wedding wasn't in 1972. *(red herring: true, not needed)*
4. The stamp collector's wedding wasn't in 1981.
5. When Abu Firas was a child, he lived in Homs.
6. The person from Aleppo got married in 1978.
7. Abu Omar got married in 1981.
8. The child from Latakia collected coins.

Question: Who collected postcards? → **Abu Omar**  
Solution: Abu Firas — Homs, stamps, 1972; Um Khaled — Aleppo, photos, 1978; Abu Salim — Latakia, coins, 1975; Abu Omar — Hama, postcards, 1981  
Reveal: Abu Omar collected postcards. He lived in Hama when he was a child, and he got married in 1981. Abu Firas collected stamps — and later, he became a postman!

**Crossword:** 3A become (to start to be); 5A want (to wish to have or do); 8A journalist (Sami was a ___ in Beirut.); 10A study (to learn at school or university); 11A composer (Mozart was a famous ___.); 1D yesterday (I was at home ___.); 2D meet (to see a person, often for the first time); 4D start (to begin); 6D ago (I moved to Damascus five years ___.); 7D graduate (to finish university); 9D skater (The ___ won a gold medal.)  
**Word search:** ago, yesterday, become, love, make, composer, meet, decide, move, skater

**Escape room — Locked in the Citadel of Damascus.** This morning you visited the Citadel of Damascus. You walked into an old tower, and the door closed behind you! Now the door isn't open. Open the locks. *Ending:* You opened the door! It was a long day, but it was a fantastic adventure.  
- Lock 1 (Find the correct sentences) — code **456**: I saw her the yesterday. / He stoped the car. / In my last birthday, I was in Beirut. / She studied maths. / He left home at eighteen. / He took a lot of photos.
- Lock 2 (The number lock) — code **122**: He ___ his first knafeh at fourteen. (1 made / 2 make / 3 maked) / ___ your father a journalist? (1 Be / 2 Was / 3 Were) / Where ___ you born? (1 are / 2 were / 3 was)
- Lock 3 (Count the correct sentences) — code **4**: They got married on the fifth of May. / We weren't late. / They was at the market. / We travelled to Rome last summer. / I went to Cairo.
- Lock 4 (Count the correct sentences) — code **2**: Yesterday it is very hot. / She becomed a teacher. / She graduated last year. / My grandparents was farmers. / I wanted to be a pilot.

**What am I?** *composer*: I wrote, but not books. / Mozart and Beethoven were famous ones. / I'm a person who writes music. · *journalist*: I asked a lot of questions yesterday. / Then I wrote a story about it. / I write for a newspaper or a website. · *skater*: I moved very fast, and it was very cold. / I won a gold medal on the ice. / I move on ice with special shoes. · *yesterday*: Tomorrow, today becomes me. / I was here, but now I'm in the past. / I'm the day before today. · *last summer*: It was hot, and the children weren't at school. / Maybe you went to the beach then. / I'm the summer before this one. · *this morning*: I started when you woke up today. / You had breakfast in me. / I'm the first part of today.  
**Guess the word (targets):** become, love, make, meet, decide, move, skater, start, study, take, want, work


### A2.2 Practice


#### Unit 8

**The case — Who saw the frightening film?** Last week, Hadi, Maya, Jad and Dima went to the cinema on different days: Thursday, Friday, Saturday and Sunday. Each friend saw a different film. One film was boring, one was enjoyable, one was frightening and one was slow.  
1. Dima went to the cinema on Sunday.
2. Maya saw the comedy.
3. Hadi didn't go on Friday. *(red herring: true, not needed)*
4. The action film was on Thursday.
5. Jad didn't see the action film.
6. Maya's film was enjoyable.
7. The film on Saturday was frightening.
8. The romance was slow.

Question: Who saw the frightening film? → **Jad**  
Solution: Hadi — action film, Thursday, boring; Maya — comedy, Friday, enjoyable; Jad — sci-fi film, Saturday, frightening; Dima — romance, Sunday, slow  
Reveal: Jad saw the sci-fi film on Saturday. It was frightening — he didn't sleep that night! Hadi saw the action film on Thursday, but it was boring.

**Crossword:** 1A boring (The film was long and ___.); 4A frightening (The film was so ___ — I didn't sleep!); 6A serious (It was a ___ film about the war.); 8A band (My cousin plays in a ___.); 9A audience (The ___ loved the concert.); 2D guitarist (The ___ was only eighteen.); 3D enjoyable (It was a very ___ evening.); 5D romantic (They watched a ___ film for Valentine's Day.); 6D slow (The play was very ___.); 7D sad (The end of the book was very ___.)  
**Word search:** happy, boring, enjoyable, romantic, exciting, sad, serious, slow, funny, audience

**Escape room — Locked in the old cinema.** You're in an old cinema in Damascus. The film finished an hour ago and everyone went home, but the door isn't open! Open the locks. *Ending:* The door is open! The film wasn't frightening, but that was! Let's go out for dinner.  
- Lock 1 (Find the correct sentences) — code **126**: They didn't go to the concert. / Where did you go? / The film didn't funny. / Did they like it? — Yes, they liked. / Did the concert good? / Did you go out last night?
- Lock 2 (The number lock) — code **232**: We ___ go to the theatre. We went to the cinema. (1 don't / 2 didn't / 3 weren't) / It was about war and history. It was very ___. (1 romantic / 2 funny / 3 serious) / How ___ the concert? (1 were / 2 was / 3 did)
- Lock 3 (Count the correct sentences) — code **3**: I wasn't at home. / He didn't see the end of the film. / Did you see the film? / She don't like the film yesterday. / I didn't went to the party.
- Lock 4 (Count the correct sentences) — code **2**: What did you do yesterday? / We weren't late. / Who you met at the party? / How did the musical? / We didn't watched TV.

**What am I?** *drummer*: I'm in a band, but I don't sing. / I sit at the back of the stage, and I'm very loud. / I play the drums. · *audience*: I didn't play or sing, but I bought a ticket. / I sit in the dark and I watch the show. / I'm all the people at a concert, and I clap at the end. · *comedy*: I'm a kind of film or play. / People don't cry when they watch me — only when they laugh! / I'm very funny. · *sci-fi film*: I'm a story, but I'm not about the past. / There are spaceships and robots in me. / Star Wars is a famous example of me. · *guitarist*: I'm in a band, but I'm not the lead singer. / I didn't learn the drums. I learned an instrument with six strings. / I play the guitar. · *historical film*: I'm a kind of film. / I'm about kings, queens and wars from long ago. / The film about Saladin is an example of me. · *frightening*: I'm an adjective for a film or a story. / People close their eyes when they watch me. / After a film like me, you don't sleep! I make you afraid.  
**Guess the word (targets):** happy, boring, serious, slow, funny, band, perform, comedy, romance, drummer


#### Unit 9

**The case — Which shop is the cheapest?** Abu Firas, Ghada, Walid and Salma have shops in four different parts of Damascus. Each shop is famous for one thing: one is the cheapest, one is the busiest, one is the oldest and one is the most modern.  
1. Abu Firas's shop is in Midan.
2. Ghada has the gift shop.
3. Abu Firas doesn't have the shoe shop. *(red herring: true, not needed)*
4. The gift shop is in Bab Touma.
5. Salma's shop is the most modern.
6. The shop in Sha'lan is the cheapest.
7. The baker's is the busiest shop.
8. The bookshop isn't in Malki.

Question: Which shop is the cheapest? → **the bookshop**  
Solution: Abu Firas — the baker's, Midan, the busiest; Ghada — the gift shop, Bab Touma, the oldest; Walid — the bookshop, Sha'lan, the cheapest; Salma — the shoe shop, Malki, the most modern  
Reveal: The bookshop is the cheapest — Walid sells second-hand books in Sha'lan. The baker's in Midan is the busiest, and Ghada's gift shop in Bab Touma is the oldest.

**Crossword:** 3A pretty (What a ___ necklace!); 5A fashionable (Those trainers are very ___.); 7A pharmacy (Nour works in a ___.); 10A sunglasses (I need new ___ for the beach.); 1D cheap (not expensive); 2D expensive (Gold is very ___.); 4D economical (Small cars are more ___.); 6D busy (with a lot of people); 8D fast (quick); 9D new (My phone is ___.)  
**Word search:** cheap, old, powerful, pretty, expensive, stylish, fast, unusual, bookshop, pharmacy

**Escape room — Locked in the spice shop in Bzouriyah.** You're in the oldest spice shop in Bzouriyah. It smells better than a garden, but the door isn't open! Open the locks. *Ending:* The door is open! That was the most exciting shopping trip of your life.  
- Lock 1 (Find the correct sentences) — code **234**: These are expensives shoes. / That was the worst meal. / Damascus is bigger than Homs. / He's the tallest in the class. / This app is easyer to use. / This phone is more cheaper than that one.
- Lock 2 (The number lock) — code **123**: You want a new novel. (1 the bookshop / 2 the butcher's / 3 the optician's) / You need new glasses. (1 the pharmacy / 2 the optician's / 3 the dry-cleaner's) / It's new and up to date. It's ___. (1 old / 2 second-hand / 3 modern)
- Lock 3 (Count the correct sentences) — code **4**: It's a use easy app. / My bag is bigger than yours. / I want a cheap phone. / It's an unusual gift. / It was the best day of my life.
- Lock 4 (Count the correct sentences) — code **2**: It's a bag stylish. / He's taller than his father. / They're very fashionable. / This café is gooder than the old one. / This is the expensivest watch.

**What am I?** *pharmacy*: I'm a shop, but I don't sell clothes or food. / When you're ill, you visit me with a paper from the doctor. / I sell medicine. · *sunglasses*: I'm darker than normal glasses. / You wear me on the beach in Latakia in summer. / I protect your eyes from the sun. · *bookshop*: I'm quieter than a café. / Reem spends hours in me. / I sell novels, dictionaries and poems. · *department store*: I'm bigger than a normal shop. / I sell clothes, perfume, toys and furniture on different floors. / Harrods in London is the most famous one. · *post office*: People visit me less than in the past — now they send emails. / You buy stamps here. / You send letters and parcels from me. · *second-hand*: I'm not new, but I'm not always old. / Another person had me before you. / Clothes like me are cheaper than new clothes. · *expensive*: Gold, diamonds and big cars are like me. / Your wallet isn't happy when a thing is like me. / I'm the opposite of cheap.  
**Guess the word (targets):** cheap, pretty, stylish, fast, unusual, busy, cool, popular, famous, high, tall, modern


#### Unit 10

**The case — Who is wearing a suit?** It's Saturday afternoon. Hala, Samer, Reem and Fadi are out in Sha'lan, but they aren't together. Each friend is doing something different and wearing different clothes — and they're very different people, too.  
1. Hala is having lunch.
2. Reem is wearing a baseball cap.
3. Samer is wearing shorts.
4. The person in the suit is having a haircut.
5. Fadi isn't playing football. *(red herring: true, not needed)*
6. The person who is buying trainers is shy.
7. The person in shorts is very bossy.
8. The person in the suit isn't cheerful.

Question: Who is wearing a suit? → **Fadi**  
Solution: Hala — a green jumper, having lunch, cheerful; Samer — shorts, playing football, bossy; Reem — a baseball cap, buying trainers, shy; Fadi — a suit, having a haircut, confident  
Reveal: Fadi is wearing a suit. He's having a haircut because he has an interview on Monday! Samer is playing football in his shorts, and he's telling everyone what to do.

**Crossword:** 2A jacket (Take a ___ — it's cold in Bloudan.); 6A tie (Ziad wears a ___ at work.); 7A appointment (I have an ___ at the hairdresser's at four.); 8A skirt (Rana is wearing a long blue ___.); 9A suit (Kareem is wearing a grey ___ today.); 10A friendly (The people in Midan are really ___.); 1D sociable (Hala is very ___. She knows everyone.); 3D confident (Maya is very ___ on stage.); 4D shorts (Kids wear ___ in summer.); 5D determined (Reem is ___ to become a doctor.); 9D shy (Joud is ___ with new people.)  
**Word search:** skirt, suit, dress, jacket, tie, jeans, trainers, jumper, shirt, trousers

**Escape room — Locked in the Azem Palace.** You're visiting the Azem Palace, and you're looking at old party costumes. Everyone is leaving, but the door isn't open! Open the locks. *Ending:* The door is open! The sun is shining and the guard is smiling at you.  
- Lock 1 (Find the correct sentences) — code **136**: Have you got a larger size? / I want to buy a jean. / I'm wearing a suit. / He's runing in the park. / I'm knowing the answer. / Do you like my costume?
- Lock 2 (The number lock) — code **111**: We ___ lunch at the moment. Call me later! (1 're having / 2 have / 3 has) / (look!) (1 Look! It's raining. / 2 Look! It rains. / 3 Look! It raining.) / What ___ you doing at the moment? (1 are / 2 do / 3 does)
- Lock 3 (Count the correct sentences) — code **4**: She's wearing a skirt. / These trousers are too long. / He's wearing trainers. / It's too much big. / They're going to the shops now.
- Lock 4 (Count the correct sentences) — code **3**: They are playing football. / He wants a new jacket. / She's wearing a red dress today. / My jeans is new. / I am usually wearing jeans.

**What am I?** *tie*: I'm long and thin. / Men wear me with a shirt at work or at weddings. / I go round your neck. · *uniform*: I'm the same for a lot of people. / Nurses, police officers and pilots wear me at work. / Students at school in Syria wear me every day. · *jewellery*: I'm small, but I'm sometimes very expensive. / Dima loves wearing me. / Rings, necklaces and earrings are all me. · *trainers*: I'm more comfortable than smart shoes. / People run and play football in me. / I'm sports shoes. · *baseball cap*: I'm from America, but you see me everywhere. / I protect your eyes from the sun, but I'm not sunglasses. / I'm a soft hat with a peak at the front. · *bossy*: I'm an adjective for a person — not a nice one. / Big sisters are sometimes like me! / I'm always telling other people what to do. · *jumper*: I'm warm and soft. / Grandmothers often make me with wool. / You wear me on top in winter.  
**Guess the word (targets):** skirt, suit, dress, jacket, jeans, jumper, shirt, shorts, bossy, uniform


#### Unit 11

**The case — Who saw a snake?** Last year, Abu Omar, Layla, Tareq and Nour went on trips in nature in Syria. Each friend went to a different place in a different month. Each friend saw a different animal there.  
1. Abu Omar went on his trip in April.
2. Layla went to the beach.
3. Nour saw a donkey.
4. Layla didn't see a horse. *(red herring: true, not needed)*
5. The person who saw a snake travelled in October.
6. The person who went to the beach saw a dog.
7. The trip to the lake was in June.
8. The trip to the desert wasn't in April.

Question: Who saw a snake? → **Tareq**  
Solution: Abu Omar — the forest, a horse, April; Layla — the beach, a dog, August; Tareq — the desert, a snake, October; Nour — the lake, a donkey, June  
Reveal: Tareq saw a snake in the desert in October — and it was a big one! Abu Omar went to the forest in April, and he saw a beautiful horse. Nour saw a donkey at the lake in June.

**Crossword:** 3A pets (Do you have any ___?); 4A volcano (Vesuvius is a ___ in Italy.); 5A sea (Latakia is on the Mediterranean ___.); 8A chimpanzee (an intelligent African animal, similar to a monkey); 9A rat (There was a ___ in the kitchen!); 11A kilogram (A ___ of apples, please.); 1D dog (Sven's ___ is very friendly.); 2D lake (___ Qattinah is near Homs.); 3D population (What's the ___ of Damascus?); 6D elephant (An ___ weighs about 6,000 kilograms.); 7D ocean (The Pacific is the biggest ___.); 10D fish (There are a lot of ___ in the Orontes.)  
**Word search:** camel, fish, horse, dog, llama, dolphin, rat, snake, donkey, elephant

**Escape room — Locked in the Citadel of Damascus.** You're in the Citadel of Damascus. How old is it? About a thousand years! The big door isn't open. Open the locks. *Ending:* The door is open! There are a lot of birds in the sky over the old city. You're free!  
- Lock 1 (Find the correct sentences) — code **256**: How much trees are there? / We haven't got much time. / How long is Beirut from Damascus? / Two thousands people came. / I've got a few friends in Toronto. / Who took this photo?
- Lock 2 (The number lock) — code **212**: ___ people live in the city? (1 How long / 2 How many / 3 How much) / ___ is a giraffe? — About five metres. (1 How tall / 2 How many / 3 How far) / There's ___ snow on Mount Hermon in winter. (1 a few / 2 a lot of / 3 many)
- Lock 3 (Count the correct sentences) — code **1**: About eight billions people live in the world. / It's five hundred five kilometres. / The baby weighed three point five kilos. / The river is two points five kilometres wide. / How fast is a giraffe? — Five metres.
- Lock 4 (Count the correct sentences) — code **2**: There isn't much rain. / Why camels have humps? / There are a little camels. / There are five million people. / Ten thousands tourists visit every year.

**What am I?** *camel*: I can walk for days without water. / I have one or two humps. / People ride me in the desert. · *dolphin*: I'm very intelligent, and I talk with clicks and whistles. / You can see me near Arwad in summer. / I'm a friendly sea animal, and I jump out of the water. · *whale*: I'm not a fish, but I live in the sea. / I'm bigger than a bus — much bigger! / I'm the biggest animal in the world. · *volcano*: I'm a mountain, but I'm not a normal mountain. / Vesuvius and Etna are examples of me. / Sometimes fire and hot rock come out of me. · *desert*: I'm very dry, and there isn't much rain. / There aren't many trees, but there's a lot of sand. / Camels walk across me for days. · *elephant*: I weigh about six thousand kilograms. / I have very big ears. / I'm the biggest land animal, and I have a very long nose. · *river*: I'm always moving, but I don't have legs. / The Barada, the Euphrates and the Orontes are examples of me. / I'm water that goes across the land to the sea.  
**Guess the word (targets):** camel, fish, horse, llama, dolphin, snake, donkey, whale, beach, ocean, desert, river, forest, valley, lake, volcano, metre, pets


#### Unit 12

**The case — Who is going to hire a band?** Walid, Ghada, Salma and Jad are going to have parties this year — a different party in a different season. Each friend has a different plan for the big day.  
1. Ghada's party is going to be in winter.
2. Jad is going to have his party in autumn.
3. Salma is going to have a graduation party.
4. Ghada isn't going to have a leaving party. *(red herring: true, not needed)*
5. The leaving party is going to be in summer.
6. The person with the wedding party is going to decorate the house.
7. The person with the winter party would like to decorate the table.
8. Walid isn't going to make traditional food.

Question: Who is going to hire a band? → **Walid**  
Solution: Walid — a leaving party, hire a band, summer; Ghada — a birthday party, decorate the table, winter; Salma — a graduation party, make traditional food, spring; Jad — a wedding party, decorate the house, autumn  
Reveal: Walid is going to hire a band for his leaving party in summer — he's going to work in Dubai. Ghada is going to decorate the table for her birthday party in winter, and Salma is going to make traditional food for her graduation party.

**Crossword:** 3A cloudy (It's ___, but it isn't raining.); 5A campsite (We're going to stay at a ___ near Kasab.); 8A cold (It's very ___ in January.); 9A wet (It's ___ today — take an umbrella.); 10A winter (It snows on Qasioun in ___ — sometimes!); 11A foggy (It was ___ on the motorway this morning.); 1D icy (The roads are ___ in Bloudan.); 2D summer (We go to the beach in ___.); 4D raining (It's ___. Take an umbrella!); 6D snowing (It's ___ in Bloudan!); 7D hot (It's really ___ in July.); 9D warm (Spring in Damascus is ___.)  
**Word search:** snowing, autumn, sunny, cloudy, warm, wet, cold, windy, cool, foggy

**Escape room — Locked in the courtyard house.** You're in an old courtyard house in Damascus. Your family is going to have a big party here tonight, but the door isn't open! Open the locks. *Ending:* The door is open! Now we're going to decorate the house and make a cake. Would you like a glass of jallab?  
- Lock 1 (Find the correct sentences) — code **123**: Do you want to come? / We're going to decorate the house. / I'd like a coffee, please. / They is going to hire a band. / Do you like to come to my party? / The weather is sun.
- Lock 2 (The number lock) — code **223**: ___ she going to take part in the parade? (1 Does / 2 Is / 3 Are) / There are a lot of clouds. It's ___. (1 dry / 2 cloudy / 3 sunny) / Let's ___ a cake for Mum's birthday. (1 do / 2 hire / 3 make)
- Lock 3 (Count the correct sentences) — code **1**: It's going to rain. / Today is very cloud. / I'd like go to the festival. / Would you like to come? — Yes, I'd love it. / It snow in Bloudan in winter.
- Lock 4 (Count the correct sentences) — code **3**: It's raining now. / Would you like to come? / Do you going to dress up? / He's not going to comes. / It's very windy on the corniche.

**What am I?** *autumn*: Children go back to school in me. / The leaves go yellow and fall from the trees. / I come after summer and before winter. · *foggy*: Drivers would like to see more on days like me. / You can't see far, and the motorway is dangerous. / There's a lot of fog. · *campsite*: I'm a place to stay, but I'm not a hotel. / There's one near Kasab, in the forest. / You sleep in a tent here. · *birthday party*: I happen once a year for everyone. / Friends sing a song and bring presents. / There's a cake with candles — how old are you? · *accommodation*: Before a trip, you'd like to find me — and not too expensive! / I'm a long word for a place to stay. / Hotels, flats and campsites are all examples of me. · *winter*: Sometimes it snows on Qasioun in me. / I'm the coldest season. / I come after autumn. · *windy*: Hats fly away on days like me. / It's a good day to fly a kite. / There's a lot of wind.  
**Guess the word (targets):** snowing, autumn, sunny, cloudy, warm, cold, windy, cool, foggy, spring, summer, winter, raining


#### Unit 13

**The case — Who has to go to an interview?** Samer, Fadi, Lina and Yara study at four different universities in Syria. This week, each student has to do one important thing.  
1. Samer studies in Aleppo.
2. Yara studies economics.
3. Lina has to do a course.
4. The engineering student studies in Damascus.
5. The student in Damascus has to pass an exam.
6. Lina doesn't have to apply for a job. *(red herring: true, not needed)*
7. The student in Homs has to apply for a job.
8. The medicine student doesn't have to go to an interview.

Question: Who has to go to an interview? → **Samer**  
Solution: Samer — law, Aleppo, go to an interview; Fadi — engineering, Damascus, pass an exam; Lina — medicine, Latakia, do a course; Yara — economics, Homs, apply for a job  
Reveal: Samer has to go to an interview. He studies law in Aleppo, and he might get a job with a big company! Fadi has to pass an engineering exam in Damascus, and Lina has to do a course in Latakia.

**Crossword:** 6A engineering (Firas has a degree in ___.); 7A law (Ziad studied ___. Now he's a lawyer.); 8A history (___ is my favourite subject.); 1D science (___ was Ghada's best subject at school.); 2D languages (I'd like to study ___.); 3D literature (Reem loves ___ — she reads every day.); 4D medicine (Layla is studying ___ at Damascus University.); 5D geography (In ___, we learned about deserts.)  
**Word search:** law, economics, maths, geography, medicine, history, languages, science, train to be, do a course

**Escape room — Locked in the old library.** You're in the old library. You have to find a book for your exam, but now the door isn't open! Open the locks. *Ending:* The door is open! You don't have to stay here all night. You'll pass your exam tomorrow!  
- Lock 1 (Find the correct sentences) — code **236**: Does you have to wear a uniform? / They have to pass an exam. / I won't forget. / It mights rain. / I will to go to university. / He doesn't have to wear a tie.
- Lock 2 (The number lock) — code **311**: "I want to work in a hotel." (1 law / 2 science / 3 leisure and tourism) / Salma ___ to be a nurse. (1 trained / 2 applied / 3 earned) / I don't know. I ___ do a course this summer. (1 might / 2 'll definitely / 3 won't)
- Lock 3 (Count the correct sentences) — code **3**: I have to study. / I might study law. / They won't to be late. / She has to work at night. / She wills pass the exam.
- Lock 4 (Count the correct sentences) — code **1**: She might not to come. / Does she have to work on Friday? / He might comes tomorrow. / We haven't to pay. / I have study tonight.

**What am I?** *geography*: You might learn about the weather in me. / Maps are very important in me. / I'm the subject about countries, mountains and rivers. · *maths*: Engineers have to be good at me. / Calculators are useful in me. / In me, two and two are four. · *history*: Saladin, the Romans and the Umayyads are all in me. / You have to remember a lot of dates in me. / I'm the study of the past. · *medicine*: You have to study me for six years. / Layla studies me at Damascus University. / I'm the subject for future doctors. · *law*: Judges know me very well. / I'm the study of the rules of a country. / You have to study me to be a lawyer. · *literature*: Nizar Qabbani and Shakespeare are in me. / Reem loves me — she reads every day. / I'm the study of novels, poems and plays. · *languages*: You might need me for a job in another country. / In me, you learn new words every day. / English, French, Arabic and Turkish are all me.  
**Guess the word (targets):** maths, history, science


#### Unit 14

**The case — Who has uploaded photos?** It's two o'clock. Abu Salim, Um Khaled, Kareem and Rana are in different places, and each person has used a different device so far today. Each person has done one thing with it.  
1. Abu Salim has left a voice message.
2. Kareem is on a train.
3. Rana has used an old mobile phone.
4. The person on the train has used a laptop.
5. Um Khaled hasn't sent an email. *(red herring: true, not needed)*
6. The person with the tablet computer has uploaded photos.
7. The person at work has made a phone call.
8. The person with the smartphone isn't at home.

Question: Who has uploaded photos? → **Um Khaled**  
Solution: Abu Salim — a smartphone, left a voice message, in a café; Um Khaled — a tablet computer, uploaded photos, at home; Kareem — a laptop, sent an email, on a train; Rana — an old mobile phone, made a phone call, at work  
Reveal: Um Khaled has uploaded photos from her tablet computer at home — photos of her grandchildren, of course! Kareem has sent an email from his laptop on the train, and Abu Salim has left a voice message from a café.

**Crossword:** 1A landline (My grandparents still use a ___.); 5A laptop (Have you charged your ___?); 6A virus (My laptop has got a ___.); 7A smartphone (Have you ever lost your ___?); 8A upload (to send files from your computer to the internet); 2D apologise (to say sorry); 3D username (My ___ is reem_reads.); 4D password (Don't tell anyone your ___!)  
**Word search:** landline, laptop, password, upload, download, username, hacker, virus, apologise, be on hold

**Escape room — Locked in the Hejaz Railway Station.** You're in the old Hejaz Railway Station. You've missed your train, and now the door isn't open! Open the locks. *Ending:* The door is open! You've done it. Send a text message to your friends: you're free!  
- Lock 1 (Find the correct sentences) — code **146**: I've written a lot of messages. / We hasn't had any emails today. / Did you uploaded the photos? / Has she ever written a poem? / I have send three emails. / Have you ever lost your phone?
- Lock 2 (The number lock) — code **312**: She's ___ two coffees so far today. (1 drinking / 2 drink / 3 drunk) / A program that damages computers: (1 a virus / 2 a hotspot / 3 anti-virus software) / Have you ever ___ a wrong number? (1 dial / 2 dialled / 3 dialling)
- Lock 3 (Count the correct sentences) — code **3**: They have never saw snow. / She has made two calls. / I've being to Dubai twice. / He's forgotten his password. / I've never been to London.
- Lock 4 (Count the correct sentences) — code **4**: She's never been to Japan. She'd like to go. / Have he ever met a hacker? / Have you seen my phone? / They have downloaded the app. / Have you ever used video chat?

**What am I?** *password*: I'm a secret, and I'm often a mix of letters and numbers. / Never tell anyone — not even your best friend! / You type me to open your online account. · *hacker*: I've never met you, but I know a lot about you. / I've stolen a lot of passwords. / I get into other people's computers. · *virus*: I'm very small, and nobody wants me. / I've damaged a lot of computers. / Your laptop has got me, and now it's very slow. · *landline*: I've lived in your grandparents' house for years. / I have a wire, so I can't go out with you. / I'm a phone at home, not a mobile. · *smartphone*: Have you ever lost me? A lot of people have! / I take photos, play music and use the internet. / I'm a mobile phone, but I'm very clever. · *username*: I'm not your real name, but websites know you by me. / reem_reads is an example of me. / You type me with your password. · *download*: You've done me a lot of times: apps, films, music… / With me, files come from the internet to your computer. / I'm the opposite of upload.  
**Guess the word (targets):** laptop, upload, hacker, virus

<!-- /AUTO:puzzles -->

## (c) Gate results (last full build)

<!-- AUTO:gates -->
```
Font: Nunito downloaded from Google Fonts at build time
warn a12u11: balloon has too little data; offered builder instead

A1.1 Practice: 6 units, 1918 scored items (U1 381, U2 324, U3 305, U4 320, U5 312, U6 276), 58 level-review items, 52 Arabic lines, 0.93 MB; reading words {1: 53, 2: 61, 3: 77, 4: 87, 5: 91, 6: 98}; places mix Damascus 47% / Syria 21% / world 32% ({'damascus': 285, 'syria': 125, 'world': 196})
A1.2 Practice: 6 units, 1707 scored items (U7 325, U8 316, U9 338, U10 240, U11 224, U12 264), 60 level-review items, 47 Arabic lines, 0.88 MB; reading words {7: 110, 8: 115, 9: 107, 10: 107, 11: 110, 12: 118}; places mix Damascus 34% / Syria 34% / world 32% ({'damascus': 78, 'syria': 78, 'world': 75})
A2.1 Practice: 7 units, 2073 scored items (U1 302, U2 294, U3 298, U4 288, U5 254, U6 300, U7 337), 56 level-review items, 67 Arabic lines, 0.98 MB; reading words {1: 107, 2: 116, 3: 124, 4: 124, 5: 123, 6: 126, 7: 128}; places mix Damascus 53% / Syria 18% / world 29% ({'damascus': 155, 'syria': 53, 'world': 85})
A2.2 Practice: 7 units, 2147 scored items (U8 310, U9 322, U10 319, U11 291, U12 340, U13 275, U14 290), 56 level-review items, 76 Arabic lines, 1.04 MB; reading words {8: 147, 9: 158, 10: 141, 11: 157, 12: 152, 13: 138, 14: 208}; places mix Damascus 48% / Syria 29% / world 23% ({'damascus': 142, 'syria': 85, 'world': 67})
ok  [browser] A1.1 Practice.html: 214 views at 390×844 (247 sets opened in the player), 204 views at 360×740, 138 views at 1920×1080 class mode (zoom 1.75); parity 13; scoring on 25 sets + unit test; B1 "Are you a student?"; B3 pile; B4 single count; B7 22 Falling Words frames; B8/B9 Escape finished; 24 puzzles solved; Arabic toggle; reload kept 25 set scores; v1 progress: 50 items, 4 sets, 2 words kept; storage-blocked run clean
ok  [browser] A1.2 Practice.html: 212 views at 390×844 (227 sets opened in the player), 200 views at 360×740, 138 views at 1920×1080 class mode (zoom 1.75); parity 13; scoring on 25 sets + unit test; B1 "I always go to bed at eleven."; B3 pile; B4 single count; B7 22 Falling Words frames; B8/B9 Escape finished; 24 puzzles solved; Arabic toggle; reload kept 25 set scores; v1 progress: 50 items, 4 sets, 2 words kept; storage-blocked run clean
ok  [browser] A2.1 Practice.html: 250 views at 390×844 (280 sets opened in the player), 240 views at 360×740, 161 views at 1920×1080 class mode (zoom 1.75); parity 13; scoring on 23 sets + unit test; B1 "I am a police officer."; B3 pile; B4 single count; B7 26 Falling Words frames; B8/B9 Escape finished; 28 puzzles solved; Arabic toggle; reload kept 23 set scores; v1 progress: 49 items, 4 sets, 2 words kept; storage-blocked run clean
ok  [browser] A2.2 Practice.html: 254 views at 390×844 (290 sets opened in the player), 244 views at 360×740, 161 views at 1920×1080 class mode (zoom 1.75); parity 13; scoring on 24 sets + unit test; B1 "I didn't go to the party."; B3 pile; B4 single count; B7 20 Falling Words frames; B8/B9 Escape finished; 28 puzzles solved; Arabic toggle; reload kept 24 set scores; v1 progress: 48 items, 4 sets, 2 words kept; storage-blocked run clean
browser smoke test: passed

RESULT: ALL GATES PASSED
```
<!-- /AUTO:gates -->

## (d) Screenshots and page heights

Before = the round-1 apps; after = round 2 (A1.1, Unit 1 or 2). Phone shots are full pages.

| Screen | Before, phone | Before, Class mode | After, phone 390×844 | After, Class mode 1920×1080 |
|---|---|---|---|---|
| home | [before](docs/screens/before/home-390.png) | [before](docs/screens/before/home-1920.png) | [after](docs/screens/after/home-390.png) | [after](docs/screens/after/home-1920.png) |
| unit | [before](docs/screens/before/unit-390.png) | [before](docs/screens/before/unit-1920.png) | [after](docs/screens/after/unit-390.png) | [after](docs/screens/after/unit-1920.png) |
| setlist | [before](docs/screens/before/setlist-390.png) | [before](docs/screens/before/setlist-1920.png) | [after](docs/screens/after/setlist-390.png) | [after](docs/screens/after/setlist-1920.png) |
| player-question | — (new) | — (new) | [after](docs/screens/after/player-question-390.png) | [after](docs/screens/after/player-question-1920.png) |
| player-checked | — (new) | — (new) | [after](docs/screens/after/player-checked-390.png) | [after](docs/screens/after/player-checked-1920.png) |
| grammar | [before](docs/screens/before/grammar-390.png) | [before](docs/screens/before/grammar-1920.png) | [after](docs/screens/after/grammar-390.png) | [after](docs/screens/after/grammar-1920.png) |
| reading | [before](docs/screens/before/reading-390.png) | [before](docs/screens/before/reading-1920.png) | [after](docs/screens/after/reading-390.png) | [after](docs/screens/after/reading-1920.png) |
| game | [before](docs/screens/before/game-390.png) | [before](docs/screens/before/game-1920.png) | [after](docs/screens/after/game-390.png) | [after](docs/screens/after/game-1920.png) |
| test | [before](docs/screens/before/test-390.png) | [before](docs/screens/before/test-1920.png) | [after](docs/screens/after/test-390.png) | [after](docs/screens/after/test-1920.png) |
| puzzle-case | — (new) | — (new) | [after](docs/screens/after/puzzle-case-390.png) | [after](docs/screens/after/puzzle-case-1920.png) |
| puzzle-words | — (new) | — (new) | [after](docs/screens/after/puzzle-words-390.png) | [after](docs/screens/after/puzzle-words-1920.png) |
| puzzle-escape | — (new) | — (new) | [after](docs/screens/after/puzzle-escape-390.png) | [after](docs/screens/after/puzzle-escape-1920.png) |
| puzzle-guess | — (new) | — (new) | [after](docs/screens/after/puzzle-guess-390.png) | [after](docs/screens/after/puzzle-guess-1920.png) |

<!-- AUTO:heights -->
| Screen (A1.1 → A2.2) | Before (px) | After (px) | After ÷ 844 |
|---|---|---|---|
| A1.1 game | 844 | 844 | 1.0 |
| A1.1 grammar | 7675 | 2202 | 2.6 |
| A1.1 home | 2620 | 1313 | 1.6 |
| A1.1 player-checked | — | 844 | 1.0 |
| A1.1 player-question | — | 844 | 1.0 |
| A1.1 puzzle-case | — | 1496 | 1.8 |
| A1.1 puzzle-escape | — | 1275 | 1.5 |
| A1.1 puzzle-guess | — | 1256 | 1.5 |
| A1.1 puzzle-words | — | 1985 | 2.4 |
| A1.1 reading | 2352 | 844 | 1.0 |
| A1.1 setlist | 22252 | 1731 | 2.1 |
| A1.1 test | 4484 | 844 | 1.0 |
| A1.1 unit | 844 | 1581 | 1.9 |
| A1.2 game | 844 | 844 | 1.0 |
| A1.2 grammar | 8423 | 2366 | 2.8 |
| A1.2 home | 2755 | 1339 | 1.6 |
| A1.2 player-checked | — | 844 | 1.0 |
| A1.2 player-question | — | 844 | 1.0 |
| A1.2 puzzle-case | — | 1632 | 1.9 |
| A1.2 puzzle-escape | — | 1325 | 1.6 |
| A1.2 puzzle-guess | — | 1210 | 1.4 |
| A1.2 puzzle-words | — | 1995 | 2.4 |
| A1.2 reading | 2325 | 962 | 1.1 |
| A1.2 setlist | 18690 | 1661 | 2.0 |
| A1.2 test | 4811 | 844 | 1.0 |
| A1.2 unit | 844 | 1581 | 1.9 |
| A2.1 game | 844 | 844 | 1.0 |
| A2.1 grammar | 7877 | 2423 | 2.9 |
| A2.1 home | 3252 | 1419 | 1.7 |
| A2.1 player-checked | — | 844 | 1.0 |
| A2.1 player-question | — | 844 | 1.0 |
| A2.1 puzzle-case | — | 1904 | 2.3 |
| A2.1 puzzle-escape | — | 1331 | 1.6 |
| A2.1 puzzle-guess | — | 1210 | 1.4 |
| A2.1 puzzle-words | — | 1829 | 2.2 |
| A2.1 reading | 2325 | 990 | 1.2 |
| A2.1 setlist | 15183 | 1653 | 2.0 |
| A2.1 test | 4220 | 844 | 1.0 |
| A2.1 unit | 844 | 1581 | 1.9 |
| A2.2 game | 844 | 844 | 1.0 |
| A2.2 grammar | 8778 | 2387 | 2.8 |
| A2.2 home | 3362 | 1419 | 1.7 |
| A2.2 player-checked | — | 844 | 1.0 |
| A2.2 player-question | — | 844 | 1.0 |
| A2.2 puzzle-case | — | 2025 | 2.4 |
| A2.2 puzzle-escape | — | 1333 | 1.6 |
| A2.2 puzzle-guess | — | 1210 | 1.4 |
| A2.2 puzzle-words | — | 1925 | 2.3 |
| A2.2 reading | 2429 | 1249 | 1.5 |
| A2.2 setlist | 17833 | 1653 | 2.0 |
| A2.2 test | 4591 | 844 | 1.0 |
| A2.2 unit | 844 | 1581 | 1.9 |

Tallest pages measured by the smoke test (all routes, all apps, 390×844): a11 #/u/3/grammar/g2 2690px (3.2 screens), a11 #/u/4/grammar/g2 2690px (3.2 screens), a11 #/u/6/grammar/g1 2689px (3.2 screens), a12 #/u/10/grammar/g1 2676px (3.2 screens), a22 #/verbs 2661px (3.2 screens), a11 #/u/3/grammar/g1 2654px (3.1 screens), a22 #/u/14/grammar/g3 2649px (3.1 screens), a22 #/u/11/grammar/g1 2634px (3.1 screens), a11 #/u/4/grammar/g3 2630px (3.1 screens), a12 #/u/10/grammar/g2 2611px (3.1 screens), a21 #/u/3/grammar/g1 2607px (3.1 screens), a12 #/u/12/grammar/g1 2584px (3.1 screens)
<!-- /AUTO:heights -->

## (e) Questions for Eid

### New in round 2

1. **Your model line for A1.1 U1** ("Every sentence needs a verb: I'm Layla. (not: I Layla.)" /
   "my = it is mine. your = it is yours.") fails the level gate: *needs* is the he/she/it form
   (taught in U6) and *it is* comes in U2. The card now says "Say the verb: I'm Layla. (not: I
   Layla.)" / "I → am. You → are." / "my = mine. your = yours." Keep this, or allow your exact words?
2. **"(you can invent one)"** in the A1.1 U1 writing task uses *can* (taught in A1.2 U8). I kept
   your wording and marked it as a fixed instruction phrase. OK?
3. **A2.2 U14 T/F item.** "Hadi has repaired phones for six years" is now "Hadi started repairing
   phones six years ago" (True) and keeps the old item's ID, so learners' progress is kept. OK?
4. **Escape-room locks are built from the unit's own grammar items** (fix-the-mistake sentences,
   choose-the-word items and gap items), not written by hand. The codes are checked by the build
   and stored only as a hash. Is that kind of lock what you had in mind?
5. **On-screen keyboard** in the crossword, Guess the word and the password lock is A–Z in
   alphabetical order (not QWERTY), so every key can be 44 px wide on a 360 px phone. OK?
6. **The word search** has 44 px letters, so a 10×10 grid is wider than a small phone: it scrolls
   sideways inside its own box (the page itself doesn't). Would you prefer smaller letters?
7. **Crossword phrases.** A few units have very few one-word book words (A1.2 U11, A2.1 U5, A2.2
   U13–14), so their crosswords also use two-word phrases written without the space, with the
   word lengths shown, e.g. "get on (3,2)". OK?
8. **The case grid** is people × each group (e.g. people × cities and people × ages), not the
   full "every group against every group" grid of logic magazines. Enough for your learners?
9. **When is "Grammar" done?** In the 4-step path, *Grammar* (Learn) counts as done when its
   Quick checks are done; *Grammar practice* when all its sets are done.
10. **Proofread questions** that need your decision (details in `docs/notes/proofread-*.md`):
    *Can I go to the bathroom?* vs British *toilet*; *on Friday* vs *on Fridays* for habits (A1);
    prices in old or new Syrian pounds; accept *must* in A2.2 U13; present perfect for news and
    *yet* in A2.2 U14; cast details (Rana and Kareem meet in A1.1 U1 but are married in U5; "Um
    Ziad" naming in A2.1 U2); a few classroom dialogues with odd replies that I couldn't edit
    without resetting their progress.

### Still open from round 1

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

## (f) Things I wasn't sure about

* **Lock and puzzle wording at A1.1.** The level gate also checks puzzle instructions, so they
  are very simple ("The code = the numbers of the correct sentences, small to big.").
* **Red herrings** in the cases are true clues that are not needed; the build proves they are
  not needed. Some cases have two.
* **Riddle options at A1** are the answer plus three other words from the same unit (same
  category first). I checked them by reading; a distractor that also fits a clue would be a bug —
  please tell me if you find one.
* **Guess the word** accepts any word of 4–7 letters from this level's word lists up to the
  current unit, so some real English words are refused ("Not in the word list").
* **Page heights.** Every page is under about 3.2 screens at 390×844 except the Words list, the
  Irregular Verbs list and a long Mistake Notebook (measured by the smoke test; see (d)).
* **The state is still saved under the same key** (`eid-practice-<code>-v1`) with `v: 2` inside.
  A save that cannot be read is copied to `…-unreadable` instead of being overwritten.
* **Class mode** keeps the zoom steps (1.25 / 1.45 / 1.75). Games and puzzles start in "2 teams";
  Memory and Balloon Spelling keep their own score (the bar only passes the turn).

* **Cases at A2 use 8 clues** (7 needed + 1 red herring). The writer searched the 4 × 3 grids and
  found none that can be solved with fewer than 7 needed clues, so most A2 cases have only one
  negative clue among the needed ones (the red herring is often a second "not").
* **New first names in a few cases** (Lana, Sami, Yara in A1.1 U1; Omar and Nadia in A1.1 U5;
  Lama and Rami in A1.2; Lina and Yara in A2.2 U13) so the puzzles don't contradict jobs or
  subjects the regular cast already has.
* **A1.1 Unit 1 puzzle language** has almost no grammar to use (no *is* except "my/your … is"
  and "What's"), so its case clues are spoken lines: *Yara: "I'm in room 15."*
* **Lock 2 in some A1.1 U1 rooms** reuses the alphabet items ("Same sound as M: 1 N / 2 H / 3 E").
* **A2.1 U5 escape room** has its own title ("Locked on a train to Aleppo"); the others are
  "Locked in + place".

### Still from round 1

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
