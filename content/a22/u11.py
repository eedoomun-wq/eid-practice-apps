META = dict(n=11, title="Nature", pages="96–105")

BOOK = """
camel, fish, chimpanzee, horse, dog, llama, dolphin, rat, snake, donkey, elephant, whale,
beach, ocean, desert, river, forest, sea, valley, lake, mountain, volcano,
five point five, fifty thousand, five hundred thousand, five million, five hundred and five, five billion,
population, active volcano, kilogram, varieties of plants, kilometres per hour, wild animals, metre, wildlife,
working animals, pets
"""

WORDS = """
@Animals
camel | a big desert animal with one or two humps | Camels can walk for days in the desert without water. | | big
fish | an animal that lives and swims in water | There are a lot of fish in the Orontes. | | water
chimpanzee | an intelligent African animal, like a small ape | Chimpanzees use sticks as tools. | | jungle
horse | a big animal people ride | Abu Omar loves horses. | | farm
dog | a pet that says "woof" | Sven's dog is very friendly. | | pet
llama | a South American animal with long hair and a long neck | Llamas live in the mountains of Peru. | | farm
dolphin | an intelligent sea animal that jumps out of the water | We saw dolphins near Arwad! | | water
rat | a small grey animal with a long tail | There was a rat in the kitchen! | | small
snake | a long animal with no legs | Some snakes are very dangerous. | | small
donkey | an animal like a small horse with long ears | Donkeys carried water in the old villages. | | farm
elephant | the biggest land animal, with a long nose | An elephant weighs about 6,000 kilograms. | | big
whale | a very big animal that lives in the sea | The blue whale is the biggest animal in the world. | | water
@Places in nature
beach | sand next to the sea | We spent the day at the beach in Latakia. | | coast
ocean | a very big sea, like the Atlantic | The Pacific is the biggest ocean. | | water-big
desert | a very dry place with sand | The Syrian Desert is very hot in summer. | | dry
river | water that goes across the land to the sea | The Euphrates is a long river. | | water-move
forest | a place with a lot of trees | There are forests near Kasab. | | green
sea | a big area of salt water | Latakia is on the Mediterranean Sea. | | water-big
valley | low land between hills or mountains | Wadi al-Nasara is a beautiful green valley. | | low
lake | water with land all around it | Lake Qattinah is near Homs. | | water-still
mountain | a very high hill | Mount Hermon is the highest mountain in Syria. | | high
volcano | a mountain that can send out fire and hot rock | Vesuvius is a volcano in Italy. | | high
@Big numbers
five point five | 5.5 | The baby weighed five point five kilos? No — three point five! | | num
fifty thousand | 50,000 | The stadium has fifty thousand seats. | | num
five hundred thousand | 500,000 | Five hundred thousand people visited the festival. | | num
five million | 5,000,000 | Five million people live in that city. | | num
five hundred and five | 505 | There are five hundred and five students in the school. | | num
five billion | 5,000,000,000 | Five billion people use mobile phones. | | num
@Other words
population | the number of people in a place | What's the population of Damascus?
active volcano | a volcano that can erupt today | Etna in Italy is an active volcano.
kilogram | 1,000 grams (kg) | A kilogram of apples, please.
varieties of plants | different types of plants | The Ghouta has many varieties of plants.
kilometres per hour | km/h: how fast | Cheetahs can run at more than 100 kilometres per hour.
wild animals | animals that don't live with people | There aren't many wild animals near the city.
metre | 100 centimetres (m) | Hadi is one metre eighty.
wildlife | wild animals and plants | The wildlife in the Amazon is amazing.
working animals | animals that work for people, like horses and donkeys | Donkeys and camels were important working animals.
pets | animals that live in your home | Do you have any pets?
"""

ODD = """
camel, elephant, horse, *dolphin | Dolphin: lives in the sea.
dog, cat, fish, *volcano | Volcano: not a pet.
river, lake, sea, *desert | Desert: no water.
a few, a little, a lot of, *ocean | Ocean: not a quantity word.
million, billion, thousand, *metre | Metre: not a number word.
What, Which, How many, *Because | Because: not a question word.
"""

GRAMMAR = [
    dict(
        id="g1",
        title="Question words",
        visual=dict(type="table", head=["question word", "asks about…", "example"],
                    rows=[["What / Which", "a thing", "Which animal is the biggest?"], ["Who", "a person", "Who took this photo?"],
                          ["Where / When / Why", "place / time / reason", "Why do camels have humps?"],
                          ["How many / How much", "number / amount", "How many legs has a spider got?"],
                          ["How long / How far / How fast / How tall", "length / distance / speed / height", "How fast can a cheetah run?"]],
                    colors=["amber", "teal", "white"]),
        pattern=[
            ["?", ["How fast", "x"], "can", "a cheetah run?"],
            ["?", ["How long", "x"], "is", "the Euphrates?"],
            ["?", ["Which", "x"], "is", "bigger: a whale or an elephant?"],
            ["?", ["Who", "x"], ["discovered", "v"], "the volcano? (Who = subject: no did)"],
        ],
        examples=[
            "{How tall} is a giraffe? — About five metres.",
            "{Why} do camels have humps? — To store fat.",
            "{Which} ocean is the biggest? — The Pacific.",
            "{How far} is Latakia from Damascus? — About 330 kilometres.",
        ],
        ar=[
            "What وWhich بيسألوا عن شي (Which لما في خيارات محدودة).",
            "How + صفة: How fast (قدّيش سريع)، How long (قدّيش طويل)، How far (قدّيش بعيد).",
            "إذا Who هو الفاعل ما منحط did: Who took the photo?، مو Who did take…?",
        ],
        watch=[("How much animals live here?", "How many animals live here?"), ("Who did take this photo?", "Who took this photo?"), ("How long is far Latakia?", "How far is Latakia?")],
        quick="""
## choose: Choose the answer.
___ is the Euphrates? — About 2,800 kilometres. | How long | How far | How many
___ can a cheetah run? — 110 km/h. | How fast | How much | How far
___ animals live in the forest? | How many | How much | What many
""",
        sets="""
## choose: Choose the answer.
___ is Mount Hermon? — About 2,800 metres. | How high | How long | How many
___ is the nearest beach? — In Latakia. | Where | When | Who
___ do camels have humps? — To store fat. | Why | Which | Who
___ people live in the city? | How many | How much | How long
___ water does an elephant drink? | How much | How many | How long
___ is bigger, a whale or an elephant? | Which | Who | Where
___ took this photo of the dolphin? | Who | Which | What
___ is Latakia from Damascus? | How far | How long time | How many
___ does a lion sleep? — About twenty hours a day! | How long | How far | How tall
___ is a giraffe? — About five metres. | How tall | How far | How many
## bank: Use the words.
[How many] legs has a spider got? — Eight.
[How much] does an elephant weigh? — About 6,000 kilos.
[How fast] can a horse run? — About 70 km/h.
[How far] is the desert from here? — 200 kilometres.
[How long] is the river? — 2,800 kilometres.
[Which] animal is the biggest? — The blue whale.
[Why] do snakes put out their tongues? — To smell.
[Who] took this fantastic photo? — My brother.
## transform: Write the question.
The Euphrates is 2,800 km long. (How long) => How long is the Euphrates?
A cheetah can run at 110 km/h. (How fast) => How fast can a cheetah run?
Latakia is 330 km from Damascus. (How far) => How far is Latakia from Damascus?
A spider has got eight legs. (How many legs) => How many legs has a spider got? | How many legs does a spider have?
An elephant weighs 6,000 kg. (How much) => How much does an elephant weigh?
Hadi is one metre eighty. (How tall) => How tall is Hadi?
Kenji took the photo. (Who) => Who took the photo?
Camels have humps to store fat. (Why) => Why do camels have humps?
## fix: Find and fix the mistake.
[How much>How many] animals live in the forest?
[Who did take>Who took] this photo?
How [long>far] is Beirut from Damascus?
[How many>How much] water do camels drink?
[What>Which] is bigger: a whale or an elephant?
How [fast>tall] is a giraffe? — Five metres.
Why [camels have>do camels have] humps?
How long [the river is>is the river]?
## order: Put the words in order.
How fast can a cheetah run?
How long is the Euphrates?
Which ocean is the biggest?
Who took this photo?
How far is the beach?
Why do camels have humps?
How many people live in Damascus?
How tall is a giraffe?
""",
    ),
    dict(
        id="g2",
        title="a lot of, a few, a little, not much, not many",
        visual=dict(type="jars", left=dict(title="countable (fish, trees)", items=["a lot of fish", "a few trees", "not many animals"]),
                    right=dict(title="uncountable (water, rain)", items=["a lot of water", "a little rain", "not much grass"])),
        pattern=[
            ["+", "There are", ["a lot of", "v"], "fish in the lake."],
            ["+", "There are", ["a few", "x"], "trees in the desert. (countable)"],
            ["+", "There's", ["a little", "x"], "water. (uncountable)"],
            ["−", "There aren't", ["many", "n"], "animals. / There isn't much rain."],
        ],
        examples=[
            "There are {a lot of} dolphins near Arwad in summer.",
            "There are {a few} trees in the desert, but {not many}.",
            "Camels need only {a little} water.",
            "There {isn't much} rain in the desert.",
        ],
        ar=[
            "a lot of = كتير، مع العدود والما بينعد.",
            "a few و not many للأشياء اللي منعدها (trees)، و a little و not much للي ما منعدها (water).",
            "a few = شوية (كفاية)، not many = مو كتير.",
        ],
        watch=[("a few water", "a little water"), ("There isn't many rain.", "There isn't much rain."), ("a little trees", "a few trees")],
        quick="""
## choose: Choose the answer.
There's ___ water in the bottle. | a little | a few | many
There are ___ trees in the desert. | a few | a little | much
There isn't ___ rain in summer. | much | many | a few
""",
        sets="""
## choose: Choose the answer.
There are ___ fish in this lake. (a big number) | a lot of | a little | much
Camels need ___ water. (a small amount) | a little | a few | many
There are ___ trees in the desert. (a small number) | a few | a little | much
There isn't ___ grass in the desert. | much | many | a few
There aren't ___ wild animals near the city. | many | much | a little
I've got ___ friends in London. | a few | a little | much
There's ___ snow on Mount Hermon in winter. | a lot of | many | a few
We haven't got ___ time. | much | many | a few
There aren't ___ dolphins in winter. | many | much | a little
Add ___ salt to the soup. | a little | a few | many
## choose: much or many?
There aren't ___ camels here. | many | much
There isn't ___ water in the river. | much | many
How ___ elephants are there? | many | much
How ___ rain is there in summer? | much | many
There aren't ___ volcanoes in Syria. | many | much
There isn't ___ wildlife in the city. | much | many
How ___ fish are in the lake? | many | much
I haven't got ___ money. | much | many
## gap: Write a few or a little.
There are [a few] trees near the oasis.
There's [a little] water in the bottle.
I've got [a few] photos of the dolphins.
Put [a little] sugar in my coffee, please.
We saw [a few] camels in the desert.
There's [a little] snow on the mountains.
There are [a few] snakes in the valley.
Can I have [a little] milk in my tea?
## fix: Find and fix the mistake.
There's a [few>little] water.
There aren't [much>many] animals.
There isn't [many>much] rain.
I've got a [little>few] friends in Toronto.
How [much>many] trees are there?
There are [a lot>a lot of] fish.
We haven't got [many>much] time.
There are a [little>few] camels.
## order: Put the words in order.
There are a lot of fish in the lake.
There isn't much rain in the desert.
There are a few trees.
Camels need only a little water.
There aren't many wild animals here.
How many dolphins did you see?
We haven't got much time.
There's a little snow on the mountain.
""",
    ),
    dict(
        id="g3",
        title="Big numbers",
        visual=dict(type="table", head=["number", "we say"],
                    rows=[["505", "five hundred {and} five"], ["5.5", "five {point} five"], ["50,000", "fifty thousand"],
                          ["500,000", "five hundred thousand"], ["5,000,000", "five million"], ["5,000,000,000", "five billion"]],
                    colors=["amber", "teal"], cap="No -s: five million (not five millions)"),
        pattern=[
            ["", "505 =", ["five hundred and five", "v"], ""],
            ["", "5.5 =", ["five point five", "v"], ""],
            ["", "2,500,000 =", ["two million, five hundred thousand", "x"], ""],
        ],
        examples=[
            "An elephant weighs about {six thousand} kilograms.",
            "A blue whale can be {thirty} metres long.",
            "About {eight billion} people live in the world.",
            "The baby weighed {three point five} kilos.",
        ],
        ar=[
            "بالإنكليزي منقول and بعد hundred: five hundred and five.",
            "الفاصلة العشرية منقولها point: 5.5 = five point five.",
            "million و thousand و billion ما بياخدوا s بعد الرقم: five million.",
        ],
        watch=[("five millions", "five million"), ("five hundred five", "five hundred and five"), ("five comma five (5.5)", "five point five")],
        quick="""
## choose: Choose the answer.
505 = ___ | five hundred and five | five hundreds five | fifty-five
5.5 = ___ | five point five | five comma five | fifty-five
5,000,000 = ___ | five million | five millions | five billion
""",
        sets="""
## choose: Choose the answer.
50,000 = ___ | fifty thousand | five thousand | fifty thousands
500,000 = ___ | five hundred thousand | fifty thousand | five million
5,000,000,000 = ___ | five billion | five million | five thousand million
2.5 = ___ | two point five | two comma five | twenty-five
1,200 = ___ | one thousand, two hundred | twelve thousand | one hundred two
330 = ___ | three hundred and thirty | thirty-three | three thousand thirty
8,000,000 = ___ | eight million | eight millions | eighty million
6,000 = ___ | six thousand | six thousands | sixty hundred
## numbers: Write the number in words.
505 => five hundred and five
5.5 => five point five
50,000 => fifty thousand
500,000 => five hundred thousand
5,000,000 => five million
5,000,000,000 => five billion
110 => a hundred and ten | one hundred and ten
3.5 => three point five
## numbers: Write the number in figures.
two thousand => 2,000 | 2000
seventy point five => 70.5
three million => 3,000,000 | 3000000
four hundred and twelve => 412
one point eight => 1.8
sixty thousand => 60,000 | 60000
nine billion => 9,000,000,000 | 9000000000
two hundred and fifty => 250
## fix: Find and fix the mistake.
There are five [millions>million] people.
It's five hundred [five>and five] kilometres.
The baby weighed three [comma>point] five kilos.
Two [thousands>thousand] people came.
About eight [billions>billion] people live in the world.
It costs one hundred [twenty>and twenty] pounds.
Ten [thousands>thousand] tourists visit every year.
The river is two [points>point] five kilometres wide.
## match: Match the number and the words.
505 = five hundred and five
5.5 = five point five
50,000 = fifty thousand
500,000 = five hundred thousand
5,000,000 = five million
5,000,000,000 = five billion
1,500 = one thousand, five hundred
15.5 = fifteen point five
""",
    ),
]

CLASSROOM = dict(
    phrases=["I'd like to ask about …", "Which one is more common?", "Is there another way to say …?", "How do you pronounce this word?",
             "Sorry, I didn't hear you.", "Can you write it on the board, please?", "Check with your partner."],
    order="""
S: I'd like to ask about big numbers.
T: Sure. What's your question?
S: How do you pronounce 5,000,000,000?
T: Five billion.
S: Sorry, I didn't hear you. Can you write it on the board, please?
T: Of course. Now check with your partner.
""",
)

READING = dict(
    title="The amazing camel",
    text="""Camels are some of the most amazing animals in the world. There are about thirty-five million camels on Earth, and a lot of them live in deserts in Africa and Asia. In Syria, there were a lot of camels in the desert near Palmyra, and they were important working animals for hundreds of years.

How do camels live in the desert? There isn't much water and there aren't many plants there. Camels can drink about a hundred litres of water in ten minutes, and then they can walk for days. Their humps don't have water in them — they have fat. A camel can carry about two hundred kilograms, and it can run at sixty-five kilometres per hour for a short time.

Which camels have one hump? Arabian camels. Which have two? Bactrian camels from Central Asia. How long do camels live? About forty or fifty years. Not many animals are as strong as the camel!""",
    qs="""
## tf: True or false?
Camels' humps have water in them. | F @ Their humps don't have water in them — they have fat
There isn't much water in the desert. | T @ There isn't much water
Camels were important working animals in Syria. | T @ they were important working animals for hundreds of years
Arabian camels have two humps. | F @ Which camels have one hump? Arabian camels
Camels live about forty or fifty years. | T @ About forty or fifty years
## choose: Choose the answer.
How many camels are there on Earth? | about thirty-five million | about five hundred thousand | about five billion @ There are about thirty-five million camels on Earth
How much can a camel carry? | about two hundred kilograms | about two thousand kilograms | about twenty kilograms @ A camel can carry about two hundred kilograms
## gap: Write one word.
Camels can drink about a [hundred] litres of water in ten minutes. @ Camels can drink about a hundred litres of water in ten minutes
""",
)

DIALOGUE = dict(
    title="A quiz night",
    intro="A nature quiz at a café in Baramkeh. Maya is the quiz host.",
    task="gaps",
    lines="""
Maya: Question one. How [fast] can a cheetah run?
Hadi: About 110 kilometres per hour!
Maya: Correct! Question two. How [many] legs has a spider got?
Layla: Eight.
Maya: Yes! Question three. Which is [bigger]: an elephant or a blue whale?
Hadi: A blue whale. It weighs about a hundred and fifty [thousand] kilos.
Maya: Right! Last question: how [much] water does a camel drink in ten minutes?
Layla: About a [hundred] litres!
""",
)

WQ = """
About 110 km/h. (How fast / a cheetah / run) => How fast can a cheetah run? | How fast does a cheetah run?
2,800 kilometres. (How long / the Euphrates) => How long is the Euphrates?
Eight. (How many legs / a spider / have) => How many legs does a spider have? | How many legs has a spider got?
About 6,000 kg. (How much / an elephant / weigh) => How much does an elephant weigh?
The blue whale. (Which animal / the biggest) => Which animal is the biggest? | What animal is the biggest?
To store fat. (Why / camels / have humps) => Why do camels have humps?
About 330 kilometres. (How far / Latakia / from Damascus) => How far is Latakia from Damascus?
My brother. (Who / take / this photo) => Who took this photo?
"""

WRITING = [
    dict(task="Write a short fact file about an animal or a place in nature in Syria or the world. Use numbers and quantity words.",
         tip="Use big numbers, a lot of / a few / not much / not many, and some question words as headings. Write 80–120 words.",
         model="The Amazon rainforest\nWhere is it? In South America — most of it is in Brazil.\nHow big is it? About five point five million square kilometres.\nWhat lives there? A lot of wild animals: jaguars, snakes, monkeys and thousands of types of fish. There are about four hundred billion trees!\nIs there much rain? Yes, a lot. It rains on most days.\nWhy is it important? The trees clean the air for the whole world. But there aren't as many trees as before, because people cut them down.",
         check=["big numbers: fifty kilometres, two thousand", "a lot of / a few / a little", "not much / not many", "question words: Where? How big? Why?"],
         min=80, max=120),
]

CANDO = [
    "ask questions with How fast / How long / How far / How many.",
    "use a lot of, a few, a little, not much and not many.",
    "say big numbers: five hundred and five, five million.",
    "talk about animals and places in nature.",
    "understand a short text with facts and numbers.",
]
