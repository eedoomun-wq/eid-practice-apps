# eid-practice-apps

Four offline practice apps for adult learners — **A1.1, A1.2, A2.1 and A2.2 Practice** —
by Eid Almunajed. Each app is one self-contained HTML file in `dist/` (inline CSS, JS and
font, no internet needed). Students open it on a phone; in class it runs on a projector
with **Class mode**.

| File | Book | Units |
|---|---|---|
| `dist/A1.1 Practice.html` | Cutting Edge Starter (New Edition) | 1–6 |
| `dist/A1.2 Practice.html` | Cutting Edge Starter (New Edition) | 7–12 |
| `dist/A2.1 Practice.html` | Cutting Edge Elementary (3rd edition) | 1–7 |
| `dist/A2.2 Practice.html` | Cutting Edge Elementary (3rd edition) | 8–14 |

Never edit the files in `dist/` by hand — they are rebuilt from the content files.

## Rebuild

You need Python 3.10+ and (for the browser test) Node with Playwright + Chromium.

```bash
python3 build.py                # build all four apps and run every gate (incl. the browser test)
python3 build.py a11 a22        # build only some levels
python3 build.py --no-browser   # skip the browser smoke test (quick check while editing)
```

The build **exits with an error** if any gate fails, and writes the full report to
`build/gate-report.txt`. A full build (all levels, with the browser test) also refreshes
the two automatic parts of `REVIEW.md`: the list of every Arabic line and the gate results.

The font (Nunito 400–900) is downloaded from Google Fonts during the build and embedded as
base64. If the download fails, the cached copy in `assets/fonts/` is used. Without either,
the apps fall back to 'Varela Round', system-ui.

## File map

```
build.py                 build + all gates; writes dist/ and REVIEW.md (auto parts)
buildlib/
  dsl.py                 the exercise mini-language (see below)
  compile.py             turns one unit file into app data; makes word practice, games, tests
  gates.py               answer-position, True/False and a/an gates + seeded shuffles
  levelgate.py           "no grammar from a later unit" checks (regex + chunk list)
  norm.py                answer normalising (same rules as norm() in engine/util.js)
engine/                  the ONE shared app (used by all four levels)
  template.html, app.css
  util.js                DOM helpers, storage (try/catch everywhere), icons, normaliser
  visuals.js             drawn grammar visuals: tables, timelines, hands, street map, clocks…
  exercises.js           all exercise types, boards, scoring, unit test runner
  games.js               Memory Match, Speed Round, Falling Words, Sentence Builder Race,
                         Odd One Out, Balloon Spelling, Escape the Souq, Boss Battle
  app.js                 pages and router (Home, units, Review Pile, Progress…)
content/
  common.py              classroom-English bank, names and places, Learn Smarter tips,
                         Resources, irregular verbs
  a11/u01.py … u06.py    A1.1 units      a12/u07.py … u12.py   A1.2 units
  a21/u01.py … u07.py    A2.1 units      a22/u08.py … u14.py   A2.2 units
tests/smoke.mjs          Playwright test: every unit/section/game at 375×812 and 1920×1080
assets/fonts/            cached Nunito woff2 files
dist/                    the four finished apps
```

## Editing content

Each unit is one Python file, e.g. `content/a11/u03.py`. Change it, run `python3 build.py`,
and fix anything the gates report.

* `META` — unit number, title, book pages.
* `BOOK` — the book's word list for the unit (the build checks every one is in `WORDS`).
* `WORDS` — one word per line: `word | simple definition | example sentence` (+ optional
  `| key words;to find | synonym-group`). `@Category` starts a group. `+word` marks an extra word.
* `GRAMMAR` — one `dict` per grammar card: `visual`, `pattern`, `examples`, `ar` (2–4 Arabic
  lines), `watch` (wrong → right), `quick` (3-item quick check) and `sets` (4+ exercise sets).
* `ODD`, `CLASSROOM`, `READING`, `DIALOGUE`, `WQ` (write the question), `WRITING`, `CANDO`.

Word practice, games, the 25-item unit test and the Level Review are generated
automatically from the unit's data.

### The exercise mini-language

```
## choose: Choose the answer.            first option is the right one; the build shuffles
I ___ a student. | am | are | is
## gap: Write the missing word.          [right|also right]
I [am|'m] from Damascus.
## order: Put the words in order.        || = another correct order
How are you?
## fix: Find and fix the mistake.        [wrong>right|also right]
I [are>am|'m] a student.
## match: Match.                         left = right
hello = goodbye
## sort: Sort the words. | a | an        group: items
a: teacher, student
## bank: Use the words.                  gaps filled from a word bank (+extra, words)
I [am] Layla.
## transform: Make it negative.          also: short, wq, numbers, spell
I'm a teacher. (−) => I'm not a teacher. | I am not a teacher.
## tf: True or false?                    reading: add  @ evidence copied from the text
Layla is a student. | T @ I'm a student
```

Typed answers ignore case, extra spaces, end punctuation and curly/straight apostrophes,
and accept contractions both ways (n't, 'm, 're, 've, 'll). **'s is never expanded
automatically** — list both forms, e.g. `She's not | She isn't`.

## Quality gates (the build fails if any breaks)

1. Answer positions: seeded shuffles; no 3 in a row in one slot, no a-b-a-b, no rotation,
   no slot over 50%; True/False keys mixed (re-rolled until they pass).
2. Distractors: checked by hand while writing (the build can't judge meaning).
3. Article giveaway: `a ___` / `an ___` fails if options start with vowel and consonant sounds.
4. Level gate: no grammar from a later unit in any student-facing text (classroom chunks and
   word definitions are exempt).
5. Book-word coverage, 6. reading alignment (every question carries evidence from the text),
7. data integrity (no empty sets, no duplicates, enough data for every game),
8. browser smoke test: no console errors, no horizontal scroll, every section opens,
   scoring works, progress survives a reload, works with storage blocked, Class mode zoom.

Also checked on the built files: size under 4 MB, no network requests, no `<details>`,
no audio, no markdown/escaping leftovers, the "© Eid Almunajed" footer.
