META = dict(n=14, title="Keep in touch", pages="124–137")

BOOK = """
send a text message, internet connection, smartphone, landline, tablet computer, laptop, update your status,
leave a voice message, use the internet, make a phone call, use video chat, pick up voicemail, Wi-Fi connection,
send an attachment, send an email, online account, access the internet, password, anti-virus software, upload,
download, username, hacker, virus, Wi-Fi hotspot, internet user, apologise, get angry, so far today, be on hold,
dial a number, dial a wrong number, text speak
"""

WORDS = """
@Phones
send a text message | to write a short message on a phone | I've sent three text messages so far today. | send a text message;sent three text messages;sent a text message
smartphone | a mobile phone that can use the internet | Have you ever lost your smartphone? | | device
landline | a phone at home with a wire | My grandparents still use a landline. | | device
leave a voice message | to speak a message when the person doesn't answer | I left a voice message for Rana. | leave a voice message;left a voice message
make a phone call | to call someone | I've made five phone calls today. | make a phone call;made five phone calls
use video chat | to talk and see each other on the internet | We use video chat with my cousin in Toronto.
pick up voicemail | to listen to your voice messages | Have you picked up your voicemail? | pick up voicemail;picked up your voicemail;pick up your voicemail
be on hold | to wait on the phone with music | I was on hold for twenty minutes! | be on hold;been on hold;was on hold
dial a number | to press the numbers on a phone | Dial the number and press the green button. | dial a number;dial the number
dial a wrong number | to call the wrong person by mistake | Sorry, I've dialled a wrong number. | dial a wrong number;dialled a wrong number;dialed a wrong number
text speak | short words in messages, like "u" for "you" | "C u l8r" is text speak for "See you later".
@Computers and the internet
internet connection | a link to the internet | The internet connection is very slow today. | | net
tablet computer | a flat computer with a touch screen | My father has bought a tablet computer. | | device
laptop | a small computer you can carry | Have you charged your laptop? | | device
update your status | to write news about you on a social networking site | Maya updates her status every day. | update your status;updates her status
use the internet | to go online | Have you ever used the internet on a plane? | use the internet;used the internet
Wi-Fi connection | a connection to the internet without wires | Is there a Wi-Fi connection in the café? | | net
send an attachment | to send a file with an email | I've sent the attachment — check your email. | send an attachment;sent the attachment
send an email | to write and send an electronic letter | Have you sent the email to the manager? | send an email;sent the email
online account | your personal page on a website | I've opened an online account at the bank. | | acc
access the internet | to get on the internet | You can access the internet in the library.
password | a secret word to open your account | Don't tell anyone your password! | | acc
anti-virus software | a program that protects your computer | Have you installed anti-virus software?
upload | to send files from your computer to the internet | I've uploaded the photos from the wedding. | | load
download | to get files from the internet to your computer | Have you downloaded the new app? | | load
username | the name you use on a website | My username is reem_reads. | | acc
hacker | a person who gets into other people's computers | A hacker has stolen my password! | | bad
virus | a program that damages computers | My laptop has got a virus. | | bad
Wi-Fi hotspot | a place where you can use Wi-Fi | The café is a free Wi-Fi hotspot. | | net
internet user | a person who uses the internet | There are billions of internet users in the world.
@Other words
apologise | to say sorry | I've apologised to Hala for the late reply.
get angry | to become angry | Abu Salim gets angry when the internet is slow.
so far today | from the morning until now | I've drunk four coffees so far today!
"""

ODD = """
smartphone, laptop, tablet computer, *password | Password: not a device.
upload, download, send an email, *landline | Landline: not an action.
hacker, virus, *anti-virus software, spam | Anti-virus software: it protects you.
been, gone, seen, *went | Went: past simple, not a past participle.
ever, so far today, never, *yesterday | Yesterday: past simple.
username, password, online account, *video chat | Video chat: not about logging in.
"""

GRAMMAR = [
    dict(
        id="g1",
        title="Present perfect: so far today",
        visual=dict(type="timeline", now="now", span={"from": -2, "to": 0, "label": "today: from the morning until now"},
                    marks=[dict(at=-2, label="this morning"), dict(at=0, label="I've sent 10 emails so far.")]),
        pattern=[
            ["+", "I / you / we / they", ["have ('ve) sent", "v"], "three emails."],
            ["+", "He / she", ["has ('s) made", "v"], "five phone calls."],
            ["−", "I", ["haven't checked", "n"], "my email."],
            ["?", ["Have", "v"], "you", "uploaded the photos? — Yes, I have."],
        ],
        examples=[
            "I{'ve sent} twenty text messages {so far today}.",
            "Rana {has made} four phone calls this morning.",
            "I {haven't checked} my email yet.",
            "{Have} you {uploaded} the photos? — No, {I haven't}.",
        ],
        ar=[
            "المضارع التام (present perfect) لشي صار بفترة لسّا ما خلصت، متل اليوم: I've sent 10 emails so far today.",
            "الشكل: have / has + التصريف التالت (past participle): sent, made, been, done.",
            "الأفعال النظامية: worked → worked. والشاذة شوفها بصفحة Irregular Verbs (العامود التالت).",
        ],
        en=[
            "Today isn't finished: I{'ve sent} ten emails so far today.",
            "have / has + the third form of the verb: sent, made, been, done.",
            "Regular verbs: worked → worked. Irregular: see the Irregular Verbs page.",
        ],
        watch=[("I have send three emails.", "I've sent three emails."), ("She have made two calls.", "She's made two calls."), ("I've sent ten emails yesterday.", "I sent ten emails yesterday.")],
        quick="""
## choose: Choose the answer.
I ___ sent three emails so far today. | 've | 's | am
She ___ made five phone calls. | 's | 've | is
Have you uploaded the photos? — Yes, I ___. | have | did | 've
""",
        sets="""
## choose: Choose the answer.
I've ___ ten text messages so far today. | sent | send | sending
Hadi ___ repaired six phones today. | has | have | is
We ___ had any emails this morning. | haven't | hasn't | didn't
___ you checked your voicemail? | Have | Has | Did
She's ___ two coffees so far today. | drunk | drink | drinking
Have they downloaded the app? — No, they ___. | haven't | didn't | don't
I've ___ my password three times today! | forgotten | forget | forgot
Maya ___ updated her status four times today. | has | have | is
How many emails ___ you sent today? | have | has | did
He's ___ on hold three times today. | been | be | being #id=a22u14-8c14aed
## gap: Write the past participle.
I've [sent] five emails. (send)
She's [made] three phone calls. (make)
We've [downloaded] the new app. (download)
Have you [seen] my phone? (see)
He's [written] two reports today. (write)
I've [been] on hold twice today. (be) #id=a22u14-dfd37f3
They've [uploaded] the photos. (upload)
Have you [done] your homework? (do)
## gap: Write have, has, haven't or hasn't.
I [have|'ve] sent the email.
Rana [has|'s] made a lot of phone calls today.
We [haven't|have not] used the internet today. No connection!
[Have] you checked your voicemail?
Hadi [hasn't|has not] answered my messages.
They [have|'ve] uploaded the wedding photos.
[Has] she apologised?
I [haven't|have not] had lunch yet.
## transform: Make the sentence negative (−).
I've sent the email. (−) => I haven't sent the email. | I have not sent the email.
She's made a phone call. (−) => She hasn't made a phone call. | She has not made a phone call.
We've downloaded the app. (−) => We haven't downloaded the app. | We have not downloaded the app.
He's checked his voicemail. (−) => He hasn't checked his voicemail. | He has not checked his voicemail.
They've uploaded the photos. (−) => They haven't uploaded the photos. | They have not uploaded the photos.
I've changed my password. (−) => I haven't changed my password. | I have not changed my password.
Maya has updated her status. (−) => Maya hasn't updated her status. | Maya has not updated her status.
You've apologised. (−) => You haven't apologised. | You have not apologised.
## fix: Find and fix the mistake.
I have [send>sent] three emails.
She [have>has|'s] made two calls.
[Did>Have] you uploaded the photos?
He's [forget>forgotten] his password.
We [hasn't>haven't] had any emails today.
Have you [saw>seen] my phone?
I've [wrote>written] a lot of messages.
They [has>have|'ve] downloaded the app.
## order: Put the words in order.
I've sent ten emails so far today.
She's made five phone calls.
Have you checked your voicemail?
We haven't used the internet today.
He's been on hold three times today. #id=a22u14-33d1c27
Have they uploaded the photos?
I haven't changed my password.
How many messages have you sent today?
""",
    ),
    dict(
        id="g2",
        title="Present perfect with ever / never",
        visual=dict(type="timeline", now="now", span={"from": -3, "to": 0, "label": "your whole life until now"},
                    marks=[dict(at=-3, label="born"), dict(at=0, label="Have you ever…?")]),
        pattern=[
            ["?", ["Have", "v"], "you", ["ever", "x"], "used video chat?"],
            ["", "Yes, I", ["have.", "v"], ""],
            ["", "No, I", ["haven't.", "n"], "I've never used it."],
            ["+", "She", ["'s been", "v"], "to London. (been = gone and come back)"],
        ],
        examples=[
            "{Have} you {ever} lost your phone? — Yes, {I have}!",
            "I{'ve never} used a landline.",
            "{Has} Hadi {ever} met a hacker? — No, {he hasn't}.",
            "Kenji{'s been} to Damascus three times.",
        ],
        ar=[
            "Have you ever…? يعني 'هل سبق و…؟' بأي وقت بحياتك.",
            "never يعني 'أبداً ما…': I've never been to London.",
            "إذا ذكرنا وقت محدد بالماضي منرجع للماضي البسيط: I went to London in 2019.",
        ],
        en=[
            "Have you {ever}…? = at any time in your life.",
            "{never} = not at any time: I{'ve never} been to London.",
            "With a past time (yesterday, in 2019), use the past: I {went} in 2019.",
        ],
        watch=[("Did you ever use video chat?", "Have you ever used video chat?"), ("I've never went to London.", "I've never been to London."), ("I've been to London last year.", "I went to London last year.")],
        quick="""
## choose: Choose the answer.
Have you ___ used video chat? | ever | yet | no #id=a22u14-9e851d0
I've ___ been to London. | never | ever | no #id=a22u14-a9c50ee
Has she ever lost her phone? — Yes, she ___. | has | did | have
""",
        sets="""
## choose: Choose the answer.
Have you ever ___ a wrong number? | dialled | dial | dialling
I've ___ been to Tokyo. | never | ever | no
___ she ever used a landline? | Has | Have | Did
Have you ever met a famous person? — No, I ___. | haven't | didn't | don't
Hadi has ___ a lot of phones. | repaired | repair | repairing
Have they ever ___ to Paris? | been | gone to | was
I've never ___ text speak. I hate it! | used | use | using
Has your computer ever had a virus? — Yes, it ___. | has | did | is
Have you ever ___ your password? | forgotten | forgot | forget
She's ___ been on a plane. She's afraid of flying. | never | ever | yet #id=a22u14-c5f035e
## short: Answer the question.
Have you ever lost your phone? (✓) => Yes, I have.
Has she ever used video chat? (✗) => No, she hasn't. | No, she has not.
Have they ever been to Paris? (✓) => Yes, they have.
Have you ever met a hacker? (✗) => No, I haven't. | No, I have not.
Has Hadi ever repaired a laptop? (✓) => Yes, he has.
Have you ever written a poem? (✗) => No, I haven't. | No, I have not.
Has your laptop ever had a virus? (✓) => Yes, it has.
Have we ever had a virus on this computer? (✗) => No, we haven't. | No, we have not. #id=a22u14-5cfb968
## transform: Write the question with ever.
you / use / video chat => Have you ever used video chat?
she / lose / her phone => Has she ever lost her phone?
they / be / to London => Have they ever been to London?
he / meet / a famous person => Has he ever met a famous person?
you / dial / a wrong number => Have you ever dialled a wrong number? | Have you ever dialed a wrong number?
your laptop / have / a virus => Has your laptop ever had a virus?
you / send / a voice message => Have you ever sent a voice message?
Maya / sing / on stage => Has Maya ever sung on stage?
## transform: Write the sentence with never.
I / be / to Tokyo => I've never been to Tokyo. | I have never been to Tokyo.
She / use / a landline => She's never used a landline. | She has never used a landline.
We / lose / our passwords => We've never lost our passwords. | We have never lost our passwords.
He / write / a poem => He's never written a poem. | He has never written a poem.
They / see / snow => They've never seen snow. | They have never seen snow.
I / meet / a hacker => I've never met a hacker. | I have never met a hacker.
My grandmother / send / an email => My grandmother has never sent an email. | My grandmother's never sent an email.
Hadi / be / on time => Hadi has never been on time. | Hadi's never been on time.
## fix: Find and fix the mistake.
[Did you ever>Have you ever] used video chat?
I've never [went>been] to London.
Have you ever [lose>lost] your phone?
She's [ever>never] been to Japan. She'd like to go.
[Have>Has] he ever met a hacker?
I've [being>been] to Dubai twice.
They have never [saw>seen] snow.
Has she ever [writed>written] a poem?
## order: Put the words in order.
Have you ever used video chat?
I've never been to London.
Has she ever lost her phone?
We've never met a hacker.
Have they ever been to Istanbul?
My grandmother has never sent an email.
Has your laptop ever had a virus?
I've never forgotten my password.
""",
    ),
    dict(
        id="g3",
        title="Technology",
        visual=dict(type="chips", groups=[
            dict(title="devices", color="purple", items=["smartphone", "landline", "laptop", "tablet computer"]),
            dict(title="actions", color="teal", items=["send an email", "send an attachment", "upload", "download", "update your status", "use video chat"]),
            dict(title="safety", color="coral", items=["password", "username", "anti-virus software", "hacker", "virus"]),
            dict(title="on the phone", color="amber", items=["make a phone call", "leave a voice message", "pick up voicemail", "be on hold", "dial a wrong number"]),
        ]),
        pattern=[
            ["", "I", ["send an email", "v"], "with an attachment."],
            ["", "You need a", ["username", "x"], "and a password."],
            ["", "Install", ["anti-virus software", "n"], "to stop viruses."],
        ],
        examples=[
            "I've {uploaded} the photos and {sent} the {attachment}.",
            "Never tell anyone your {password}.",
            "I was {on hold} for half an hour!",
            "We {use video chat} to talk to my uncle in Dubai.",
        ],
        ar=[
            "upload = نرفع ع الإنترنت، download = ننزّل من الإنترنت.",
            "landline = تلفون أرضي، smartphone = موبايل ذكي.",
            "be on hold = ننطر ع الخط، leave a voice message = نترك رسالة صوتية.",
        ],
        en=[
            "{upload} = send to the internet. {download} = get from the internet.",
            "{landline} = a phone at home. {smartphone} = a phone with the internet.",
            "{be on hold} = wait on the phone. {leave a voice message} = speak after the beep.",
        ],
        watch=[("I opened the internet.", "I accessed the internet. / I went online."), ("I downloaded my photos to Facebook.", "I uploaded my photos to Facebook."), ("I called a false number.", "I dialled a wrong number.")],
        quick="""
## choose: Choose the answer.
A phone at home with a wire: | landline | smartphone | tablet computer
A secret word for your account: | password | username | hotspot
To get a file from the internet: | download | upload | update
""",
        sets="""
## choose: Choose the right word.
A person who gets into your computer: | a hacker | a username | a landline
A program that damages computers: | a virus | anti-virus software | a hotspot
A program that protects computers: | anti-virus software | a virus | a hacker
A place with free Wi-Fi: | a Wi-Fi hotspot | a landline | a password
To send files to the internet: | upload | download | dial
To write news about you online: | update your status | pick up voicemail | dial a number
To wait on the phone with music: | be on hold | send an attachment | upload
To listen to your voice messages: | pick up voicemail | update your status | be on hold
To call the wrong person: | dial a wrong number | use video chat | upload
Short words in messages like "u" and "l8r": | text speak | username | password
## match: Match.
upload = send files to the internet
download = get files from the internet
password = a secret word
username = your name on a website
hacker = a person who breaks into computers
landline = a phone with a wire at home
voicemail = voice messages on your phone
attachment = a file with an email
## bank: Use the words.
I can't send it — the internet [connection] is very slow.
Have you installed [anti-virus] software?
Don't tell anyone your [password].
I've [uploaded] the wedding photos.
I was on [hold] for thirty minutes!
Sorry, I dialled [a wrong] number.
We use video [chat] with my cousin in Toronto.
Did you get my [attachment]? It's the report.
## sort: Device or action? | device | action
device: smartphone, landline, laptop, tablet computer
action: upload, download, send an email, dial a number
## order: Put the words in order.
I've uploaded the photos.
Have you installed anti-virus software?
Never tell anyone your password.
I was on hold for an hour.
We use video chat every week.
Sorry, I dialled a wrong number.
The internet connection is very slow.
Have you sent the attachment?
""",
    ),
]

CLASSROOM = dict(
    phrases=["Sorry, I missed the last lesson. Have I missed anything important?", "Have you finished?", "Could you check my writing, please?",
             "I'm not sure, but I think …", "Is there another way to say …?", "What's the opposite of …?", "Well done!"],
    order="""
S: Sorry, I missed the last lesson. Have I missed anything important?
T: We started the present perfect. Look at page 126.
S: What's the opposite of 'upload'?
T: Download.
S: Have you finished? Could you check my writing, please?
T: Of course. Well done — only one mistake!
""",
)

READING = dict(
    title="A day without the internet",
    text="""Last month, Hadi's phone shop in Bab Touma lost its internet connection for a whole day. "It was a disaster," he says. "I started repairing phones six years ago, and I've never had a day like that!"

Usually, Hadi uses the internet all day. He sends emails to customers, he downloads software for the phones, and he updates his shop's status on social networking sites. "So far today, I've sent twenty-five messages, and it's only midday!" he laughs.

On the day with no connection, he had to use the old landline in the shop. He made a lot of phone calls, and he was on hold for forty minutes with the internet company. Some customers got angry, and Hadi apologised a lot.

But there was a good side. "I talked to my customers face to face," he says. "Have you ever had a real conversation in a phone shop? It was really nice! I've decided to have one 'no-internet hour' every week." His friend Jad loves the idea. "I turned off my phone for an hour this morning," he says. "I didn't miss anything — and I've read ten pages of a real book!"

Have you ever spent a day without the internet? Can you do it?""",
    qs="""
## tf: True or false?
Hadi's shop lost its internet connection for a week. | F @ lost its internet connection for a whole day
Hadi started repairing phones six years ago. | T @ I started repairing phones six years ago #id=a22u14-8a74a76
He has sent twenty-five messages so far today. | T @ So far today, I've sent twenty-five messages
Hadi was on hold for ten minutes. | F @ he was on hold for forty minutes
Some customers got angry. | T @ Some customers got angry
## choose: Choose the answer.
What did Hadi use on the day with no connection? | the old landline | video chat | a Wi-Fi hotspot @ he had to use the old landline in the shop
What has Hadi decided? | to have a 'no-internet hour' every week | to close the shop | to buy a new landline @ I've decided to have one 'no-internet hour' every week
## gap: Write one word.
Hadi [apologised] a lot to his customers. @ Hadi apologised a lot
""",
)

DIALOGUE = dict(
    title="Have you sent it?",
    intro="An office in Malki. Ziad and his colleague Sana prepare a report.",
    task="gaps",
    lines="""
Ziad: Sana, have you [sent] the report to the manager?
Sana: Not yet. I've [written] it, but the internet connection is very slow.
Ziad: Have you [tried] the Wi-Fi in the meeting room?
Sana: Yes, I have. It's slow there, too.
Ziad: OK. Have you [ever] used the Wi-Fi hotspot in the café downstairs?
Sana: No, I [haven't]. Is it good?
Ziad: It's fantastic. And don't forget the [attachment]!
Sana: Don't worry — I've [never] forgotten an attachment!
""",
)

WQ = """
Yes, I have. Ten emails. (you / send / any emails today) => Have you sent any emails today?
No, I've never been there. (you / ever / be / to London) => Have you ever been to London?
Twenty-five. (How many messages / you / send / so far today) => How many messages have you sent so far today?
Yes, she has. Last year! (Rana / ever / lose / her phone) => Has Rana ever lost her phone?
No, he hasn't. He hates it. (Hadi / ever / use / text speak) => Has Hadi ever used text speak?
Yes, we have. They're on the website. (you / upload / the photos) => Have you uploaded the photos?
No, I haven't. I'll do it now. (you / change / your password) => Have you changed your password?
Yes, it has. Twice! (your laptop / ever / have / a virus) => Has your laptop ever had a virus?
"""

WRITING = [
    dict(task="Write about you and technology. What have you done so far today with your phone or computer? What have you ever (or never) done?",
         tip="Use the present perfect with so far today, ever and never. Write 90–130 words.",
         model="So far today, I've sent about thirty text messages and I've made three phone calls. I've checked my email twice, and I've downloaded a new English dictionary app. I haven't updated my status — I don't use social networking sites much.\nI've used video chat a lot, because my brother lives in Toronto. I've never met a hacker, but my laptop has had a virus once. Now I always use anti-virus software. I've never lost my phone, but I've forgotten my password many times! Have you ever spent a whole week without the internet? I haven't — and I don't want to try!",
         check=["have / has + past participle", "so far today", "Have you ever…? / I've never…", "technology words: download, password, video chat…"],
         min=90, max=130),
]

CANDO = [
    "use the present perfect with so far today.",
    "ask 'Have you ever…?' and answer.",
    "say what I've never done.",
    "talk about phones, computers and the internet.",
    "understand a story about technology.",
]
