META = dict(n=7, title="Life stories", pages="60–69")

BOOK = """
get a job, meet someone, get married, move to a different (city/country), go to university, start a business,
graduate from university, have children, start school, study maths, leave school,
last summer, ago, when I was, on my last birthday, yesterday, this morning,
become, love, collect things, make, composer, meet, decide, move, skater, start, study, graduate, take, want, work,
journalist
"""

WORDS = """
@Life events
get a job | to start work for a company or a person | Hadi got a job in a phone shop in 2019. | get a job;got a job
meet someone | to see a person for the first time and love them | Rana met someone special at a wedding. | meet someone;met someone
get married | to become husband and wife | They got married in 2012.
move to a different (city/country) | to start living in a new place | Bassel moved to a different country — the UAE. | moved to a different country;moved to a different city;move to a different city;move to a different country
go to university | to start studying at a university | Layla went to university in 2023.
start a business | to open your own shop or company | Walid started a business in 1998.
graduate from university | to finish university with a degree | Ghada graduated from university in 2010.
have children | to become a mother or father | They had children in 2005.
start school | to go to school for the first time | Joud started school at six.
study maths | to learn numbers and calculations | I studied maths at university.
leave school | to finish school | Walid left school at sixteen.
@Time phrases
last summer | the summer before this one | We went to Latakia last summer.
ago | before now | I moved to Damascus five years ago.
when I was | words to start a story about your past: a child, ten, young… | When I was a child, I lived in Hama.
on my last birthday | on the day of my birthday last year | On my last birthday, my friends made a cake.
yesterday | the day before today | I was at home yesterday.
this morning | the morning of today | I had coffee with Maya this morning.
@Verbs
become | to start to be | She became a doctor in 2010. | become;became
love | to like very much | He loved music when he was a child. | love;loved
collect things | to keep and save things of one type, like coins | My grandfather collected coins. | collect things;collected coins;collect coins
make | to build or produce something | Walid made his first knafeh at fourteen. | make;made
composer | a person who writes music | Mozart was a famous composer.
meet | to see a person, often for the first time | I met my best friend at school. | meet;met
decide | to choose what to do | Hadi decided to open a phone shop.
move | to go to live in a new place | We moved to Mezzeh in 2015.
skater | a person who moves on ice with special shoes | The skater won a gold medal.
start | to begin | The lesson started at nine.
study | to learn at school or university | She studied law in Damascus.
graduate | to finish university | He graduated in 2005.
take | to carry or get something | I took a lot of photos in Maaloula. | take;took
want | to wish to have or do | When I was young, I wanted to be a pilot.
work | to have a job | My grandfather worked in a bank for forty years.
journalist | a person who writes for a newspaper or website | Sami was a journalist in Beirut.
"""

ODD = """
went, had, made, *start | Start: not past.
worked, studied, moved, *took | Took: irregular.
composer, skater, journalist, *graduate | Graduate: a verb.
yesterday, last summer, two years ago, *tomorrow | Tomorrow: not past.
was, were, *are, went | Are: present.
get married, have children, start a business, *this morning | This morning: a time phrase.
"""

GRAMMAR = [
    dict(
        id="g1",
        title="was / were",
        visual=dict(type="timeline", now="now: am / is / are", marks=[dict(at=-3, label="in 1990", text="I was a child."), dict(at=-1, label="yesterday", text="We were at home.")]),
        pattern=[
            ["+", "I / he / she / it", ["was", "v"], "at home."],
            ["+", "you / we / they", ["were", "v"], "in Paris."],
            ["−", "He", ["wasn't", "n"], "late. / They weren't late."],
            ["?", ["Where", "x"], ["were", "v"], "you born? — I was born in Rome."],
        ],
        examples=[
            "I {was} born in Cairo in 1995.",
            "My grandparents {were} farmers.",
            "Walid {wasn't} a good student. He {was} always in the kitchen!",
            "{Were} you at the concert? — Yes, I {was}.",
        ],
        ar=[
            "was و were هني الماضي تبع am / is / are.",
            "was مع I / he / she / it، و were مع you / we / they.",
            "منقول I was born (انولدت) — مو I born.",
        ],
        watch=[("I born in 1995.", "I was born in 1995."), ("They was at home.", "They were at home."), ("Were you born in Hama? — Yes, I were.", "Yes, I was.")],
        quick="""
## choose: Choose the answer.
I ___ born in Homs. | was | were | am
My parents ___ teachers. | were | was | are
___ you at home yesterday? | Were | Was | Are
""",
        sets="""
## choose: Choose the answer.
Walid ___ born in 1974. | was | were | is #id=a21u7-1febd37
My grandparents ___ farmers. | were | was | are
I ___ at the concert. I was at home. | wasn't | weren't | isn't
The film ___ fantastic! | was | were | is be
___ your father a journalist? | Was | Were | Be
Where ___ you born? | were | was | are
We ___ in Istanbul last summer. | were | was | are
It ___ cold yesterday. | was | were | be
They ___ at school this morning. They were ill. | weren't | wasn't | aren't
Was Mozart a composer? — Yes, he ___. | was | were | is
## gap: Write was, were, wasn't or weren't.
I [was] born in Damascus.
My parents [were] at work.
The museum [wasn't|was not] open yesterday.
[Were] you at the party?
We [weren't|were not] late — we were early!
Abu Firas [was] a postman.
The children [were] happy on Eid.
[Was] the exam difficult?
## short: Answer the question.
Were you born in Damascus? (✓) => Yes, I was.
Was Walid a good student? (✗) => No, he wasn't. | No, he was not.
Were they at home yesterday? (✓) => Yes, they were.
Was the concert good? (✗) => No, it wasn't. | No, it was not.
Were you at university in 2010? (✓) => Yes, I was.
Was your grandfather a doctor? (✗) => No, he wasn't. | No, he was not.
Was the weather nice? (✓) => Yes, it was.
Were your parents teachers? (✗) => No, they weren't. | No, they were not.
## fix: Find and fix the mistake.
I [born>was born] in Cairo.
They [was>were] at the market.
Where [you were>were you] born?
She [were>was] a journalist.
[Was>Were] you at home?
We [wasn't>weren't] late.
Yesterday it [is>was] very hot.
My grandparents [was>were] farmers.
## order: Put the words in order.
I was born in Hama.
Where were you born?
My parents were teachers.
He wasn't at work yesterday.
Were you at the concert?
The film was fantastic.
We were in Latakia last summer.
Was the exam difficult?
""",
    ),
    dict(
        id="g2",
        title="Past simple: regular verbs",
        visual=dict(type="compare", cols=[
            dict(title="+ ed / + d", color="teal", items=["work → worked", "move → moved", "decide → decided", "love → loved"]),
            dict(title="y → ied", color="purple", items=["study → studied", "marry → married"]),
            dict(title="double + ed", color="amber", items=["stop → stopped", "travel → travelled"]),
        ], cap="Same form for I, you, he, she, we, they"),
        pattern=[
            ["+", "I / you / he / she / we / they", ["worked", "v"], "in a bank."],
            ["+", "She", ["studied", "v"], "maths."],
            ["+", "They", ["moved", "v"], "to Damascus in 2015."],
        ],
        examples=[
            "My grandfather {worked} in a bank for forty years.",
            "We {moved} to Mezzeh in 2015.",
            "Ghada {studied} medicine and {graduated} in 2010.",
            "Hadi {decided} to open a phone shop.",
        ],
        ar=[
            "الماضي البسيط للأشياء اللي صارت وخلصت بوقت معروف: in 2015, last summer.",
            "الأفعال النظامية بتاخد ed: worked, moved، و study بتصير studied.",
            "نفس الشكل مع كل الأشخاص: I worked, she worked.",
        ],
        watch=[("I work in a bank in 2010.", "I worked in a bank in 2010."), ("She studyed law.", "She studied law."), ("We was move to Mezzeh.", "We moved to Mezzeh.")],
        quick="""
## choose: Choose the answer.
We ___ to Mezzeh in 2015. | moved | move | was move
She ___ medicine. | studied | studyed | study
I ___ in a bank last year. | worked | work | works
""",
        sets="""
## choose: Choose the answer.
My grandfather ___ in a bank for forty years. | worked | work | works
Ghada ___ from university in 2010. | graduated | graduate | graduates
They ___ to Dubai five years ago. | moved | move | moves
I ___ maths at university. | studied | studyed | study
Hadi ___ to open a phone shop. | decided | decide | decides
We ___ in Cairo when I was a child. | lived | live | was live
She ___ music when she was young. | loved | love | loves
The lesson ___ at nine this morning. | started | start | starts
My grandfather ___ coins. | collected | collect | collects
They ___ to Istanbul last summer. | travelled | travel | travels
## gap: Write the past simple.
I [moved] to Damascus five years ago. (move)
She [studied] law. (study)
We [lived] in Rome. (live)
He [worked] as a journalist. (work)
They [decided] to start a business. (decide)
The bus [stopped] near my house. (stop)
I [wanted] to be a pilot. (want)
Ghada [graduated] in 2010. (graduate)
## sort: How do you write it? | + ed / + d | y → ied | double + ed
+ ed / + d: worked, moved, decided, wanted
y → ied: studied, married, carried, tried
double + ed: stopped, travelled, planned, shopped
## transform: Change to the past.
I work in a bank. (last year) => I worked in a bank last year.
We live in Cairo. (in 2005) => We lived in Cairo in 2005.
She studies law. (at university) => She studied law at university.
They move to Dubai. (two years ago) => They moved to Dubai two years ago.
He decides to leave. (yesterday) => He decided to leave yesterday.
The film starts at nine. (yesterday) => The film started at nine yesterday.
I want a new phone. (last month) => I wanted a new phone last month.
My grandfather collects coins. (when he was young) => My grandfather collected coins when he was young.
## fix: Find and fix the mistake.
I [work>worked] in a bank in 2010.
She [studyed>studied] maths.
We [was moved>moved] to Mezzeh.
They [live>lived] in Homs ten years ago.
He [stoped>stopped] the car.
I [wantted>wanted] to be a pilot.
She [graduate>graduated] last year.
We [travel>travelled] to Rome last summer.
## order: Put the words in order.
I moved to Damascus five years ago.
She studied law at university.
My grandfather worked in a bank.
They decided to start a business.
We lived in Hama when I was a child.
He graduated in 2005.
I wanted to be a pilot.
The lesson started at nine.
""",
    ),
    dict(
        id="g3",
        title="Past simple: irregular verbs",
        visual=dict(type="table", head=["now", "past"],
                    rows=[["go", "went"], ["get", "got"], ["meet", "met"], ["have", "had"], ["leave", "left"], ["become", "became"],
                          ["make", "made"], ["take", "took"], ["begin", "began"], ["buy", "bought"]],
                    colors=["teal", "purple"], cap="Learn them by heart — see Irregular Verbs on the Home screen"),
        pattern=[
            ["+", "She", ["went", "v"], "to university in 2015."],
            ["+", "They", ["got", "v"], "married in 2012."],
            ["+", "I", ["met", "v"], "my wife at a wedding."],
        ],
        examples=[
            "Walid {left} school at sixteen.",
            "He {made} his first knafeh at fourteen.",
            "Rana and Kareem {met} at a wedding and {got} married in 2012.",
            "I {took} a lot of photos in Barcelona.",
        ],
        ar=[
            "في أفعال إلها شكل خاص بالماضي: go → went, get → got, meet → met.",
            "ما منزيدلها ed: went، مو goed.",
            "احفظها مع الصفحة Irregular Verbs بالتطبيق.",
        ],
        watch=[("I goed to Paris.", "I went to Paris."), ("She meeted her husband in 2010.", "She met her husband in 2010."), ("He taked a photo.", "He took a photo.")],
        quick="""
## choose: Choose the answer.
I ___ to Aleppo last week. | went | goed | go
They ___ married in 2012. | got | getted | get
She ___ a doctor in 2010. | became | becomed | become
""",
        sets="""
## choose: Choose the answer.
Walid ___ school at sixteen. | left | leaved | leave
I ___ my best friend at school. | met | meeted | meet
They ___ two children. | had | haved | have
He ___ his first knafeh at fourteen. | made | maked | make
She ___ a journalist in 2015. | became | becomed | become
We ___ a lot of photos. | took | taked | take
Hadi ___ a job in a phone shop. | got | getted | get
I ___ to university in 2018. | went | goed | go
The concert ___ at eight. | began | begined | begin
They ___ a flat in Mezzeh. | bought | buyed | buy
## gap: Write the past simple.
I [went] to Maaloula last summer. (go)
She [got] a job in 2019. (get)
We [met] at university. (meet)
He [left] school at sixteen. (leave)
They [had] a big party. (have)
I [took] a taxi to the airport. (take)
Walid [made] a fantastic knafeh. (make)
She [became] a journalist. (become)
## match: Match the verb and the past.
go = went
get = got
meet = met
have = had
leave = left
become = became
make = made
take = took
## fix: Find and fix the mistake.
I [goed>went] to Cairo.
She [meeted>met] her husband in 2010.
He [taked>took] a lot of photos.
They [buyed>bought] a car.
We [haved>had] a great time.
She [becomed>became] a teacher.
I [getted>got] a new job.
He [leaved>left] home at eighteen.
## bank: Use the words.
Walid [left] school at sixteen.
He [got] a job in his uncle's sweet shop.
He [made] his first knafeh at fourteen.
In 1998 he [started] a business.
He [met] his wife, Sana, at a wedding.
They [had] three children.
His shop [became] famous in Midan.
He [won] a prize for his knafeh.
## order: Put the words in order.
I went to university in 2018.
They got married in 2012.
She became a doctor.
He left school at sixteen.
We met at a wedding.
I took a lot of photos.
They had three children.
He made a fantastic cake.
""",
    ),
    dict(
        id="g4",
        title="Past time phrases",
        visual=dict(type="timeline", now="now", marks=[dict(at=-3, label="five years ago"), dict(at=-2, label="last summer"),
                                                      dict(at=-1, label="yesterday"), dict(at=0, label="this morning")]),
        pattern=[
            ["", "number + time +", ["ago", "v"], "two years ago, three days ago"],
            ["", ["last", "v"], "+ week / month / summer / year", "(no the!)"],
            ["", ["in", "s"], "+ year / month:", "in 2015, in May"],
            ["", ["when I was", "x"], "+ age / time:", "when I was ten"],
        ],
        examples=[
            "I moved to Damascus {five years ago}.",
            "We went to Athens {last summer}.",
            "{When I was} a child, I collected stamps.",
            "{On my last birthday}, my friends made a cake.",
        ],
        ar=[
            "ago بتجي بعد المدة: two years ago (من سنتين).",
            "last بلا the: last week، last summer.",
            "When I was… يعني لما كنت: When I was ten (لما كان عمري عشر سنين).",
        ],
        watch=[("before two years", "two years ago"), ("the last summer", "last summer"), ("When I was child", "When I was a child")],
        quick="""
## choose: Choose the answer.
I moved here three years ___. | ago | before | last
We went to Vienna ___ summer. | last | ago | the last
___ I was a child, I lived in Hama. | When | Ago | Last
""",
        sets="""
## choose: Choose the answer.
I started this job two years ___. | ago | before | last
We visited Barcelona ___ year. | last | ago | the last
She graduated ___ 2010. | in | on | ago
___ I was ten, I wanted to be a pilot. | When | Last | Ago
I saw Maya ___ morning. | this | last | ago
They got married ___ May. | in | on | last
I was at home ___. | yesterday | ago | last
He left school ___ he was sixteen. | when | ago | last
___ my last birthday, my friends made a cake. | On | In | At
We moved to Mezzeh five years ___. | ago | last | before
## bank: Use the words.
I moved to Damascus ten years [ago].
We went to Istanbul [last] summer.
She was born [in] 1999.
[When] I was a child, I lived in a village.
I had coffee with Hala [this] morning.
[On] my last birthday, I got a new watch.
I was at the gym [yesterday].
They met two weeks [ago].
## fix: Find and fix the mistake.
I moved here [before two years>two years ago].
We went to Tartus [the last>last] summer.
She was born [on>in] 1999.
[When I was child>When I was a child], I lived in Cairo.
I saw him [ago two days>two days ago].
They got married [in>on] the fifth of May.
I saw her [the yesterday>yesterday].
[In>On] my last birthday, I was in Beirut.
## order: Put the words in order.
I moved here two years ago.
We went to Athens last summer.
When I was a child, I lived in Hama.
She was born in 1999.
I saw Maya this morning.
On my last birthday, I was in Beirut.
They got married three years ago.
I was at the gym yesterday.
""",
    ),
]

CLASSROOM = dict(
    phrases=["What page are we on?", "When is the homework for?", "Can you explain that again, please?", "Sorry, I didn't hear you.",
             "I was absent last lesson.", "What did we do yesterday?", "Good luck!"],
    order="""
S: Sorry, I was absent last lesson.
T: That's OK. Were you ill?
S: Yes, I was. What did we do yesterday?
T: Irregular verbs: went, got, met…
S: Can you explain that again, please?
T: Of course. Look at page 64.
""",
)

READING = dict(
    title="Walid's story",
    text="""Walid was born in Midan in 1974. When he was a child, he loved sweets. He wasn't a good student — he was always in his uncle's sweet shop! He made his first knafeh when he was fourteen, and he left school at sixteen.

He got a job in his uncle's shop, and he worked there for ten years. In 1998, he decided to start his own business. He opened a small knafeh shop near his house. Two years later, he met Sana at a cousin's wedding, and they got married in 2001. They had three children: Layla, Ziad and Joud.

Walid's shop became famous in Midan. Five years ago, he won a prize for his knafeh. "It was a very special day," he says. "But my wedding day was special, too!" """,
    qs="""
## tf: True or false?
Walid was born in Midan. | T @ Walid was born in Midan in 1974
He was a very good student. | F @ He wasn't a good student
He left school at sixteen. | T @ he left school at sixteen
He met Sana at a wedding. | T @ he met Sana at a cousin's wedding
They had two children. | F @ They had three children
## choose: Choose the answer.
He started his business in ___. | 1998 | 1974 | 2001 @ In 1998, he decided to start his own business #id=a21u7-1b1d3c9
He worked in his uncle's shop for ___. | ten years | two years | five years @ he worked there for ten years
## gap: Write one word.
Five years ago, he won a [prize]. @ he won a prize for his knafeh
""",
)

DIALOGUE = dict(
    title="Family history",
    intro="Joud asks her grandmother about her life.",
    task="gaps",
    lines="""
Joud: Grandma, where [were] you born?
Grandmother: I was born in a village near Homs, sixty years [ago].
Joud: Wow! What was your first job?
Grandmother: I [was] a teacher. I taught maths for thirty years.
Joud: And when [was] your wedding?
Grandmother: In 1985. We [met] at my cousin's house.
Joud: Where were you and Grandpa when Dad was born?
Grandmother: We [were] in Damascus. We moved to Midan in 1986.
""",
)

WQ = """
In Hama. (Where / you / born) => Where were you born?
Yes, she was. (your grandmother / a teacher) => Was your grandmother a teacher?
In 2012. (When / their wedding) => When was their wedding?
No, it wasn't. It was easy. (the exam / difficult) => Was the exam difficult?
At home. (Where / you / yesterday) => Where were you yesterday?
Fantastic! (How / the concert) => How was the concert?
No, they weren't. They were in Beirut. (they / in Damascus / last week) => Were they in Damascus last week?
He was a journalist. (What / his job) => What was his job?
"""

WRITING = [
    dict(task="Write the life story of someone in your family (or a famous person): born, school, job, marriage, children, important moments.",
         tip="Use was / were, the past simple and time phrases: in 1990, when he was ten, two years ago. Write 80–110 words.",
         model="My grandfather, Abu Mazen, was born in a village near Hama in 1950. When he was a child, he loved horses. He left school at fourteen and he worked on his father's farm. In 1970 he moved to Damascus and got a job in a bakery. He met my grandmother at a wedding, and they got married in 1975. They had four children. In 1985 he started his own bakery in Midan. He worked there for thirty years. He was a kind and funny man.",
         check=["was born in + year / place", "regular past: worked, moved, started", "irregular past: left, got, met, had", "time phrases: in 1970, when he was a child, ago"],
         min=80, max=110),
]

CANDO = [
    "use was and were: I was born in…",
    "use the past simple of regular verbs.",
    "use irregular past forms: went, got, met, left.",
    "use past time phrases: ago, last summer, when I was…",
    "tell the life story of a person.",
]
