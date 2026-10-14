"""Content shared by all four apps: classroom English, names and places, Learn Smarter tips,
Resources and the irregular verbs list.

Classroom phrases: (phrase, situation, who, level, group).
who: S = student says it, T = teacher says it (learners only need to understand it).
level: 1 = A1.1, 2 = A1.2, 3 = A2.1, 4 = A2.2.  Phrases from lower levels are recycled later.
group: phrases in the same group are never used as wrong options for each other.
"""

_CLS = [
    # ---------------- A1.1, student
    ("Hello. / Good morning.", "You arrive at class. It's 9 o'clock in the morning.", "S", 1, "greet"),
    ("Sorry I'm late.", "The lesson started 10 minutes ago. You open the door.", "S", 1, "late"),
    ("Can I come in?", "You're at the classroom door. The lesson is on.", "S", 1, "late"),
    ("I don't understand.", "The teacher explains a rule, but it isn't clear for you.", "S", 1, "understand"),
    ("I don't know.", "The teacher asks you a question. You have no idea of the answer.", "S", 1, "know"),
    ("Can you repeat that, please?", "You didn't hear the teacher's last sentence.", "S", 1, "understand"),
    ("Slowly, please.", "The teacher speaks very fast for you.", "S", 1, "understand"),
    ("How do you spell …?", "You want to write a new word, but you don't know the letters.", "S", 1, "word"),
    ("What's … in English?", "You know a word in Arabic. You need the English word.", "S", 1, "word"),
    ("What does … mean?", "You see a new English word in the book. You don't know its meaning.", "S", 1, "word"),
    ("Which page?", "The teacher says 'Open your books', but you don't know where.", "S", 1, "page"),
    ("Can I go to the bathroom?", "You need the toilet in the lesson.", "S", 1, "ask"),
    ("Can I have a pen / some paper?", "You need to write, but you have nothing to write with or on.", "S", 1, "borrow"),
    ("Sorry, I don't have my book.", "Your coursebook is at home today.", "S", 1, "book"),
    ("Is this right?", "You finish an exercise and want the teacher to look at your answer.", "S", 1, "check"),
    ("I'm ready.", "The teacher asks: 'Ready to start?' Your book and pen are on the table.", "S", 1, "ready"),
    ("I'm finished.", "You complete the exercise before the others.", "S", 1, "ready"),
    ("It's my turn.", "In a game, your partner had a go. Now you want to play.", "S", 1, "turn"),
    ("Excuse me.", "You want to get the teacher's attention politely.", "S", 1, "attention"),
    ("Thank you.", "The teacher gives you a pen.", "S", 1, "thanks"),
    ("See you tomorrow. / See you next lesson.", "The lesson finishes. You leave the classroom.", "S", 1, "bye"),
    # ---------------- A1.1, teacher
    ("Open your books.", "The teacher wants you to start using your coursebook.", "T", 1, "books"),
    ("Close your books.", "The teacher wants your coursebooks shut.", "T", 1, "books"),
    ("Turn to page …", "The teacher tells everyone the page number.", "T", 1, "books"),
    ("Look at the board.", "The teacher writes something and wants your eyes on it.", "T", 1, "look"),
    ("Listen.", "The teacher wants you to use your ears, not your mouth.", "T", 1, "listen"),
    ("Repeat.", "The teacher says a word and wants you to say it again.", "T", 1, "say"),
    ("Read.", "The teacher wants you to look at a text and understand it.", "T", 1, "readwrite"),
    ("Write.", "The teacher wants you to use your pen and notebook.", "T", 1, "readwrite"),
    ("Work in pairs.", "The teacher wants you to work with one other student.", "T", 1, "work"),
    ("Work in groups.", "The teacher wants you to work with three or four other students.", "T", 1, "work"),
    ("Change partners.", "The teacher wants you to work with a new person.", "T", 1, "work"),
    ("Check with your partner.", "The teacher wants you and the student next to you to compare answers.", "T", 1, "check"),
    ("Stand up.", "The teacher wants everyone on their feet.", "T", 1, "body"),
    ("Sit down.", "The teacher wants everyone back on their chairs.", "T", 1, "body"),
    ("Hands up.", "The teacher wants you to raise your hand.", "T", 1, "body"),
    ("Be quiet, please.", "The class is very noisy.", "T", 1, "quiet"),
    ("Homework.", "This is work for you to do at home, after the lesson.", "T", 1, "home"),
    # ---------------- A1.2
    ("Can you help me?", "You have a problem with an exercise and need the teacher.", "S", 2, "help"),
    ("Can I ask a question?", "You want to ask the teacher something.", "S", 2, "help"),
    ("Can you write it on the board, please?", "You can't see how a new word is written.", "S", 2, "word"),
    ("How do you say this word?", "You can read a word, but you don't know how it sounds.", "S", 2, "word"),
    ("What's the answer to number 3?", "You don't have the answer to the third question.", "S", 2, "answer"),
    ("Is it a or b?", "You're not sure which of two choices is right.", "S", 2, "answer"),
    ("I think it's …", "You have an idea of the answer, but it's only your opinion.", "S", 2, "know"),
    ("I'm not sure.", "Maybe you know the answer, maybe not.", "S", 2, "know"),
    ("Can I work with …?", "You want a friend as your partner.", "S", 2, "partner"),
    ("Whose turn is it?", "In a game, nobody knows who plays next.", "S", 2, "turn"),
    ("You go first.", "You want your partner to start the game.", "S", 2, "turn"),
    ("Let's start.", "Everyone is ready. You want the pair work to begin.", "S", 2, "ready"),
    ("Sorry, can you speak louder, please?", "The teacher's voice is very quiet.", "S", 2, "understand"),
    ("I was absent last lesson.", "You weren't in class last time.", "S", 2, "absent"),
    ("What did we do yesterday?", "You missed yesterday's lesson and want to know about it.", "S", 2, "absent"),
    ("What's the homework?", "The lesson finishes, but you didn't hear the work for home.", "S", 2, "home"),
    ("Good luck!", "Your friend has a test now.", "S", 2, "wish"),
    ("Well done!", "Your partner gets all the answers right.", "S", 2, "wish"),
    # ---------------- A2.1
    ("What's the difference between … and …?", "Two words look similar to you, for example 'make' and 'do'.", "S", 3, "word"),
    ("Can you give me an example?", "You understand the rule, but you need to see it in a sentence.", "S", 3, "example"),
    ("How do you say … in English?", "You know the Arabic word, but not the English one.", "S", 3, "word"),
    ("Do we need to write this?", "The teacher writes on the board. Is it important for your notebook?", "S", 3, "home"),
    ("When is the homework for?", "You know the homework, but not the day to give it to the teacher.", "S", 3, "home"),
    ("Can I borrow your …?", "You need your friend's dictionary for a minute.", "S", 3, "borrow"),
    ("I agree. / I don't agree.", "Your partner gives an opinion. You say if you think the same.", "S", 3, "opinion"),
    ("What do you think?", "You want your partner's opinion.", "S", 3, "opinion"),
    ("Can you explain that again, please?", "The teacher explains a rule, but you need to hear it one more time.", "S", 3, "understand"),
    ("Shall we start?", "You and your partner are ready for the activity.", "S", 3, "ready"),
    ("Let's change roles.", "In a role play, you were the customer. Now you want to be the waiter.", "S", 3, "turn"),
    ("Sorry, I didn't hear you.", "Your partner says something, but the class is noisy.", "S", 3, "understand"),
    ("What page are we on?", "You look up from your phone and you're lost in the book.", "S", 3, "page"),
    ("How do you pronounce this word?", "You can read a word, but you don't know how it sounds.", "S", 3, "word"),
    # ---------------- A2.2
    ("Is there another way to say …?", "You want a different word with the same meaning.", "S", 4, "word"),
    ("Which one is more common?", "There are two words for one thing. You want the one people use more.", "S", 4, "word"),
    ("Would you like to go first?", "You politely offer your partner the start in a game.", "S", 4, "turn"),
    ("I'd like to ask about …", "You want to ask the teacher about a topic.", "S", 4, "help"),
    ("I have to leave early today.", "You have a doctor's appointment in the middle of the lesson.", "S", 4, "absent"),
    ("Sorry, I missed the last lesson. Have I missed anything important?", "You were ill last time and want to know about the lesson.", "S", 4, "absent"),
    ("Have you finished?", "You want to know if your partner is ready.", "S", 4, "ready"),
    ("What's the opposite of …?", "You know 'cheap' and want the word with the other meaning.", "S", 4, "word"),
    ("Could you check my writing, please?", "You finish a paragraph and want the teacher to look at it.", "S", 4, "check"),
    ("I'm going to be absent on Thursday.", "You know about a family wedding next Thursday.", "S", 4, "absent"),
    ("I'm not sure, but I think …", "You have an idea, but you aren't certain.", "S", 4, "know"),
    ("That's a good idea!", "Your partner suggests a great plan for the project.", "S", 4, "opinion"),
]

CLASSROOM_ALL = [dict(p=p, s=s, who=w, lvl=l, grp=g) for p, s, w, l, g in _CLS]

# Chunks taught as fixed phrases before the grammar (removed before the level gate checks).
CHUNKS = {
    "starter": ["How do you spell it", "How do you spell that", "My name's", "What's your name",
                "What's your phone number", "What's your email address", "What's your job",
                "I'm fine, thanks", "Fine, thanks", "Good morning", "Good afternoon", "Good evening",
                "Excuse me", "See you later", "Here you are", "Let's go", "Let's start",
                "you can invent one"],
    "elementary": ["How do you spell it", "How do you spell that", "Here you are", "Excuse me",
                   "Let's go", "Nice to meet you too"],
}

CAST = ["Abu Salim", "Um Khaled", "Layla", "Kareem", "Rana", "Hadi", "Nour", "Tareq", "Maya", "Abu Firas",
        "Salma", "Jad", "Dima", "Reem", "Abu Omar", "Hala", "Walid", "Ghada", "Samer", "Fadi"]
NAMES = ["Ahmad", "Omar", "Yusuf", "Sami", "Ziad", "Rami", "Khaled", "Bassel", "Mazen", "Firas", "Wassim", "Majd",
         "Karam", "Lina", "Maha", "Razan", "Aya", "Hiba", "Joud", "Mais", "Lama", "Yara", "Tala", "Sana", "Ruba", "Hind",
         "James", "Lucas", "Marco", "Pierre", "Carlos", "Kenji", "Wei", "Raj", "Mehmet", "Sven", "Emma", "Sofia",
         "Chloé", "Giulia", "Yuki", "Mei", "Priya", "Olga", "Elif", "Lucía", "Hannah"]

PLACES = {
    "damascus": ["Damascus", "Umayyad Mosque", "Souq al-Hamidiyah", "Hamidiyah", "Souq al-Bzouriyah", "Bzouriyah",
                 "Straight Street", "Azem Palace", "the Citadel of Damascus", "Bab Touma", "Bab Sharqi",
                 "Hejaz Railway Station", "Hejaz", "Tekkiye Mosque", "Tekkiye", "Qasioun", "Barada", "Tishreen Park", "Sibki Park",
                 "Ghouta", "Midan", "Sarouja", "Qassaa", "Mezzeh", "Malki", "Abu Rummaneh", "Sha'lan", "Baramkeh",
                 "Rukn al-Din", "Dummar", "Kafr Sousa", "Jaramana", "Muhajirin", "Marjeh", "Bakdash", "Al-Nofara",
                 "Nofara", "Khan As'ad Pasha", "National Museum", "Old City", "Qaboun"],
    "syria": ["Aleppo", "Homs", "Latakia", "Hama", "Krak des Chevaliers", "Maaloula", "Saidnaya", "Bloudan",
              "Zabadani", "Tartus", "Arwad", "Kasab", "Bosra", "Palmyra", "Orontes", "Bab al-Faraj", "Syria"],
    "world": ["Istanbul", "Dubai", "London", "Paris", "Cairo", "Beirut", "New York", "Tokyo", "Rome", "Amman",
              "Barcelona", "Vienna", "Seoul", "Toronto", "Sydney", "Doha", "Brazil", "China", "Egypt", "England",
              "Italy", "Japan", "Poland", "Russia", "Vietnam", "the USA", "Portugal", "Argentina", "Spain",
              "Australia", "Turkey", "Lebanon", "Jordan", "Germany", "France", "Canada", "India", "Mexico",
              "Ireland", "Britain", "Moscow", "Madrid", "Lisbon", "Warsaw", "Beijing", "Hanoi", "Rio", "Buenos Aires",
              "Milan", "Berlin", "Athens", "Mumbai", "Iceland", "Norway"],
}

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
          "November", "December"]
EXTRA_PROPER = ["English", "Arabic", "Syrian", "Turkish", "French", "Spanish", "Italian", "Chinese", "Japanese",
                "Polish", "Russian", "Vietnamese", "American", "Brazilian", "Australian", "Egyptian", "Portuguese",
                "Argentinian", "Lebanese", "Jordanian", "German", "British", "Irish", "Mr", "Mrs", "Ms", "Dr",
                "Um", "Abu", "Ramadan", "Eid", "TV", "OK", "DVD", "Wi-Fi", "Instagram", "Facebook", "Google",
                "Internet", "Sham", "Qatar", "Saudi", "Kenya", "Mexico", "UK", "USA", "Uncle", "Aunt", "Grandma",
                "Grandpa", "Mum", "Dad", "Northern", "Lights", "Christmas", "Mother's", "Tai", "Chi", "Professor"]

PROPER = set()
for _n in CAST + NAMES + DAYS + MONTHS + EXTRA_PROPER:
    PROPER.update(_n.replace("'", " ").split())
    PROPER.add(_n.split()[0])
for _l in PLACES.values():
    for _n in _l:
        PROPER.update(w for w in _n.split() if w[:1].isupper())

# ---------------------------------------------------------------- Learn Smarter
# Each tip: title, one-line summary, and 3-4 slides. A slide: heading, text, drawn visual name.
SMARTER = [
    dict(id="cards", title="Word cards that work", icon="cards",
         summary="Make small cards and test yourself, don't only read.",
         slides=[
             dict(h="One word, one card", t="Front: the English word. Back: a picture or a simple meaning, and one example sentence from your life.", v="card"),
             dict(h="Test, don't read", t="Look at the front. Say the meaning. Then turn the card. Reading the list again and again is slow. Testing yourself is fast.", v="flip"),
             dict(h="Three boxes", t="Box 1: new words, every day. Box 2: OK words, every three days. Box 3: easy words, every week. A wrong word goes back to Box 1.", v="boxes"),
             dict(h="In this app", t="Mark words 'Still learning'. They go to your Review Pile. Practise the pile for five minutes a day.", v="pile"),
         ]),
    dict(id="little", title="Little and often", icon="clock",
         summary="15 minutes every day is better than 2 hours on Friday.",
         slides=[
             dict(h="Your brain likes repeats", t="You forget new words fast. A short review the next day, and again a few days later, keeps them.", v="curve"),
             dict(h="A daily habit", t="Choose a fixed time: after breakfast, on the service taxi, before bed. Same time, every day.", v="calendar"),
             dict(h="Keep your streak", t="The flame on the Home screen counts your days in a row. Try not to break it!", v="streak"),
         ]),
    dict(id="mistakes", title="Love your mistakes", icon="pencil",
         summary="Mistakes show you what to learn next.",
         slides=[
             dict(h="Everyone makes mistakes", t="Mistakes are normal. They show your brain is working on a new rule.", v="smile"),
             dict(h="Your Mistake Notebook", t="The app saves your wrong answers with the right answers. Read them before a test.", v="notebook"),
             dict(h="Find your pattern", t="Is it always the same mistake? For example, 'He go' instead of 'He goes'? Write it on a card and look at it every day.", v="pattern"),
         ]),
    dict(id="chunks", title="Learn chunks, not single words", icon="blocks",
         summary="Learn words together with their friends.",
         slides=[
             dict(h="Words have friends", t="Don't learn only 'homework'. Learn 'do my homework'. Don't learn only 'photo'. Learn 'take a photo'.", v="chunks"),
             dict(h="Copy whole sentences", t="When you read a useful sentence, write the full sentence in your notebook.", v="notebook"),
             dict(h="Use them today", t="Say your new chunk three times today: in class, at home, in a message to a friend.", v="three"),
         ]),
    dict(id="arabic", title="Arabic can help — and trick you", icon="bridge",
         summary="Notice where English and Arabic are different.",
         slides=[
             dict(h="No 'is' in Arabic", t="In Arabic, 'I student' is a full sentence, with no verb. In English you need the verb: 'I am a student.'", v="slots",
                  ar="بالعربي منقول «أنا طالب» بلا فعل. بالإنكليزي لازم الفعل: I am a student."),
             dict(h="Age", t="In English we say 'I'm 20', not 'I have 20 years'.", v="swap",
                  ar="بالعربي منقول «عمري 20 سنة». بالإنكليزي: I'm 20، مو I have 20 years."),
             dict(h="Make a 'trap list'", t="Write the sentences where Arabic tricks you. Check the list before you write or speak.", v="list"),
         ]),
    dict(id="speak", title="Talk to yourself in English", icon="chat",
         summary="Practise speaking anywhere, alone.",
         slides=[
             dict(h="Describe your day", t="Walking to work? Say in your head: 'I'm at the bakery. The bread is hot.' Simple is fine.", v="walk"),
             dict(h="Record yourself", t="Use your phone's voice recorder for one minute. Listen and choose one thing to make better.", v="phone"),
             dict(h="Shadow", t="Play a short English video. Pause after each sentence and say it like the speaker.", v="shadow"),
         ]),
    dict(id="read", title="Read a little, every day", icon="book",
         summary="Easy reading builds vocabulary fast.",
         slides=[
             dict(h="Easy is good", t="Choose texts where you know almost all the words. Easy reading is fast and fun, and you read more.", v="book"),
             dict(h="Graded readers", t="These are short books for learners, with levels from A1 up. Start one level below your level.", v="stairs"),
             dict(h="Guess, then check", t="Meet a new word? First guess from the sentence. Then check in a learner's dictionary.", v="magnifier"),
         ]),
    dict(id="test", title="Before a test", icon="target",
         summary="A simple plan for test week.",
         slides=[
             dict(h="Test yourself first", t="Do the Unit test in the app. Look at your wrong answers. Practise those parts again.", v="target"),
             dict(h="Sleep is study time", t="Your brain saves new things while you sleep. Don't study all night before the test.", v="moon"),
             dict(h="Read the question twice", t="In the test, read each question carefully. Check your answers at the end.", v="check"),
         ]),
]

# ---------------------------------------------------------------- Resources
RESOURCES = [
    dict(name="LearnEnglish (British Council)", url="https://learnenglish.britishcouncil.org", kind="Website",
         what="Free lessons, grammar explanations and exercises for every level."),
    dict(name="BBC Learning English", url="https://www.bbc.co.uk/learningenglish", kind="Website",
         what="Short lessons, videos and grammar practice. Free."),
    dict(name="Cambridge Dictionary", url="https://dictionary.cambridge.org", kind="Dictionary",
         what="Clear meanings and example sentences. There is also an English–Arabic dictionary."),
    dict(name="Oxford Learner's Dictionaries", url="https://www.oxfordlearnersdictionaries.com", kind="Dictionary",
         what="A dictionary written for learners, with simple meanings."),
    dict(name="Duolingo", url="https://www.duolingo.com", kind="App",
         what="A free app for short daily practice. Good for a daily habit."),
    dict(name="Quizlet", url="https://quizlet.com", kind="App",
         what="Make your own word cards and test yourself."),
    dict(name="Anki", url="https://apps.ankiweb.net", kind="App",
         what="Word cards that come back just before you forget them."),
    dict(name="ESL Video", url="https://www.eslvideo.com", kind="Website",
         what="Short videos with quizzes, sorted by level."),
]

# ---------------------------------------------------------------- Irregular verbs
# (base, past, past participle, first level where it appears)
VERBS = [(b, p, pp, lvl) for b, p, pp, lvl in [
    ("be", "was / were", "been", 2), ("become", "became", "become", 2), ("begin", "began", "begun", 3),
    ("buy", "bought", "bought", 2), ("come", "came", "come", 2), ("do", "did", "done", 2),
    ("drink", "drank", "drunk", 2), ("drive", "drove", "driven", 2), ("eat", "ate", "eaten", 2),
    ("find", "found", "found", 2), ("fly", "flew", "flown", 2), ("forget", "forgot", "forgotten", 2),
    ("get", "got", "got", 2), ("give", "gave", "given", 2), ("go", "went", "gone / been", 2),
    ("have", "had", "had", 2), ("hear", "heard", "heard", 3), ("know", "knew", "known", 2),
    ("leave", "left", "left", 2), ("lose", "lost", "lost", 3), ("make", "made", "made", 2),
    ("meet", "met", "met", 2), ("pay", "paid", "paid", 3), ("put", "put", "put", 3),
    ("read", "read", "read", 2), ("ride", "rode", "ridden", 2), ("run", "ran", "run", 2),
    ("say", "said", "said", 2), ("see", "saw", "seen", 2), ("sell", "sold", "sold", 2),
    ("send", "sent", "sent", 3), ("sing", "sang", "sung", 2), ("sit", "sat", "sat", 3),
    ("sleep", "slept", "slept", 3), ("speak", "spoke", "spoken", 2), ("spend", "spent", "spent", 3),
    ("swim", "swam", "swum", 2), ("take", "took", "taken", 2), ("teach", "taught", "taught", 2),
    ("tell", "told", "told", 3), ("think", "thought", "thought", 2), ("understand", "understood", "understood", 3),
    ("wake up", "woke up", "woken up", 3), ("wear", "wore", "worn", 4), ("win", "won", "won", 2),
    ("write", "wrote", "written", 2), ("bring", "brought", "brought", 3), ("choose", "chose", "chosen", 4),
    ("feel", "felt", "felt", 3), ("grow", "grew", "grown", 3), ("keep", "kept", "kept", 4),
    ("break", "broke", "broken", 4), ("catch", "caught", "caught", 4), ("draw", "drew", "drawn", 4),
]]
