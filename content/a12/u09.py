META = dict(n=9, title="Now and then", pages="66–71")

BOOK = """
January, February, March, April, May, June, July, August, September, October, November, December,
the first of January, the second of April, the third of December, the fourth of August,
first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth, eleventh, twelfth, thirteenth, fourteenth,
fifteenth, sixteenth, seventeenth, eighteenth, nineteenth, twentieth, twenty-first, thirtieth,
nineteen hundred, nineteen oh six, nineteen forty-five, nineteen eighty-four, two thousand, two thousand and five,
twenty ten, twenty twelve,
national holiday, President, (vinyl) record, sporting event, quiet, noisy, clean, dirty, naughty, yesterday
"""

WORDS = """
@Months
January | the first month of the year | My birthday is in January.
February | the second month; it's short | February is cold in Bloudan.
March | the third month | Mother's Day in Syria is on the twenty-first of March.
April | the fourth month | The weather in Damascus is lovely in April.
May | the fifth month | Layla's exams are in May.
June | the sixth month | Schools usually finish in June.
July | the seventh month; it's hot | July is very hot in Damascus.
August | the eighth month | We were on holiday in Latakia in August.
September | the ninth month | School starts in September.
October | the tenth month | The food festival was in October.
November | the eleventh month | It's often rainy in November.
December | the twelfth month; the last month | December is cold and wet.
@Dates
the first of January | 1st January, the first day of the year | The first of January is New Year's Day.
the second of April | 2nd April | My brother's birthday is on the second of April.
the third of December | 3rd December | The exam was on the third of December.
the fourth of August | 4th August | We were in Tartus on the fourth of August.
@Ordinal numbers
first | 1st | January is the first month.
second | 2nd | I live on the second floor.
third | 3rd | My office is on the third floor.
fourth | 4th | Reem was fourth in the race.
fifth | 5th | My birthday is on the fifth of May.
sixth | 6th | Today is the sixth of June.
seventh | 7th | July is the seventh month.
eighth | 8th | August is the eighth month.
ninth | 9th | The ninth of October was a Friday.
tenth | 10th | October is the tenth month.
eleventh | 11th | November is the eleventh month.
twelfth | 12th | December is the twelfth month.
thirteenth | 13th | Hadi's flat is on the thirteenth floor!
fourteenth | 14th | The fourteenth of February was a Tuesday.
fifteenth | 15th | The meeting is on the fifteenth.
sixteenth | 16th | Reem was sixteen on the sixteenth of May.
seventeenth | 17th | My cousin's wedding was on the seventeenth.
eighteenth | 18th | You can drive at eighteen — after your eighteenth birthday.
nineteenth | 19th | The nineteenth of March was a busy day.
twentieth | 20th | The twentieth of July was very hot.
twenty-first | 21st | Layla is twenty-one. Her twenty-first birthday was in May.
thirtieth | 30th | The thirtieth of June was the last day of school.
@Years
nineteen hundred | 1900 | The house was new in 1900 — nineteen hundred.
nineteen oh six | 1906 | My grandmother's house is from 1906 — nineteen oh six.
nineteen forty-five | 1945 | My grandfather was born in 1945 — nineteen forty-five.
nineteen eighty-four | 1984 | Kareem was born in nineteen eighty-four.
two thousand | 2000 | Reem wasn't born in two thousand. She's seventeen.
two thousand and five | 2005 | Our son was born in two thousand and five.
twenty ten | 2010 | We were in Istanbul in twenty ten.
twenty twelve | 2012 | The Olympic Games were in London in twenty twelve.
@Other words
national holiday | a day off for everyone in a country | The first of January is a national holiday in many countries.
President | the leader of a country | The President of the USA lives in the White House.
record | a big black disc with music on it; you play it on a special machine | My grandfather has old vinyl records of Fairuz.
sporting event | a big competition, like a football match | The World Cup is a big sporting event.
quiet | with very little noise | My street was quiet in the evening. | | noise
noisy | with a lot of noise | The souq is always noisy! | | noise
clean | not dirty | The kitchen was clean. | | clean
dirty | not clean | My shoes were dirty after the rain. | | clean
naughty | (a child) bad and not listening | The children were naughty today!
yesterday | the day before today | Where were you yesterday?
"""

ODD = """
January, March, May, *Monday | Monday: a day, not a month.
first, second, third, *four | Four: not an ordinal number.
quiet, noisy, clean, *yesterday | Yesterday: not an adjective.
was, were, wasn't, *is | Is: now, not past.
nineteen forty-five, twenty ten, two thousand, *thirtieth | Thirtieth: not a year.
June, July, August, *winter | Winter: a season, not a month.
twelfth, fifth, eighth, *eighty | Eighty: not an ordinal number.
"""

GRAMMAR = [
    dict(
        id="g1",
        title="was / were",
        visual=dict(type="timeline", now="now: is / are", marks=[dict(at=-2, label="yesterday: was / were", text="I was at home."),
                                                                dict(at=0, label="today", text=""), dict(at=-3, label="in 1984", text="")]),
        pattern=[
            ["+", "I / he / she / it", ["was", "v"], "at home."],
            ["+", "you / we / they", ["were", "v"], "at school."],
            ["−", "I / he / she / it", ["wasn't", "n"], "busy."],
            ["−", "you / we / they", ["weren't", "n"], "late."],
        ],
        examples=[
            "I {was} at the souq yesterday.",
            "The streets {were} quiet in 1980.",
            "Hadi {wasn't} at work yesterday. He {was} ill.",
            "We {weren't} at home on Friday. We {were} in London.",
        ],
        ar=[
            "was و were هني ماضي am و is و are: كان / كانوا.",
            "was مع I و he و she و it، و were مع you و we و they.",
            "للنفي: wasn't / weren't.",
        ],
        watch=[("I were at home.", "I was at home."), ("They was late.", "They were late."), ("Yesterday I am at work.", "Yesterday I was at work.")],
        quick="""
## choose: Choose the answer.
I ___ at home yesterday. | was | were | am
They ___ in Dubai last week. | were | was | are
She ___ at work on Friday. | wasn't | weren't | isn't
""",
        sets="""
## choose: Choose the answer.
Abu Firas ___ a postman. | was | were | be
We ___ in Istanbul in August. | were | was | are
The film ___ fantastic! | was | were | is be
My parents ___ at home yesterday. | weren't | wasn't | aren't
I ___ late yesterday. I was on time. | wasn't | weren't | not
You ___ at the party! Where were you? | weren't | wasn't | aren't
The souq ___ very noisy yesterday. | was | were | be
The children ___ naughty today. | were | was | is
It ___ cold in December. | was | were | are
Reem and Tala ___ at school on Monday. | were | was | is
## gap: Write was or were.
I [was] at the gym yesterday.
The shops [were] closed on Friday.
My grandfather [was] a teacher.
We [were] in Beirut in 2010.
It [was] a national holiday yesterday.
You [were] very busy last week.
The streets [were] dirty after the festival.
Hadi [was] late again!
## gap: Write wasn't or weren't.
I [wasn't|was not] at home. I was at work.
They [weren't|were not] happy with the food.
The museum [wasn't|was not] open on Tuesday.
We [weren't|were not] in Damascus in July.
The children [weren't|were not] naughty today. They were great!
Maya [wasn't|was not] at the café yesterday.
The tickets [weren't|were not] cheap.
It [wasn't|was not] very cold in January.
## transform: Change to the past (yesterday).
I'm at home. (yesterday) => I was at home.
They're in the park. (yesterday) => They were in the park.
She isn't busy. (yesterday) => She wasn't busy. | She was not busy.
We're late. (yesterday) => We were late.
The shop is closed. (yesterday) => The shop was closed.
You aren't at school. (yesterday) => You weren't at school. | You were not at school.
It's hot. (yesterday) => It was hot.
The children are quiet. (yesterday) => The children were quiet.
## fix: Find and fix the mistake.
I [were>was] at the cinema yesterday.
They [was>were] in Cairo last week.
Yesterday she [is>was] at home.
We [wasn't>weren't] late.
The streets [was>were] quiet.
My father [were>was] a postman.
You [was>were] at the party!
It [weren't>wasn't] cold yesterday.
## order: Put the words in order.
I was at home yesterday.
They were in Latakia in August.
She wasn't at work on Monday.
The streets were very quiet.
We weren't late.
My grandfather was a postman.
It was a fantastic day.
The children were naughty.
""",
    ),
    dict(
        id="g2",
        title="Questions with was / were",
        visual=dict(type="table", head=["question", "yes", "no"],
                    rows=[["Was she at home?", "Yes, she was.", "No, she wasn't."], ["Were they late?", "Yes, they were.", "No, they weren't."],
                          ["Where were you yesterday?", "At the souq.", ""]],
                    colors=["purple", "teal", "coral"], cap="Was / Were + person …?"),
        pattern=[
            ["?", ["Was", "v"], ["he", "s"], "at work yesterday?"],
            ["", "Yes, he", ["was.", "v"], ""],
            ["?", ["Were", "v"], ["you", "s"], "late?"],
            ["", "No, I", ["wasn't.", "n"], ""],
            ["?", "Where", ["were", "v"], "you on Friday?"],
        ],
        examples=[
            "{Were} you at home yesterday? — No, {I wasn't}. I {was} at work.",
            "{Was} the film good? — Yes, {it was}!",
            "{Where were} you on Friday? — In Bloudan.",
            "{What was} your first job? — I {was} a postman.",
        ],
        ar=[
            "لنسأل بالماضي منقدّم was أو were: Were you at home?",
            "الجواب: Yes, I was. / No, I wasn't.",
            "مع كلمات السؤال: Where were you? What was your job?",
        ],
        watch=[("You were at home?", "Were you at home?"), ("Where you were yesterday?", "Where were you yesterday?"), ("Was you late?", "Were you late?")],
        quick="""
## choose: Choose the answer.
___ you at the party? | Were | Was | Are
Was Hadi late? — Yes, he ___. | was | were | is
Where ___ she yesterday? | was | were | is
""",
        sets="""
## choose: Choose the answer.
___ you at home on Friday? | Were | Was | Be
___ the exam difficult? | Was | Were | Be
Were they in Aleppo? — Yes, they ___. | were | was | are
Was Maya at the café? — No, she ___. | wasn't | weren't | isn't
Where ___ you yesterday? | were | was | are
What ___ your grandfather's job? | was | were | be
___ the children naughty? | Were | Was | Be
Was it cold? — Yes, it ___. | was | were | is
How ___ your holiday? | was | were | be
Who ___ your first teacher? | was | were | be
## short: Answer the question.
Were you at home yesterday? (✓) => Yes, I was.
Was the film good? (✗) => No, it wasn't. | No, it was not.
Were they late? (✓) => Yes, they were.
Was Hadi at work? (✗) => No, he wasn't. | No, he was not.
Were the shops open? (✓) => Yes, they were.
Was it a holiday? (✗) => No, it wasn't. | No, it was not.
Was Reem at school? (✓) => Yes, she was.
Were you tired? (✗) => No, I wasn't. | No, I was not.
## transform: Make a question (?).
She was at the souq. (?) => Was she at the souq?
They were on holiday. (?) => Were they on holiday?
The food was good. (?) => Was the food good?
You were late. (?) => Were you late?
Hadi was ill. (?) => Was Hadi ill?
The children were at school. (?) => Were the children at school?
It was a national holiday. (?) => Was it a national holiday?
We were noisy. (?) => Were we noisy?
## match: Match the question and the answer.
Where were you yesterday? = At my grandmother's house.
Was the film good? = Yes, it was fantastic.
Were they at the party? = No, they weren't.
What was your first job? = I was a postman.
When was the exam? = On the fifth of May. #id=a12u9-6a41f56
Who was at the door? = It was Jad with a delivery.
How was your holiday? = Great, thanks!
Was Hadi late again? = Yes, he was!
## fix: Find and fix the mistake.
[Was>Were] you at home?
Where [you were>were you] on Friday?
Was it cold? — Yes, it [were>was].
[Were>Was] Reem at school?
[They were>Were they] on holiday?
What [were>was] your first job?
Were they late? — No, they [wasn't>weren't].
How [were>was] the party?
## order: Put the words in order.
Were you at home yesterday?
Was the film good?
Where were you on Friday?
What was your first job?
Were the shops open?
Was it a holiday?
How was your weekend?
Who was your first teacher?
""",
    ),
    dict(
        id="g3",
        title="Dates: the first of January",
        visual=dict(type="calendar", title="May", days=[str(d) for d in range(1, 32)], mark=["1", "2", "3", "5", "21"],
                    notes=["1 = the {first} · 2 = the {second} · 3 = the {third} · 5 = the {fifth} · 21 = the {twenty-first}"]),
        pattern=[
            ["", "We say:", ["the fifth of May", "v"], ""],
            ["", "We write:", ["5th May / 5 May", "x"], ""],
            ["", ["on", "s"], "+ date:", "on the first of January"],
            ["", ["in", "s"], "+ month / year:", "in May, in 1984"],
        ],
        examples=[
            "My birthday is {on the fifth of May}.",
            "Reem was born {in} 2009.",
            "The exam was {on the third of December}.",
            "1984 = {nineteen eighty-four} · 2012 = {twenty twelve}",
        ],
        ar=[
            "التاريخ منقولو بالرقم الترتيبي: the first, the second, the third of May.",
            "منقول on مع التاريخ: on the 5th of May، و in مع الشهر أو السنة: in May, in 2012.",
            "السنين منقسمها: 1984 = nineteen eighty-four، 2012 = twenty twelve.",
        ],
        watch=[("in the 5th of May", "on the 5th of May"), ("the five of May", "the fifth of May"), ("1984 = one thousand nine hundred eighty-four", "nineteen eighty-four")],
        quick="""
## choose: Choose the answer.
2 = ___ | second | twoth | secondth
My birthday is ___ the 3rd of May. | on | in | at
1984 = ___ | nineteen eighty-four | nineteen hundred eighty-four | one nine eight four
""",
        sets="""
## numbers: Write the ordinal number.
1st => first
2nd => second
3rd => third
5th => fifth
8th => eighth
9th => ninth
12th => twelfth
20th => twentieth
21st => twenty-first | twenty first
30th => thirtieth
## choose: Choose the answer.
4th = ___ | fourth | fourst | four
22nd = ___ | twenty-second | twenty-two | twenty-twoth
3rd = ___ | third | threeth | three
The ___ month is May. | fifth | five | fiveth
December is the ___ month. | twelfth | twelve | twelveth
August is the ___ month. | eighth | eight | eightth
My birthday is ___ the 10th of June. | on | in | at
I was born ___ 1999. | in | on | at
The exam was ___ April. | in | on | at
Eid was ___ the 30th. | on | in | at
## numbers: Write the year in words.
1900 => nineteen hundred
1906 => nineteen oh six | nineteen o six
1945 => nineteen forty-five | nineteen forty five
1984 => nineteen eighty-four | nineteen eighty four
2000 => two thousand
2005 => two thousand and five | two thousand five
2010 => twenty ten | two thousand and ten | two thousand ten
2012 => twenty twelve | two thousand and twelve | two thousand twelve
## numbers: Write the date in words.
1/1 => the first of January | first of January | January the first | January first
2/4 => the second of April | second of April | April the second
3/12 => the third of December | third of December | December the third
4/8 => the fourth of August | fourth of August | August the fourth
21/3 => the twenty-first of March | twenty-first of March | the twenty first of March | March the twenty-first
5/5 => the fifth of May | fifth of May | May the fifth
12/10 => the twelfth of October | twelfth of October | October the twelfth
30/6 => the thirtieth of June | thirtieth of June | June the thirtieth
## gap: Write on or in.
My birthday is [on] the fourth of August.
Kareem was born [in] 1984.
The festival is [in] October.
The exam was [on] Monday.
School starts [in] September.
Eid was [on] the tenth.
The museum was new [in] 1919.
We were in Hama [on] the first of May.
## fix: Find and fix the mistake.
My birthday is [in>on] the fifth of May.
I was born [on>in] 1990.
Today is the [two>second] of April.
The [twelveth>twelfth] month is December.
School starts [on>in] September.
The [five>fifth] of May was a Friday.
2012 = [two zero one two>twenty twelve|two thousand and twelve].
The [threeth>third] of March was cold.
""",
    ),
]

CLASSROOM = dict(
    phrases=["Sorry, can you speak louder, please?", "I was absent last lesson.", "What's the homework?",
             "What did we do yesterday?", "Can you help me?", "I'm not sure.", "Is it a or b?"],
    order="""
S: Excuse me, I was absent last lesson.
T: OK. Were you ill?
S: Yes, I was. What did we do yesterday?
T: Page 68 — was and were.
S: Sorry, can you speak louder, please?
T: Page sixty-eight!
""",
)

READING = dict(
    title="Abu Firas remembers",
    text="""Abu Firas is sixty-two. He was a postman in Sarouja for thirty-five years. "My first day at work was on the third of March, 1980," he says. "I was very young and very happy.

Life was different then. The streets were quiet and clean, and there weren't a lot of cars. There weren't any mobile phones! Letters were very important. People were always happy to see the postman.

My favourite things were my old bike and my radio. There was a small café near the post office, and my friends were there every evening. Was life easy then? I don't know. It was slow and quiet!" """,
    qs="""
## tf: True or false?
Abu Firas was a postman for thirty-five years. | T @ He was a postman in Sarouja for thirty-five years
His first day at work was in 1990. | F @ the third of March, 1980
The streets were noisy and dirty. | F @ The streets were quiet and clean
There weren't any mobile phones. | T @ There weren't any mobile phones
Letters were important. | T @ Letters were very important
## choose: Choose the answer.
Where were his friends every evening? | at a café | at the post office | at home @ There was a small café near the post office, and my friends were there every evening
What were his favourite things? | his bike and his radio | his phone and his car | letters and photos @ My favourite things were my old bike and my radio
## gap: Write one word.
On his first day, Abu Firas was very young and very [happy]. @ I was very young and very happy
""",
)

DIALOGUE = dict(
    title="Where were you?",
    intro="Monday morning. Layla meets Hadi at university.",
    task="gaps",
    lines="""
Layla: Hadi! Where [were] you yesterday?
Hadi: I was at home. I [was] ill.
Layla: Oh no! Are you OK now?
Hadi: Yes, thanks. [Was] the lesson good?
Layla: Yes, it was. The teacher [wasn't] happy — the class was very noisy!
Hadi: Were the other students [there]?
Layla: No, they [weren't]. Only five students!
Hadi: And when is the exam? Is it [on] the fifteenth?
""",
)

WQ = """
I was at the souq. (Where / you / yesterday) => Where were you yesterday?
Yes, it was. It was great. (the film / good) => Was the film good?
No, they weren't. They were on time. (they / late) => Were they late?
On the fifth of May. (When / your birthday) => When's your birthday? | When is your birthday?
I was a postman. (What / your first job) => What was your first job?
Fantastic, thanks! (How / your holiday) => How was your holiday?
No, she wasn't. She was at work. (Maya / at home) => Was Maya at home?
In 1984. (When / Kareem / born) => When was Kareem born?
"""

WRITING = [
    dict(task="Write about your town or your street when you were a child. What was there? What was different?",
         tip="Use was / were / wasn't / weren't and there was / there were. Write 50–80 words.",
         model="When I was a child, my family's home was in Jaramana. Our street was small and quiet. There were a lot of trees and there was a little shop on the corner. There weren't a lot of cars. The people were friendly, and the children were always outside. My school was near our house. Life was simple then!",
         check=["was / were", "wasn't / weren't", "there was / there were", "an adjective: quiet, noisy, clean…"],
         min=50, max=80),
]

CANDO = [
    "use was and were.",
    "ask 'Where were you yesterday?'",
    "say the months and ordinal numbers.",
    "say dates and years: the fifth of May, nineteen eighty-four.",
    "talk about the past: my town then and now.",
]
