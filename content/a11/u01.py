META = dict(n=1, title="Nice to meet you", pages="6–13")

# The unit's book words ("Remember these words"). Numbers 0–20 are listed one by one.
BOOK = """
accountant, actor, architect, businessman/businesswoman, engineer, shop assistant, student, teacher,
zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen,
sixteen, seventeen, eighteen, nineteen, twenty,
name, first name, surname, number, phone number, email address, alphabet, spell, job, town, school, workplace,
hello, goodbye, How are you?, I'm fine, Nice to meet you!, See you again!
"""

WORDS = """
@Jobs
accountant | a person who works with money and numbers for a company | I'm an accountant.
actor | a person who works in films, on TV or in the theatre | Are you an actor? — Yes, I am!
architect | a person who draws plans for new houses and buildings | I'm an architect in Damascus.
businessman / businesswoman | a man / a woman who buys and sells for a company | I'm a businesswoman, and you're a businessman!
engineer | a person who designs and makes machines, roads or bridges | Are you an engineer, Hadi?
shop assistant | a person who helps people in a shop | I'm a shop assistant in Souq al-Hamidiyah.
student | a person who studies at a school or university | I'm a student at Damascus University.
teacher | a person who teaches students | Are you a teacher? — No, I'm not. I'm a student.
@Numbers 0–20
zero | the number 0 | My phone number? Zero, nine, four, four…
one | the number 1 | I'm student number one!
two | the number 2 | Room two? Room four?
three | the number 3 | One, two, three… go!
four | the number 4 | I'm in room four.
five | the number 5 | Five, four, three, two, one!
six | the number 6 | I'm number six in the class list.
seven | the number 7 | Seven? Are you sure?
eight | the number 8 | I'm in group eight.
nine | the number 9 | My phone number is zero, nine, three, three…
ten | the number 10 | Ten out of ten! Well done!
eleven | the number 11 | Are you in room eleven?
twelve | the number 12 | I'm on page twelve.
thirteen | the number 13 | My bus is number thirteen.
fourteen | the number 14 | I'm in room fourteen.
fifteen | the number 15 | Fifteen minutes, please!
sixteen | the number 16 | Page sixteen? OK!
seventeen | the number 17 | I'm student number seventeen.
eighteen | the number 18 | My number is eighteen.
nineteen | the number 19 | You're number nineteen.
twenty | the number 20 | Twenty out of twenty — fantastic!
@About you
name | the word for a person: Layla, Hadi, Rana… | My name's Layla. |  | name
first name | your name before your family name | My first name is Rana. |  | name
surname | your family name | What's your surname? — Haddad. |  | name
number | 1, 2, 3, 4 … | What's your number in the class list? — Number nine. |  | num
phone number | the numbers you call on a phone | My phone number is 0933 456 721. |  | num
email address | the address for your emails, with @ | My email address is nour.k@mail.com.
alphabet | the letters A, B, C … to Z | The English alphabet: A to Z!
spell | to say the letters of a word | How do you spell your name?
job | the work you do for money | What's your job? — I'm an engineer.
town | a small city | My town is Bloudan.
school | a place where children learn | My school is in Mezzeh.
workplace | the place where you work | My workplace is a bank in Malki.
@Hello and goodbye
hello | a word you say when you meet a person | Hello! I'm Kareem. |  | greet
goodbye | a word you say when you leave | Goodbye, Rana! See you again! |  | bye
How are you? | a question to ask if a person is well | Hi, Hadi! How are you?
I'm fine | an answer that says "I am well" | How are you? — I'm fine, thanks.
Nice to meet you! | what you say to a new person | I'm Maya. — Nice to meet you, Maya! |  | greet
See you again! | what you say when you leave a person, for next time | Goodbye, Abu Salim! See you again! |  | bye
"""

WORDSETS = """
## numbers: Write the number in words.
7 => seven
12 => twelve
3 => three
15 => fifteen
0 => zero
19 => nineteen
8 => eight
13 => thirteen
20 => twenty
11 => eleven
## numbers: Write the number.
fourteen => 14
six => 6
eighteen => 18
nine => 9
seventeen => 17
two => 2
sixteen => 16
ten => 10
"""

ODD = """
teacher, student, actor, *seven | Seven: a number, not a job.
one, nine, *name, twelve | Name: not a number.
hello, goodbye, *engineer, See you again! | Engineer: a job, not hello or goodbye.
surname, first name, *architect, name | Architect: a job.
town, school, workplace, *goodbye | Goodbye: not a place.
accountant, engineer, architect, *alphabet | Alphabet: A, B, C… not a job.
businessman, businesswoman, shop assistant, *phone number | Phone number: not a job.
"""

GRAMMAR = [
    dict(
        id="g1",
        title="I'm / you're · my / your",
        visual=dict(type="table", head=["", "be", "short form", "my / your"],
                    rows=[["I", "am", "I'm", "my name"], ["you", "are", "you're", "your name"]],
                    colors=["teal", "purple", "purple", "amber"],
                    cap="I + am · you + are"),
        pattern=[
            ["+", "I", "'m", "Layla."],
            ["−", "I", "'m not", "a teacher."],
            ["+", "You", "'re", "in room 5."],
            ["?", ["Are", "v"], ["you", "s"], "a student?"],
            ["", "My name", "'s", "Rana. What's your name?"],
        ],
        examples=[
            "{I'm} Layla. {I'm} a student.",
            "{Are you} Hadi? — Yes, {I am}.",
            "{My} name's Rana. What's {your} name?",
            "{I'm not} an actor. {I'm} an accountant.",
        ],
        ar=[
            "بالإنكليزي ما فينا نحذف الفعل: لازم نقول I am، مو بس I.",
            "منستعمل am مع I بس، و are مع you.",
            "my يعني تبعي، و your يعني تبعك: my name = اسمي.",
            "بالسؤال منقدّم الفعل: Are you…?",
        ],
        en=[
            "Say the verb: I'm Layla. (not: I Layla.)",
            "I → am. You → are.",
            "my = mine. your = yours.",
        ],
        watch=[("I Layla.", "I'm Layla."), ("You student?", "Are you a student?"), ("I are a teacher.", "I'm a teacher.")],
        quick="""
## choose: Choose the answer.
I ___ Kareem. | 'm | 're | are
___ you a teacher? | Are | Am | I'm
What's ___ name? — Rana. | your | you | you're
""",
        sets="""
## choose: Choose the answer.
I ___ a student. | am | are | you
You ___ in room 3. | 're | 'm | am
___ name's Hadi. | My | I | I'm
Are you Maya? — Yes, I ___. | am | are | 'm
I ___ not an actor. | 'm | 're | are
What's ___ phone number? | your | you | you're
___ you an engineer? | Are | Am | I
Hello, I ___ Layla. | 'm | are | 're
Nice to meet ___! | you | your | you're
I'm from Istanbul. And ___? | you | your | I
## gap: Write am or are.
I [am|'m] a teacher.
You [are|'re] a student.
[Are] you Nour?
I [am|'m] not from Paris.
Yes, I [am].
[Are] you from Aleppo?
I [am|'m] in room 12.
You [are|'re] in group 4.
## gap: Write my or your.
Hello! [My] name's Abu Salim.
What's [your] name?
What's [your] job, Rana?
[My] phone number is 0944 213 800.
Hi! I'm Dima. [My] job? I'm a teacher.
[My] surname is Haddad.
What's [your] email address?
[My] first name is Kareem.
## order: Put the words in order.
I'm a student.
Are you an engineer?
My name's Layla.
What's your name?
I'm not a teacher.
You're in room 7.
Are you from Cairo?
What's your phone number?
## fix: Find and fix the mistake.
I [Layla>'m Layla|am Layla] Haddad.
[You>Are you] a student?
I [are>am|'m] an engineer.
[I>My] name's Hadi.
What's [you>your] surname?
You [is>are|'re] in room 2.
I'm [no>not] a teacher.
[Am>Are] you from London?
## short: Answer with Yes, I am or No, I'm not.
Are you a student? (✓) => Yes, I am.
Are you a teacher? (✗) => No, I'm not. | No, I am not.
Are you from Beirut? (✓) => Yes, I am.
Are you an actor? (✗) => No, I'm not. | No, I am not.
Are you in room 4? (✓) => Yes, I am.
Are you Kareem? (✗) => No, I'm not. | No, I am not.
Are you OK? (✓) => Yes, I am. #id=a11u1-bfd0c81
Are you an architect? (✗) => No, I'm not. | No, I am not.
## transform: Make the sentence negative (−).
I'm a teacher. (−) => I'm not a teacher. | I am not a teacher.
I'm from Tokyo. (−) => I'm not from Tokyo. | I am not from Tokyo.
You're in room 9. (−) => You aren't in room 9. | You're not in room 9. | You are not in room 9.
I'm an actor. (−) => I'm not an actor. | I am not an actor.
You're a student. (−) => You aren't a student. | You're not a student. | You are not a student.
I'm fine. (−) => I'm not fine. | I am not fine.
You're Hadi. (−) => You aren't Hadi. | You're not Hadi. | You are not Hadi.
I'm in group 3. (−) => I'm not in group 3. | I am not in group 3.
""",
    ),
    dict(
        id="g2",
        title="a / an with jobs",
        visual=dict(type="compare", cols=[
            dict(title="a + consonant sound", color="teal", items=["a teacher", "a student", "a businessman", "a shop assistant"], note="b, c, d, s, t…"),
            dict(title="an + vowel sound", color="purple", items=["an actor", "an engineer", "an architect", "an accountant"], note="a, e, i, o, u"),
        ], cap="Listen to the first sound of the job."),
        pattern=[
            ["+", "I", "'m", ["a", "x"], "teacher."],
            ["+", "I", "'m", ["an", "n"], "engineer."],
            ["?", ["Are", "v"], ["you", "s"], ["an", "n"], "actor?"],
        ],
        examples=[
            "I'm {a} shop assistant in Souq al-Hamidiyah.",
            "Are you {an} architect? — No, I'm {a} student.",
            "I'm {an} accountant in Mezzeh.",
            "You're {an} engineer in Dubai.",
        ],
        ar=[
            "قبل الوظيفة لازم نحط a أو an: I'm a teacher، مو I'm teacher.",
            "منحط an قبل الكلمة اللي بتبلش بصوت a, e, i, o, u: an actor, an engineer.",
            "وباقي الكلمات بتاخد a: a student, a shop assistant.",
        ],
        en=[
            "Before a job, say {a} or {an}: I'm {a} teacher.",
            "First sound a, e, i, o, u → {an}: {an} actor.",
            "Other jobs → {a}: {a} student, {a} shop assistant.",
        ],
        watch=[("I'm teacher.", "I'm a teacher."), ("I'm a engineer.", "I'm an engineer."), ("I'm an student.", "I'm a student.")],
        quick="""
## choose: Choose a or an.
I'm ___ actor. | an | a
I'm ___ student. | a | an
Are you ___ engineer? | an | a
""",
        sets="""
## sort: a or an? | a | an
a: teacher, student, businessman, businesswoman, shop assistant
an: actor, engineer, architect, accountant, email address
## choose: Choose a or an.
I'm ___ teacher. | a | an
Are you ___ accountant? | an | a
I'm ___ shop assistant. | a | an
I'm not ___ actor. | an | a
You're ___ businesswoman. | a | an
I'm ___ architect in Aleppo. | an | a
Are you ___ student? | a | an
I'm ___ engineer. | an | a
You're ___ businessman. | a | an
I'm not ___ teacher. I'm ___ student. | a / a | an / an | a / an
## gap: Write a or an.
I'm [an] engineer.
Are you [a] teacher?
I'm [a] student in Damascus.
You're [an] actor!
I'm [an] accountant.
Are you [an] architect?
I'm [a] businessman.
I'm not [a] shop assistant.
## choose: What's the job?
"Books, students and a classroom: I'm ___." | a teacher | an actor | a businessman
"Films and TV: I'm ___." | an actor | an accountant | a student
"Plans for new houses: I'm ___." | an architect | a shop assistant | a teacher
"Money and numbers for a company: I'm ___." | an accountant | an actor | an engineer
"Clothes, a shop and customers: I'm ___." | a shop assistant | an architect | a teacher
"University and exams: I'm ___." | a student | an engineer | an actor
"Machines and roads: I'm ___." | an engineer | a student | a shop assistant
"Buying and selling for my company: I'm ___." | a businesswoman | an actor | a student
## fix: Find and fix the mistake.
I'm [teacher>a teacher].
I'm [a>an] engineer.
You're [an>a] student.
Are you [accountant>an accountant]?
I'm [a>an] actor.
I'm not [an>a] shop assistant.
I'm [architect>an architect] in Hama.
You're [an>a] businessman.
## order: Put the words in order.
I'm an architect.
Are you a teacher?
I'm not an actor.
You're a shop assistant.
I'm a student in Rome.
Are you an accountant?
I'm an engineer.
You're not a businessman. || You aren't a businessman.
""",
    ),
    dict(
        id="g3",
        title="The alphabet · How do you spell …?",
        visual=dict(type="letters", groups=[
            ["A H J K", "like 'say'"], ["B C D E G P T V", "like 'see'"], ["F L M N S X Z", "like 'yes'"],
            ["I Y", "like 'my'"], ["O", "like 'no'"], ["Q U W", "like 'you'"], ["R", "like 'car'"],
        ], cap="Letters in one line have the same sound."),
        pattern=[
            ["?", "How do you spell", ["your name?", "r"]],
            ["+", ["K-A-R-E-E-M", "x"]],
            ["+", ["Double L:", "v"], ["H-E-L-L-O", "x"]],
        ],
        examples=[
            "How do you spell your name? — {R-A-N-A}.",
            "How do you spell 'teacher'? — {T-E-A-C-H-E-R}.",
            "'Hello' — H-E-{double L}-O.",
            "My surname is Saleh: {S-A-L-E-H}.",
        ],
        ar=[
            "لما بدك تسأل كيف بتنكتب الكلمة منقول: How do you spell …?",
            "منلفظ الأحرف حرف حرف: K-A-R-E-E-M.",
            "انتبه: E متل 'إي'، و I متل 'آي'، و A متل 'إيه'.",
            "إذا في حرفين متل بعض منقول double: double L.",
        ],
        en=[
            "Ask: How do you spell your name?",
            "Say the letters one by one: K-A-R-E-E-M.",
            "Careful: E = 'see', I = 'my', A = 'say'.",
            "Two letters the same? Say double: double L.",
        ],
        watch=[("How you spell your name?", "How do you spell your name?"), ("H-E-L-O (hello)", "H-E-double L-O"), ("E sounds like 'eye'.", "I sounds like 'eye'.")],
        quick="""
## choose: Choose the answer.
How do you spell 'name'? | N-A-M-E | N-E-M-A | M-A-N-E
Same sound as B: | C | F | O
Same sound as A: | K | E | I
""",
        sets="""
## choose: Same sound? Choose the letter.
Same sound as A: | J | E | Q
Same sound as B: | D | F | R
Same sound as F: | S | E | Y
Same sound as I: | Y | E | A
Same sound as Q: | U | K | G
Same sound as E: | V | I | A
Same sound as M: | N | E | H
Same sound as K: | H | X | C
Same sound as T: | P | L | I
Same sound as L: | X | E | Y
## spell: Write the word.
T-E-A-C-H-E-R => teacher
A-C-T-O-R => actor
S-T-U-D-E-N-T => student
E-N-G-I-N-E-E-R => engineer
S-U-R-N-A-M-E => surname
H-E-L-L-O => hello
T-O-W-N => town
S-C-H-O-O-L => school
J-O-B => job
N-A-M-E => name
## spell: Write the name.
L-A-Y-L-A => Layla
K-A-R-E-E-M => Kareem
H-A-D-I => Hadi
R-A-N-A => Rana
N-O-U-R => Nour
M-A-Y-A => Maya
D-I-M-A => Dima
J-A-D => Jad
S-A-L-M-A => Salma
G-H-A-D-A => Ghada
## sort: Sort the letters by sound. | like 'say' | like 'see' | like 'yes'
like 'say': A, H, J, K
like 'see': B, C, D, P
like 'yes': F, L, M, N
## choose: How do you spell it?
How do you spell 'student'? | S-T-U-D-E-N-T | S-T-O-D-E-N-T | S-T-U-D-A-N-T
How do you spell 'engineer'? | E-N-G-I-N-E-E-R | I-N-G-I-N-E-E-R | E-N-G-E-N-I-R
How do you spell 'actor'? | A-C-T-O-R | A-K-T-O-R | A-C-T-E-R
How do you spell 'goodbye'? | G-O-O-D-B-Y-E | G-U-D-B-A-Y | G-O-D-B-Y-E
How do you spell 'twelve'? | T-W-E-L-V-E | T-W-I-L-V-E | T-W-E-L-F
How do you spell 'phone'? | P-H-O-N-E | F-O-N-E | P-H-O-N
How do you spell 'eight'? | E-I-G-H-T | A-I-T | E-G-H-I-T
How do you spell 'eleven'? | E-L-E-V-E-N | I-L-E-V-E-N | E-L-E-F-E-N
## order: Put the words in order.
How do you spell your name?
How do you spell your surname?
How do you spell 'hello'?
What's your first name?
How do you spell 'job'?
My surname is Kassem.
How do you spell 'Damascus'?
What's your email address?
""",
    ),
]

CLASSROOM = dict(
    phrases=["Hello. / Good morning.", "Sorry I'm late.", "Can I come in?", "I don't understand.",
             "How do you spell …?", "What's … in English?", "Open your books.", "Close your books.", "Listen.", "Repeat."],
    order="""
S: Good morning. Sorry I'm late.
T: OK. Come in, please.
S: Thank you.
T: Open your books. Page 8.
S: Sorry, I don't understand.
T: Open your books — page eight.
""",
)

READING = dict(
    title="Hello from Bab Touma",
    text="""Hello! I'm Hadi Saleh. I'm from Bab Touma in Damascus. I'm not a student. I'm an engineer, and my workplace is a phone shop in Bab Touma.

My phone number is 0933 17 18 19, and my email address is hadi.fix@mail.com. Are you a student? Are you an engineer, too? Nice to meet you!""",
    qs="""
## choose: Choose the answer.
Hadi: "I'm ___." | an engineer | a student | a teacher @ I'm an engineer
Hadi: "I'm from ___." | Damascus | Aleppo | Homs @ I'm from Bab Touma in Damascus
Email address: | hadi.fix@mail.com | hadi.fax@mail.com | hadi@fix.com @ hadi.fix@mail.com
## tf: True or false?
Hadi: "I'm a student." | F @ I'm not a student
Hadi: "My workplace is a phone shop." | T @ my workplace is a phone shop
Hadi: "I'm from Bab Touma." | T @ I'm from Bab Touma
Hadi: "My surname is Haddad." | F @ I'm Hadi Saleh
## numbers: Write the number.
Phone number: 0933 17 18 ___ => 19 | nineteen @ 0933 17 18 19
""",
)

DIALOGUE = dict(
    title="A new student",
    intro="Rana and Kareem meet at an English class in Mezzeh.",
    task="both",
    lines="""
Rana: Hello! I'm Rana. What's your [name]?
Kareem: Hi, Rana. My name's Kareem. Nice to [meet] you.
Rana: Nice to meet you, [too]. Are you a student?
Kareem: No, I'm [not]. I'm a businessman. And you?
Rana: I'm [a] teacher.
Kareem: How do you [spell] your surname?
Rana: H-A-D-D-A-D.
Kareem: Thanks, Rana. See you [again]!
""",
)

WQ = """
My name's Hadi. => What's your name?
I'm fine, thanks. => How are you?
No, I'm not. I'm an architect. (a teacher?) => Are you a teacher?
My phone number is 0944 551 203. => What's your phone number?
S-A-L-M-A. (spell / your name) => How do you spell your name?
My email address is reem@mail.com. => What's your email address?
I'm an accountant. (your job) => What's your job?
Yes, I am. I'm from Homs. (from Homs?) => Are you from Homs?
"""

WRITING = [
    dict(task="Write about you. Write your name, your job, your town and a phone number (you can invent one).",
         tip="Use I'm, my and a / an. Write 20–40 words.",
         model="Hello! My name's Nour Haddad. I'm a pharmacist. I'm from Damascus, and my workplace is a pharmacy in Sha'lan. My phone number is 0955 12 34 56. Nice to meet you!",
         check=["I'm … (= I am)", "a or an + my job", "my name, my job, my phone number", "A capital letter at the start of a sentence, a full stop (.) at the end"],
         min=20, max=40),
    dict(task="A new student in your class! Write a short dialogue: hello, the name, the job, goodbye.",
         tip="Use Hello, What's your name?, Are you a …?, Nice to meet you!, See you again!",
         model="A: Hello! I'm Maya. What's your name?\nB: Hi, Maya. I'm Jad. Nice to meet you.\nA: Nice to meet you, too. Are you a student?\nB: No, I'm not. I'm a shop assistant. And you?\nA: I'm a student. See you again!",
         check=["Hello … and goodbye …", "What's your name?", "a question with 'Are you …?'", "a or an + job"],
         min=25, max=60),
]

CANDO = [
    "say hello and goodbye.",
    "say my name and my job.",
    "use a and an with jobs.",
    "spell my name in English.",
    "say the numbers 0 to 20.",
    "ask 'What's your phone number?'",
]

# ---- Puzzles (round 2): the case, the escape room texts, What am I? riddles.
# The crossword, word search, escape locks and Guess the word are built from the unit data.
PUZZLES = dict(
    case=dict(
        title="Sami, what's your job?",
        story="You're new in an office building in Malki. Hello, Lana, Sami and Yara! Three jobs, three rooms: 7, 12 and 15.",
        people=["Lana", "Sami", "Yara"],
        groups=[["accountant", "architect", "engineer"], ["7", "12", "15"]],
        group_names=["job", "room"],
        clues=[
            dict(t="The engineer: \"My workplace is room 12.\"", f=("is", "engineer", "12")),
            dict(t="Yara: \"I'm in room 15.\"", f=("is", "Yara", "15")),
            dict(t="Yara: \"I'm not an engineer.\"", f=("not", "Yara", "engineer"), need=False),
            dict(t="Lana: \"I'm not in room 7.\"", f=("not", "Lana", "7")),
            dict(t="Yara: \"I'm not an accountant.\"", f=("not", "Yara", "accountant")),
            dict(t="Sami: \"I'm not in room 15.\"", f=("not", "Sami", "15"), need=False),
        ],
        question=dict(q="Sami, what's your job?", target="Sami", among=0),
        reveal="Sami: \"I'm an accountant. My workplace is room 7.\" Lana: \"I'm an engineer, in room 12.\" Yara: \"And I'm an architect, in room 15!\"",
    ),
    escape=dict(
        place="Bait Nizam",
        intro="You're in Bait Nizam, a beautiful old house in Damascus. But the big door? Not open! Open the locks, please.",
        ending="Fantastic — you're out! Goodbye, Bait Nizam. See you again!",
    ),
    riddles=[
        ("teacher", ["My workplace is a school, but I'm not a student.", "Books, a board and twenty students: my day!", "\"Open your books, please!\" — I'm the person at the board."]),
        ("architect", ["I'm in an office with a pen and big paper.", "My work: plans for new houses and buildings.", "A new house in Mezzeh? My plan first!"]),
        ("engineer", ["I'm in an office, on a road or on a bridge.", "Machines, roads and bridges: my work!", "Hadi Saleh from Bab Touma and me: the same job!"]),
        ("actor", ["I'm a doctor today and a king tomorrow!", "My workplace: the theatre, TV or a film.", "Duraid Lahham — Ghawar! — and me: the same job."]),
        ("alphabet", ["I'm a long line of letters.", "My first letter: A. My last letter: Z.", "A, B, C, D, E… I'm all the letters!"]),
        ("surname", ["I'm a name, but not your first name.", "Haddad? Saleh? Nasser? Yes, me!", "I'm your family name."]),
        ("email address", ["I'm not a phone number, but I'm for messages.", "My letters, a dot… and @!", "hadi.fix@mail.com — me!"]),
    ],
)
