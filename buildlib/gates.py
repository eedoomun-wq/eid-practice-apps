"""Answer-position, True/False and article gates, plus the seeded shuffles that satisfy them."""
import random
import re

MAX_TRIES = 4000


# ---------- answer positions ----------
def slot_problems(slots, nopts=None):
    """slots: index of the right option for each choice item, in order. Returns a list of problems."""
    p = []
    n = len(slots)
    if n == 0:
        return p
    for i in range(n - 2):
        if slots[i] == slots[i + 1] == slots[i + 2]:
            p.append(f"3 in a row in slot {slots[i]} at item {i + 1}")
            break
    for i in range(n - 3):
        a, b, c, d = slots[i:i + 4]
        if a == c and b == d and a != b:
            p.append(f"alternation {a},{b},{a},{b} at item {i + 1}")
            break
    for i in range(n - 5):
        w = slots[i:i + 6]
        if w[0:3] == w[3:6] and len(set(w[0:3])) == 3:
            p.append(f"rotation {w} at item {i + 1}")
            break
    for i in range(n - 3):
        w = slots[i:i + 4]
        if all(w[j + 1] - w[j] == 1 for j in range(3)) or all(w[j + 1] - w[j] == -1 for j in range(3)):
            p.append(f"step rotation {w} at item {i + 1}")
            break
    if n >= 4:
        for s in set(slots):
            if slots.count(s) * 2 > n:
                p.append(f"slot {s} holds {slots.count(s)}/{n} keys")
                break
    elif n >= 2 and len(set(slots)) == 1:
        p.append("all keys in one slot")
    return p


def tail_problems(slots):
    """Problems in the last few positions only (used while building a sequence)."""
    tail = slots[-8:]
    p = slot_problems(tail if len(tail) < 4 else tail + [], None)
    return [x for x in p if not x.startswith("slot ") and "all keys" not in x]


def arrange(seq_id, things, key_fn, tries=300):
    """Build an order step by step so no local pattern appears; drop surplus keys of an over-full slot."""
    things = list(things)
    keys = [key_fn(t) for t in things]
    n = len(things)
    for s_ in set(keys):
        while keys.count(s_) * 2 > len(keys) and len(keys) >= 4:
            k = keys.index(s_)
            # drop from the end of the list (decks are samples)
            k = len(keys) - 1 - keys[::-1].index(s_)
            things.pop(k)
            keys.pop(k)
    rng = random.Random(seq_id + ":arrange")
    for attempt in range(tries):
        pool = list(things)
        rng.shuffle(pool)
        out = []
        ok = True
        while pool:
            cands = [t for t in pool if not tail_problems([key_fn(x) for x in out] + [key_fn(t)])]
            if not cands:
                ok = False
                break
            t = rng.choice(cands)
            out.append(t)
            pool.remove(t)
        if ok and not slot_problems([key_fn(x) for x in out]):
            return out
    return None


def tf_problems(vals):
    p = []
    n = len(vals)
    if n == 0:
        return p
    if n >= 2 and len(set(vals)) == 1:
        p.append("all True/False keys are the same")
    run = 1
    for i in range(1, n):
        run = run + 1 if vals[i] == vals[i - 1] else 1
        if run > 3:
            p.append("True/False run longer than 3")
            break
    if n >= 4 and all(vals[i] != vals[i + 1] for i in range(n - 1)):
        p.append("True/False keys strictly alternate")
    return p


def shuffle_choice_set(set_id, items):
    """items: choice item dicts (non-TF) of one set, options with the right one at 'a'.
    Permutes options with a seeded shuffle, re-rolling the seed until the set passes."""
    shufflable = [it for it in items if not it.get("tf")]
    if not shufflable:
        return None
    originals = [(list(it["o"]), it["a"]) for it in shufflable]
    for attempt in range(MAX_TRIES):
        rng = random.Random(f"{set_id}:{attempt}")
        slots = []
        for it, (opts, a) in zip(shufflable, originals):
            order = list(range(len(opts)))
            rng.shuffle(order)
            it["o"] = [opts[i] for i in order]
            it["a"] = order.index(a)
            slots.append(it["a"])
        if not slot_problems(slots):
            return attempt
    return f"could not find a passing shuffle for {set_id}: {slot_problems(slots)}"


def reorder_until(seq_id, things, problems_fn, key_fn, tries=MAX_TRIES):
    """Reorder a list (seeded) until problems_fn(keys) is empty. Returns the new list or None."""
    if not problems_fn([key_fn(t) for t in things]):
        return list(things)
    for attempt in range(tries):
        rng = random.Random(f"{seq_id}:order:{attempt}")
        cand = list(things)
        rng.shuffle(cand)
        if not problems_fn([key_fn(t) for t in cand]):
            return cand
    return None


# ---------- article giveaway ----------
VOWEL_SOUND_PREFIX = ("hour", "honest", "honour", "heir", "mba", "fbi", "mp3", "sms", "x-ray", "8", "11", "18", "80")
CONS_SOUND_PREFIX = ("uni", "use", "usu", "eu", "one", "once", "ewe", "ufo", "uk", "usa", "u.s")


def vowel_sound(word):
    w = word.lower().strip().lstrip("\"'(")
    if w.startswith(VOWEL_SOUND_PREFIX):
        return True
    if w.startswith(CONS_SOUND_PREFIX):
        return False
    return w[:1] in "aeiou"


ART_GAP = re.compile(r"\b(a|an)\s+___", re.I)


def article_problem(stem, options):
    if not ART_GAP.search(stem or ""):
        return None
    kinds = {vowel_sound(o) for o in options if o.strip()}
    if len(kinds) > 1:
        return f"'a/an ___' gives the answer away: {stem} / {options}"
    return None


# ---------- clocks ----------
PART_OF_DAY = re.compile(r"in the morning|in the afternoon|in the evening|at night|midday|midnight|lunchtime|noon", re.I)
