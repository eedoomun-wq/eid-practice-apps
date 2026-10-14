META = dict(n=1, title="People and places", pages="6–15")

BOOK = """
Australian, Japanese, Polish, Brazilian, Chinese, Russian, British, Spanish, Irish, American, Italian, Vietnamese,
actor, lawyer, businessman, musician, police officer, businesswoman, shop assistant, doctor, engineer, singer,
footballer, waiter,
mobile number, address, friend, really, married, single, student, name, on business, tourist, on holiday
"""

WORDS = """
@Nationalities
Australian | from Australia | Hannah's husband is Australian. He's from Sydney. | | nat
Japanese | from Japan | Kenji is Japanese. He's an engineer in Tokyo. | | nat
Polish | from Poland | Olga isn't Russian. She's Polish, from Warsaw. | | nat
Brazilian | from Brazil | Carlos is Brazilian. He's a footballer in Rio. | | nat
Chinese | from China | Mei is Chinese, and her husband is Japanese. | | nat
Russian | from Russia | Is your teacher Russian? | | nat
British | from the UK: England, Scotland, Wales or Northern Ireland | James is British. He's from London. | | nat
Spanish | from Spain | Lucía isn't Spanish. She's from Argentina. | | nat
Irish | from Ireland | My friend Sean is Irish. He's from Dublin. | | nat
American | from the USA | The tourists in Bab Touma are American. | | nat
Italian | from Italy | Marco is Italian. He's a waiter in Rome. | | nat
Vietnamese | from Vietnam | Pho is a Vietnamese soup. | | nat
+Syrian | from Syria | I'm Syrian, and I'm from Damascus. | | nat
@Jobs
actor | a person who acts in films or plays | Is he an actor? He's very famous! | | job
lawyer | a person who knows the law and helps people in court | Ziad is a lawyer in Malki. | | job
businessman | a man who works in business | Kareem is a businessman. | | job
musician | a person who plays music as a job | Is she a musician? — Yes, she plays the oud. | | job
police officer | a person who works for the police | The police officer is very friendly. | | job
businesswoman | a woman who works in business | Hala is a businesswoman. She has a café. | | job
shop assistant | a person who helps customers in a shop | I'm a shop assistant in a clothes shop. | | job
doctor | a person who helps sick people | Ghada is a doctor at a hospital in Mezzeh. | | job
engineer | a person who designs machines, roads or buildings | Firas is an engineer. | | job
singer | a person who sings as a job | Fairuz is a famous singer. | | job
footballer | a person who plays football as a job | Messi is a famous footballer. | | job
waiter | a person who brings food to the tables in a restaurant | The waiter at Al-Nofara café is very fast. | | job
@About people
mobile number | the number of your phone | What's your mobile number?
address | the street, number and town where you live | What's your address? — 12 Baghdad Street, Damascus.
friend | a person you like and know well | Maya is my friend from university.
really | very | The café is really nice.
married | with a husband or wife | Rana is married. Her husband is Kareem. | | mar
single | not married | Hadi is single. | | mar
student | a person who studies | Are you a student? — Yes, I'm a law student.
name | what people call you | What's your name?
on business | travelling for your job | Is he on holiday? — No, he's on business. | | trip
tourist | a person on holiday in another place | There are a lot of tourists in Maaloula.
on holiday | travelling for fun, not for work | We're on holiday in Tartus. | | trip
"""

ODD = """
Irish, British, American, *Ireland | Ireland: a country, not a nationality.
lawyer, doctor, waiter, *married | Married: not a job.
married, single, *tourist | Tourist: a person, not married or single.
Polish, Russian, Japanese, *student | Student: not a nationality.
footballer, singer, musician, *mobile number | Mobile number: not a job.
am, is, are, *be from | Be from: not a form of be.
actor, engineer, architect, *police officer | Police officer: 'a', not 'an'.
"""

GRAMMAR = [
    dict(
        id="g1",
        title="be: am / is / are",
        visual=dict(type="table", head=["", "+", "−", "short"],
                    rows=[["I", "am", "am not", "I'm / I'm not"], ["you / we / they", "are", "aren't", "you're / we're / they're"],
                          ["he / she / it", "is", "isn't", "he's / she's / it's"]],
                    colors=["teal", "purple", "coral", "amber"], cap="Every English sentence needs a verb: am / is / are"),
        pattern=[
            ["+", "I", "'m", "a lawyer."],
            ["+", "She", "'s", "Irish."],
            ["−", "They", "aren't", "on holiday."],
            ["−", "He", "isn't", "married."],
        ],
        examples=[
            "{I'm} Syrian, and {I'm} from Midan.",
            "Olga {isn't} Russian. {She's} Polish.",
            "Ghada and Samer {are} doctors.",
            "The tourists {aren't} on business. {They're} on holiday.",
        ],
        ar=[
            "بالعربي منقول 'أنا محامي' بلا فعل، بس بالإنكليزي لازم am / is / are.",
            "am مع I، و is مع he / she / it، و are مع you / we / they.",
            "للنفي: I'm not، isn't، aren't.",
        ],
        watch=[("She doctor.", "She's a doctor."), ("They is Brazilian.", "They're Brazilian."), ("I'm not single, I'm marry.", "I'm not single. I'm married.")],
        quick="""
## choose: Choose the answer.
Mei ___ Chinese. | is | are | am
We ___ on holiday. | 're | 's | 'm
Hadi ___ married. He's single. | isn't | aren't | not
""",
        sets="""
## choose: Choose the answer.
James ___ British. | is | are | am
My parents ___ teachers. | are | is | am
I ___ not a lawyer. | 'm | 's | 're
The waiter ___ really friendly. | is | are | be
Lucía and Carlos ___ from Argentina. | are | is | am
It ___ a Vietnamese restaurant. | 's | 're | 'm
We ___ tourists. We live here. | aren't | isn't | not
Sean ___ Irish. | is | are | be
You ___ really late! | 're | 's | 'm
Rana ___ single. She's married. | isn't | aren't | not
## gap: Write am, is or are.
I [am|'m] a student.
Firas [is|'s] an engineer.
Kenji and Mei [are] in Tokyo.
The hotel [is|'s] really nice.
You [are|'re] my best friend.
We [are|'re] from Cairo.
My mobile number [is|'s] 0933 245 718.
Marco [is|'s] a waiter.
## gap: Write isn't, aren't or 'm not.
Olga [isn't|is not] Russian.
I ['m not|am not] married.
They [aren't|are not] on business.
Hadi [isn't|is not] a doctor.
We [aren't|are not] British.
The café [isn't|is not] expensive.
I ['m not|am not] a tourist.
You [aren't|are not] late.
## transform: Make the sentence negative (−).
She's a lawyer. (−) => She isn't a lawyer. | She's not a lawyer. | She is not a lawyer.
They're on holiday. (−) => They aren't on holiday. | They're not on holiday. | They are not on holiday.
I'm Irish. (−) => I'm not Irish. | I am not Irish.
He's married. (−) => He isn't married. | He's not married. | He is not married.
We're students. (−) => We aren't students. | We're not students. | We are not students.
It's a Japanese car. (−) => It isn't a Japanese car. | It's not a Japanese car. | It is not a Japanese car.
You're a footballer. (−) => You aren't a footballer. | You're not a footballer. | You are not a footballer.
The tourists are American. (−) => The tourists aren't American. | The tourists are not American.
## fix: Find and fix the mistake.
She [doctor>'s a doctor|is a doctor].
They [is>are|'re] Brazilian.
I [is>am|'m] a police officer.
My friends [isn't>aren't] here.
He [not>isn't|is not] married.
We [am>are|'re] on business.
Ziad [are>is|'s] a lawyer.
[Are>Is] she from Poland?
## order: Put the words in order.
I'm not married.
She's a police officer.
They're on holiday in Athens.
We aren't British.
My mobile number is 0944 312 678.
He isn't a waiter.
The tourists are really friendly.
It's a Japanese car.
""",
    ),
    dict(
        id="g2",
        title="a / an with jobs",
        visual=dict(type="compare", cols=[
            dict(title="a + consonant sound", color="teal", items=["a doctor", "a lawyer", "a waiter", "a musician", "a police officer"]),
            dict(title="an + vowel sound", color="purple", items=["an actor", "an engineer", "an artist", "an accountant", "an architect"]),
        ], cap="Plural jobs: no a / an — They're doctors."),
        pattern=[
            ["+", "She's", ["a", "x"], "lawyer."],
            ["+", "He's", ["an", "n"], "actor."],
            ["+", "They're", "", "waiters. (no a / an)"],
        ],
        examples=[
            "Ziad is {a} lawyer, and his wife is {an} engineer.",
            "I'm {a} shop assistant in Sha'lan.",
            "Is he {an} actor? — No, he's {a} singer.",
            "Ghada and Salma are {doctors}. (plural: no a)",
        ],
        ar=[
            "قبل الوظيفة منحط a أو an: She's a doctor، مو She's doctor.",
            "an قبل الصوت a, e, i, o, u: an engineer, an actor.",
            "بالجمع ما منحط a: They're doctors.",
        ],
        watch=[("He's lawyer.", "He's a lawyer."), ("She's a engineer.", "She's an engineer."), ("They're a doctors.", "They're doctors.")],
        quick="""
## choose: Choose the answer.
She's ___ lawyer. | a | an | —
He's ___ actor. | an | a | —
They're ___ waiters. | — (nothing) | a | an
""",
        sets="""
## choose: Choose the answer.
Ziad is ___ lawyer. | a | an | —
I'm ___ engineer. | an | a | —
Is Hala ___ businesswoman? | a | an | —
My sister is ___ actor. | an | a | —
They're ___ footballers. | — (nothing) | a | an
He's ___ police officer. | a | an | —
Ghada is ___ doctor. | a | an | —
Is Sean ___ Irish musician? | an | a | —
We're ___ students. | — (nothing) | a | an
She's ___ accountant. | an | a | —
## sort: a or an? | a | an
a: doctor, lawyer, waiter, singer, police officer, footballer
an: actor, engineer, artist, accountant, architect, Irish singer
## gap: Write a, an or x (= nothing).
Marco is [a] waiter.
I'm [an] engineer.
They're [x|nothing] doctors.
She's [an] actor.
He's [a] shop assistant.
We're [x|nothing] musicians.
Firas is [an] architect.
Is she [a] lawyer?
## choose: What's the job?
"I help sick people in a hospital." | a doctor | an actor | a waiter
"I bring food to tables in a restaurant." | a waiter | a lawyer | an engineer
"I play football for a big team." | a footballer | a musician | a police officer
"I help people with the law." | a lawyer | a singer | a waiter
"I play the oud in a band." | a musician | an engineer | a doctor
"I work for the police." | a police officer | a shop assistant | an actor
"I sell clothes in a shop." | a shop assistant | a footballer | a lawyer
"I'm in films and on TV." | an actor | a police officer | a waiter
## fix: Find and fix the mistake.
He's [lawyer>a lawyer].
She's [a>an] engineer.
They're [a doctors>doctors].
I'm [an>a] musician.
Is he [actor>an actor]?
We're [a students>students].
My father is [a>an] architect.
She's [an>a] waiter.
## order: Put the words in order.
She's a lawyer in Malki.
He's an engineer.
They're doctors.
Is your sister an actor?
I'm a shop assistant.
My brother is a police officer.
We're not musicians. || We aren't musicians.
Is he a famous footballer?
""",
    ),
    dict(
        id="g3",
        title="Questions with be",
        visual=dict(type="table", head=["question", "answer"],
                    rows=[["Are you married?", "Yes, I am. / No, I'm not."], ["Is she Irish?", "Yes, she is. / No, she isn't."],
                          ["Where are you from?", "I'm from Rome."], ["What's your job?", "I'm a lawyer."], ["How old is he?", "He's thirty."]],
                    colors=["purple", "teal"], cap="Questions: put am / is / are before the person"),
        pattern=[
            ["?", ["Are", "v"], ["you", "s"], "married?"],
            ["", "Yes, I", ["am.", "v"], "/ No, I'm not."],
            ["?", ["Where", "x"], ["is", "v"], "she from?"],
            ["?", ["What", "x"], ["'s", "v"], "your mobile number?"],
        ],
        examples=[
            "{Are you} on holiday? — No, {I'm not}. I'm on business.",
            "{Is} Sean British? — No, {he isn't}. He's Irish.",
            "{Where are} your parents from? — They're from Hama.",
            "{What's} your address? — 15 Baghdad Street.",
        ],
        ar=[
            "بالسؤال منقدّم am / is / are قبل الشخص: Are you married?",
            "مع كلمات السؤال: Where are you from? What's your job? How old is she?",
            "بالجواب القصير ما منختصر الإيجاب: Yes, I am، مو Yes, I'm.",
        ],
        watch=[("You are married?", "Are you married?"), ("Where you are from?", "Where are you from?"), ("Yes, I'm.", "Yes, I am.")],
        quick="""
## choose: Choose the answer.
___ you a student? | Are | Is | Am
Where ___ Mei from? | is | are | be
Is he married? — No, he ___. | isn't | not | aren't
""",
        sets="""
## choose: Choose the answer.
___ she a lawyer? | Is | Are | Am
___ they on holiday? | Are | Is | Be
Where ___ you from? | are | is | am
What ___ your mobile number? | 's | are | am
Are you single? — Yes, I ___. | am | 'm | is
Is Kenji Chinese? — No, he ___. | isn't | not | aren't
How old ___ your children? | are | is | be
___ I late? | Am | Is | Are
Are they American? — Yes, they ___. | are | 're | is
Who ___ your English teacher? | 's | are | am
## short: Answer the question.
Are you a student? (✓) => Yes, I am.
Is Olga Russian? (✗) => No, she isn't. | No, she's not. | No, she is not.
Are they on business? (✓) => Yes, they are.
Is the hotel expensive? (✗) => No, it isn't. | No, it's not. | No, it is not.
Is Ziad a lawyer? (✓) => Yes, he is.
Are you married? (✗) => No, I'm not. | No, I am not.
Are your parents from Cairo? (✓) => Yes, they are.
Is Marco Spanish? (✗) => No, he isn't. | No, he's not. | No, he is not.
## transform: Make a question (?).
She's Irish. (?) => Is she Irish?
They're tourists. (?) => Are they tourists?
You're married. (?) => Are you married?
He's a police officer. (?) => Is he a police officer?
Your address is in Mezzeh. (?) => Is your address in Mezzeh?
The waiter is Italian. (?) => Is the waiter Italian?
We're late. (?) => Are we late?
Carlos is a footballer. (?) => Is Carlos a footballer?
## bank: Use the words.
[Where] are you from? — From Istanbul.
[What's] your job? — I'm a doctor.
[How old] is your son? — He's eight.
[Who] is your teacher? — Rana.
[What's] your mobile number? — 0944 123 987.
[Where] is the hotel? — In Bab Sharqi.
[How old] are you? — Twenty-six.
[Who] is that man? — He's my uncle.
## fix: Find and fix the mistake.
[You are>Are you] a student?
Where [you are>are you] from?
Is she married? — Yes, she ['s>is]. #id=a21u1-68ea1ec
[Is>Are] they Brazilian?
What [are>is|'s] your name?
Are you on business? — Yes, I ['m>am].
How old [is>are] your children?
[Are>Is] Hadi from Bab Touma?
## order: Put the words in order.
Are you married?
Where are you from?
What's your job?
Is she a lawyer?
How old are your children?
What's your mobile number?
Are they on holiday?
Is the waiter Italian?
""",
    ),
]

CLASSROOM = dict(
    phrases=["What's the difference between … and …?", "Can you give me an example?", "How do you say … in English?",
             "I don't understand.", "Can you repeat that, please?", "Work in pairs.", "Is this right?"],
    order="""
S: Excuse me, what's the difference between 'single' and 'married'?
T: 'Single' — no husband or wife. 'Married' — a husband or a wife.
S: Can you give me an example?
T: Hadi is single. Rana is married.
S: Thank you. Is this right: 'I'm single'?
T: Yes, it's right!
""",
)

READING = dict(
    title="A language café in Damascus",
    text="""Every Thursday evening, there's a language café at Al-Nofara in the Old City. The people at the café are from different countries, and they're all really friendly.

Sean is Irish. He's thirty-two, and he's a musician. He's in Damascus on business — his band is here for a concert. Lucía is from Buenos Aires, so she's Argentinian, not Spanish! She's a lawyer, and she's on holiday with her husband, Carlos. He's a waiter in a famous restaurant.

Maya is Syrian. She's a student and a barista, and she's single. "This café is fantastic," she says. "My English is really good now — and my Spanish, too!" """,
    qs="""
## tf: True or false?
The language café is on Thursday evenings. | T @ Every Thursday evening, there's a language café #id=a21u1-f4e3dd3
Sean is British. | F @ Sean is Irish
Sean is in Damascus on business. | T @ He's in Damascus on business
Lucía is Spanish. | F @ she's Argentinian, not Spanish
Maya is married. | F @ she's single
## choose: Choose the answer.
What's Lucía's job? | a lawyer | a waiter | a musician @ She's a lawyer
What's Carlos's job? | a waiter | a lawyer | a student @ He's a waiter in a famous restaurant
## gap: Write one word.
Sean is a [musician]. @ he's a musician
""",
)

DIALOGUE = dict(
    title="Nice to meet you",
    intro="A hotel in Bab Sharqi. Ziad meets a guest, Olga.",
    task="gaps",
    lines="""
Ziad: Good evening! Are you [on] holiday?
Olga: No, I'm not. I'm here [on] business.
Ziad: Oh, really? [Where] are you from?
Olga: I'm from Warsaw. I'm [Polish].
Ziad: And what's your [job]?
Olga: I'm [an] engineer. And you?
Ziad: I'm a lawyer. Here's my card with my mobile [number].
Olga: Thank you. Nice to meet you, Ziad.
""",
)

WQ = """
I'm from Aleppo. (where / you) => Where are you from?
No, she isn't. She's single. (married / she) => Is she married?
He's a police officer. (what / his job) => What's his job? | What is his job?
Yes, they are. They're on holiday. (tourists / they) => Are they tourists?
0933 456 789. (what / your mobile number) => What's your mobile number? | What is your mobile number?
We're twenty-five. (how old / you) => How old are you?
No, I'm not. I'm Irish. (British / you) => Are you British?
Rana. (who / your teacher) => Who's your teacher? | Who is your teacher?
"""

WRITING = [
    dict(task="Write a short profile of a classmate or a friend: name, nationality, age, job, married or single, mobile number.",
         tip="Use am / is / are and a / an with jobs. Write 40–70 words.",
         model="This is my friend Sean. He's Irish, from Dublin, and he's thirty-two. He's a musician — he's in a band. He isn't married. He's single. He's in Damascus on business this month. His mobile number is 0944 778 210. He's really friendly, and his Arabic is very good!",
         check=["am / is / are", "isn't / aren't", "a / an + job", "nationality words with a capital letter"],
         min=40, max=70),
]

CANDO = [
    "use am, is and are in positive and negative sentences.",
    "use a and an with jobs.",
    "ask and answer questions with be.",
    "talk about nationalities and jobs.",
    "give my mobile number and address.",
]
