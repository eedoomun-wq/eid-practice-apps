META = dict(n=2, title="Around the world", pages="14–19")

# Book words. "Numbers 21–100 and How old…?" is listed as the tens plus twenty-one.
BOOK = """
Australia – Australian, Brazil – Brazilian, China – Chinese, Egypt – Egyptian, England – English, Italy – Italian,
Japan – Japanese, Poland – Polish, Russia – Russian, Vietnam – Vietnamese, the USA – American, Portugal – Portuguese,
Argentina – Argentinian, Spain – Spanish,
twenty-one, thirty, forty, fifty, sixty, seventy, eighty, ninety, a hundred, How old…?,
pizza, tortilla, samba music, a (clothes/car) company, a place, a person, people, a river, winner, best friend, age,
How old are you?, I'm fifty, I think…, I don't know
"""

WORDS = """
@Countries and nationalities
Australia – Australian | a very big country; Sydney is there | Sydney is in Australia. Is Hannah Australian? | &Australia;Australian
Brazil – Brazilian | a big country in South America; samba is from there | Rio is in Brazil. Carlos is Brazilian. | &Brazil;Brazilian
China – Chinese | a very big country in Asia; Beijing is the capital | Wei is from China. He's Chinese. | &China;Chinese
Egypt – Egyptian | a country in North Africa; the Nile is there | Cairo is in Egypt. Koshary is Egyptian food. | &Egypt;Egyptian
England – English | a country in the UK; London is there | London is in England. Hannah is English. | &England;English
Italy – Italian | a country in Europe; Rome is the capital | Rome is in Italy. Pizza is Italian. | &Italy;Italian
Japan – Japanese | a country in Asia; Tokyo is the capital | Kenji is from Japan. He's Japanese. | &Japan;Japanese
Poland – Polish | a country in Europe; Warsaw is the capital | Olga is from Poland. Is she Polish? Yes, she is. | &Poland;Polish
Russia – Russian | a very, very big country; Moscow is the capital | Moscow is in Russia. Olga isn't Russian. | &Russia;Russian
Vietnam – Vietnamese | a country in Asia; Hanoi is the capital | Hanoi is in Vietnam. Mei isn't Vietnamese. | &Vietnam;Vietnamese
the USA – American | a big country; New York is there | New York is in the USA. Is Hannah American? No, she's English. | &USA;American
Portugal – Portuguese | a country in Europe, next to Spain | Lisbon is in Portugal. Is Sofia Portuguese? | &Portugal;Portuguese
Argentina – Argentinian | a country in South America; Buenos Aires is the capital | Lucía is from Argentina. She's Argentinian. | &Argentina;Argentinian
Spain – Spanish | a country in Europe; Madrid is the capital | Barcelona is in Spain. Tortilla is Spanish food. | &Spain;Spanish
+Syria – Syrian | our country! Damascus is the capital | Damascus is in Syria. Layla is Syrian. | &Syria;Syrian
+Lebanon – Lebanese | a small country next to Syria; Beirut is the capital | Beirut is in Lebanon. Is Rami Lebanese? | &Lebanon;Lebanese
+Turkey – Turkish | a country north of Syria; Istanbul is there | Istanbul is in Turkey. Elif is Turkish. | &Turkey;Turkish
@Numbers 21–100
twenty-one | 21 | Layla is twenty-one.
thirty | 30 | Rana is thirty-four.
forty | 40 | Kareem is forty.
fifty | 50 | How old is Um Khaled? — She's fifty-five.
sixty | 60 | Abu Firas is sixty-two.
seventy | 70 | My grandfather is seventy.
eighty | 80 | My grandmother is eighty-one!
ninety | 90 | Is he ninety? — Yes, he is!
a hundred | 100 | A hundred out of a hundred — fantastic!
How old…? | a question about age | How old is Hadi? — He's twenty-four. |  | age
@Other words
pizza | Italian food: bread, cheese and tomato | Pizza is my favourite food. |  | food
tortilla | Spanish food: eggs and potatoes, or flat Mexican bread | Tortilla is Spanish food. |  | food
samba music | music and dance from Brazil | Samba music is Brazilian.
company | a business: people work there and sell things | Zara is a Spanish clothes company. Fiat is an Italian car company.
place | a town, a city, a country, a building… | Bab Touma is a nice place.
person | one man, woman or child | Ghada is a kind person. |  | pp
people | more than one person | People in Damascus? Very friendly! |  | pp
river | water that goes across the land to the sea | The Barada is a river in Damascus.
winner | the person or team that is first in a competition | Brazil is the winner!
best friend | your number one friend | Maya is my best friend.
age | how old you are | Name: Reem. Age: 17. |  | age
How old are you? | a question to ask a person's age | How old are you? — I'm nineteen. |  | age
I'm fifty | a way to say your age | How old are you, Tareq? — I'm forty-five. | I'm | age
I think… | you are not sure, but… | Is Sofia Spanish? — I think she's Portuguese.
I don't know | you have no answer | Is he Russian? — I don't know.
"""

WORDSETS = """
## numbers: Write the number in words.
21 => twenty-one | twenty one
35 => thirty-five | thirty five
48 => forty-eight | forty eight
50 => fifty
62 => sixty-two | sixty two
77 => seventy-seven | seventy seven
83 => eighty-three | eighty three
99 => ninety-nine | ninety nine
100 => a hundred | one hundred
14 => fourteen
## numbers: Write the number.
forty-four => 44
thirteen => 13
thirty => 30
sixty-six => 66
eighteen => 18
eighty => 80
ninety-one => 91
seventy-two => 72
## match: Match the country and the nationality.
Brazil = Brazilian
China = Chinese
Egypt = Egyptian
Poland = Polish
Russia = Russian
Portugal = Portuguese
Argentina = Argentinian
Syria = Syrian
"""

ODD = """
Italian, Spanish, Polish, *Italy | Italy: a country. The others: nationalities.
Brazil, Japan, Egypt, *Chinese | Chinese: a nationality.
pizza, tortilla, *river, koshary | River: not food.
thirty, forty, sixty, *thirteen | Thirteen: not 30, 40, 60…
he, she, *his, it | His: his car, his name.
her, his, their, *she | She: she's, she is.
age, How old…?, *winner, I'm fifty | Winner: not about age.
"""

GRAMMAR = [
    dict(
        id="g1",
        title="be: he / she / it",
        visual=dict(type="table", head=["", "be", "short", "negative"],
                    rows=[["I", "am", "I'm", "I'm not"], ["you", "are", "you're", "you aren't"],
                          ["he", "is", "he's", "he isn't"], ["she", "is", "she's", "she isn't"], ["it", "is", "it's", "it isn't"]],
                    colors=["teal", "purple", "purple", "coral"],
                    cap="he, she, it + is"),
        pattern=[
            ["+", "She", "'s", "Brazilian."],
            ["−", "He", "isn't", "from Rome."],
            ["?", ["Is", "v"], ["she", "s"], "a student?"],
            ["", "Yes, she", "is.", ""],
            ["", "No, he", "isn't.", ""],
        ],
        examples=[
            "Kenji {is} from Japan. {He's} Japanese.",
            "{Is} Layla a student? — Yes, {she is}.",
            "Abu Salim {isn't} a teacher. {He's} a driver.",
            "How old {is} Reem? — {She's} seventeen.",
        ],
        ar=[
            "مع he و she و it منستعمل is: He is، She is، It is.",
            "بالعربي منقول 'هي أستاذة' بلا فعل، بس بالإنكليزي لازم: She's a teacher.",
            "للنفي منحط not: He isn't Italian. وللسؤال منقدّم is: Is she Syrian?",
            "والعمر بالإنكليزي مع be: I'm 20، مو I have 20 years.",
        ],
        watch=[("She teacher.", "She's a teacher."), ("I have 20 years.", "I'm 20."), ("He are Egyptian.", "He's Egyptian."), ("Is Italian he?", "Is he Italian?")],
        quick="""
## choose: Choose the answer.
Kenji ___ Japanese. | is | are | am
___ she from Spain? | Is | Are | Am
Hadi ___ thirty. He's twenty-four. | isn't | aren't | not
""",
        sets="""
## choose: Choose the answer.
Olga ___ from Poland. | is | are | am
He ___ an engineer. | 's | 're | 'm
___ Carlos Brazilian? | Is | Are | Am
Sofia ___ Spanish. She's Portuguese. | isn't | aren't | not
Is Hannah English? — Yes, she ___. | is | 's | are
Is Wei from Japan? — No, he ___. | isn't | not | aren't
How old ___ Abu Firas? | is | are | am
Layla ___ twenty-one. | is | have | are
It ___ a car company. | 's | 're | 'm
Is Rome in Italy? — Yes, it ___. | is | 's | isn't
## gap: Write is, 's or isn't.
Mehmet [is|'s] Turkish.
Priya [isn't|is not] Chinese. She's from India.
[Is] Dima a hairdresser? — Yes, she is.
Cairo [is|'s] in Egypt.
Kareem [isn't|is not] a teacher. He's a businessman.
How old [is] Jad?
[Is] pizza Italian? — Yes, it is.
Lucía [is|'s] from Argentina.
Tokyo [isn't|is not] in China. It's in Japan.
Walid [is|'s] fifty-two.
## short: Answer the question.
Is Nour a pharmacist? (✓) => Yes, she is.
Is Kenji Chinese? (✗) => No, he isn't. | No, he's not. | No, he is not.
Is Bab Touma in Damascus? (✓) => Yes, it is.
Is Marco Italian? (✓) => Yes, he is.
Is Olga Russian? (✗) => No, she isn't. | No, she's not. | No, she is not.
Is the Nile in Egypt? (✓) => Yes, it is.
Is Hadi fifty? (✗) => No, he isn't. | No, he's not. | No, he is not.
Is Salma a nurse? (✓) => Yes, she is.
## transform: Make a question (?).
She's from Brazil. (?) => Is she from Brazil?
He's an architect. (?) => Is he an architect?
It's a Spanish company. (?) => Is it a Spanish company?
Ghada is a doctor. (?) => Is Ghada a doctor?
He's thirty-three. (?) => Is he thirty-three?
Mei is Chinese. (?) => Is Mei Chinese?
She's a student. (?) => Is she a student?
Abu Omar is from Kafr Sousa. (?) => Is Abu Omar from Kafr Sousa?
## transform: Make the sentence negative (−).
He's Polish. (−) => He isn't Polish. | He's not Polish. | He is not Polish.
She's an actor. (−) => She isn't an actor. | She's not an actor. | She is not an actor.
It's Japanese food. (−) => It isn't Japanese food. | It's not Japanese food. | It is not Japanese food.
Raj is from England. (−) => Raj isn't from England. | Raj is not from England.
Maya is twenty. (−) => Maya isn't twenty. | Maya is not twenty.
He's a winner. (−) => He isn't a winner. | He's not a winner. | He is not a winner.
She's Vietnamese. (−) => She isn't Vietnamese. | She's not Vietnamese. | She is not Vietnamese.
Kasab is a big city. (−) => Kasab isn't a big city. | Kasab is not a big city.
## fix: Find and fix the mistake.
She [teacher>'s a teacher|is a teacher].
He [are>is|'s] from Egypt.
I [have 20 years>'m 20|am 20|'m twenty|am twenty].
[Are>Is] Yuki Japanese?
Tala [not>isn't|is not] Lebanese.
How old [are>is] Reem?
Is Pierre French? — Yes, he [are>is].
[He>He's|He is] an engineer.
## order: Put the words in order.
Is she from Turkey?
He's an accountant.
How old is Kareem?
She isn't Russian.
Is it an Italian company?
Elif is from Istanbul.
He's not a student. || He isn't a student.
How old is she?
""",
    ),
    dict(
        id="g2",
        title="his / her / their / our",
        visual=dict(type="table", head=["who?", "+ noun"],
                    rows=[["I", "{my} car"], ["you", "{your} car"], ["Hadi (a man)", "{his} car"],
                          ["Layla (a woman)", "{her} car"], ["Layla + Hadi", "{their} car"], ["me + my family", "{our} car"]],
                    colors=["teal", "amber"], cap="his = for a man · her = for a woman"),
        pattern=[
            ["", "Hadi:", ["his", "v"], "phone"],
            ["", "Layla:", ["her", "v"], "name"],
            ["", "Rana + Kareem:", ["their", "v"], "best friend"],
            ["", "me + my family:", ["our", "v"], "flat"],
        ],
        examples=[
            "Tareq is from Qassaa. {His} restaurant is famous.",
            "Dima is a hairdresser. {Her} shop is in Rukn al-Din.",
            "Mei and Kenji: {their} flat is in Tokyo.",
            "{Our} teacher is Rana. She's from Mezzeh.",
        ],
        ar=[
            "بالعربي منقول 'سيارته' و'سيارتها'، بس بالإنكليزي منحط كلمة قبل الاسم: his car، her car.",
            "his للرجّال و her للمرا، حتى لو الشي نفسه مذكّر أو مؤنث بالعربي.",
            "their يعني تبعهن، و our يعني تبعنا: our teacher = أستاذنا.",
        ],
        watch=[("Layla is a student. His university is in Damascus.", "Layla is a student. Her university is in Damascus."),
               ("Kareem: her shop", "Kareem: his shop"), ("car his", "his car")],
        quick="""
## choose: Choose the answer.
Hadi is an engineer. ___ shop is in Bab Touma. | His | Her | Their
Maya is a student. ___ favourite music is jazz. | Her | His | Our
Rana and Kareem: ___ best friend is Nour. | their | his | our
""",
        sets="""
## choose: Choose the answer.
Kenji is Japanese. ___ wife is Chinese. | His | Her | Their
Salma is a nurse. ___ hospital is in Malki. | Her | His | Our
Abu Salim is a driver. ___ taxi is yellow. | His | Her | Their
Hala is from Sha'lan. ___ café is small. | Her | His | Their
Lina and Ziad: ___ son is Karam. | their | his | her
Me and my family: ___ house is in Midan. | our | their | her
Marco is Italian. ___ surname is Rossi. | His | Her | Our
Sofia is a teacher. ___ school is in Lisbon. | Her | His | Their
Walid is fifty-two. ___ knafeh is fantastic! | His | Her | Our
Yuki is a student. ___ phone number is 0933 222 100. | Her | His | Their
## gap: Write his, her, their or our.
Nour is a pharmacist. [Her] pharmacy is in Sha'lan.
Jad is a delivery driver. [His] motorbike is red.
Mehmet and Elif: [their] restaurant is in Istanbul.
Me and my brother: [our] surname is Haddad.
Ghada is a doctor. [Her] first name is short.
Samer is an electrician. [His] phone number is 0944 555 000.
Lucía and Carlos: [their] city is Buenos Aires.
Me and my friends: [our] teacher is Rana.
## bank: Use the words.
Salma is a nurse. [Her] job is hard.
Abu Firas is sixty-two. [His] age? Sixty-two!
Me and Jad: [our] English teacher is Rana.
Joud and Sana: [their] mother is a cook.
Kareem is a businessman. [His] shop is in Souq al-Hamidiyah.
Hello, I'm Hiba. [My] surname is Nasser.
What's [your] name?
Tala is Lebanese. [Her] city is Beirut.
## sort: his or her? | his | her
his: Kareem, Abu Salim, Tareq, Kenji, Carlos, Hadi
her: Layla, Um Khaled, Rana, Olga, Mei, Salma
## fix: Find and fix the mistake.
Maya is a barista. [His>Her] café is in Baramkeh.
Abu Omar is a greengrocer. [Her>His] shop is in Kafr Sousa.
Kenji and Mei: [her>their] flat is in Tokyo.
Me and my family: [their>our] house is in Midan.
Reem is seventeen. [His>Her] school is in Dummar.
Fadi is a taxi-app driver. [Her>His] car is white.
Lucía is Argentinian. [His>Her] surname is Gómez.
Reem and Tala: [her>their] school is in Dummar.
## choose: Who is it?
"Her name is Mei." — Mei: a man or a woman? | a woman | a man
"His job? He's a driver." — Abu Salim: a man or a woman? | a man | a woman
"Their best friend is Nour." — one person or two? | two | one
"Our teacher is great." — me alone, or me and my friends? | me and my friends | me alone
"Her shop is in Rukn al-Din." — Dima: a man or a woman? | a woman | a man
"His restaurant is in Qassaa." — Tareq: a man or a woman? | a man | a woman
"Their company is Italian." — one person or two? | two | one
"Our flat is small." — me alone, or me and my family? | me and my family | me alone
## order: Put the words in order.
Her name is Elif.
His car is Japanese.
Their teacher is Rana.
Our flat is in Midan.
Is her name Olga?
His shop is in Bab Touma.
Her best friend is Maya.
Their son is twenty.
""",
    ),
]

CLASSROOM = dict(
    phrases=["I don't know.", "Can you repeat that, please?", "Slowly, please.", "What does … mean?", "Which page?",
             "Look at the board.", "Turn to page …", "Read.", "Write."],
    order="""
T: Turn to page 15, please.
S: Sorry, which page?
T: Page fifteen. Look at the board.
S: What does 'Polish' mean?
T: From Poland.
S: Thank you.
""",
)

READING = dict(
    title="Friends around the world",
    text="""Kenji Sato is from Tokyo in Japan. He's Japanese. He's thirty-five, and he's an engineer. His wife is Mei. She isn't Japanese. She's Chinese, from Beijing. She's a teacher, and her school is in Tokyo.

Their best friend is Elif. She's from Istanbul, so she's Turkish. Is she a student? No, she isn't. She's an actor, and she's twenty-eight.""",
    qs="""
## tf: True or false?
Kenji is Japanese. | T @ He's Japanese
Mei is from Tokyo. | F @ She's Chinese, from Beijing
Mei is a teacher. | T @ She's a teacher
Elif is a student. | F @ No, she isn't
Elif is twenty-eight. | T @ she's twenty-eight
## choose: Choose the answer.
How old is Kenji? | thirty-five | twenty-eight | fifty-three @ He's thirty-five
Elif is ___. | Turkish | Chinese | Japanese @ she's Turkish
## gap: Write one word.
Kenji is an [engineer]. @ he's an engineer
""",
)

DIALOGUE = dict(
    title="At a restaurant in Qassaa",
    intro="A restaurant in Qassaa. Nour, Tareq and his friend Pierre.",
    task="gaps",
    lines="""
Nour: Hi, Tareq! How [are] you?
Tareq: Fine, thanks. Nour, meet Pierre. [He's] from Paris.
Nour: Nice to meet you, Pierre. Are you [French]?
Pierre: Yes, I am. And you? Where are you [from]?
Nour: I'm from Damascus. I'm a pharmacist.
Tareq: Pierre is a chef. [His] restaurant is in Paris.
Nour: Fantastic! How [old] is the restaurant?
Pierre: Oh, it's very old — [eighty] years!
""",
)

WQ = """
She's from Brazil. (where) => Where's she from? | Where is she from?
He's twenty-four. (how old) => How old is he?
Yes, she is. She's a nurse. (a nurse?) => Is she a nurse?
Her name's Lucía. (what) => What's her name? | What is her name?
No, he isn't. He's Spanish. (Italian?) => Is he Italian?
His surname is Rossi. (his surname) => What's his surname? | What is his surname?
I'm nineteen. (how old / you) => How old are you?
Yes, it is. It's in Egypt. (Cairo / in Egypt?) => Is Cairo in Egypt?
"""

WRITING = [
    dict(task="Write about a friend: name, age, nationality, job, town.",
         tip="Use He's / She's and his / her. Write 25–45 words.",
         model="My best friend is Maya. She's nineteen, and she's Syrian. She's a student and a barista. Her café is in Baramkeh. Her favourite music is jazz. She's a great person!",
         check=["He's / She's + age", "nationality: Syrian, Turkish, Italian…", "his or her + noun", "Capital letters for names and countries"],
         min=25, max=45),
    dict(task="Write about two famous people from two countries. Write their names, nationalities and jobs.",
         tip="Use is / isn't. Write 25–50 words.",
         model="Messi is Argentinian. He's a footballer. His city is Rosario. Adele is English. She's a singer. She isn't American. Her city is London.",
         check=["is / isn't", "Nationality words with a capital letter", "his / her", "a / an with jobs"],
         min=25, max=50),
]

CANDO = [
    "say countries and nationalities.",
    "use is and isn't with he, she and it.",
    "ask 'How old is he?' and say ages.",
    "use his, her, their and our.",
    "say the numbers 21 to 100.",
]
