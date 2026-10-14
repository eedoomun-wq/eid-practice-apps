META = dict(n=5, title="Home and family", pages="36–41")

BOOK = """
husband, wife, parents, father, mother, children, son, daughter, brother, sister, grandparents, grandfather,
grandmother, grandchildren, grandson, granddaughter,
go to school, go to work by bus, go home for lunch, live in a flat, live in a house, live with your family,
work in an office, work for a big company, work long hours, have children, have a car, have two brothers,
study medicine, study at university, study languages,
medicine, engineering, business, at the weekend, speak, teach, alone, magazine
"""

WORDS = """
@Family
husband | the man you are married to | Kareem is Rana's husband.
wife | the woman you are married to | Rana is Kareem's wife.
parents | your mother and your father | My parents live in Midan. |  | par
father | your male parent | My father is a taxi driver. |  | par
mother | your female parent | Um Khaled is Khaled's mother. |  | par
children | sons and daughters | Rana and Kareem have two children. |  | child
son | your male child | Khaled is Um Khaled's son. |  | child
daughter | your female child | Joud is Rana's daughter. |  | child
brother | a boy or man with the same parents as you | I have two brothers. |  | sib-m
sister | a girl or woman with the same parents as you | Mais is Joud's sister. |  | sib-f
grandparents | the parents of your mother or father | My grandparents live in Sarouja. |  | gpar
grandfather | the father of your mother or father | Abu Firas is Joud's grandfather. |  | gpar
grandmother | the mother of your mother or father | My grandmother's kibbeh is fantastic! |  | gpar
grandchildren | the children of your son or daughter | Abu Firas and Hind have two grandchildren. |  | child
grandson | the son of your son or daughter | Khaled is Abu Salim's grandson. |  | child
granddaughter | the daughter of your son or daughter | Mais is Hind's granddaughter. |  | child
@Verbs + nouns
go to school | to be a student at a school every day | Joud and Mais go to school in Mezzeh.
go to work by bus | to travel to your job on a bus | I go to work by bus.
go home for lunch | to have your midday meal at home | Do you go home for lunch? — Yes, I do.
live in a flat | your home is in a big building | We live in a flat in Mezzeh.
live in a house | your home is a house | My grandparents live in a house with a courtyard.
live with your family | your home is with your parents, brothers… | Do you live with your family? — Yes, I do.
work in an office | your workplace is an office | I don't work in an office. I work in a shop.
work for a big company | your job is with a big business | They work for a big company in Dubai.
work long hours | to work a lot of hours every day | Nurses work long hours.
have children | to be a mother or father | Do you have children? — Yes, two.
have a car | a car is yours | We don't have a car. We go by service taxi.
have two brothers | two boys or men have the same parents as you | I have two brothers and one sister.
study medicine | to learn to be a doctor | I study medicine at Damascus University.
study at university | to be a student at a university | My sisters study at university.
study languages | to learn English, French, Turkish… | We study languages: English and French.
@Other words
medicine | the study of how to help sick people | Medicine is a long course.
engineering | the study of machines, roads and buildings | My brothers study engineering.
business | buying and selling | I study business in Aleppo.
at the weekend | on Friday and Saturday in Syria | We visit our grandparents at the weekend.
speak | to say words | I speak Arabic and English.
teach | to help people learn | I teach English in Mezzeh.
alone | with nobody | I don't live alone. I live with my family.
magazine | a thin book with photos; there's a new one every week or month | I read a magazine on the bus.
"""

ODD = """
mother, sister, daughter, *brother | Brother: a man. The others: women.
father, son, husband, *wife | Wife: a woman.
medicine, engineering, business, *magazine | Magazine: not a subject.
speak, teach, live, *alone | Alone: not a verb.
grandson, granddaughter, grandchildren, *parents | Parents: not grandchildren.
go to school, study at university, study languages, *have a car | Have a car: not about study.
car, bus, taxi, *son | Son: a person. #id=a11u5-0ebef98
"""

GRAMMAR = [
    dict(
        id="g1",
        title="possessive 's",
        visual=dict(type="tree", gen=[
            [dict(name="Abu Firas", cap="Rana's father"), dict(name="Hind", cap="Rana's mother")],
            [dict(name="Kareem", cap="Rana's husband"), dict(name="Rana", cap="Kareem's wife"), dict(name="Samer", cap="Rana's brother")],
            [dict(name="Joud", cap="Rana's daughter"), dict(name="Mais", cap="Joud's sister")],
        ], notes=["Joud is {Kareem's} daughter.", "Abu Firas is {Joud's} grandfather.", "Mais is {Samer's} niece — and Samer is her uncle!"]),
        pattern=[
            ["", "Rana", ["'s", "v"], "husband = Kareem"],
            ["", "Joud", ["'s", "v"], "sister = Mais"],
            ["", "my parents", ["'", "v"], "house (more than one: s')"],
            ["?", "Who's", "Joud's", "mother? — Rana."],
        ],
        examples=[
            "{Rana's} husband is Kareem.",
            "{Mais's} grandparents live in Mezzeh.",
            "{Walid's} knafeh shop is in Midan.",
            "My {parents'} flat is small. (two parents → s')",
        ],
        ar=[
            "بالإنكليزي ما منقول 'زوج رنا' متل العربي، منقول Rana's husband: صاحب الشي أول، بعدين 's.",
            "يعني الترتيب معكوس: بيت أبو فراس = Abu Firas's house.",
            "انتبه: 's بتجي كمان بمعنى is: Rana's a teacher = Rana is a teacher.",
            "إذا الصاحب جمع بـ s منحط بس ': my parents' car.",
        ],
        watch=[("the husband of Rana", "Rana's husband"), ("Kareem wife", "Kareem's wife"), ("my parent's house (two parents)", "my parents' house")],
        quick="""
## choose: Choose the answer.
Kareem is ___ husband. | Rana's | Rana | Ranas
Joud is ___ daughter. | Rana's | Rana's's | Ranas'
Mais is Joud's ___. | sister | brother | father
""",
        sets="""
## choose: Look at the family tree. Choose the answer.
Rana is Kareem's ___. | wife | husband | sister
Samer is Rana's ___. | brother | father | son
Abu Firas is Joud's ___. | grandfather | father | brother
Hind is Rana's ___. | mother | daughter | sister
Joud is Mais's ___. | sister | mother | brother
Kareem is Joud's ___. | father | grandfather | brother
Mais is Hind's ___. | granddaughter | daughter | mother
Abu Firas and Hind are Rana's ___. | parents | children | grandparents
Joud and Mais are Rana's ___. | children | parents | grandchildren
Samer is Mais's ___. | uncle | father | grandfather
## gap: Write the word with 's.
Kareem is [Rana's] husband. (Rana)
Joud is [Kareem's] daughter. (Kareem)
Hind is [Abu Firas's|Abu Firas'] wife. (Abu Firas)
Mais is [Joud's] sister. (Joud)
[Walid's] shop is in Midan. (Walid)
[Hadi's] phone is new. (Hadi)
Is this [Maya's] bag? (Maya)
[Tareq's] restaurant is in Qassaa. (Tareq)
## fix: Find and fix the mistake.
Kareem is [the husband of Rana>Rana's husband].
[Joud>Joud's] grandfather is Abu Firas.
This is [Hadi>Hadi's] car.
Samer is [Rana brother>Rana's brother].
[Maya's's>Maya's] café is in Baramkeh.
My [parent's>parents'] house is in Sarouja. (two parents)
Is [Layla>Layla's] brother a student?
[The name of my sister>My sister's name] is Hiba.
## transform: Write it with 's.
the husband of Rana => Rana's husband
the car of Fadi => Fadi's car
the sister of Joud => Joud's sister
the café of Hala => Hala's café
the son of Um Khaled => Um Khaled's son
the phone of Hadi => Hadi's phone
the school of Reem => Reem's school
the knafeh of Walid => Walid's knafeh
## order: Put the words in order.
Rana's husband is Kareem.
Joud's sister is Mais.
Is this Hadi's phone?
My mother's name is Hind.
Who's Joud's grandfather?
Walid's shop is in Midan.
Maya's café is small.
Kareem's wife is a teacher.
""",
    ),
    dict(
        id="g2",
        title="Present simple: I / you / we / they",
        visual=dict(type="timeline", now="today", marks=[dict(at=-2, label="Monday"), dict(at=0, label="today"), dict(at=2, label="Thursday")],
                    span={"from": -3, "to": 3, "label": "every day: I live, I work"}, cap="Present simple = true every day, again and again"),
        pattern=[
            ["+", "I / you / we / they", ["live", "v"], "in a flat."],
            ["−", "I / you / we / they", ["don't live", "n"], "in a house."],
            ["+", "We", ["work", "v"], "long hours."],
            ["−", "They", ["don't have", "n"], "a car."],
        ],
        examples=[
            "I {live} in a flat in Midan.",
            "We {go} to work by bus.",
            "They {don't have} a car.",
            "My parents {speak} Arabic and Turkish.",
        ],
        ar=[
            "المضارع البسيط منستعملو للأشياء اللي دايماً صحيحة أو للعادات: I live in Damascus.",
            "مع I و you و we و they الفعل بيضل متل ما هو: I work, we work, they work.",
            "للنفي منحط don't قبل الفعل: I don't live alone.",
            "انتبه: ما منحط am مع الفعل: I go، مو I am go.",
        ],
        watch=[("I am go to work by bus.", "I go to work by bus."), ("I no have a car.", "I don't have a car."), ("We are live in Mezzeh.", "We live in Mezzeh.")],
        quick="""
## choose: Choose the answer.
I ___ in a flat in Mezzeh. | live | am live | living
We ___ have a car. | don't | not | aren't
They ___ English and French. | speak | are speak | speaking
""",
        sets="""
## choose: Choose the answer.
I ___ to work by bus. | go | am go | going
We ___ in a house in Sarouja. | live | living | are live
They ___ for a big company. | work | working | are work
I ___ have children. | don't | not | no
You ___ English very well. | speak | speaking | are speak
My parents ___ live in Damascus. They live in Homs. | don't | aren't | not
We ___ at the weekend. | don't work | not work | aren't work
I ___ medicine at university. | study | studying | am study
They ___ a car. They go by service taxi. | don't have | no have | not have #id=a11u5-c22dd8f
I ___ English at a school in Mezzeh. | teach | teaching | am teach
## gap: Write the verb or don't.
I [live] in a flat. (live)
We [go] home for lunch. (go)
They [don't] work long hours. (−)
I [study] languages at university. (study)
You [have] two brothers. (have)
We [don't] live alone. (−)
My grandparents [speak] French. (speak)
I [don't] have a car. (−)
## transform: Make the sentence negative (−).
I live in a house. (−) => I don't live in a house. | I do not live in a house.
We have a car. (−) => We don't have a car. | We do not have a car.
They work in an office. (−) => They don't work in an office. | They do not work in an office.
I go home for lunch. (−) => I don't go home for lunch. | I do not go home for lunch.
You speak Turkish. (−) => You don't speak Turkish. | You do not speak Turkish.
My parents live alone. (−) => My parents don't live alone. | My parents do not live alone.
We study at the weekend. (−) => We don't study at the weekend. | We do not study at the weekend.
I teach English. (−) => I don't teach English. | I do not teach English.
## bank: Use the words.
We [live] in a flat in Mezzeh.
I [work] for a big company in Malki.
They [study] engineering at university.
I [speak] Arabic, English and a little Turkish.
We [have] two children, Joud and Mais.
I [teach] maths at a school in Dummar.
They [go] to school by bus.
I [read] a magazine on the bus.
## fix: Find and fix the mistake.
I [am live>live] in Midan.
We [no have>don't have] a car.
They [are work>work] long hours.
I [am study>study] medicine.
My parents [not live>don't live] alone.
You [are speak>speak] English very well!
We [are go>go] to work by bus.
I [not>don't] have a sister.
## order: Put the words in order.
I live in a flat.
We don't have a car.
They work for a big company.
I go to work by bus.
My parents live in Homs.
We don't work at the weekend.
I study languages at university.
They don't live alone.
""",
    ),
    dict(
        id="g3",
        title="Questions: Do you…? / Do they…?",
        visual=dict(type="table", head=["question", "yes", "no"],
                    rows=[["Do you live in Damascus?", "Yes, I do.", "No, I don't."], ["Do they have children?", "Yes, they do.", "No, they don't."],
                          ["Do we work at the weekend?", "Yes, we do.", "No, we don't."]],
                    colors=["purple", "teal", "coral"], cap="Do + I / you / we / they + verb?"),
        pattern=[
            ["?", ["Do", "v"], ["you", "s"], "live with your family?"],
            ["", "Yes, I", ["do.", "v"], ""],
            ["", "No, I", ["don't.", "n"], ""],
            ["?", ["Do", "v"], ["they", "s"], "have a car?"],
        ],
        examples=[
            "{Do you} live in a flat? — Yes, {I do}.",
            "{Do they} work long hours? — No, {they don't}.",
            "{Do you} speak French? — No, {I don't}. I speak English.",
            "{Do your parents} live in Aleppo? — Yes, {they do}.",
        ],
        ar=[
            "لنسأل بالمضارع البسيط منحط Do بالأول: Do you live…?",
            "الجواب القصير: Yes, I do. أو No, I don't. ما منكرر الفعل.",
            "انتبه: ما منقول Are you live…? منقول Do you live…?",
        ],
        watch=[("Are you live in Damascus?", "Do you live in Damascus?"), ("You have children?", "Do you have children?"), ("Yes, I live.", "Yes, I do.")],
        quick="""
## choose: Choose the answer.
___ you speak English? | Do | Are | Is
Do they live in Homs? — Yes, they ___. | do | are | live
Do you have a car? — No, I ___. | don't | haven't | not
""",
        sets="""
## choose: Choose the answer.
___ you live with your family? | Do | Are | Is
___ they work for a big company? | Do | Are | Is
Do you study medicine? — Yes, I ___. | do | study | am
Do your parents have a car? — No, they ___. | don't | aren't | haven't
___ you go home for lunch? | Do | Are | Have
Do we have homework? — Yes, we ___. | do | have | are
Do you speak Turkish? — No, I ___. | don't | not | no
___ your sisters study at university? | Do | Are | Is
Do they live alone? — No, they ___. | don't | aren't | not
___ you teach English? | Do | Are | Is
## short: Answer the question.
Do you live in a flat? (✓) => Yes, I do.
Do they have children? (✗) => No, they don't. | No, they do not.
Do you work long hours? (✓) => Yes, I do.
Do your parents speak English? (✗) => No, they don't. | No, they do not.
Do you study languages? (✓) => Yes, I do.
Do we have a test today? (✗) => No, we don't. | No, we do not.
Do they go to work by bus? (✓) => Yes, they do.
Do you live alone? (✗) => No, I don't. | No, I do not.
## transform: Make a question (?).
You live in Malki. (?) => Do you live in Malki?
They have a car. (?) => Do they have a car?
You work in an office. (?) => Do you work in an office?
They speak French. (?) => Do they speak French?
You go to school by bus. (?) => Do you go to school by bus?
Your grandparents live in Hama. (?) => Do your grandparents live in Hama?
You study engineering. (?) => Do you study engineering?
They work long hours. (?) => Do they work long hours?
## fix: Find and fix the mistake.
[Are>Do] you live in Damascus?
[You have>Do you have] children?
Do you speak English? — Yes, I [speak>do].
[Is>Do] they work at the weekend?
Do they have a car? — No, they [haven't>don't].
[Have>Do] you study medicine?
Do you live alone? — No, I [not>don't].
Do [they works>they work] in an office?
## order: Put the words in order.
Do you live with your family?
Do they have a car?
Do you speak French?
Do your parents live in Hama?
Do you go home for lunch?
Do they study at university?
Do you work long hours?
Do we have homework?
## match: Match the question and the answer.
Do you have a car? = No, I don't. I go by bus.
Do they live in a house? = Yes, they do. It's in Sarouja.
Do you speak Turkish? = Yes, I do. My mother is from Istanbul.
Do your children go to school? = Yes, they do. They're eight and five.
Do you work in an office? = No, I don't. I'm a driver.
Do they study medicine? = No, they don't. They study business.
Do you live alone? = No, I don't. I live with my parents.
Do we have homework? = Yes, we do. Page 40.
""",
    ),
]

CLASSROOM = dict(
    phrases=["Homework.", "See you tomorrow. / See you next lesson.", "I don't understand.", "What does … mean?",
             "Can you repeat that, please?", "Work in pairs.", "Is this right?"],
    order="""
T: Homework: page 40, exercises 1 and 2.
S: Sorry, can you repeat that, please?
T: Page forty, exercises one and two.
S: What does 'exercise' mean?
T: Practice: like this activity.
S: Thank you. See you tomorrow!
""",
)

READING = dict(
    title="Layla's family",
    text="""Hi! I'm Layla, and I'm twenty-one. I live with my family in a flat in Midan. My parents have a small knafeh shop near our flat. My father's name is Walid, and my mother's name is Sana.

I have one brother, Ziad. We study at Damascus University: I study medicine, and Ziad's subject is engineering. We don't have a car, so we go to university by bus. At the weekend, we go to our grandparents' house in Sarouja. My grandmother's food is fantastic! Do you live with your family, too?""",
    qs="""
## tf: True or false?
Layla: "I live alone." | F @ I live with my family
Layla: "My parents have a knafeh shop." | T @ My parents have a small knafeh shop
Layla's mother's name is Sana. | T @ my mother's name is Sana
Ziad's subject is medicine. | F @ Ziad's subject is engineering
Layla: "We have a car." | F @ We don't have a car
## choose: Choose the answer.
Where's the grandparents' house? | in Sarouja | in Midan | in Mezzeh @ our grandparents' house in Sarouja
To university: ___ | by bus | by car | by taxi @ we go to university by bus
## gap: Write one word.
Layla's father's name is [Walid]. @ My father's name is Walid
""",
)

DIALOGUE = dict(
    title="A new neighbour",
    intro="Mezzeh. Ghada and her new neighbour, Raj.",
    task="gaps",
    lines="""
Ghada: Hello! I'm Ghada. Do you [live] in this building?
Raj: Yes, I [do]. I live on the second floor.
Ghada: Nice to meet you. Do you live [alone]?
Raj: No, I live with my wife and our two [children].
Ghada: Do you work [near] here?
Raj: No, I [don't]. I work for a big company in Malki.
Ghada: And what's your [wife's] name?
Raj: Priya. She's a doctor, like you!
""",
)

WQ = """
Yes, I do. I live in Mezzeh. (live / in Damascus) => Do you live in Damascus?
No, they don't. They go by bus. (have / a car) => Do they have a car?
Yes, we do. Two daughters. (have / children) => Do you have children?
No, I don't. I speak English and Arabic. (speak / French) => Do you speak French?
Yes, I do. Two brothers. (have / brothers) => Do you have brothers? | Do you have any brothers?
Yes, they do. They work long hours. (work / for a big company) => Do they work for a big company?
Kareem. (who / Rana's husband) => Who's Rana's husband? | Who is Rana's husband?
No, I don't. I live with my parents. (live / alone) => Do you live alone?
"""

WRITING = [
    dict(task="Write about your family: who they are, where they live and their jobs.",
         tip="Use 's (my father's name…) and the present simple with I / we / they. Write 40–70 words.",
         model="My name's Hiba, and I'm twenty. I live with my parents and my sister in a flat in Jaramana. My father's name is Majd, and my mother's name is Lama. My parents work in a bank. My sister and I study at university. We don't have a car. My grandparents live in a house in Sarouja.",
         check=["'s: my father's name, my sister's job…", "I / we / they + verb: live, work, study…", "don't + verb", "family words: parents, brother, sister…"],
         min=40, max=70),
]

CANDO = [
    "talk about my family.",
    "use 's: Rana's husband, my father's name.",
    "talk about my day: I live, I work, I study.",
    "use don't: I don't have a car.",
    "ask 'Do you…?' and answer 'Yes, I do.' / 'No, I don't.'",
]
