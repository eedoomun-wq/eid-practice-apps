META = dict(n=12, title="Good times", pages="106–113")

BOOK = """
birthday party, leaving party, coming-of-age party, make a cake, decorate the house, make traditional food,
national holiday, decorate the table, dress up in party clothes, religious holiday, take part in a competition,
dress up in traditional costumes, take part in a parade, graduation party, wedding party, hire a band,
hire an entertainer,
snowing, autumn, dry season, sunny, cloudy, warm, wet, cold, windy, cool, foggy, spring, summer, hot, wet season, icy,
winter, raining,
live on stage, accommodation, arts and crafts workshops, local specialities, campsite
"""

WORDS = """
@Celebrations
birthday party | a party on your birthday | Joud's birthday party is on Saturday. | | party
leaving party | a party when someone leaves a job or a town | We're having a leaving party for Bassel. | | party
coming-of-age party | a party when a young person becomes an adult | In some countries, a coming-of-age party is at eighteen. | | party
make a cake | to bake a cake | I'm going to make a cake for Mum.
decorate the house | to make the house beautiful for a celebration | We decorate the house with lights for Eid.
make traditional food | to cook the special dishes of your culture | My grandmother makes traditional food for Eid: ma'amoul!
national holiday | a day off for the whole country | The first of January is a national holiday.
decorate the table | to make the table beautiful with flowers or candles | Let's decorate the table with jasmine.
dress up in party clothes | to wear your best clothes for a party | Everyone dresses up in party clothes for the wedding.
religious holiday | a holiday for a religion, like Eid or Christmas | Eid al-Fitr is a religious holiday.
take part in a competition | to be one of the people in a competition | Walid is going to take part in a competition.
dress up in traditional costumes | to wear the old clothes of your culture | At the festival, people dress up in traditional costumes.
take part in a parade | to walk with music in a street celebration | Children take part in a parade in Bab Touma.
graduation party | a party when you finish university | Layla's graduation party will be in 2028!
wedding party | a party after a wedding | The wedding party was in a big hall in Mezzeh.
hire a band | to pay musicians to play | We're going to hire a band for the wedding.
hire an entertainer | to pay a person to entertain children | They hired an entertainer for Joud's party.
@Weather and seasons
snowing | snow is falling | It's snowing in Bloudan! | | precip
autumn | the season after summer | In autumn the leaves fall. | | season
dry season | the time of year with no rain | In some countries, the dry season is very long. | | season2
sunny | with a lot of sun | It's sunny today. | | weather
cloudy | with a lot of clouds | It's cloudy, but it isn't raining. | | weather
warm | a bit hot, nice | Spring in Damascus is warm. | | temp
wet | with a lot of rain | It's wet today — take an umbrella. | | weather
cold | not warm | It's very cold in January. | | temp
windy | with a lot of wind | It's windy on the corniche. | | weather
cool | a bit cold, nice | The evenings in Bloudan are cool in summer. | | temp
foggy | with fog; you can't see far | It was foggy on the motorway this morning. | | weather
spring | the season after winter | Spring is the best season in Damascus. | | season
summer | the hottest season | We go to the beach in summer. | | season
hot | very warm | It's really hot in July. | | temp
wet season | the time of year with a lot of rain | The wet season in India is from June to September. | | season2
icy | with ice; very cold and dangerous | The roads are icy in Bloudan. | | weather
winter | the coldest season | It snows on Qasioun in winter — sometimes! | | season
raining | rain is falling | It's raining. Take an umbrella! | | precip
@Other words
live on stage | performing in front of people, not recorded | The band is going to play live on stage.
accommodation | a place to stay: a hotel, a flat… | The festival has cheap accommodation.
arts and crafts workshops | classes where you make things with your hands | There are arts and crafts workshops for children.
local specialities | special food from one place | Try the local specialities: kebab halabi in Aleppo!
campsite | a place where you can stay in a tent | We're going to stay at a campsite near Kasab.
"""

ODD = """
spring, summer, winter, *sunny | Sunny: weather, not a season.
sunny, cloudy, windy, *autumn | Autumn: a season.
birthday party, wedding party, leaving party, *campsite | Campsite: a place to stay.
hire a band, make a cake, decorate the house, *icy | Icy: weather.
going to, would like to, want to, *went | Went: past.
hot, warm, cool, *raining | Raining: not a temperature word.
"""

GRAMMAR = [
    dict(
        id="g1",
        title="going to: plans",
        visual=dict(type="timeline", now="now: the plan is ready", span={"from": 0, "to": 3, "label": "future plans"},
                    marks=[dict(at=2, label="next Saturday", text="We're going to have a party.")]),
        pattern=[
            ["+", "I", ["'m going to", "v"], "make a cake."],
            ["+", "They", ["'re going to", "v"], "hire a band."],
            ["−", "She", ["isn't going to", "n"], "come."],
            ["?", ["Are", "v"], "you", "going to dress up? — Yes, I am."],
        ],
        examples=[
            "We{'re going to} have a leaving party for Bassel.",
            "Um Khaled {is going to} make traditional food.",
            "I{'m not going to} wear a suit. It's a casual party.",
            "What {are} you {going to} do for Eid?",
        ],
        ar=[
            "going to للخطط اللي قررناها قبل: We're going to hire a band (رح نجيب فرقة).",
            "الشكل: am / is / are + going to + الفعل.",
            "Look at the clouds! It's going to rain. — كمان لشي رح يصير وعم نشوف إشاراتو.",
        ],
        watch=[("I going to make a cake.", "I'm going to make a cake."), ("She's going make food.", "She's going to make food."), ("Are you going to came?", "Are you going to come?")],
        quick="""
## choose: Choose the answer.
We ___ going to have a party. | 're | 's | 'm
She's going ___ a cake. | to make | make | making
___ you going to dress up? | Are | Do | Will
""",
        sets="""
## choose: Choose the answer.
I'm ___ to decorate the house. | going | go | goes
They're going to ___ a band. | hire | hiring | hired
Um Khaled ___ going to make ma'amoul. | is | are | am
We ___ going to invite a lot of people. | aren't | isn't | don't
___ she going to take part in the parade? | Is | Are | Does
What are you going to ___ for Eid? | do | doing | did
Look at those clouds! It's going to ___. | rain | raining | rained
Are you going to dress up? — Yes, I ___. | am | do | going
Hadi ___ going to come. He's ill. | isn't | doesn't | aren't
Where ___ they going to stay? | are | do | is
## gap: Write am, is or are.
I [am|'m] going to make a cake.
My sister [is|'s] going to decorate the table.
We [are|'re] going to hire an entertainer.
[Are] you going to wear party clothes?
Bassel [is|'s] going to leave on Friday.
They [are|'re] going to take part in a competition.
[Is] it going to rain tomorrow?
I [am|'m] not going to dance. I'm shy!
## transform: Make the sentence negative (−).
I'm going to wear a dress. (−) => I'm not going to wear a dress. | I am not going to wear a dress.
They're going to hire a band. (−) => They aren't going to hire a band. | They're not going to hire a band. | They are not going to hire a band.
She's going to make a cake. (−) => She isn't going to make a cake. | She's not going to make a cake. | She is not going to make a cake.
We're going to stay at a campsite. (−) => We aren't going to stay at a campsite. | We're not going to stay at a campsite. | We are not going to stay at a campsite.
It's going to rain. (−) => It isn't going to rain. | It's not going to rain. | It is not going to rain.
He's going to dress up. (−) => He isn't going to dress up. | He's not going to dress up. | He is not going to dress up.
I'm going to make traditional food. (−) => I'm not going to make traditional food. | I am not going to make traditional food.
The children are going to take part in the parade. (−) => The children aren't going to take part in the parade. | The children are not going to take part in the parade.
## transform: Make a question (?).
You're going to have a party. (?) => Are you going to have a party?
She's going to make traditional food. (?) => Is she going to make traditional food?
They're going to hire an entertainer. (?) => Are they going to hire an entertainer?
It's going to snow. (?) => Is it going to snow?
He's going to take part in the parade. (?) => Is he going to take part in the parade?
We're going to decorate the house. (?) => Are we going to decorate the house?
Maya is going to sing live on stage. (?) => Is Maya going to sing live on stage?
You're going to dress up. (?) => Are you going to dress up?
## fix: Find and fix the mistake.
I [going to>'m going to|am going to] make a cake.
She's going [make>to make] ma'amoul.
Are you going to [came>come]?
They [is>are] going to hire a band.
We're going to [decorating>decorate] the house.
[Do>Are] you going to dress up?
He's not going to [comes>come].
It's going [rain>to rain].
## order: Put the words in order.
We're going to have a party.
She's going to make a cake.
Are you going to dress up?
They aren't going to hire a band.
What are you going to do for Eid?
It's going to rain.
I'm going to decorate the table.
Is he going to take part in the parade?
""",
    ),
    dict(
        id="g2",
        title="would like to / want to",
        visual=dict(type="compare", cols=[
            dict(title="want to (direct)", color="teal", items=["I want to go to the party.", "Do you want to come?"]),
            dict(title="would like to (polite)", color="purple", items=["I'd like to go to the party.", "Would you like to come?"]),
        ], cap="'d = would · would like + noun / would like to + verb"),
        pattern=[
            ["+", "I", ["'d like to", "v"], "go to the festival."],
            ["+", "She", ["wants to", "v"], "hire a band."],
            ["?", ["Would", "v"], "you like to", "come? — Yes, I'd love to!"],
            ["+", "I", ["'d like", "v"], "a coffee, please. (+ noun)"],
        ],
        examples=[
            "I{'d like to} visit the festival in Bosra.",
            "{Would you like to} come to my graduation party? — Yes, I'd love to!",
            "Joud {wants to} hire an entertainer for her party.",
            "I{'d like} a piece of cake, please.",
        ],
        ar=[
            "would like to يعني 'حابب' بطريقة مؤدبة: I'd like to come.",
            "Would you like to…? منستعملها للدعوة: Would you like to come? — Yes, I'd love to!",
            "انتبه: I'd like to go، مو I'd like go، ومو I like to go (هي بتعني بحب عادةً).",
        ],
        watch=[("I would like go.", "I'd like to go."), ("Would you like come?", "Would you like to come?"), ("Do you like to come to my party? (invitation)", "Would you like to come to my party?")],
        quick="""
## choose: Choose the answer.
I'd like ___ to the concert. | to go | go | going
___ you like to come? | Would | Do | Are
She ___ to hire a band. | wants | want | would
""",
        sets="""
## choose: Choose the answer.
I'd ___ to visit Tokyo. | like | likes | liking
Would you like ___ to my party? | to come | come | coming
She ___ to take part in the competition. | wants | want | would #id=a22u12-24aeee6
___ you like a cup of tea? | Would | Do | Are
Would you like to come? — Yes, I'd ___ to! | love | loved | loving
They ___ like to stay at a campsite. | 'd | 're | 's
I'd like ___ piece of ma'amoul, please. | a | to | the to
Do you want ___ the parade? | to see | see | seeing
What would you like ___? | to do | do | doing
He'd like ___ a band for the wedding. | to hire | hire | hiring
## gap: Write to or – (x).
I'd like [to] visit the festival.
Would you like [x|nothing] a coffee?
She wants [to] dress up.
I'd like [x|nothing] a piece of cake, please.
Do you want [to] come with us?
We'd like [to] hire an entertainer.
Would you like [x|nothing] some tea?
They want [to] see the parade.
## transform: Make it polite with would like.
I want a coffee. => I'd like a coffee. | I would like a coffee.
I want to sit here. => I'd like to sit here. | I would like to sit here.
Do you want to come? => Would you like to come?
We want to book a table. => We'd like to book a table. | We would like to book a table.
Do you want some cake? => Would you like some cake?
She wants to see the menu. => She'd like to see the menu. | She would like to see the menu.
I want the fish, please. => I'd like the fish, please. | I would like the fish, please.
Do they want to stay? => Would they like to stay?
## match: Match the invitation and the answer.
Would you like to come to my party? = Yes, I'd love to! Thank you.
Would you like some cake? = No, thank you. I'm full.
Would you like to dance? = Sorry, I'm a bit shy.
Do you want to see the parade? = Yes! What time does it start?
Would you like a cup of tea? = Yes, please. With sugar.
Would you like to stay for dinner? = I'd love to, but I can't.
What would you like to do on Eid? = I'd like to visit my grandparents.
Would you like to hire a band? = Yes — a band that plays traditional music.
## fix: Find and fix the mistake.
I'd like [go>to go] to the festival.
Would you like [come>to come]?
[Do you like>Would you like] to come to my party?
She [want>wants] to dress up.
I'd like [to a>a] coffee, please.
Would you like to come? — Yes, I'd love [it>to].
They'd like [visiting>to visit] Rome.
[Would>Do] you want to come?
## order: Put the words in order.
Would you like to come to my party?
I'd like to visit the festival.
She wants to take part in the competition.
Would you like a cup of tea?
I'd love to come!
What would you like to do?
We'd like to hire a band.
Do you want to see the parade?
""",
    ),
    dict(
        id="g3",
        title="Celebrations",
        visual=dict(type="chips", groups=[
            dict(title="parties", color="purple", items=["birthday party", "wedding party", "graduation party", "leaving party", "coming-of-age party"]),
            dict(title="getting ready", color="teal", items=["decorate the house", "decorate the table", "make a cake", "make traditional food", "hire a band", "hire an entertainer"]),
            dict(title="on the day", color="amber", items=["dress up in party clothes", "dress up in traditional costumes", "take part in a parade", "take part in a competition"]),
        ]),
        pattern=[
            ["", "We're going to", ["decorate the house", "v"], "with lights."],
            ["", "They", ["hired a band", "v"], "for the wedding."],
            ["", "Children", ["take part in a parade", "v"], "on Eid."],
        ],
        examples=[
            "For Eid, we {decorate the house} and {make traditional food} like ma'amoul.",
            "My cousins {dressed up in traditional costumes} for the festival.",
            "We're going to {hire an entertainer} for Joud's birthday party.",
            "Eid al-Fitr is a {religious holiday}; the first of January is a {national holiday}.",
        ],
        ar=[
            "كلمات الاحتفالات: decorate (نزيّن)، hire a band (نجيب فرقة)، dress up (نلبس أحلى شي).",
            "take part in = نشارك بـ: take part in a parade.",
            "religious holiday = عيد ديني، national holiday = عطلة وطنية.",
        ],
        watch=[("We will make a party.", "We're going to have a party."), ("I participated a competition.", "I took part in a competition."), ("rent a band", "hire a band")],
        quick="""
## choose: Choose the answer.
We're going to ___ a band. | hire | make | decorate
Let's ___ the table with flowers. | decorate | hire | take #id=a22u12-85bd1aa
Children ___ part in the parade. | take | make | do
""",
        sets="""
## choose: Choose the right verb.
We're going to ___ the house with lights. | decorate | hire | take
My grandmother is going to ___ traditional food. | make | take | hire
They're going to ___ an entertainer for the children. | hire | make | dress
Everyone is going to ___ up in party clothes. | dress | make | take
Walid is going to take ___ in a competition. | part | place | piece
Let's ___ a cake for Mum's birthday. | make | do | hire
The children are going to take part in a ___. | parade | cake | table
They ___ a band for the wedding last year. | hired | made | decorated
## match: Match the party and the reason.
birthday party = you're a year older
graduation party = you finish university
leaving party = someone leaves a job or a town
wedding party = two people get married
coming-of-age party = a young person becomes an adult
religious holiday = Eid or Christmas
national holiday = a day off for the whole country
festival = music, food and fun for a few days #id=a22u12-adfac46
## bank: Use the words.
We're going to [decorate] the table with jasmine.
My aunt is going to [make] ma'amoul for Eid.
They're going to [hire] a band.
Everyone is going to [dress] up in party clothes.
The children are going to take [part] in a parade.
Bassel is leaving, so we're having a [leaving] party.
Layla finishes university next year — then it's her [graduation] party!
Eid is a [religious] holiday.
## order: Put the words in order.
We're going to decorate the house.
They hired a band for the wedding.
My grandmother makes traditional food.
Children take part in a parade.
Are they going to dress up?
Let's hire an entertainer.
Eid is a religious holiday.
We're going to make a cake.
""",
    ),
    dict(
        id="g4",
        title="Weather and seasons",
        visual=dict(type="table", head=["season", "weather in Damascus (usually)"],
                    rows=[["spring", "warm and sunny"], ["summer", "hot and dry"], ["autumn", "cool and windy"], ["winter", "cold and wet, sometimes icy or snowing"]],
                    colors=["teal", "white"], cap="What's the weather like? — It's sunny. / It's raining."),
        pattern=[
            ["?", "What's the weather", ["like?", "v"], ""],
            ["", "It's", ["sunny / cloudy / windy.", "x"], "(adjective)"],
            ["", "It's", ["raining / snowing.", "v"], "(now: -ing)"],
        ],
        examples=[
            "What's the weather {like} today? — It's {sunny} and {warm}.",
            "Look! It's {snowing} in Bloudan!",
            "{Summer} in Damascus is {hot} and {dry}.",
            "It's {foggy} — drive slowly.",
        ],
        ar=[
            "لنسأل عن الطقس: What's the weather like? — It's sunny.",
            "sunny, cloudy, windy صفات، بس raining و snowing منستعملهن مع ing: It's raining.",
            "الفصول: spring (ربيع)، summer (صيف)، autumn (خريف)، winter (شتي).",
        ],
        watch=[("It's rain.", "It's raining."), ("The weather is sun.", "It's sunny."), ("How is the weather like?", "What's the weather like?")],
        quick="""
## choose: Choose the answer.
Take an umbrella. It's ___. | raining | rain | rainy day
What's the weather ___? | like | likes | how
It's very ___ today — 40°C! | hot | cool | icy
""",
        sets="""
## choose: Choose the right word.
There's a lot of sun. It's ___. | sunny | cloudy | foggy
There are a lot of clouds. It's ___. | cloudy | sunny | dry
You can't see far. It's ___. | foggy | sunny | warm
The trees are moving a lot. It's ___. | windy | foggy | warm
There's ice on the road. It's ___. | icy | sunny | warm
It's 35°C. It's ___. | hot | cold | cool
It's 15°C in the evening. It's ___. | cool | hot | icy
Take an umbrella. It's ___. | raining | sunny | dry
## sort: Season or weather? | season | weather
season: spring, summer, autumn, winter
weather: sunny, cloudy, windy, foggy, icy, warm
## gap: Write the word.
It's raining. Take an [umbrella].
In [winter], it sometimes snows in Bloudan.
After summer comes [autumn].
It's [snowing]! Let's make a snowman.
The [summer] in Damascus is hot and dry.
There's a lot of wind today. It's [windy].
In [spring], there are flowers everywhere.
You can't see the mountains. It's [foggy].
## fix: Find and fix the mistake.
It's [rain>raining] now.
The weather is [sun>sunny].
[How>What]'s the weather like?
It's very [wind>windy] on the corniche.
It [snow>snows] in Bloudan in winter. #id=a22u12-088d8c7
It's [snow>snowing] in Bloudan!
Today is very [cloud>cloudy].
It's [ice>icy] on the roads.
## order: Put the words in order.
What's the weather like today?
It's sunny and warm.
It's raining in London.
Summer is hot and dry.
It's going to snow tonight.
Take an umbrella — it's raining.
It's very windy on the corniche.
Spring is my favourite season.
""",
    ),
]

CLASSROOM = dict(
    phrases=["I'm going to be absent on Thursday.", "Would you like to go first?", "I'd like to ask about …", "That's a good idea!",
             "I'm not sure, but I think …", "Good luck!", "See you tomorrow. / See you next lesson."],
    order="""
S: Excuse me. I'm going to be absent on Thursday.
T: OK, thanks for telling me. Is everything all right?
S: Yes, it's my sister's wedding!
T: Congratulations! I'd like to give you the homework now.
S: That's a good idea! Thank you.
T: Have a great time. See you next lesson!
""",
)

READING = dict(
    title="A summer festival in Bosra",
    text="""This summer, there's a big festival in Bosra's old Roman theatre. Ghada and her family would like to go, and they're making plans.

"We're going to drive there on Friday morning," says Ghada. "It's about two hours from Damascus. It's going to be hot and sunny, so we're going to take a lot of water and our hats."

There are concerts every evening. Famous singers are going to perform live on stage, and there are going to be arts and crafts workshops for the children. Ghada's daughter, Mais, wants to take part in a painting competition. Her son wants to see the parade — people are going to dress up in traditional costumes.

Where are they going to stay? "The hotels are full, so we're going to stay at a campsite," says Ghada. "And we'd like to try the local specialities. My husband says the food is the best part of the festival!" """,
    qs="""
## tf: True or false?
The festival is in the winter. | F @ This summer, there's a big festival
They're going to drive to Bosra. | T @ We're going to drive there on Friday morning
It's going to be cold and wet. | F @ It's going to be hot and sunny
Mais wants to take part in a painting competition. | T @ Mais, wants to take part in a painting competition
They're going to stay in a hotel. | F @ we're going to stay at a campsite
## choose: Choose the answer.
How long is the drive from Damascus? | about two hours | about five hours | about thirty minutes @ It's about two hours from Damascus
What's in the parade? | people in traditional costumes | singers on stage | children painting @ people are going to dress up in traditional costumes
## gap: Write one word.
They'd like to try the local [specialities]. @ we'd like to try the local specialities
""",
)

DIALOGUE = dict(
    title="An invitation",
    intro="Layla calls her friend Elif.",
    task="gaps",
    lines="""
Layla: Hi, Elif! Would you [like] to come to my graduation party?
Elif: Oh, I'd [love] to! When is it?
Layla: On Saturday the twelfth. We're going [to] have it in the garden.
Elif: Fantastic! What's the weather going to be [like]?
Layla: Sunny and warm, I hope! We're going to [hire] a band.
Elif: Great! Would you like me to make a [cake]?
Layla: Yes, please! And remember — dress up in party [clothes]!
Elif: OK. See you on Saturday!
""",
)

WQ = """
I'm going to visit my grandparents. (What / you / going to do / for Eid) => What are you going to do for Eid?
Yes, I'd love to! (you / like / come to my party) => Would you like to come to my party?
It's sunny and warm. (What / the weather / like) => What's the weather like? | What is the weather like?
At a campsite. (Where / they / going to stay) => Where are they going to stay?
No, she isn't. She's ill. (she / going to come) => Is she going to come?
Yes, please. With milk. (you / like / a cup of tea) => Would you like a cup of tea?
They're going to hire a band. (What / they / going to do / for the wedding) => What are they going to do for the wedding?
Spring. (What / your favourite season) => What's your favourite season? | What is your favourite season?
"""

WRITING = [
    dict(task="Write an invitation to a party or celebration. Say what it is, when and where, what you're going to do, and what the weather is going to be like.",
         tip="Use going to, would like to, and celebration and weather words. Write 80–120 words.",
         model="Dear friends,\nWould you like to come to my leaving party? I'm going to move to Toronto next month, so I'd like to say goodbye to everyone! The party is going to be on Friday the 20th in my grandparents' courtyard in Sarouja. It's going to be warm and sunny, so we're going to have dinner outside. My mother is going to make traditional food, and we're going to hire a small band. Please dress up in party clothes! I'd love to see you all there.\nBassel",
         check=["Would you like to come…?", "going to for plans", "celebration words: hire a band, make traditional food…", "weather: It's going to be sunny…"],
         min=80, max=120),
]

CANDO = [
    "talk about plans with going to.",
    "invite people with 'Would you like to…?'",
    "answer invitations: 'I'd love to!'",
    "talk about celebrations and parties.",
    "talk about the weather and the seasons.",
]
