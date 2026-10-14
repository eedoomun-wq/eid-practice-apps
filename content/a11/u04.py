META = dict(n=4, title="Around town", pages="28–35")

BOOK = """
a café, a bank, a restaurant, a car park, a train station, a supermarket, a park, a cinema, a hotel, a shopping centre,
a square, a bus stop,
the sea, a lake, an island, a mountain, a beach, a river, a hill, a rainforest,
town/city centre, cathedral, university, street, fantastic, beautiful, great, good, famous, big, small, old, nice,
eat, travel, buy (food), get (money), meet (friends)
"""

WORDS = """
@Places in a town
café | a place for coffee, tea and cake | Al-Nofara is a famous café in the Old City. |  | eat
bank | a place for your money | There's a bank in Marjeh Square.
restaurant | a place where you eat a meal | There's a good restaurant in Qassaa. |  | eat
car park | a place for cars when you aren't in them | Is there a car park in the city centre?
train station | a place where trains stop | The Hejaz Railway Station is a beautiful old train station.
supermarket | a big shop for food and drink | There's a supermarket next to my house.
park | a green place with trees in a town | Tishreen Park is big and green.
cinema | a place where you watch films | There's a new cinema in the shopping centre.
hotel | a place where you sleep when you travel | There are a lot of hotels in Bab Sharqi.
shopping centre | a big building with a lot of shops | Is there a shopping centre in Mezzeh?
square | an open place in a town, with streets around it | Marjeh Square is in the city centre.
bus stop | a place by the road where you wait for a bus | The bus stop is opposite the bank.
@Nature
the sea | a very big area of salt water | Latakia and Tartus are on the sea.
lake | water with land all around it | There's a big lake near Homs.
island | land with water all around it | Arwad is a small island near Tartus.
mountain | a very high hill | Qasioun is the mountain behind Damascus. |  | high
beach | sand next to the sea | There are a lot of beaches in Latakia.
river | water that goes to the sea | The Orontes is a river in Hama and Homs.
hill | a small mountain | There's a hill behind the village. |  | high
rainforest | a forest with a lot of rain and tall trees | There's a big rainforest in Brazil.
@Other places
town/city centre | the middle of a town or city | There are a lot of shops in the city centre. | city centre;town centre
cathedral | a big, important church | There's a famous cathedral in Barcelona.
university | a place for study after school | Damascus University is in Baramkeh.
street | a road in a town, with buildings | Straight Street is very old.
@Adjectives
fantastic | very, very good | The view from Qasioun is fantastic! |  | pos
beautiful | very nice to look at | The Azem Palace is beautiful. |  | pos
great | very good | There's a great café in Sha'lan. |  | pos
good | nice, not bad | Is there a good restaurant near here? |  | pos
famous | a lot of people know about it | The Umayyad Mosque is very famous.
big | not small | The Citadel is very big.
small | not big | My street is small and quiet.
old | not new | Bab Sharqi is very old.
nice | good, pleasant | There's a nice park near my house. |  | pos
@Verbs
eat | to have food | Qassaa is a good place to eat.
travel | to go to other places | The train is a nice way to travel.
buy (food) | to get food and pay for it | The supermarket is a place to buy food.
get (money) | to take money from a bank | The bank is a place to get money.
meet (friends) | to see friends and talk with them | Al-Nofara café is a great place to meet friends.
"""

ODD = """
café, restaurant, cinema, *mountain | Mountain: nature, not a building.
beach, island, lake, *bank | Bank: not nature.
big, small, old, *street | Street: a place, not an adjective.
in, on, under, *island | Island: a place, not a preposition.
eat, travel, meet, *square | Square: a place.
next to, opposite, behind, *beautiful | Beautiful: an adjective.
some, any, a lot of, *the sea | The sea: nature.
"""

GRAMMAR = [
    dict(
        id="g1",
        title="Prepositions of place",
        visual=dict(type="box", items=[["in", ""], ["on", ""], ["under", ""], ["next to", ""], ["behind", ""], ["in front of", ""],
                                       ["between", ""], ["near", ""], ["opposite", ""]],
                    notes=["The ball is {in} / {on} / {under} the box.", "The ball is {between} the boxes."]),
        pattern=[
            ["", "The bank", "is", ["next to", "x"], "the café."],
            ["", "The bus stop", "is", ["opposite", "x"], "the cinema."],
            ["", "The car park", "is", ["behind", "x"], "the hotel."],
            ["?", ["Where's", "v"], "the park?", ["Near", "x"], "the university."],
        ],
        examples=[
            "The Umayyad Mosque is {in} the Old City.",
            "Al-Nofara café is {behind} the mosque.",
            "The bus stop is {opposite} the bank.",
            "My keys are {on} the table, {next to} the phone.",
        ],
        ar=[
            "هي كلمات بتقول وين الشي: in (جوّا)، on (فوق ع)، under (تحت).",
            "next to (جنب)، near (قريب من)، behind (ورا)، in front of (قدّام).",
            "between (بين شيئين)، opposite (مقابل، بالجهة التانية من الشارع).",
            "انتبه: منقول next to مو next the، و in front of بثلاث كلمات.",
        ],
        en=[
            "These words say where: {in}, {on}, {under}, {near}.",
            "{in} the bag, {on} the table, {under} the chair.",
            "{opposite} = on the other side of the street.",
            "Say {next to} (not: next) and {in front of}.",
        ],
        watch=[("The bank is next the café.", "The bank is next to the café."), ("The car is in front the hotel.", "The car is in front of the hotel."),
               ("The book is on under the table.", "The book is under the table.")],
        quick="""
## choose: Choose the answer.
The keys are ___ the bag. (inside) | in | on | under
The cat is ___ the table. (on the floor, below the table) | under | on | in
The bank is ___ the café and the hotel. | between | next | on #id=a11u4-ef2f82e
""",
        sets="""
## choose: Choose the answer.
The ball is ___ the box. (inside) | in | on | under
The phone is ___ the table. (on top) | on | in | between
The shoes are ___ the bed. (below) | under | on | opposite
The café is ___ the bank. (very close, on the left) | next to | between | under
The bus stop is ___ the cinema. (other side of the street) | opposite | in | under
The car park is ___ the hotel. (at the back) | behind | in front of | on
The taxi is ___ the hotel. (at the front) | in front of | behind | under
The park is ___ the station and the university. | between | under | in #id=a11u4-9f476da
The supermarket is ___ my house. (five minutes) | near | in | under
The cat is ___ the two chairs. | between | next | in #id=a11u4-db0791d
## gap: Write in, on or under.
The tea is [on] the table.
Bab Touma is [in] Damascus.
The bag is [under] the chair.
The eggs are [in] the fridge.
The photos are [on] the wall.
The children are [in] the park.
The pen is [under] the book.
Arwad is [in] the sea.
## bank: Use the words.
The café is [next to] the bank — no space between them.
The bus stop is [opposite] the cinema, on the other side of the street.
The car park is [behind] the hotel.
The taxi is [in front of] the hotel.
The bank is [between] the café and the supermarket.
The station is [near] the university — five minutes, no more.
The ball is [between] the two boxes.
The fountain is [in front of] the Azem Palace door.
## fix: Find and fix the mistake.
The bank is [next>next to] the café.
The taxi is in front [the>of the] hotel.
The keys are [in the on>on] the table.
The café is [between>next to] the bank.
The cat is [under of>under] the bed.
The park is [opposite to>opposite] the station.
Damascus is [on>in] Syria.
The book is [in front>in front of] the computer.
## order: Put the words in order.
The bank is next to the café.
The car park is behind the hotel.
The bus stop is opposite the cinema.
Where's the train station?
The park is near the university.
The keys are on the table.
The shop is between the bank and the hotel.
The taxi is in front of the hotel.
""",
    ),
    dict(
        id="g2",
        title="there is / there are",
        visual=dict(type="street", street="Straight Street",
                    top=["café", "bank", "hotel", "cinema"], bottom=["park", "bus stop", "", "supermarket"],
                    notes=["{There's} a bank next to the café.", "{There are} two buildings next to the bank.",
                           "{There isn't} a school in this street.", "{Is there} a cinema? — Yes, {there is}."]),
        pattern=[
            ["+", "There", "'s", "a bank in the square."],
            ["+", "There", "are", "two cinemas."],
            ["−", "There", "isn't", "a hotel."],
            ["−", "There", "aren't", "any shops."],
            ["?", ["Is", "v"], ["there", "s"], "a café? — Yes, there is."],
            ["?", ["Are", "v"], ["there", "s"], "any buses? — No, there aren't."],
        ],
        examples=[
            "{There's} a famous café in the Old City.",
            "{There are} seven gates in the old wall of Damascus.",
            "{There isn't} a beach in Damascus.",
            "{Is there} a bank near here? — Yes, {there is}. It's in the square.",
        ],
        ar=[
            "There is (There's) يعني 'في' لشي واحد، و There are يعني 'في' لأكتر من شي.",
            "للنفي: There isn't / There aren't. وللسؤال منقدّم is و are: Is there…? Are there…?",
            "انتبه: بالعربي 'في محلّين' بس بالإنكليزي There are two shops، مو There is two shops.",
        ],
        en=[
            "One thing → {There's}: There's a bank in my street.",
            "More than one → {There are}: There are two shops.",
            "Negative: {There isn't} / {There aren't}.",
            "Question: {Is there}…? / {Are there}…?",
        ],
        watch=[("There is two shops.", "There are two shops."), ("In my street have a bank.", "There's a bank in my street."),
               ("There are a hotel.", "There's a hotel."), ("Is there two cafés?", "Are there two cafés?")],
        quick="""
## choose: Choose the answer.
There ___ a bank in the square. | 's | are | is a
There ___ three cafés. | are | is | 's
___ there a cinema? | Is | Are | It
""",
        sets="""
## choose: Choose the answer.
There ___ a big park in Mezzeh. | 's | are | aren't
There ___ a lot of shops in Hamidiyah. | are | is | 's
___ there a bus stop near here? | Is | Are | It
There ___ a beach in Damascus. | isn't | aren't | not
___ there any hotels in Bloudan? | Are | Is | They
Is there a lake? — No, there ___. | isn't | aren't | not
Are there taxis? — Yes, there ___. | are | is | 're
There ___ two banks in the square. | are | is | 's
There ___ a cinema in my town. | isn't | aren't | no
There ___ an island near Tartus. | 's | are | aren't
## gap: Write is, are, isn't or aren't.
There [is|'s] a nice café in Baramkeh.
There [are] four hotels in this street.
There [isn't|is not] a train station in Bloudan.
[Is] there a supermarket near here?
There [aren't|are not] any buses at night.
[Are] there a lot of tourists in Maaloula?
There [is|'s] an old cathedral in Bab Touma.
There [are] two parks near my house.
## short: Answer the question.
Is there a bank in the square? (✓) => Yes, there is.
Are there any cinemas in your town? (✗) => No, there aren't. | No, there are not.
Is there a beach in Latakia? (✓) => Yes, there is.
Is there a lake in Damascus? (✗) => No, there isn't. | No, there is not. #id=a11u4-c325978
Are there a lot of shops in Hamidiyah? (✓) => Yes, there are.
Is there a car park near here? (✗) => No, there isn't. | No, there is not.
Are there islands near Tartus? (✓) => Yes, there are.
Are there any taxis? (✗) => No, there aren't. | No, there are not.
## transform: Make the sentence negative (−).
There's a cinema in my street. (−) => There isn't a cinema in my street. | There is not a cinema in my street.
There are hotels in the village. (−) => There aren't any hotels in the village. | There are not any hotels in the village. | There aren't hotels in the village.
There's a bus stop near here. (−) => There isn't a bus stop near here. | There is not a bus stop near here.
There are a lot of cars. (−) => There aren't a lot of cars. | There are not a lot of cars.
There's a lake in the park. (−) => There isn't a lake in the park. | There is not a lake in the park.
There are students in the classroom. (−) => There aren't any students in the classroom. | There are not any students in the classroom. | There aren't students in the classroom.
There's a supermarket. (−) => There isn't a supermarket. | There is not a supermarket.
There are buses at midnight. (−) => There aren't any buses at midnight. | There are not any buses at midnight. | There aren't buses at midnight.
## transform: Make a question (?).
There's a bank here. (?) => Is there a bank here?
There are cafés in the square. (?) => Are there any cafés in the square? | Are there cafés in the square?
There's a hotel in Maaloula. (?) => Is there a hotel in Maaloula?
There are mountains in Syria. (?) => Are there any mountains in Syria? | Are there mountains in Syria?
There's a park in Malki. (?) => Is there a park in Malki?
There are beaches in Tartus. (?) => Are there any beaches in Tartus? | Are there beaches in Tartus?
There's a cinema near here. (?) => Is there a cinema near here?
There are students in the café. (?) => Are there any students in the café? | Are there students in the café?
## fix: Find and fix the mistake.
There [is>are] two shops in my street.
There [are>is|'s] a big hotel in the square.
[Is>Are] there any cafés near here?
There [isn't>aren't] any taxis.
[Are>Is] there a bank in Sarouja?
Is there a park? — Yes, there [are>is].
[It is>There is|There's] a cinema in the shopping centre.
There [aren't>isn't] a beach in Damascus.
## order: Put the words in order.
There's a bank in the square.
Is there a cinema near here?
There are a lot of cafés in Sha'lan.
There isn't a beach in Damascus.
Are there any hotels in Bloudan?
There aren't any buses at night.
Is there a supermarket in your street?
There are two parks in my town.
""",
    ),
    dict(
        id="g3",
        title="a / an, some, any, a lot of",
        visual=dict(type="compare", cols=[
            dict(title="+ one: a / an", color="teal", items=["There's {a} bank.", "There's {an} old café."]),
            dict(title="+ more: some / a lot of", color="purple", items=["There are {some} shops.", "There are {a lot of} cafés."]),
            dict(title="− and ?: any", color="coral", items=["There aren't {any} hotels.", "Are there {any} buses?"]),
        ], cap="some = a small number · a lot of = a big number"),
        pattern=[
            ["+", "There's", ["a", "x"], "café."],
            ["+", "There's", ["an", "x"], "island."],
            ["+", "There are", ["some", "v"], "shops."],
            ["+", "There are", ["a lot of", "v"], "people."],
            ["−", "There aren't", ["any", "n"], "cinemas."],
            ["?", "Are there", ["any", "n"], "parks?"],
        ],
        examples=[
            "There's {an} island near Tartus.",
            "There are {some} nice cafés in Sha'lan.",
            "There are {a lot of} shops in Souq al-Hamidiyah.",
            "There aren't {any} beaches in Damascus. Are there {any} lakes?",
        ],
        ar=[
            "a و an لشي واحد، و some لعدد قليل (شوية)، و a lot of لعدد كبير (كتير).",
            "بالنفي وبالسؤال منستعمل any مو some: There aren't any…, Are there any…?",
            "ما منحط a قبل الجمع: There are a lot of shops، مو There are a shops.",
        ],
        en=[
            "One → {a} / {an}: There's {a} bank.",
            "{some} = not many. {a lot of} = very many.",
            "Negative and question → {any}: Are there {any} hotels?",
            "No {a} with more than one: There are {some} shops.",
        ],
        watch=[("There aren't some cafés.", "There aren't any cafés."), ("Are there some hotels?", "Are there any hotels?"),
               ("There are a hotels.", "There are some hotels."), ("There's a lot of shops.", "There are a lot of shops.")],
        quick="""
## choose: Choose the answer.
There are ___ cafés in the square. | some | any | a
Are there ___ banks near here? | any | some | an
There's ___ old hotel in Bab Sharqi. | an | a | some
""",
        sets="""
## choose: Choose the answer.
There's ___ supermarket in my street. | a | an | some
There's ___ island near Tartus. | an | a | any
There are ___ hotels in Bloudan. | some | any | a
There aren't ___ cinemas in my village. | any | some | a
Are there ___ restaurants near here? | any | a | an
There are ___ people in Souq al-Hamidiyah! (a big number) | a lot of | any | an
There's ___ university in Baramkeh. | a | an | any
There isn't ___ beach in Damascus. | a | any | some
There are ___ taxis in front of the hotel. (a small number) | some | any | a
Are there ___ parks in Mezzeh? | any | a | an
## sort: a / an or some / any? | a / an | some / any
a / an: bank, island, café, old hotel, university
some / any: shops, apples, people, cafés, taxis
## gap: Write a, an, some or any.
There's [an] old car park behind the cinema.
There are [some] nice shops in the square.
There aren't [any] cafés in my street.
Are there [any] hotels in Maaloula?
There's [a] bus stop opposite the bank.
There are [some] apples on the table.
Is there [a] bank near here?
There isn't [an] island in the lake.
## choose: some or any?
There are ___ cafés in Sha'lan. | some | any
There aren't ___ banks near here. | any | some
Are there ___ shops in your street? | any | some
There are ___ tourists in the square. | some | any
There aren't ___ trains at night. | any | some
Are there ___ good restaurants in Midan? | any | some
There are ___ buses in front of the station. | some | any
There aren't ___ hills in my town. | any | some
## fix: Find and fix the mistake.
There aren't [some>any] hotels here.
Are there [some>any] banks near here?
There are [a>some|a lot of] shops in my street.
There's [a>an] old cinema in the city centre.
There [is>are] a lot of people in the park.
There's [an>a] university in Baramkeh.
There are a lot [people>of people] in the souq.
There isn't [any>a] bank in the village. #id=a11u4-18e39f2
## order: Put the words in order.
There are some cafés in the square.
There aren't any hotels in my village.
Are there any shops near here?
There are a lot of people in the park.
There's an old cinema in Malki.
Is there a bank in this street?
There are some apples in the bag.
There isn't a train station here.
""",
    ),
]

CLASSROOM = dict(
    phrases=["I'm ready.", "I'm finished.", "It's my turn.", "Excuse me.", "Thank you.", "Change partners.", "Hands up.", "Be quiet, please."],
    order="""
T: Be quiet, please. Are you ready?
S: Yes, I'm ready.
T: Change partners, please.
S: Excuse me, it's my turn.
T: OK. Finished? Hands up!
S: I'm finished!
""",
)

READING = dict(
    title="Bab Touma: a great place to visit",
    text="""Bab Touma is in the Old City of Damascus. There's an old gate with the same name. There are a lot of small streets, and there are some beautiful old houses with courtyards.

There are a lot of cafés and restaurants here, so it's a good place to eat and meet friends. There's a small hotel opposite the gate, and there's a bank next to the hotel. There isn't a cinema in Bab Touma, and there aren't any big supermarkets. The streets are small and old!""",
    qs="""
## tf: True or false?
Bab Touma is in the Old City. | T @ Bab Touma is in the Old City of Damascus
There's a cinema in Bab Touma. | F @ There isn't a cinema in Bab Touma
There are a lot of cafés. | T @ There are a lot of cafés and restaurants here
There's a big supermarket. | F @ there aren't any big supermarkets
The streets are big and new. | F @ The streets are small and old
## choose: Choose the answer.
Where's the bank? | next to the hotel | opposite the gate | behind the café @ there's a bank next to the hotel
Where's the hotel? | opposite the gate | behind the bank | in front of the cinema @ There's a small hotel opposite the gate #id=a11u4-3a5ff80
## gap: Write one word.
There are some beautiful old houses with [courtyards]. @ some beautiful old houses with courtyards
""",
)

DIALOGUE = dict(
    title="Is there a bank near here?",
    intro="Marjeh Square. A tourist, Lucas, and Jad, a delivery driver.",
    task="gaps",
    lines="""
Lucas: Excuse me. Is [there] a bank near here?
Jad: Yes, there [is]. It's in the square, next to the hotel.
Lucas: Great, thanks. And are there [any] cafés near here?
Jad: Yes, there are [a lot of] cafés in this street.
Lucas: Is there a bus stop for the Hejaz Railway Station?
Jad: Yes. It's [opposite] the bank, in front of the post office.
Lucas: Thank you very much!
""",
)

WQ = """
Yes, there is. It's next to the café. (a bank) => Is there a bank near here? | Is there a bank? | Is there a bank here?
No, there aren't. (any hotels / in the village) => Are there any hotels in the village?
It's opposite the cinema. (where / the bus stop) => Where's the bus stop? | Where is the bus stop?
Yes, there are a lot. (any cafés / in Sha'lan) => Are there any cafés in Sha'lan?
They're on the table. (where / my keys) => Where are my keys?
No, there isn't. (a beach / in Damascus) => Is there a beach in Damascus?
It's behind the hotel. (where / the car park) => Where's the car park? | Where is the car park?
Yes, there's a big park. (a park / in Mezzeh) => Is there a park in Mezzeh?
"""

WRITING = [
    dict(task="Write about your street or your area. What's there? What isn't there?",
         tip="Use there's / there are / there isn't / there aren't, and in, next to, opposite. Write 30–60 words.",
         model="I'm from Malki. It's a nice area. There's a big park, and there are a lot of shops and cafés. There's a bank opposite the park. There's a bakery next to my building. There isn't a cinema, and there aren't any hotels.",
         check=["There's + one thing", "There are + more things", "There isn't / There aren't", "a preposition: next to, opposite, in…"],
         min=30, max=60),
]

CANDO = [
    "say where things are: in, on, under, next to…",
    "use there's and there are.",
    "ask 'Is there a … near here?'",
    "use some, any and a lot of.",
    "say places in a town.",
]

# ---- Puzzles (round 2): the case, the escape room texts, What am I? riddles.
# The crossword, word search, escape locks and Guess the word are built from the unit data.
PUZZLES = dict(
    case=dict(
        title="Where's Hadi?",
        story="Saturday in the city centre. There are three friends here — Rana, Kareem and Hadi — but where are they? One friend is in a café, one is at a bus stop and one is in a car park.",
        people=["Rana", "Kareem", "Hadi"],
        groups=[["café", "bus stop", "car park"], ["next to the bank", "opposite the cinema", "behind the hotel"]],
        group_names=["place", "where"],
        clues=[
            dict(t="The bus stop is opposite the cinema.", f=("is", "bus stop", "opposite the cinema")),
            dict(t="Hadi isn't in the car park.", f=("not", "Hadi", "car park"), need=False),
            dict(t="The car park is behind the hotel.", f=("is", "car park", "behind the hotel")),
            dict(t="Kareem is behind the hotel.", f=("is", "Kareem", "behind the hotel")),
            dict(t="There's a friend at the bus stop, but it isn't Rana.", f=("not", "Rana", "bus stop")),
            dict(t="Kareem isn't next to the bank.", f=("not", "Kareem", "next to the bank"), need=False),
        ],
        question=dict(q="Where's Hadi?", target="Hadi", among=0),
        reveal="Hadi is at the bus stop, opposite the cinema. Kareem is in the car park behind the hotel, and Rana is in the café next to the bank.",
    ),
    escape=dict(
        place="the Hejaz Railway Station",
        intro="You're in the Hejaz Railway Station. There's a big old door in front of you, but it isn't open!",
        ending="The door is open! There's a train to Zabadani next to you. Have a good trip!",
    ),
    riddles=[
        ("cinema", ["I'm dark inside, but the people are happy.", "There are a lot of seats and a big screen in me.", "Popcorn and a film? Come in!"]),
        ("bank", ["I'm a place for numbers, not letters.", "There's a lot of money in me.", "Your money? It's safe with me!"]),
        ("island", ["I'm in the sea or in a lake.", "There's water all around me.", "Arwad, near Tartus — that's me!"]),
        ("mountain", ["I'm very high, and there's snow on me in winter.", "There are a lot of us in Syria.", "Qasioun, behind Damascus, is one of us!"]),
        ("supermarket", ["There are a lot of things in me, from apples to soap.", "I'm a big shop for food and drink.", "Trolleys, baskets and a long queue — that's me!"]),
        ("rainforest", ["I'm green, wet and very big.", "There are a lot of tall trees and animals in me.", "The Amazon, in Brazil — that's me!"]),
        ("café", ["There's music, and there are a lot of people in me.", "Tea, coffee and cake: that's my menu.", "Al-Nofara, behind the Umayyad Mosque, is a famous one!"]),
    ],
)
