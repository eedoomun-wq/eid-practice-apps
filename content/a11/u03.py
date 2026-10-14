META = dict(n=3, title="Going places", pages="20–27")

BOOK = """
shop – shops, taxi – taxis, car – cars, student – students, bus – buses, address – addresses, sandwich – sandwiches,
city – cities, country – countries, nationality – nationalities, man – men, woman – women, person – people,
child – children,
friendly – unfriendly, happy – sad, cheap – expensive, fantastic – awful,
tea, coffee, milk, water, meat, fish, chicken, fruit, apples, vegetables, potatoes, bread, rice, pasta, eggs, cheese,
on holiday, on business, hotel, capital city, official language, colours, black, white, red, yellow, delicious,
horrible, breakfast, the same as, different from, typical, favourite
"""

WORDS = """
@Plurals
shop – shops | a place where you buy things | This shop is small, but those shops are big. | &shop;shops
taxi – taxis | a car with a driver; you pay for the trip | That taxi is yellow. These taxis are white. | &taxi;taxis
car – cars | it has four wheels; you drive it | My car is old. Those cars are new. | &car;cars
student – students | a person who studies | I'm a student. We're students at the same school. | &student;students
bus – buses | a big vehicle for a lot of passengers | This bus is full. Those buses are empty. | &bus;buses
address – addresses | the number, street and town of a house or building | What's your address? These addresses are in Mezzeh. | &address;addresses
sandwich – sandwiches | bread with cheese, meat or egg inside | This sandwich is for you. These sandwiches are for Jad. | &sandwich;sandwiches
city – cities | a big town | Damascus is a city. Aleppo and Homs are cities, too. | &city;cities
country – countries | Syria, Italy, Japan… | Syria is a country. Spain and Portugal are countries in Europe. | &country;countries
nationality – nationalities | Syrian, Brazilian, Chinese… | My nationality is Syrian. Syrian and Lebanese are nationalities. | &nationality;nationalities
man – men | an adult male / adult males | That man is a driver. Those men are drivers, too. | &man;men
woman – women | an adult female / adult females | This woman is a doctor. These women are nurses. | &woman;women
person – people | one man, woman or child / more than one | Hala is a friendly person. The people in Sha'lan are friendly. | &person;people
child – children | a young boy or girl / more than one | Joud is a child. Joud and Mais are children. | &child;children
@Opposites
friendly – unfriendly | nice and kind to people / not nice to people | The people here are friendly. That man is unfriendly. | &friendly;unfriendly
happy – sad | with a smile / with tears | We're happy today. Why is he sad? | &happy;sad
cheap – expensive | not much money / a lot of money | Ka'ak is cheap. These shoes are expensive! | &cheap;expensive
fantastic – awful | very, very good / very, very bad | This knafeh is fantastic! That coffee is awful. | &fantastic;awful
@Food and drink
tea | a hot drink; Syrians love it with sugar | This tea is very sweet! |  | drink
coffee | a hot black drink, often with cardamom | Arabic coffee is my favourite drink. |  | drink
milk | a white drink from cows | Is this milk fresh? |  | drink
water | a drink with no colour; it's in rivers | This water is cold. |  | drink
meat | food from animals, like lamb or beef | The meat in this kebab is delicious. |  | food-meat
fish | an animal from the sea or a river; also food | Fish is typical food in Latakia. |  | food-meat
chicken | a bird; its meat is food | Shish tawook is chicken. |  | food-meat
fruit | apples, oranges, grapes… | The fruit in the Ghouta orchards is fantastic. |  | food-plant
apples | red or green fruit | These apples are from Zabadani. |  | food-plant
vegetables | potatoes, tomatoes, carrots… | These vegetables are cheap and fresh. |  | food-plant
potatoes | brown or yellow vegetables; chips are made from them | These potatoes are from Abu Omar, the greengrocer. |  | food-plant
bread | food made from flour; Syrians eat it every day | This bread is hot! |  | food-grain
rice | small white grains, good with meat | Maqluba is rice, meat and vegetables. |  | food-grain
pasta | Italian food, like spaghetti | Pasta is typical Italian food. |  | food-grain
eggs | food from chickens, white or brown | These eggs are for breakfast. |  | food-egg
cheese | white or yellow food made from milk | Halawet el-jibn is a sweet with cheese. |  | food-egg
@Other words
on holiday | not at work; you travel for fun | We're on holiday in Latakia.
on business | you travel for your job | Are they on business in Dubai?
hotel | a building where you sleep when you travel | Our hotel is in Bab Sharqi.
capital city | the most important city of a country | Damascus is the capital city of Syria.
official language | the language of a country, used by the government | The official language of Brazil is Portuguese.
colours | black, white, red, yellow… | What colours are your bags? — Red and black.
black | the colour of the night | Arabic coffee is black.
white | the colour of milk and snow | These eggs are white.
red | the colour of tomatoes | Those apples are red.
yellow | the colour of lemons and the sun | The taxis in Damascus are yellow.
delicious | it tastes very good | This fattoush is delicious! |  | good-taste
horrible | very bad | That coffee is cold and horrible. |  | bad
breakfast | the first meal of the day | Labneh and bread are a typical Syrian breakfast.
the same as | not different | My bag is the same as your bag!
different from | not the same | Syrian bread is different from French bread.
typical | normal for a place or a person | Ful is a typical Damascus breakfast.
favourite | you like it best | Mutabbal is my favourite dish.
"""

ODD = """
apples, potatoes, vegetables, *tea | Tea: a drink.
milk, water, coffee, *cheese | Cheese: food, not a drink.
men, women, children, *child | Child: one, not more.
cheap, happy, friendly, *awful | Awful: a bad word. The others: good words.
black, white, yellow, *bread | Bread: not a colour.
this, that, *these, it | These: more than one. #id=a11u3-9f21d6c
shops, cars, buses, *bus | Bus: one, not more.
"""

GRAMMAR = [
    dict(
        id="g1",
        title="this / that / these / those",
        visual=dict(type="hands", obj="bag", labels=dict(
            this="This bag is red.", these="These bags are cheap.",
            that="That bag is black.", those="Those bags are expensive.")),
        pattern=[
            ["", ["This", "v"], "is", "my bag. (one, near)"],
            ["", ["These", "v"], "are", "my bags. (more, near)"],
            ["", ["That", "x"], "is", "a hotel. (one, far)"],
            ["", ["Those", "x"], "are", "hotels. (more, far)"],
            ["?", "What's", ["this?", "v"], "— It's ka'ak."],
            ["?", "What are", ["those?", "x"], "— They're norias."],
        ],
        examples=[
            "{This} ka'ak is delicious!",
            "{These} apples are from Zabadani.",
            "{That} man is Abu Salim. He's a taxi driver.",
            "{Those} buses are for Bab Touma.",
        ],
        ar=[
            "this و these للشي القريب (هاد، هدول)، و that و those للشي البعيد (هداك، هدوليك).",
            "this و that لشي واحد مع is، و these و those لأكتر من شي مع are.",
            "بالسؤال: What's this? → It's… و What are these? → They're…",
        ],
        watch=[("This apples are red.", "These apples are red."), ("Those is my bag.", "That is my bag. / Those are my bags."),
               ("What are this?", "What's this?")],
        quick="""
## choose: Choose the answer.
___ bag is mine. (near, one) | This | These | Those
___ buses are old. (far, more) | Those | That | This
What are ___? — They're apples. (near) | these | this | that
""",
        sets="""
## choose: Choose the answer.
___ coffee is hot. (near) | This | These | Those
___ shops are expensive. (far) | Those | That | This
___ men are drivers. (near) | These | This | That
___ hotel is fantastic. (far) | That | Those | These
What's ___? (near) — It's makdous. | this | these | those
___ children are happy. (far) | Those | That | This
___ is my friend, Maya. (near) | This | These | Those
Are ___ taxis free? (far) | those | that | this
___ bread is fresh. (near) | This | These | Those
___ apples are red. (near) | These | This | That
## sort: One or more than one? | this / that | these / those
this / that: bag, taxi, child, woman, person, city
these / those: bags, taxis, children, women, people, cities
## gap: Write this, that, these or those.
[This] tea is sweet. (near)
[Those] people are from Brazil. (far)
[That] restaurant is famous. (far)
[These] eggs are white. (near)
Is [that] the Citadel? (far)
[These] sandwiches are cheap. (near)
What are [those]? (far) — They're norias.
[This] is my teacher, Rana. (near)
## fix: Find and fix the mistake.
[This>These] apples are red.
[Those>That] is my car.
These [is>are] my friends.
What [are>is|'s] this?
That [are>is] a cheap hotel.
[That>Those] buses are new.
These [child>children] are happy.
[These>This] bread is hot.
## order: Put the words in order.
This tea is delicious.
Those shops are expensive.
What's that?
These are my children.
Is that your hotel?
What are these?
That man is unfriendly.
These apples are cheap.
## match: Match the question and the answer.
What's this? = It's a sandwich.
What are these? = They're potatoes.
Is that your car? = Yes, it is. It's new.
Are those your bags? = No, they aren't.
What's that? = It's the Umayyad Mosque.
Are these eggs fresh? = Yes, they are.
Is this tea sweet? = No, it isn't.
What are those? = They're the norias of Hama.
""",
    ),
    dict(
        id="g2",
        title="be: we / they",
        visual=dict(type="table", head=["", "+", "−", "?"],
                    rows=[["we", "we're", "we aren't", "Are we…?"], ["they", "they're", "they aren't", "Are they…?"],
                          ["you (more)", "you're", "you aren't", "Are you…?"]],
                    colors=["teal", "purple", "coral", "amber"], cap="we, you, they + are"),
        pattern=[
            ["+", "We", "'re", "on holiday."],
            ["−", "They", "aren't", "from Homs."],
            ["?", ["Are", "v"], ["they", "s"], "students?"],
            ["", "Yes, they", "are.", ""],
            ["", "No, we", "aren't.", ""],
        ],
        examples=[
            "{We're} from Damascus. {We're} Syrian.",
            "Rana and Kareem {are} teachers. {They're} friendly.",
            "{Are they} on business? — No, {they aren't}. {They're} on holiday.",
            "Lucas and Sofia {aren't} English. {They're} Brazilian.",
        ],
        ar=[
            "مع we و they منستعمل are: We are، They are.",
            "we يعني نحنا، و they يعني هنّن. You كمان بتنفع لأكتر من شخص.",
            "للنفي: aren't، وللسؤال منقدّم are: Are they Syrian?",
        ],
        watch=[("They is from Aleppo.", "They're from Aleppo."), ("We from Syria.", "We're from Syria."), ("Are Brazilian they?", "Are they Brazilian?")],
        quick="""
## choose: Choose the answer.
We ___ students. | 're | 's | 'm
___ they on holiday? | Are | Is | Am
Lina and Maha ___ from Hama. | are | is | am
""",
        sets="""
## choose: Choose the answer.
They ___ on business. | 're | 's | 'm
We ___ from Syria. | are | is | am
___ we late? | Are | Is | Am
Kenji and Mei ___ Italian. Kenji is Japanese. | aren't | isn't | not #id=a11u3-33f7729
Are they friendly? — Yes, they ___. | are | is | 're
Are you on holiday? — No, we ___. | aren't | isn't | not
The apples ___ cheap. | are | is | am
My parents ___ in Aleppo. | are | is | be
The hotel ___ expensive. | is | are | be
These sandwiches ___ delicious. | are | is | am
## gap: Write are, 're or aren't.
We [are|'re] on holiday in Tartus.
They [aren't|are not] Italian. They're Spanish.
[Are] you and Salma friends?
Ahmad and Omar [are] students.
We [aren't|are not] from Homs. We're from Hama.
[Are] they at the hotel? — Yes, they are.
You [are|'re] great students!
The vegetables [aren't|are not] expensive.
## short: Answer the question.
Are they from Egypt? (✓) => Yes, they are.
Are you students? (✗) => No, we aren't. | No, we're not. | No, we are not.
Are we late? (✓) => Yes, we are. | Yes, you are.
Are these apples cheap? (✓) => Yes, they are.
Are Bassel and Mazen on business? (✗) => No, they aren't. | No, they're not. | No, they are not.
Are you on holiday? (✓) => Yes, we are.
Are those taxis free? (✗) => No, they aren't. | No, they're not. | No, they are not.
Are the people friendly? (✓) => Yes, they are.
## transform: Make it plural.
I'm a student. (+) => We're students. | We are students.
She's on holiday. (+) => They're on holiday. | They are on holiday.
He's Brazilian. (+) => They're Brazilian. | They are Brazilian.
This is my bag. (+) => These are my bags.
That car is expensive. (+) => Those cars are expensive.
Is she a teacher? (+) => Are they teachers?
I'm not from Homs. (+) => We aren't from Homs. | We're not from Homs. | We are not from Homs.
This woman is a doctor. (+) => These women are doctors.
## transform: Make a question (?).
They're from Aleppo. (?) => Are they from Aleppo?
We're late. (?) => Are we late?
These eggs are fresh. (?) => Are these eggs fresh?
You're on business. (?) => Are you on business?
They're Chinese. (?) => Are they Chinese?
Those buses are new. (?) => Are those buses new?
The children are happy. (?) => Are the children happy?
Wei and Mei are students. (?) => Are Wei and Mei students?
## fix: Find and fix the mistake.
They [is>are|'re] from Aleppo.
We [from>'re from|are from] Syria.
[Is>Are] they on holiday?
My friends [is>are] friendly.
We [isn't>aren't|are not] Italian.
Mais and Lama [is>are] sisters.
[They>They're|They are] typical Syrian dishes.
Are they Polish? — Yes, they [is>are].
## order: Put the words in order.
We're on holiday.
Are they from Spain?
They aren't from Spain.
We're not students. || We aren't students.
Are you on business?
They're my friends.
Are the shops expensive?
We're from the same city.
""",
    ),
]

CLASSROOM = dict(
    phrases=["Can I go to the bathroom?", "Can I have a pen / some paper?", "Sorry, I don't have my book.", "Is this right?",
             "Work in pairs.", "Work in groups.", "Check with your partner.", "Stand up.", "Sit down."],
    order="""
T: Work in pairs, please.
S: Sorry, I don't have my book.
T: OK. Look at the book with your partner.
S: Thank you. Is this right?
T: Yes, it is. Well done!
S: Can I go to the bathroom?
""",
)

READING = dict(
    title="A postcard from Rome",
    text="""Hi Dima!

We're in Rome on holiday. Rome is the capital city of Italy, and the official language is Italian. Our hotel is small and cheap, but it's fantastic. The people here are friendly.

The food is delicious! Pizza and pasta are typical Italian dishes. The gelato is my favourite. The coffee is different from Arabic coffee — it's very strong. These scooters are everywhere, and they're red, white and yellow.

See you in Damascus!
Rana and Kareem""",
    qs="""
## tf: True or false?
Rana and Kareem are on business. | F @ We're in Rome on holiday
The hotel is expensive. | F @ Our hotel is small and cheap
The people are friendly. | T @ The people here are friendly
Pizza and pasta are typical Italian dishes. | T @ Pizza and pasta are typical Italian dishes
Italian coffee is the same as Arabic coffee. | F @ The coffee is different from Arabic coffee
## choose: Choose the answer.
The official language of Italy is ___. | Italian | English | Arabic @ the official language is Italian
Rana: "The ___ is my favourite." | gelato | pizza | pasta @ The gelato is my favourite
## gap: Write one word.
The scooters are red, white and [yellow]. @ they're red, white and yellow
""",
)

DIALOGUE = dict(
    title="In the souq",
    intro="Souq al-Hamidiyah. Sven, a tourist from Sweden, and Um Khaled.",
    task="both",
    lines="""
Sven: Excuse me, what's [this]?
Um Khaled: It's makdous. It's [typical] Syrian food.
Sven: And what are [those]?
Um Khaled: They're ka'ak. They're [delicious]!
Sven: Are [they] cheap?
Um Khaled: Yes, they [are]. Are you on holiday?
Sven: No, I'm on [business]. My company is in Damascus this week.
Um Khaled: Welcome to Damascus!
""",
)

WQ = """
They're from Aleppo. (where) => Where are they from?
It's ka'ak. (what / this) => What's this? | What is this? | What's that? | What is that?
They're potatoes. (what / these) => What are these? | What are those?
Yes, we are. We're on holiday. (on holiday?) => Are you on holiday?
No, they aren't. They're cheap. (expensive?) => Are they expensive?
We're from Brazil. (where / you) => Where are you from?
Yes, it is. It's my car. (your car?) => Is that your car? | Is this your car? | Is it your car?
Mutabbal. (your favourite dish) => What's your favourite dish? | What is your favourite dish?
"""

WRITING = [
    dict(task="You're on holiday. Write a postcard to a friend: where you are, the hotel, the people, the food.",
         tip="Use We're / They're and this / these. Write 30–60 words.",
         model="Hi Hiba!\nWe're in Latakia on holiday. Our hotel is on the corniche. It's small but nice. The people are friendly, and the fish is delicious. These photos are from the beach. See you soon!\nLina",
         check=["We're … on holiday", "is for one thing, are for more", "an adjective: cheap, friendly, delicious…", "Hi … at the start, your name at the end"],
         min=30, max=60),
    dict(task="Write about a typical breakfast in your house. What's on the table?",
         tip="Write 20–40 words.",
         model="Our breakfast is typical Syrian food. Labneh, cheese, eggs and olives are on the table. The bread is hot. The tea is strong and sweet. My favourite is ful!",
         check=["food words: bread, cheese, eggs…", "drink words: tea, coffee, milk…", "is / are", "My favourite is …"],
         min=20, max=40),
]

CANDO = [
    "use this, that, these and those.",
    "say plural words: bus – buses, man – men.",
    "use we're and they're.",
    "say food and drink words.",
    "ask 'What's this?' and 'What are those?'",
]
