META = dict(n=10, title="Look good", pages="88–95")

BOOK = """
skirt, baseball cap, suit, dress, jacket, tie, jeans, trainers, jumper, shirt, trousers, shorts,
bossy, cheerful, confident, determined, shy, easy-going, sociable, friendly, hard-working,
smart clothes, appointment, casual clothes, suit someone, too big, fancy-dress party, jewellery, try something on,
uniform, larger size, party costume
"""

WORDS = """
@Clothes
skirt | women's clothes from the waist down, no legs | Rana is wearing a long blue skirt. | | lower
baseball cap | a soft hat with a peak at the front | Jad always wears a baseball cap. | | head
suit | a jacket and trousers of the same material | Kareem is wearing a grey suit today. | | formal
dress | one piece of women's clothing, top and skirt | Maya is wearing a red dress for the party. | | formal
jacket | a short coat | Take a jacket — it's cold in Bloudan. | | top
tie | a long thin piece of cloth you wear round your neck with a shirt | Ziad wears a tie at work. | | formal
jeans | blue trousers made of strong cotton | I usually wear jeans at the weekend. | | lower
trainers | sports shoes | Mazen is wearing new trainers. | | feet
jumper | a warm top made of wool | My grandmother knitted this jumper. | | top
shirt | a top with buttons and a collar | He's wearing a white shirt. | | top
trousers | clothes for your legs | These trousers are too long. | | lower
shorts | short trousers for summer | Kids wear shorts in summer. | | lower
@Personality
bossy | always telling other people what to do | My big sister is really bossy! | | neg
cheerful | happy and smiling | Um Khaled is always cheerful. | | pos
confident | sure about yourself | Maya is very confident on stage. | | pos
determined | you don't stop until you get what you want | Reem is determined to become a doctor. | | pos
shy | nervous with new people | Joud is shy with new people. | | quiet
easy-going | relaxed; you don't get angry easily | Hadi is easy-going — he's never stressed. | | pos
sociable | you like being with people | Hala is very sociable. She knows everyone. | | pos
friendly | kind and nice to people | The people in Midan are really friendly. | | pos
hard-working | you work a lot | Abu Omar is very hard-working. | | pos
@Other words
smart clothes | clothes for work or special events | You need smart clothes for the interview. | | style
appointment | a fixed time to see a doctor, a hairdresser… | I have an appointment at the hairdresser's at four.
casual clothes | comfortable clothes for every day | On Friday I wear casual clothes. | | style
suit someone | to look good on a person | That colour really suits you! | suit you;suits you;suits her;suit someone
too big | bigger than you need | These shoes are too big for me.
fancy-dress party | a party where people wear costumes | We had a fancy-dress party for Eid.
jewellery | rings, necklaces and earrings | Dima loves wearing jewellery.
try something on | to put on clothes in a shop to see if they fit | Can I try this jacket on? | try this jacket on;try something on;try it on
uniform | the same clothes for everyone in a school or a job | Nurses wear a uniform.
larger size | a bigger size | Have you got this in a larger size?
party costume | special clothes for a fancy-dress party | Reem is wearing a pirate party costume.
"""

ODD = """
skirt, dress, trousers, *tie | Tie: not for your legs.
shy, bossy, cheerful, *jumper | Jumper: clothes.
trainers, baseball cap, jeans, *suit | Suit: smart clothes.
I'm wearing, she's working, they're eating, *I wear | I wear: present simple.
confident, determined, hard-working, *uniform | Uniform: not personality.
know, like, want, *run | Run: not a 'state' verb.
"""

GRAMMAR = [
    dict(
        id="g1",
        title="Present continuous",
        visual=dict(type="timeline", now="now!", span={"from": -1, "to": 1, "label": "happening around now"},
                    marks=[dict(at=0, label="I'm wearing a jacket.")]),
        pattern=[
            ["+", "I", ["'m wearing", "v"], "a jacket."],
            ["+", "She", ["'s trying on", "v"], "a dress."],
            ["−", "They", ["aren't working", "n"], "today."],
            ["?", ["Are", "v"], "you", "listening? — Yes, I am."],
        ],
        examples=[
            "Kareem {is wearing} a grey suit today.",
            "Look! Maya {is trying on} a red dress.",
            "We {aren't working} today. It's Friday.",
            "What {are} you {doing}? — I'{m looking} for a uniform.",
        ],
        ar=[
            "المضارع المستمر لشي عم يصير هلق: I'm wearing a jacket (عم ألبس جاكيت).",
            "الشكل: am / is / are + الفعل مع ing.",
            "للنفي: isn't / aren't + ing، وللسؤال: Are you…ing?",
            "انتبه: لا تنسى am / is / are: She's wearing، مو She wearing.",
        ],
        watch=[("She wearing a dress.", "She's wearing a dress."), ("I am wear a suit.", "I'm wearing a suit."), ("Are you listen?", "Are you listening?")],
        quick="""
## choose: Choose the answer.
Kareem ___ a suit today. | is wearing | wearing | wears now
What ___ you doing? | are | do | is
They ___ working today. | aren't | don't | isn't
""",
        sets="""
## choose: Choose the answer.
Maya ___ a red dress today. | is wearing | wearing | wear
I ___ my homework now. | 'm doing | do | 'm do
Look! Hadi ___ his new trainers. | is trying on | try on | tries on now
We ___ working today. It's Friday. | aren't | don't | isn't
___ you listening to me? | Are | Do | Is
What is Reem ___? — A party costume. | wearing | wear | wears
The children ___ in the garden. | are playing | is playing | play now
She ___ her hair today — it's a holiday! | isn't doing | doesn't do | not doing
Are they waiting for the bus? — Yes, they ___. | are | do | waiting
Why ___ you smiling? | are | do | is
## gap: Write the -ing form.
She's [wearing] a long skirt. (wear)
I'm [trying] on a jacket. (try)
They're [shopping] in Sha'lan. (shop)
He's [running] in the park. (run)
We're [having] lunch. (have)
Maya is [dancing] at the party. (dance)
Are you [sitting] in the garden? (sit)
Dima is [making] a costume. (make)
## transform: Make the sentence negative (−).
I'm wearing a tie. (−) => I'm not wearing a tie. | I am not wearing a tie.
She's working today. (−) => She isn't working today. | She's not working today. | She is not working today.
They're watching TV. (−) => They aren't watching TV. | They're not watching TV. | They are not watching TV.
He's wearing a uniform. (−) => He isn't wearing a uniform. | He's not wearing a uniform. | He is not wearing a uniform.
We're having fun. (−) => We aren't having fun. | We're not having fun. | We are not having fun.
Maya is singing. (−) => Maya isn't singing. | Maya is not singing.
The baby is sleeping. (−) => The baby isn't sleeping. | The baby is not sleeping.
I'm trying it on. (−) => I'm not trying it on. | I am not trying it on.
## transform: Make a question (?).
She's wearing a dress. (?) => Is she wearing a dress?
They're having lunch. (?) => Are they having lunch?
You're listening. (?) => Are you listening?
He's working today. (?) => Is he working today?
Maya is trying on a jacket. (?) => Is Maya trying on a jacket?
The children are playing. (?) => Are the children playing?
It's raining. (?) => Is it raining?
You're wearing a uniform. (?) => Are you wearing a uniform?
## fix: Find and fix the mistake.
She [wearing>'s wearing|is wearing] a skirt.
I [am wear>'m wearing|am wearing] a suit.
Are you [listen>listening]?
They [is>are] playing football.
He's [runing>running] in the park.
We [don't>aren't|are not] working today.
What [you are>are you] doing?
She's [makeing>making] a costume.
## order: Put the words in order.
She's wearing a red dress.
I'm trying on a jacket.
They aren't working today.
Are you listening to me?
What are you doing?
He's wearing a grey suit.
We're having a great time.
Is Maya wearing her new trainers?
""",
    ),
    dict(
        id="g2",
        title="Present simple or present continuous?",
        visual=dict(type="compare", cols=[
            dict(title="present simple: always / usually", color="teal", items=["Ziad usually {wears} a tie.", "I {work} in a bank.", "every day, usually, never"]),
            dict(title="present continuous: now / today", color="purple", items=["Today he{'s wearing} a T-shirt.", "I{'m working} at home today.", "now, today, at the moment, look!"]),
        ], cap="State verbs (know, like, want, need) — present simple only: I know, not I'm knowing."),
        pattern=[
            ["", "He usually", ["wears", "v"], "a suit."],
            ["", "Today he", ["'s wearing", "x"], "jeans."],
            ["", "I", ["want", "v"], "a coffee. (not: I'm wanting)"],
        ],
        examples=[
            "Ziad usually {wears} a tie, but today he{'s wearing} a T-shirt.",
            "I {work} in an office, but this week I{'m working} at home.",
            "Salma {doesn't usually wear} jewellery. She{'s wearing} a uniform now.",
            "I {like} your jacket! (not: I'm liking)",
        ],
        ar=[
            "البسيط للعادة والشي الدايم: I usually wear jeans.",
            "المستمر للشي اللي عم يصير هلق أو هالفترة: Today I'm wearing a suit.",
            "أفعال متل like / know / want / need ما بتاخد ing: I want, مو I'm wanting.",
        ],
        watch=[("I'm usually wearing jeans.", "I usually wear jeans."), ("Look! It rains.", "Look! It's raining."), ("I'm knowing the answer.", "I know the answer.")],
        quick="""
## choose: Choose the answer.
Ziad usually ___ a tie. | wears | is wearing | wear
Today he ___ a T-shirt. | 's wearing | wears | wear
I ___ your jacket! | like | 'm liking | likes
""",
        sets="""
## choose: Choose the answer.
I usually ___ jeans at the weekend. | wear | 'm wearing | wearing
Look! Maya ___ a party costume. | 's wearing | wears | wear
Nurses ___ a uniform at work. | wear | are wearing now | wears
Shh! The baby ___. | 's sleeping | sleeps | sleep
Hadi ___ to the gym every Monday. | goes | is going | go
I ___ the answer. | know | 'm knowing | knowing
What ___ you doing at the moment? | are | do | does
She ___ coffee. She hates it. | doesn't drink | isn't drinking | not drink
We ___ a holiday this week, so we're at home. | 're having | have | has
Do you ___ this dress? | like | liking | likes
## choose: Simple or continuous? Choose the right sentence.
(now) | I'm wearing a jumper. | I wear a jumper now. | I wearing a jumper.
(every day) | She wears a uniform. | She's wearing a uniform every day. | She wearing a uniform.
(at the moment) | They're having lunch. | They have lunch at the moment. | They having lunch.
(usually) | He usually works late. | He's usually working late. | He usually working late.
(state verb) | I need a larger size. | I'm needing a larger size. | I needing a larger size.
(today) | Kareem is wearing a suit today. | Kareem wears a suit today. | Kareem wearing a suit today.
(never) | Rana never wears a tie. | Rana is never wearing a tie. | Rana never wearing a tie.
(look!) | Look! It's raining. | Look! It rains. | Look! It raining.
## gap: Write the verb in the present simple or continuous.
Ziad usually [wears] a suit. (wear)
Today he [is wearing|'s wearing] jeans. (wear)
I [work] in a bank. (work)
This week I [am working|'m working] at home. (work)
Look! Maya [is dancing|'s dancing]. (dance)
She [loves] dancing. (love)
We [don't like|do not like] bossy people. (not like)
Shh! I [am studying|'m studying]. (study)
## fix: Find and fix the mistake.
I [am usually wearing>usually wear] jeans.
Look! It [rains>'s raining|is raining].
I ['m knowing>know] the answer.
She [wears>'s wearing|is wearing] a red dress today.
He [is wanting>wants] a new jacket.
They [go>'re going|are going] to the shops now.
We [are having>have] dinner at eight every day.
Do you [liking>like] my costume?
## order: Put the words in order.
He usually wears a suit.
Today he's wearing jeans.
I'm working at home this week.
She doesn't usually wear jewellery.
What are you doing at the moment?
I know the answer.
Look! It's raining.
They usually have lunch at two.
""",
    ),
    dict(
        id="g3",
        title="Clothes",
        visual=dict(type="chips", groups=[
            dict(title="smart clothes", color="purple", items=["suit", "tie", "shirt", "dress", "skirt"]),
            dict(title="casual clothes", color="teal", items=["jeans", "trainers", "baseball cap", "shorts", "jumper", "T-shirt"]),
            dict(title="in a shop", color="amber", items=["Can I try it on?", "It's too big.", "Have you got a larger size?", "It suits you!"]),
        ]),
        pattern=[
            ["", "He's wearing", ["a suit and a tie.", "v"], "(smart)"],
            ["", "She's wearing", ["jeans and trainers.", "x"], "(casual)"],
            ["?", "Can I", ["try it on?", "v"], ""],
            ["", "It's", ["too big.", "n"], "Have you got a smaller size?"],
        ],
        examples=[
            "For the interview, wear {smart clothes}: a {suit} and a {tie}.",
            "On Friday I wear {casual clothes}: {jeans} and {trainers}.",
            "Can I {try on} this {jumper}? — Of course.",
            "That colour really {suits} you!",
        ],
        ar=[
            "smart clothes = لبس رسمي، casual clothes = لبس عادي ومريح.",
            "try something on = نجرّب اللبسة بالمحل، و It suits you = لابقلك.",
            "trousers و jeans و shorts دايماً جمع: My jeans are new.",
        ],
        watch=[("a jean", "jeans / a pair of jeans"), ("My trousers is black.", "My trousers are black."), ("Can I try on it?", "Can I try it on?")],
        quick="""
## choose: Choose the answer.
A jacket and trousers of the same colour: | a suit | a jumper | shorts
Sports shoes: | trainers | a tie | a skirt
My jeans ___ new. | are | is | be
""",
        sets="""
## choose: Choose the right word.
You wear it round your neck with a shirt. | a tie | a skirt | trainers
A soft hat for sport. | a baseball cap | a suit | a jumper
Short trousers for summer. | shorts | a dress | a tie
A warm top made of wool. | a jumper | shorts | a baseball cap
Blue trousers made of strong cotton. | jeans | a skirt | a suit
Sports shoes. | trainers | a tie | a dress
One piece of women's clothing, top and skirt. | a dress | a jacket | trousers
A short coat. | a jacket | a tie | shorts
## sort: Smart or casual? | smart | casual
smart: suit, tie, shirt, smart dress
casual: jeans, trainers, baseball cap, shorts
## bank: Use the words.
Can I [try] this jacket on?
These shoes are [too] big. Have you got a smaller size?
That colour really [suits] you!
Have you got this in a [larger] size?
For the interview, wear [smart] clothes.
On Friday I wear [casual] clothes.
Nurses wear a [uniform] at work.
Reem is wearing a pirate [costume] for the party.
## fix: Find and fix the mistake.
My jeans [is>are] new.
Can I try [on it>it on]?
These trousers [is>are] too long.
I want to buy [a jean>a pair of jeans|jeans].
That dress really [suits to>suits] you.
Have you got a [more large>larger] size?
He's wearing [a trainers>trainers].
It's [too much big>too big].
## order: Put the words in order.
Can I try it on?
It's too big for me.
Have you got a larger size?
That colour really suits you.
He's wearing a suit and a tie.
I wear casual clothes at the weekend.
These trainers are very comfortable.
She's wearing a long blue skirt.
""",
    ),
    dict(
        id="g4",
        title="Personality",
        visual=dict(type="faces", items=[["cheerful", "happy"], ["confident", "happy"], ["shy", "neutral"], ["bossy", "sad"]]),
        pattern=[
            ["", "Hadi", "is", ["easy-going.", "v"], "He's never stressed."],
            ["", "Joud", "is", ["shy.", "x"], "She's quiet with new people."],
            ["?", "What's she", ["like?", "v"], "— She's cheerful and sociable."],
        ],
        examples=[
            "Um Khaled is always {cheerful}.",
            "Reem is {determined} to become a doctor.",
            "My boss is very {bossy}!",
            "What's your brother {like}? — He's {easy-going} and {hard-working}.",
        ],
        ar=[
            "صفات الشخصية: cheerful (مبسوط دايماً)، shy (خجول)، bossy (بيحب يأمر).",
            "determined = مصمّم، easy-going = هادي ومو معقّد، hard-working = مجتهد.",
            "What's he like? يعني كيف شخصيتو؟ — مو شو بيحب!",
        ],
        watch=[("What does he like? (personality)", "What's he like?"), ("She is a shy.", "She's shy."), ("He is very work-hard.", "He's very hard-working.")],
        quick="""
## choose: Choose the answer.
She's always happy and smiling. She's ___. | cheerful | bossy | shy
He's nervous with new people. He's ___. | shy | confident | sociable
What's your sister ___? — She's friendly. | like | likes | liking
""",
        sets="""
## choose: Choose the right word.
She always tells people what to do. She's ___. | bossy | shy | cheerful
He's relaxed and never angry. He's ___. | easy-going | bossy | shy
She works very hard. She's ___. | hard-working | easy-going | shy
He's sure about himself. He's ___. | confident | shy | bossy
She loves being with people. She's ___. | sociable | shy | determined
He doesn't stop until he wins. He's ___. | determined | easy-going | shy
She's always happy. She's ___. | cheerful | bossy | shy
He's quiet with new people. He's ___. | shy | sociable | confident
## match: Match the opposites.
shy = confident
cheerful = miserable
hard-working = lazy
easy-going = stressed
sociable = unsociable
friendly = unfriendly
confident = nervous
determined = easily stopped
## gap: Write the word.
Hala knows everyone. She's very [sociable].
Abu Omar works fourteen hours a day. He's [hard-working].
Joud doesn't talk to new people. She's [shy].
My sister tells everyone what to do. She's [bossy].
Hadi is never stressed. He's [easy-going].
Maya sings on stage with no fear. She's [confident].
Um Khaled is always smiling. She's [cheerful].
Reem never stops until she wins. She's [determined].
## order: Put the words in order.
What's your brother like?
She's cheerful and friendly.
He's very hard-working.
Joud is shy with new people.
My boss is really bossy.
Hadi is easy-going.
Reem is determined to be a doctor.
Is your sister sociable?
""",
    ),
]

CLASSROOM = dict(
    phrases=["Could you check my writing, please?", "Have you finished?", "Would you like to go first?", "What's the opposite of …?",
             "Can I borrow your …?", "Let's change roles.", "That's a good idea!"],
    order="""
S: Have you finished?
S: Yes. Would you like to go first?
S: OK. What's the man in the photo wearing?
S: A suit and a tie. Let's change roles.
S: Could you check my writing, please?
T: Of course. That's a good idea!
""",
)

READING = dict(
    title="Clothes and personality",
    text="""Do your clothes show your personality? We visited a busy clothes shop in Sha'lan on a Saturday afternoon.

Dima is twenty-three, and she's a hairdresser. Today she's wearing a long purple skirt and a lot of jewellery. "I'm very creative and sociable," she says. "I usually wear bright colours. I never wear grey!"

Ziad is a lawyer. He usually wears a suit and a tie at work, but today he isn't working, so he's wearing jeans and a jumper. "I'm hard-working, but at the weekend I'm easy-going. My clothes are easy-going too!"

Joud is fourteen. She's shy, and she doesn't like shopping. At the moment, she's trying on a baseball cap, and her mother is waiting. "Do you like it?" her mother asks. "It really suits you." Joud is smiling — maybe she's a bit more confident today!""",
    qs="""
## tf: True or false?
Dima is wearing a purple skirt. | T @ she's wearing a long purple skirt
Dima often wears grey. | F @ I never wear grey
Ziad is working today. | F @ today he isn't working
Ziad usually wears a suit at work. | T @ He usually wears a suit and a tie at work
Joud loves shopping. | F @ she doesn't like shopping
## choose: Choose the answer.
What is Joud trying on? | a baseball cap | a skirt | a jumper @ she's trying on a baseball cap
What is Ziad like at the weekend? | easy-going | bossy | shy @ at the weekend I'm easy-going
## gap: Write one word.
Joud's mother is [waiting]. @ her mother is waiting
""",
)

DIALOGUE = dict(
    title="Can I try it on?",
    intro="A clothes shop in Sha'lan. Rana is looking for a jacket.",
    task="gaps",
    lines="""
Assistant: Hello. Are you looking [for] anything special?
Rana: Yes, I need a jacket for work. Something smart.
Assistant: What about this one? It's very popular.
Rana: It's nice. Can I try it [on]?
Assistant: Of course. … How is it?
Rana: It's [too] big. Have you got a smaller size?
Assistant: Yes, here you are. Oh, that colour really [suits] you!
Rana: Thank you. I [like] it. This one, please.
""",
)

WQ = """
I'm wearing a suit. (What / you / wear / today) => What are you wearing today?
Yes, she is. She's in the kitchen. (Um Khaled / cook / now) => Is Um Khaled cooking now?
She's cheerful and sociable. (What / Hala / like) => What's Hala like? | What is Hala like?
Jeans and trainers. (What / you / usually / wear / at the weekend) => What do you usually wear at the weekend?
No, he isn't. It's his day off. (Ziad / work / today) => Is Ziad working today?
Of course! (I / try / it on) => Can I try it on?
I'm looking for a dress. (What / you / look for) => What are you looking for?
No, she doesn't. She hates it. (Joud / like shopping) => Does Joud like shopping?
"""

WRITING = [
    dict(task="Look at the people around you (or think of your family). Write about three people: what they usually wear, what they're wearing today, and what they're like.",
         tip="Use the present simple and the present continuous, clothes and personality words. Write 80–120 words.",
         model="My father is a lawyer. He usually wears a suit and a tie, but today is Friday, so he's wearing a jumper and jeans. He's hard-working and very calm. My little sister, Mais, is eight. She usually wears her school uniform, but today she's wearing a party costume — she's a princess! She's cheerful and a bit bossy. My grandmother is wearing a long black dress and gold jewellery. She's sitting in the courtyard and drinking tea. She's sociable and kind.",
         check=["present simple for habits: usually wears", "present continuous for now: is wearing", "clothes words", "personality words: cheerful, shy, bossy…"],
         min=80, max=120),
]

CANDO = [
    "use the present continuous: I'm wearing…",
    "choose present simple or present continuous.",
    "talk about clothes and shopping for clothes.",
    "describe personality: What's he like?",
    "describe people in a photo.",
]
