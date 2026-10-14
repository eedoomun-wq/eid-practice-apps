"""Puzzles (round 2): the case (logic grid), crossword + word search, grammar escape room,
guess the word + What am I? Everything is generated or validated here at build time."""
import itertools
import random
import re

from . import gates as G
from .norm import norm

# ---------------------------------------------------------------- shared
RUDE = {"ass", "arse", "anus", "piss", "shit", "fuck", "cunt", "dick", "cock", "tit", "tits", "fag", "slut",
        "whore", "porn", "sex", "sexy", "nazi", "hell", "damn", "crap", "boob", "nude", "kill", "rape", "bum",
        "poo", "pee", "turd", "wank", "twat", "hore", "pis", "fuk", "kkk", "gay", "die", "dead", "drug", "isis"}


def letters_only(s):
    return re.fullmatch(r"[A-Za-z]+", s) is not None


def word_entries(words):
    """Crossword / word-search candidates from a unit's word list.
    Single words first (heads like 'businessman / businesswoman' give two), then two-word phrases."""
    singles, phrases = [], []
    for w in words:
        for part in re.split(r"\s*/\s*", w["w"]):
            part = part.strip()
            if letters_only(part) and 3 <= len(part) <= 12:
                singles.append(dict(ans=part.upper(), show=part, enum=str(len(part)), w=w))
            else:
                bits = part.split()
                if 2 <= len(bits) <= 3 and all(letters_only(b) for b in bits) and 4 <= sum(map(len, bits)) <= 12:
                    phrases.append(dict(ans="".join(bits).upper(), show=part, enum=",".join(str(len(b)) for b in bits), w=w))
    seen, out = set(), []
    for e in singles + phrases:
        if e["ans"] not in seen:
            seen.add(e["ans"])
            out.append(e)
    return out, len({e["ans"] for e in singles})


def gapped_example(e):
    ex = e["w"]["ex"]
    pat = re.compile(r"\b" + r"\s+".join(re.escape(b) for b in e["show"].split()) + r"(s|es|ed|d|ing)?\b", re.I)
    m = pat.search(ex)
    if not m or m.group(1):
        return None
    return ex[:m.start()] + "___" + ex[m.end():]


def def_clue(e):
    d = e["w"]["d"]
    if re.search(r"\b" + re.escape(e["show"].split()[0]) + r"\b", d, re.I):
        return None
    return d


# ---------------------------------------------------------------- crossword
def _fits(grid, ans, r, c, d):
    dr, dc = (0, 1) if d == "a" else (1, 0)
    cross = 0
    for i, ch in enumerate(ans):
        rr, cc = r + dr * i, c + dc * i
        cur = grid.get((rr, cc))
        if cur is not None:
            if cur != ch:
                return -1
            cross += 1
        else:
            # no side neighbours for new letters
            if grid.get((rr + dc, cc + dr)) is not None or grid.get((rr - dc, cc - dr)) is not None:
                return -1
    # nothing directly before or after the word
    if grid.get((r - dr, c - dc)) is not None or grid.get((r + dr * len(ans), c + dc * len(ans))) is not None:
        return -1
    return cross


def make_crossword(seed, cands, nmin=8, nmax=12, maxdim=11):
    best = None
    for attempt in range(400):
        rng = random.Random(f"{seed}:cw:{attempt}")
        pool = list(cands)
        rng.shuffle(pool)
        pool.sort(key=lambda e: -len(e["ans"]))
        first = pool[0]
        grid = {}
        placed = []

        def put(e, r, c, d):
            dr, dc = (0, 1) if d == "a" else (1, 0)
            for i, ch in enumerate(e["ans"]):
                grid[(r + dr * i, c + dc * i)] = ch
            placed.append(dict(e=e, r=r, c=c, d=d))

        put(first, 0, 0, "a")
        for e in pool[1:]:
            if len(placed) >= nmax:
                break
            opts = []
            for p in placed:
                for i, ch in enumerate(p["e"]["ans"]):
                    pr = p["r"] + (0 if p["d"] == "a" else i)
                    pc = p["c"] + (i if p["d"] == "a" else 0)
                    d = "d" if p["d"] == "a" else "a"
                    for j, ch2 in enumerate(e["ans"]):
                        if ch2 != ch:
                            continue
                        r = pr - (j if d == "d" else 0)
                        c = pc - (j if d == "a" else 0)
                        k = _fits(grid, e["ans"], r, c, d)
                        if k >= 1:
                            rows = [x[0] for x in grid] + [r, r + (len(e["ans"]) - 1 if d == "d" else 0)]
                            cols = [x[1] for x in grid] + [c, c + (len(e["ans"]) - 1 if d == "a" else 0)]
                            if max(rows) - min(rows) < maxdim and max(cols) - min(cols) < maxdim:
                                opts.append((k, rng.random(), r, c, d))
            if opts:
                opts.sort(reverse=True)
                _, _, r, c, d = opts[0]
                put(e, r, c, d)
        if len(placed) >= nmin:
            rows = [x[0] for x in grid]
            cols = [x[1] for x in grid]
            area = (max(rows) - min(rows) + 1) * (max(cols) - min(cols) + 1)
            score = (len(placed), -area)
            if best is None or score > best[0]:
                r0, c0 = min(rows), min(cols)
                best = (score, [dict(p, r=p["r"] - r0, c=p["c"] - c0) for p in placed],
                        max(rows) - r0 + 1, max(cols) - c0 + 1)
            if len(placed) >= min(nmax, len(cands)) or attempt > 120:
                break
    if not best:
        return None
    _, placed, h, w = best
    # numbering in reading order
    starts = sorted({(p["r"], p["c"]) for p in placed})
    num = {rc: i + 1 for i, rc in enumerate(starts)}
    for p in placed:
        p["n"] = num[(p["r"], p["c"])]
    placed.sort(key=lambda p: (p["d"], p["n"]))
    return dict(h=h, w=w, entries=placed)


def check_crossword(cw, pool_answers):
    probs = []
    grid = {}
    for p in cw["entries"]:
        dr, dc = (0, 1) if p["d"] == "a" else (1, 0)
        for i, ch in enumerate(p["e"]["ans"]):
            k = (p["r"] + dr * i, p["c"] + dc * i)
            if grid.get(k, ch) != ch:
                probs.append(f"clash at {k}")
            grid[k] = ch
        if p["e"]["ans"] not in pool_answers:
            probs.append(f"{p['e']['ans']} is not in the unit's word list")
    # every word crosses another
    cells = {}
    for idx, p in enumerate(cw["entries"]):
        dr, dc = (0, 1) if p["d"] == "a" else (1, 0)
        for i in range(len(p["e"]["ans"])):
            cells.setdefault((p["r"] + dr * i, p["c"] + dc * i), []).append(idx)
    for idx, p in enumerate(cw["entries"]):
        dr, dc = (0, 1) if p["d"] == "a" else (1, 0)
        if not any(len(cells[(p["r"] + dr * i, p["c"] + dc * i)]) > 1 for i in range(len(p["e"]["ans"]))):
            probs.append(f"{p['e']['ans']} crosses no other word")
    # connected
    adj = {i: set() for i in range(len(cw["entries"]))}
    for ids in cells.values():
        for a in ids:
            adj[a].update(ids)
    seen, stack = {0}, [0]
    while stack:
        for b in adj[stack.pop()]:
            if b not in seen:
                seen.add(b)
                stack.append(b)
    if len(seen) != len(cw["entries"]):
        probs.append("the grid is not connected")
    # no accidental words: every run of 2+ letters is an entry
    words = {(p["r"], p["c"], p["d"]): p["e"]["ans"] for p in cw["entries"]}
    for (r, c) in grid:
        for d, (dr, dc) in (("a", (0, 1)), ("d", (1, 0))):
            if (r - dr, c - dc) in grid:
                continue
            run = ""
            rr, cc = r, c
            while (rr, cc) in grid:
                run += grid[(rr, cc)]
                rr, cc = rr + dr, cc + dc
            if len(run) >= 2 and words.get((r, c, d)) != run:
                probs.append(f"accidental word {run} at {(r, c)}")
    return probs


# ---------------------------------------------------------------- word search
DIRS_A1 = [(0, 1), (1, 0)]
DIRS_A2 = [(0, 1), (1, 0), (1, 1), (-1, 1)]
ALL8 = [(0, 1), (1, 0), (1, 1), (-1, 1), (0, -1), (-1, 0), (-1, -1), (1, -1)]
FILL = "AAABCDEEEEFGHIIIKLLMNNOOOPRRSSTTTUWY"


def make_wordsearch(seed, words, size, dirs):
    for attempt in range(600):
        rng = random.Random(f"{seed}:ws:{attempt}")
        grid = {}
        places = []
        ok = True
        for wd in sorted(words, key=len, reverse=True):
            spots = []
            for dr, dc in dirs:
                for r in range(size):
                    for c in range(size):
                        er, ec = r + dr * (len(wd) - 1), c + dc * (len(wd) - 1)
                        if not (0 <= er < size and 0 <= ec < size):
                            continue
                        good, over = True, 0
                        for i, ch in enumerate(wd):
                            cur = grid.get((r + dr * i, c + dc * i))
                            if cur is not None and cur != ch:
                                good = False
                                break
                            over += cur is not None
                        if good:
                            spots.append((over, rng.random(), r, c, dr, dc))
            if not spots:
                ok = False
                break
            spots.sort(reverse=True)
            pick = spots[0] if rng.random() < .35 else rng.choice(spots)
            _, _, r, c, dr, dc = pick
            for i, ch in enumerate(wd):
                grid[(r + dr * i, c + dc * i)] = ch
            places.append(dict(w=wd, r=r, c=c, dr=dr, dc=dc))
        if not ok:
            continue
        rows = []
        for r in range(size):
            rows.append("".join(grid.get((r, c)) or rng.choice(FILL) for c in range(size)))
        if not check_wordsearch(rows, words, dirs):
            return dict(size=size, rows=rows, places=places)
    return None


def lines_all(rows):
    n = len(rows)
    out = []
    for dr, dc in ALL8:
        for r in range(n):
            for c in range(n):
                s = ""
                rr, cc = r, c
                while 0 <= rr < n and 0 <= cc < n:
                    s += rows[rr][cc]
                    rr, cc = rr + dr, cc + dc
                out.append((s, r, c, dr, dc))
    return out


def check_wordsearch(rows, words, dirs):
    probs = []
    n = len(rows)
    for wd in words:
        hits = 0
        for dr, dc in ALL8:
            for r in range(n):
                for c in range(n):
                    if all(0 <= r + dr * i < n and 0 <= c + dc * i < n and rows[r + dr * i][c + dc * i] == ch for i, ch in enumerate(wd)):
                        hits += 1
        if hits != 1:
            probs.append(f"{wd} appears {hits} times")
    text = {s for s, *_ in lines_all(rows)}
    for bad in RUDE:
        b = bad.upper()
        if any(b in t for t in text) and not any(b in w for w in words):
            probs.append(f"unwanted word {b} in the grid")
    return probs


# ---------------------------------------------------------------- the case (logic grid)
def case_solutions(case):
    people = case["people"]
    groups = case["groups"]
    ent_group = {p: -1 for p in people}
    for gi, g in enumerate(groups):
        for v in g:
            ent_group[v] = gi
    sols = []
    for perms in itertools.product(*[list(itertools.permutations(g)) for g in groups]):
        owner = {p: p for p in people}
        for g in perms:
            for p, v in zip(people, g):
                owner[v] = p
        if all(_clue_true(cl, owner) for cl in case["_logic"]):
            sols.append(owner)
    return sols


def _clue_true(cl, owner):
    kind, a, b = cl
    if kind == "is":
        return owner[a] == owner[b]
    return owner[a] != owner[b]


def check_case(case, a2, ukey):
    probs = []
    n_people, n_groups = (4, 3) if a2 else (3, 2)
    people, groups = case.get("people", []), case.get("groups", [])
    if len(people) != n_people or len(groups) != n_groups or any(len(g) != n_people for g in groups):
        probs.append(f"needs {n_people} people × {n_groups} groups of {n_people}")
        return probs, None
    ents = set(people) | {v for g in groups for v in g}
    if len(ents) != n_people * (n_groups + 1):
        probs.append("names and values must all be different")
    clues = case.get("clues", [])
    if not (5 <= len(clues) <= 8):
        probs.append(f"{len(clues)} clues (need 5–8)")
    logic, needed, extra = [], [], []
    for cl in clues:
        f = cl.get("f")
        if not f or f[0] not in ("is", "not") or f[1] not in ents or f[2] not in ents:
            probs.append(f"clue without valid logic: {cl}")
            continue
        logic.append(tuple(f))
        (needed if cl.get("need", True) else extra).append(tuple(f))
    if not any(f[0] == "not" for f in logic):
        probs.append("needs at least one negative clue")
    if not extra:
        probs.append("needs a red herring (a true clue marked need=False)")
    if a2 and not any(f[1] not in people and f[2] not in people for f in needed):
        probs.append("A2: needs a needed clue that links two things, not a person (two steps of reasoning)")
    case["_logic"] = logic
    sols = case_solutions(case)
    if len(sols) != 1:
        probs.append(f"{len(sols)} solutions with all clues (need exactly 1)")
        return probs, None
    sol = sols[0]
    case["_logic"] = needed
    if len(case_solutions(case)) != 1:
        probs.append("the needed clues alone do not give one solution")
    for i in range(len(needed)):
        case["_logic"] = needed[:i] + needed[i + 1:]
        if len(case_solutions(case)) == 1:
            probs.append(f"clue {needed[i]} is marked needed but the case is solved without it")
    case.pop("_logic", None)
    q = case.get("question", {})
    target, among = q.get("target"), q.get("among", "people")
    pool = people if among == "people" else groups[among]
    ans = [x for x in pool if sol[x] == sol[target]] if target in ents else []
    if len(ans) != 1:
        probs.append("question target/among do not give one answer")
        return probs, None
    answer = ans[0]
    for cl in clues:
        f = cl.get("f") or ()
        if f and f[0] == "is" and {f[1], f[2]} == {target, answer}:
            probs.append(f"a clue prints the answer: {cl['t']}")
    if re.search(r"\b" + re.escape(answer) + r"\b", q.get("q", "")):
        probs.append("the question prints the answer")
    return probs, (sol, answer, pool)


def case_table(case, sol):
    rows = []
    for p in case["people"]:
        rows.append([p] + [next(v for v in g if sol[v] == p) for g in case["groups"]])
    return rows


# ---------------------------------------------------------------- escape room
PLACES = ["Khan As'ad Pasha", "the courtyard house", "the Azem Palace", "the old library", "the Hejaz Railway Station",
          "the Citadel of Damascus", "the old hammam", "the spice shop in Bzouriyah"]


def escape_locks(ukey, a2, items, grammar_ids, pool_words):
    rng = random.Random(ukey + ":escape")
    fix = [i for i in grammar_ids if items[i]["t"] == "fix" and norm(items[i]["full"]) != norm(" ".join(items[i]["tokens"]))]
    choice = [i for i in grammar_ids if items[i]["t"] == "choice" and not items[i].get("tf") and len(items[i]["o"]) == 3 and items[i].get("q")]
    gaps = [i for i in grammar_ids if items[i]["t"] == "typed" and items[i].get("k") == "gap" and len(items[i]["acc"][0].split()) == 1
            and len({norm(a)[:1] for a in items[i]["acc"]}) == 1 and letters_only(items[i]["acc"][0])]
    # numeric codes can never show up by accident: no digits in lock sentences
    rng.shuffle(fix)
    rng.shuffle(choice)
    # sentences without digits first, so a numeric code rarely shows up by accident
    fix.sort(key=lambda i: bool(re.search(r"\d", items[i]["full"] + " ".join(items[i]["tokens"]))))
    choice.sort(key=lambda i: bool(re.search(r"\d", items[i]["q"] + " ".join(items[i]["o"]))))

    def shows(code, texts):
        return re.search(r"(?<!\d)" + re.escape(code) + r"(?!\d)", " ".join(texts)) is not None
    locks = []

    def tick(srcs, kind):
        for attempt in range(80):
            k = (2 if len(srcs) == 5 else 3) if kind == "tick" else rng.choice([1, 2, 3, 4])
            right = sorted(rng.sample(range(len(srcs)), k))
            texts = [items[i]["full"] if n in right else " ".join(items[i]["tokens"]) for n, i in enumerate(srcs)]
            code = "".join(str(n + 1) for n in right) if kind == "tick" else str(k)
            if not shows(code, texts):
                break
        sents = []
        for n, i in enumerate(srcs):
            it = items[i]
            sents.append(it["full"] if n in right else " ".join(it["tokens"]))
        if kind == "tick":
            code = "".join(str(n + 1) for n in right)
            return dict(kind="tick", title="Find the correct sentences",
                        instr="The code = the numbers of the correct sentences, small to big.",
                        lines=sents, code=code, hint=f"Sentence {right[0] + 1}: correct.", src=srcs)
        code = str(k)
        wrong = [n for n in range(len(srcs)) if n not in right]
        return dict(kind="count", title="Count the correct sentences",
                    instr="Count the correct sentences. The number = the code.",
                    lines=sents, code=code, hint=f"Sentence {wrong[0] + 1}: wrong.", src=srcs)

    n_tick = 6 if a2 else 5
    if len(fix) >= n_tick:
        locks.append(tick(fix[:n_tick], "tick"))
    if len(choice) >= 3:
        srcs = choice[:3]
        for attempt in range(60):
            code = "".join(str(items[i]["a"] + 1) for i in srcs)
            if not shows(code, [items[i]["q"] + " " + " ".join(items[i]["o"]) for i in srcs]):
                break
            srcs = rng.sample(choice, 3)
        code = "".join(str(items[i]["a"] + 1) for i in srcs)
        locks.append(dict(kind="numbers", title="The number lock",
                          instr="Choose the right word: 1, 2 or 3. Write the three numbers: the code!",
                          qs=[dict(q=items[i]["q"], o=items[i]["o"]) for i in srcs], code=code,
                          hint=f"First digit: {code[0]}.", src=srcs))
    # password: first letters of the missing words spell a word
    by_letter = {}
    for i in gaps:
        by_letter.setdefault(norm(items[i]["acc"][0])[0].upper(), []).append(i)
    pw = None
    for cand in sorted(pool_words, key=lambda w: (-len(w), w)):
        if not (4 <= len(cand) <= 5):
            continue
        use, ok = [], True
        for ch in cand:
            opts = [i for i in by_letter.get(ch, []) if i not in use]
            if not opts:
                ok = False
                break
            use.append(rng.choice(opts))
        if ok and not any(re.search(r"\b" + cand + r"\b", items[i]["q"], re.I) for i in use):
            pw = (cand, use)
            break
    if pw:
        word, use = pw
        locks.append(dict(kind="password", title="The password",
                          instr="Find the missing words. First letters = the password.",
                          lines=[items[i]["q"] for i in use], code=word,
                          hint=f"First letter: {word[0]}.", src=use))
    else:
        rest = fix[n_tick:n_tick + 5]
        if len(rest) == 5:
            locks.append(tick(rest, "count"))
    if a2:
        rest = fix[n_tick + 5:n_tick + 10] if not pw else fix[n_tick:n_tick + 5]
        if len(rest) == 5:
            locks.append(tick(rest, "count"))
    return locks


def check_escape(locks, a2, items):
    probs = []
    want = (4, 5) if a2 else (3, 3)
    if not (want[0] <= len(locks) <= want[1]):
        probs.append(f"{len(locks)} locks (need {want[0]}–{want[1]})")
    for L in locks:
        # re-derive the code from the item data
        if L["kind"] == "tick":
            right = [n + 1 for n, i in enumerate(L["src"]) if norm(L["lines"][n]) in [norm(x) for x in items[i]["fulls"]]]
            code = "".join(map(str, right))
        elif L["kind"] == "count":
            code = str(sum(norm(L["lines"][n]) in [norm(x) for x in items[i]["fulls"]] for n, i in enumerate(L["src"])))
        elif L["kind"] == "numbers":
            code = "".join(str(items[i]["a"] + 1) for i in L["src"])
        else:
            firsts = set()
            code = ""
            for i in L["src"]:
                fl = {norm(a)[:1].upper() for a in items[i]["acc"]}
                if len(fl) != 1:
                    probs.append(f"password item {i} has answers with different first letters")
                code += fl.pop()
        if code != L["code"]:
            probs.append(f"{L['kind']} lock: code re-derived as {code}, stored {L['code']}")
        # a wrong sentence must really be wrong (it must not be one of the accepted corrections)
        if L["kind"] in ("tick", "count"):
            for n, i in enumerate(L["src"]):
                if norm(L["lines"][n]) == norm(" ".join(items[i]["tokens"])) and norm(" ".join(items[i]["tokens"])) in [norm(x) for x in items[i]["fulls"]]:
                    probs.append(f"lock sentence {n + 1} is both right and wrong")
        visible = " ".join([L["title"], L["instr"]] + L.get("lines", []) + [q["q"] + " " + " ".join(q["o"]) for q in L.get("qs", [])])
        if L["kind"] == "password":
            if re.search(r"\b" + re.escape(L["code"]) + r"\b", visible, re.I):
                probs.append(f"password {L['code']} is visible before solving")
        elif re.search(r"(?<!\d)" + re.escape(L["code"]) + r"(?!\d)", visible):
            probs.append(f"code {L['code']} is visible before solving")
    return probs


# ---------------------------------------------------------------- riddles and guess the word
def check_riddles(riddles, heads, ukey):
    probs = []
    if not (6 <= len(riddles) <= 8):
        probs.append(f"{len(riddles)} riddles (need 6–8)")
    for r in riddles:
        ans, clues = r[0], r[1]
        if norm(ans) not in heads:
            probs.append(f"riddle answer '{ans}' is not a unit word")
        if len(clues) != 3:
            probs.append(f"riddle '{ans}' needs 3 clues")
        stem = norm(ans)
        for c in clues:
            if re.search(r"\b" + re.escape(stem) + r"(s|es)?\b", norm(c)):
                probs.append(f"riddle '{ans}': a clue contains the answer: {c}")
    return probs


def riddle_options(ukey, riddles, words):
    """A1: the answer + 3 other unit words (same group first)."""
    out = []
    heads = [w for w in words]
    for k, (ans, clues) in enumerate(riddles):
        rng = random.Random(f"{ukey}:rid:{k}")
        me = next((w for w in words if norm(w["w"]) == norm(ans) or norm(ans) in [norm(p) for p in re.split(r"\s*/\s*", w["w"])]), None)
        same = [w["w"] for w in heads if me and w["cat"] == me["cat"] and norm(w["w"]) != norm(ans) and "/" not in w["w"]]
        other = [w["w"] for w in heads if norm(w["w"]) != norm(ans) and w["w"] not in same and "/" not in w["w"]]
        rng.shuffle(same)
        rng.shuffle(other)
        opts = [ans] + (same + other)[:3]
        out.append(dict(ans=ans, clues=clues, o=opts, a=0))
    return out


def guess_words(words):
    out = []
    for w in words:
        for part in re.split(r"\s*[/–]\s*", w["w"]):
            if re.fullmatch(r"[a-z]{4,7}", part):
                out.append(dict(w=part, d=w["d"], ex=w["ex"]))
    seen, res = set(), []
    for x in out:
        if x["w"] not in seen:
            seen.add(x["w"])
            res.append(x)
    return res
