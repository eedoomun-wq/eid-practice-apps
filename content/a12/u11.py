META = dict(n=11, title="Travel", pages="80–87")

BOOK = """
go by bus/train/plane, go on a journey, buy a single (ticket), buy a return (ticket), buy a travel card, be late, be early,
be on time,
in August / in 2013, a year / two months / three weeks ago, last week / month / year,
yesterday (morning/afternoon/evening), first, then, after that, in the end,
eat out, go sightseeing, go walking, go shopping, go on a boat trip, visit museums, go skiing, go to the beach,
dangerous, tunnel, flight, airport, passenger, raise money (for charity), to cross / to go across,
a bike ride / to ride a bike
"""

WORDS = """
@Transport and travel
go by bus/train/plane | to travel on a bus, a train or a plane | We went to Aleppo by train. | go by bus;went by bus;go by train;went to Aleppo by train;go by plane;went by plane
go on a journey | to travel a long way | My grandfather went on a journey to Mecca by bus.
buy a single (ticket) | a ticket to go there, not back | I bought a single ticket to Homs. | buy a single;bought a single
buy a return (ticket) | a ticket to go there and come back | Did you buy a return ticket? | buy a return;bought a return
buy a travel card | a card for a lot of trips on buses or trains | In London, Kenji bought a travel card for the Tube. | buy a travel card;bought a travel card
be late | to arrive after the right time | Hadi was late for his flight! | be late;was late
be early | to arrive before the right time | Rana was early for the meeting. | be early;was early
be on time | to arrive at the right time | Was the train on time? | be on time;was the train on time
@Time expressions
in August / in 2013 | in + month / in + year | We went to Tartus in August. | in August;in 2013
a year / two months / three weeks ago | before now: a year before today… | I visited Istanbul two months ago. | a year ago;two months ago;three weeks ago
last week / month / year | the week / month / year before this one | Did you go out last week? | last week;last month;last year
yesterday (morning/afternoon/evening) | the morning / afternoon / evening of yesterday | I saw Maya yesterday afternoon. | yesterday morning;yesterday afternoon;yesterday evening
first, then, after that, in the end | words for the order of a story | First we had breakfast. Then we went to the souq. | first;then;after that;in the end
@Holiday activities
eat out | to have a meal in a restaurant | We ate out in Qassaa on Friday. | eat out;ate out
go sightseeing | to visit famous places as a tourist | They went sightseeing in Rome. | go sightseeing;went sightseeing
go walking | to walk in the country for fun | We went walking in the hills near Bloudan. | go walking;went walking
go shopping | to go to shops to buy things | Did you go shopping in Souq al-Hamidiyah? | go shopping;went shopping
go on a boat trip | to travel on a boat for fun | We went on a boat trip to Arwad. | go on a boat trip;went on a boat trip
visit museums | to go to see museums | We visited museums in Paris. | visit museums;visited museums
go skiing | to move on snow with skis | Did they go skiing in Lebanon? | go skiing;went skiing
go to the beach | to go to the sandy place next to the sea | We went to the beach every day in Latakia. | go to the beach;went to the beach
@Other words
dangerous | it can hurt you | The mountain road was dangerous at night.
tunnel | a road under the ground or through a mountain | The train went through a long tunnel.
flight | a journey by plane | Our flight to Dubai was three hours.
airport | a place where planes arrive and leave | We arrived at the airport early.
passenger | a person who travels in a car, bus, train or plane | There were two hundred passengers on the plane.
raise money (for charity) | to get money from people to help others | Jad and his friends raised money for a children's hospital. | raise money;raised money
to cross / to go across | to go from one side to the other | We crossed the street. / We went across the bridge. | cross;crossed;go across;went across
a bike ride / to ride a bike | a trip on a bike / to go on a bike | We went on a bike ride in Tishreen Park. | bike ride;ride a bike;rode their bikes
"""

ODD = """
bus, train, plane, *tunnel | Tunnel: not transport.
last week, two days ago, yesterday, *tomorrow | Tomorrow: not the past.
go skiing, go walking, go shopping, *be late | Be late: not a holiday activity.
first, then, after that, *ago | Ago: not a story word.
airport, flight, passenger, *museum | Museum: not about planes.
Did, Was, Were, *Do | Do: present.
went, saw, bought, *go | Go: not past.
"""

GRAMMAR = [
    dict(
        id="g1",
        title="Past simple: Yes / No questions",
        visual=dict(type="timeline", now="now", marks=[dict(at=-3, label="last year", text="Did you go?"), dict(at=-1, label="yesterday", text="Yes, I did.")],
                    cap="Did + person + verb? — Yes, I did. / No, I didn't."),
        pattern=[
            ["?", ["Did", "v"], ["you", "s"], "go to Latakia?"],
            ["", "Yes, I", ["did.", "v"], ""],
            ["", "No, I", ["didn't.", "n"], ""],
            ["", "(Did + go, not Did + went)", "", ""],
        ],
        examples=[
            "{Did} you {have} a good holiday? — Yes, {I did}.",
            "{Did} the train {arrive} on time? — No, {it didn't}. It was late.",
            "{Did} Jad {ride} his bike to Latakia? — Yes, {he did}!",
            "{Were} you tired? — Yes, I {was}. (be: no did!)",
        ],
        ar=[
            "لنسأل بالماضي منحط Did بالأول، والفعل بيرجع لأصله: Did you go?",
            "الجواب: Yes, I did. / No, I didn't.",
            "انتبه: مع was / were ما منستعمل did: Were you tired? مو Did you tired?",
        ],
        watch=[("Did you went to Aleppo?", "Did you go to Aleppo?"), ("You went to Aleppo?", "Did you go to Aleppo?"), ("Did you tired?", "Were you tired?")],
        quick="""
## choose: Choose the answer.
___ you go out last night? | Did | Were | Do
Did she ___ the museum? | visit | visited | visits
Did they like the hotel? — Yes, they ___. | did | were | liked
""",
        sets="""
## choose: Choose the answer.
___ you have a good holiday? | Did | Were | Do
Did they ___ by train? | go | went | goes
Did Hadi arrive on time? — No, he ___. | didn't | wasn't | doesn't
___ the flight late? | Was | Did | Were
Did you ___ a return ticket? | buy | bought | buys
Did she enjoy the trip? — Yes, she ___. | did | was | enjoyed
___ you tired after the journey? | Were | Did | Do
Did they go skiing? — No, they ___. | didn't | weren't | don't
Did you ___ out last night? | eat | ate | eats
___ Jad ride his bike to Latakia? | Did | Was | Were #id=a12u11-8fe60a3
## short: Answer the question.
Did you go to the beach? (✓) => Yes, I did.
Did they visit museums? (✗) => No, they didn't. | No, they did not.
Did Hadi miss his flight? (✓) => Yes, he did.
Did the train arrive on time? (✗) => No, it didn't. | No, it did not.
Did you eat out in London? (✓) => Yes, I did.
Did she buy a travel card? (✗) => No, she didn't. | No, she did not.
Did they go sightseeing? (✓) => Yes, they did.
Did you go skiing? (✗) => No, I didn't. | No, I did not.
## transform: Make a question (?).
You went to Cairo. (?) => Did you go to Cairo?
She bought a single ticket. (?) => Did she buy a single ticket?
They went on a boat trip. (?) => Did they go on a boat trip?
He crossed the bridge. (?) => Did he cross the bridge?
You visited the Azem Palace. (?) => Did you visit the Azem Palace?
The plane arrived early. (?) => Did the plane arrive early?
They raised a lot of money. (?) => Did they raise a lot of money?
Maya went walking. (?) => Did Maya go walking?
## fix: Find and fix the mistake.
Did you [went>go] to the beach?
[You visited>Did you visit] the museum?
Did she [bought>buy] a ticket?
[Did>Were] you tired?
Did they go skiing? — Yes, they [went>did].
[Do>Did] you go out yesterday?
Did the train [arrived>arrive] on time?
[Did>Was] the flight late?
## order: Put the words in order.
Did you have a good holiday?
Did they go by train?
Did she buy a return ticket?
Did you go sightseeing?
Was the flight on time?
Did he ride his bike to Beirut?
Did they eat out last night?
Were you late for the flight?
""",
    ),
    dict(
        id="g2",
        title="Past simple: Wh- questions",
        visual=dict(type="table", head=["question word", "did", "person", "verb"],
                    rows=[["Where", "did", "you", "go?"], ["When", "did", "she", "arrive?"], ["How", "did", "they", "travel?"],
                          ["What", "did", "you", "do?"], ["Who", "did", "you", "meet?"]],
                    colors=["amber", "purple", "teal", "white"], cap="Question word + did + person + verb?"),
        pattern=[
            ["?", ["Where", "x"], ["did", "v"], "you go on holiday?"],
            ["?", ["How", "x"], ["did", "v"], "they travel? — By train."],
            ["?", ["What", "x"], ["did", "v"], "you do there?"],
            ["?", ["When", "x"], ["did", "v"], "you come back? — Last Friday."],
        ],
        examples=[
            "{Where did} you go last summer? — To Amman.",
            "{How did} you travel? — We went by bus.",
            "{What did} you do there? — We visited the old city and the Roman theatre.",
            "{When did} you get back? — Three days ago.",
        ],
        ar=[
            "بالماضي: كلمة السؤال + did + الشخص + الفعل بأصلو: Where did you go?",
            "ago بتجي بعد المدة: two days ago = من يومين.",
            "last week / last year بلا the: last week، مو the last week.",
        ],
        watch=[("Where you went?", "Where did you go?"), ("What did you did?", "What did you do?"), ("I went there before two days.", "I went there two days ago.")],
        quick="""
## choose: Choose the answer.
Where ___ you go last summer? | did | were | do
How did you ___? — By plane. | travel | travelled | travels
I went to Aleppo two weeks ___. | ago | before | last
""",
        sets="""
## choose: Choose the answer.
Where ___ you go on holiday? | did | were | do
What did you ___ in Paris? | do | did | does
How ___ they travel? — By train. | did | were | do
When did she ___ back? — On Friday. | come | came | comes
Who did you ___ at the airport? | meet | met | meets
What time ___ the flight leave? | did | was | were
Where did you ___? — At a small hotel. | stay | stayed | stays
We went to Vienna three days ___. | ago | before | last
I saw Hadi ___ week. | last | ago | before
How long ___ the journey? — Four hours. | was | did | were
## bank: Use the words.
[Where] did you go? — To Beirut.
[When] did you go? — Last August.
[How] did you travel? — By bus.
[Who] did you go with? — My family.
[What] did you do? — We went on a boat trip.
[Where] did you stay? — In a small hotel.
[What time|When] did you get back? — At midnight.
[How long] was the journey? — Three hours.
## transform: Write the question.
We went to Rome. (Where / you) => Where did you go?
She arrived at nine. (What time / she) => What time did she arrive? | When did she arrive?
They travelled by plane. (How / they) => How did they travel?
I met Hala at the café. (Who / you) => Who did you meet?
He bought a scarf. (What / he) => What did he buy?
We got back last Friday. (When / you) => When did you get back?
Rana stayed at a hotel. (Where / Rana) => Where did Rana stay?
They ate sushi in Tokyo. (What / they) => What did they eat?
## match: Match the question and the answer.
Where did you go? = To Paris.
How did you travel? = By train.
When did you get back? = Two days ago.
Who did you go with? = With my brother.
What did you see? = The Eiffel Tower and the river.
Where did you stay? = At my aunt's house.
What did you eat? = Croissants — fantastic!
How was the journey? = Long, but nice.
## fix: Find and fix the mistake.
Where [you went>did you go]?
What did you [did>do] yesterday?
How did they [travelled>travel]?
I went there two weeks [before>ago].
We arrived [the last week>last week].
When [you did>did you] come back?
Who [you met>did you meet]?
What [did>was] the weather like?
## order: Put the words in order.
Where did you go last summer?
How did you travel?
What did you do there?
When did you get back?
Who did you meet?
Where did you stay?
What did you eat?
How long was the flight?
""",
    ),
]

CLASSROOM = dict(
    phrases=["What did we do yesterday?", "I was absent last lesson.", "Can you write it on the board, please?", "Let's start.",
             "Good luck!", "What's the homework?"],
    order="""
S: Sorry, I was absent last lesson.
T: OK, no problem.
S: What did we do yesterday?
T: Past simple questions: 'Did you go…?'
S: Can you write it on the board, please?
T: Of course. And the homework is page 84.
""",
)

READING = dict(
    title="A bike ride for charity",
    text="""Last April, Jad and four friends went on a bike ride from Damascus to Latakia. Why? To raise money for a children's hospital.

First, they rode to Homs. The road was long and flat, and they arrived in the evening. After that, they crossed the mountains. "That day was hard and a bit dangerous," says Jad. "We went through a long tunnel, and there were a lot of lorries."

Then, on the fourth day, they saw the sea! In the end, they arrived in Latakia on the eighth of April. They raised five million Syrian pounds. Did they go back by bike? No, they didn't — they went back by bus!""",
    qs="""
## tf: True or false?
Jad went on the bike ride alone. | F @ Jad and four friends went on a bike ride
They raised money for a hospital. | T @ To raise money for a children's hospital
The day in the mountains was easy. | F @ That day was hard and a bit dangerous
They went through a tunnel. | T @ We went through a long tunnel
They went back to Damascus by bike. | F @ they went back by bus
## choose: Choose the answer.
When did they arrive in Latakia? | on the eighth of April | on the fourth of April | in August @ they arrived in Latakia on the eighth of April
Where did they go first? | to Homs | to Latakia | to Aleppo @ First, they rode to Homs
## gap: Write one word.
They saw the sea on the fourth [day]. @ on the fourth day, they saw the sea
""",
)

DIALOGUE = dict(
    title="Did you have a good trip?",
    intro="Monday. Rana asks Hala about her trip to Istanbul.",
    task="gaps",
    lines="""
Rana: Hi, Hala! [Did] you have a good trip?
Hala: Yes, I did, thanks! It was fantastic.
Rana: How did you [travel]?
Hala: By plane. The flight was only two hours, and it was on [time].
Rana: What did you [do] there?
Hala: I went sightseeing, and we went on a boat [trip] on the Bosphorus.
Rana: Did you [eat] simit?
Hala: Yes, every morning! We came back two days [ago].
""",
)

WQ = """
To Doha. (Where / you / go) => Where did you go?
By train. (How / they / travel) => How did they travel?
Yes, I did. It was fantastic. (you / have a good holiday) => Did you have a good holiday?
Last Friday. (When / she / come back) => When did she come back?
No, he didn't. He was late. (Hadi / arrive on time) => Did Hadi arrive on time?
Kebab halabi. (What / you / eat) => What did you eat?
At a small hotel. (Where / you / stay) => Where did you stay?
Three hours. (How long / the flight) => How long was the flight?
"""

WRITING = [
    dict(task="Write about a trip you went on: where, when, how you travelled, what you did, and how it was.",
         tip="Use first, then, after that, in the end, and the past simple. Write 60–90 words.",
         model="Two years ago, I went to Aleppo with my sister. We went by train, and the journey was four hours. First, we visited the Citadel. Then we went shopping in the old souq. After that, we ate kebab halabi in a small restaurant. We didn't go to the museum — it was closed. In the end, we came back on Sunday. It was a fantastic trip!",
         check=["when: last year, two years ago, in August", "first / then / after that / in the end", "past simple: went, visited, ate", "didn't + verb"],
         min=60, max=90),
    dict(task="Write five questions to ask a friend about their last holiday.",
         tip="Use Did you…? and Where / When / How / What did you…?",
         model="Where did you go?\nHow did you travel?\nWhat did you do there?\nDid you eat out?\nWhen did you come back?",
         check=["Did + person + verb?", "question word + did + person + verb?", "the verb without -ed after did"],
         min=20, max=60),
]

CANDO = [
    "ask 'Did you…?' and answer 'Yes, I did.' / 'No, I didn't.'",
    "ask Wh- questions in the past: Where did you go?",
    "use ago and last: two days ago, last week.",
    "talk about transport and tickets.",
    "tell a story with first, then, after that, in the end.",
]
