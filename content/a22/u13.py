META = dict(n=13, title="Live and learn", pages="114–123")

BOOK = """
business studies, law, leisure and tourism, design and technology, economics, literature, engineering, maths,
media studies, geography, medicine, history, performing arts, information technology, languages, science,
get a degree, apply for a job, be unemployed, get into university, have an interview, choose a career, pass an exam,
train to be, do a course, earn money,
foreign language, internet access, video facilities, interactive whiteboards
"""

WORDS = """
@Subjects
business studies | the study of how companies work | Hala did business studies before she opened her café. | | subj-biz
law | the study of the rules of a country | Ziad studied law. Now he's a lawyer. | | subj-soc
leisure and tourism | the study of hotels, travel and free-time businesses | Leisure and tourism is a popular subject in Latakia. | | subj-biz
design and technology | making and designing things with materials and machines | We made a lamp in design and technology. | | subj-tech
economics | the study of money, trade and markets | Economics is a difficult subject. | | subj-biz
literature | the study of novels, poems and plays | Reem loves literature — she reads every day. | | subj-arts
engineering | designing machines, roads and buildings | Firas has a degree in engineering. | | subj-tech
maths | numbers and calculations | You have to be good at maths for engineering. | | subj-sci
media studies | the study of TV, newspapers and the internet | She did media studies and became a journalist. | | subj-arts
geography | the study of countries, mountains, rivers and weather | In geography, we learned about deserts. | | subj-soc
medicine | the study of how to be a doctor | Layla is studying medicine at Damascus University. | | subj-sci
history | the study of the past | History is my favourite subject. | | subj-soc
performing arts | music, dance and theatre | Maya would like to study performing arts. | | subj-arts
information technology | computers and how to use them (IT) | Hadi did a course in information technology. | | subj-tech
languages | English, French, Arabic, Turkish… | I'd like to study languages. | | subj-arts
science | physics, chemistry and biology | Science was Ghada's best subject at school. | | subj-sci
@School and careers
get a degree | to finish university with a qualification | You have to get a degree to be a doctor.
apply for a job | to ask a company for a job, often in writing | I'm going to apply for a job at the bank.
be unemployed | to have no job | My cousin is unemployed at the moment. | be unemployed;is unemployed
get into university | to be accepted by a university | You have to pass your exams to get into university.
have an interview | to meet a company and answer questions for a job | I have an interview on Monday!
choose a career | to decide what job to do in your life | It isn't easy to choose a career.
pass an exam | to get a good result in an exam | You have to pass an exam to get into university.
train to be | to learn the skills for a job | Salma trained to be a nurse.
do a course | to study for a short time | Hadi did a course in phone repair.
earn money | to get money for your work | Students often work in cafés to earn money.
@In a modern school
foreign language | a language from another country | Every student has to learn a foreign language.
internet access | being able to use the internet | The library has free internet access.
video facilities | rooms and machines for watching and making videos | Our school has good video facilities.
interactive whiteboards | big touch screens in classrooms | The classrooms have interactive whiteboards.
"""

ODD = """
maths, science, engineering, *apply for a job | Apply for a job: not a subject.
history, geography, literature, *interactive whiteboards | Interactive whiteboards: not a subject.
have to, has to, don't have to, *might | Might: not 'have to'.
will, might, won't, *has to | Has to: not will or might.
get a degree, pass an exam, do a course, *be unemployed | Be unemployed: no job.
law, medicine, economics, *video facilities | Video facilities: not a subject.
"""

GRAMMAR = [
    dict(
        id="g1",
        title="have to / don't have to",
        visual=dict(type="compare", cols=[
            dict(title="have to = it's necessary", color="coral", items=["Students {have to} wear a uniform.", "Doctors {have to} study for six years."]),
            dict(title="don't have to = it isn't necessary", color="teal", items=["You {don't have to} come on Friday.", "She {doesn't have to} work at the weekend."]),
        ], cap="he / she / it: has to · doesn't have to"),
        pattern=[
            ["+", "I / you / we / they", ["have to", "n"], "study hard."],
            ["+", "He / she", ["has to", "n"], "wear a uniform."],
            ["−", "You", ["don't have to", "v"], "pay. It's free."],
            ["?", ["Do", "v"], "I", "have to bring a dictionary? — No, you don't."],
        ],
        examples=[
            "To be a doctor, you {have to} study medicine for six years.",
            "Salma {has to} work at night.",
            "You {don't have to} pay for internet access in the library.",
            "{Do} we {have to} write this? — Yes, you do.",
        ],
        ar=[
            "have to يعني لازم / مضطر: I have to study.",
            "don't have to يعني مو لازم (مو ضروري)، مو 'ممنوع': You don't have to come.",
            "مع he / she: has to، وبالنفي doesn't have to.",
        ],
        watch=[("She have to work.", "She has to work."), ("I must to study. / I have study.", "I have to study."), ("You don't have to smoke here. (when you mean it's not allowed)", "You can't smoke here.")],
        quick="""
## choose: Choose the answer.
Doctors ___ study for a long time. | have to | has to | don't have
Salma ___ work at night. | has to | have to | have
You ___ pay. It's free. | don't have to | have to | doesn't have to
""",
        sets="""
## choose: Choose the answer.
Students ___ wear a uniform at my school. | have to | has to | having to
Ziad ___ wear a suit at work. | has to | have to | have
You ___ bring food. There's a café. | don't have to | have to | doesn't have to
___ we have to write this? | Do | Does | Are
Does Hadi have to work on Friday? — No, he ___. | doesn't | don't | hasn't
Nurses ___ work long hours. | have to | has to | need
My sister ___ get up early. Her school starts at seven. | has to | have to | is have to
We ___ pay for internet access. It's free. | don't have to | haven't to | doesn't have to
Do you have to ___ an interview? | have | has | having
She ___ have to study at the weekend. | doesn't | don't | isn't
## gap: Write have to, has to, don't have to or doesn't have to.
To get into university, you [have to] pass your exams.
Salma is a nurse. She [has to] work at night.
It's a holiday! We [don't have to|do not have to] go to school.
The museum is free. You [don't have to|do not have to] pay.
Hadi is the boss. He [doesn't have to|does not have to] ask anyone.
Lawyers [have to] study law.
My brother [has to] wear a uniform at his school.
Reem [doesn't have to|does not have to] cook — her mother cooks.
## transform: Make the sentence negative (−).
I have to work on Friday. (−) => I don't have to work on Friday. | I do not have to work on Friday.
She has to wear a uniform. (−) => She doesn't have to wear a uniform. | She does not have to wear a uniform.
We have to pay for the course. (−) => We don't have to pay for the course. | We do not have to pay for the course.
He has to get up early. (−) => He doesn't have to get up early. | He does not have to get up early.
You have to bring a dictionary. (−) => You don't have to bring a dictionary. | You do not have to bring a dictionary.
They have to do an exam. (−) => They don't have to do an exam. | They do not have to do an exam.
Students have to speak English in class. (−) => Students don't have to speak English in class. | Students do not have to speak English in class.
Rana has to work late. (−) => Rana doesn't have to work late. | Rana does not have to work late.
## transform: Make a question (?).
You have to wear a uniform. (?) => Do you have to wear a uniform?
She has to work at night. (?) => Does she have to work at night?
We have to write this. (?) => Do we have to write this?
He has to study maths. (?) => Does he have to study maths?
They have to pay. (?) => Do they have to pay?
Doctors have to study for six years. (?) => Do doctors have to study for six years?
Reem has to get up early. (?) => Does Reem have to get up early?
I have to bring my book. (?) => Do I have to bring my book?
## fix: Find and fix the mistake.
She [have>has] to work at night.
I [must to>have to] study.
He [don't>doesn't] have to wear a tie.
[Does>Do] you have to wear a uniform?
We [haven't to>don't have to] pay.
Does she have to [works>work] on Friday?
They [has>have] to pass an exam.
I have [study>to study] tonight.
## order: Put the words in order.
Students have to wear a uniform.
She has to work at night.
You don't have to pay.
Do we have to write this?
He doesn't have to get up early.
Doctors have to study for six years.
Does she have to wear a suit?
I have to pass my exams.
""",
    ),
    dict(
        id="g2",
        title="might and will",
        visual=dict(type="scale", items=[["won't", 0], ["might not", 35], ["might", 55], ["will probably", 80], ["will", 100]]),
        pattern=[
            ["+", "I", ["will", "v"], "pass the exam. (I'm sure.)"],
            ["+", "I", ["might", "x"], "study law. (Maybe.)"],
            ["−", "She", ["won't", "n"], "be late. (= will not)"],
            ["−", "We", ["might not", "n"], "go. (Maybe not.)"],
        ],
        examples=[
            "Reem studies every day. She{'ll} pass her exams.",
            "I {might} study medicine, or I {might} choose engineering.",
            "It's late. The shop {won't} be open now.",
            "Hadi {might not} come — he's very busy.",
        ],
        ar=[
            "will (رح) لما نكون متأكدين من المستقبل: She'll pass.",
            "might (يمكن / ممكن) لما ما نكون متأكدين: I might study law.",
            "won't = will not، و might not = يمكن لأ.",
            "بعد will و might الفعل بلا to وبلا s: She might come.",
        ],
        watch=[("I might to study law.", "I might study law."), ("She wills pass.", "She'll pass."), ("I will to go.", "I'll go.")],
        quick="""
## choose: Choose the answer.
I'm not sure. I ___ study law. | might | will | won't
She studies hard. She ___ pass. | 'll | might not | won't
It's midnight. The bank ___ be open. | won't | will | might
""",
        sets="""
## choose: Choose the answer.
I don't know. I ___ do a course this summer. | might | 'll definitely | won't
Reem always studies. She ___ pass her exams. | 'll | might not | won't
The shop closes at 8. It's 10 now. It ___ be open. | won't | will | might
Take an umbrella. It ___ rain. | might | won't | 'll not
I'm sure you ___ get the job! | 'll | might not | won't
He's very busy. He ___ come to the party. Maybe. | might not | 'll | will
We ___ have an interview next week — I'm not sure. | might | will | won't
Don't worry. I ___ forget. | won't | might | will
She ___ choose medicine or law. She can't decide. | might | 'll definitely | won't
In the future, all schools ___ have interactive whiteboards. I'm sure! | will | might not | won't
## gap: Write will, won't, might or might not.
I'm sure Reem [will|'ll] pass. (100%)
I [might] study languages. I'm not sure. (50%)
Hadi is ill. He [won't|will not] come today. (0%)
We [might not] go to the festival. Maybe. (35%)
Don't worry, I [will|'ll] help you. (100%)
It [might] snow tonight. (50%)
The exam [won't|will not] be easy. (0%)
She [might not] get into university. (35%)
## transform: Make it less sure with might.
I'll study law. => I might study law.
She'll get the job. => She might get the job.
It'll rain tomorrow. => It might rain tomorrow.
They won't come. => They might not come.
He'll choose engineering. => He might choose engineering.
We won't pass. => We might not pass.
The course will be expensive. => The course might be expensive.
I won't apply for the job. => I might not apply for the job.
## fix: Find and fix the mistake.
I [might to>might] study law.
She [wills>will|'ll] pass the exam.
I will [to go>go] to university.
He might [comes>come] tomorrow.
They [won't to>won't] be late.
It [mights>might] rain.
I [will not to>won't|will not] forget.
She might [not to>not] come.
## order: Put the words in order.
I might study law.
She'll pass her exams.
It won't be easy.
We might not go.
Hadi might come later.
I'll help you with your homework.
It might rain tomorrow.
They won't be late.
""",
    ),
    dict(
        id="g3",
        title="School and careers",
        visual=dict(type="chips", groups=[
            dict(title="subjects", color="purple", items=["maths", "science", "history", "geography", "literature", "languages", "IT", "economics"]),
            dict(title="university and work", color="teal", items=["get into university", "get a degree", "train to be", "do a course", "choose a career"]),
            dict(title="getting a job", color="amber", items=["apply for a job", "have an interview", "earn money", "be unemployed"]),
        ]),
        pattern=[
            ["", "First you", ["get into university.", "v"], ""],
            ["", "Then you", ["get a degree.", "v"], ""],
            ["", "After that, you", ["apply for a job", "x"], "and have an interview."],
        ],
        examples=[
            "To be a lawyer, you have to {get a degree} in {law}.",
            "Hadi {did a course} in {information technology}.",
            "I'm going to {apply for a job} at the bank. I'll {have an interview} next week.",
            "Salma {trained to be} a nurse in Aleppo.",
        ],
        ar=[
            "أسماء المواد: maths (رياضيات)، science (علوم)، history (تاريخ)، geography (جغرافيا)، literature (أدب).",
            "get into university = نفوت ع الجامعة، get a degree = ناخد شهادة.",
            "apply for a job = نقدّم ع شغل، be unemployed = بلا شغل.",
        ],
        watch=[("I applied to a job.", "I applied for a job."), ("I got a degree of law.", "I got a degree in law."), ("I made a course.", "I did a course.")],
        quick="""
## choose: Choose the answer.
I want to be a doctor. I'm going to study ___. | medicine | law | literature
You ___ for a job. | apply | make | do
She ___ a course in IT. | did | made | got
""",
        sets="""
## choose: What do they study?
"I want to be a lawyer." | law | geography | performing arts
"I want to build bridges." | engineering | literature | media studies
"I love novels and poems." | literature | economics | engineering
"I want to be a journalist on TV." | media studies | medicine | maths
"I want to work in a hotel." | leisure and tourism | law | science
"I want to be a dancer or an actor." | performing arts | economics | geography
"I want to repair computers." | information technology | history | literature
"I'm interested in the past." | history | science | IT
"I want to study mountains, rivers and countries." | geography | literature | law
"I want to be a doctor." | medicine | business studies | media studies
## choose: Choose the right verb.
You have to ___ into university first. | get | do | make
She ___ a degree in economics. | got | made | won #id=a22u13-4681385
I'm going to ___ for a job at the bank. | apply | do | make
He's going to ___ an interview tomorrow. | have | make | apply
I ___ a course in phone repair. | did | made | got
Students work in cafés to ___ money. | earn | win | make up
Salma ___ to be a nurse. | trained | earned | applied
It's difficult to ___ a career. | choose | take | pass
## match: Match.
get a degree = finish university
apply for a job = ask a company for work
be unemployed = have no job
have an interview = answer questions for a job
earn money = get money for your work
do a course = study for a short time
pass an exam = get a good result in an exam
foreign language = a language from another country
## bank: Use the words.
To be an engineer, you have to get [a degree].
I'm going to [apply] for a job at a bank.
My cousin is [unemployed] at the moment. He's looking for work.
Hadi did [a course] in information technology.
Salma [trained] to be a nurse.
Students often work in cafés to [earn] money.
The library has free internet [access].
Every student has to study one [foreign] language.
## order: Put the words in order.
I'm going to apply for a job.
She got a degree in law.
You have to pass the exam.
He did a course in IT.
It isn't easy to choose a career.
My brother is unemployed.
I have an interview on Monday.
She trained to be a nurse.
""",
    ),
]

CLASSROOM = dict(
    phrases=["I have to leave early today.", "Could you check my writing, please?", "Do we need to write this?", "When is the homework for?",
             "Have you finished?", "What do you think?", "I agree. / I don't agree."],
    order="""
S: Excuse me, I have to leave early today. I have an interview.
T: OK. Good luck! When is the homework for?
S: Sorry — that's my question! When is the homework for?
T: For Thursday. Now finish exercise 3, please.
S: Yes. Could you check my writing, please?
T: Of course. Hmm… very good!
""",
)

READING = dict(
    title="Choosing a career",
    text="""Reem is seventeen, and next year she'll finish secondary school. She has to choose a career, and it isn't easy.

"I love literature and languages," she says, "so I might study English literature at Damascus University. But my parents would like me to study medicine. Doctors have to study for six years, and they have to work long hours. I'm good at science, but I don't know…"

Her cousin, Firas, has a degree in engineering. "You don't have to decide now," he tells her. "First, you have to pass your exams and get into university. You might change your mind!"

Reem has a plan. This summer, she's going to do a course in translation. "I'll learn a lot, and I might earn some money with it later. Then I'll decide. One thing is sure — I won't stop reading!" """,
    qs="""
## tf: True or false?
Reem will finish secondary school next year. | T @ next year she'll finish secondary school
Reem's parents would like her to study medicine. | T @ my parents would like me to study medicine
Doctors have to study for four years. | F @ Doctors have to study for six years
Firas has a degree in engineering. | T @ Firas, has a degree in engineering
Reem has to decide today. | F @ You don't have to decide now
## choose: Choose the answer.
What is Reem going to do this summer? | a course in translation | a course in medicine | an interview @ she's going to do a course in translation
What does Firas say she has to do first? | pass her exams | choose a career | get a job @ First, you have to pass your exams
## gap: Write one word.
Reem says she won't stop [reading]. @ I won't stop reading
""",
)

DIALOGUE = dict(
    title="A job interview",
    intro="Hiba has an interview for a job at a language school.",
    task="gaps",
    lines="""
Manager: So, Hiba, have you got a degree?
Hiba: Yes. I [got] a degree in English literature last year.
Manager: Good. Do you speak a [foreign] language?
Hiba: Yes, English and a little French.
Manager: In this job, you [have] to work on Saturdays. Is that OK?
Hiba: Yes, that's fine. Do I [have] to wear a uniform?
Manager: No, you don't. But you have [to] arrive at eight.
Hiba: No problem. When will I [know] about the job?
Manager: We [might] call you this week — maybe next week.
""",
)

WQ = """
Yes, you do. It's the school rule. (I / have to / wear a uniform) => Do I have to wear a uniform?
No, she doesn't. It's her day off. (Salma / have to / work today) => Does Salma have to work today?
Engineering. (What / you / study) => What do you study? | What did you study? | What are you studying?
I might study law. (What / you / study / next year) => What will you study next year? | What are you going to study next year?
Yes, I'm sure she will. (Reem / pass her exams) => Will Reem pass her exams?
Next Monday. (When / your interview) => When's your interview? | When is your interview?
Maybe. I'm not sure. (it / rain / tomorrow) => Will it rain tomorrow?
For Thursday. (When / the homework / for) => When's the homework for? | When is the homework for?
"""

WRITING = [
    dict(task="Write about your studies or work: what you have to do and don't have to do, and your plans for the future (will / might).",
         tip="Use have to / don't have to, will / won't, might / might not. Write 80–120 words.",
         model="I'm a second-year economics student at Damascus University. On weekdays I have to get up at six, because my lectures start at eight. I have to read a lot and write reports, but I don't have to wear a uniform. I don't have to work, but I teach maths to two children to earn some money. Next year I'll finish my degree. After that, I might do a course in business studies, or I might apply for a job at a bank. I won't stop learning English!",
         check=["have to / has to", "don't have to / doesn't have to", "will / won't (sure)", "might / might not (not sure)"],
         min=80, max=120),
]

CANDO = [
    "say what I have to and don't have to do.",
    "use will for things I'm sure about.",
    "use might for things I'm not sure about.",
    "talk about school subjects and careers.",
    "answer questions in a job interview.",
]
