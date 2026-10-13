"""Compile one level's content files into the JSON the engine reads, and run the data gates."""
import importlib.util
import os
import random
import re

from .dsl import Ctx, DslError, parse_sets, tokens_for_tiles, h6
from . import gates as G
from .levelgate import LevelGate
from .norm import norm

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_module(path):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3] + "_" + h6(path), path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


COMMON = load_module(os.path.join(ROOT, "content", "common.py"))

ARTICLES = re.compile(r"^(a|an|the|to)\s+", re.I)


def head_norm(s):
    s = re.sub(r"\([^)]*\)", "", s)
    s = s.replace("–", "-").replace("—", "-")
    s = ARTICLES.sub("", s.strip().lower())
    s = re.sub(r"[!?.…]", "", s)
    s = re.sub(r"\s*/\s*", "/", s)
    s = re.sub(r"\s*-\s*", "-", s)
    return re.sub(r"\s+", " ", s).strip()


def default_keys(head):
    h = re.sub(r"\([^)]*\)", "", head).strip()
    h = re.sub(r"[!?.…]", "", h)
    parts = re.split(r"\s*/\s*|\s+–\s+|\s+-\s+", h)
    keys = []
    for p in parts:
        p = ARTICLES.sub("", p.strip())
        if p:
            keys.append(p)
    return keys


def key_regex(key):
    words = key.split()
    out = []
    for w in words:
        e = re.escape(w)
        alts = [e + r"(?:s|es|ed|d|ing|'s)?"]
        if w.endswith("y") and len(w) > 2:
            alts.append(re.escape(w[:-1]) + r"(?:ies|ied)")
        if w.endswith("e") and len(w) > 2:
            alts.append(re.escape(w[:-1]) + "ing")
        if re.match(r"^[a-z]+[^aeiouy][aeiou][bdgmnpt]$", w):
            alts.append(e + w[-1] + "(?:ed|ing)")
        out.append("(?:" + "|".join(alts) + ")")
    return re.compile(r"(?<![\w])" + r"\s+".join(out) + r"(?![\w])", re.I)


def split_top(text):
    """Split a book list on commas / new lines that are not inside brackets."""
    out, cur, depth = [], "", 0
    for ch in text:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if (ch in ",\n") and depth == 0:
            if cur.strip():
                out.append(cur.strip())
            cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur.strip())
    return out


def fill_gaps(q, ans):
    parts = [a.strip() for a in ans.split(" / ")] if q.count("___") > 1 else [ans]
    for a in parts:
        q = q.replace("___", a, 1)
    return q


SPELLABLE = re.compile(r"^[A-Za-z]{4,12}$")


def spell_pattern(word, seed):
    rng = random.Random(seed)
    letters = list(word)
    idx = [i for i in range(1, len(letters))]
    vowels = [i for i in idx if letters[i].lower() in "aeiou"]
    cons = [i for i in idx if i not in vowels]
    rng.shuffle(cons)
    hide = set(vowels[: max(1, len(word) // 3)])
    target = max(2, round(len(word) * 0.4))
    for i in cons:
        if len(hide) >= target:
            break
        hide.add(i)
    return " ".join("_" if i in hide else c for i, c in enumerate(letters))


class LevelCompiler:
    def __init__(self, level):
        self.level = level
        self.code = level["code"]
        self.series = level["series"]
        self.errors = []
        self.warnings = []
        self.items = {}
        self.texts = []  # (unit, label, text) for the level gate
        self.arabic = []  # (unit, label, line)
        self.stats = {}
        self.proper = set(COMMON.PROPER)

    # ------------------------------------------------------------ helpers
    def err(self, msg):
        self.errors.append(msg)

    def gate_text(self, unit, label, text):
        if text:
            self.texts.append((unit, label, text))

    def finish_choice_set(self, s):
        its = [self.items[i] for i in s["items"] if self.items[i]["t"] == "choice"]
        res = G.shuffle_choice_set(s["id"], its)
        if isinstance(res, str):
            self.err("[positions] " + res)
        tfs = [it for it in its if it.get("tf")]
        if tfs:
            # reorder the set so True/False keys pass; other items keep their relative slots
            ids = list(s["items"])
            tf_ids = [i for i in ids if self.items[i].get("tf")]
            new = G.reorder_until(s["id"] + ":tf", tf_ids, G.tf_problems, lambda i: self.items[i]["a"])
            if new is None:
                self.err(f"[positions] True/False keys in {s['id']} cannot pass")
            else:
                it_new = iter(new)
                s["items"] = [next(it_new) if self.items[i].get("tf") else i for i in ids]
            nontf = [self.items[i]["a"] for i in s["items"] if self.items[i]["t"] == "choice" and not self.items[i].get("tf")]
            if nontf and G.slot_problems(nontf):
                self.err(f"[positions] {s['id']}: {G.slot_problems(nontf)}")
        for it in its:
            p = G.article_problem(it.get("q", ""), it["o"])
            if p:
                self.err(f"[article] {s['id']}: {p}")
            if len(set(o.strip().lower() for o in it["o"])) != len(it["o"]):
                self.err(f"[data] repeated option in {it['id']}: {it['o']}")

    def finish_set(self, s, unit, label):
        s["n"] = len(s["items"])
        if s["k"] in ("choose", "tf", "odd"):
            self.finish_choice_set(s)
        if s["k"] == "order":
            for i in s["items"]:
                it = self.items[i]
                toks = it["toks"]
                for attempt in range(200):
                    rng = random.Random(f"{i}:tiles:{attempt}")
                    order = list(range(len(toks)))
                    rng.shuffle(order)
                    if order != list(range(len(toks))) or len(toks) < 2:
                        break
                it["tiles"] = [toks[j] for j in order]
        if s["k"] == "bank":
            bank = []
            for i in s["items"]:
                a = self.items[i]["acc"][0]
                if a not in bank:
                    bank.append(a)
            for e in s.get("extra", []):
                if e not in bank:
                    bank.append(e)
            s["bank"] = sorted(bank, key=lambda w: w.lower())
            for i in s["items"]:
                p = G.article_problem(self.items[i]["q"], s["bank"])
                if p:
                    self.err(f"[article] {s['id']}: {p}")
        self.make_alts(s)
        # gate text
        self.gate_text(unit, f"{label} instruction", s["instr"])
        for i in s["items"]:
            it = self.items[i]
            if it.get("cls"):
                continue  # classroom chunks and their situations are exempt from the level gate
            for f in ("q", "l", "r", "x", "full"):
                if (f == "q" and it.get("wid")) or (f == "r" and it.get("wdef")):
                    continue  # word definitions are exempt
                if it.get(f):
                    txt = it[f]
                    if f == "q" and "___" in txt:
                        txt = fill_gaps(txt, it["o"][it["a"]] if it["t"] == "choice" else it["acc"][0])
                    self.gate_text(unit, f"{label} [{s['instr']}]", txt)
            for f in ("o", "acc", "fulls"):
                for v in it.get(f, []) or []:
                    if not it.get("tf"):
                        self.gate_text(unit, f"{label} [{s['instr']}] option", v)
            if it.get("fb"):
                self.gate_text(unit, f"{label} feedback", it["fb"])
            if it["t"] in ("typed", "bank", "fix") and not it.get("acc"):
                self.err(f"[data] {i} has no answer")
            if it["t"] == "choice" and not (0 <= it.get("a", -1) < len(it["o"])):
                self.err(f"[data] {i} has no right option")
        for e in s.get("extra", []):
            self.gate_text(unit, f"{label} bank extra", e)

    def make_alts(self, s):
        """Single-question versions of board items (match, sort, bank) for the Review Pile and tests."""
        k = s["k"]
        if k not in ("match", "sort", "bank"):
            return
        ids = s["items"]
        alts = []
        for n, i in enumerate(ids):
            it = self.items[i]
            rng = random.Random(i + ":alt")
            if k == "match":
                others = [self.items[j]["r"] for j in ids if j != i]
                rng.shuffle(others)
                opts = [it["r"]] + others[:2]
                q = it["l"]
            elif k == "sort":
                opts = [it["g"]] + [g for g in s["groups"] if g != it["g"]][:2]
                q = it["x"]
            else:
                others = [b for b in s["bank"] if norm(b) not in [norm(a) for a in it["acc"]]]
                rng.shuffle(others)
                opts = [it["acc"][0]] + others[:2]
                q = it["q"]
            if len(opts) < 2:
                continue
            it["alt"] = {"t": "choice", "q": q, "o": opts, "a": 0}
            alts.append(it["alt"])
        if alts:
            res = G.shuffle_choice_set(s["id"] + ":alt", alts)
            if isinstance(res, str):
                self.err("[positions] " + res)
            for a in alts:
                p = G.article_problem(a["q"], a["o"])
                if p and k != "sort":
                    self.err(f"[article] {s['id']} (review version): {p}")

    def sets_from(self, text, ctx, prefix, unit, label):
        try:
            sets = parse_sets(text, ctx, f"{self.code} U{unit} {label}")
        except DslError as e:
            self.err(f"[data] {e}")
            return []
        for n, s in enumerate(sets, 1):
            s["id"] = f"{prefix}.s{n}"
            self.finish_set(s, unit, label)
        return sets

    # ------------------------------------------------------------ words
    def parse_words(self, mod, ukey, unit):
        words = []
        cat = "Words"
        for n, raw in enumerate(mod.WORDS.strip().splitlines(), 1):
            line = raw.strip()
            if not line or line.startswith("//"):
                continue
            if line.startswith("@"):
                cat = line[1:].strip()
                continue
            extra = line.startswith("+")
            if extra:
                line = line[1:].strip()
            f = [p.strip() for p in line.split("|")]
            if len(f) < 3:
                self.err(f"[data] {self.code} U{unit} word line {n} needs 'word | definition | example': {line}")
                continue
            head, d, ex = f[0], f[1], f[2]
            keyspec = f[3] if len(f) > 3 else ""
            syn = f[4] if len(f) > 4 else ""
            need_all = keyspec.startswith("&")
            keys = [k.strip() for k in keyspec.lstrip("&").split(";") if k.strip()] or default_keys(head)
            w = {"id": f"{ukey}-w{h6(head)}", "w": head, "d": d, "ex": ex, "cat": cat}
            if extra:
                w["x"] = 1
            if syn:
                w["syn"] = syn
            found = [k for k in keys if key_regex(k).search(ex)]
            if (need_all and len(found) != len(keys)) or not found:
                self.err(f"[words] {self.code} U{unit}: example for '{head}' does not use it: {ex}")
            w["_keys"] = keys
            w["_found"] = found
            words.append(w)
            self.gate_text(unit, f"word example '{head}'", ex)
        seen = set()
        for w in words:
            k = head_norm(w["w"])
            if k in seen:
                self.err(f"[data] {self.code} U{unit}: word '{w['w']}' listed twice")
            seen.add(k)
        return words

    def check_book_words(self, mod, words, unit):
        heads = {}
        for w in words:
            heads[head_norm(w["w"])] = w
            for k in w["_keys"]:
                heads.setdefault(head_norm(k), w)
        book = split_top(mod.BOOK)
        missing = [b for b in book if head_norm(b) not in heads]
        for b in missing:
            self.err(f"[book words] {self.code} U{unit}: '{b}' is not in the Words section")
        self.stats.setdefault("book_words", 0)
        self.stats["book_words"] += len(book)
        return book

    def word_sets(self, words, ctx, ukey, unit):
        sets = []
        usable = [w for w in words]
        rng = random.Random(ukey + ":words")

        def distractors(w, pool, n):
            cands = [x for x in pool if x is not w and (not w.get("syn") or x.get("syn") != w.get("syn"))
                     and norm(x["w"]) != norm(w["w"])]
            rng2 = random.Random(w["id"] + ":d")
            rng2.shuffle(cands)
            return cands[:n]

        def add(item, key):
            return ctx.add(item, key, f"{ukey} words")

        # 1. Which word? (definition -> word)
        bycat = {}
        for w in usable:
            bycat.setdefault(w["cat"], []).append(w)
        which = []
        for w in usable:
            if any(key_regex(k).search(w["d"]) for k in w["_keys"]):
                self.warnings.append(f"{self.code} U{unit}: definition of '{w['w']}' contains the word; left out of 'Which word?'")
                continue
            pool = bycat[w["cat"]] if len(bycat[w["cat"]]) >= 4 else usable
            ds = distractors(w, pool, 2)
            if len(ds) < 2:
                ds = distractors(w, usable, 2)
            it = {"k": "choose", "t": "choice", "q": w["d"], "o": [w["w"]] + [d["w"] for d in ds], "a": 0, "wid": w["id"]}
            w["qid"] = add(it, "which:" + w["w"])
            which.append(w["qid"])
        for n in range(0, len(which), 10):
            chunk = which[n:n + 10]
            if len(chunk) < 4 and sets:
                sets[-1]["items"] += chunk
                continue
            sets.append({"k": "choose", "instr": "Choose the word.", "items": chunk})

        # 2. Match word <-> meaning, 6-8 per set, no two words of one synonym group together
        pairs = [w for w in usable if len(w["d"]) <= 70]
        rng.shuffle(pairs)
        groups, cur = [], []
        for w in pairs:
            if w.get("syn") and any(x.get("syn") == w.get("syn") for x in cur):
                continue
            cur.append(w)
            if len(cur) == 8:
                groups.append(cur)
                cur = []
        if len(cur) >= 4:
            groups.append(cur)
        for g in groups[:4]:
            ids = [add({"k": "match", "t": "pair", "l": w["w"], "r": w["d"], "syn": w.get("syn", ""), "wdef": 1}, "match:" + w["w"]) for w in g]
            sets.append({"k": "match", "instr": "Match the word and meaning.", "items": ids})

        # 3. Missing letters
        sp = [w for w in usable if SPELLABLE.match(w["w"])]
        rng.shuffle(sp)
        nsp = 20 if (self.series == "starter" and unit <= 3) else 10
        sp = sp[:nsp]
        for n in range(0, len(sp), 10):
            ids = []
            for w in sp[n:n + 10]:
                pat = spell_pattern(w["w"], w["id"])
                ids.append(add({"k": "spell", "t": "typed", "q": pat, "acc": [w["w"]], "hint": w["d"], "spell": 1}, "spell:" + w["w"]))
            if len(ids) >= 4:
                sets.append({"k": "spell", "instr": "Write the whole word.", "items": ids})

        # 4. First-letter gap in the example sentence
        gaps = []
        for w in usable:
            if " " in w["w"].strip() or not w["_found"]:
                continue
            m = key_regex(w["_found"][0]).search(w["ex"])
            if not m or " " in m.group(0):
                continue
            surface = m.group(0)
            q = w["ex"][: m.start()] + "___" + w["ex"][m.end():]
            if "___" in q.replace("___", "", 1):
                continue
            gaps.append((w, surface, q))
        rng.shuffle(gaps)
        gaps = gaps[:20]
        for n in range(0, len(gaps), 10):
            ids = []
            for w, surface, q in gaps[n:n + 10]:
                hint = surface[0] + " " + " ".join("_" for _ in surface[1:])
                ids.append(add({"k": "gap", "t": "typed", "q": q, "acc": [surface], "hint": hint, "first": 1}, "gapw:" + w["w"]))
            if len(ids) >= 4:
                sets.append({"k": "gap", "instr": "Write the word.", "items": ids})

        # 5. Sort into categories
        cats = [c for c, ws in bycat.items() if len(ws) >= 3 and all(len(w["w"]) <= 22 for w in ws[:5])]
        if len(cats) >= 2:
            pick = cats[:3]
            ids = []
            for c in pick:
                ws = [w for w in bycat[c] if len(w["w"]) <= 22]
                rng2 = random.Random(ukey + c)
                rng2.shuffle(ws)
                for w in ws[:5]:
                    ids.append(add({"k": "sort", "t": "sortit", "x": w["w"], "g": c}, "sort:" + w["w"]))
            r3 = random.Random(ukey + ":sortorder")
            r3.shuffle(ids)
            sets.append({"k": "sort", "instr": "Sort the words.", "groups": pick, "items": ids})
        return sets

    # ------------------------------------------------------------ unit
    def compile_unit(self, path, extra_chunks):
        mod = load_module(path)
        m = mod.META
        unit = m["n"]
        ukey = f"{self.code}u{unit}"
        ctx = Ctx(ukey, self.items, self.proper, self.errors)
        U = {"n": unit, "title": m["title"], "pages": m["pages"], "id": f"u{unit}"}

        words = self.parse_words(mod, ukey, unit)
        book = self.check_book_words(mod, words, unit)
        wsets = self.word_sets(words, ctx, ukey, unit)
        for n, s in enumerate(wsets, 1):
            s["id"] = f"{ukey}.w.s{n}"
            self.finish_set(s, unit, "word practice")
        if getattr(mod, "WORDSETS", None):
            wsets += self.sets_from(mod.WORDSETS, ctx, f"{ukey}.wx", unit, "word practice")
        odd_sets = []
        if getattr(mod, "ODD", None):
            odd_sets = self.sets_from("## odd: Find the odd one.\n" + mod.ODD, ctx, f"{ukey}.odd", unit, "odd one out")
            wsets += odd_sets
        for w in words:
            w.pop("_keys", None)
            w.pop("_found", None)
        U["words"] = words
        U["wsets"] = wsets
        if len(wsets) < 3:
            self.err(f"[data] {ukey}: fewer than 3 word-practice sets")

        # grammar
        U["grammar"] = []
        for gi, g in enumerate(mod.GRAMMAR, 1):
            gid = g.get("id") or f"g{gi}"
            label = f"grammar '{g['title']}'"
            GP = {"id": gid, "title": g["title"], "visual": g.get("visual"), "pattern": g.get("pattern", []),
                  "examples": g.get("examples", []), "ar": g.get("ar", []), "watch": g.get("watch", []),
                  "note": g.get("note", "")}
            for row in GP["pattern"]:
                self.gate_text(unit, label + " pattern", " ".join(x for x in row[1:] if isinstance(x, str)))
            for ex in GP["examples"]:
                self.gate_text(unit, label + " example", ex)
            if GP["note"]:
                self.gate_text(unit, label + " note", GP["note"])
            for wr in GP["watch"]:
                self.gate_text(unit, label + " watch-out (right)", wr[1])
            self.gate_visual(unit, label, GP["visual"])
            for line in GP["ar"]:
                self.arabic.append((unit, g["title"], line))
            if not (2 <= len(GP["ar"]) <= 4):
                self.err(f"[arabic] {ukey} {g['title']}: Arabic block must be 2–4 lines")
            if not GP["examples"] or not GP["watch"]:
                self.err(f"[data] {ukey} {g['title']}: needs examples and a Watch out box")
            q = self.sets_from(g["quick"], ctx, f"{ukey}.{gid}.q", unit, label + " quick check")
            GP["quick"] = q[0] if q else None
            if q and len(q[0]["items"]) != 3:
                self.err(f"[data] {ukey} {g['title']}: quick check must have 3 items")
            GP["sets"] = self.sets_from(g["sets"], ctx, f"{ukey}.{gid}", unit, label)
            if len(GP["sets"]) < 4:
                self.err(f"[volume] {ukey} {g['title']}: {len(GP['sets'])} sets (need 4+)")
            for s in GP["sets"]:
                if not (8 <= len(s["items"]) <= 12):
                    self.err(f"[volume] {s['id']} '{s['instr']}': {len(s['items'])} items (need 8–12)")
            U["grammar"].append(GP)

        # classroom
        bank = {p["p"]: p for p in COMMON.CLASSROOM_ALL}
        phrases = []
        for p in mod.CLASSROOM["phrases"]:
            if p not in bank:
                self.err(f"[data] {ukey}: classroom phrase not in bank: {p}")
                continue
            phrases.append(bank[p])
        if not (6 <= len(phrases) <= 10):
            self.err(f"[data] {ukey}: classroom needs 6–10 phrases (has {len(phrases)})")
        U["cls"] = {"phrases": [{"p": p["p"], "s": p["s"], "who": p["who"]} for p in phrases]}
        csets = []
        ids = []
        for p in phrases:
            pool = [x for x in phrases if x is not p and x.get("grp") != p.get("grp", "-") and x["who"] == p["who"]]
            if len(pool) < 2:
                pool = [x for x in COMMON.CLASSROOM_ALL if x is not p and x["who"] == p["who"] and x.get("grp") != p.get("grp", "-") and x["lvl"] <= self.level["clsmax"]]
            rr = random.Random(ukey + p["p"])
            rr.shuffle(pool)
            it = {"k": "choose", "t": "choice", "q": p["s"], "o": [p["p"]] + [x["p"] for x in pool[:2]], "a": 0, "cls": 1}
            ids.append(ctx.add(it, "cls:" + p["p"], ukey + " classroom"))
        csets.append({"k": "choose", "instr": "Choose the right phrase.", "items": ids})
        mids = [ctx.add({"k": "match", "t": "pair", "l": p["s"], "r": p["p"], "cls": 1}, "clsm:" + p["p"], ukey) for p in phrases]
        csets.append({"k": "match", "instr": "Match.", "items": mids})
        for n, s in enumerate(csets, 1):
            s["id"] = f"{ukey}.c.s{n}"
            self.finish_set(s, unit, "classroom")
        order_lines = [l.strip() for l in mod.CLASSROOM.get("order", "").strip().splitlines() if l.strip()]
        if order_lines:
            lines = []
            for l in order_lines:
                who, _, txt = l.partition(":")
                lines.append([who.strip(), txt.strip()])
                self.gate_text(unit, "classroom dialogue", txt.strip())
            it = {"k": "dorder", "t": "lines", "lines": lines}
            lid = ctx.add(it, "clsorder:" + "|".join(t for _, t in lines), ukey)
            it["shuf"] = self.shuffle_lines(lid, len(lines))
            s = {"id": f"{ukey}.c.s3", "k": "dorder", "instr": "Put the dialogue in order.", "items": [lid], "n": 1}
            csets.append(s)
        U["cls"]["sets"] = csets

        # reading
        R = mod.READING
        U["reading"] = {"title": R["title"], "text": R["text"]}
        self.gate_text(unit, "reading", R["title"] + ". " + R["text"])
        rsets = self.sets_from(R["qs"], ctx, f"{ukey}.r", unit, "reading")
        nq = sum(len(s["items"]) for s in rsets)
        if not (6 <= nq <= 8):
            self.err(f"[reading] {ukey}: {nq} questions (need 6–8)")
        flat = re.sub(r"\s+", " ", R["text"]).lower()
        for s in rsets:
            for i in s["items"]:
                it = self.items[i]
                if not it.get("ev"):
                    self.err(f"[reading] {ukey}: question without @evidence: {it.get('q')}")
                elif re.sub(r"\s+", " ", it["ev"]).lower() not in flat:
                    self.err(f"[reading] {ukey}: evidence not in the text: '{it['ev']}'")
        U["reading"]["sets"] = rsets
        wc = len(re.findall(r"[A-Za-z']+", R["text"]))
        U["reading"]["wc"] = wc
        self.stats.setdefault("reading_words", {})[unit] = wc

        # dialogue
        D = mod.DIALOGUE
        lines = []
        dids = []
        for n, raw in enumerate(D["lines"].strip().splitlines(), 1):
            who, _, txt = raw.strip().partition(":")
            txt = txt.strip()
            lines.append([who.strip(), re.sub(r"\[([^\]|]+)(\|[^\]]*)?\]", r"\1", txt)])
            self.gate_text(unit, "dialogue", lines[-1][1])
        if not (6 <= len(lines) <= 10):
            self.err(f"[data] {ukey}: dialogue must have 6–10 lines (has {len(lines)})")
        dsets = []
        if D.get("task", "gaps") in ("gaps", "both"):
            txt = "## bank: Complete the dialogue." + ("" if not D.get("extra") else " | +" + ", ".join(D["extra"])) + "\n"
            for raw in D["lines"].strip().splitlines():
                if "[" in raw:
                    txt += raw.strip() + "\n"
            ss = self.sets_from(txt, ctx, f"{ukey}.d", unit, "dialogue")
            for s in ss:
                s["k"] = "bank"
                s["dlg"] = 1
                for i in s["items"]:
                    q = self.items[i]["q"]
                    who, _, rest = q.partition(":")
                    self.items[i]["sp"] = who.strip()
                    self.items[i]["q"] = rest.strip()
                gi = iter(s["items"])
                s["lines"] = [[who, txt, next(gi) if "[" in raw else None]
                              for (who, txt), raw in zip(lines, D["lines"].strip().splitlines())]
            dsets += ss
        if D.get("task", "gaps") in ("order", "both"):
            it = {"k": "dorder", "t": "lines", "lines": lines}
            lid = ctx.add(it, "dorder:" + "|".join(t for _, t in lines), ukey)
            it["shuf"] = self.shuffle_lines(lid, len(lines))
            dsets.append({"id": f"{ukey}.d.o", "k": "dorder", "instr": "Put the dialogue in order.", "items": [lid], "n": 1})
        U["dialogue"] = {"title": D["title"], "intro": D.get("intro", ""), "lines": lines, "sets": dsets,
                         "task": D.get("task", "gaps")}
        if D.get("intro"):
            self.gate_text(unit, "dialogue intro", D["intro"])

        # write the question
        U["wq"] = self.sets_from("## wq: Write the question.\n" + mod.WQ, ctx, f"{ukey}.q", unit, "write the question")

        # writing
        U["writing"] = []
        for wi, w in enumerate(mod.WRITING, 1):
            U["writing"].append({"id": f"{ukey}.wr{wi}", "task": w["task"], "model": w["model"], "check": w["check"],
                                 "min": w.get("min", 20), "max": w.get("max", 80), "tip": w.get("tip", "")})
            self.gate_text(unit, "writing task", w["task"] + " " + w.get("tip", ""))
            self.gate_text(unit, "writing model", w["model"])
            for c in w["check"]:
                self.gate_text(unit, "writing self-check", c)
            if not (3 <= len(w["check"]) <= 5):
                self.err(f"[data] {ukey} writing {wi}: self-check must have 3–5 items")
        if not (1 <= len(U["writing"]) <= 2):
            self.err(f"[data] {ukey}: 1–2 writing tasks")

        U["cando"] = list(mod.CANDO)
        for c in U["cando"]:
            self.gate_text(unit, "I can", c)
        if not (4 <= len(U["cando"]) <= 6):
            self.err(f"[data] {ukey}: 4–6 'I can' statements")

        self.build_games_and_test(U, words, ukey, unit, odd_sets)

        # counts
        def count(sets):
            return sum(len(s["items"]) for s in sets if s)
        scored = count(U["wsets"]) + sum(count(g["sets"]) + (len(g["quick"]["items"]) if g["quick"] else 0) for g in U["grammar"])
        scored += count(U["cls"]["sets"]) + count(U["reading"]["sets"]) + count(U["dialogue"]["sets"]) + count(U["wq"])
        U["scored"] = scored
        self.stats.setdefault("scored", {})[unit] = scored
        if scored < 150:
            self.err(f"[volume] {ukey}: {scored} scored items (aim 150+)")
        return U, book

    def shuffle_lines(self, lid, n):
        for attempt in range(500):
            rng = random.Random(f"{lid}:{attempt}")
            o = list(range(n))
            rng.shuffle(o)
            if o[0] != 0 and all(o[i + 1] != o[i] + 1 for i in range(n - 1)):
                return o
        return list(reversed(range(n)))

    def gate_visual(self, unit, label, v):
        if not v:
            self.err(f"[data] {self.code} U{unit} {label}: no visual")
            return
        def walk(x):
            if isinstance(x, str):
                yield x
            elif isinstance(x, (list, tuple)):
                for y in x:
                    yield from walk(y)
            elif isinstance(x, dict):
                for k2, y in x.items():
                    if k2 not in ("type", "color", "c"):
                        yield from walk(y)
        for s in walk(v):
            if re.search(r"[A-Za-z]{2,}", s):
                self.gate_text(unit, label + " visual", s)
        if v.get("type") == "clocks":
            for t in v["times"]:
                if not G.PART_OF_DAY.search(t[1]):
                    self.err(f"[clock] {self.code} U{unit} {label}: clock {t[0]} has no part of the day: '{t[1]}'")

    # ------------------------------------------------------------ games & test
    def deck(self, deck_id, ids):
        ch = [i for i in ids if self.items[i]["t"] == "choice"]
        if not ch:
            return list(ids)
        new = G.reorder_until(deck_id, ch, G.slot_problems, lambda i: self.items[i]["a"], tries=50)
        if new is None:
            new = G.arrange(deck_id, ch, lambda i: self.items[i]["a"])
        if new is None:
            self.err(f"[positions] deck {deck_id} cannot pass")
            return ids
        others = [i for i in ids if self.items[i]["t"] != "choice"]
        if not others:
            return new
        # spread the non-choice items through the deck; choice items keep their gated order
        out, step = [], max(1, len(new) // (len(others) + 1))
        oi = iter(others)
        for k, i in enumerate(new):
            out.append(i)
            if (k + 1) % step == 0:
                nx = next(oi, None)
                if nx:
                    out.append(nx)
        out += list(oi)
        return out

    def build_games_and_test(self, U, words, ukey, unit, odd_sets):
        rng = random.Random(ukey + ":games")
        gram_sets = [s for g in U["grammar"] for s in g["sets"]]
        choice = [i for s in gram_sets for i in s["items"] if self.items[i]["t"] == "choice" and not self.items[i].get("tf") and s["k"] == "choose"]
        typed = [i for s in gram_sets for i in s["items"] if self.items[i]["t"] == "typed" and len(self.items[i]["acc"][0]) <= 40]
        order = [i for s in gram_sets for i in s["items"] if self.items[i]["t"] == "order"]
        which = [w["qid"] for w in words if w.get("qid")]
        cls_choice = [i for i in U["cls"]["sets"][0]["items"]]
        games = {}
        # memory pairs: word <-> short meaning, plus grammar match pairs
        mem = [[w["w"], w["d"], w.get("syn", "")] for w in words if len(w["d"]) <= 40 and len(w["w"]) <= 24]
        for s in gram_sets:
            if s["k"] == "match":
                mem += [[self.items[i]["l"], self.items[i]["r"], ""] for i in s["items"] if len(self.items[i]["r"]) <= 40]
        games["memory"] = mem
        sp = list(choice)
        rng.shuffle(sp)
        games["speed"] = self.deck(ukey + ":speed", sp[:40] + [i for i in which[:10]])
        fall = []
        for i in choice:
            it = self.items[i]
            if "___" in it["q"] and all(len(o) <= 16 for o in it["o"]) and len(it["q"]) <= 70:
                fall.append(i)
        rng.shuffle(fall)
        games["falling"] = self.deck(ukey + ":fall", fall[:30])
        b = [i for i in order if len(self.items[i]["toks"]) <= 9]
        rng.shuffle(b)
        games["builder"] = b[:12]
        games["odd"] = self.deck(ukey + ":odd", [i for s in odd_sets for i in s["items"]])
        games["balloon"] = [[w["w"].lower(), w["d"]] for w in words if re.match(r"^[A-Za-z]{3,12}$", w["w"])]
        esc = list(choice)
        rng.shuffle(esc)
        games["escape"] = self.deck(ukey + ":escape", esc[:24])
        games["cls"] = self.deck(ukey + ":cls", cls_choice)

        if self.series == "starter":
            lst = ["memory", "speed", "falling", "balloon", "escape"] if unit % 2 else ["memory", "builder", "odd", "balloon", "escape"]
        else:
            lst = ["memory", "speed", "falling", "builder", "escape"] if unit % 2 else ["memory", "speed", "odd", "builder", "escape"]
        need = {"memory": 6, "speed": 15, "falling": 10, "builder": 5, "odd": 5, "balloon": 8, "escape": 15}
        for gname in list(lst):
            if len(games[gname]) < need[gname]:
                self.err(f"[games] {ukey}: not enough data for {gname} ({len(games[gname])}/{need[gname]})")
        games["list"] = lst
        U["games"] = games

        # unit test: 25 items, mixed, from every grammar point
        pick = []
        per_g = []
        for g in U["grammar"]:
            ch = [i for s in g["sets"] for i in s["items"] if self.items[i]["t"] == "choice" and not self.items[i].get("tf") and s["k"] == "choose"]
            ty = [i for s in g["sets"] for i in s["items"] if self.items[i]["t"] == "typed"]
            od = [i for s in g["sets"] for i in s["items"] if self.items[i]["t"] == "order"]
            per_g.append((ch, ty, od))
        r2 = random.Random(ukey + ":test")
        quotas = (11, 7, 4)
        for kind in range(3):
            pools = [list(p[kind]) for p in per_g]
            for p in pools:
                r2.shuffle(p)
            k = 0
            got = 0
            while got < quotas[kind] and any(pools):
                p = pools[k % len(pools)]
                if p:
                    pick.append(p.pop())
                    got += 1
                k += 1
        wq = [i for i in which]
        r2.shuffle(wq)
        pick += wq[: 25 - len(pick)]
        r2.shuffle(pick)
        test = self.deck(ukey + ":test", pick[:25])
        spare = [i for p in per_g for i in p[1] + p[2] if i not in test]
        r2.shuffle(spare)
        while len(test) < 25 and spare:
            test.insert(r2.randrange(len(test) + 1), spare.pop())
        U["test"] = test
        if len(U["test"]) != 25:
            self.err(f"[data] {ukey}: unit test has {len(U['test'])} items (need 25)")
