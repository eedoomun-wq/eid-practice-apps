META = dict(n=2, title="People and things", pages="16–23")

BOOK = """
bag, key, bottle of water, memory stick, camera, mobile phone, coin, packet of chewing gum, credit card, photo,
dictionary, tissue, glasses, wallet, identity card, watch,
boyfriend, husband, brother, mother, cousin, nephew, grandchildren, parents, grandmother, son, grandparents, uncle,
grandson,
here, information, fantastic, interview, favourite person, lovely, fictional character, there
"""

WORDS = """
@Things in your bag
bag | you carry things in it | My bag is really heavy today!
key | it opens a door | Have you got your house key?
bottle of water | water in a plastic bottle | I've got a bottle of water in my bag.
memory stick | a small thing for computer files | My homework is on this memory stick.
camera | you take photos with it | Kenji has got a very expensive camera.
mobile phone | a phone you carry with you | Have you got a mobile phone?
coin | money made of metal | These coins are old Syrian pounds.
packet of chewing gum | small pieces of sweet gum in a packet | Have you got a packet of chewing gum?
credit card | a plastic card for paying | I haven't got a credit card.
photo | a picture from a camera | This is a photo of my grandparents.
dictionary | a book with words and their meanings | Is that your dictionary?
tissue | soft paper for your nose | Have you got a tissue?
glasses | you wear them to see better | My grandfather's glasses are on the table.
wallet | a small case for money and cards | Hadi's wallet is in his pocket.
identity card | a card with your photo, name and number | Have you got your identity card?
watch | a small clock you wear on your wrist | My watch is from my father.
@Family
boyfriend | a man you love, but you aren't married | Her boyfriend is a doctor. | | fam-m
husband | the man you are married to | Mei's husband is Japanese. | | fam-m
brother | a boy or man with the same parents as you | My brother's name is Bassel. | | fam-m
mother | your female parent | Um Khaled's son is Khaled — she's his mother. | | fam-f
cousin | the child of your uncle or aunt | Tala is my cousin. Her father is my uncle. | | fam
nephew | the son of your brother or sister | My nephew Karam is two. | | fam-m
grandchildren | the children of your son or daughter | Abu Firas has got five grandchildren. | | fam
parents | your mother and father | My parents are from Hama. | | fam
grandmother | the mother of your mother or father | My grandmother's kitchen is lovely. | | fam-f
son | a male child | Walid's son is Ziad. | | fam-m
grandparents | the parents of your parents | My grandparents have got a house in Sarouja. | | fam
uncle | the brother of your mother or father | My uncle is a lawyer. | | fam-m
grandson | the son of your son or daughter | Abu Salim's grandson is a student. | | fam-m
@Other words
here | in this place | Your keys are here, on the table. | | place
information | facts about something | The information is on the website.
fantastic | very, very good | This photo is fantastic! | | good
interview | a meeting with questions, for a job or for TV | My job interview is tomorrow.
favourite person | the person you like best | My favourite person is my grandmother.
lovely | very nice | What a lovely photo! | | good
fictional character | a person from a book or film, not real | Harry Potter is a fictional character.
there | in that place | The café is there, next to the bank. | | place
"""

ODD = """
key, wallet, coin, *uncle | Uncle: a person.
glasses, watch, camera, *cousin | Cousin: a person.
nephew, son, grandson, *mother | Mother: a woman.
this, these, *those, here | Those: far.
fantastic, lovely, great, *information | Information: a noun.
have got, has got, haven't got, *has | Has: not 'have got'.
memory stick, mobile phone, camera, *tissue | Tissue: not technology.
"""

GRAMMAR = [
    dict(
        id="g1",
        title="this / that / these / those",
        visual=dict(type="hands", obj="book", labels=dict(this="This is my dictionary.", these="These are my keys.",
                                                         that="That's my brother's car.", those="Those are my glasses.")),
        pattern=[
            ["", ["This", "v"], "is", "my bag. (here)"],
            ["", ["These", "v"], "are", "my keys. (here)"],
            ["", ["That", "x"], "is", "your camera. (there)"],
            ["", ["Those", "x"], "are", "your coins. (there)"],
        ],
        examples=[
            "{This} is my identity card.",
            "Are {these} your glasses? — Yes, they are. Thanks!",
            "{That} man is my uncle.",
            "{Those} photos are lovely.",
        ],
        ar=[
            "this (هاد) و these (هدول) للقريب، that (هداك) و those (هدوليك) للبعيد.",
            "this و that لشي واحد مع is، و these و those لأكتر من شي مع are.",
            "منستعمل This is… لنعرّف شخص: This is my cousin, Tala.",
        ],
        en=[
            "this / these = here, near you. that / those = there.",
            "One thing → this / that + is.",
            "More than one → these / those + are.",
            "This is… for people too: This is my cousin, Tala.",
        ],
        watch=[("This keys are mine.", "These keys are mine."), ("Those is my car.", "That's my car."), ("These are my glass.", "These are my glasses.")],
        quick="""
## choose: Choose the answer.
___ is my wallet. (here) | This | These | Those
___ are my keys. (there) | Those | That | This
Are ___ your glasses? (here) | these | this | that
""",
        sets="""
## choose: Choose the answer.
___ is my camera. (here) | This | These | Those
___ are my coins. (here) | These | This | That
___ woman is my aunt. (there) | That | Those | These
Is ___ your phone? (here) | this | these | those
___ are my cousins. (there) | Those | That | This
Are ___ your tissues? (here) | these | this | that
___ photo is lovely. (there) | That | Those | These
___ keys are for the car. (here) | These | This | That
Is ___ your brother? (there) | that | those | these
___ glasses are expensive! (there) | Those | That | This
## gap: Write this, that, these or those.
[This] is my dictionary. (here)
[Those] are my parents. (there)
Is [that] your bag? (there)
[These] coins are old. (here)
[That] is my uncle's shop. (there)
[These] photos are from Vienna. (here)
Are [those] your keys? (there)
[This] is my cousin, Tala. (here)
## fix: Find and fix the mistake.
[This>These] are my keys.
[Those>That] is my car.
These [is>are] my glasses.
[That>Those] are my coins.
Is [these>this] your wallet?
These are my [glass>glasses]. They're new. #id=a21u2-299d8d0
[These>This] is my nephew.
Those [is>are] lovely photos.
## order: Put the words in order.
This is my identity card.
Are these your keys?
That's my uncle's car.
Those are my grandparents.
Is this your memory stick?
These coins are very old.
Is that your camera?
These are lovely photos.
""",
    ),
    dict(
        id="g2",
        title="possessive 's",
        visual=dict(type="tree", gen=[
            [dict(name="Abu Salim", cap="Ziad's grandfather"), dict(name="Um Ziad", cap="Ziad's grandmother")],
            [dict(name="Walid", cap="Ziad's father"), dict(name="Sana", cap="Walid's wife"), dict(name="Mazen", cap="Ziad's uncle")],
            [dict(name="Ziad", cap="Walid's son"), dict(name="Layla", cap="Ziad's sister"), dict(name="Tala", cap="Ziad's cousin")],
        ], notes=["Ziad is {Walid's} son.", "Mazen is {Ziad's} uncle.", "Tala is {Mazen's} daughter — Ziad's cousin."]),
        pattern=[
            ["", "Walid", ["'s", "v"], "son = Ziad"],
            ["", "my parents", ["'", "v"], "flat (plural owner: s')"],
            ["", "the children", ["'s", "v"], "room (irregular plural: 's)"],
            ["?", ["Whose", "x"], "bag", "is this? — It's Maya's."],
        ],
        examples=[
            "{Maya's} camera is on the table.",
            "Is this {Hadi's} wallet? — Yes, it is.",
            "My {grandparents'} house is in Sarouja.",
            "{Whose} keys are these? — They're {Kareem's}.",
        ],
        ar=[
            "للملكية منحط 's بعد صاحب الشي: Maya's camera = كاميرا مايا.",
            "إذا الصاحب جمع منتهي بـ s منحط بس ': my parents' house.",
            "Whose…? يعني لمين؟ Whose keys are these?",
        ],
        en=[
            "Name + 's = it is his or hers: Maya's camera.",
            "More than one, with s at the end: add only ' → my parents' house.",
            "Whose…? = which person's? Whose keys are these? — Kareem's.",
        ],
        watch=[("the camera of Maya", "Maya's camera"), ("Hadi wallet", "Hadi's wallet"), ("my parent's house (two parents)", "my parents' house")],
        quick="""
## choose: Choose the answer.
This is ___ camera. | Maya's | Maya | Mayas'
Mazen is Ziad's ___. | uncle | nephew | son
My ___ flat is in Malki. (two parents) | parents' | parent's | parents
""",
        sets="""
## choose: Look at the family tree. Choose the answer.
Walid is Ziad's ___. | father | uncle | grandfather
Layla is Ziad's ___. | sister | cousin | mother
Mazen is Layla's ___. | uncle | father | brother
Tala is Ziad's ___. | cousin | sister | nephew
Abu Salim is Layla's ___. | grandfather | father | uncle
Sana is Walid's ___. | wife | sister | daughter
Ziad is Mazen's ___. | nephew | son | cousin
Ziad and Layla are Abu Salim's ___. | grandchildren | children | parents
Um Ziad is Tala's ___. | grandmother | mother | aunt
Abu Salim and Um Ziad are Tala's ___. | grandparents | parents | uncles
## gap: Write the name with 's.
This is [Maya's] camera. (Maya)
[Hadi's] wallet is in his bag. (Hadi)
[Kareem's] shop is in the souq. (Kareem)
That's [Rana's] dictionary. (Rana)
Is this [Jad's] mobile phone? (Jad)
[Salma's] watch is new. (Salma)
[Walid's] knafeh is famous. (Walid)
These are [Tareq's] keys. (Tareq)
## fix: Find and fix the mistake.
This is [the camera of Maya>Maya's camera].
[Hadi>Hadi's] wallet is black.
[Whos>Whose] keys are these?
My [parent's>parents'] house is in Midan. (two parents)
Is this [Rana>Rana's] bag?
[The name of my uncle>My uncle's name] is Mazen.
They're [Kareems>Kareem's] coins.
The [childrens'>children's] room is small.
## transform: Write it with 's.
the camera of Maya => Maya's camera
the wallet of Hadi => Hadi's wallet
the son of Walid => Walid's son
the keys of Kareem => Kareem's keys
the café of Hala => Hala's café
the uncle of Ziad => Ziad's uncle
the glasses of my grandfather => my grandfather's glasses | My grandfather's glasses
the identity card of Reem => Reem's identity card
## order: Put the words in order.
This is Maya's camera.
Whose keys are these?
Mazen is Ziad's uncle.
My parents' flat is in Malki.
Is this Hadi's wallet?
Tala is Ziad's cousin.
Hala's café is lovely.
My grandmother's kitchen is big.
""",
    ),
    dict(
        id="g3",
        title="have got / has got",
        visual=dict(type="table", head=["", "+", "−", "?"],
                    rows=[["I / you / we / they", "'ve got", "haven't got", "Have you got…?"],
                          ["he / she / it", "'s got", "hasn't got", "Has she got…?"]],
                    colors=["teal", "purple", "coral", "amber"], cap="have got = have (for things, family, features)"),
        pattern=[
            ["+", "I", ["'ve got", "v"], "a camera."],
            ["+", "She", ["'s got", "v"], "two brothers."],
            ["−", "We", ["haven't got", "n"], "a car."],
            ["?", ["Has", "v"], "he", "got a credit card? — No, he hasn't."],
        ],
        examples=[
            "I{'ve got} a memory stick in my bag.",
            "Abu Firas {has got} five grandchildren.",
            "Hadi {hasn't got} his wallet. It's at home!",
            "{Have} you {got} a tissue? — Yes, {I have}.",
        ],
        ar=[
            "have got يعني 'عندي': I've got a car = عندي سيارة.",
            "مع he / she / it منقول has got: She's got a camera.",
            "للنفي: haven't got / hasn't got، وللسؤال: Have you got…? Has she got…?",
            "انتبه: She's got = She has got، مو She is got.",
        ],
        en=[
            "have got = have: I've got a car.",
            "He / she / it → has got: She's got a camera.",
            "Negative: haven't got / hasn't got. Question: Have you got…?",
            "She's got = She has got. (not: She is got.)",
        ],
        watch=[("She have got a car.", "She's got a car."), ("I haven't a car.", "I haven't got a car."), ("Have you got a pen? — Yes, I've got.", "Yes, I have.")],
        quick="""
## choose: Choose the answer.
I ___ got a camera. | 've | 's | am
Maya ___ got two sisters. | 's | 've | is have
___ you got a tissue? | Have | Has | Are
""",
        sets="""
## choose: Choose the answer.
I ___ got a dictionary. | 've | 's | 'm
Hadi ___ got a new phone. | 's | 've | have
We ___ got a car. We go by bus. | haven't | hasn't | aren't
___ she got a credit card? | Has | Have | Is
Have you got my keys? — Yes, I ___. | have | 've | 've got
They ___ got three children. | 've | 's | 're
Has Kareem got a shop? — Yes, he ___. | has | 's | is
My phone ___ got a good camera. | 's | 've | have
I ___ got any coins. Sorry! | haven't | hasn't | aren't
___ your parents got a house? | Have | Has | Are
## gap: Write have, has, haven't or hasn't.
I [have|'ve] got a camera.
Rana [has|'s] got two children.
We [haven't|have not] got a dog.
[Has] Jad got a motorbike?
They [have|'ve] got a lovely flat.
Hadi [hasn't|has not] got his wallet.
[Have] you got a tissue?
My grandmother [has|'s] got blue eyes.
## short: Answer the question.
Have you got a camera? (✓) => Yes, I have.
Has she got a car? (✗) => No, she hasn't. | No, she has not.
Have they got children? (✓) => Yes, they have.
Has Hadi got his keys? (✗) => No, he hasn't. | No, he has not.
Have you got a credit card? (✗) => No, I haven't. | No, I have not.
Has your flat got a balcony? (✓) => Yes, it has.
Have we got homework? (✓) => Yes, we have.
Has Salma got a brother? (✗) => No, she hasn't. | No, she has not. #id=a21u2-d0f6169
## transform: Make the sentence negative (−).
I've got a car. (−) => I haven't got a car. | I have not got a car.
She's got a camera. (−) => She hasn't got a camera. | She has not got a camera.
They've got a dog. (−) => They haven't got a dog. | They have not got a dog.
He's got a credit card. (−) => He hasn't got a credit card. | He has not got a credit card.
We've got a big flat. (−) => We haven't got a big flat. | We have not got a big flat.
Hala's got a sister. (−) => Hala hasn't got a sister. | Hala has not got a sister.
I've got a tissue. (−) => I haven't got a tissue. | I have not got a tissue.
My phone's got a camera. (−) => My phone hasn't got a camera. | My phone has not got a camera.
## transform: Make a question (?).
You've got a pen. (?) => Have you got a pen?
She's got a brother. (?) => Has she got a brother?
They've got a car. (?) => Have they got a car?
He's got the keys. (?) => Has he got the keys?
Your flat has got a balcony. (?) => Has your flat got a balcony?
You've got a dictionary. (?) => Have you got a dictionary?
Rana's got two children. (?) => Has Rana got two children?
We've got time. (?) => Have we got time?
## fix: Find and fix the mistake.
She [have>has|'s] got a camera.
I [haven't>haven't got] a car.
[Have>Has] Hadi got a wallet?
Have you got a tissue? — Yes, I ['ve got>have].
They [has>have|'ve] got two sons.
He [hasn't>hasn't got] a credit card.
[Has>Have] they got a dog?
She [is got>has got|'s got] blue eyes.
""",
    ),
]

CLASSROOM = dict(
    phrases=["Can I borrow your …?", "Do we need to write this?", "Can I have a pen / some paper?", "Sorry, I don't have my book.",
             "How do you spell …?", "Check with your partner.", "Thank you."],
    order="""
S: Excuse me, can I borrow your dictionary?
S: Yes, of course. Here you are.
S: Thank you. How do you spell 'nephew'?
S: N-E-P-H-E-W.
T: Check with your partner, please.
S: Do we need to write this?
""",
)

READING = dict(
    title="What's in your bag?",
    text="""Three people in Souq al-Hamidiyah. One question: "What's in your bag?"

Hala, café owner: "I've got my wallet, my keys and my mobile phone, of course. I've got a packet of chewing gum and some tissues, too. I haven't got a credit card — I only use cash. Oh, and this is a photo of my nephew, Karam. He's two!"

Kenji, tourist: "I've got my camera — it's very important to me. I've got a bottle of water, a small dictionary and my passport. My wife has got the money!"

Abu Salim, taxi driver: "Bag? I haven't got a bag. My keys are here, in my pocket, and my glasses are there, on my head. That's all!" """,
    qs="""
## tf: True or false?
Hala has got a credit card. | F @ I haven't got a credit card
Karam is Hala's nephew. | T @ this is a photo of my nephew, Karam
Kenji has got a camera. | T @ I've got my camera
Kenji has got the money. | F @ My wife has got the money
Abu Salim has got a bag. | F @ I haven't got a bag
## choose: Choose the answer.
How old is Karam? | two | twelve | twenty @ He's two
Where are Abu Salim's glasses? | on his head | in his bag | in his pocket @ my glasses are there, on my head
## gap: Write one word.
Abu Salim's keys are in his [pocket]. @ My keys are here, in my pocket
""",
)

DIALOGUE = dict(
    title="Whose is this?",
    intro="After the English lesson. Rana finds some things on the desks.",
    task="gaps",
    lines="""
Rana: Whose phone is [this]?
Hadi: It's [Jad's]. He's outside.
Rana: And are those your keys, Hadi?
Hadi: No, they [aren't]. My keys are in my bag.
Rana: [Whose] keys are they, then?
Hadi: I think they're Maya's. She's [got] a red key ring.
Rana: OK. And this dictionary? Has Maya [got] a dictionary?
Hadi: Yes, she has. That's her dictionary — her name is [on] it!
""",
)

WQ = """
It's Maya's. (whose / camera) => Whose camera is this? | Whose camera is that? | Whose camera is it? | Whose is this camera?
Yes, I have. Here you are. (you / a tissue) => Have you got a tissue?
No, he hasn't. He's single. (Hadi / children) => Has Hadi got children? | Has Hadi got any children?
They're my keys. (whose / keys / these) => Whose keys are these? | Whose are these keys?
Yes, she has. Two brothers. (Maya / brothers) => Has Maya got brothers? | Has Maya got any brothers?
He's my uncle. (who / that man) => Who's that man? | Who is that man?
No, we haven't. We go by bus. (you / a car) => Have you got a car?
It's my identity card. (what / this) => What's this? | What is this?
"""

WRITING = [
    dict(task="What's in your bag today? Write about five things, and say what you haven't got.",
         tip="Use I've got / I haven't got, this / these, and 's. Write 40–70 words.",
         model="In my bag today, I've got my wallet, my keys and my mobile phone. I've got a bottle of water and a packet of chewing gum. This is my sister's dictionary — mine is at home! I haven't got a credit card, and I haven't got my glasses. They're on my desk.",
         check=["I've got …", "I haven't got …", "this / these + noun", "a name + 's (my sister's …)"],
         min=40, max=70),
    dict(task="Write about your favourite person. Who is it? What has he or she got?",
         tip="Write 40–70 words.",
         model="My favourite person is my grandmother, Um Ziad. She's seventy-two. She's got six grandchildren — I'm her favourite! She's got a lovely house in Sarouja with a courtyard and a lemon tree. She's got beautiful green eyes, and she's always happy.",
         check=["has got / hasn't got", "family words: grandmother, cousin…", "an adjective: lovely, fantastic…"],
         min=40, max=70),
]

CANDO = [
    "use this, that, these and those.",
    "use 's: Maya's camera, my parents' house.",
    "ask 'Whose … is this?'",
    "say what I have got and haven't got.",
    "ask and answer 'Have you got…?'",
]
