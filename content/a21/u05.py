META = dict(n=5, title="From A to B", pages="42–51")

BOOK = """
bicycle, underground train, drive a car, fly, get off, get on, ride a bicycle, ride a scooter, take a bus,
wait for a bus, walk to work,
board the plane, destination, boarding pass, gate number, book your ticket online, go through immigration,
check-in desk, go through security, luggage, screens,
several times a week, smoke, once a week, twice a week, terminal, public transport
"""

WORDS = """
@Transport
bicycle | a bike: two wheels, you move it with your feet | I go to university by bicycle.
underground train | a train under the ground in a big city | In London, people say 'the Tube' for the underground train. | | train
drive a car | to control a car on the road | Can you drive a car?
fly | to travel by plane | We fly to Dubai once a year.
get off | to leave a bus or a train | Get off the bus at Marjeh Square. | | onoff
get on | to go into a bus or a train | Get on the bus at the university. | | onoff
ride a bicycle | to travel on a bicycle | Joud can ride a bicycle.
ride a scooter | to travel on a small motorbike | In Rome, a lot of people ride a scooter to work.
take a bus | to travel by bus | I take a bus to work every day.
wait for a bus | to stand at a bus stop until the bus comes | I wait for a bus for twenty minutes every morning.
walk to work | to go to your job on foot | Rana walks to work — her school is near her flat. | walk to work;walks to work
@At the airport
board the plane | to get on the plane | You can board the plane at half past nine.
destination | the place you travel to | Our destination is Istanbul.
boarding pass | a card or paper you show to get on the plane | Can I see your boarding pass, please?
gate number | the number of the door where you get on the plane | The gate number is on your boarding pass.
book your ticket online | to buy your ticket on the internet | You can book your ticket online. It's cheap.
go through immigration | to show your passport to officers in a new country | You go through immigration after the flight.
check-in desk | the place where you give your luggage and get a boarding pass | The check-in desk is in Terminal 2.
go through security | to have your bags checked before the flight | We go through security before the gate.
luggage | your bags and suitcases | You can't take a lot of luggage on small planes.
screens | TV-like boards with flight information | Look at the screens for your gate number.
@Other words
several times a week | three, four or five times every week | I go to the gym several times a week. | | freq
smoke | to have a cigarette | You can't smoke on the plane.
once a week | one time every week | We visit my grandmother once a week. | | freq
twice a week | two times every week | Hadi plays football twice a week. | | freq
terminal | a big building at an airport | Our flight leaves from Terminal 1.
public transport | buses, trains and service taxis for everyone | Public transport in Damascus is cheap.
"""

ODD = """
bus, train, bicycle, *luggage | Luggage: not transport.
get on, get off, take a bus, *boarding pass | Boarding pass: not an action.
check-in desk, gate, terminal, *street market | Street market: not at the airport.
once a week, twice a week, several times a week, *destination | Destination: a place.
can, can't, cannot, *does | Does: not can.
a, an, the, *some time | Some time: not an article.
"""

GRAMMAR = [
    dict(
        id="g1",
        title="can / can't",
        visual=dict(type="compare", cols=[
            dict(title="ability", color="teal", items=["I {can} drive.", "She {can't} swim."]),
            dict(title="possible / OK", color="purple", items=["You {can} book your ticket online.", "You {can't} smoke on the plane."]),
        ], cap="can + verb (no to, no s)"),
        pattern=[
            ["+", "I / you / he / she / we / they", ["can", "v"], "ride a bicycle."],
            ["−", "You", ["can't", "n"], "smoke here."],
            ["?", ["Can", "v"], "I", "take this bag on the plane? — Yes, you can."],
        ],
        examples=[
            "Joud {can} ride a bicycle, but she {can't} swim.",
            "You {can} book your ticket online.",
            "You {can't} take water through security.",
            "{Can} you drive a car? — No, {I can't}.",
        ],
        ar=[
            "can يعني 'بقدر / بعرف'، وكمان 'مسموح': You can sit here.",
            "can't يعني 'ما بقدر' أو 'ممنوع': You can't smoke here.",
            "بعد can الفعل بلا to وبلا s: She can drive.",
        ],
        watch=[("She cans drive.", "She can drive."), ("I can to swim.", "I can swim."), ("Do you can ride a scooter?", "Can you ride a scooter?")],
        quick="""
## choose: Choose the answer.
You ___ smoke on the plane. | can't | doesn't | aren't #id=a21u5-ae8d5c1
Joud can ___ a bicycle. | ride | rides | to ride
___ you drive a car? | Can | Does | Are #id=a21u5-fab0975
""",
        sets="""
## choose: Choose the answer.
You ___ book your ticket online. It's easy. | can | can to | cans
Passengers ___ smoke on the plane. | can't | don't can | not can
___ I take this bag on the plane? | Can | Does | Am #id=a21u5-ebe22a1
My grandmother can't ___ a car. | drive | drives | to drive
Can you ride a scooter? — No, I ___. | can't | don't | not
You can ___ the plane at 9:30. | board | boards | to board
Hadi ___ fix phones very well. | can | cans | can to
Can she swim? — Yes, she ___. | can | does | swims
We ___ take a bus. The station is near. | can | can to | cans
You ___ take water through security. | can't | doesn't | aren't #id=a21u5-5f27dda
## gap: Write can or can't.
You [can] book your ticket online.
You [can't|cannot|can not] smoke at the airport.
Babies [can't|cannot|can not] drive.
You [can] get a service taxi in Marjeh Square.
We [can't|cannot|can not] board the plane yet. It's too early.
I [can] ride a bicycle, and I'm good at it.
Passengers [can't|cannot|can not] take big knives on the plane.
You [can] see your gate number on the screens.
## short: Answer the question.
Can you drive? (✓) => Yes, I can.
Can I smoke here? (✗) => No, you can't. | No, you cannot.
Can Joud ride a bicycle? (✓) => Yes, she can.
Can we board the plane now? (✗) => No, you can't. | No, we can't. | No, you cannot.
Can they speak Turkish? (✓) => Yes, they can.
Can I take this bottle through security? (✗) => No, you can't. | No, you cannot.
Can you book tickets online? (✓) => Yes, you can. | Yes, I can.
Can Abu Salim fly a plane? (✗) => No, he can't. | No, he cannot.
## transform: Make a question (?).
You can drive. (?) => Can you drive?
She can ride a scooter. (?) => Can she ride a scooter?
We can book online. (?) => Can we book online?
They can swim. (?) => Can they swim?
I can take this bag on the plane. (?) => Can I take this bag on the plane?
He can fly a plane. (?) => Can he fly a plane?
You can see the screens. (?) => Can you see the screens?
Passengers can smoke here. (?) => Can passengers smoke here?
## fix: Find and fix the mistake.
She [cans>can] drive a car.
I can [to ride>ride] a scooter.
[Do you can>Can you] swim?
He can [speaks>speak] French.
You [don't can>can't|cannot] smoke here.
Can I [took>take] this bag?
Can you drive? — Yes, I [do>can].
We [not can>can't|cannot] board yet.
## order: Put the words in order.
You can book your ticket online.
You can't smoke on the plane.
Can you ride a bicycle?
I can't drive a car.
Can I see your boarding pass?
She can speak three languages.
We can take a bus to the airport.
Can we board the plane now?
""",
    ),
    dict(
        id="g2",
        title="a / an, the, no article",
        visual=dict(type="compare", cols=[
            dict(title="a / an = one, not known", color="teal", items=["There's {a} bus stop near here.", "I've got {an} idea."]),
            dict(title="the = we know which", color="purple", items=["{The} bus stop is opposite the bank.", "{The} sun, {the} airport"]),
            dict(title="no article = in general", color="amber", items=["I love {—} trains.", "by bus, at work, go home"]),
        ], cap="First time: a / an. Second time: the."),
        pattern=[
            ["", "There's", ["a", "x"], "café near the station."],
            ["", "", ["The", "v"], "café is very good."],
            ["", "I go to work by", ["— bus", "n"], "(no article)"],
        ],
        examples=[
            "I've got {a} new bicycle. {The} bicycle is red.",
            "{The} airport is twenty kilometres from the city.",
            "I usually go to work by {bus}. (no article)",
            "{—} Public transport in Damascus is cheap.",
        ],
        ar=[
            "a / an لشي واحد لأول مرة منحكي عنو: I've got a car.",
            "the لشي معروف أو حكينا عنو قبل: The car is red. وكمان the airport, the sun.",
            "ما منحط شي بالعموميات وبـ by bus, at home, go to work: I love trains.",
        ],
        watch=[("I go to work by the bus.", "I go to work by bus."), ("I love the trains. (all trains)", "I love trains."), ("Where's airport?", "Where's the airport?")],
        quick="""
## choose: Choose the answer.
I've got ___ new scooter. | a | the | an
I go to work by ___ bus. | — (nothing) | the | a
Where's ___ airport? | the | a | an
""",
        sets="""
## choose: Choose the answer.
There's ___ bus stop near my flat. | a | the | an
___ bus stop is opposite the bank. | The | A | An
I go to university by ___ bicycle. | — (nothing) | the | a
Is there ___ underground train in Damascus? | an | the | a
___ airport in Damascus is south-east of the city. | The | A | An #id=a21u5-2efdef6
I love ___ trains. They're fun. | — (nothing) | the | a
Can you see ___ screens over there? | the | a | an
I've got ___ idea! Let's take a taxi. | an | a | the
We walk to ___ work. | — (nothing) | the | a
My keys are at ___ home. | — (nothing) | the | a
## gap: Write a, an, the or x (= nothing).
I've got [a] new bicycle.
[The] bicycle is red and white.
I go to work by [x|nothing] bus.
Can I see your passport? It's in [the] bag.
She's [an] engineer at the airport.
I love [x|nothing] travelling.
[The] check-in desk is over there.
There's [a] café in Terminal 2.
## fix: Find and fix the mistake.
I go to work by [the bus>bus].
Where's [airport>the airport]?
I've got [the>a] new car. The car is blue.
She's [engineer>an engineer].
I love [the trains>trains]. (all trains)
[A>The] gate number is on your boarding pass.
We go to [the work>work] by scooter.
There's [a>an] underground train in Paris. #id=a21u5-090cc31
## sort: a / an, the or no article? | a / an | the | no article
a / an: new scooter, idea, bus stop near here
the: airport, sun, screens over there
no article: by bus, at home, public transport (in general)
## order: Put the words in order.
I go to work by bus.
The airport is near the city.
There's a café in the terminal.
I've got an old bicycle.
The check-in desk is over there.
We love travelling.
Is there an underground train in Cairo?
The boarding pass is in my bag.
""",
    ),
    dict(
        id="g3",
        title="Transport and travel",
        visual=dict(type="chips", groups=[
            dict(title="by + transport (no article)", color="teal", items=["by bus", "by train", "by plane", "by car", "by bicycle", "but: on foot"]),
            dict(title="verbs", color="purple", items=["take a bus", "get on / get off", "ride a scooter", "drive a car", "fly", "walk to work"]),
            dict(title="at the airport", color="amber", items=["check-in desk", "security", "immigration", "gate", "board the plane"]),
        ]),
        pattern=[
            ["", "I go to work", ["by bus.", "v"], ""],
            ["", "I", ["get on", "x"], "the bus at the university."],
            ["", "I", ["get off", "x"], "at Marjeh Square."],
            ["", "First: check-in desk →", "security →", "immigration → gate → board the plane"],
        ],
        examples=[
            "I usually {take a bus} to work, but I sometimes {walk}.",
            "{Get off} the bus at the Hejaz Railway Station.",
            "At the airport, we go to the {check-in desk} first.",
            "Then we {go through security} and wait at the {gate}.",
        ],
        ar=[
            "منقول by bus، by car بلا a أو the، بس on foot (مشي).",
            "get on = نطلع ع الباص، get off = ننزل من الباص.",
            "بالمطار: check-in desk ← security ← immigration ← gate.",
        ],
        watch=[("I go to work with the bus.", "I go to work by bus."), ("I go by foot.", "I go on foot."), ("I go down from the bus.", "I get off the bus.")],
        quick="""
## choose: Choose the answer.
I go to university ___ bus. | by | with | on
I walk. I go ___ foot. | on | by | with
I ___ the bus at Marjeh Square. | get off | go down | get up
""",
        sets="""
## choose: Choose the answer.
I go to work ___ car. | by | with | on
Maya walks. She goes ___ foot. | on | by | in
You ___ the bus at the front door. | get on | go in on | get up
___ the bus at the third stop. | Get off | Go down from | Get up
We ___ to Dubai once a year. | fly | ride | swim
My grandfather ___ a scooter. | rides | flies | swims
First you go to the ___ desk with your luggage. | check-in | boarding | gate
You show your passport at ___. | immigration | the screens | the luggage
Your gate number is on your ___. | boarding pass | luggage | terminal
Look at the ___ for flight information. | screens | gates | luggage
## match: Match.
check-in desk = you give your luggage here
security = they check your bags
immigration = they check your passport
gate = you wait here to board the plane
screens = flight information
boarding pass = you show it to get on the plane
terminal = a big building at the airport
destination = the place you travel to
## bank: Use the words.
I [take|get] a bus to work every morning.
I [get] off at Marjeh Square.
My brother [rides] a scooter.
We [fly] to Istanbul twice a year.
You can [book] your ticket online.
[Wait] for the bus at the bus stop.
Rana [walks] to work. Her school is near.
You can [board] the plane at gate 7.
## order: Put the words in order.
I go to university by bus.
Get off the bus at the station.
We go through security first.
You can board the plane now.
My gate number is twelve.
I walk to work on Mondays. #id=a21u5-4b0710a
Can you ride a scooter?
Public transport is very cheap here.
""",
    ),
]

CLASSROOM = dict(
    phrases=["Sorry, I didn't hear you.", "How do you pronounce this word?", "Can you give me an example?", "What does … mean?",
             "Can I ask a question?", "Work in groups.", "Change partners."],
    order="""
S: Excuse me, how do you pronounce this word: 'q-u-e-u-e'?
T: 'Queue' — like the letter Q.
S: Sorry, I didn't hear you.
T: 'Queue'. What does it mean? People in a line.
S: Can you give me an example?
T: There's a long queue at the check-in desk.
""",
)

READING = dict(
    title="How do you get to work?",
    text="""Public transport in Damascus is cheap, but it can be busy. How do people get to work?

Jad is a delivery driver. He rides a scooter, so he doesn't wait for buses. "I can go everywhere fast — I know all the shortcuts!" he says.

Rana is a teacher. She walks to work because her school is near her flat in Mezzeh. "It takes ten minutes. I love walking in the morning," she says.

Abu Salim drives a service taxi from Marjeh Square to Jaramana. He works six days a week. "People get on and get off all day. I talk to a hundred people every day!"

Fadi drives for a taxi app. His car is very old, but he calls it "my Ferrari"!""",
    qs="""
## tf: True or false?
Public transport in Damascus is expensive. | F @ Public transport in Damascus is cheap
Jad waits for buses. | F @ he doesn't wait for buses
Rana's school is near her flat. | T @ her school is near her flat in Mezzeh
Abu Salim works six days a week. | T @ He works six days a week
Rana takes a bus to work. | F @ She walks to work
## choose: Choose the answer.
How does Jad travel? | He rides a scooter. | He walks. | He takes a bus. @ He rides a scooter
How long is Rana's walk to work? | ten minutes | an hour | twenty minutes @ It takes ten minutes
## gap: Write one word.
Abu Salim drives a service [taxi]. @ Abu Salim drives a service taxi
""",
)

DIALOGUE = dict(
    title="At the check-in desk",
    intro="Damascus airport. Ghada has a flight to Doha.",
    task="gaps",
    lines="""
Assistant: Good morning. Can I [see] your passport, please?
Ghada: Yes, here you are.
Assistant: Thank you. What's your [destination]?
Ghada: Doha. Can I take this small bag [on] the plane?
Assistant: Yes, you [can]. But you can't take water through security.
Ghada: OK. What's the [gate] number?
Assistant: It's 4. It's on your boarding [pass]. You can board at half past ten.
Ghada: Thank you very [much].
""",
)

WQ = """
Yes, I can. (you / drive a car) => Can you drive a car? | Can you drive?
No, you can't. (I / smoke here) => Can I smoke here?
By bus. (How / you / go to work) => How do you go to work? | How do you get to work?
It's on your boarding pass. (Where / the gate number) => Where's the gate number? | Where is the gate number?
Twice a week. (How often / you / fly) => How often do you fly?
Istanbul. (What / your destination) => What's your destination? | What is your destination?
Yes, she can. She's very good. (Joud / ride a bicycle) => Can Joud ride a bicycle?
At Marjeh Square. (Where / you / get off) => Where do you get off?
"""

WRITING = [
    dict(task="Write about how you travel: to work or university, in your town, and on holiday. What can you do? What can't you do?",
         tip="Use by bus / on foot, get on / get off, and can / can't. Write 60–90 words.",
         model="I usually go to university by bus. I get on the bus near my flat in Dummar and I get off at Baramkeh. It takes twenty-five minutes. Sometimes I walk — I like walking in the fresh air. I can ride a bicycle, but I can't drive a car. On holiday, my family and I usually take a bus to Latakia. We fly once every two or three years.",
         check=["by bus / by car / on foot", "get on / get off", "can / can't + verb", "frequency: usually, sometimes, once a week"],
         min=60, max=90),
]

CANDO = [
    "use can and can't for ability and rules.",
    "use a, an, the and no article.",
    "talk about transport: by bus, on foot, get on, get off.",
    "understand words at the airport.",
    "say how often I travel: once a week, twice a week.",
]
