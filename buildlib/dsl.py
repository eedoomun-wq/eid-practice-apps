"""Parser for the exercise mini-language used in content/*.py files.

A block of sets looks like this:

    ## choose: Choose the answer.
    I ___ a student. | am | are | is          (first option is the right one)
    ## gap: Write the missing word.
    I [am|'m] from Damascus.                  ([right|also right])
    ## order: Put the words in order.
    How are you?  || How you are?             (|| = other correct orders)
    ## fix: Find and fix the mistake.
    I [are>am|'m] a student.                  ([wrong>right|also right])
    ## match: Match.
    hello = goodbye
    ## sort: Sort the words. | a | an
    a: teacher, student
    ## bank: Use the words. | +extra, words
    I [am] Layla.
    ## transform: Make it negative.           (also: short, wq, numbers, spell)
    I'm a teacher. (−) => I'm not a teacher. | I am not a teacher.
    ## tf: True or false?
    Layla is a student. | T @ evidence from the text
    ## odd: Which one is different?
    teacher, student, *pizza, actor | Pizza is food.

Lines starting with // are comments. " @ evidence" (reading only) must be a
phrase copied from the reading text; the build checks it is really there.
"""
import hashlib
import re

SET_TYPES = {
    "choose": "choice", "tf": "choice", "odd": "choice",
    "gap": "typed", "transform": "typed", "short": "typed", "wq": "typed",
    "numbers": "typed", "spell": "typed",
    "bank": "bank", "order": "order", "fix": "fix", "match": "pair", "sort": "sortit",
}

CUES = {"(−)": "−", "(-)": "−", "(?)": "?", "(+)": "+", "(✓)": "✓", "(✗)": "✗"}
CUE_RE = re.compile(r"\s*\((−|-|\?|\+|✓|✗)\)\s*$")
END_PUNCT = ".?!"


class DslError(Exception):
    pass


def h6(*parts):
    return hashlib.sha1("\x1f".join(parts).encode("utf-8")).hexdigest()[:7]


def split_alts(s):
    return [a.strip() for a in s.split("|") if a.strip()]


def one_gap(line, where):
    m = list(re.finditer(r"\[([^\]]+)\]", line))
    if len(m) != 1:
        raise DslError(f"{where}: need exactly one [gap] in: {line}")
    m = m[0]
    q = line[: m.start()] + "___" + line[m.end():]
    return q.strip(), split_alts(m.group(1))


def tokens_for_tiles(sentence, proper):
    s = sentence.strip()
    end = ""
    if s and s[-1] in END_PUNCT:
        end = s[-1]
        s = s[:-1].rstrip()
    toks = s.split()
    if toks:
        first = toks[0]
        bare = re.sub(r"[^\w']", "", first)
        keep = bare in proper or bare.startswith("I'") or bare == "I"
        if not keep:
            toks[0] = first[0].lower() + first[1:]
    return toks, end


class Ctx:
    def __init__(self, unitkey, registry, proper, errors):
        self.unitkey = unitkey
        self.registry = registry  # id -> item (whole unit)
        self.proper = proper
        self.errors = errors
        self.seen = {}  # dedupe key -> where

    def add(self, item, dedupe_key, where):
        iid = f"{self.unitkey}-{h6(item['k'], dedupe_key)}"
        if iid in self.registry or dedupe_key in self.seen:
            self.errors.append(f"[data] duplicate item in {self.unitkey}: {where}: {dedupe_key[:80]}")
            iid = iid + "x" + str(len(self.registry))
        self.seen[dedupe_key] = where
        item["id"] = iid
        self.registry[iid] = item
        return iid


def parse_item(k, line, header_extra, ctx, where):
    t = SET_TYPES[k]
    ev = None
    if " @ " in line:
        line, ev = line.split(" @ ", 1)
        line, ev = line.strip(), ev.strip()
    it = {"k": k, "t": t}
    if ev:
        it["ev"] = ev
    if k == "choose":
        parts = [p.strip() for p in line.split(" | ")]
        if len(parts) < 3:
            raise DslError(f"{where}: choose needs a stem and 2+ options: {line}")
        it.update(q=parts[0], o=parts[1:], a=0)
        key = parts[0] + "|" + "|".join(parts[1:])
    elif k == "tf":
        parts = [p.strip() for p in line.split(" | ")]
        if len(parts) != 2 or parts[1] not in ("T", "F"):
            raise DslError(f"{where}: tf needs 'statement | T/F': {line}")
        it.update(q=parts[0], o=["True", "False"], a=0 if parts[1] == "T" else 1, tf=True)
        key = parts[0]
    elif k == "odd":
        body, _, reason = line.partition(" | ")
        opts = [o.strip() for o in body.split(",") if o.strip()]
        stars = [i for i, o in enumerate(opts) if o.startswith("*")]
        if len(stars) != 1 or len(opts) < 3:
            raise DslError(f"{where}: odd needs 3+ words and one *odd: {line}")
        opts = [o.lstrip("*").strip() for o in opts]
        # put the odd one first, the shuffler moves it
        odd = opts.pop(stars[0])
        it.update(q="", o=[odd] + opts, a=0, fb=reason.strip())
        key = ",".join(sorted([odd] + opts))
    elif k in ("gap",):
        q, acc = one_gap(line, where)
        it.update(q=q, acc=acc)
        key = q + "=" + acc[0]
    elif k == "bank":
        q, acc = one_gap(line, where)
        it.update(q=q, acc=acc)
        key = q + "=" + acc[0]
    elif k in ("transform", "short", "wq", "numbers", "spell"):
        if "=>" not in line:
            raise DslError(f"{where}: {k} needs 'prompt => answer': {line}")
        prompt, ans = [p.strip() for p in line.split("=>", 1)]
        cue = None
        m = CUE_RE.search(prompt)
        if m:
            cue = CUES["(" + m.group(1) + ")"]
            prompt = prompt[: m.start()].strip()
        it.update(q=prompt, acc=split_alts(ans))
        if k == "spell":
            it["spell"] = 1
        if cue:
            it["cue"] = cue
        key = prompt + "=" + it["acc"][0] + (cue or "")
    elif k == "order":
        alts = [a.strip() for a in line.split("||") if a.strip()]
        toks, end = tokens_for_tiles(alts[0], ctx.proper)
        if len(toks) < 2:
            raise DslError(f"{where}: order needs 2+ words: {line}")
        it.update(acc=alts, toks=toks, end=end)
        key = alts[0]
    elif k == "fix":
        full_alts = []
        if "||" in line:
            line, rest = line.split("||", 1)
            full_alts = [a.strip() for a in rest.split("||") if a.strip()]
            line = line.strip()
        m = list(re.finditer(r"\[([^\]>]+)>([^\]]+)\]", line))
        if len(m) != 1:
            raise DslError(f"{where}: fix needs one [wrong>right]: {line}")
        m = m[0]
        before, bad, good, after = line[: m.start()], m.group(1).strip(), m.group(2), line[m.end():]
        goods = split_alts(good)
        btoks, badtoks, atoks = before.split(), bad.split(), after.split()
        # punctuation glued to the span ("[go>goes]." ) stays on the last bad token
        if after and not after.startswith(" ") and atoks:
            glue = atoks.pop(0)
            badtoks[-1] += glue
            goods = [g + glue for g in goods]
        if before and not before.endswith(" ") and btoks:
            raise DslError(f"{where}: put a space before [wrong>right]: {line}")
        tokens = btoks + badtoks + atoks
        bad_idx = list(range(len(btoks), len(btoks) + len(badtoks)))
        full = " ".join(btoks + [goods[0]] + atoks)
        it.update(tokens=tokens, bad=bad_idx, acc=[re.sub(r"[.?!,]$", "", g) for g in goods],
                  full=full, fulls=[full] + full_alts)
        key = line
    elif k == "match":
        if " = " not in line:
            raise DslError(f"{where}: match needs 'left = right': {line}")
        l, r = [p.strip() for p in line.split(" = ", 1)]
        it.update(l=l, r=r)
        key = l + "=" + r
    elif k == "sort":
        raise DslError("sort lines are parsed by the set")
    else:
        raise DslError(f"{where}: unknown type {k}")
    return it, key


def parse_sets(text, ctx, where):
    """Parse a block that may contain several ## sets. Returns a list of set dicts."""
    sets = []
    cur = None
    for n, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("//"):
            continue
        m = re.match(r"^##\s*([a-z]+)\s*:\s*(.*)$", line)
        if m:
            k = m.group(1)
            if k not in SET_TYPES:
                raise DslError(f"{where}:{n}: unknown set type '{k}'")
            rest = [p.strip() for p in m.group(2).split(" | ")]
            cur = {"k": k, "instr": rest[0], "items": []}
            if k == "sort":
                cur["groups"] = rest[1:]
                if len(cur["groups"]) < 2:
                    raise DslError(f"{where}:{n}: sort needs 2+ groups")
            if k == "bank":
                extra = [p for p in rest[1:] if p.startswith("+")]
                cur["extra"] = [w.strip() for p in extra for w in p[1:].split(",") if w.strip()]
            sets.append(cur)
            continue
        if cur is None:
            raise DslError(f"{where}:{n}: item before any ## header: {line}")
        w = f"{where}:{n}"
        if cur["k"] == "sort":
            g, _, xs = line.partition(":")
            g = g.strip()
            if g not in cur["groups"]:
                raise DslError(f"{w}: '{g}' is not a group of this sort set")
            for x in [x.strip() for x in xs.split(",") if x.strip()]:
                it = {"k": "sort", "t": "sortit", "x": x, "g": g}
                cur["items"].append(ctx.add(it, x + ">" + g, w))
            continue
        try:
            it, key = parse_item(cur["k"], line, None, ctx, w)
        except DslError:
            raise
        cur["items"].append(ctx.add(it, key, w))
    for s in sets:
        if not s["items"]:
            raise DslError(f"{where}: empty set '{s['instr']}'")
    return sets
