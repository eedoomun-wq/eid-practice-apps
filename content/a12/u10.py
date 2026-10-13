META = dict(n=10, title="Famous lives", pages="72–79")

BOOK = """
leave (primary/secondary) school, go to university, leave university, pass your driving test, get your first job,
start a business, meet your partner/someone, get married, buy a house or flat, have children,
artist, musician, singer, fashion designer, writer, architect, inventor, film director, dancer,
special, computer scientist, prize, award, TV show, search engine, plane, bridge, jewellery
"""

WORDS = """
@Life events
leave (primary/secondary) school | to finish your time at school | Layla left secondary school in 2023. | leave school;left school;leave secondary school;left secondary school
go to university | to start studying at a university | She went to university in Damascus. | go to university;went to university
leave university | to finish at university | Hadi left university after one year. | leave university;left university
pass your driving test | to get a "yes" in the test for a driving licence | Jad passed his driving test at eighteen. | pass your driving test;passed his driving test
get your first job | to start work for the first time | I got my first job in a bank. | get your first job;got my first job
start a business | to open your own company or shop | Kareem started a business in 1995. | start a business;started a business
meet your partner/someone | to see a person for the first time and love them | My parents met at university. | meet your partner;met at university;meet someone;met someone
get married | to become husband and wife | Rana and Kareem got married in 2012. | get married;got married
buy a house or flat | to pay for a home | They bought a flat in Mezzeh. | buy a house;buy a flat;bought a flat;bought a house
have children | to become a mother or father | They had two children, Joud and Mais. | have children;had two children;had children
@Creative jobs
artist | a person who paints or draws pictures | Reem's aunt is an artist.
musician | a person who plays music as a job | My uncle was a musician. He played the oud.
singer | a person who sings as a job | Fairuz is a famous Lebanese singer.
fashion designer | a person who makes new clothes styles | Dima's sister is a fashion designer in Paris.
writer | a person who writes books | Nizar Qabbani was a famous Syrian writer of poems.
architect | a person who plans buildings | The architect finished the new library in 2019.
inventor | a person who makes something new for the first time | An inventor made the first telephone.
film director | a person who makes films | The film director worked in Cairo.
dancer | a person who dances as a job | Lina was a dancer before she was a teacher.
@Other words
special | different and important | Her wedding was a very special day.
computer scientist | a person who studies how computers work | Wei is a computer scientist.
prize | something you get when you win | Walid won a prize for his knafeh.
award | a prize, often for important work | The film won an award in 2015.
TV show | a programme on TV | The TV show about cooking was very popular.
search engine | a website that finds things for you on the internet | Google is a search engine.
plane | it flies in the sky and carries people | We travelled to Dubai by plane.
bridge | it goes over a river or a road | There's an old bridge over the Orontes.
jewellery | rings, necklaces, earrings | My grandmother's jewellery is from Souq al-Hamidiyah.
"""

ODD = """
artist, musician, singer, *bridge | Bridge: not a person.
went, had, met, *start | Start: not past.
played, worked, lived, *bought | Bought: irregular.
writer, dancer, inventor, *prize | Prize: not a job.
got married, had children, bought a house, *search engine | Search engine: not a life event.
plane, bridge, search engine, *jewellery | Jewellery: you wear it.
studied, tried, carried, *stayed | Stayed: y stays (stay → stayed).
"""

GRAMMAR = [
    dict(
        id="g1",
        title="Past simple: regular verbs",
        visual=dict(type="compare", cols=[
            dict(title="+ ed / + d", color="teal", items=["work → worked", "play → played", "live → lived", "dance → danced"]),
            dict(title="y → ied", color="purple", items=["study → studied", "try → tried", "carry → carried"]),
            dict(title="double + ed", color="amber", items=["stop → stopped", "travel → travelled", "plan → planned"]),
        ], cap="Past simple = finished time: yesterday, in 1990, last year"),
        pattern=[
            ["+", "I / you / he / she / we / they", ["worked", "v"], "in a bank."],
            ["−", "I / you / he / she / we / they", ["didn't work", "n"], "on Friday."],
            ["", "(didn't + verb, no -ed)", "", ""],
        ],
        examples=[
            "Abu Firas {worked} as a postman for thirty-five years.",
            "We {lived} in Beirut in 2010.",
            "Layla {studied} English at school.",
            "Kareem {didn't travel} last year. He {stayed} in Damascus.",
        ],
        ar=[
            "الماضي البسيط للأشياء اللي خلصت بوقت معروف: yesterday, in 2010.",
            "الأفعال النظامية منزيدلها ed: worked, played. وstudy بتصير studied.",
            "الماضي نفسه مع كل الأشخاص: I worked, she worked — بلا s.",
            "للنفي: didn't + الفعل بلا ed: I didn't work، مو I didn't worked.",
        ],
        watch=[("I didn't worked.", "I didn't work."), ("She work yesterday.", "She worked yesterday."), ("I was work in a bank.", "I worked in a bank."),
               ("He studyed medicine.", "He studied medicine.")],
        quick="""
## choose: Choose the answer.
I ___ in a bank in 2015. | worked | work | was work
She ___ English at university. | studied | studyed | study
We didn't ___ on Friday. | work | worked | works
""",
        sets="""
## choose: Choose the answer.
Abu Firas ___ as a postman. | worked | works | was work
My parents ___ in Dubai in 1990. | lived | live | was live
Maya ___ the guitar at the party. | played | plaied | play
I ___ English at school. | studied | studyed | studies
The film ___ at nine o'clock. | started | start | was start
We ___ to Istanbul last year. | travelled | travels | travel
Hadi didn't ___ his phone. | answer | answered | answers
They ___ dinner at Um Khaled's house. | cooked | cook | cooks
The bus ___ in front of the station. | stopped | stoped | stops
I didn't ___ the film. | like | liked | likes
## gap: Write the past simple.
Rana [worked] in a school in Mezzeh. (work)
We [lived] in a small flat. (live)
Layla [studied] hard for the exam. (study)
The concert [started] at eight. (start)
Hadi [stopped] the car. (stop)
I [watched] a film yesterday. (watch)
They [travelled|traveled] to Cairo in 2019. (travel)
Joud [tried] knafeh for the first time. (try)
## transform: Make the sentence negative (−).
I worked on Friday. (−) => I didn't work on Friday. | I did not work on Friday.
She liked the film. (−) => She didn't like the film. | She did not like the film.
We stayed at home. (−) => We didn't stay at home. | We did not stay at home.
They played football. (−) => They didn't play football. | They did not play football.
He studied medicine. (−) => He didn't study medicine. | He did not study medicine.
The shop opened at nine. (−) => The shop didn't open at nine. | The shop did not open at nine.
I cooked dinner. (−) => I didn't cook dinner. | I did not cook dinner.
Maya danced at the party. (−) => Maya didn't dance at the party. | Maya did not dance at the party.
## sort: Sort the verbs. | + ed / + d | y → ied | double + ed
+ ed / + d: worked, played, lived, danced
y → ied: studied, tried, carried, married
double + ed: stopped, travelled, planned, shopped
## fix: Find and fix the mistake.
I [work>worked] in a bank in 2015.
She didn't [worked>work] yesterday.
He [studyed>studied] at Damascus University.
We [was live>lived] in Homs.
The bus [stoped>stopped] here.
They [didn't liked>didn't like] the film.
My grandfather [play>played] the oud.
I [no watched>didn't watch] TV yesterday.
## order: Put the words in order.
I worked in a bank in 2015.
She didn't like the film.
We travelled to Istanbul last year.
My grandfather played the oud.
They lived in Aleppo.
He didn't study medicine.
The shop opened at nine.
I watched a film yesterday.
""",
    ),
    dict(
        id="g2",
        title="Past simple: irregular verbs",
        visual=dict(type="table", head=["now", "past"],
                    rows=[["go", "went"], ["have", "had"], ["meet", "met"], ["buy", "bought"], ["get", "got"], ["leave", "left"],
                          ["become", "became"], ["win", "won"], ["write", "wrote"], ["make", "made"]],
                    colors=["teal", "purple"], cap="Irregular verbs: learn them one by one!"),
        pattern=[
            ["+", "She", ["went", "v"], "to university in 2005."],
            ["+", "They", ["got", "v"], "married in 2012."],
            ["−", "He", ["didn't go", "n"], "to university."],
            ["", "(didn't + go, not didn't went)", "", ""],
        ],
        examples=[
            "Nizar Qabbani {wrote} a lot of love poems.",
            "Rana and Kareem {met} at a wedding and {got} married in 2012.",
            "Walid {won} a prize for his knafeh.",
            "Hadi {didn't go} to university. He {started} a business.",
        ],
        ar=[
            "في أفعال ما بتاخد ed، إلها شكل خاص بالماضي: go → went, have → had.",
            "هي الأفعال لازم نحفظها، شوف قائمة Irregular Verbs بالصفحة الرئيسية.",
            "بالنفي منرجع للفعل الأصلي: I didn't go، مو I didn't went.",
        ],
        watch=[("I goed to Dubai.", "I went to Dubai."), ("She didn't went.", "She didn't go."), ("We buyed a flat.", "We bought a flat.")],
        quick="""
## choose: Choose the answer.
We ___ to Istanbul last summer. | went | goed | go
I ___ my first job in 2018. | got | getted | get
She didn't ___ a car. | buy | bought | buyed
""",
        sets="""
## choose: Choose the answer.
Rana and Kareem ___ at a wedding. | met | meeted | meet
I ___ a flat in Jaramana. | bought | buyed | buy
They ___ married in 2012. | got | getted | get
Walid ___ a prize for his knafeh. | won | winned | win
Nizar Qabbani ___ a lot of poems. | wrote | writed | write
She ___ school in 2019. | left | leaved | leave
We ___ two children. | had | haved | have
He ___ a famous singer. | became | becomed | become
I didn't ___ to the party. | go | went | goed
Tareq ___ a big kibbeh for the competition. | made | maked | make
## gap: Write the past simple.
Layla [went] to university in 2023. (go)
Abu Salim [bought] a new taxi. (buy)
We [had] a party for Eid. (have)
I [met] my best friend at school. (meet)
Maya [left] the café at ten. (leave)
Jad [got] his first job at nineteen. (get)
Reem [wrote] a story for school. (write)
Hala [became] a café owner in 2020. (become)
## match: Match the verb and the past.
go = went
have = had
meet = met
buy = bought
get = got
leave = left
win = won
write = wrote
## transform: Make the sentence negative (−).
I went to the cinema. (−) => I didn't go to the cinema. | I did not go to the cinema.
She bought a car. (−) => She didn't buy a car. | She did not buy a car.
They had children. (−) => They didn't have children. | They did not have children.
He won the prize. (−) => He didn't win the prize. | He did not win the prize.
We met at university. (−) => We didn't meet at university. | We did not meet at university.
I got the job. (−) => I didn't get the job. | I did not get the job.
She left school at sixteen. (−) => She didn't leave school at sixteen. | She did not leave school at sixteen.
He wrote a book. (−) => He didn't write a book. | He did not write a book.
## fix: Find and fix the mistake.
I [goed>went] to Dubai last week.
She didn't [went>go] to school.
We [buyed>bought] a new car.
They [meeted>met] in 2010.
He [get>got] married in 2015.
I didn't [had>have] breakfast.
Tareq [maked>made] a fantastic dinner.
She [winned>won] the competition.
## bank: Use the words.
Kareem [started] a business in 1995.
Rana and Kareem [got] married in 2012.
They [bought] a flat in Mezzeh.
Hadi [left] university after one year.
Jad [passed] his driving test at eighteen.
My parents [met] at university.
Layla [went] to university in 2023.
They [had] two children.
""",
    ),
]

CLASSROOM = dict(
    phrases=["What's the answer to number 3?", "I think it's …", "Can I ask a question?", "How do you say this word?",
             "Whose turn is it?", "You go first.", "Well done!"],
    order="""
S: Can I ask a question?
T: Of course.
S: How do you say this word: b-o-u-g-h-t?
T: 'Bought'. It's the past of 'buy'.
S: Thank you! What's the answer to number 3?
T: I think you know it. Try!
""",
)

READING = dict(
    title="A famous life: Nizar Qabbani",
    text="""Nizar Qabbani was a famous Syrian poet. He was born in Damascus in 1923. He grew up in an old house with a beautiful courtyard and a lot of jasmine.

He studied law at Damascus University and left university in 1945. After that, he worked for the government in a lot of countries: in Egypt, in Turkey, in England, in Spain and in China. But he didn't stop writing. He wrote a lot of love poems, and they became very popular. Famous singers sang his poems.

Later, he lived in London. He died there in 1998, but people in Syria and in the Arab world still love his poems today.""",
    qs="""
## tf: True or false?
Nizar Qabbani was born in Aleppo. | F @ He was born in Damascus in 1923
He studied law. | T @ He studied law at Damascus University
He worked only in Syria. | F @ he worked for the government in a lot of countries
He stopped writing. | F @ he didn't stop writing
Famous singers sang his poems. | T @ Famous singers sang his poems
## choose: Choose the answer.
He left university in ___. | 1945 | 1923 | 1998 @ left university in 1945
Where was his house in Damascus? | an old house with a courtyard | a new flat | a hotel @ an old house with a beautiful courtyard
## gap: Write one word.
He died in [London] in 1998. @ Later, he lived in London. He died there in 1998
""",
)

DIALOGUE = dict(
    title="How was your weekend?",
    intro="Sunday morning at work. Nour and Ghada.",
    task="gaps",
    lines="""
Nour: Hi, Ghada! How [was] your weekend?
Ghada: Great, thanks! I [went] to Maaloula with my family.
Nour: Lovely! Was it cold?
Ghada: Yes, it was. We [stayed] in a small hotel. And you?
Nour: Oh, I didn't [go] out. I was very tired.
Ghada: So what about Friday?
Nour: I [watched] an old film, and I cooked mahshi for my parents.
Ghada: Mmm! I [love] mahshi!
""",
)

WQ = """
Great, thanks! (How / your weekend) => How was your weekend?
Yes, he was. He was a famous poet. (Nizar Qabbani / famous) => Was Nizar Qabbani famous?
In 1923. (When / he / born) => When was he born?
No, they weren't. They were at home. (they / at the party) => Were they at the party?
They were at Damascus University. (Where / your parents / in 1990) => Where were your parents in 1990?
I'm a writer. (What / you / do) => What do you do?
It's a search engine. (What / Google) => What's Google? | What is Google?
Yes, she is. She's a fashion designer. (your sister / a designer) => Is your sister a designer?
"""

WRITING = [
    dict(task="Write about the life of a person in your family: when they were born, school, first job, marriage, children.",
         tip="Use the past simple: was born, went, left, got, met, had. Write 60–90 words.",
         model="My grandfather, Abu Mazen, was born in Hama in 1950. He went to school in Hama, and he left school at sixteen. He got his first job in a bakery. In 1972 he moved to Damascus. He met my grandmother at a wedding, and they got married in 1975. They had four children. He started a small business, and he worked there for forty years.",
         check=["was born in + year", "regular verbs: worked, moved, started", "irregular verbs: went, got, met, had", "didn't + verb (no -ed)"],
         min=60, max=90),
]

CANDO = [
    "use the past simple of regular verbs: worked, studied.",
    "use irregular past forms: went, had, met, bought.",
    "use didn't + verb.",
    "talk about life events.",
    "write a short life story.",
]
