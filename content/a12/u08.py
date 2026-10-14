META = dict(n=8, title="You can do it!", pages="58–65")

BOOK = """
walk, run, drive a car, ride a bike, swim, dance, sing, play chess, take photographs, paint a picture, remember, forget,
head, nose, ear(s), mouth, eye(s), hair, hand(s), arm(s), finger(s), thumb(s), leg(s), foot (feet), toe(s),
(sing/cook) well, (run/drive) fast, fit, sporty, skills, abilities, baby/babies, personal trainer, nanny, dance teacher,
team games, blow your nose, shake hands, touch your toes, up/down the stairs, be interested in, be good at, be good with
"""

WORDS = """
@Things you do
walk | to move on your feet, not fast | I walk to work. It's ten minutes. | | move
run | to move very fast on your feet | Ghada can run five kilometres. | | move
drive a car | to control a car on the road | Abu Salim can drive a car very well.
ride a bike | to sit on a bike and move it with your feet | Can you ride a bike?
swim | to move in water | Can you swim? — Yes, I can. I swim in the sea in Latakia.
dance | to move to music | Lina can dance the dabke.
sing | to make music with your voice | Maya sings in a café on Thursday.
play chess | a game for two people with a black and white board | Abu Firas plays chess with his friends.
take photographs | to use a camera | Kenji takes photographs of old buildings. | take photographs;takes photographs
paint a picture | to make art with colours | Reem can paint a picture of the Umayyad Mosque.
remember | to keep in your head; not to forget | I can't remember his name! | | mind
forget | not to remember | I always forget my keys! | | mind
@The body
head | the top part of your body, with your face | My head hurts.
nose | the part of your face you smell with | Blow your nose, please!
ear | you hear with them; you have two | I can't hear — my ears are cold!
mouth | you eat and speak with it | Open your mouth, please.
eye | you see with them; you have two | Maya has big brown eyes.
hair | it grows on your head | Dima can cut hair very well.
hand | it's at the end of your arm, with five fingers | Shake hands, please!
arm | between your shoulder and your hand | Kareem can carry heavy boxes in his arms.
finger | one of five on your hand | Reem can play the piano with ten fingers.
thumb | the short, thick finger | Thumbs up! Well done!
leg | you walk on them; you have two | My legs are tired after the gym.
foot (feet) | at the end of your leg; you stand on them | My feet hurt in these shoes. | foot;feet
toe | one of five on your foot | Can you touch your toes?
@Abilities
well | in a good way | Um Khaled cooks very well.
fast | quickly; not slow | Jad can drive fast — but he doesn't!
fit | strong and healthy | Mazen is very fit. He's a personal trainer.
sporty | you like sport and you're good at it | My sister is very sporty.
skills | things you can do well | Computer skills are important for jobs.
abilities | things you can do | A nanny needs a lot of abilities.
baby/babies | a very young child / very young children | The baby can't walk. Babies can't talk. | baby;babies
personal trainer | a person who helps you get fit at the gym | My personal trainer is very strict!
nanny | a person who looks after children in their home | The nanny takes the children to the park.
dance teacher | a person who teaches dancing | Lina is a dance teacher in Malki.
team games | games like football and basketball | Do you like team games?
blow your nose | to clean your nose with a tissue | Can you blow your nose? Here's a tissue.
shake hands | to hold hands when you meet | We shake hands when we meet.
touch your toes | to put your hands on your feet, legs straight | Touch your toes — one, two, three!
up/down the stairs | from low to high / from high to low on stairs | My grandfather can't walk up the stairs. | up the stairs;down the stairs
be interested in | to like and want to know about | Reem is interested in history.
be good at | to do something well | Hadi is good at computer games.
be good with | to work well with people or things | Hiba is good with children.
"""

ODD = """
nose, mouth, eye, *toe | Toe: on your foot, not your face.
finger, thumb, hand, *leg | Leg: not part of your hand.
swim, run, walk, *chess | Chess: a game, not a way to move.
can, can't, *does, cannot | Does: not can.
fit, sporty, fast, *nanny | Nanny: a job.
sing, dance, paint, *head | Head: a part of the body.
personal trainer, nanny, dance teacher, *team games | Team games: not a job.
"""

GRAMMAR = [
    dict(
        id="g1",
        title="can / can't",
        visual=dict(type="faces", items=[["can swim ✓", "happy"], ["can't drive ✗", "sad"], ["can cook ✓", "happy"]],
                    cap="can = I'm able to · can't = I'm not able to"),
        pattern=[
            ["+", "I / you / he / she / we / they", ["can", "v"], "swim."],
            ["−", "I / you / he / she / we / they", ["can't", "n"], "drive."],
            ["", "(can't = cannot)", "", ""],
        ],
        examples=[
            "Abu Salim {can} drive very well.",
            "Joud is five. She {can't} read.",
            "Maya {can} sing and play the guitar.",
            "My grandmother {can't} walk up the stairs.",
        ],
        ar=[
            "can يعني بقدر / بعرف، و can't يعني ما بقدر.",
            "can ما بتتغيّر: I can, she can — بلا s أبداً.",
            "بعد can الفعل بيجي لحالو بلا to: I can swim، مو I can to swim.",
        ],
        watch=[("She cans swim.", "She can swim."), ("I can to drive.", "I can drive."), ("He can swims.", "He can swim."),
               ("I don't can dance.", "I can't dance.")],
        quick="""
## choose: Choose the answer.
Jad ___ drive fast. | can | cans | can to
Babies ___ walk. | can't | don't can | not can
Maya can ___ the guitar. | play | plays | to play
""",
        sets="""
## choose: Choose the answer.
Abu Salim ___ drive very well. | can | cans | is can
Joud is five. She ___ read yet. | can't | doesn't can | isn't can
I can ___ in the sea. | swim | swims | to swim
My grandfather ___ walk up the stairs. | can't | not can | don't can
Lina can ___ the dabke. | dance | dances | dancing
Can you ___ a bike? | ride | rides | to ride
Hiba ___ cook very well. | can | cans | can to
Penguins ___ fly. | can't | can | cans
Reem can ___ beautiful pictures. | paint | paints | to paint
I'm sorry, I ___ remember your name. | can't | don't | am not
## gap: Write can or can't.
Fish [can] swim.
Fish [can't|cannot|can not] walk.
Babies [can't|cannot|can not] drive a car.
A personal trainer [can] run fast.
Cats [can] see at night.
A baby [can't|cannot|can not] read.
Birds [can] fly.
Elephants [can't|cannot|can not] jump.
## transform: Make the sentence negative (−).
I can swim. (−) => I can't swim. | I cannot swim. | I can not swim.
She can drive. (−) => She can't drive. | She cannot drive. | She can not drive.
They can dance. (−) => They can't dance. | They cannot dance. | They can not dance.
He can play chess. (−) => He can't play chess. | He cannot play chess. | He can not play chess.
We can sing. (−) => We can't sing. | We cannot sing. | We can not sing.
Hadi can cook. (−) => Hadi can't cook. | Hadi cannot cook. | Hadi can not cook.
You can take photographs here. (−) => You can't take photographs here. | You cannot take photographs here. | You can not take photographs here.
My son can ride a bike. (−) => My son can't ride a bike. | My son cannot ride a bike. | My son can not ride a bike.
## fix: Find and fix the mistake.
She [cans>can] swim.
I can [to drive>drive].
He can [swims>swim] very well.
I [don't can>can't|cannot] dance.
They [can't to>can't] sing.
Maya [can plays>can play] the guitar.
We [not can>can't|cannot] remember.
Can he [rides>ride] a bike?
## order: Put the words in order.
I can swim very well.
She can't drive a car.
They can play chess.
My grandmother can't walk fast.
Can you ride a bike?
He can sing and dance.
We can't remember the address.
Hiba is good with children.
## bank: Use the words.
I can [swim]. I go to the sea in Istanbul every summer.
Abu Salim can [drive] a car very well. He's a taxi driver.
Reem can [paint] a picture of the Citadel.
Lina can [dance] the dabke.
Maya can [sing] in English and Arabic.
Abu Firas can [play] chess very well.
I can't [remember] his name. What is it?
Kenji can [take] beautiful photographs.
""",
    ),
    dict(
        id="g2",
        title="Questions with can",
        visual=dict(type="table", head=["question", "yes", "no"],
                    rows=[["Can you swim?", "Yes, I can.", "No, I can't."], ["Can she drive?", "Yes, she can.", "No, she can't."],
                          ["Can they dance?", "Yes, they can.", "No, they can't."]],
                    colors=["purple", "teal", "coral"], cap="Can + person + verb?"),
        pattern=[
            ["?", ["Can", "v"], ["you", "s"], "swim?"],
            ["", "Yes, I", ["can.", "v"], ""],
            ["", "No, I", ["can't.", "n"], ""],
            ["?", "What", ["can", "v"], "you cook?"],
        ],
        examples=[
            "{Can} you play a musical instrument? — Yes, {I can}. The oud.",
            "{Can} Hadi repair my phone? — Yes, {he can}.",
            "{Can} your children swim? — No, {they can't}.",
            "{What can} you cook? — I can cook kibbeh and fattoush.",
        ],
        ar=[
            "لنسأل بـ can منقدّم can: Can you swim?",
            "الجواب القصير: Yes, I can. / No, I can't. ما منكرر الفعل.",
            "ما منستعمل do مع can: Do you can…? غلط.",
        ],
        watch=[("Do you can swim?", "Can you swim?"), ("Can you to drive?", "Can you drive?"), ("Can you swim? — Yes, I swim.", "Can you swim? — Yes, I can.")],
        quick="""
## choose: Choose the answer.
___ you play chess? | Can | Do can | Are can
Can she drive? — No, she ___. | can't | doesn't | isn't
What ___ you cook? | can | do can | cans
""",
        sets="""
## choose: Choose the answer.
___ you ride a bike? | Can | Do | Are
Can Hiba swim? — Yes, she ___. | can | does | swims
Can your children read? — No, they ___. | can't | don't | aren't
Can he ___ the piano? | play | plays | to play
What languages ___ you speak? | can | can do | are can
Can Abu Salim drive? — Yes, he ___. | can | drives | does
Can you remember my name? — No, I ___. Sorry! | can't | don't | not
___ Reem paint? | Can | Does can | Is
Can they dance? — Yes, they ___. | can | dance | do
Can I ___ a question? | ask | asks | to ask
## short: Answer the question.
Can you swim? (✓) => Yes, I can.
Can Joud read? (✗) => No, she can't. | No, she cannot.
Can Abu Salim drive? (✓) => Yes, he can.
Can babies walk? (✗) => No, they can't. | No, they cannot.
Can Maya sing? (✓) => Yes, she can.
Can your grandfather walk up the stairs? (✗) => No, he can't. | No, he cannot.
Can they play chess? (✓) => Yes, they can.
Can you remember the address? (✗) => No, I can't. | No, I cannot.
## transform: Make a question (?).
She can swim. (?) => Can she swim?
They can speak French. (?) => Can they speak French?
He can repair phones. (?) => Can he repair phones?
You can cook mansaf. (?) => Can you cook mansaf?
Lina can dance. (?) => Can Lina dance?
Your brother can drive. (?) => Can your brother drive?
The baby can walk. (?) => Can the baby walk?
We can take photographs. (?) => Can we take photographs?
## fix: Find and fix the mistake.
[Do you can>Can you] swim?
Can she [drives>drive]?
Can you [to play>play] chess?
Can Hadi cook? — Yes, he [does>can].
[Are you can>Can you] dance?
Can they swim? — No, they [don't>can't].
What [you can>can you] cook?
[Cans>Can] he ride a bike?
## order: Put the words in order.
Can you swim?
Can she drive a car?
What can you cook?
Can they play chess?
Can your son ride a bike?
What languages can you speak?
Can he touch his toes?
Can I take a photograph?
""",
    ),
    dict(
        id="g3",
        title="Review of questions",
        visual=dict(type="compare", cols=[
            dict(title="be", color="teal", items=["Are you Syrian?", "Is she a nurse?", "Where are they from?"]),
            dict(title="do / does", color="purple", items=["Do you live here?", "Does he work?", "What time do you get up?"]),
            dict(title="can", color="amber", items=["Can you swim?", "Can she drive?", "What can you cook?"]),
        ], cap="Three kinds of questions. Look at the verb."),
        pattern=[
            ["?", ["Is", "v"], "she", "a teacher? (be)"],
            ["?", ["Does", "v"], "she", "teach English? (do / does + verb)"],
            ["?", ["Can", "v"], "she", "speak English? (can + verb)"],
            ["?", "Where", ["does", "v"], "she work?"],
        ],
        examples=[
            "{Are} you a student? — Yes, I am.",
            "{Do} you like jazz? — Yes, I do.",
            "{Can} you play the guitar? — No, I can't.",
            "{Where does} Samer live? — In Qaboun.",
        ],
        ar=[
            "إذا الجملة فيها am / is / are منقدّمو بالسؤال: Is he Syrian?",
            "إذا فيها فعل عادي منحط do أو does: Does he live here?",
            "وإذا فيها can منقدّم can: Can he swim?",
        ],
        watch=[("Do you are a student?", "Are you a student?"), ("Is she live here?", "Does she live here?"), ("Does she can drive?", "Can she drive?")],
        quick="""
## choose: Choose the answer.
___ you a teacher? | Are | Do | Can
___ she work in a bank? | Does | Is | Can
___ you swim? | Can | Are | Does
""",
        sets="""
## choose: Choose the answer.
___ Hadi from Bab Touma? | Is | Does | Can
___ Nour work on Friday? | Does | Is | Are
___ you play the oud? | Can | Are | Is
Where ___ your parents live? | do | are | can
___ they Brazilian? | Are | Do | Can
What time ___ the bank open? | does | is | can
___ your sister swim? | Can | Is | Are
How old ___ your son? | is | does | can
___ you like fast food? | Do | Are | Can
Where ___ Mehmet from? | is | does | do
## bank: Use the words.
[Are] you on holiday?
[Do] you live in Mezzeh?
[Can] you speak Turkish?
[Is] Kareem a businessman?
[Does] Rana teach English?
[Can] Abu Salim drive fast?
[Do] they have children?
[Is] the bank open?
## short: Answer the question.
Are you a student? (✓) => Yes, I am.
Does Hadi like rock music? (✓) => Yes, he does.
Can Joud swim? (✗) => No, she can't. | No, she cannot.
Is Maya a barista? (✓) => Yes, she is.
Do your parents live in Dubai? (✗) => No, they don't. | No, they do not.
Can you play chess? (✓) => Yes, I can.
Is the shop open? (✗) => No, it isn't. | No, it's not. | No, it is not.
Does Salma work at night? (✓) => Yes, she does.
## fix: Find and fix the mistake.
[Do you are>Are you] a teacher?
[Is>Does] she live in Midan?
[Does she can>Can she] drive?
Where [she is>is she] from?
[Are>Do] you like dancing?
What time [you get>do you get] up?
[Does>Is] Tareq a chef?
Can you swim? — Yes, I [do>can].
## order: Put the words in order.
Are you a student?
Does she work in a bank?
Can you speak Turkish?
Where do you live?
Is he from Aleppo?
What can she cook?
Do they like football?
Where does Hala work?
## match: Match the question and the answer.
Are you a doctor? = No, I'm not. I'm a nurse.
Do you live near here? = Yes, I do. In Malki.
Can you speak English? = Yes, I can — a little!
Is Hadi late again? = Yes, he is!
Does Maya play the guitar? = Yes, she does.
Can your son swim? = No, he can't. He's two.
Where do you work? = In a bank in Marjeh.
What can you cook? = Kibbeh and fattoush.
""",
    ),
]

CLASSROOM = dict(
    phrases=["Can you write it on the board, please?", "Can I work with …?", "Whose turn is it?", "You go first.", "Let's start.",
             "Good luck!", "Well done!"],
    order="""
S: Can I work with Hiba?
T: Yes, of course. Let's start.
S: Whose turn is it?
S: You go first.
S: Good luck!
T: Well done, both of you!
""",
)

READING = dict(
    title="Special skills",
    text="""Mazen is a personal trainer at a gym in Mezzeh. He's very fit and sporty. He can run ten kilometres in fifty minutes, and he can touch his toes with his hands on the floor! He works with people of all ages. "One of my clients is seventy," he says. "He can't run, but he can walk fast."

Hiba is a nanny. She looks after two children, Tala and Karam. She's good with children, and she has a lot of skills. She can cook, she can sing, and she can paint pictures with them. She can't drive a car, so they walk to the park. Tala can ride a bike, but Karam is a baby — he can't walk yet!""",
    qs="""
## tf: True or false?
Mazen is fit and sporty. | T @ He's very fit and sporty
Mazen's client of seventy can run. | F @ He can't run
Hiba can drive a car. | F @ She can't drive a car
Hiba is good with children. | T @ She's good with children
Karam can walk. | F @ he can't walk yet
## choose: Choose the answer.
How far can Mazen run in fifty minutes? | ten kilometres | five kilometres | seventy kilometres @ He can run ten kilometres in fifty minutes
How do Hiba and the children go to the park? | They walk. | By car. | By bus. @ they walk to the park
## gap: Write one word.
Tala can ride a [bike]. @ Tala can ride a bike
""",
)

DIALOGUE = dict(
    title="A job interview",
    intro="A job interview for a dance teacher. Ruba asks Lina some questions.",
    task="gaps",
    lines="""
Ruba: So, Lina, [can] you dance the dabke?
Lina: Yes, I [can]. I can dance salsa, too.
Ruba: Great. Are you good [with] children?
Lina: Yes, I am. I have two nephews.
Ruba: Can you play a musical [instrument]?
Lina: No, I [can't]. But I can sing!
Ruba: Do you [work] at the weekend?
Lina: Yes, I do. Saturday is fine. When can I [start]?
""",
)

WQ = """
Yes, I can. I swim every week. (you / swim) => Can you swim?
No, she can't. She's five. (Joud / read) => Can Joud read?
Kibbeh and fattoush. (What / you / cook) => What can you cook?
Arabic, English and French. (What languages / you / speak) => What languages can you speak? | What languages do you speak?
Yes, he does. He loves it. (Hadi / like his job) => Does Hadi like his job?
Yes, he is. He's very fit. (Mazen / a personal trainer) => Is Mazen a personal trainer?
No, they can't. They're babies. (the children / walk) => Can the children walk?
In Mezzeh. (Where / Mazen / work) => Where does Mazen work?
"""

WRITING = [
    dict(task="Write about your skills: what can you do well? What can't you do?",
         tip="Use can / can't, well, fast, and be good at. Write 40–70 words.",
         model="I can do a lot of things! I can cook very well — my makdous is famous in my family. I can swim, and I can ride a bike. I'm good at maths. But I can't sing, and I can't drive a car. I can't dance the dabke very well, but I love it!",
         check=["can + verb (no to, no s)", "can't + verb", "well / fast / very well", "I'm good at …"],
         min=40, max=70),
]

CANDO = [
    "say what I can and can't do.",
    "ask 'Can you…?' and answer 'Yes, I can.' / 'No, I can't.'",
    "name parts of the body.",
    "ask questions with be, do / does and can.",
    "talk about skills for a job.",
]
