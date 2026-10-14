META = dict(n=3, title="Your life", pages="24–33")

BOOK = """
live in a house, get up, go to work, live with my parents, study, have a shower, work in an office, have breakfast,
have lunch,
five to nine, quarter to eight, five o'clock, twenty past ten, half past one, quarter past two,
shopping centre, small shops, block of flats, cinema, street market, supermarket, restaurant, swimming pool,
evening, lunchtime, morning, midday, weekdays, midnight, open, weekend, start, town, village, afternoon
"""

WORDS = """
@Your day
live in a house | your home is a house, not a flat | We live in a house with a garden in Kafr Sousa.
get up | to leave your bed | I get up at half past six.
go to work | to travel to your job | I go to work by service taxi.
live with my parents | my home is with my mother and father | I'm single, so I live with my parents.
study | to learn at school or university | I study law at Damascus University.
have a shower | to wash under water | I have a shower in the morning.
work in an office | your workplace is an office | My brothers work in an office in Malki.
have breakfast | to eat in the morning | We have breakfast at seven — bread, labneh and tea.
have lunch | to eat at midday | I have lunch at two o'clock.
@Telling the time
five to nine | 8:55 | My lesson starts at five to nine. | | time
quarter to eight | 7:45 | I leave home at quarter to eight. | | time
five o'clock | 5:00 | I finish work at five o'clock. | | time
twenty past ten | 10:20 | The film starts at twenty past ten. | | time
half past one | 1:30 | We have lunch at half past one. | | time
quarter past two | 2:15 | The bus comes at quarter past two. | | time
@Places in a town
shopping centre | a big building with a lot of shops | There's a new shopping centre in Mezzeh.
small shops | little shops, often family shops | I love the small shops in the Old City.
block of flats | a big building with a lot of homes | We live in a block of flats in Dummar.
cinema | a place where you watch films | Is there a cinema near here?
street market | a market in the street, with fruit, clothes… | There's a street market on Friday mornings.
supermarket | a big shop for food and things for the house | The supermarket is open until midnight.
restaurant | a place where you buy and eat meals | We eat at a restaurant in Qassaa on Thursdays.
swimming pool | a place with water for swimming | The swimming pool at the sports club is very big.
@Times of day
evening | the time between afternoon and night | I watch TV in the evening. | | day
lunchtime | the time for lunch, around midday | The café is busy at lunchtime. | | day
morning | the first part of the day | I drink coffee in the morning. | | day
midday | 12:00 in the day | We have lunch at midday. | | noon
weekdays | Sunday to Thursday in Syria | I work on weekdays. | | week
midnight | 12:00 at night | Hadi finishes work at midnight. | | noon
open | not closed | The bakery is open at six in the morning.
weekend | Friday and Saturday in Syria | What do you do at the weekend? | | week
start | to begin | Lessons start at eight.
town | a place bigger than a village but smaller than a city | Bloudan is a small town in the mountains. | | place
village | a very small place in the countryside | My grandparents live in a village near Homs. | | place
afternoon | the time between midday and evening | I study in the afternoon. | | day
"""

ODD = """
morning, afternoon, evening, *midnight | Midnight: a time, not a part of the day.
cinema, supermarket, swimming pool, *village | Village: not a building.
get up, have a shower, have breakfast, *weekdays | Weekdays: not an action.
half past one, quarter to eight, five o'clock, *lunchtime | Lunchtime: not a clock time.
do, don't, *does, Do you…? | Does: he / she / it (Unit 4).
town, village, city, *street market | Street market: a place in a town.
"""

GRAMMAR = [
    dict(
        id="g1",
        title="Present simple: I / you / we / they",
        visual=dict(type="table", head=["", "+", "−", "?"],
                    rows=[["I / you / we / they", "I live in Midan.", "I don't live alone.", "Do you live in Midan? — Yes, I do."],
                          ["", "We work on weekdays.", "We don't work on Friday.", "Where do you work?"]],
                    colors=["teal", "purple", "coral", "amber"], cap="Present simple: habits and things that are always true"),
        pattern=[
            ["+", "I / we / they", ["work", "v"], "in an office."],
            ["−", "I / we / they", ["don't work", "n"], "at the weekend."],
            ["?", ["Do", "v"], "you", "work on Friday? — No, I don't."],
            ["?", "Where", ["do", "v"], "you live?"],
        ],
        examples=[
            "I {live} with my parents in a block of flats.",
            "We {don't have} lunch at home on weekdays.",
            "{Do} you {study} at university? — Yes, {I do}.",
            "{What time do} you get up? — At half past six.",
        ],
        ar=[
            "المضارع البسيط للعادات والأشياء الثابتة: I get up at six.",
            "للنفي don't + الفعل، وللسؤال Do + you + الفعل: Do you work?",
            "انتبه: ما منحط am مع الفعل: I go، مو I am go.",
        ],
        watch=[("I am work in an office.", "I work in an office."), ("I no live with my parents.", "I don't live with my parents."), ("Where you live?", "Where do you live?")],
        quick="""
## choose: Choose the answer.
I ___ in a block of flats. | live | am live | lives
We ___ work on Friday. | don't | aren't | not
___ you have a shower in the morning? | Do | Are | Is
""",
        sets="""
## choose: Choose the answer.
I ___ up at six thirty. | get | gets | am get
We ___ in a house. We live in a flat. | don't live | aren't live | not live
___ you live with your parents? | Do | Are | Does
Do they work in an office? — Yes, they ___. | do | are | work
Where ___ you study? | do | are | does
I ___ breakfast at home. | have | has | am have
They ___ have lunch at midday. | don't | doesn't | aren't
What time ___ you go to work? | do | are | is
You ___ English very well. | speak | speaks | are speak
Do you like the street market? — No, I ___. | don't | not | doesn't
## gap: Write do or don't.
[Do] you live in Damascus?
I [don't|do not] work at the weekend.
Where [do] they have lunch?
We [don't|do not] have a car.
[Do] your parents live in a village?
I [don't|do not] get up early on Friday.
What [do] you do in the evening?
They [don't|do not] study on Saturday.
## transform: Make the sentence negative (−).
I live in a house. (−) => I don't live in a house. | I do not live in a house.
We go to work by bus. (−) => We don't go to work by bus. | We do not go to work by bus.
They study English. (−) => They don't study English. | They do not study English.
I have a shower in the evening. (−) => I don't have a shower in the evening. | I do not have a shower in the evening.
You work in an office. (−) => You don't work in an office. | You do not work in an office.
We have lunch at home. (−) => We don't have lunch at home. | We do not have lunch at home.
My parents live in a block of flats. (−) => My parents don't live in a block of flats. | My parents do not live in a block of flats.
I get up at six. (−) => I don't get up at six. | I do not get up at six.
## short: Answer the question.
Do you live with your parents? (✓) => Yes, I do.
Do they work on Friday? (✗) => No, they don't. | No, they do not.
Do you have breakfast at home? (✓) => Yes, I do.
Do we have a test today? (✗) => No, we don't. | No, we do not.
Do your friends study English? (✓) => Yes, they do.
Do you go to work by car? (✗) => No, I don't. | No, I do not.
Do they live in a village? (✓) => Yes, they do.
Do you work in an office? (✗) => No, I don't. | No, I do not.
## bank: Use the words.
[Where] do you live? — In Dummar.
[What time|When] do you get up? — At half past six.
[When|What time] do you have lunch? — At lunchtime, at one.
[What] do you study? — Law.
[Who] do you live with? — My parents.
[How] do you go to work? — By service taxi.
[Where] do they work? — In an office in Malki.
[What] do you do at the weekend? — I relax.
## fix: Find and fix the mistake.
I [am live>live] with my parents.
Where [you work>do you work]?
We [no have>don't have] a car.
[Are>Do] you study at university?
They [doesn't>don't] work on Friday.
Do you like it? — Yes, I [like>do].
What time [you get>do you get] up?
I [doesn't>don't] have breakfast.
## order: Put the words in order.
I live with my parents.
Do you work in an office?
We don't have lunch at home.
What time do you get up?
Where do you study?
They don't work at the weekend.
Do you go to the street market?
How do you go to work?
""",
    ),
    dict(
        id="g2",
        title="Telling the time",
        visual=dict(type="clocks", times=[["8:55", "five to nine in the morning"], ["7:45", "quarter to eight in the morning"],
                                          ["17:00", "five o'clock in the afternoon"], ["22:20", "twenty past ten in the evening"],
                                          ["13:30", "half past one in the afternoon"], ["14:15", "quarter past two in the afternoon"]]),
        pattern=[
            ["", "1–30 minutes:", ["past", "v"], "twenty past ten (10:20)"],
            ["", "31–59 minutes:", ["to", "x"], "five to nine (8:55)"],
            ["", "15, 30, 45 minutes:", ["quarter past (2:15) · half past (2:30) · quarter to (2:45)", "s"], ""],
            ["?", "What time", "is it?", "It's half past one."],
        ],
        examples=[
            "It's {quarter past} two. (2:15)",
            "The film starts at {twenty to} nine. (8:40)",
            "I get up at {half past} six. (6:30)",
            "The supermarket closes at {midnight}.",
        ],
        ar=[
            "past يعني 'وْ' (بعد): twenty past ten = عشرة وتلت.",
            "to يعني 'إلا': five to nine = تسعة إلا خمسة.",
            "quarter = ربع، half = نص: half past one = وحدة ونص.",
        ],
        watch=[("half to two (1:30)", "half past one"), ("It's ten and twenty.", "It's twenty past ten."), ("fifteen past two", "quarter past two")],
        quick="""
## choose: Choose the answer.
2:15 = ___ | quarter past two | quarter to two | half past two
8:55 = ___ | five to nine | five past nine | nine to five
1:30 = ___ | half past one | half past two | half to one
""",
        sets="""
## choose: What time is it?
7:45 | quarter to eight | quarter past seven | quarter to seven
10:20 | twenty past ten | twenty to ten | ten past twenty
4:30 | half past four | half past five | half to four
11:55 | five to twelve | five past eleven | five to eleven
3:15 | quarter past three | quarter to three | three past quarter
6:40 | twenty to seven | twenty past six | twenty to six
9:05 | five past nine | five to nine | nine past five
12:30 | half past twelve | half past one | half to twelve
1:50 | ten to two | ten past one | ten to one
5:00 | five o'clock | five past | five clock
## numbers: Write the time in words.
2:15 => quarter past two | a quarter past two | two fifteen
8:55 => five to nine | eight fifty-five | eight fifty five
1:30 => half past one | one thirty
10:20 => twenty past ten | ten twenty
7:45 => quarter to eight | a quarter to eight | seven forty-five | seven forty five
5:00 => five o'clock | five
3:10 => ten past three | three ten
6:35 => twenty-five to seven | twenty five to seven | six thirty-five | six thirty five
## numbers: Write the time in numbers.
quarter past four => 4:15
half past seven => 7:30
twenty to nine => 8:40
five past eleven => 11:05
quarter to two => 1:45
ten past six => 6:10
twenty-five past one => 1:25
ten to twelve => 11:50
## fix: Find and fix the mistake.
It's [half to>half past] three. (3:30)
It's twenty [to>past] ten. (10:20)
It's [fifteen>quarter] past two. (2:15)
The film starts at five [past>to] nine. (8:55)
It's quarter [past>to] eight. (7:45)
I get up at [six and half>half past six].
It's ten [to>past] four. (4:10)
Lunch is at [one and half>half past one].
## order: Put the words in order.
What time is it?
It's quarter past two.
The bus comes at twenty to nine.
I get up at half past six.
The shop opens at quarter to eight.
It's five to nine.
We have lunch at half past one.
The film starts at ten past ten.
""",
    ),
    dict(
        id="g3",
        title="Places in a town",
        visual=dict(type="street", street="Baghdad Street",
                    top=["cinema", "shopping centre", "small shops", "restaurant"], bottom=["block of flats", "swimming pool", "street market", "supermarket"],
                    notes=["The {cinema} is opposite the {block of flats}.", "There's a {street market} next to the {swimming pool}."]),
        pattern=[
            ["", "There's a", ["swimming pool", "v"], "in my town."],
            ["", "There are", ["small shops", "v"], "in the Old City."],
            ["", "I go to the", ["street market", "v"], "on Friday."],
        ],
        examples=[
            "There's a big {shopping centre} in Mezzeh.",
            "I buy fruit at the {street market}.",
            "We live in a {block of flats} near the {cinema}.",
            "My grandparents live in a {village}, not a {town}.",
        ],
        ar=[
            "أسماء الأماكن بالمدينة: shopping centre (مول)، street market (سوق شعبي)، block of flats (بناية).",
            "منستعمل There's / There are لنقول شو في بالمدينة.",
            "village أصغر من town، و town أصغر من city.",
        ],
        watch=[("There is two cinemas.", "There are two cinemas."), ("I go to market street.", "I go to the street market."), ("a block of flat", "a block of flats")],
        quick="""
## choose: Choose the answer.
You buy food there: | supermarket | cinema | swimming pool
You swim there: | swimming pool | block of flats | shopping centre
A lot of homes in one building: | block of flats | street market | small shops
""",
        sets="""
## choose: Where do you go?
I want to see a film. | the cinema | the swimming pool | the supermarket
I want to swim. | the swimming pool | the street market | the restaurant
I need food for dinner tonight. | the supermarket | the cinema | the block of flats
I want to eat a meal with my friends. | a restaurant | a swimming pool | a block of flats
I need new clothes and shoes. | the shopping centre | the swimming pool | the cinema
I want cheap fruit in the open air. | the street market | the cinema | the block of flats
I want to visit a family shop in the Old City. | the small shops | the swimming pool | the supermarket car park
I need a flat in a big building. | a block of flats | a street market | a cinema
## match: Match.
cinema = films
swimming pool = water and swimming
supermarket = food and things for the house
restaurant = meals
block of flats = homes
street market = fruit and clothes in the street
shopping centre = a lot of shops in one building
village = a very small place in the countryside
## gap: Write the place.
I watch films at the [cinema].
We buy fruit at the street [market].
My aunt lives in a block of [flats].
There are a lot of shops in the shopping [centre].
I swim at the swimming [pool] on Monday.
We have dinner at a [restaurant] in Qassaa.
I buy milk at the [supermarket].
My grandparents live in a small [village].
## sort: Bigger or smaller? | big places | small places
big places: city, shopping centre, supermarket, block of flats
small places: village, small shops, café, kiosk
## order: Put the words in order.
There's a cinema in my town.
I go to the street market on Friday.
We live in a block of flats.
Is there a swimming pool near here?
There are small shops in the Old City.
The supermarket is open until midnight.
My grandparents live in a village.
The restaurant opens at midday.
""",
    ),
]

CLASSROOM = dict(
    phrases=["When is the homework for?", "What page are we on?", "Do we need to write this?", "Can you explain that again, please?",
             "Which page?", "I'm finished.", "Homework."],
    order="""
T: Homework: exercise 4 on page 30.
S: When is the homework for?
T: For Sunday.
S: Sorry, what page are we on now?
T: Page 28. Look at the clocks.
S: 'Quarter to'? Can you explain that again, please?
""",
)

READING = dict(
    title="A nurse's day",
    text="""My name's Salma, and I'm a nurse at a hospital in Malki. I live with my parents in a block of flats in Dummar. I work at night, so my day is different.

I start work at eight o'clock in the evening and I finish at eight in the morning. I get home at half past eight. Then I have breakfast with my mother — she gets up early. I go to bed at about ten and I get up at four in the afternoon.

I don't work every night. I have four nights off every week. On my days off, I go to the street market or I meet my friends at a café. I don't go to the cinema — I always fall asleep!""",
    qs="""
## tf: True or false?
Salma lives alone. | F @ I live with my parents
She works at a hospital. | T @ I'm a nurse at a hospital in Malki
She finishes work at eight in the morning. | T @ I finish at eight in the morning
She gets up at four in the morning. | F @ I get up at four in the afternoon
She goes to the cinema on her days off. | F @ I don't go to the cinema
## choose: Choose the answer.
What time does she get home? | at half past eight | at eight o'clock | at ten @ I get home at half past eight
How many nights off has she got every week? | four | two | seven @ I have four nights off every week
## gap: Write one word.
Salma has breakfast with her [mother]. @ Then I have breakfast with my mother
""",
)

DIALOGUE = dict(
    title="A new neighbour",
    intro="A block of flats in Dummar. Ruba meets her new neighbour, Hiba.",
    task="gaps",
    lines="""
Ruba: Hi! I'm Ruba from the second floor. Do you [live] here now?
Hiba: Yes, I do. I'm Hiba. Nice to meet you!
Ruba: Nice to meet you, too. Where do you [work]?
Hiba: In an office in Malki. I go to work [by] bus.
Ruba: What time do you [leave] in the morning?
Hiba: At [quarter] to eight.
Ruba: Me too! Do you know the street [market]? It's on Friday.
Hiba: No, I [don't]. Let's go together!
""",
)

WQ = """
In Dummar. (Where / you / live) => Where do you live?
At half past six. (What time / you / get up) => What time do you get up?
Yes, I do. I live with my parents. (you / live with your parents) => Do you live with your parents?
Law. (What / you / study) => What do you study?
No, we don't. We work on weekdays. (you / work at the weekend) => Do you work at the weekend?
It's quarter past two. (What time / it) => What time is it?
By service taxi. (How / you / go to work) => How do you go to work?
Yes, there is. It's next to the cinema. (a swimming pool / near here) => Is there a swimming pool near here?
"""

WRITING = [
    dict(task="Write about your weekday routine. What time do you get up, go to work or university, have lunch and go to bed?",
         tip="Use the present simple and times: at half past six, at quarter to eight. Write 60–90 words.",
         model="On weekdays I get up at half past six. I have a shower and I have breakfast with my sister. I leave home at quarter past seven and I go to university by bus. My lectures start at eight. I have lunch at half past one in the university café. I get home at about five. In the evening I study, and I go to bed at eleven. I don't watch TV on weekdays.",
         check=["present simple: I get up, I go, I have", "don't + verb", "times with past / to: quarter past seven", "at / on / in"],
         min=60, max=90),
]

CANDO = [
    "talk about my routine with the present simple.",
    "ask and answer 'Do you…?' and 'Where do you…?'",
    "tell the time with past and to.",
    "name places in a town.",
    "say what there is in my town.",
]
