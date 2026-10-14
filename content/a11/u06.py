META = dict(n=6, title="Things you do", pages="42–49")

BOOK = """
watch TV / a film, listen to music / live music, play tennis / computer games, go to the gym / the cinema,
read books / magazines, cook a meal / dinner, use a computer / a laptop, go out with friends / your family,
love, like, don't mind, don't like, hate,
Chinese food, jazz, rock music, dancing, football, running, basketball, dogs, fast food, horses,
to win / winner, (cooking) competition, computer programming, musical instrument, piano, guitar, cricket, hockey,
window, window cleaner, library, animal, pet (dog, cat, fish), popular dish, chicken curry, vegetable curry,
unusual (job, person)
"""

WORDS = """
@Activities
watch TV / a film | to look at programmes on TV, or at a film | Reem watches a film every Friday. | watch;watches
listen to music / live music | to hear songs; live music = a band plays in front of you | Maya listens to live music in a café in Baramkeh. | listen to music;listens to music;listen to live music;listens to live music
play tennis / computer games | to do a sport with a ball and a racket / to play games on a screen | Hadi plays computer games at night. | play tennis;plays tennis;play computer games;plays computer games
go to the gym / the cinema | to go to a place for sport / for films | Kareem goes to the gym near his shop. | go to the gym;goes to the gym;go to the cinema;goes to the cinema
read books / magazines | to look at and understand books or magazines | Reem reads books in the library. | read books;reads books;read magazines;reads magazines
cook a meal / dinner | to make food | Um Khaled cooks dinner for the whole street! | cook a meal;cooks a meal;cook dinner;cooks dinner
use a computer / a laptop | to work or play on a computer | Rana uses a laptop at school. | use a computer;uses a computer;use a laptop;uses a laptop
go out with friends / your family | to leave home for fun with people | Dima goes out with her friends on Thursday. | go out with friends;goes out with friends;go out with her friends;goes out with her friends;go out with your family
@Likes and dislikes
love | to like very, very much | Salma loves Arabic coffee. |  | like-scale
like | to think something is nice | Hadi likes rock music. |  | like-scale
don't mind | it's OK for you; not good, not bad | I don't mind football. |  | like-scale
don't like | to think something isn't nice | I don't like fast food. |  | like-scale
hate | to not like at all | Abu Salim hates traffic! |  | like-scale
Chinese food | food from China | Mei loves Chinese food — it's from her country!
jazz | a type of music with saxophones and piano | Maya likes jazz.
rock music | loud music with electric guitars | Hadi loves rock music.
dancing | moving to music | Lina loves dancing at weddings.
football | a team sport with a ball you kick | Jad plays football with his friends.
running | moving very fast on your feet as a sport | Ghada likes running in Tishreen Park.
basketball | a team sport; you throw the ball into a high net | Samer plays basketball at the weekend.
dogs | animals that are often pets; they say "woof" | Sven loves dogs.
fast food | quick food like burgers and chips | Fadi eats fast food in his car.
horses | big animals; people ride them | Abu Omar likes horses.
@Other words
win / winner | to be first in a competition / the person who is first | Walid wins the knafeh competition every year. He's the winner! | win;wins;winner
competition | an event where people try to be the best | Tareq loves the cooking competition on TV.
computer programming | writing code for computers | Wei studies computer programming.
musical instrument | a piano, a guitar, an oud… | Does Maya play a musical instrument?
piano | a big musical instrument with black and white keys | Reem plays the piano.
guitar | a musical instrument with six strings | Hadi plays the guitar.
cricket | a sport with a bat and a ball, popular in England and India | Raj loves cricket.
hockey | a sport with sticks and a small ball, or on ice | Olga plays ice hockey in winter.
window | glass in a wall; you see out of it | Our kitchen window is big.
window cleaner | a person who cleans windows as a job | Bassel is a window cleaner in Dubai.
library | a place with a lot of books; you borrow them | Reem studies in the library.
animal | a living thing, like a dog, a cat or a horse | Joud loves animals.
pet | an animal in your home: a dog, a cat, a fish | Mais has a pet cat.
popular dish | food a lot of people like | Kibbeh is a popular dish in Syria.
chicken curry | an Indian dish with chicken and spices | Priya cooks chicken curry.
vegetable curry | an Indian dish with vegetables and spices | Raj doesn't eat meat. He likes vegetable curry.
unusual | not normal; different | A window cleaner on tall buildings? That's an unusual job!
"""

ODD = """
jazz, rock music, *football, samba music | Football: a sport.
piano, guitar, *library, oud | Library: not a musical instrument.
running, hockey, cricket, *window | Window: not a sport.
love, like, hate, *pet | Pet: an animal.
dogs, horses, cats, *dancing | Dancing: not an animal.
lives, works, goes, *live | Live: I / you / we / they.
watches, studies, has, *study | Study: no -s.
"""

GRAMMAR = [
    dict(
        id="g1",
        title="Present simple: he / she / it",
        visual=dict(type="compare", cols=[
            dict(title="+ s", color="teal", items=["live → lives", "work → works", "play → plays", "like → likes"]),
            dict(title="+ es", color="purple", items=["go → goes", "watch → watches", "teach → teaches", "do → does"]),
            dict(title="y → ies / have → has", color="amber", items=["study → studies", "fly → flies", "have → {has}"]),
        ], cap="he / she / it: the verb gets an s"),
        pattern=[
            ["+", "He / She / It", ["works", "v"], "in a shop."],
            ["−", "He / She / It", ["doesn't work", "n"], "at the weekend."],
            ["+", "She", ["has", "v"], "a pet cat."],
            ["−", "He", ["doesn't have", "n"], "a car."],
        ],
        examples=[
            "Abu Salim {drives} a service taxi.",
            "Nour {works} in a pharmacy in Sha'lan.",
            "Maya {loves} jazz, but she {doesn't like} rock music.",
            "Kareem {has} a fabric shop. He {doesn't work} on Friday.",
        ],
        ar=[
            "مع he و she و it منزيد s ع الفعل: he works, she lives.",
            "بعض الأفعال بتاخد es: goes, watches. و study بتصير studies، و have بتصير has.",
            "للنفي: doesn't + الفعل بلا s: She doesn't work، مو She doesn't works.",
            "انتبه: أكتر غلطة عنا 'He go' — صحّها: He goes.",
        ],
        watch=[("He go to work by bus.", "He goes to work by bus."), ("She doesn't works.", "She doesn't work."), ("He have a car.", "He has a car."),
               ("She is work in a bank.", "She works in a bank.")],
        quick="""
## choose: Choose the answer.
Hadi ___ computer games. | plays | play | playing
Nour ___ in a pharmacy. | works | work | is work
Salma ___ have a car. | doesn't | don't | isn't
""",
        sets="""
## choose: Choose the answer.
Rana ___ English at a school in Mezzeh. | teaches | teach | is teach
Abu Salim ___ a service taxi. | drives | drive | driving
Maya ___ jazz. | loves | love | is love
Jad ___ to the gym. | goes | go | gos
Tareq ___ a restaurant in Qassaa. | has | have | haves
Reem ___ books in the library. | reads | read | is read
Fadi ___ like cooking. | doesn't | don't | isn't
Wei ___ computer programming. | studies | studys | study
Kareem ___ work on Friday. | doesn't | don't | not
My cat ___ fish. | loves | love | is love
## gap: Write the verb with -s, -es or -ies.
Salma [works] at night. (work)
Hadi [watches] a film every Friday. (watch)
Reem [studies] English. (study)
Abu Omar [goes] to work early. (go)
Ghada [has] two children. (have)
Maya [listens] to music on the bus. (listen)
Um Khaled [cooks] dinner for the family. (cook)
Hala [does] her shopping at the souq. (do)
## transform: Make the sentence negative (−).
Hadi likes football. (−) => Hadi doesn't like football. | Hadi does not like football.
Nour works on Friday. (−) => Nour doesn't work on Friday. | Nour does not work on Friday.
Abu Salim has a laptop. (−) => Abu Salim doesn't have a laptop. | Abu Salim does not have a laptop.
Maya plays the piano. (−) => Maya doesn't play the piano. | Maya does not play the piano.
Kareem goes to the cinema. (−) => Kareem doesn't go to the cinema. | Kareem does not go to the cinema.
Reem watches TV. (−) => Reem doesn't watch TV. | Reem does not watch TV.
My dog likes cats. (−) => My dog doesn't like cats. | My dog does not like cats.
Tareq cooks fast food. (−) => Tareq doesn't cook fast food. | Tareq does not cook fast food.
## bank: Use the words.
Salma is a nurse. She [works] at night.
Jad [plays] football with his friends.
Mei [loves] Chinese food.
Raj [doesn't] eat meat.
Kareem [has] a fabric shop.
Reem [reads] books in the library.
Abu Salim [hates] traffic!
Wei [studies] computer programming.
## fix: Find and fix the mistake.
Hadi [like>likes] rock music.
Nour [don't>doesn't] work at the weekend.
Maya [doesn't plays>doesn't play] the guitar.
Abu Omar [have>has] a shop in Kafr Sousa.
Rana [teachs>teaches] English.
Reem [studys>studies] at the library.
Kareem [is work>works] in Souq al-Hamidiyah.
Jad [go>goes] to the gym.
## sort: Sort the verbs. | + s | + es | y → ies
+ s: works, plays, likes, reads
+ es: goes, watches, teaches, does
y → ies: studies, flies, tries
## order: Put the words in order.
She works in a pharmacy.
He doesn't like fast food.
Maya listens to live music.
Abu Salim drives a taxi.
Reem doesn't watch TV.
He has a pet dog.
My sister loves dancing.
Tareq cooks a fantastic kibbeh.
""",
    ),
    dict(
        id="g2",
        title="Questions: Does he / she…?",
        visual=dict(type="table", head=["question", "yes", "no"],
                    rows=[["Does she like jazz?", "Yes, she does.", "No, she doesn't."], ["Does he play football?", "Yes, he does.", "No, he doesn't."],
                          ["Does it have Wi-Fi?", "Yes, it does.", "No, it doesn't."]],
                    colors=["purple", "teal", "coral"], cap="Does + he / she / it + verb (no s!)?"),
        pattern=[
            ["?", ["Does", "v"], ["she", "s"], "like jazz?"],
            ["", "Yes, she", ["does.", "v"], ""],
            ["", "No, she", ["doesn't.", "n"], ""],
            ["?", ["Does", "v"], ["Hadi", "s"], "play the guitar? (play, not plays)"],
        ],
        examples=[
            "{Does} Maya {play} a musical instrument? — Yes, {she does}. The guitar.",
            "{Does} Abu Salim {like} his job? — Yes, {he does}.",
            "{Does} your hotel {have} a gym? — No, {it doesn't}.",
            "{Does} Raj {eat} meat? — No, {he doesn't}.",
        ],
        ar=[
            "لنسأل عن he و she و it منحط Does بالأول، والفعل بيرجع بلا s: Does she like…?",
            "الجواب القصير: Yes, she does. / No, he doesn't.",
            "انتبه: Does she likes? غلط — الـ s بتروح لـ does.",
        ],
        watch=[("Does she likes jazz?", "Does she like jazz?"), ("Do he play football?", "Does he play football?"), ("Is she like dancing?", "Does she like dancing?")],
        quick="""
## choose: Choose the answer.
___ Hadi like rock music? | Does | Do | Is
Does Maya play the piano? — No, she ___. | doesn't | don't | isn't
Does Reem ___ books? | read | reads | reading
""",
        sets="""
## choose: Choose the answer.
___ Salma work at night? | Does | Do | Is
Does Jad ___ football? | play | plays | playing
Does Mei like Chinese food? — Yes, she ___. | does | do | likes
___ your parents live in Aleppo? | Do | Does | Are
Does Kareem have a car? — No, he ___. | doesn't | don't | hasn't
___ the hotel have a gym? | Does | Do | Is
Does Abu Omar ___ horses? | like | likes | liking
Does Wei study programming? — Yes, he ___. | does | studies | is
___ you like dancing? | Do | Does | Are
Does your cat like fish? — Yes, it ___. | does | do | is
## short: Answer the question.
Does Maya like jazz? (✓) => Yes, she does.
Does Abu Salim like traffic? (✗) => No, he doesn't. | No, he does not.
Does Reem read books? (✓) => Yes, she does.
Does Raj eat meat? (✗) => No, he doesn't. | No, he does not.
Does the library have computers? (✓) => Yes, it does.
Does Fadi cook? (✗) => No, he doesn't. | No, he does not.
Does Ghada go running? (✓) => Yes, she does.
Does Kareem work on Friday? (✗) => No, he doesn't. | No, he does not.
## transform: Make a question (?).
She plays the guitar. (?) => Does she play the guitar?
He likes rock music. (?) => Does he like rock music?
Nour works in Sha'lan. (?) => Does Nour work in Sha'lan?
It has a big window. (?) => Does it have a big window?
Hadi goes to the gym. (?) => Does Hadi go to the gym?
Maya watches films. (?) => Does Maya watch films?
He studies computer programming. (?) => Does he study computer programming?
She cooks dinner. (?) => Does she cook dinner?
## fix: Find and fix the mistake.
Does she [likes>like] jazz?
[Do>Does] Hadi play the guitar?
[Is>Does] Rana teach English?
Does Jad play football? — Yes, he [plays>does].
Does he have a pet? — No, he [don't>doesn't].
[Does>Do] they live in Homs?
Does Reem [reads>read] magazines?
[She likes>Does she like] dogs?
## order: Put the words in order.
Does she like jazz?
Does Hadi play the guitar?
Does your brother work in an office?
Does it have a garden?
Does Maya listen to live music?
Does he watch TV?
Does your mother cook dinner?
Does Abu Omar like horses?
## match: Match the question and the answer.
Does Salma work at night? = Yes, she does. She's a nurse.
Does Raj eat meat? = No, he doesn't. He loves vegetable curry.
Does Maya play the guitar? = Yes, she does. She loves music. #id=a11u6-86c5c4b
Does Abu Salim like traffic? = No, he doesn't! He hates it.
Does the café have Wi-Fi? = Yes, it does. The password is 1234.
Does Fadi cook? = No, he doesn't. He eats fast food.
Does Reem go to the library? = Yes, she does. She loves books.
Does Kareem work on Friday? = No, he doesn't. His shop is closed.
""",
    ),
]

CLASSROOM = dict(
    phrases=["How do you spell …?", "Which page?", "Sorry, I don't have my book.", "Check with your partner.", "Hands up.",
             "It's my turn.", "Listen.", "Thank you."],
    order="""
T: Listen, please. Check with your partner.
S: Sorry, I don't have my book.
T: That's OK. Look with Hiba.
S: Thank you. Which page?
T: Page 44.
S: How do you spell 'guitar'?
""",
)

READING = dict(
    title="An unusual job",
    text="""Bassel is from Homs, but he lives in Dubai. He's a window cleaner, and he has a very unusual job. He cleans the windows of very tall buildings! He starts work at six in the morning and finishes at two in the afternoon. He doesn't work on Friday.

Bassel loves his job. He likes the view from the top of the buildings, and he doesn't mind the hot weather. His wife, Aya, is a chef. She works in a restaurant, and chicken curry is a popular dish in her restaurant. Bassel doesn't like curry. He loves Aya's kibbeh!""",
    qs="""
## tf: True or false?
Bassel lives in Homs. | F @ he lives in Dubai
He cleans the windows of tall buildings. | T @ He cleans the windows of very tall buildings
He works on Friday. | F @ He doesn't work on Friday
He doesn't mind the hot weather. | T @ he doesn't mind the hot weather
Bassel likes chicken curry. | F @ Bassel doesn't like curry
## choose: Choose the answer.
What's Aya's job? | a chef | a window cleaner | a teacher @ His wife, Aya, is a chef
Bassel: "I start work ___." | at six in the morning | at two in the afternoon | at nine at night @ He starts work at six in the morning
## gap: Write one word.
Bassel loves Aya's [kibbeh]. @ He loves Aya's kibbeh
""",
)

DIALOGUE = dict(
    title="A present for Maya",
    intro="Hala and Hadi are in a shop. Maya's birthday is on Thursday.",
    task="gaps",
    lines="""
Hala: Does Maya [like] music?
Hadi: Yes, she [does]. She loves jazz.
Hala: Does she play a musical [instrument]?
Hadi: Yes, she plays the guitar. She doesn't [play] the piano.
Hala: What about books? Does she [read] a lot?
Hadi: No, she [doesn't]. She watches films.
Hala: OK. A jazz CD, then!
Hadi: Great idea. She [loves] jazz!
""",
)

WQ = """
Yes, she does. She loves jazz. (Maya / like jazz) => Does Maya like jazz?
No, he doesn't. He hates it. (Abu Salim / like traffic) => Does Abu Salim like traffic?
Yes, it does. It has free Wi-Fi. (the café / have Wi-Fi) => Does the café have Wi-Fi?
No, she doesn't. She works in the day. (Nour / work at night) => Does Nour work at night?
Yes, he does. He's very good! (Hadi / play the guitar) => Does Hadi play the guitar?
She's a chef. (what / Aya's job) => What's Aya's job? | What is Aya's job?
No, they don't. They live in Dubai. (Bassel and Aya / live in Homs) => Do Bassel and Aya live in Homs?
Yes, I do. I love it! (you / like dancing) => Do you like dancing?
"""

WRITING = [
    dict(task="Write about a person in your family or a friend: job, free time, likes and dislikes.",
         tip="Use he / she + verb-s, doesn't, loves / likes / hates. Write 40–70 words.",
         model="My brother Firas is twenty-six. He's an engineer, and he works for a big company in Mezzeh. He goes to the gym after work. He loves football and he plays with his friends at the weekend. He doesn't like fast food, and he hates traffic! He has a cat. Her name is Lulu.",
         check=["he / she + verb-s: works, goes, plays", "doesn't + verb (no s)", "love / like / don't mind / hate", "has, not haves"],
         min=40, max=70),
    dict(task="Write five questions for your teacher with Does… or Do you…? Example: Do you like football?",
         tip="Write 5 questions.",
         model="Do you like football?\nDo you have a pet?\nDoes your family live in Damascus?\nDo you play a musical instrument?\nDoes your best friend speak English?",
         check=["Do you + verb?", "Does + he / she / it + verb (no s)?", "A question mark (?) at the end"],
         min=20, max=60),
]

CANDO = [
    "use he / she + verb-s: She works, he goes.",
    "use doesn't: He doesn't like fast food.",
    "ask 'Does she…?' and answer 'Yes, she does.'",
    "say what I like and don't like.",
    "talk about free-time activities.",
]
