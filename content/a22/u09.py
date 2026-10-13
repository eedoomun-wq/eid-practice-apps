META = dict(n=9, title="Buy and sell", pages="78–87")

BOOK = """
cheap, old, powerful, easy to use, economical, pretty, expensive, stylish, fashionable, uncomfortable, fast, unusual,
gift shop, baker's, bookshop, hairdresser's, butcher's, optician's, clothes shop, pharmacy, dry-cleaner's, post office,
shoe shop, estate agent's,
busy, new, online shopping site, cool, department store, popular, famous, post letters, rent a flat, sunglasses,
second-hand, have a haircut, high, tall, modern
"""

WORDS = """
@Describing things
cheap | not expensive | This phone is cheaper than that one. | | price
old | not new | My laptop is very old. | | age
powerful | strong; it can do a lot | This computer is more powerful than my old one.
easy to use | not difficult to use | This app is really easy to use.
economical | it doesn't use a lot of money or petrol | Small cars are more economical.
pretty | nice to look at | What a pretty necklace!
expensive | it costs a lot of money | Gold is very expensive. | | price
stylish | good-looking and modern | Dima's bag is very stylish. | | style
fashionable | popular now, in fashion | Those trainers are very fashionable. | | style
uncomfortable | not comfortable; it hurts a bit | These shoes are uncomfortable.
fast | quick | My new phone is faster than my old phone.
unusual | different, not normal | It's an unusual gift — I love it!
@Shops
gift shop | a shop that sells presents | We bought a lantern at a gift shop in Bab Touma.
baker's | a shop that sells bread and cakes | I buy bread at the baker's every morning.
bookshop | a shop that sells books | Reem spends hours in the bookshop.
hairdresser's | a shop where you get your hair cut | Dima works at a hairdresser's in Rukn al-Din.
butcher's | a shop that sells meat | The butcher's in Midan sells very good lamb.
optician's | a shop where you test your eyes and buy glasses | I need new glasses, so I need to go to the optician's.
clothes shop | a shop that sells clothes | There are a lot of clothes shops in Sha'lan.
pharmacy | a shop that sells medicine | Nour works in a pharmacy.
dry-cleaner's | a shop that cleans clothes without water | I took my suit to the dry-cleaner's.
post office | a place where you send letters and parcels | The post office is next to the bank.
shoe shop | a shop that sells shoes | I bought these trainers at a shoe shop in Hamra Street.
estate agent's | an office that sells and rents houses and flats | We found our flat at an estate agent's in Malki.
@Other words
busy | with a lot of people | Souq al-Hamidiyah is busier on Thursday.
new | not old | My phone is new.
online shopping site | a website where you buy things | Online shopping sites are very popular.
cool | fashionable and nice (informal) | Your sunglasses are really cool!
department store | a very big shop with a lot of departments | Harrods is a famous department store in London.
popular | a lot of people like it | Bakdash is the most popular ice cream shop in Damascus.
famous | known by a lot of people | Souq al-Hamidiyah is very famous.
post letters | to send letters by post | My grandfather posts letters every week.
rent a flat | to pay money every month to live in a flat | They rent a flat in Jaramana.
sunglasses | dark glasses for the sun | I need new sunglasses for the beach.
second-hand | not new; another person had it before | I bought a second-hand bike.
have a haircut | to get your hair cut | I had a haircut yesterday.
high | far from the ground | Qasioun is very high.
tall | (a person or building) big from bottom to top | Hadi is taller than his brother.
modern | new and up to date | Dubai has a lot of modern buildings.
"""

ODD = """
baker's, butcher's, pharmacy, *sunglasses | Sunglasses: not a shop.
cheaper, bigger, faster, *the oldest | The oldest: a superlative.
the best, the worst, the most expensive, *better | Better: a comparative.
stylish, fashionable, cool, *uncomfortable | Uncomfortable: a bad word.
bookshop, shoe shop, gift shop, *post letters | Post letters: an action.
high, tall, big, *economical | Economical: not about size.
"""

GRAMMAR = [
    dict(
        id="g1",
        title="Comparatives",
        visual=dict(type="bars", items=[["Homs", 3, "big"], ["Aleppo", 5, "bigger"], ["Damascus", 7, "bigger than Aleppo"]],
                    cap="short: cheap → cheap{er} · big → bi{gger} · easy → eas{ier} · long: {more} expensive · good → {better}, bad → {worse}"),
        pattern=[
            ["", "This phone", "is", ["cheaper than", "v"], "that phone."],
            ["", "Damascus", "is", ["bigger than", "v"], "Homs."],
            ["", "Gold", "is", ["more expensive than", "v"], "silver."],
            ["", "This café", "is", ["better than", "x"], "that café."],
        ],
        examples=[
            "My new phone is {faster than} my old one.",
            "Second-hand clothes are {cheaper than} new clothes.",
            "This bag is {more stylish than} that one.",
            "The trains in Tokyo are {better than} our buses!",
        ],
        ar=[
            "للمقارنة بين شيئين: الصفة + er + than: cheaper than (أرخص من).",
            "الصفات الطويلة منحط قبلها more: more expensive than (أغلى من).",
            "big → bigger (منضاعف الحرف)، easy → easier، و good → better، bad → worse.",
            "انتبه: ما منقول more cheaper — بس cheaper.",
        ],
        watch=[("more cheaper", "cheaper"), ("expensiver", "more expensive"), ("bigger from Homs", "bigger than Homs"), ("gooder", "better")],
        quick="""
## choose: Choose the answer.
This phone is ___ than that one. | cheaper | more cheap | cheapest
Gold is ___ than silver. | more expensive | expensiver | most expensive
This café is ___ than the old one. | better | gooder | more good
""",
        sets="""
## choose: Choose the answer.
My new laptop is ___ than my old one. | faster | more fast | fastest
Damascus is ___ than Homs. | bigger | biger | more big
This dress is ___ than that one. | more expensive | expensiver | most expensive
Online shopping is ___ than going to the shops. | easier | more easy | easyer
The weather today is ___ than yesterday. | worse | badder | more bad
Hadi is ___ than his brother. | taller | more tall | tallest
This bag is ___ than mine. | more stylish | stylisher | more stylisher
Second-hand books are ___ than new books. | cheaper | more cheap | cheapest
Electric cars are ___ than old cars. | more economical | economicaler | most economical
My grandmother's food is ___ than restaurant food! | better | more good | best
## gap: Write the comparative.
This shop is [cheaper] than that shop. (cheap)
Dubai is [hotter] than London. (hot)
English is [easier] than Chinese for me. (easy)
This phone is [more powerful] than my old one. (powerful)
Aleppo is [older] than many European cities. (old)
Your sunglasses are [cooler] than mine. (cool)
The Tube in London is [busier] than our buses! (busy)
His new job is [better] than his old one. (good)
## transform: Write a sentence with than.
my phone / your phone / new => My phone is newer than your phone.
Tokyo / London / big => Tokyo is bigger than London.
gold / silver / expensive => Gold is more expensive than silver.
the souq / the department store / busy => The souq is busier than the department store.
this chair / that chair / uncomfortable => This chair is more uncomfortable than that chair.
Mount Everest / Mont Blanc / high => Mount Everest is higher than Mont Blanc.
online shopping / the souq / easy => Online shopping is easier than the souq.
my old bike / my new bike / bad => My old bike is worse than my new bike.
## fix: Find and fix the mistake.
This phone is [more cheaper>cheaper] than that one.
Gold is [expensiver>more expensive] than silver.
Damascus is bigger [from>than] Homs.
This café is [gooder>better] than the old one.
My bag is [more big>bigger] than yours.
Today is [badder>worse] than yesterday.
This app is [easyer>easier] to use.
He's taller [that>than] his father.
## order: Put the words in order.
This phone is cheaper than that one.
Damascus is bigger than Homs.
Gold is more expensive than silver.
My new laptop is faster than my old one.
This café is better than the old one.
Online shopping is easier than going to the shops.
Is Aleppo older than Damascus?
Second-hand books are cheaper than new books.
""",
    ),
    dict(
        id="g2",
        title="Superlatives",
        visual=dict(type="bars", items=[["Bakdash", 9, "the most popular"], ["café A", 6, ""], ["café B", 4, ""]],
                    cap="short: cheap → {the} cheap{est} · big → {the} bi{ggest} · long: {the most} expensive · good → {the best}, bad → {the worst}"),
        pattern=[
            ["", "This is", ["the cheapest", "v"], "phone in the shop."],
            ["", "Bakdash is", ["the most popular", "v"], "ice cream shop in Damascus."],
            ["", "It was", ["the best", "x"], "day of my life."],
            ["", "That was", ["the worst", "n"], "film of the year."],
        ],
        examples=[
            "Souq al-Hamidiyah is {the busiest} souq in Damascus.",
            "This is {the most expensive} watch in the shop.",
            "My grandmother makes {the best} kibbeh in the family.",
            "Qasioun is {the highest} place in Damascus.",
        ],
        ar=[
            "لنقول 'الأكتر' من مجموعة: the + الصفة + est: the cheapest (الأرخص).",
            "الصفات الطويلة: the most + الصفة: the most expensive (الأغلى).",
            "good → the best، و bad → the worst.",
            "لا تنسَ the: the biggest، مو biggest لحالها.",
        ],
        watch=[("the most cheapest", "the cheapest"), ("He's the taller in the class.", "He's the tallest in the class."), ("Bakdash is most popular.", "Bakdash is the most popular.")],
        quick="""
## choose: Choose the answer.
This is ___ phone in the shop. | the cheapest | the most cheap | cheaper
It was ___ film of the year. | the best | the goodest | better
That's ___ watch in the shop. | the most expensive | the expensivest | more expensive
""",
        sets="""
## choose: Choose the answer.
Bakdash is ___ ice cream shop in Damascus. | the most popular | the popularest | more popular
This is ___ bag in the shop. | the cheapest | the most cheap | the cheaper
Hadi is ___ person in our family. | the tallest | the most tall | taller
It was ___ day of my life! | the best | the goodest | the most good
That was ___ meal of the week. It was awful! | the worst | the baddest | the most bad
This is ___ phone on the online shopping site. | the most powerful | the powerfulest | more powerful
Souq al-Hamidiyah is ___ place in the city on Thursday. | the busiest | the busyest | the most busy
Qasioun is ___ place in Damascus. | the highest | the most high | higher
This shop has ___ clothes in Sha'lan. | the most fashionable | the fashionablest | more fashionable
Dima has ___ haircut in the class! | the coolest | the most cool | cooler
## gap: Write the superlative.
This is [the cheapest] hotel in the city. (cheap)
Ramadan nights are [the busiest] nights in the souq. (busy)
This is [the most comfortable] chair in the house. (comfortable)
My grandfather is [the oldest] man in our street. (old)
That was [the best] film of the year. (good)
It's [the biggest] department store in Dubai. (big)
This is [the most unusual] gift in the shop. (unusual)
That was [the worst] meal of my life! (bad)
## transform: Write a sentence with the superlative.
Bakdash / popular / ice cream shop in Damascus => Bakdash is the most popular ice cream shop in Damascus.
Hadi / tall / person in his family => Hadi is the tallest person in his family.
this watch / expensive / in the shop => This watch is the most expensive in the shop. | This watch is the most expensive watch in the shop.
Thursday / busy / day in the souq => Thursday is the busiest day in the souq.
my grandmother / good / cook in the family => My grandmother is the best cook in the family.
Qasioun / high / place in Damascus => Qasioun is the highest place in Damascus.
this phone / cheap / on the site => This phone is the cheapest on the site. | This phone is the cheapest phone on the site.
that / bad / film of the year => That was the worst film of the year. | That is the worst film of the year.
## fix: Find and fix the mistake.
It's [the most cheapest>the cheapest] phone.
He's [the taller>the tallest] in the class.
Bakdash is [most popular>the most popular].
It was the [goodest>best] day of my life.
This is [the expensivest>the most expensive] watch.
That was the [baddest>worst] meal.
Damascus is [the older>the oldest] city in the world? Maybe!
It's [biggest>the biggest] store in Dubai.
## order: Put the words in order.
This is the cheapest phone in the shop.
Bakdash is the most popular ice cream shop.
It was the best day of my life.
Hadi is the tallest person in his family.
That was the worst film of the year.
Thursday is the busiest day in the souq.
What's the most expensive thing in the shop?
Qasioun is the highest place in Damascus.
""",
    ),
    dict(
        id="g3",
        title="Describing objects",
        visual=dict(type="chips", groups=[
            dict(title="price", color="amber", items=["cheap", "expensive", "economical", "second-hand"]),
            dict(title="look", color="purple", items=["pretty", "stylish", "fashionable", "cool", "modern", "unusual"]),
            dict(title="how it works", color="teal", items=["fast", "powerful", "easy to use", "uncomfortable"]),
        ], cap="It's + adjective · It's a / an + adjective + noun"),
        pattern=[
            ["", "It's", ["stylish.", "v"], ""],
            ["", "It's", ["a stylish", "v"], "bag."],
            ["", "It's", ["easy to use.", "v"], ""],
            ["", "They're", ["very fashionable", "v"], "sunglasses."],
        ],
        examples=[
            "It's a {cheap} phone, but it's {fast} and {easy to use}.",
            "I bought a {second-hand} bike. It's old, but it's {economical}.",
            "Your sunglasses are really {cool}!",
            "These shoes are {pretty}, but they're {uncomfortable}.",
        ],
        ar=[
            "الصفة بتجي قبل الاسم بالإنكليزي: a stylish bag (شنتاية أنيقة)، مو a bag stylish.",
            "الصفة ما بتاخد s بالجمع: expensive shoes، مو expensives shoes.",
            "economical يعني ما بيصرف كتير، و second-hand يعني مستعمل.",
        ],
        watch=[("a bag stylish", "a stylish bag"), ("expensives shoes", "expensive shoes"), ("It's a easy phone to use.", "It's an easy phone to use.")],
        quick="""
## choose: Choose the answer.
It's ___ bag. | a stylish | a bag stylish | stylish a
These shoes are ___. | expensive | expensives | an expensive
Not new: | second-hand | modern | powerful
""",
        sets="""
## choose: Choose the right word.
It doesn't cost a lot. It's ___. | cheap | expensive | powerful
It hurts my feet. It's ___. | uncomfortable | stylish | economical
It's very popular now. It's ___. | fashionable | old | second-hand
It can do a lot of things. It's ___. | powerful | pretty | cheap
It doesn't use a lot of petrol. It's ___. | economical | uncomfortable | unusual
Another person had it before me. It's ___. | second-hand | modern | fashionable
It's different, not normal. It's ___. | unusual | cheap | easy to use
It's not difficult. It's ___. | easy to use | powerful | uncomfortable
It's new and up to date. It's ___. | modern | second-hand | old
It costs a lot of money. It's ___. | expensive | cheap | economical
## fix: Find and fix the mistake.
I want [a phone cheap>a cheap phone].
These are [expensives>expensive] shoes.
It's [a bag stylish>a stylish bag].
It's [a>an] unusual gift.
They're very [fashionables>fashionable].
I bought [a car second-hand>a second-hand car].
It's a [use easy>easy-to-use|easy to use] app.
She's got [a dress pretty>a pretty dress].
## match: Match the opposites.
cheap = expensive
old = new
uncomfortable = comfortable
slow = fast
modern = old-fashioned
easy to use = difficult to use
second-hand = brand new
unusual = normal
## order: Put the words in order.
It's a stylish bag.
These shoes are uncomfortable.
I bought a second-hand bike.
Your sunglasses are really cool.
It's cheap but very fast.
This app is easy to use.
She's got a pretty necklace.
They're fashionable trainers.
""",
    ),
    dict(
        id="g4",
        title="Shops",
        visual=dict(type="street", street="Sha'lan Street",
                    top=["baker's", "butcher's", "pharmacy", "bookshop"], bottom=["post office", "optician's", "shoe shop", "hairdresser's"],
                    notes=["You buy bread at the {baker's}.", "You have a haircut at the {hairdresser's}."]),
        pattern=[
            ["", "You buy bread at", ["the baker's.", "v"], ""],
            ["", "You buy medicine at", ["the pharmacy.", "v"], ""],
            ["", "You post letters at", ["the post office.", "v"], ""],
        ],
        examples=[
            "I bought fresh bread at the {baker's}.",
            "Nour gave me medicine at the {pharmacy}.",
            "I need new glasses, so I went to the {optician's}.",
            "We found our flat at an {estate agent's}.",
        ],
        ar=[
            "كتير من أسماء المحلات بتنتهي بـ 's: the baker's (الفرن)، the butcher's (اللحام).",
            "optician's = محل النظارات، estate agent's = مكتب عقاري، dry-cleaner's = دراي كلين.",
            "منقول at the baker's: I buy bread at the baker's.",
        ],
        watch=[("I buy bread at the bakery's.", "I buy bread at the baker's."), ("I bought medicine in the butcher's.", "I bought medicine at the pharmacy."), ("the opticians", "the optician's")],
        quick="""
## choose: Where do you go?
You want bread. | the baker's | the butcher's | the post office
You want medicine. | the pharmacy | the bookshop | the shoe shop
You want a haircut. | the hairdresser's | the optician's | the baker's
""",
        sets="""
## choose: Where do you go?
You want lamb for kibbeh. | the butcher's | the baker's | the bookshop
You need new glasses. | the optician's | the pharmacy | the dry-cleaner's
You want to post a letter. | the post office | the gift shop | the shoe shop
You want to rent a flat. | the estate agent's | the department store | the butcher's
You want a present for a friend. | the gift shop | the post office | the butcher's
Your suit is dirty. | the dry-cleaner's | the bookshop | the optician's
You need trainers. | the shoe shop | the baker's | the pharmacy
You want a new novel. | the bookshop | the butcher's | the optician's
You want a new jacket. | the clothes shop | the post office | the baker's
You need everything in one big building. | the department store | the gift shop | the post office
## match: Match the shop and the thing.
baker's = bread and cakes
butcher's = meat
optician's = glasses
pharmacy = medicine
post office = letters and parcels
bookshop = books
shoe shop = shoes and trainers
estate agent's = flats and houses
## gap: Write the shop.
I bought some bread at the [baker's|bakers|baker's shop].
She works at a [hairdresser's|hairdressers] in Rukn al-Din.
I need medicine. Where's the [pharmacy|chemist's]?
You can post letters at the post [office].
We rented our flat through an estate [agent's|agents].
I took my jacket to the dry-[cleaner's|cleaners].
I bought my glasses at the [optician's|opticians].
I bought a lantern at a [gift] shop in Bab Touma.
## order: Put the words in order.
I buy bread at the baker's.
Where's the nearest pharmacy?
She works at a hairdresser's.
I need to go to the optician's.
We rented our flat through an estate agent's.
The post office is next to the bank.
There's a great bookshop in Sha'lan.
I bought these trainers at a shoe shop.
""",
    ),
]

CLASSROOM = dict(
    phrases=["What's the opposite of …?", "Is there another way to say …?", "Which one is more common?", "I agree. / I don't agree.",
             "What do you think?", "Work in pairs.", "Good luck!"],
    order="""
S: What's the opposite of 'cheap'?
T: Expensive.
S: Is there another way to say 'expensive'?
T: Yes: 'It costs a lot'.
S: Which one is more common?
T: Both are common. Now work in pairs, please.
""",
)

READING = dict(
    title="The souq or online?",
    text="""Is it better to shop in the souq or on an online shopping site? We asked two people.

Kareem, 40, fabric-shop owner, Souq al-Hamidiyah: "The souq is the best place to shop! Online shopping is easier, but the souq is more interesting. You can see the colours, touch the fabric and talk to people. And you can get a better price — I love a bargain! The souq is busier and noisier than a website, but it's more fun. Online, the photos are sometimes prettier than the real thing."

Wei, 29, computer scientist: "For me, online shopping sites are faster and more economical. I bought my laptop online. It was cheaper than in the shops, and it's more powerful than my old one. But I bought my sunglasses at the optician's — the online ones were uncomfortable. And for presents, the gift shops in Bab Touma are the most unusual places in the city."

So which is better? Maybe both!""",
    qs="""
## tf: True or false?
Kareem thinks online shopping is more interesting. | F @ Online shopping is easier, but the souq is more interesting
Kareem loves a bargain. | T @ I love a bargain
Wei thinks online sites are faster. | T @ online shopping sites are faster and more economical
Wei's laptop was more expensive online. | F @ It was cheaper than in the shops
Wei bought his sunglasses online. | F @ I bought my sunglasses at the optician's
## choose: Choose the answer.
What does Kareem say about the souq? | It's busier and noisier, but more fun. | It's quieter than a website. | It's more expensive. @ The souq is busier and noisier than a website, but it's more fun
Where does Wei buy unusual presents? | in the gift shops in Bab Touma | online | at the optician's @ the gift shops in Bab Touma are the most unusual places in the city
## gap: Write one word.
Wei's new laptop is more [powerful] than his old one. @ it's more powerful than my old one
""",
)

DIALOGUE = dict(
    title="Which phone?",
    intro="A phone shop in Bab Touma. Hadi helps a customer, Elif.",
    task="gaps",
    lines="""
Elif: Hi. I want a new phone, but not an expensive one.
Hadi: OK. This one is [cheaper] than that one, and it's very easy to use.
Elif: Is it fast?
Hadi: Yes, but that black one is [faster]. It's the most powerful phone in the shop.
Elif: How much is it?
Hadi: It's 2 million pounds. It's [more] expensive than the white one.
Elif: Hmm. Is the white one [second-hand]?
Hadi: No, it's new. It's the [best] phone for the price!
""",
)

WQ = """
The baker's. (Where / you / buy bread) => Where do you buy bread?
Yes, it's cheaper. (this phone / cheaper than that one) => Is this phone cheaper than that one?
Bakdash. (What / the most popular ice cream shop in Damascus) => What's the most popular ice cream shop in Damascus? | What is the most popular ice cream shop in Damascus? | Which is the most popular ice cream shop in Damascus?
Hadi. (Who / the tallest in your family) => Who's the tallest in your family? | Who is the tallest in your family? | Who is the tallest person in your family?
At the optician's. (Where / you / buy your glasses) => Where did you buy your glasses? | Where do you buy your glasses?
2 million pounds. (How much / the black phone) => How much is the black phone? | How much does the black phone cost?
Yes, I did. It was second-hand. (you / buy a bike) => Did you buy a bike?
Online. (Where / you / buy your laptop) => Where did you buy your laptop?
"""

WRITING = [
    dict(task="Compare two shops or two shopping places in your town (for example, a souq and a shopping centre). Which is better for you?",
         tip="Use comparatives (cheaper, more interesting) and superlatives (the best, the most popular). Write 80–120 words.",
         model="I usually shop in two places: the street market in Jaramana and the new shopping centre in Mezzeh. The street market is cheaper and noisier, and the fruit is fresher. The shopping centre is more comfortable and more modern, but it's more expensive. It's also quieter and cleaner. For clothes, the shopping centre is better because the shops are more fashionable. But for food, the market is the best place in my area. The most fun day is Friday, when the market is the busiest!",
         check=["comparatives: cheaper than, more modern than", "superlatives: the best, the most popular", "better / worse / the best / the worst", "shop words: baker's, clothes shop…"],
         min=80, max=120),
]

CANDO = [
    "compare two things: cheaper than, more expensive than.",
    "use superlatives: the cheapest, the most popular, the best.",
    "describe objects: stylish, economical, easy to use.",
    "name shops: the baker's, the pharmacy, the optician's.",
    "talk about shopping in the souq and online.",
]
