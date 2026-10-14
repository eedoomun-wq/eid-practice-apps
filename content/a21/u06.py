META = dict(n=6, title="Food and drink", pages="52–59")

BOOK = """
apple, grape, sandwich, banana, tomato, biscuit, olive oil, orange juice, salad, water,
knife and fork, bread and butter, salt and pepper, fish and chips, sweet and sour, food and drink, tea and coffee,
fruit and vegetables, herbs and spices,
picnic, cappuccino, receipt, change, delicious, rice, side dish, takeaway, medium, healthy, unhealthy,
lively atmosphere, snack, main dish, typical dish, vegetarian, olive
"""

WORDS = """
@Food
apple | a round fruit, red or green | There's an apple in my bag. | | fruit
grape | a small green or purple fruit; wine is made from them | Are there any grapes in the fridge? | | fruit
sandwich | two pieces of bread with food inside | I have a cheese sandwich for lunch. | | meal
banana | a long yellow fruit | Monkeys love bananas! | | fruit
tomato | a red fruit, used as a vegetable in salads | There are some tomatoes on the table. | | veg
biscuit | a small, dry, sweet cake | Have a biscuit with your tea! | | sweet
olive oil | oil from olives, good for salads | Syrian olive oil is delicious. | | oil
orange juice | a drink from oranges | Is there any orange juice? | | drink
salad | a mix of cold vegetables | Fattoush is a Syrian salad. | | meal
water | a clear drink | How much water do you drink every day? | | drink
rice | small white grains, cooked | How much rice is there? | | grain
olive | a small green or black fruit; it gives oil | There are some olives on the plate. | | veg
@Food pairs
knife and fork | the things you use to cut and eat food | Can I have a knife and fork, please?
bread and butter | bread with butter on it | There's some bread and butter for breakfast.
salt and pepper | white and black things to make food taste better | Pass the salt and pepper, please.
fish and chips | a British dish: fried fish and potatoes | Fish and chips is a typical British dish.
sweet and sour | a Chinese taste: sugar and vinegar | Mei likes sweet and sour chicken.
food and drink | things to eat and drink | The food and drink at the festival is cheap.
tea and coffee | two hot drinks | There's tea and coffee in the kitchen.
fruit and vegetables | apples, bananas, tomatoes, potatoes… | Abu Omar sells fruit and vegetables.
herbs and spices | plants and powders for taste: mint, cumin… | Syrian food has a lot of herbs and spices.
@In a café or restaurant
picnic | a meal outside, on the grass | We often have a picnic in the Ghouta orchards on Fridays.
cappuccino | coffee with hot milk and foam | A cappuccino, please — medium.
receipt | a paper that shows what you paid | Can I have a receipt, please?
change | the money you get back | Here's your change: two hundred pounds.
delicious | it tastes very good | This muhammara is delicious!
side dish | a small dish with the main dish | Rice is a side dish with kebab.
takeaway | food you buy at a restaurant and eat at home | Let's get a takeaway tonight!
medium | not big and not small | A medium cappuccino, please.
healthy | good for your body | Fruit and vegetables are healthy. | | health
unhealthy | bad for your body | Fast food is unhealthy. | | health
lively atmosphere | a happy, busy feeling in a place | Al-Nofara café has a lively atmosphere.
snack | a small amount of food between meals | Ka'ak is a good snack.
main dish | the most important dish in a meal | The main dish is maqluba.
typical dish | a dish that is common in a country or place | Kibbeh is a typical dish in Syria.
vegetarian | a person who doesn't eat meat | Raj is vegetarian. He loves mujaddara.
"""

ODD = """
apple, banana, grape, *rice | Rice: not a fruit.
water, orange juice, cappuccino, *biscuit | Biscuit: not a drink.
receipt, change, menu, *olive | Olive: food.
healthy, delicious, lively, *knife | Knife: not an adjective.
rice, water, milk, *apple | Apple: you can count it.
salt and pepper, knife and fork, fish and chips, *main dish | Main dish: not a pair.
"""

GRAMMAR = [
    dict(
        id="g1",
        title="there is / there are",
        visual=dict(type="compare", cols=[
            dict(title="there's (is) + one / uncountable", color="teal", items=["There's an apple.", "There's some milk."]),
            dict(title="there are + plural", color="purple", items=["There are some grapes.", "There are two sandwiches."]),
            dict(title="− / ?", color="coral", items=["There isn't any rice.", "Are there any olives?"]),
        ]),
        pattern=[
            ["+", "There", ["'s", "v"], "some cheese in the fridge."],
            ["+", "There", ["are", "v"], "six eggs."],
            ["−", "There", ["isn't", "n"], "any bread."],
            ["?", ["Are", "v"], "there", "any tomatoes? — Yes, there are."],
        ],
        examples=[
            "{There's} a lively atmosphere at Al-Nofara café.",
            "{There are} a lot of herbs and spices in Syrian food.",
            "{There isn't} any orange juice. Sorry!",
            "{Is there} a vegetarian dish on the menu? — Yes, {there is}.",
        ],
        ar=[
            "There's (في) لشي واحد أو شي ما بينعد، و There are لأكتر من شي.",
            "للنفي: There isn't / There aren't، وللسؤال: Is there…? Are there…?",
            "انتبه: There are two apples، مو There is two apples.",
        ],
        en=[
            "There's = one thing, or things you can't count: There's some milk.",
            "There are = more than one: There are two apples.",
            "Negative: There isn't / There aren't. Question: Is there…? Are there…?",
        ],
        watch=[("There is three tomatoes.", "There are three tomatoes."), ("In the fridge have some milk.", "There's some milk in the fridge."), ("Is there any grapes?", "Are there any grapes?")],
        quick="""
## choose: Choose the answer.
There ___ some milk in the fridge. | 's | are | have
There ___ two bananas. | are | is | 's
___ there any rice? | Is | Are | Has
""",
        sets="""
## choose: Choose the answer.
There ___ a café near the station. | 's | are | have
There ___ some apples on the table. | are | is | 's
There ___ any water in the bottle. | isn't | aren't | not
___ there any olives? | Are | Is | Have
Is there a knife and fork? — Yes, there ___. | is | are | has
There ___ six eggs in the fridge. | are | is | has
There ___ any biscuits. Sorry! | aren't | isn't | not
___ there a vegetarian dish? | Is | Are | Has
Are there any grapes? — No, there ___. | aren't | isn't | not
There ___ some olive oil in the kitchen. | 's | are | have
## gap: Write is, are, isn't or aren't.
There [is|'s] some bread on the table.
There [are] three tomatoes in the bag.
There [isn't|is not] any milk. We need some.
[Is] there a receipt in the bag?
There [aren't|are not] any vegetarian dishes on the menu.
[Are] there any olives?
There [is|'s] a lively atmosphere in the café.
There [are] a lot of spices in this dish.
## transform: Make the sentence negative (−).
There's some cheese. (−) => There isn't any cheese. | There is not any cheese.
There are some grapes. (−) => There aren't any grapes. | There are not any grapes.
There's a receipt. (−) => There isn't a receipt. | There is not a receipt.
There are some biscuits. (−) => There aren't any biscuits. | There are not any biscuits.
There's some rice. (−) => There isn't any rice. | There is not any rice.
There are some olives. (−) => There aren't any olives. | There are not any olives.
There's a side dish. (−) => There isn't a side dish. | There is not a side dish.
There's some orange juice. (−) => There isn't any orange juice. | There is not any orange juice.
## fix: Find and fix the mistake.
There [is>are] three bananas.
There [are>is|'s] some water.
[Is>Are] there any grapes?
There [isn't>aren't] any eggs.
[It has>There is|There's] a café in the station.
Are there any olives? — Yes, there [is>are].
There [aren't>isn't] any milk.
[Have>Is] there a knife?
## order: Put the words in order.
There's some cheese in the fridge.
Are there any tomatoes?
There isn't any milk.
There are a lot of olives.
Is there a vegetarian dish?
There aren't any biscuits.
There's a lively atmosphere here.
Is there any orange juice?
""",
    ),
    dict(
        id="g2",
        title="some / any · countable and uncountable",
        visual=dict(type="jars", left=dict(title="countable", items=["an apple", "two eggs", "some grapes", "a sandwich", "olives"]),
                    right=dict(title="uncountable", items=["some rice", "some water", "milk", "bread", "olive oil"])),
        pattern=[
            ["+", "There are", ["some", "v"], "apples. / There's some rice."],
            ["−", "There aren't", ["any", "n"], "eggs. / There isn't any milk."],
            ["?", "Are there", ["any", "n"], "grapes? / Is there any water?"],
            ["", "Uncountable:", ["no a / an, no -s", "x"], "rice, water, bread, cheese"],
        ],
        examples=[
            "There are {some} grapes in the bowl.",
            "There isn't {any} bread. Can you buy {some}?",
            "Is there {any} olive oil? — Yes, there's {some} in the kitchen.",
            "{Rice} and {water} are uncountable: some rice, some water.",
        ],
        ar=[
            "في أشياء منعدّها (apple → apples) وأشياء ما منعدّها (rice, water, bread).",
            "اللي ما بينعد ما بياخد a ولا s: some bread، مو a bread أو breads.",
            "some بالإيجاب، و any بالنفي والسؤال.",
        ],
        en=[
            "Things you can count: an apple → two apples.",
            "Things you can't count: rice, water, bread → no a, no s.",
            "some: There are some eggs. any: There aren't any eggs. Are there any eggs?",
        ],
        watch=[("a bread", "some bread / a loaf of bread"), ("There aren't some eggs.", "There aren't any eggs."), ("rices", "rice")],
        quick="""
## choose: Choose the answer.
There's ___ milk in the fridge. | some | any | a
Are there ___ olives? | any | some | an
There isn't ___ bread. | any | some | a
""",
        sets="""
## sort: Countable or uncountable? | countable | uncountable
countable: apple, egg, sandwich, banana, tomato, biscuit
uncountable: rice, water, milk, bread, olive oil, cheese
## choose: Choose some or any.
There's ___ rice in the kitchen. | some | any
There aren't ___ eggs. | any | some
Is there ___ orange juice? | any | some
There are ___ grapes on the table. | some | any
There isn't ___ cheese. | any | some
Are there ___ biscuits? | any | some
We've got ___ olives. | some | any
I haven't got ___ change. Sorry. | any | some
## choose: Choose the answer.
There's ___ apple in my bag. | an | some | a
I need ___ bread. | some | a | an
There isn't ___ water. | any | a | some
Can I have ___ banana? | a | some | an
We haven't got ___ rice. | any | a | an
There's ___ milk in the fridge. | some | a | any
Have you got ___ olive oil? | any | an | a
There are ___ tomatoes in the salad. | some | a | any
## gap: Write a, an, some or any.
There's [an] olive on the floor.
Is there [any] milk for my tea?
There are [some] biscuits in the box.
I've got [a] cheese sandwich.
There isn't [any] rice.
We need [some] water.
Are there [any] grapes?
I want [an] apple, please.
## fix: Find and fix the mistake.
There's [a bread>some bread] on the table.
I want some [rices>rice].
There aren't [some>any] eggs.
Is there [some>any] milk?
Can I have [a>an] apple? #id=a21u6-c58a191
We need some [waters>water].
There are [any>some] grapes.
I haven't got [some>any] change.
## order: Put the words in order.
There's some rice in the kitchen.
There aren't any eggs.
Is there any milk?
We need some bread.
Are there any olives?
I've got an apple.
There isn't any cheese.
There are some grapes on the table.
""",
    ),
    dict(
        id="g3",
        title="How much? How many?",
        visual=dict(type="compare", cols=[
            dict(title="How many + countable", color="teal", items=["How many eggs?", "How many apples?", "How many people?"]),
            dict(title="How much + uncountable", color="purple", items=["How much milk?", "How much rice?", "How much is it? (price)"]),
        ]),
        pattern=[
            ["?", ["How many", "v"], "eggs", "are there? — Six."],
            ["?", ["How much", "v"], "water", "do you drink? — Two litres."],
            ["?", ["How much", "v"], "is a cappuccino?", "— 15,000 pounds."],
        ],
        examples=[
            "{How many} sandwiches do you want? — Two, please.",
            "{How much} rice is there? — A kilo.",
            "{How much} is the cappuccino? — 15,000 pounds.",
            "{How many} people are there at the picnic? — Twelve.",
        ],
        ar=[
            "How many للأشياء اللي منعدها (eggs, apples)، و How much للي ما منعدها (milk, rice).",
            "How much is it? كمان منسأل فيها عن السعر: قدّيش حقها؟",
            "بعد How many الاسم جمع: How many apples? مو How many apple?",
        ],
        en=[
            "How many + things you can count: How many eggs?",
            "How much + things you can't count: How much milk?",
            "How much is it? = What's the price?",
            "After How many: more than one → How many apples?",
        ],
        watch=[("How much eggs?", "How many eggs?"), ("How many milk?", "How much milk?"), ("How many apple?", "How many apples?")],
        quick="""
## choose: Choose the answer.
How ___ eggs are there? | many | much | lot
How ___ water do you drink? | much | many | lot
How much ___ the cappuccino? | is | are | does
""",
        sets="""
## choose: How much or how many?
How ___ bananas are there? | many | much
How ___ milk do you want? | much | many
How ___ people are at the café? | many | much
How ___ rice do we need? | much | many
How ___ olives are in the bowl? | many | much
How ___ olive oil is there? | much | many
How ___ biscuits do you eat every day? | many | much
How ___ is a cappuccino? (price) | much | many
How ___ tomatoes do you want? | many | much
How ___ orange juice is there? | much | many
## bank: Use the words.
How [many] eggs are there? — Six.
How [much] cheese is there? — Not a lot.
How [many] sandwiches do you want? — Two.
How [much] is the takeaway? — 40,000 pounds.
How [many] people are vegetarian? — Three.
How [much] water do you drink? — Two litres a day.
How [many] grapes are there? — A lot!
How [much] bread do we need? — Two packets.
## transform: Write the question.
There are six eggs. (How many / eggs) => How many eggs are there?
There's a kilo of rice. (How much / rice) => How much rice is there?
I drink two litres of water a day. (How much / water / you / drink) => How much water do you drink?
The cappuccino is 15,000 pounds. (How much / the cappuccino) => How much is the cappuccino? | How much does the cappuccino cost?
There are twelve people. (How many / people) => How many people are there?
I want three bananas. (How many / bananas / you / want) => How many bananas do you want?
There's a lot of cheese. (How much / cheese) => How much cheese is there?
There are ten olives. (How many / olives) => How many olives are there?
## fix: Find and fix the mistake.
How [much>many] eggs are there?
How [many>much] milk do you want?
How many [apple>apples] do you want?
How much [are>is] the sandwich?
How [many>much] rice is there?
How many [peoples>people] are there?
How [much>many] biscuits are in the box?
How much water [you drink>do you drink]?
## order: Put the words in order.
How many eggs are there?
How much is a cappuccino?
How much water do you drink?
How many people are at the picnic?
How much rice do we need?
How many sandwiches do you want?
How much cheese is there?
How many olives are on the plate?
""",
    ),
]

CLASSROOM = dict(
    phrases=["How do you say … in English?", "What's the difference between … and …?", "I agree. / I don't agree.", "What do you think?",
             "Can I borrow your …?", "Check with your partner.", "I'm ready."],
    order="""
S: How do you say 'khubz' in English?
T: Bread. It's uncountable — some bread.
S: What's the difference between 'bread' and 'a sandwich'?
T: A sandwich is two pieces of bread with food inside.
S: I think sandwiches are healthy. What do you think?
S: I don't agree — not with a lot of cheese!
""",
)

READING = dict(
    title="A picnic in the Ghouta",
    text="""Every spring, Um Khaled and her family have a picnic in the Ghouta orchards. There's always a lively atmosphere, and there's always a lot of food!

This year, there are twelve people. In the big basket, there are some sandwiches, some olives and a lot of fruit and vegetables: tomatoes, cucumbers, grapes and bananas. There's some bread, of course, and a big bottle of olive oil. Um Khaled's main dish is kibbeh — pumpkin kibbeh, with no meat — and the side dish is a big salad with herbs and spices.

Is there any meat? No, there isn't — Um Khaled's nephew is vegetarian. And how much tea is there? A lot! There's always tea and coffee at Syrian picnics. "It isn't a picnic without tea," says Um Khaled.""",
    qs="""
## tf: True or false?
The family has a picnic every spring. | T @ Every spring, Um Khaled and her family have a picnic
There are ten people this year. | F @ This year, there are twelve people
There's some bread. | T @ There's some bread, of course
There's some meat. | F @ Is there any meat? No, there isn't
Um Khaled's nephew is vegetarian. | T @ Um Khaled's nephew is vegetarian
## choose: Choose the answer.
What's the main dish? | kibbeh | salad | sandwiches @ Um Khaled's main dish is kibbeh
How much tea is there? | a lot | a little | none @ And how much tea is there? A lot
## gap: Write one word.
The side dish is a big [salad]. @ the side dish is a big salad with herbs and spices
""",
)

DIALOGUE = dict(
    title="At a café",
    intro="Hala's café in Sha'lan. Sven orders.",
    task="gaps",
    lines="""
Hala: Hello! What can I get you?
Sven: A cappuccino, please. [Medium], please.
Hala: Sure. Anything to eat?
Sven: Are there [any] vegetarian sandwiches?
Hala: Yes, there [are]. Cheese and tomato, or labneh and olives.
Sven: Labneh and olives, please. How [much] is that?
Hala: 30,000 pounds, please.
Sven: Here you are. Can I have the [receipt], please?
""",
)

WQ = """
Six. (How many / eggs / there) => How many eggs are there?
15,000 pounds. (How much / the cappuccino) => How much is the cappuccino? | How much does the cappuccino cost?
Yes, there is. It's in the fridge. (any milk) => Is there any milk?
No, there aren't. Sorry. (any grapes) => Are there any grapes?
A kilo. (How much / rice / we / need) => How much rice do we need?
Yes, I am. I don't eat meat. (you / vegetarian) => Are you vegetarian? | Are you a vegetarian?
Kibbeh. (What / the main dish) => What's the main dish? | What is the main dish?
Twelve. (How many / people / at the picnic) => How many people are at the picnic? | How many people are there at the picnic?
"""

WRITING = [
    dict(task="Write about your fridge or your kitchen today. What is there? What isn't there? What do you need to buy?",
         tip="Use there is / there are, some / any, and countable / uncountable words. Write 50–80 words.",
         model="In our fridge today, there's some milk, some cheese and a lot of labneh. There are six eggs and some tomatoes. There isn't any orange juice, and there aren't any grapes. In the kitchen, there's some rice and a big bottle of olive oil, but there isn't any bread. I need to buy some bread, some fruit and a cappuccino for me!",
         check=["there's / there are", "some (+) and any (− and ?)", "no a / an with uncountable words", "How much / How many (if you ask a question)"],
         min=50, max=80),
]

CANDO = [
    "use there is and there are with food.",
    "use some and any.",
    "know countable and uncountable words.",
    "ask 'How much…?' and 'How many…?'",
    "order food and drink in a café.",
]

PUZZLES = dict(
    case=dict(
        title="Whose basket is yellow?",
        story="Four friends are at a picnic in the Ghouta. Each one has got a basket of a different colour. In each basket, there's some food and a drink.",
        people=["Abu Omar", "Um Khaled", "Rana", "Hadi"],
        groups=[["grapes", "olives", "sandwiches", "biscuits"], ["orange juice", "water", "tea", "coffee"], ["red", "blue", "green", "yellow"]],
        group_names=["food", "drink", "basket"],
        clues=[
            dict(t="There's some tea in Um Khaled's basket.", f=("is", "Um Khaled", "tea")),
            dict(t="There are some olives in the yellow basket.", f=("is", "olives", "yellow")),
            dict(t="There isn't any water in Rana's basket.", f=("not", "Rana", "water")),
            dict(t="There are some biscuits in Hadi's basket.", f=("is", "Hadi", "biscuits")),
            dict(t="There aren't any sandwiches in the blue basket.", f=("not", "sandwiches", "blue"), need=False),
            dict(t="There's some water in the basket with the grapes.", f=("is", "grapes", "water")),
            dict(t="Um Khaled's basket is red.", f=("is", "Um Khaled", "red")),
            dict(t="There's some coffee in the blue basket.", f=("is", "coffee", "blue")),
        ],
        question=dict(q="Whose basket is yellow?", target="yellow", among="people"),
        reveal="The yellow basket is Rana's. There are some olives and some orange juice in it. In Abu Omar's green basket, there are some grapes and some water.",
    ),
    escape=dict(
        place="a spice shop in Bzouriyah",
        intro="You're in a spice shop in Bzouriyah. There are a lot of herbs and spices here, but there isn't a key — and the door isn't open! Open the locks.",
        ending="The door is open! The owner is back, and there's some hot tea and a biscuit for you.",
    ),
    riddles=[
        ("banana", ["There's a soft white fruit inside me.", "Monkeys love me.", "I'm long and yellow."]),
        ("olive", ["There's a stone inside me.", "There are thousands of us on one tree.", "I'm green or black, and I give oil."]),
        ("receipt", ["There are prices and numbers on me.", "I'm a small piece of paper from the shop.", "The cashier gives me to you after you pay."]),
        ("vegetarian", ["I love mujaddara and fattoush.", "There isn't any meat on my plate.", "I don't eat meat or chicken."]),
        ("picnic", ["There isn't a table — there's a blanket on the grass.", "Sometimes there are ants!", "I'm a meal outside, in the Ghouta or in a park."]),
        ("cappuccino", ["I'm from Italy.", "There's some milk and some foam in me.", "I'm a coffee."]),
        ("sandwich", ["There's some cheese or some falafel inside me.", "I'm good for lunch at school or at work.", "I'm two pieces of bread with food inside."]),
        ("tomato", ["I'm a fruit, but people use me as a vegetable.", "There's a lot of me in fattoush.", "I'm red and round."]),
    ],
)
