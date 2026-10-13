"""Level gate: no grammar from a later unit in an earlier unit's student-facing text.

Each rule has the unit where the grammar is introduced. A text in unit u breaks every rule
whose unit is > u. 99 = never taught in that book. Fixed chunks (classroom English, the
unit's book words and a few starter chunks) are removed before checking.
"""
import re

NEVER = 99

PAST_IRREG = (
    "went had saw came took ate drank wrote became gave said told found sold began ran swam sang drove "
    "flew knew thought bought brought met sent spent taught caught felt kept paid sat slept stood "
    "understood wore woke broke chose fell forgot heard held rang rode spoke stole threw did won made "
    "grew drew hid shook"
).split()

PAST_PARTICIPLES = (
    "been seen done gone eaten drunk written taken given known spoken broken chosen forgotten won met bought "
    "brought sent spent made had heard found lost left read tried finished visited started played watched "
    "lived worked studied used travelled called opened downloaded uploaded updated received cooked cleaned "
    "booked changed decided flown driven ridden swum sung begun become"
).split()

ED_OK = set((
    "interested tired married retired bored excited crowded worried surprised red bed need feed speed seed "
    "shed hundred naked wicked sacred beloved closed united fried grilled boiled baked stuffed mixed dried "
    "roasted sliced salted smoked toasted talented coloured colored relaxed organised organized experienced "
    "skilled advanced detailed unemployed employed disabled pleased confused embarrassed amazed annoyed scared "
    "frightened shocked delighted satisfied qualified limited indeed weed breed shaped skied wed sled "
    "air-conditioned old-fashioned self-employed handed left-handed right-handed fred bled led fed "
    "medicated dedicated complicated sophisticated stressed packed"
).split())

ING_OK = set((
    "boring interesting exciting amazing relaxing frightening morning evening something nothing everything "
    "anything king thing ring spring wedding building ceiling evening during shopping swimming clothing "
    "sightseeing surprising tiring annoying confusing charming"
).split())

FAMILY_ETC = (
    "mother|father|brother|sister|wife|husband|son|daughter|parents|children|child|family|grandmother|"
    "grandfather|grandparents|grandson|granddaughter|grandchildren|friend|friends|car|house|flat|book|bag|"
    "name|phone|job|shop|café|restaurant|office|baby|cat|dog|birthday|uncle|aunt|cousin|"
    "nephew|niece|keys|key|wallet|camera|watch|glasses|room|kitchen|garden|bike|laptop|address|number"
)

PP_RE = "|".join(PAST_PARTICIPLES)


def _rx(p, flags=re.I):
    return re.compile(p, flags)


def f_is_u1(text):
    """'is' / 's before Starter U2, except the U1 chunks 'my/your … is', 'what's', 'name's'."""
    hits = []
    for m in re.finditer(r"\b(is|isn't)\b", text, re.I):
        before = text[max(0, m.start() - 40):m.start()].lower()
        if re.search(r"(\b(my|your)|___)\s+([\w-]+\s+){0,2}$", before) or re.search(r"\bwhat\s+$", before):
            continue
        hits.append(m.group(0))
    for m in re.finditer(r"\b([\w-]+)'s\b", text, re.I):
        if m.group(1).lower() in ("what", "name", "let", "number", "address", "surname", "job", "xchunkx"):
            continue
        hits.append(m.group(0))
    return hits


def f_plural_are(text):
    """'are/aren't' with anything but 'you' (plural be = Starter U3)."""
    hits = []
    toks = re.findall(r"[\w']+", text.lower())
    for i, t in enumerate(toks):
        if t in ("are", "aren't"):
            prev = toks[i - 1] if i else ""
            nxt = toks[i + 1] if i + 1 < len(toks) else ""
            if prev == "you" or nxt == "you":
                continue
            if not nxt or nxt in ("or", "and") or prev in ("or", "and", "write", "choose"):
                continue  # talking about the word: "am or are"
            hits.append(t)
    return hits


def f_continuous(text, allow_going_to=False):
    hits = []
    for m in re.finditer(r"\b(am|is|are|'m|'s|'re|isn't|aren't|was|were|wasn't|weren't)\s+(not\s+)?([a-z]+ing)\b", text, re.I):
        w = m.group(3).lower()
        if w in ING_OK:
            continue
        if w == "going":
            after = text[m.end():m.end() + 30].lower()
            if re.match(r"\s+to\b(?!\s+(the|a|an|my|your|his|her|our|their|school|work|bed|university|town)\b)", after):
                continue  # 'going to' + verb is handled by its own rule
        hits.append(m.group(0))
    return hits


def f_going_to(text):
    return [m.group(0) for m in re.finditer(
        r"\bgoing\s+to\s+(?!the\b|a\b|an\b|my\b|your\b|his\b|her\b|our\b|their\b|school\b|work\b|bed\b|university\b|town\b)[a-z]+",
        text, re.I)]


def f_past_ed(text):
    hits = []
    for m in re.finditer(r"(?<![\w'-])([a-z][a-z-]*ed)\b", text):  # lowercase only: skips names like Khaled
        w = m.group(1)
        if w in ED_OK or w.endswith("eed") or len(w) <= 3:
            continue
        hits.append(w)
    return hits


def f_past_irreg(text):
    hits = []
    for w in PAST_IRREG:
        for m in re.finditer(rf"\b{w}\b", text, re.I):
            hits.append(m.group(0))
    for m in re.finditer(r"\bgot\b", text, re.I):
        before = text[max(0, m.start() - 20):m.start()].lower()
        if re.search(r"(have|has|'ve|'s|haven't|hasn't)\s+((you|we|they|i|he|she|it)\s+)?$", before):
            continue  # 'have got' has its own rule
        hits.append("got")
    return hits


def f_superlative(text):
    hits = []
    for m in re.finditer(r"\bthe\s+([a-z]+est)\b", text, re.I):
        w = m.group(1).lower()
        if w in ("rest", "test", "west", "guest", "forest", "chest", "nest", "interest", "request", "contest",
                 "protest", "harvest", "honest", "modest", "best"):
            continue
        hits.append(m.group(0))
    return hits


def f_present_perfect(text):
    pat = rf"\b(have|has|'ve|haven't|hasn't)\s+((you|he|she|it|we|they|i)\s+)?(ever\s+|never\s+|just\s+|already\s+|not\s+)?({PP_RE})\b"
    hits = [m.group(0) for m in re.finditer(pat, text, re.I)]
    hits += [m.group(0) for m in re.finditer(rf"\b\w+'s\s+(ever\s+|never\s+|just\s+|already\s+)?(been|gone|done|seen|finished|eaten)\b", text, re.I)]
    return hits


def f_did_question(text):
    """'did' used to make a question: at the start of a sentence, or in a sentence ending with '?'."""
    hits = []
    for sent in re.split(r"(?<=[.!?])\s+|\n", text):
        for m in re.finditer(r"\bdid\s+(?!not\b|n't\b)([a-z]+)", sent, re.I):
            before = sent[:m.start()].strip().lower()
            if sent.rstrip().endswith("?") or before == "" or re.search(r"(what|where|when|who|why|how|which|whose|time|often|long|much|many)$", before):
                hits.append(m.group(0))
    return hits


def rule(unit, name, pat=None, fn=None):
    return {"unit": unit, "name": name, "rx": _rx(pat) if pat else None, "fn": fn}


COMPARATIVE = r"\b[a-z]+er\s+than\b|\bmore\s+[a-z]+\s+than\b|\bless\s+[a-z]+\s+than\b|\bthe\s+(most|least)\b|\b(better|worse|best|worst)\b"
WILL = r"\bwill\b|\bwon't\b|\b(i|you|he|she|it|we|they|that|there)'ll\b"
WOULD = r"\bwould\b|\b(i|you|he|she|we|they)'d\b"
HAVE_TO = r"\b(have|has|had|having)\s+to\b"
HAVE_GOT = r"\b(have|has|'ve|'s|haven't|hasn't)\s+((you|he|she|it|we|they|i)\s+)?got\b"
CAN = r"\b(can|can't|cannot)\b"
WAS = r"\b(was|were|wasn't|weren't)\b"

STARTER = [
    rule(2, "he/she/it, his/her/our/their (U2)", r"\b(he|she|it|his|her|hers|its|our|ours|their|theirs|he's|she's|it's)\b"),
    rule(2, "is / 's with he, she, it (U2)", fn=f_is_u1),
    rule(3, "this/that/these/those, we/they (U3)", r"\b(this|that|these|those|we|they|we're|they're|us|them|that's)\b"),
    rule(3, "plural are (U3)", fn=f_plural_are),
    rule(4, "there is / there are (U4)", r"\bthere\s+(is|are|isn't|aren't)\b|\bthere's\b|\b(is|are|isn't|aren't)\s+there\b"),
    rule(4, "some / any / a lot of (U4)", r"\b(some|any|a lot of|lots of)\b"),
    rule(4, "prepositions of place (U4)", r"\b(next to|opposite|behind|between|in front of|under)\b|\bnear\s+(the|a|an|my|your|his|her|our|their|here|[A-Z])"),
    rule(5, "possessive 's (U5)", rf"\b(?!(?:it|he|she|that|what|there|let|here|who|where|how|this|name)'s)[\w-]+'s\s+(\w+\s+)?({FAMILY_ETC})\b"),
    rule(5, "present simple do/don't (U5)", r"\b(do|don't)\b"),
    rule(5, "present simple I/you/we/they (U5)", r"\b(i|you|we|they)\s+(live|work|like|have|go|study|speak|eat|drink|play|teach|love|know|need|read|watch|cook|get|make|start|finish|hate|use|listen|buy|travel|meet|visit|walk|drive|sell|take|come|leave|sleep|wake|sing|dance|swim|run|write|help|open|close|stay|wear|pay|ask|try|see|feel|say|think)\b"),
    rule(6, "does / doesn't (U6)", r"\b(does|doesn't)\b"),
    rule(6, "present simple he/she/it -s (U6)", r"\b(lives|works|likes|has|goes|studies|speaks|eats|drinks|plays|teaches|watches|loves|hates|reads|cooks|uses|gets|starts|finishes|wants|knows|needs|makes|says|sells|drives|runs|swims|walks|listens|travels|buys|meets|visits|takes|comes|leaves|sleeps|wakes|sings|dances|writes|helps|stays|wears|pays|tries|sees|feels|thinks|does)\b"),
    rule(7, "frequency adverbs (U7)", r"\b(always|usually|often|sometimes|never|hardly ever|rarely)\b"),
    rule(7, "Wh- questions with do/does (U7)", r"\b(what|where|when|who|why|how|which|whose)\s+([a-z]+\s+)?(do|does)\b"),
    rule(8, "can / can't (U8)", CAN),
    rule(9, "was / were (U9)", WAS),
    rule(10, "past simple: didn't (U10)", r"\bdidn't\b"),
    rule(10, "past simple irregular (U10)", fn=f_past_irreg),
    rule(10, "past simple regular -ed (U10)", fn=f_past_ed),
    rule(11, "past simple questions: did + subject (U11)", fn=f_did_question),
    rule(12, "want / want to (U12)", r"\b(want|wants|wanted)\b"),
    rule(12, "going to + verb (U12)", fn=f_going_to),
    rule(NEVER, "present continuous (not in Starter)", fn=f_continuous),
    rule(NEVER, "comparatives / superlatives (not in Starter)", COMPARATIVE),
    rule(NEVER, "superlative -est (not in Starter)", fn=f_superlative),
    rule(NEVER, "will (not in Starter)", WILL),
    rule(NEVER, "would (not in Starter)", WOULD),
    rule(NEVER, "might (not in Starter)", r"\bmight\b"),
    rule(NEVER, "have to (not in Starter)", HAVE_TO),
    rule(NEVER, "have got (not in Starter)", HAVE_GOT),
    rule(NEVER, "present perfect (not in Starter)", fn=f_present_perfect),
    rule(NEVER, "could/should/must (not in Starter)", r"\b(could|couldn't|should|shouldn't|must|mustn't)\b"),
]

ELEMENTARY = [
    rule(2, "have got (U2)", HAVE_GOT),
    rule(3, "do / does / don't / doesn't (U3)", r"\b(do|does|don't|doesn't)\b"),
    rule(5, "can / can't (U5)", CAN),
    rule(7, "was / were (U7)", WAS),
    rule(7, "past simple irregular (U7)", fn=f_past_irreg),
    rule(7, "past simple regular -ed (U7)", fn=f_past_ed),
    rule(8, "past simple negative (U8)", r"\bdidn't\b|\bdid\s+not\b"),
    rule(8, "past simple questions (U8)", fn=f_did_question),
    rule(9, "comparatives / superlatives (U9)", COMPARATIVE),
    rule(9, "superlative -est (U9)", fn=f_superlative),
    rule(10, "present continuous (U10)", fn=f_continuous),
    rule(12, "going to + verb (U12)", fn=f_going_to),
    rule(12, "will (U12)", WILL),
    rule(12, "would like (U12)", WOULD),
    rule(13, "have to (U13)", HAVE_TO),
    rule(13, "might (U13)", r"\bmight\b"),
    rule(14, "present perfect (U14)", fn=f_present_perfect),
    rule(NEVER, "could/should/must (not in this book's list)", r"\b(could|couldn't|should|shouldn't|must|mustn't)\b"),
]

BASE_CHUNKS = [
    "How do you spell", "How old are you", "I don't know", "I think", "See you", "Nice to meet you",
    "best friend", "What does … mean", "How do you say", "How are you", "I'm fine", "Thank you",
]


def chunk_regex(chunks):
    parts = []
    for c in sorted(set(c for c in chunks if c and len(c) > 2), key=len, reverse=True):
        c = c.strip().rstrip(".?!")
        esc = re.escape(c)
        esc = esc.replace(re.escape("…"), r"[\w' ,.-]{0,40}?").replace(re.escape("..."), r"[\w' ,.-]{0,40}?")
        parts.append(esc)
    if not parts:
        return None
    return re.compile(r"(?<![\w])(" + "|".join(parts) + r")(?![\w])", re.I)


class LevelGate:
    def __init__(self, series, chunks):
        self.rules = STARTER if series == "starter" else ELEMENTARY
        self.chunk_rx = chunk_regex(BASE_CHUNKS + list(chunks))

    def strip(self, text, extra_rx=None):
        t = text.replace("\u2019", "'").replace("{", "").replace("}", "")
        if self.chunk_rx is not None:
            t = self.chunk_rx.sub(" xchunkx ", t)
        if extra_rx is not None:
            t = extra_rx.sub(" xchunkx ", t)
        return t

    def check(self, text, unit, extra_rx=None, short=False):
        """short=True: a one- or two-word option on its own; rules that need the sentence around are skipped."""
        t = self.strip(text, extra_rx)
        out = []
        for r in self.rules:
            if r["unit"] <= unit:
                continue
            if short and r["fn"] in (f_is_u1, f_plural_are):
                continue
            hits = r["fn"](t) if r["fn"] else [m.group(0) for m in r["rx"].finditer(t)]
            if hits:
                out.append((r["name"], sorted(set(h.strip() for h in hits))))
        return out
