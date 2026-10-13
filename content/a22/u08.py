META = dict(n=8, title="Fact or fiction?", pages="70–77")

BOOK = """
happy, boring, enjoyable, romantic, exciting, sad, fast-moving, serious, frightening, slow, funny,
cook dinner for friends, go to a party, go to the theatre, download music, go to the cinema, go for a walk,
play computer games, go to a concert, go out for dinner, read a book, go to a musical, watch a DVD at home,
action film, historical film, adventure film, hit song, lead singer, audience, make phone calls, band, guitarist,
perform, comedy, romance, sci-fi film, drummer, get good reviews, write poems
"""

WORDS = """
@How was it?
happy | with a good feeling; not sad | The film had a happy ending. | | feel
boring | not interesting | The film was long and boring. | | neg
enjoyable | nice; you have a good time | It was a very enjoyable evening. | | pos
romantic | about love | They watched a romantic film for Valentine's Day. | | type
exciting | very interesting and full of action | The match was really exciting! | | pos
sad | it makes you cry | The end of the book was very sad. | | feel
fast-moving | a lot happens quickly | It's a fast-moving story — I loved it. | | pos
serious | not funny; about important things | It was a serious film about the war. | | type
frightening | it makes you afraid | The film was so frightening — I didn't sleep! | | neg
slow | not fast; nothing happens for a long time | The play was very slow. | | neg
funny | it makes you laugh | The comedy was really funny. | | pos
@Going out and staying in
cook dinner for friends | to make an evening meal for your friends | On Friday I cooked dinner for friends.
go to a party | to go to an event with music and friends | Did you go to a party on Eid?
go to the theatre | to see a play in a theatre | We went to the theatre in the Opera House.
download music | to get music from the internet | Hadi downloads music every week.
go to the cinema | to watch a film in a cinema | We didn't go to the cinema last week.
go for a walk | to walk for fun | We went for a walk on the corniche in Latakia.
play computer games | to play games on a computer | My brother played computer games all evening.
go to a concert | to listen to live music | Maya went to a concert at the Citadel.
go out for dinner | to eat in a restaurant | We went out for dinner in Qassaa.
read a book | to read a story or information in a book | I read a book on the bus.
go to a musical | to see a show with songs and dancing | Did you go to a musical in London?
watch a DVD at home | to watch a film on a disc at home | We stayed in and watched a DVD at home.
@Films and music
action film | a film with fights and fast cars | He loves action films.
historical film | a film about the past | It was a historical film about Saladin.
adventure film | a film about an exciting journey | Indiana Jones is an adventure film.
hit song | a very popular song | The band had a hit song in 2019.
lead singer | the main singer in a band | The lead singer has a fantastic voice.
audience | the people who watch a show or a film | The audience loved the concert.
make phone calls | to call people on the phone | She made phone calls all morning.
band | a group of musicians | My cousin plays in a band.
guitarist | a person who plays the guitar | The guitarist was only eighteen.
perform | to sing, dance or act in front of people | The band performed in Bosra's theatre.
comedy | a funny film or play | We watched a comedy and laughed all night.
romance | a love story | She reads a lot of romance.
sci-fi film | a film about the future and space | Star Wars is a famous sci-fi film.
drummer | a person who plays the drums | The drummer in our band is Rami.
get good reviews | when critics say good things | The film got good reviews.
write poems | to write short texts with rhythm | Nizar Qabbani wrote poems about love.
"""

ODD = """
funny, exciting, enjoyable, *boring | Boring: bad. The others: good.
guitarist, drummer, lead singer, *audience | Audience: they watch.
comedy, romance, sci-fi film, *band | Band: musicians, not a film.
didn't go, didn't see, didn't like, *don't like | Don't like: present.
Did, Was, Were, *Does | Does: present.
go to a concert, go to the theatre, go to a musical, *download music | Download music: at home.
"""

GRAMMAR = [
    dict(
        id="g1",
        title="Past simple: negative",
        visual=dict(type="table", head=["+", "−"],
                    rows=[["I went to the cinema.", "I {didn't go} to the theatre."], ["She liked the film.", "She {didn't like} the book."],
                          ["They watched a DVD.", "They {didn't watch} TV."]],
                    colors=["teal", "coral"], cap="didn't + verb (no -ed, no went)"),
        pattern=[
            ["−", "I / you / he / she / we / they", ["didn't", "n"], ["go", "v"], "out last night."],
            ["", "(didn't = did not)", "", ""],
            ["−", "She", ["wasn't", "n"], "at the party. (be: wasn't / weren't)"],
        ],
        examples=[
            "We {didn't go} to the cinema. We watched a DVD at home.",
            "Hadi {didn't like} the film. It was boring.",
            "The band {didn't perform} on Friday — the singer was ill.",
            "The film {wasn't} frightening. It was funny!",
        ],
        ar=[
            "بالماضي للنفي منحط didn't + الفعل بأصلو: I didn't go، مو I didn't went.",
            "didn't نفسها مع كل الأشخاص: I / she / they didn't.",
            "بس مع was / were منقول wasn't / weren't بلا didn't.",
        ],
        watch=[("I didn't went.", "I didn't go."), ("She didn't liked it.", "She didn't like it."), ("I didn't was at home.", "I wasn't at home.")],
        quick="""
## choose: Choose the answer.
I ___ go out last night. | didn't | wasn't | don't
She didn't ___ the film. | like | liked | likes
The film ___ funny. It was boring. | wasn't | didn't | weren't
""",
        sets="""
## choose: Choose the answer.
We ___ go to the theatre. We went to the cinema. | didn't | weren't | don't
Hadi didn't ___ the book. | read | reads | readed
The audience ___ happy. The show was bad. | wasn't | didn't | weren't
I didn't ___ dinner for friends on Friday. | cook | cooked | cooks
They ___ watch the match. | didn't | wasn't | don't
The band didn't ___ their hit song. | play | played | plays
The concert ___ exciting. It was slow. | wasn't | didn't | weren't
My parents didn't ___ to the musical. | go | went | goes
We ___ at the party. We were at home. | weren't | didn't | wasn't
She didn't ___ good reviews. | get | got | gets
## transform: Make the sentence negative (−).
I went to the cinema. (−) => I didn't go to the cinema. | I did not go to the cinema.
She liked the comedy. (−) => She didn't like the comedy. | She did not like the comedy.
They watched a DVD. (−) => They didn't watch a DVD. | They did not watch a DVD.
He wrote poems. (−) => He didn't write poems. | He did not write poems.
The band performed in Bosra. (−) => The band didn't perform in Bosra. | The band did not perform in Bosra.
We had a good time. (−) => We didn't have a good time. | We did not have a good time.
The film got good reviews. (−) => The film didn't get good reviews. | The film did not get good reviews.
I downloaded the album. (−) => I didn't download the album. | I did not download the album.
## transform: Make it negative: wasn't, weren't or didn't.
The film was funny. (−) => The film wasn't funny. | The film was not funny.
We went out for dinner. (−) => We didn't go out for dinner. | We did not go out for dinner.
The tickets were cheap. (−) => The tickets weren't cheap. | The tickets were not cheap.
Maya sang at the concert. (−) => Maya didn't sing at the concert. | Maya did not sing at the concert.
The story was exciting. (−) => The story wasn't exciting. | The story was not exciting.
They saw the musical. (−) => They didn't see the musical. | They did not see the musical.
The actors were good. (−) => The actors weren't good. | The actors were not good.
I read the book. (−) => I didn't read the book. | I did not read the book.
## fix: Find and fix the mistake.
I didn't [went>go] to the party.
She [don't>didn't] like the film yesterday.
We didn't [watched>watch] TV.
I [didn't was>wasn't] at home.
They [not went>didn't go] to the concert.
He didn't [saw>see] the end of the film.
The film [didn't>wasn't] funny.
We [didn't were>weren't] late.
## order: Put the words in order.
I didn't go to the cinema.
She didn't like the film.
The concert wasn't very exciting.
We didn't watch the match.
They didn't download the album.
The band didn't play their hit song.
He wasn't at the party.
I didn't read the book.
## bank: Use the words.
The film was boring, so we [didn't] stay to the end.
I [wasn't] at the party — I was ill.
The singer was ill, so the band didn't [perform].
We didn't [go] out. We watched a DVD at home.
The tickets [weren't] cheap.
I didn't [like] the end. It was sad.
They [didn't] get good reviews.
He didn't [write] the song. His brother wrote it.
""",
    ),
    dict(
        id="g2",
        title="Past simple: questions",
        visual=dict(type="table", head=["question word", "did", "person", "verb"],
                    rows=[["", "Did", "you", "like the film?"], ["Where", "did", "you", "go?"], ["What", "did", "she", "watch?"],
                          ["Who", "did", "they", "see?"], ["How", "was", "", "the concert? (be)"]],
                    colors=["amber", "purple", "teal", "white"], cap="(Question word) + did + person + verb?"),
        pattern=[
            ["?", ["Did", "v"], "you", "go to the concert? — Yes, I did. / No, I didn't."],
            ["?", ["What", "x"], ["did", "v"], "you watch?"],
            ["?", ["Where", "x"], ["did", "v"], "they go?"],
            ["?", ["How", "x"], ["was", "v"], "the film? (be)"],
        ],
        examples=[
            "{Did} you {enjoy} the musical? — Yes, {I did}!",
            "{What did} you {do} at the weekend? — I went to a party.",
            "{Who did} you {go} with? — With my cousin.",
            "{How was} the film? — It was really funny.",
        ],
        ar=[
            "لنسأل بالماضي: Did + الشخص + الفعل بأصلو: Did you see it?",
            "مع كلمة السؤال: What did you do? Where did you go?",
            "مع was / were ما منستعمل did: How was the film?",
        ],
        watch=[("Did you saw the film?", "Did you see the film?"), ("Where you went?", "Where did you go?"), ("Did the film was good?", "Was the film good?")],
        quick="""
## choose: Choose the answer.
___ you like the concert? | Did | Were | Do
What did you ___ last night? | do | did | done
How ___ the film? | was | did | were
""",
        sets="""
## choose: Choose the answer.
___ you go to the theatre? | Did | Were | Do
Did she ___ the album? | download | downloaded | downloads
What ___ you watch last night? | did | were | do
Where did they ___ for dinner? | go | went | goes
___ the film exciting? | Was | Did | Were
Did you enjoy it? — Yes, I ___. | did | was | enjoyed
Who ___ you go with? | did | were | was
How ___ the concert? | was | did | were
Did they like the comedy? — No, they ___. | didn't | weren't | don't
When did the band ___ the song? | write | wrote | writes
## short: Answer the question.
Did you go to the party? (✓) => Yes, I did.
Did she like the film? (✗) => No, she didn't. | No, she did not.
Was the concert good? (✓) => Yes, it was.
Did they see the musical? (✗) => No, they didn't. | No, they did not.
Did Hadi download the album? (✓) => Yes, he did.
Were the actors good? (✗) => No, they weren't. | No, they were not.
Did you cook dinner for friends? (✓) => Yes, I did.
Did the film get good reviews? (✗) => No, it didn't. | No, it did not.
## transform: Make a question (?).
You went to the cinema. (?) => Did you go to the cinema?
She liked the book. (?) => Did she like the book?
They performed in Bosra. (?) => Did they perform in Bosra?
He wrote the song. (?) => Did he write the song?
The film was funny. (?) => Was the film funny?
You saw the match. (?) => Did you see the match?
The audience was happy. (?) => Was the audience happy?
Maya sang at the concert. (?) => Did Maya sing at the concert?
## bank: Use the words.
[What] did you do on Friday? — I went to a concert.
[Where] did you go for dinner? — To Qassaa.
[Who] did you go with? — My sister.
[When] did the film start? — At nine.
[How] was the musical? — Fantastic!
[What] did you watch? — A comedy.
[Who] did you see? — The lead singer!
[Where] did they perform? — In Bosra's theatre.
## fix: Find and fix the mistake.
Did you [saw>see] the film?
Where [you went>did you go]?
[Did>Was] the concert good?
What did you [did>do] yesterday?
Did they like it? — Yes, they [liked>did].
[Do>Did] you go out last night?
Who [you met>did you meet] at the party?
How [did>was] the musical?
## order: Put the words in order.
Did you enjoy the film?
What did you do last night?
Where did you go for dinner?
Who did you go with?
How was the concert?
Did they get good reviews?
When did the band start?
Was the film frightening?
""",
    ),
    dict(
        id="g3",
        title="Stories and entertainment",
        visual=dict(type="chips", groups=[
            dict(title="types of film", color="purple", items=["action film", "comedy", "romance", "sci-fi film", "historical film", "adventure film"]),
            dict(title="good", color="teal", items=["funny", "exciting", "enjoyable", "fast-moving", "romantic"]),
            dict(title="bad", color="coral", items=["boring", "slow", "frightening (for some people!)"]),
            dict(title="people", color="amber", items=["lead singer", "guitarist", "drummer", "band", "audience"]),
        ]),
        pattern=[
            ["", "It was a", ["comedy.", "v"], "It was really funny."],
            ["", "The", ["audience", "x"], "loved the band."],
            ["", "The film", ["got good reviews.", "v"], ""],
        ],
        examples=[
            "We watched a {comedy}. It was really {funny}.",
            "The {lead singer} and the {guitarist} are brothers.",
            "The film {got good reviews}, but I thought it was {slow}.",
            "The {audience} was very quiet — it was a {serious} film.",
        ],
        ar=[
            "أنواع الأفلام: comedy (كوميدي)، romance (رومانسي)، sci-fi (خيال علمي).",
            "صفات: funny (مضحك)، boring (ممل)، frightening (بيخوّف)، fast-moving (أحداثو سريعة).",
            "audience يعني الجمهور، و get good reviews يعني ياخد آراء منيحة.",
        ],
        watch=[("The film was very bored.", "The film was very boring."), ("I was boring in the film.", "I was bored in the film."), ("a comedy film very sad", "a very sad film")],
        quick="""
## choose: Choose the answer.
A film about the future and space: | sci-fi film | romance | historical film
It makes you laugh: | funny | serious | sad
The people who watch a show: | audience | band | lead singer
""",
        sets="""
## choose: What kind of film is it?
"Two people fall in love in Paris." | romance | sci-fi film | action film
"Fast cars, fights and explosions!" | action film | romance | historical film
"Spaceships and robots in the year 3000." | sci-fi film | comedy | historical film
"A funny story about a crazy family wedding." | comedy | historical film | sci-fi film
"The life of a king in the twelfth century." | historical film | sci-fi film | comedy
"A long journey to find treasure in the jungle." | adventure film | romance | historical film
"A man and a woman meet on a train and fall in love." | romance | action film | sci-fi film
"Aliens arrive on Earth from Mars." | sci-fi film | romance | historical film
## choose: Choose the right adjective.
I laughed all the time. It was very ___. | funny | sad | serious
I cried at the end. It was very ___. | sad | funny | fast-moving
Nothing happened for an hour! It was so ___. | slow | exciting | fast-moving
I closed my eyes. It was really ___. | frightening | romantic | funny
A lot happened very quickly. It was ___. | fast-moving | slow | boring
It was about war and history. It was very ___. | serious | funny | romantic
I had a really nice evening. It was very ___. | enjoyable | boring | frightening
I loved the story. It was so ___. | exciting | boring | slow
## match: Match.
lead singer = the main singer in a band
guitarist = plays the guitar
drummer = plays the drums
audience = the people who watch a show
band = a group of musicians
hit song = a very popular song
perform = to sing or act in front of people
get good reviews = critics say good things
## gap: Write the word.
We laughed a lot. It was a [comedy].
The [audience] stood up and clapped.
The [drummer] played very loudly.
The film got good [reviews] in the newspapers.
The band [performed] in Bosra's theatre last summer.
Their hit [song] was on the radio every day.
The lead [singer] has a beautiful voice.
I watched a [DVD] at home last night.
## sort: Good or bad? | good | bad
good: funny, exciting, enjoyable, fast-moving
bad: boring, slow, awful, horrible
## order: Put the words in order.
It was a really funny comedy.
The audience loved the band.
The film got good reviews.
The lead singer was fantastic.
We watched a DVD at home.
Did you like the sci-fi film?
The story was slow and boring.
The guitarist wrote the hit song.
""",
    ),
]

CLASSROOM = dict(
    phrases=["Is there another way to say …?", "Which one is more common?", "What's the difference between … and …?",
             "Can you give me an example?", "I'm not sure.", "I think it's …", "Well done!"],
    order="""
S: Is there another way to say 'funny'?
T: Yes — 'hilarious' or 'very funny'.
S: Which one is more common?
T: 'Very funny' — people say it all the time.
S: What's the difference between 'funny' and 'fun'?
T: A funny film makes you laugh. A fun party is enjoyable.
""",
)

READING = dict(
    title="The band that almost became famous",
    text="""In 1978, four friends from Bab Touma started a band. Rami was the drummer, Ziad and Bassel were guitarists, and Maha was the lead singer. They called the band "Jasmine".

At first, they didn't have money for instruments, so they practised with old guitars in Rami's garage. They performed at weddings and small parties. Then, in 1981, they wrote a song called "Qasioun Nights". A radio station played it, and it became a hit song in Syria and Lebanon. The band got good reviews in the newspapers, and they performed in Bosra's theatre in front of a big audience.

But they didn't become really famous. Bassel moved to Canada, and Maha decided to study medicine. The band didn't record a second album. Today, Rami still plays the drums — for his grandchildren!

Is this story fact or fiction? It's fiction — but a lot of real bands have stories like this.""",
    qs="""
## tf: True or false?
The band started in 1981. | F @ In 1978, four friends from Bab Touma started a band
Maha was the lead singer. | T @ Maha was the lead singer
They had a lot of money at first. | F @ they didn't have money for instruments
"Qasioun Nights" became a hit song. | T @ it became a hit song in Syria and Lebanon
The band recorded a second album. | F @ The band didn't record a second album
## choose: Choose the answer.
Where did they practise? | in Rami's garage | in Bosra's theatre | at a radio station @ they practised with old guitars in Rami's garage
Why did Maha leave the band? | She decided to study medicine. | She moved to Canada. | She got married. @ Maha decided to study medicine
## gap: Write one word.
The story is [fiction]. @ It's fiction
""",
)

DIALOGUE = dict(
    title="How was your weekend?",
    intro="Monday morning. Dima and Samer talk at the hairdresser's.",
    task="gaps",
    lines="""
Dima: So, Samer, what [did] you do at the weekend?
Samer: I went to the cinema with my brother.
Dima: Oh! What did you [see]?
Samer: A sci-fi film. It got good [reviews], but I didn't like it.
Dima: Why not? Was it [boring]?
Samer: Yes, it was long and slow. And you? [Did] you go out?
Dima: No, I [didn't]. I cooked dinner for friends and we watched a comedy.
Samer: How [was] it?
""",
)

WQ = """
I went to a concert. (What / you / do / on Friday) => What did you do on Friday?
Yes, I did. It was fantastic. (you / enjoy / the musical) => Did you enjoy the musical?
With my cousin. (Who / you / go with) => Who did you go with?
No, it wasn't. It was funny. (the film / frightening) => Was the film frightening?
In Bosra's theatre. (Where / the band / perform) => Where did the band perform?
At nine o'clock. (When / the film / start) => When did the film start? | What time did the film start?
No, they didn't. They stayed at home. (they / go out) => Did they go out?
It was boring. (How / the play) => How was the play?
"""

WRITING = [
    dict(task="Write a short review of a film, a concert or a book. What was it? When did you see or read it? What happened? Did you like it? Why or why not?",
         tip="Use the past simple (+, −, ?) and adjectives: funny, boring, exciting, slow. Write 80–120 words.",
         model="Last Thursday, I went to the cinema in the shopping centre with my sister. We saw a historical film about Saladin. It got very good reviews, so we were excited. The first hour was fast-moving and exciting, with fantastic battles. But the second hour was slow, and the end was very sad — my sister cried! The actors were very good, but the film was too long. I didn't love it, but it was enjoyable. Did I recommend it to my friends? Yes, I did — but I told them to take some popcorn!",
         check=["past simple: went, saw, was", "didn't + verb", "a question: Did…? / What did…?", "adjectives: exciting, slow, sad, funny"],
         min=80, max=120),
]

CANDO = [
    "use didn't + verb in the past.",
    "ask past questions: Did you…? What did you…?",
    "describe films and shows: funny, boring, exciting.",
    "talk about what I did at the weekend.",
    "write a short review of a film or a concert.",
]
