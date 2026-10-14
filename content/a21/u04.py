META = dict(n=4, title="Likes and dislikes", pages="34–41")

BOOK = """
reading, cooking, spending time on the internet, spending time with friends, dancing, going for walks, swimming,
playing computer games, watching sport,
always, never, often, sometimes, usually,
album, in your free time, in the fresh air, artistic person, learn something new, at the beach, check your email,
make friends, concert, make mistakes, creative person, nervous, friendly person, relax with friends,
social networking sites, have fun, have a rest, win
"""

WORDS = """
@Free-time activities
reading | looking at books and understanding them | Reem loves reading. She reads every night.
cooking | making food | Um Khaled loves cooking for her neighbours.
spending time on the internet | using the internet for a long time | Hadi spends a lot of time on the internet. | spending time on the internet;spends a lot of time on the internet
spending time with friends | being with your friends | I love spending time with friends at the weekend.
dancing | moving to music | Lina loves dancing — she's a dance teacher!
going for walks | walking for fun | My grandparents like going for walks in the evening.
swimming | moving in water | Jad hates swimming. He doesn't like water!
playing computer games | playing games on a computer or a phone | Fadi's son loves playing computer games.
watching sport | looking at sport on TV or at a stadium | My father loves watching sport on TV.
@How often?
always | 100% of the time | Abu Omar always gets up early. | | freq
never | 0% of the time | Fadi never cooks. | | freq
often | a lot of times | Maya often goes to concerts. | | freq
sometimes | some of the time, not always | I sometimes go swimming on Fridays. | | freq
usually | most of the time | We usually have lunch at two. | | freq
@Other words
album | a collection of songs from one singer or band | Fairuz has got a lot of albums.
in your free time | when you aren't working or studying | What do you do in your free time?
in the fresh air | outside, not in a building | I love walking in the fresh air in Bloudan.
artistic person | a person who is good at art, music… | Reem is an artistic person. She paints and draws. | | person
learn something new | to study a new skill or subject | I like learning something new every month.
at the beach | by the sea, on the sand | We have fun at the beach in Latakia.
check your email | to look at your new emails | Rana checks her email every morning. | check your email;checks her email
make friends | to meet people and become friends | Maya makes friends easily.
concert | a music event with live music | There's a jazz concert at the Citadel on Thursday.
make mistakes | to do or say something wrong | Everyone makes mistakes in English — it's normal!
creative person | a person with a lot of new ideas | Dima is a creative person. | | person
nervous | worried and a bit afraid | Reem is nervous before exams.
friendly person | a person who is nice to other people | Hala is a very friendly person. | | person
relax with friends | to rest and have a good time with friends | On Fridays I relax with friends at a café.
social networking sites | websites like Facebook and Instagram | Hadi spends hours on social networking sites.
have fun | to enjoy yourself | We always have fun at Maya's parties!
have a rest | to stop and relax for a short time | Salma has a rest in the afternoon. | have a rest;has a rest
win | to be first in a game or a competition | Our team usually wins on Fridays.
"""

ODD = """
reading, cooking, dancing, *album | Album: not an activity.
always, often, never, *concert | Concert: not a frequency word.
works, goes, watches, *work | Work: no -s.
nervous, friendly, creative, *swimming | Swimming: an activity.
love, like, hate, *often | Often: a frequency word.
plays, studies, has, *do | Do: no -s.
"""

GRAMMAR = [
    dict(
        id="g1",
        title="Present simple: he / she / it",
        visual=dict(type="compare", cols=[
            dict(title="+ s", color="teal", items=["works", "likes", "plays", "reads"]),
            dict(title="+ es", color="purple", items=["goes", "watches", "does", "finishes"]),
            dict(title="y → ies · have → has", color="amber", items=["studies", "tries", "{has}"]),
        ], cap="he / she / it: add s! Negative and questions: does / doesn't + verb"),
        pattern=[
            ["+", "She", ["likes", "v"], "cooking."],
            ["−", "He", ["doesn't like", "n"], "swimming."],
            ["?", ["Does", "v"], "she", "play computer games? — Yes, she does."],
            ["?", "What", ["does", "v"], "he do in his free time?"],
        ],
        examples=[
            "Reem {reads} every night.",
            "Jad {doesn't like} swimming.",
            "{Does} Maya {go} to concerts? — Yes, {she does}.",
            "What {does} Hadi {do} in his free time? — He {plays} computer games.",
        ],
        ar=[
            "مع he / she / it الفعل بياخد s: she likes, he goes, she studies.",
            "للنفي doesn't + الفعل بلا s، وللسؤال Does + الشخص + الفعل بلا s.",
            "انتبه للغلطة المشهورة: He go → He goes.",
        ],
        en=[
            "He / she / it: add s to the verb → she likes, he goes, she studies.",
            "Negative: doesn't + verb, no s. Question: Does she + verb?",
            "Watch out: He go → He goes.",
        ],
        watch=[("He go to the gym.", "He goes to the gym."), ("She doesn't likes cooking.", "She doesn't like cooking."), ("Does he plays football?", "Does he play football?")],
        quick="""
## choose: Choose the answer.
Reem ___ every night. | reads | read | is read
Jad ___ like swimming. | doesn't | don't | isn't
___ Maya go to concerts? | Does | Do | Is
""",
        sets="""
## choose: Choose the answer.
Hadi ___ computer games. | plays | play | playing
Um Khaled ___ dinner for her neighbours. | cooks | cook | is cook
My father ___ sport on TV. | watches | watchs | watch
Salma ___ work at the weekend. | doesn't | don't | isn't
___ Rana check her email every day? | Does | Do | Is
Does Lina like dancing? — Yes, she ___. | does | do | likes
What ___ Maya do in her free time? | does | do | is
Reem ___ English and French. | studies | studys | study
Does Jad like swimming? — No, he ___. | doesn't | don't | isn't
Kareem ___ a fabric shop. | has | have | haves
## gap: Write the verb in the present simple.
Maya [goes] to concerts. (go)
Hadi [spends] a lot of time on the internet. (spend)
Rana [teaches] English. (teach)
Reem [studies] every evening. (study)
Abu Omar [has] a shop in Kafr Sousa. (have)
Dima [does] her friends' hair. (do)
Mazen [watches] sport on TV. (watch)
Hala [tries] new recipes at her café. (try)
## transform: Make the sentence negative (−).
She likes swimming. (−) => She doesn't like swimming. | She does not like swimming.
He plays tennis. (−) => He doesn't play tennis. | He does not play tennis.
Maya goes to the gym. (−) => Maya doesn't go to the gym. | Maya does not go to the gym.
Hadi watches sport. (−) => Hadi doesn't watch sport. | Hadi does not watch sport.
Rana has a car. (−) => Rana doesn't have a car. | Rana does not have a car.
He studies at night. (−) => He doesn't study at night. | He does not study at night.
She checks her email. (−) => She doesn't check her email. | She does not check her email.
Jad cooks at home. (−) => Jad doesn't cook at home. | Jad does not cook at home.
## transform: Make a question (?).
She likes reading. (?) => Does she like reading?
He goes to concerts. (?) => Does he go to concerts?
Maya plays the guitar. (?) => Does Maya play the guitar?
Reem studies French. (?) => Does Reem study French?
Hadi has a laptop. (?) => Does Hadi have a laptop?
She spends time online. (?) => Does she spend time online?
He watches sport. (?) => Does he watch sport?
Lina teaches dance. (?) => Does Lina teach dance?
## fix: Find and fix the mistake.
He [go>goes] to the gym every day.
She doesn't [likes>like] cooking.
[Do>Does] Maya play the guitar?
Hadi [watchs>watches] sport on TV.
Reem [studys>studies] at night.
Does he [plays>play] football?
She [don't>doesn't] work on Friday.
Abu Omar [have>has] a shop.
## order: Put the words in order.
She likes reading.
He doesn't like swimming.
Does Maya go to concerts?
What does Hadi do in his free time?
Reem studies every evening.
Does your sister play the piano?
He spends a lot of time online.
My father watches sport on TV.
""",
    ),
    dict(
        id="g2",
        title="like / love / hate + -ing",
        visual=dict(type="faces", items=[["love ♥♥", "happy"], ["like ♥", "happy"], ["don't mind", "neutral"], ["don't like", "sad"], ["hate", "sad"]]),
        pattern=[
            ["+", "I", ["love", "v"], ["dancing.", "x"]],
            ["+", "She", ["likes", "v"], ["going for walks.", "x"]],
            ["−", "He", ["doesn't like", "n"], ["swimming.", "x"]],
            ["", "We", ["don't mind", "v"], ["cooking.", "x"]],
            ["−", "They", ["hate", "n"], ["making mistakes.", "x"]],
        ],
        examples=[
            "Lina {loves dancing}.",
            "I {don't mind cooking}, but I {hate washing} the dishes!",
            "My grandparents {like going} for walks in the fresh air.",
            "Do you {like spending} time on social networking sites?",
        ],
        ar=[
            "بعد love / like / don't mind / hate منحط الفعل مع ing: I love dancing.",
            "don't mind يعني ما عندي مشكلة، مو كتير حلو ومو كتير عاطل.",
            "تهجئة ing: dance → dancing، swim → swimming، go → going.",
        ],
        en=[
            "After love / like / don't mind / hate: verb + ing → I love dancing.",
            "don't mind = it's OK, not good and not bad.",
            "Spelling: dance → dancing, swim → swimming, go → going.",
        ],
        watch=[("I like swim.", "I like swimming."), ("She loves to dancing.", "She loves dancing."), ("I hate cook.", "I hate cooking."), ("swiming", "swimming")],
        quick="""
## choose: Choose the answer.
I love ___ to Arabic music. | dancing | dance | to dancing #id=a21u4-84d02b7
She doesn't like ___. | swimming | swim | swiming
We don't mind ___. | cooking | cook | cooks
""",
        sets="""
## choose: Choose the answer.
Reem loves ___. | reading | read | reads
I hate ___ mistakes. | making | make | makeing
Do you like ___ sport? | watching | watch | watches
My mother doesn't mind ___. | cooking | cook | cooks
Hadi loves ___ computer games. | playing | play | plays
They like ___ for walks. | going | go | goes
She hates ___ her email on Friday. | checking | check | checks
We love ___ time with friends. | spending | spend | spends
Jad doesn't like ___. | swimming | swim | swiming
I don't mind ___ the bus. | taking | take | takeing
## gap: Write the -ing form.
I love [dancing]. (dance)
She hates [swimming]. (swim)
We like [going] for walks. (go)
He doesn't mind [cooking]. (cook)
They love [watching] sport. (watch)
Do you like [reading]? (read)
I hate [making] mistakes. (make)
Maya loves [singing]. (sing)
## sort: How do you write the -ing form? | + ing | e → ing | double + ing
+ ing: reading, cooking, watching, going
e → ing: dancing, making, taking, writing
double + ing: swimming, running, shopping, sitting
## bank: Use the words.
Lina is a dance teacher. She loves [dancing].
Jad doesn't like water. He hates [swimming].
Reem has a lot of books. She loves [reading].
Um Khaled loves [cooking] for her family.
My grandparents like [going] for walks.
Hadi likes [playing] computer games.
My father loves [watching] sport on TV.
I like [learning] something new.
## fix: Find and fix the mistake.
I like [swim>swimming].
She loves [to dancing>dancing].
We hate [cook>cooking].
He doesn't mind [makeing>making] mistakes.
Do you like [shoping>shopping]?
They love [go>going] to concerts.
I don't like [runing>running].
She hates [watch>watching] sport.
## order: Put the words in order.
I love dancing.
She doesn't like swimming.
We don't mind cooking.
Do you like reading?
He hates making mistakes.
They love going to concerts.
My mother likes going for walks.
I like spending time with friends.
""",
    ),
    dict(
        id="g3",
        title="How often? Frequency",
        visual=dict(type="scale", items=[["never", 0], ["sometimes", 40], ["often", 65], ["usually", 85], ["always", 100]]),
        pattern=[
            ["+", "I", ["always", "x"], "check my email."],
            ["+", "He", "'s", ["often", "x"], "late. (after be)"],
            ["?", ["How often", "v"], "do you", "go swimming?"],
            ["", "", ["once / twice / three times", "x"], "a week"],
        ],
        examples=[
            "Rana {always} checks her email in the morning.",
            "I {sometimes} go to concerts.",
            "Hadi is {often} on social networking sites.",
            "{How often} do you go swimming? — {Twice a week}.",
        ],
        ar=[
            "كلمات التكرار بتجي قبل الفعل العادي: I usually walk.",
            "وبعد am / is / are: She's always happy.",
            "How often…? منجاوب: once a week (مرة بالأسبوع)، twice a week (مرتين)، every day.",
        ],
        en=[
            "always / usually / often / never go before the verb: I usually walk.",
            "But after am / is / are: She's always happy.",
            "How often…? → once a week, twice a week, every day.",
        ],
        watch=[("I go always to the gym.", "I always go to the gym."), ("She always is late.", "She's always late."), ("two times a week", "twice a week")],
        quick="""
## choose: Choose the answer.
I ___ go swimming. (40%) | sometimes | always | never
He's ___ late. (0%) | never | always | usually
How ___ do you check your email? | often | many | much
""",
        sets="""
## choose: Choose the right sentence.
(always) I check my email. | I always check my email. | I check always my email. | I check my always email.
(often) She is late. | She is often late. | She often is late is. | Often she late is.
(never) We go dancing. | We never go dancing. | We go never dancing. | We go dancing never never.
(usually) He has lunch at two. | He usually has lunch at two. | He has lunch usually usually at two. | He has lunch at usually two.
(sometimes) They are nervous. | They are sometimes nervous. | They sometimes are nervous are. | They nervous sometimes are.
(always) Maya has fun at parties. | Maya always has fun at parties. | Maya has always fun at parties. | Maya has fun always at parties always.
(never) I make mistakes! | I never make mistakes! | I make never mistakes! | I make mistakes never never!
(often) Dima goes to the beach. | Dima often goes to the beach. | Dima goes to the often beach. | Dima goes to often the beach.
## choose: Choose the answer.
I go swimming every Monday and Thursday. I go ___. | twice a week | once a week | three times a week
She checks her email at 8:00, 13:00 and 20:00. She checks it ___. | three times a day | twice a day | once a day
We have a concert in May only. We have it ___. | once a year | twice a year | every month
Hadi plays football every Friday. He plays ___. | once a week | twice a week | every day #id=a21u4-7872d1f
Reem reads every night. She reads ___. | every day | once a week | never
I go to my grandparents' house every Friday and Saturday. I go ___. | twice a week | once a week | three times a week #id=a21u4-44d32e1
Jad hates swimming. He ___ swims. | never | always | often
Abu Omar gets up early every day. He ___ gets up early. | always | sometimes | never
## gap: Write the frequency word.
I check my email every day. I [always] check it.
Fadi doesn't cook — not once! He [never] cooks. #id=a21u4-40945b3
We go out most weekends. We [usually] go out.
She goes to concerts — a lot. She [often] goes.
I go to the gym some weeks, but not all. I [sometimes] go.
He has a rest every afternoon. He [always] has a rest.
They go swimming three or four times a month. They [often] go swimming.
I'm always on time. I'm [never] late. #id=a21u4-fdcead6
## order: Put the words in order.
I always check my email.
How often do you go swimming?
She's never late.
We usually have fun at the beach.
He sometimes plays computer games.
I go to the gym twice a week.
They often relax with friends.
Do you usually make friends easily?
## short: Answer about you. Write a full sentence.
How often do you go swimming? (sometimes) => I sometimes go swimming.
How often do you check your email? (always) => I always check my email.
How often do you cook? (often) => I often cook.
How often are you nervous? (sometimes) => I'm sometimes nervous. | I am sometimes nervous.
How often do you go to concerts? (never) => I never go to concerts.
How often do you watch sport? (usually) => I usually watch sport.
How often are you late? (never) => I'm never late. | I am never late.
How often do you go for walks? (often) => I often go for walks.
""",
    ),
]

CLASSROOM = dict(
    phrases=["I agree. / I don't agree.", "What do you think?", "Shall we start?", "Let's change roles.", "It's my turn.", "You go first.", "Well done!"],
    order="""
S: Shall we start?
S: Yes. You go first.
S: OK. I think reading is a great hobby. What do you think?
S: I don't agree. I think dancing is fantastic!
S: Let's change roles. It's my turn now.
T: Well done, both of you!
""",
)

READING = dict(
    title="What do you do in your free time?",
    text="""Three people in Damascus answer our question.

Dima, hairdresser, 23: "I'm a very creative person. In my free time, I love drawing and painting. I usually go to an art class on Saturdays — I always learn something new. I don't like watching sport. It's boring!"

Mazen, personal trainer, 30: "I love being in the fresh air. I go for walks on Mount Qasioun twice a week, and I sometimes go swimming. I don't spend a lot of time on the internet. I hate social networking sites!"

Hiba, nanny, 26: "I'm a friendly person, and I love making friends. My friends and I often meet at a café in Sha'lan on Fridays. We have fun, and we relax. I don't mind cooking, but I hate washing the dishes!" """,
    qs="""
## tf: True or false?
Dima likes watching sport. | F @ I don't like watching sport
Mazen goes for walks twice a week. | T @ I go for walks on Mount Qasioun twice a week
Mazen loves social networking sites. | F @ I hate social networking sites
Hiba often meets her friends on Friday. | T @ My friends and I often meet at a café in Sha'lan on Friday
Hiba hates cooking. | F @ I don't mind cooking
## choose: Choose the answer.
What does Dima do on Saturday? | She goes to an art class. | She goes swimming. | She watches sport. @ I usually go to an art class on Saturday
Who is a creative person? | Dima | Mazen | Hiba @ I'm a very creative person
## gap: Write one word.
Hiba hates washing the [dishes]. @ I hate washing the dishes
""",
)

DIALOGUE = dict(
    title="Are we a good match?",
    intro="A language exchange website. Ahmad and Pierre plan their first meeting.",
    task="gaps",
    lines="""
Ahmad: So, Pierre, what do you do in your [free] time?
Pierre: I love [reading], and I often go to concerts.
Ahmad: Me too! How [often] do you go?
Pierre: About [twice] a month. Does your sister like music too?
Ahmad: Yes, she [does]. She plays the oud.
Pierre: Fantastic! Do you like [cooking]?
Ahmad: No, I hate it! But my mother always [cooks] for guests.
Pierre: Great — I [never] say no to Syrian food!
""",
)

WQ = """
She plays tennis. (What / Maya / do in her free time) => What does Maya do in her free time?
Yes, he does. He loves it. (Hadi / like computer games) => Does Hadi like computer games?
Twice a week. (How often / you / go swimming) => How often do you go swimming?
No, she doesn't. She hates it. (Reem / like watching sport) => Does Reem like watching sport?
In Sha'lan. (Where / Hiba / meet her friends) => Where does Hiba meet her friends?
Yes, I do. I love dancing. (you / like dancing) => Do you like dancing?
Every morning. (When / Rana / check her email) => When does Rana check her email?
He's a personal trainer. (What / Mazen / do) => What does Mazen do?
"""

WRITING = [
    dict(task="Write about a friend or family member's free time: what he or she loves, likes, doesn't mind and hates, and how often.",
         tip="Use he / she + verb-s, love / like / hate + -ing, and frequency words. Write 60–90 words.",
         model="My cousin Joud is fifteen. In her free time she loves reading and drawing. She usually reads in bed at night. She likes going for walks with her friends in Tishreen Park, and she sometimes goes swimming at the club. She doesn't mind cooking — she often helps my aunt. But she hates watching sport on TV. She says it's boring!",
         check=["he / she + verb-s", "love / like / don't mind / hate + -ing", "always / usually / sometimes / never", "once / twice a week"],
         min=60, max=90),
]

CANDO = [
    "use the present simple with he, she and it.",
    "say what I like, love and hate doing.",
    "ask 'Does she…?' and 'What does he do…?'",
    "use frequency words: always, usually, sometimes.",
    "ask 'How often…?' and answer 'twice a week'.",
]

PUZZLES = dict(
    case=dict(
        title="Who loves cooking?",
        story="Reem, Maya, Fadi and Salma talk about their free time. Each friend loves a different activity and has a different job. They all go to concerts at the Opera House — but how often?",
        people=["Reem", "Maya", "Fadi", "Salma"],
        groups=[["reading", "dancing", "cooking", "swimming"], ["always", "often", "sometimes", "never"], ["artist", "student", "taxi driver", "nurse"]],
        group_names=["loves", "concerts", "job"],
        clues=[
            dict(t="The student often goes to concerts.", f=("is", "student", "often")),
            dict(t="Reem doesn't like swimming.", f=("not", "Reem", "swimming")),
            dict(t="The nurse loves cooking.", f=("is", "nurse", "cooking")),
            dict(t="Fadi never goes to concerts.", f=("is", "Fadi", "never"), need=False),
            dict(t="Maya loves dancing.", f=("is", "Maya", "dancing")),
            dict(t="The person who loves cooking always goes to concerts.", f=("is", "cooking", "always")),
            dict(t="Fadi is a taxi driver.", f=("is", "Fadi", "taxi driver")),
            dict(t="Reem sometimes goes to concerts.", f=("is", "Reem", "sometimes")),
        ],
        question=dict(q="Who loves cooking?", target="cooking", among="people"),
        reveal="Salma loves cooking. She's a nurse, and she always goes to concerts. Fadi loves swimming, but he never goes to concerts.",
    ),
    escape=dict(
        place="the old library",
        intro="You love reading, so you often spend Friday afternoon in the old library. Today it's late, and the door isn't open! Open the locks.",
        ending="The door is open! You always have fun in the library — but next time, check the time!",
    ),
    riddles=[
        ("reading", ["Your eyes go from left to right — or right to left in Arabic!", "Reem does it every night.", "You need a book or a newspaper."]),
        ("swimming", ["Jad hates it.", "You need a pool or the sea.", "You do it in water."]),
        ("cooking", ["Fadi never does it.", "Um Khaled loves it — her kibbeh is famous!", "You do it in the kitchen."]),
        ("dancing", ["You don't need your hands — only your feet!", "People usually do it at weddings.", "You move your body to music."]),
        ("concert", ["People buy tickets for me.", "A band or a singer is on the stage.", "I'm an event with live music."]),
        ("album", ["I've got ten or twelve songs.", "A singer makes a new one every year or two.", "Fairuz has got a lot of these."]),
        ("never", ["I'm the opposite of 'always'.", "I'm 0%.", "Fadi ___ cooks. Not once!"]),
        ("nervous", ["Your hands are cold, and your heart is fast.", "Reem feels like this before exams.", "You're worried and a bit afraid."]),
    ],
)
