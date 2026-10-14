META = dict(n=12, title="What do you want?", pages="88–97")

BOOK = """
get a cat, go diving, see the Northern Lights, travel round the world, join a singing group, start a football team,
do a course in jewellery making, take part in a TV quiz show, meet a famous film star, perform on stage,
clothes, jeans, a scarf, a jacket, a T-shirt, a handbag, an umbrella, accessories, technology, jewellery, earrings,
a necklace, a bracelet,
red, orange, yellow, green, blue, purple, brown, white, black, grey, small, medium, large, extra-large,
fun, boring, frightening, exciting, sociable, creative, carry, buy online
"""

WORDS = """
@Wants
get a cat | to take a cat into your home as a pet | Joud wants to get a cat.
go diving | to swim under the sea with special equipment | Hadi wants to go diving in the Red Sea.
see the Northern Lights | to see green and purple lights in the sky in the far north | I want to see the Northern Lights in Iceland.
travel round the world | to visit a lot of countries on one long trip | Tareq wants to travel round the world.
join a singing group | to become a member of a group that sings together | Maya wants to join a singing group.
start a football team | to make a new team for football | Jad is going to start a football team in Jaramana.
do a course in jewellery making | to study how to make rings and necklaces | Dima is going to do a course in jewellery making.
take part in a TV quiz show | to be a player in a question game on TV | Reem wants to take part in a TV quiz show.
meet a famous film star | to see and talk to a very famous actor | Lina wants to meet a famous film star.
perform on stage | to sing, dance or act in front of people | Maya is going to perform on stage in June.
@Things you can buy
clothes | things you wear, like shirts and trousers | I want some new clothes for Eid.
jeans | trousers made of strong cotton, often blue | These jeans are very comfortable. | | wear-legs
scarf | a long piece of cloth for your neck | I want a red scarf for winter. | | wear
jacket | a short coat | Are you going to buy that leather jacket? | | wear
T-shirt | a cotton shirt with short sleeves and no buttons | I want a white T-shirt, size medium. | | wear
handbag | a bag for women to carry small things | Rana wants a new handbag. | | bag
umbrella | you hold it over your head in the rain | Take an umbrella — it's going to rain!
accessories | small things you wear: bags, belts, scarves | The shop sells clothes and accessories.
technology | phones, computers and machines | Hadi loves technology.
jewellery | rings, necklaces and earrings | Souq al-Hamidiyah has a lot of jewellery shops.
earrings | jewellery for your ears | My sister wants gold earrings. | | jewel
necklace | jewellery you wear round your neck | That necklace is beautiful! | | jewel
bracelet | jewellery you wear round your wrist | I'm going to buy a silver bracelet. | | jewel
@Colours and sizes
red | the colour of tomatoes | I want the red scarf, please. | | colour
orange | the colour of carrots | Do you have this T-shirt in orange? | | colour
yellow | the colour of the sun | Yellow is a happy colour. | | colour
green | the colour of grass | My favourite colour is green. | | colour
blue | the colour of the sky | I want blue jeans. | | colour
purple | red + blue | Purple is Maya's favourite colour. | | colour
brown | the colour of coffee | I'm going to buy brown shoes. | | colour
white | the colour of milk | A white T-shirt, please. | | colour
black | the colour of the night | He wants a black jacket. | | colour
grey | black + white | The sky is grey today. | | colour
small | size S | Do you have it in small? | | size
medium | size M | I'm a medium. | | size
large | size L | This jacket is large. | | size
extra-large | size XL | My brother wants extra-large. | | size
@Other words
fun | nice and you enjoy it | The party is going to be fun! | | good
boring | not interesting | That film was boring. | | bad
frightening | it makes you afraid | Diving is a bit frightening for me. | | bad
exciting | very interesting, it makes you happy | Travelling round the world is exciting! | | good
sociable | you like being with people | Maya is very sociable. | | person
creative | you have new ideas and make things | Dima is very creative. | | person
carry | to hold and take something with you | Can you carry my bag, please?
buy online | to buy things on the internet | I usually buy online — it's easy.
"""

ODD = """
earrings, necklace, bracelet, *jeans | Jeans: clothes, not jewellery.
red, blue, green, *large | Large: a size.
small, medium, extra-large, *purple | Purple: a colour.
boring, frightening, exciting, *umbrella | Umbrella: not an adjective.
want, wants, want to, *going | Going: going to.
jacket, scarf, T-shirt, *technology | Technology: not clothes.
go diving, travel round the world, join a singing group, *grey | Grey: a colour.
"""

GRAMMAR = [
    dict(
        id="g1",
        title="want and want to",
        visual=dict(type="compare", cols=[
            dict(title="want + noun", color="teal", items=["I want {a cat}.", "She wants {a new jacket}.", "We want {pizza}."]),
            dict(title="want to + verb", color="purple", items=["I want {to travel}.", "He wants {to go} diving.", "They want {to meet} a star."]),
        ], cap="want + a thing · want to + an action"),
        pattern=[
            ["+", "I / you / we / they", ["want", "v"], "a new phone."],
            ["+", "He / she", ["wants to", "v"], "travel round the world."],
            ["−", "I", ["don't want to", "n"], "go diving."],
            ["?", ["Does", "v"], "she", "want a cat? — Yes, she does."],
            ["?", "What", ["do", "v"], "you want to do?"],
        ],
        examples=[
            "Joud {wants} a cat.",
            "Tareq {wants to} travel round the world.",
            "I {don't want to} perform on stage — it's frightening!",
            "{Do} you {want to} join a singing group? — Yes, I do!",
        ],
        ar=[
            "want يعني بدّي: I want a cat (بدي بسة).",
            "إذا بعدها فعل منحط to: I want to travel، مو I want travel.",
            "مع he و she: wants. وبالنفي والسؤال منستعمل do / does: She doesn't want to go.",
        ],
        en=[
            "{want} + a thing: I want a cat.",
            "want + {to} + verb: I want to travel. (not: I want travel)",
            "He / she → {wants}: She wants a new jacket.",
            "Negative and question: She {doesn't} want to go. {Does} she want a cat?",
        ],
        watch=[("I want travel.", "I want to travel."), ("She want a cat.", "She wants a cat."), ("I am want a phone.", "I want a phone."),
               ("He doesn't wants to go.", "He doesn't want to go.")],
        quick="""
## choose: Choose the answer.
I want ___ a new phone. | to buy | buy | buying
Joud ___ a cat. | wants | want | is want
I don't want ___ diving. | to go | go | going
""",
        sets="""
## choose: Choose the answer.
Maya ___ to join a singing group. | wants | want | is want
I want ___ the Northern Lights. | to see | see | seeing
They want ___ new car. | a | to | an
I want ___ cup of tea, please. | a | to | an
Hadi doesn't want ___ to the party. | to go | go | going
What ___ you want for your birthday? | do | are | does
Reem wants ___ part in a TV quiz show. | to take | take | taking
We ___ want to go out tonight. | don't | aren't | doesn't
Does Lina ___ to meet a film star? | want | wants | wanting
It's going to rain. I want ___ umbrella. | an | to | a
## gap: Write want, wants, want to or wants to.
I [want] a new jacket.
Joud [wants] a cat.
We [want to] travel round the world.
Hadi [wants to] go diving.
My parents [want] a new car.
Maya [wants to] perform on stage.
I [want to] do a course in jewellery making.
Dima [wants] a silver bracelet.
## transform: Write a sentence with want or want to.
a cat (Joud) => Joud wants a cat.
go diving (I) => I want to go diving.
a new phone (Hadi) => Hadi wants a new phone.
see the Northern Lights (we) => We want to see the Northern Lights.
join a singing group (Maya) => Maya wants to join a singing group.
a red scarf (I) => I want a red scarf.
meet a film star (Lina) => Lina wants to meet a film star.
travel round the world (they) => They want to travel round the world.
## fix: Find and fix the mistake.
I want [travel>to travel] round the world.
She [want>wants] a cat.
I [am want>want] a new phone.
He doesn't [wants>want] to go.
We want [to a>a] new car.
[Does>Do] you want to come?
Reem [wants take>wants to take] part in a quiz show.
They [doesn't>don't] want to go diving.
## order: Put the words in order.
I want to see the Northern Lights.
She wants a new handbag.
Do you want to go diving?
He doesn't want to perform on stage.
What do you want for your birthday?
We want to travel round the world.
Joud wants a cat.
Does Maya want to join a singing group?
""",
    ),
    dict(
        id="g2",
        title="going to",
        visual=dict(type="timeline", now="now: the plan is in my head", marks=[dict(at=2, label="next week", text="I'm going to buy it."),
                                                                             dict(at=3, label="next year", text="")],
                    span={"from": 0, "to": 3, "label": "plans for the future"}),
        pattern=[
            ["+", "I", ["'m going to", "v"], "buy a jacket."],
            ["+", "She", ["'s going to", "v"], "do a course."],
            ["−", "We", ["aren't going to", "n"], "go out."],
            ["?", ["Are", "v"], "you", "going to travel? — Yes, I am."],
            ["?", "What", ["are", "v"], "you going to do?"],
        ],
        examples=[
            "I'm {going to} buy a new jacket on Saturday.",
            "Dima {is going to} do a course in jewellery making.",
            "We {aren't going to} eat out tonight.",
            "{Are} you {going to} perform on stage? — Yes, I am!",
        ],
        ar=[
            "going to منستعملها للخطط بالمستقبل: رح + فعل: I'm going to travel = رح سافر.",
            "الشكل: am / is / are + going to + الفعل.",
            "للنفي: I'm not going to…، وللسؤال: Are you going to…?",
        ],
        en=[
            "{going to} = a plan for the future: I'm going to travel.",
            "am / is / are + going to + verb: She's {going to} buy a car.",
            "Negative: I'm {not} going to… Question: {Are} you going to…?",
        ],
        watch=[("I going to buy it.", "I'm going to buy it."), ("She's going buy a car.", "She's going to buy a car."),
               ("Are you going to bought it?", "Are you going to buy it?")],
        quick="""
## choose: Choose the answer.
I'm going ___ buy a scarf. | to | for | —
She ___ going to travel. | 's | are | going
___ you going to buy it? | Are | Do | Is
""",
        sets="""
## choose: Choose the answer.
I ___ going to buy a new phone. | 'm | 's | are
Jad is going to ___ a football team. | start | starts | started
We ___ going to eat out tonight. | aren't | isn't | don't
___ she going to do a course? | Is | Are | Does
They're going ___ travel round the world. | to | for | at
Are you going to buy the jacket? — Yes, I ___. | am | do | going
What are you going to ___ at the weekend? | do | doing | does
Maya ___ going to perform on stage. | is | are | am
It's cloudy. It's going to ___. | rain | rains | rained
Hadi isn't going ___ go diving. | to | for | —
## gap: Write am, is or are.
I [am|'m] going to buy a scarf.
Dima [is|'s] going to make a necklace.
We [are|'re] going to see the Northern Lights.
[Are] you going to join the singing group?
Jad [is|'s] going to start a team.
They [are|'re] going to buy a flat.
[Is] Reem going to take part in the quiz?
I [am|'m] not going to eat fast food.
## transform: Make the sentence negative (−).
I'm going to buy it. (−) => I'm not going to buy it. | I am not going to buy it.
She's going to travel. (−) => She isn't going to travel. | She's not going to travel. | She is not going to travel.
We're going to eat out. (−) => We aren't going to eat out. | We're not going to eat out. | We are not going to eat out.
They're going to get a cat. (−) => They aren't going to get a cat. | They're not going to get a cat. | They are not going to get a cat.
He's going to go diving. (−) => He isn't going to go diving. | He's not going to go diving. | He is not going to go diving.
I'm going to wear the blue jacket. (−) => I'm not going to wear the blue jacket. | I am not going to wear the blue jacket.
Maya is going to sing. (−) => Maya isn't going to sing. | Maya is not going to sing.
It's going to rain. (−) => It isn't going to rain. | It's not going to rain. | It is not going to rain.
## transform: Make a question (?).
You're going to buy a car. (?) => Are you going to buy a car?
She's going to do a course. (?) => Is she going to do a course?
They're going to travel. (?) => Are they going to travel?
He's going to start a team. (?) => Is he going to start a team?
Maya is going to perform. (?) => Is Maya going to perform?
You're going to buy it online. (?) => Are you going to buy it online?
It's going to be exciting. (?) => Is it going to be exciting?
We're going to meet at six. (?) => Are we going to meet at six?
## fix: Find and fix the mistake.
I [going to>'m going to|am going to] buy a jacket.
She's going [buy>to buy] earrings.
We're going to [went>go] to Bloudan.
[Do>Are] you going to travel?
He [are>is|'s] going to start a business.
They're going to [buys>buy] a flat.
I'm not [go>going] to eat out.
Is she going to [doing>do] a course?
## order: Put the words in order.
I'm going to buy a new jacket.
She's going to do a course.
Are you going to travel?
We aren't going to eat out.
What are you going to do?
He's going to start a football team.
Is it going to rain?
They're going to see the Northern Lights.
""",
    ),
]

CLASSROOM = dict(
    phrases=["Can I work with …?", "Sorry, can you speak louder, please?", "Can you help me?", "I think it's …", "I'm not sure.",
             "Well done!", "See you tomorrow. / See you next lesson."],
    order="""
T: Work in pairs, please.
S: Can I work with Reem?
T: Yes, of course.
S: Can you help me? Is it 'want' or 'want to'?
T: 'I want to go.' Want to + verb.
S: Thank you! See you tomorrow.
""",
)

READING = dict(
    title="Big plans",
    text="""Maya is nineteen. She's a student, and she works part-time as a barista in Baramkeh. She's very sociable and creative, and she has big plans!

First, she wants to join a singing group. "I love jazz," she says. "I'm going to perform on stage in June. It's going to be exciting, but a bit frightening, too!"

Next winter, she's going to visit her cousin in Toronto. She doesn't want to go diving or skiing — she wants to see the big lakes and visit museums. "I'm going to buy a warm jacket and a good umbrella," she laughs. "It's cold in Canada!"

One day, she wants to travel round the world. "But first, I'm going to finish university!" """,
    qs="""
## tf: True or false?
Maya is sociable and creative. | T @ She's very sociable and creative
She's going to perform on stage in June. | T @ I'm going to perform on stage in June
She wants to go diving in Canada. | F @ She doesn't want to go diving or skiing
She's going to visit her cousin in Toronto. | T @ she's going to visit her cousin in Toronto
She's going to buy a scarf. | F @ I'm going to buy a warm jacket and a good umbrella
## choose: Choose the answer.
What does Maya want to do first? | join a singing group | travel round the world | go skiing @ First, she wants to join a singing group
What is she going to do before travelling round the world? | finish university | buy a car | get a cat @ But first, I'm going to finish university
## gap: Write one word.
Maya loves [jazz]. @ I love jazz
""",
)

DIALOGUE = dict(
    title="In a clothes shop",
    intro="A clothes shop in Sha'lan. Fadi wants a present for his wife.",
    task="gaps",
    lines="""
Assistant: Hello! Can I help you?
Fadi: Yes, please. I [want] a scarf for my wife.
Assistant: What [colour] does she like?
Fadi: Purple, I think. Or [grey].
Assistant: This purple scarf is very popular. And it's not expensive.
Fadi: It's lovely. Do you have [earrings], too?
Assistant: Yes. These silver earrings go well [with] the scarf.
Fadi: Perfect. I'm going to [buy] both!
""",
)

WQ = """
I want a new phone. (What / you / want) => What do you want?
Yes, she does. She loves cats. (Joud / want a cat) => Does Joud want a cat?
I'm going to visit my grandparents. (What / you / do / at the weekend) => What are you going to do at the weekend?
No, I'm not. I'm going to buy it online. (you / buy it in the shop) => Are you going to buy it in the shop?
Medium, please. (What size / you / want) => What size do you want?
Yes, he is. In June. (Jad / start a team) => Is Jad going to start a team?
To Toronto. (Where / Maya / go next winter) => Where is Maya going to go next winter? | Where's Maya going to go next winter? | Where is Maya going next winter? #id=a12u12-dbae050
Blue. (What colour / you / want) => What colour do you want?
"""

WRITING = [
    dict(task="Write about your plans and wishes: three things you want to do one day, and three things you're going to do this year.",
         tip="Use want to and going to. Write 50–80 words.",
         model="One day, I want to travel round the world. I want to see the Northern Lights, and I want to meet a famous film star! This year, I'm going to do a course in English. I'm going to buy a new laptop for my studies. I'm not going to eat fast food — I'm going to cook at home!",
         check=["want to + verb", "going to + verb", "I'm not going to …", "time words: one day, this year, next summer"],
         min=50, max=80),
]

CANDO = [
    "say what I want: I want a new phone.",
    "use want to + verb: I want to travel.",
    "talk about plans with going to.",
    "ask 'Are you going to…?' and 'What are you going to do?'",
    "talk about clothes, colours and sizes in a shop.",
]
