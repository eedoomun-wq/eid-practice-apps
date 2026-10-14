META = dict(n=7, title="Your time", pages="50–57")

BOOK = """
get up (late/early), have breakfast/lunch/dinner, go to work, start work, finish work, get home, go to bed,
go out with friends, have a party, have a day off work, go on holiday,
Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday,
three o'clock, two fifteen, five thirty, nine forty-five, midday, midnight,
on weekdays / Friday / Sunday, at two o'clock / three forty-five / the weekend,
in the morning / the afternoon / the evening, every day / week / weekend / month / year,
busy, celebrate, (birthday) party, young, old, exam, Tai Chi, football match, relax, doctor's appointment, meeting,
TV programme, tourists/tourism, (food/music) festival
"""

WORDS = """
@Routines
get up (late/early) | to leave your bed in the morning | Abu Omar gets up early, at five o'clock. | get up;gets up
have breakfast/lunch/dinner | to eat your morning / midday / evening meal | We have breakfast at seven. | have breakfast;has breakfast;have lunch;has lunch;have dinner;has dinner
go to work | to travel to your job | Rana goes to work by service taxi. | go to work;goes to work
start work | to begin your work | Nour starts work at nine.
finish work | to stop work at the end of the day | Kareem finishes work at seven in the evening.
get home | to arrive at your house | What time do you get home?
go to bed | to go to sleep at night | Reem goes to bed at ten.
go out with friends | to leave home for fun with friends | I go out with friends on Thursday evening.
have a party | to celebrate with friends, music and food | We have a party for Eid.
have a day off work | a day when you don't go to work | Hadi has a day off work on Tuesday.
go on holiday | to travel for fun, not work | We go on holiday to Latakia every summer.
@Days
Monday | the day after Sunday | I have an English lesson on Monday.
Tuesday | the day after Monday | The museum is closed on Tuesday.
Wednesday | the day after Tuesday | Rana has a meeting on Wednesday.
Thursday | the day after Wednesday | We go out on Thursday evening.
Friday | the day after Thursday; a day off in Syria | Kareem's shop is closed on Friday.
Saturday | the day after Friday | Maya works at the café on Saturday.
Sunday | the day after Saturday | Sunday is a work day in Syria.
@Times
three o'clock | 3:00 | The lesson starts at three o'clock.
two fifteen | 2:15 | The bus leaves at two fifteen.
five thirty | 5:30 | I finish work at five thirty.
nine forty-five | 9:45 | The film starts at nine forty-five.
midday | 12:00 in the day | We have lunch at midday. | | noon
midnight | 12:00 at night | Salma finishes work at midnight. | | noon
@Time words
on weekdays / Friday / Sunday | on + days | I work on weekdays. I relax on Friday. | on weekdays;on Friday;on Sunday
at two o'clock / three forty-five / the weekend | before clock times, and before the two days off at the end of the week | Let's meet at two o'clock. We relax at the weekend. | at two o'clock;at three forty-five;at the weekend
in the morning / the afternoon / the evening | in + parts of the day | I drink coffee in the morning. | in the morning;in the afternoon;in the evening
every day / week / weekend / month / year | all the days / weeks… again and again | Hala opens her café every day. | every day;every week;every weekend;every month;every year
@Other words
busy | with a lot to do; no free time | Tareq is always busy on Friday.
celebrate | to do something special for a happy day | We celebrate Eid with our family.
party | an event with friends, food and music | Joud's birthday party is on Saturday. | party;parties
young | not old | Reem is young. She's seventeen. | | age
old | not young | My grandfather is old, but he's very active. | | age
exam | a test at school or university | Layla has an exam on Monday.
Tai Chi | a slow Chinese exercise | Mei does Tai Chi in the park every morning.
football match | a game of football | There's a football match on TV tonight.
relax | to rest and feel calm | I relax in the garden in the evening.
doctor's appointment | a time to see the doctor | I have a doctor's appointment at four.
meeting | people come together to talk about work | The meeting starts at ten.
TV programme | a show on TV | My favourite TV programme is on Thursday.
tourists/tourism | people on holiday / the business of holidays | There are a lot of tourists in Maaloula. | tourists;tourism
festival | a big event with food or music, often for days | Our street has a small food festival every spring. | festival;festivals
"""

ODD = """
Monday, Friday, Sunday, *midday | Midday: a time, not a day.
get up, have breakfast, go to work, *football match | Football match: not a routine.
always, usually, never, *Tuesday | Tuesday: a day.
in the morning, in the evening, in the afternoon, *at the weekend | At the weekend: at, not in.
midday, midnight, three o'clock, *young | Young: not a time.
meeting, exam, doctor's appointment, *relax | Relax: a verb.
What, Where, When, *Usually | Usually: not a question word.
"""

GRAMMAR = [
    dict(
        id="g1",
        title="How often? Frequency adverbs",
        visual=dict(type="scale", items=[["never", 0], ["hardly ever", 10], ["sometimes", 40], ["often", 65], ["usually", 85], ["always", 100]]),
        pattern=[
            ["+", "I", ["always", "x"], "get up early."],
            ["+", "She", ["usually", "x"], "has breakfast at seven."],
            ["+", "He", "'s", ["never", "x"], "late. (after be)"],
            ["?", "How often", "do you", "go to the gym?"],
        ],
        examples=[
            "Abu Omar {always} gets up at five.",
            "Hadi is {often} late for work.",
            "We {sometimes} have lunch at Um Khaled's house.",
            "Fadi {hardly ever} cooks. He {usually} eats fast food.",
        ],
        ar=[
            "هي الكلمات بتقول قدّيش منعمل الشي: always (دايماً) لـ never (أبداً).",
            "منحطها قبل الفعل: I always get up early. بس بعد am / is / are: He's never late.",
            "never بتكون لحالها نفي، ما منحط معها don't: I never drink coffee.",
            "لنسأل: How often do you…? (قدّيش بتعمل…؟)",
        ],
        en=[
            "How often? {always} 100% → {usually} → {often} → {sometimes} → {hardly ever} → {never} 0%.",
            "Put the word before the verb: I {always} get up early.",
            "After am / is / are, put it after: He's {never} late.",
            "{never} is already negative: I never drink coffee. (not: I don't never…)",
        ],
        watch=[("I go always to bed late.", "I always go to bed late."), ("He always is late.", "He's always late."),
               ("I don't never eat meat.", "I never eat meat.")],
        quick="""
## choose: Choose the answer.
I ___ get up at six. (100%) | always | never | sometimes
Hadi is ___ late. (90%) | usually | never | hardly ever
She ___ drinks coffee. (0%) | never | always | often
""",
        sets="""
## choose: Choose the right sentence.
Abu Omar gets up early. (always) | Abu Omar always gets up early. | Abu Omar gets always up early. | Abu Omar gets up always early.
Hadi is late. (often) | Hadi is often late. | Hadi is late often is. | Often Hadi is often late.
I have lunch at home. (usually) | I usually have lunch at home. | I have usually lunch at home. | I have lunch at usually home.
Maya is tired. (never) | Maya is never tired. | Maya is tired never is. | Maya never tired is.
We go out on Thursday. (sometimes) | We sometimes go out on Thursday. | We go sometimes out on Thursday. | We go out on sometimes Thursday.
Fadi cooks. (hardly ever) | Fadi hardly ever cooks. | Fadi hardly cooks ever ever. | Fadi cooks hardly hardly ever.
The shop is busy on Friday. (always) | The shop is always busy on Friday. | The shop is busy on always Friday. | Always the shop always is busy.
They watch TV in the evening. (often) | They often watch TV in the evening. | They watch often TV in the evening. | They watch TV in often the evening.
## choose: Choose the answer.
Salma works at night. She ___ sleeps in the day. (90%) | usually | never | hardly ever
I ___ drink coffee — I hate it! (0%) | never | always | usually
Abu Omar ___ gets up late. (10%) | hardly ever | always | often
The bus is ___ late. (40%) | sometimes | always | never
Mei does Tai Chi every morning. She ___ does it. | always | never | hardly ever
Tareq is ___ busy on Friday. (100%) | always | never | sometimes
We ___ go to the cinema — once or twice a month. (60%) | often | never | always
Hadi ___ arrives on time. He's late every day! (0%) | never | always | usually
The trains in Tokyo are ___ late. (0%) | never | always | usually
I ___ eat fast food. It's not healthy. (10%) | hardly ever | always | usually
## gap: Write the adverb.
Abu Omar gets up at five every day. He [always] gets up at five. (100%)
Fadi [never] cooks dinner. (0%)
I [usually] have breakfast at seven. (85%)
We [sometimes] go to Bloudan at the weekend. (40%)
Hadi is [often] late. (65%)
Maya [hardly ever] watches TV. (10%)
The cafés in Paris are [always] busy in the evening. (100%)
My grandparents [never] go to bed late. (0%)
## order: Put the words in order.
I always get up early.
He's never late.
We sometimes go out on Thursday.
She usually has breakfast at seven.
They often watch films.
I hardly ever drink coffee.
Is he always busy?
How often do you go to the gym?
## fix: Find and fix the mistake.
I [go always>always go] to bed at eleven.
She [always is>is always] happy.
We [don't never>never] eat fast food.
He [eats usually>usually eats] at home.
They [often are>are often] late.
I [sometimes am>am sometimes|'m sometimes] tired.
Fadi [cooks hardly ever>hardly ever cooks].
Rana [always is>is always] busy on Monday.
## short: Answer about you. Write a full sentence.
How often do you drink tea? (always) => I always drink tea.
How often do you go to the cinema? (sometimes) => I sometimes go to the cinema.
How often are you late? (never) => I'm never late. | I am never late.
How often do you cook dinner? (often) => I often cook dinner.
How often do you eat fast food? (hardly ever) => I hardly ever eat fast food.
How often do you get up early? (usually) => I usually get up early.
How often are you busy? (always) => I'm always busy. | I am always busy.
How often do you go to the gym? (never) => I never go to the gym.
""",
    ),
    dict(
        id="g2",
        title="Wh- questions: What time do you…?",
        visual=dict(type="table", head=["question word", "do / does", "subject", "verb"],
                    rows=[["What time", "do", "you", "get up?"], ["Where", "does", "she", "work?"], ["When", "do", "they", "have lunch?"],
                          ["What", "does", "he", "do?"], ["How often", "do", "you", "go out?"]],
                    colors=["amber", "purple", "teal", "white"], cap="Question word + do / does + subject + verb?"),
        pattern=[
            ["?", ["What time", "x"], ["do", "v"], "you get up?"],
            ["?", ["Where", "x"], ["does", "v"], "she work?"],
            ["?", ["What", "x"], ["does", "v"], "he do? (= his job)"],
            ["?", ["When", "x"], ["do", "v"], "they have lunch?"],
        ],
        examples=[
            "{What time do} you get up? — At six o'clock.",
            "{Where does} Nour work? — In a pharmacy in Sha'lan.",
            "{What does} Jad {do}? — He's a delivery driver.",
            "{When do} you go to the gym? — On Monday and Wednesday.",
        ],
        ar=[
            "السؤال بيبلش بكلمة السؤال: What, Where, When, What time، بعدين do أو does.",
            "does مع he و she و it، و do مع الباقي، والفعل بيرجع لأصله بلا s.",
            "What do you do? يعني شو شغلتك؟ مو شو عم تعمل هلق.",
        ],
        en=[
            "Question word + do / does + person + verb: Where {does} she work?",
            "{does} with he / she / it. {do} with I / you / we / they.",
            "After does, the verb has no s: Where does he {work}? (not: works)",
            "What do you do? = What's your job?",
        ],
        watch=[("Where she works?", "Where does she work?"), ("What time you get up?", "What time do you get up?"),
               ("Where does he works?", "Where does he work?")],
        quick="""
## choose: Choose the answer.
What time ___ you get up? | do | does | are
Where ___ Salma work? | does | do | is
What does Hadi ___? — He repairs phones. | do | does | doing
""",
        sets="""
## choose: Choose the answer.
Where ___ you live? | do | does | are
What time ___ Abu Omar get up? | does | do | is
When ___ they have dinner? | do | does | are
What ___ Rana do? — She's a teacher. | does | do | is
Where does Hadi ___? — In Bab Touma. | work | works | working
What time do you ___ work? | finish | finishes | finishing
How often ___ Mei do Tai Chi? | does | do | is
What do you ___ at the weekend? | do | does | doing
When ___ the museum open? | does | do | are #id=a12u7-148749b
Where do your parents ___? | live | lives | living
## bank: Use the words.
[What time|When] do you get up? — At six.
[Where] does Nour work? — In a pharmacy.
[When] do you go to the gym? — On Monday.
[What] does Jad do? — He's a delivery driver.
[How often] do you go out? — Every weekend.
[What time|When] does the film start? — At nine forty-five.
[Where] do they live? — In Jaramana.
[What] do you have for breakfast? — Labneh and bread.
## match: Match the question and the answer.
What time do you get up? = At six o'clock.
Where does Maya work? = In a café in Baramkeh.
When do you have lunch? = At midday.
What does Samer do? = He's an electrician.
How often do you go to the gym? = Twice a week.
Where do your grandparents live? = In Sarouja.
What do you do on Friday? = I relax with my family.
When does the festival start? = On Thursday evening.
## transform: Write the question.
I get up at six. (What time / you) => What time do you get up?
Nour works in Sha'lan. (Where / Nour) => Where does Nour work?
They have dinner at eight. (What time / they) => What time do they have dinner?
Hadi finishes work at seven. (When / Hadi) => When does Hadi finish work? | What time does Hadi finish work?
We go out on Thursday. (When / you) => When do you go out?
Abu Omar sells fruit. (What / Abu Omar) => What does Abu Omar sell?
My parents live in Istanbul. (Where / your parents) => Where do your parents live?
Mei does Tai Chi every day. (How often / Mei) => How often does Mei do Tai Chi?
## fix: Find and fix the mistake.
Where [she works>does she work]?
What time [you get>do you get] up?
Where does he [works>work]?
What [do>does] Rana do?
When [does>do] they have lunch?
What time [is>does] the film start?
How often [you go>do you go] to the gym?
Where [do>does] Salma live?
## order: Put the words in order.
What time do you get up?
Where does Nour work?
When do they have dinner?
What does Jad do?
How often do you go out?
What do you do at the weekend?
Where do your parents live?
What time does the bank open?
""",
    ),
    dict(
        id="g3",
        title="Times and at / on / in",
        visual=dict(type="clocks", times=[["7:00", "seven o'clock in the morning"], ["2:15", "two fifteen in the afternoon"],
                                          ["5:30", "five thirty in the afternoon"], ["9:45", "nine forty-five in the evening"],
                                          ["12:00", "midday (12:00 in the day)"], ["12:00", "midnight (12:00 at night)"]]),
        pattern=[
            ["", ["at", "x"], "+ clock time:", "at three o'clock, at five thirty"],
            ["", ["on", "v"], "+ day:", "on Monday, on weekdays"],
            ["", ["in", "s"], "+ part of the day:", "in the morning, in the evening"],
            ["", ["at", "x"], "the weekend,", "at midday, at midnight"],
        ],
        examples=[
            "The lesson starts {at} three o'clock.",
            "Kareem's shop is closed {on} Friday.",
            "I drink tea {in} the morning and {in} the evening.",
            "We relax {at} the weekend.",
        ],
        ar=[
            "at للساعة: at five o'clock، on لليوم: on Monday، in لقسم من النهار: in the morning.",
            "بس منقول at night و at the weekend و at midday.",
            "الوقت منقولو بالأرقام: 2:15 = two fifteen، 5:30 = five thirty.",
        ],
        en=[
            "{at} + clock time: at five o'clock. Also: at night, at the weekend.",
            "{on} + day: on Monday, on weekdays.",
            "{in} + part of the day: in the morning, in the evening.",
            "Say times like this: 2:15 = two fifteen, 5:30 = five thirty.",
        ],
        watch=[("in Monday", "on Monday"), ("at the morning", "in the morning"), ("on five o'clock", "at five o'clock")],
        quick="""
## choose: Choose the answer.
The film starts ___ nine o'clock. | at | on | in
I go to the gym ___ Monday. | on | at | in
We have breakfast ___ the morning. | in | on | at
""",
        sets="""
## choose: Choose at, on or in.
Banks in Dubai open ___ eight thirty. | at | on | in
Maya works ___ Saturday. | on | at | in
I read ___ the evening. | in | on | at
We relax ___ the weekend. | at | in | on
Salma works ___ night. | at | in | on
The meeting is ___ Wednesday. | on | in | at
Abu Omar gets up ___ five o'clock. | at | on | in
I have English ___ the afternoon. | in | at | on
We have lunch ___ midday. | at | in | on
The museum is closed ___ Tuesday. | on | in | at
## sort: at, on or in? | at | on | in
at: five o'clock, the weekend, midnight, night
on: Monday, Friday, weekdays, Sunday
in: the morning, the afternoon, the evening
## numbers: Write the time in words.
3:00 => three o'clock | three
2:15 => two fifteen | quarter past two | a quarter past two
5:30 => five thirty | half past five
9:45 => nine forty-five | nine forty five | quarter to ten | a quarter to ten
7:10 => seven ten | ten past seven
12:00 (day) => midday | twelve o'clock | noon
11:20 => eleven twenty | twenty past eleven
6:05 => six oh five | five past six
## numbers: Write the time in numbers.
four fifteen => 4:15
eight thirty => 8:30
ten o'clock => 10:00 | 10
one forty-five => 1:45
six twenty => 6:20
twelve thirty => 12:30
nine fifty => 9:50
three oh five => 3:05
## gap: Write at, on or in.
I go to the gym [on] Tuesday and Thursday.
The film starts [at] nine forty-five.
Rana has meetings [in] the afternoon.
We have a party [at] the weekend.
The café is busy [in] the evening.
I have a doctor's appointment [on] Wednesday.
Hadi gets home [at] midnight.
I work [on] weekdays.
## fix: Find and fix the mistake.
I get up [in>at] six o'clock.
The shop is closed [in>on] Friday.
I study [at>in] the evening.
We go out [on>at] the weekend.
The lesson is [at>on] Monday.
She drinks coffee [on>in] the morning.
Salma works [in>at] night.
The meeting is [in>at] three thirty.
""",
    ),
]

CLASSROOM = dict(
    phrases=["Can you help me?", "Can I ask a question?", "How do you say this word?", "What's the answer to number 3?",
             "Is it a or b?", "I think it's …", "I'm not sure."],
    order="""
S: Excuse me, can I ask a question?
T: Yes, of course.
S: What's the answer to number 3? Is it a or b?
T: What do you think?
S: I'm not sure. I think it's b.
T: Yes, it's b. Well done!
""",
)

READING = dict(
    title="An early riser",
    text="""Abu Omar is a greengrocer in Kafr Sousa. He's forty-eight, and he's always busy. He gets up at five o'clock every day — he never gets up late! He has breakfast with his wife at five thirty. They usually have bread, labneh and tea.

He opens his shop at six fifteen. In the morning, the shop is always busy. He has lunch at midday, and he sometimes has a short sleep in the afternoon. He finishes work at seven in the evening and gets home at seven thirty.

He doesn't work on Friday. He usually visits his family, and he often watches a football match on TV in the evening.""",
    qs="""
## tf: True or false?
Abu Omar sometimes gets up late. | F @ he never gets up late
He has breakfast with his wife. | T @ He has breakfast with his wife at five thirty
The shop is quiet in the morning. | F @ In the morning, the shop is always busy
He works on Friday. | F @ He doesn't work on Friday
He often watches football on Friday evening. | T @ he often watches a football match on TV in the evening
## choose: Choose the answer.
What time does he open his shop? | at six fifteen | at five o'clock | at seven thirty @ He opens his shop at six fifteen
When does he get home? | at seven thirty | at midday | at five thirty @ gets home at seven thirty
## gap: Write one word.
Abu Omar is a [greengrocer]. @ Abu Omar is a greengrocer
""",
)

DIALOGUE = dict(
    title="A busy week",
    intro="Layla and Reem make a plan in the library.",
    task="gaps",
    lines="""
Reem: Layla, what do you [do] on Thursday afternoon?
Layla: I usually go to the gym [at] four o'clock.
Reem: And what [time] do you finish?
Layla: At five thirty. Why?
Reem: There's a food festival in Tishreen Park [on] Thursday evening!
Layla: Great! How [often] do they have it?
Reem: Every year, in October. It's [always] fantastic.
Layla: OK. Let's meet at six, [in] front of the park.
""",
)

WQ = """
At six o'clock. (What time / you / get up) => What time do you get up?
In a café in Baramkeh. (Where / Maya / work) => Where does Maya work?
He's an electrician. (What / Samer / do) => What does Samer do?
Every day. (How often / you / drink tea) => How often do you drink tea?
On Friday. (When / you / relax) => When do you relax?
At midnight. (What time / Salma / finish work) => What time does Salma finish work? | When does Salma finish work?
In Jaramana. (Where / they / live) => Where do they live?
Bread and cheese. (What / you / have for breakfast) => What do you have for breakfast?
"""

WRITING = [
    dict(task="Write about your typical day: what time you get up, start work or school, have lunch, get home, go to bed.",
         tip="Use times, at / on / in, and always / usually / sometimes / never. Write 50–80 words.",
         model="I usually get up at six thirty on weekdays. I have breakfast with my family at seven — always tea and bread! I start work at eight. I have lunch at midday. I finish work at four and I get home at five. In the evening I sometimes go out with friends. I never go to bed late. At the weekend I relax.",
         check=["times: at seven, at four thirty", "on + days, in the morning / evening", "always / usually / sometimes / never", "before the verb: I always get up…"],
         min=50, max=80),
    dict(task="Write five questions for a partner about their week.",
         tip="Use What time…? Where…? When…? How often…?",
         model="What time do you get up?\nWhere do you have lunch?\nWhen do you go to the gym?\nHow often do you go out with friends?\nWhat do you do on Friday?",
         check=["question word + do / does", "the verb without s after does", "a question mark (?)"],
         min=20, max=60),
]

CANDO = [
    "say how often I do things: always, usually, sometimes, never.",
    "ask Wh- questions: What time do you…? Where does she…?",
    "say the time: two fifteen, five thirty.",
    "use at, on and in with times and days.",
    "talk about my daily routine.",
]
