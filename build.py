#!/usr/bin/env python3
"""Build the four practice apps into dist/ and run every quality gate.

    python3 build.py              build all levels, run all gates incl. the browser smoke test
    python3 build.py a11 a12      build only these levels
    python3 build.py --no-browser skip the Playwright smoke test (NOT for a final build)

Exits non-zero if any gate fails.
"""
import base64
import glob
import json
import os
import random
import re
import subprocess
import sys
import urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)

from buildlib.compile import LevelCompiler, COMMON  # noqa: E402
from buildlib import gates as G  # noqa: E402
from buildlib.levelgate import LevelGate, chunk_regex  # noqa: E402
from buildlib.norm import norm, PARITY_CASES  # noqa: E402

LEVELS = [
    dict(code="a11", title="A1.1 Practice", book="Cutting Edge Starter (New Edition)", units="Units 1–6",
         series="starter", verbs=False, pp=False, out="A1.1 Practice.html", clsmax=1),
    dict(code="a12", title="A1.2 Practice", book="Cutting Edge Starter (New Edition)", units="Units 7–12",
         series="starter", verbs=True, pp=False, out="A1.2 Practice.html", clsmax=2),
    dict(code="a21", title="A2.1 Practice", book="Cutting Edge Elementary (3rd edition)", units="Units 1–7",
         series="elementary", verbs=True, pp=False, out="A2.1 Practice.html", clsmax=3),
    dict(code="a22", title="A2.2 Practice", book="Cutting Edge Elementary (3rd edition)", units="Units 8–14",
         series="elementary", verbs=True, pp=True, out="A2.2 Practice.html", clsmax=4),
]

FONT_CSS_URL = "https://fonts.googleapis.com/css2?family=Nunito:wght@400..900&display=swap"
FONT_DIR = os.path.join(ROOT, "assets", "fonts")
MAX_BYTES = 4 * 1024 * 1024


def log(*a):
    print(*a, flush=True)


# ---------------------------------------------------------------- font
def get_font():
    """Download Nunito (400..900) from Google Fonts; fall back to the cached copy, then to no font."""
    note = ""
    files = {"latin": os.path.join(FONT_DIR, "nunito-latin.woff2"), "latin-ext": os.path.join(FONT_DIR, "nunito-latin-ext.woff2")}
    try:
        req = urllib.request.Request(FONT_CSS_URL, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0 Safari/537.36"})
        css = urllib.request.urlopen(req, timeout=20).read().decode()
        for subset in ("latin-ext", "latin"):
            m = re.search(r"/\* " + re.escape(subset) + r" \*/.*?url\((https://[^)]+\.woff2)\)", css, re.S)
            if m:
                data = urllib.request.urlopen(m.group(1), timeout=20).read()
                if data[:4] == b"wOF2":
                    os.makedirs(FONT_DIR, exist_ok=True)
                    open(files[subset], "wb").write(data)
        note = "Nunito downloaded from Google Fonts at build time"
    except Exception as e:  # network blocked: use cache
        note = f"Google Fonts not reachable ({type(e).__name__}); used the cached copy in assets/fonts"
    ranges = {
        "latin": "U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD",
        "latin-ext": "U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304, U+0308, U+0329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C4, U+2113, U+2C60-2C7F, U+A720-A7FF",
    }
    css = ""
    for subset, path in files.items():
        if os.path.exists(path):
            b64 = base64.b64encode(open(path, "rb").read()).decode()
            css += ("@font-face{font-family:'Nunito';font-style:normal;font-weight:400 900;font-display:swap;"
                    f"src:url(data:font/woff2;base64,{b64}) format('woff2');unicode-range:{ranges[subset]};}}\n")
    if not css:
        note = "Nunito NOT available: the apps fall back to 'Varela Round', system-ui"
    return css, note


# ---------------------------------------------------------------- level
def build_level(L, font_css, report):
    code = L["code"]
    comp = LevelCompiler(L)
    paths = sorted(glob.glob(os.path.join(ROOT, "content", code, "u*.py")))
    if not paths:
        report.append(f"{L['title']}: no content yet")
        return None
    units = []
    books = {}
    for p in paths:
        U, book = comp.compile_unit(p, [])
        units.append(U)
        books[U["n"]] = book
    units.sort(key=lambda u: u["n"])

    # level gate (source data)
    chunks = [p["p"] for p in COMMON.CLASSROOM_ALL] + list(COMMON.CHUNKS.get(L["series"], []))
    lg = LevelGate(L["series"], chunks)
    first = units[0]["n"]
    for u in units:
        earlier = [b for n, bl in books.items() if n <= u["n"] for b in bl]
        u["_bookrx"] = chunk_regex([re.sub(r"\s*\([^)]*\)", "", b) for b in earlier])
    level_errors = []
    for unit, label, text in comp.texts:
        u = next(x for x in units if x["n"] == unit)
        short = label.endswith("option") and len(text.split()) <= 2 or label.endswith("visual")
        for name, hits in lg.check(text, unit, u["_bookrx"], short=short):
            level_errors.append(f"[level] {L['title']} U{unit} {label}: {name}: {', '.join(hits)} — \"{text[:90]}\"")
    for u in units:
        u.pop("_bookrx", None)

    # level-wide sections
    data = {
        "code": code, "title": L["title"], "book": L["book"], "unitsLabel": L["units"],
        "storageKey": f"eid-practice-{code}-v1", "series": L["series"],
        "units": units, "items": comp.items, "guessWords": comp.guess_all,
        "classroom": [dict(p=p["p"], s=p["s"], who=p["who"], lvl=p["lvl"]) for p in COMMON.CLASSROOM_ALL if p["lvl"] <= L["clsmax"]],
        "smarter": COMMON.SMARTER, "resources": COMMON.RESOURCES,
        "verbs": [v for v in COMMON.VERBS if v[3] <= L["clsmax"]] if L["verbs"] else [],
        "pp": L["pp"], "parity": PARITY_CASES,
    }
    # level review: ~60 items across units + boss deck
    rng = random.Random(code + ":review")
    review = []
    per = max(8, 60 // len(units))
    for u in units:
        pool_c = [i for g in u["grammar"] for s in g["sets"] for i in s["items"] if comp.items[i]["t"] == "choice" and s["k"] == "choose" and i not in u["test"]]
        pool_t = [i for g in u["grammar"] for s in g["sets"] for i in s["items"] if comp.items[i]["t"] in ("typed", "order") and i not in u["test"]]
        rng.shuffle(pool_c)
        rng.shuffle(pool_t)
        review += pool_c[: per * 6 // 10] + pool_t[: per - per * 6 // 10]
    review = review[:62]
    rng.shuffle(review)
    data["review"] = comp.deck(code + ":review", review)
    boss = [i for i in data["review"] if comp.items[i]["t"] == "choice"]
    extra = [i for u in units for i in u["games"]["speed"] if i not in boss]
    rng.shuffle(extra)
    data["boss"] = comp.deck(code + ":boss", boss + extra[: max(0, 40 - len(boss))])
    if len(data["review"]) < 55:
        comp.err(f"[data] {code}: level review has {len(data['review'])} items (need ~60)")

    # ID lock: every item, set and word ID from v1 must still exist (saved progress stays linked)
    lock_path = os.path.join(ROOT, "buildlib", "idlock", f"{code}-v1.json")
    if os.path.exists(lock_path):
        lock = json.load(open(lock_path))
        set_ids = set()
        for u in units:
            for ss in u["wsets"] + [x for g in u["grammar"] for x in ([g["quick"]] if g["quick"] else []) + g["sets"]] \
                    + u["cls"]["sets"] + u["reading"]["sets"] + u["dialogue"]["sets"] + u["wq"]:
                set_ids.add(ss["id"])
        word_ids = {w["id"] for u in units for w in u["words"]}
        for kind, have in (("items", set(comp.items)), ("sets", set_ids), ("words", word_ids)):
            lost = [x for x in lock[kind] if x not in have]
            if lost:
                comp.err(f"[ids] {code}: {len(lost)} {kind} from v1 are missing (saved progress would break), e.g. {lost[:5]}")
    for e in comp.errors + level_errors:
        report.append("FAIL " + e)
    for w in comp.warnings:
        report.append("warn " + w)
    stats = comp.stats
    return data, comp, level_errors, stats


def cultural_mix(texts):
    cats = {k: 0 for k in ("damascus", "syria", "world")}
    blob = " ".join(t for _, _, t in texts)
    for cat, names in COMMON.PLACES.items():
        for n in names:
            cats[cat] += len(re.findall(r"(?<![\w])" + re.escape(n) + r"(?![\w])", blob))
    tot = sum(cats.values()) or 1
    return {k: round(100 * v / tot) for k, v in cats.items()}, cats


# ---------------------------------------------------------------- html
def assemble(L, data, font_css):
    tpl = open(os.path.join(ROOT, "engine", "template.html"), encoding="utf-8").read()
    css = open(os.path.join(ROOT, "engine", "app.css"), encoding="utf-8").read()
    js = "\n".join(open(os.path.join(ROOT, "engine", f), encoding="utf-8").read()
                   for f in ("util.js", "visuals.js", "exercises.js", "games.js", "puzzles.js", "app.js"))
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    html = (tpl.replace("@@TITLE@@", L["title"])
               .replace("/*@@FONT@@*/", font_css)
               .replace("/*@@CSS@@*/", css)
               .replace("@@DATA@@", payload)
               .replace("/*@@JS@@*/", js))
    out = os.path.join(ROOT, "dist", L["out"])
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(html)
    return out


def gate_built(L, path, report):
    """Gates on the BUILT file: size, no external requests, data survives escaping, markup leftovers."""
    errs = []
    raw = open(path, encoding="utf-8").read()
    size = len(raw.encode("utf-8"))
    if size > MAX_BYTES:
        errs.append(f"[size] {L['out']} is {size / 1e6:.2f} MB (max 4 MB)")
    m = re.search(r'<script id="app-data" type="application/json">(.*?)</script>', raw, re.S)
    if not m:
        errs.append(f"[built] {L['out']}: data block not found")
        return errs, size, None
    data = json.loads(m.group(1).replace("<\\/", "</"))
    # no network: no http(s) URLs in src/href/url() except plain links in the Resources list
    for mm in re.finditer(r"(src|href)\s*=\s*[\"'](https?:)?//", raw):
        errs.append(f"[built] {L['out']}: external reference {mm.group(0)}")
    for mm in re.finditer(r"url\(\s*['\"]?https?:", raw):
        errs.append(f"[built] {L['out']}: external url() in CSS")
    for mm in re.finditer(r"@import", raw):
        errs.append(f"[built] {L['out']}: @import found")
    # markup leftovers inside the data
    blob = json.dumps(data, ensure_ascii=False)
    for bad, why in (("**", "markdown bold"), ("&amp;", "double-escaped &"), ("&lt;", "escaped <"), ("&#", "HTML entity"),
                     ("undefined", "undefined"), ("NaN", "NaN"), ("[object", "[object"), ("B2BEC3", "unreadable grey")):
        if bad in blob:
            errs.append(f"[built] {L['out']}: data contains {why} ({bad})")
    if "B2BEC3" in raw.upper():
        errs.append(f"[built] {L['out']}: uses #B2BEC3")
    if re.search(r"<details", raw):
        errs.append(f"[built] {L['out']}: uses <details>")
    if re.search(r"(speechSynthesis|SpeechSynthesisUtterance|new Audio\(|<audio)", raw):
        errs.append(f"[built] {L['out']}: audio found")
    if re.search(r"\binstitute\b", raw, re.I):
        errs.append(f"[built] {L['out']}: the word 'institute' appears")
    if raw.count("© Eid Almunajed") < 1:
        errs.append(f"[built] {L['out']}: footer missing")
    return errs, size, data


def run_smoke(paths, report):
    script = os.path.join(ROOT, "tests", "smoke.mjs")
    env = dict(os.environ)
    gl = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
    env["NODE_PATH"] = gl
    try:
        r = subprocess.run(["node", script] + paths, capture_output=True, text=True, env=env, timeout=3000)
    except FileNotFoundError:
        report.append("SKIP browser smoke test: node not found")
        return True, "node not found"
    out = (r.stdout or "") + (r.stderr or "")
    report.append(out.strip())
    return r.returncode == 0, out


def write_review(results, smoke_out, font_note):
    path = os.path.join(ROOT, "REVIEW.md")
    text = open(path, encoding="utf-8").read() if os.path.exists(path) else "# REVIEW\n\n<!-- AUTO:arabic -->\n<!-- /AUTO:arabic -->\n\n<!-- AUTO:gates -->\n<!-- /AUTO:gates -->\n"
    ar = ["English is shown first; the Arabic opens with the عربي pill or the global \"Arabic help\" switch.\n"]
    cell = lambda xs: "<br>".join(x.replace("|", "\\|") for x in xs) or "—"
    for L, comp in results:
        ar.append(f"\n### {L['title']}\n")
        cur = None
        for unit, title, en, arl in comp.cards:
            if unit != cur:
                ar.append(f"\n**Unit {unit}**\n\n| Grammar card | In simple words | عربي |\n|---|---|---|")
                cur = unit
            ar.append(f"| {title} | {cell(en)} | {cell(arl)} |")
    ar.append("\n### Learn Smarter (same in all four apps)\n\n| Slide | English | عربي |\n|---|---|---|")
    for tip in COMMON.SMARTER:
        for sl in tip["slides"]:
            if sl.get("ar") or re.search(r"[\u0600-\u06FF]", sl["t"]):
                ar.append(f"| {tip['title']} — {sl['h']} | {sl['t']} | {sl.get('ar', '')} |")
    ar_block = "\n".join(ar) + "\n"
    text = re.sub(r"<!-- AUTO:arabic -->.*?<!-- /AUTO:arabic -->", lambda m: "<!-- AUTO:arabic -->\n" + ar_block + "<!-- /AUTO:arabic -->", text, flags=re.S)
    gates_block = "```\n" + smoke_out.strip() + "\n```\n"
    text = re.sub(r"<!-- AUTO:gates -->.*?<!-- /AUTO:gates -->", lambda m: "<!-- AUTO:gates -->\n" + gates_block + "<!-- /AUTO:gates -->", text, flags=re.S)
    open(path, "w", encoding="utf-8").write(text)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    no_browser = "--no-browser" in sys.argv
    levels = [L for L in LEVELS if not args or L["code"] in args]
    font_css, font_note = get_font()
    report = [f"Font: {font_note}"]
    ok = True
    results = []
    built = []
    summary = []
    for L in levels:
        log(f"== {L['title']}")
        res = build_level(L, font_css, report)
        if res is None:
            continue
        data, comp, level_errors, stats = res
        if comp.errors or level_errors:
            ok = False
        path = assemble(L, data, font_css)
        errs, size, _ = gate_built(L, path, report)
        for e in errs:
            report.append("FAIL " + e)
        if errs:
            ok = False
        built.append(path)
        results.append((L, comp))
        mix, raw = cultural_mix(comp.texts)
        n_items = sum(u["scored"] for u in data["units"])
        summary.append(
            f"{L['title']}: {len(data['units'])} units, {n_items} scored items "
            f"({', '.join('U%d %d' % (u['n'], u['scored']) for u in data['units'])}), "
            f"{len(data['review'])} level-review items, {len(comp.arabic)} Arabic lines, "
            f"{size / 1e6:.2f} MB; reading words {stats.get('reading_words')}; "
            f"places mix Damascus {mix['damascus']}% / Syria {mix['syria']}% / world {mix['world']}% ({raw})"
        )
        log(f"   {len(comp.errors) + len(level_errors)} data/level problems, {size / 1e6:.2f} MB")
    report.append("")
    report += summary
    os.makedirs(os.path.join(ROOT, "build"), exist_ok=True)
    json.dump([[c, norm(c)] for c in PARITY_CASES], open(os.path.join(ROOT, "build", "parity.json"), "w"))
    if built and not no_browser:
        sok, _ = run_smoke(built, report)
        ok = ok and sok
    elif no_browser:
        report.append("SKIP browser smoke test (--no-browser)")
    fails = [l for r in report for l in r.splitlines() if l.startswith("FAIL")]
    report.append("")
    report.append("RESULT: " + ("ALL GATES PASSED" if ok and not fails else f"FAILED ({len(fails)} problems)"))
    out = "\n".join(report)
    os.makedirs(os.path.join(ROOT, "build"), exist_ok=True)
    open(os.path.join(ROOT, "build", "gate-report.txt"), "w", encoding="utf-8").write(out)
    if not args and not no_browser:
        write_review(results, out, font_note)
    log(out if len(out) < 20000 else out[:10000] + "\n...\n" + out[-8000:])
    sys.exit(0 if ok and not fails else 1)


if __name__ == "__main__":
    main()
