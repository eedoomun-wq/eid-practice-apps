# eid-practice-apps

Four offline practice apps for adult learners — **A1.1, A1.2, A2.1 and A2.2 Practice** —
by Eid Almunajed. Each app is one self-contained HTML file in `dist/` (inline CSS, JS and
font, no internet needed). Students open it on a phone; in class it runs on a projector
with **Class mode**.

Each unit is a path of 4 steps — **Learn** (Words · Grammar), **Practise** (Word practice ·
Grammar practice · Classroom English · Write the question), **Use it** (Reading · Dialogue ·
Writing) and **Play & check** (Games · Puzzles · Unit test · I can…). Exercises run one
question per screen. Grammar is explained in simple English first; the Arabic opens with the
**عربي** pill on each card, or everywhere with the **Arabic help** switch at the top (saved).

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
the automatic parts of `REVIEW.md`: English beside Arabic for every grammar card, the full
text of every puzzle (with solutions and codes), the gate results and the page heights.

Screenshots for REVIEW: `node tests/screens.mjs after "dist/A1.1 Practice.html" …` writes
`docs/screens/after/` (phone 390×844 full pages + projector 1920×1080 in Class mode).

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
  norm.py                answer normalising (same rules as norm() in engine/util.js),
                         incl. British/American spelling folding (colour/color, -ise/-ize…)
  puzzles.py             puzzle builders and validators: case solver, crossword, word search,
                         escape-room locks, riddles, guess-the-word lists
  idlock/                every item / set / word ID of the v1 apps (the build fails if one is lost)
engine/                  the ONE shared app (used by all four levels)
  template.html, app.css
  util.js                DOM helpers, storage (try/catch everywhere), icons, normaliser
  visuals.js             drawn grammar visuals: tables, timelines, hands, street map, clocks…
  exercises.js           all exercise types, boards, scoring; the player (one question per
                         screen, Check bar, feedback sheet) and the test player
  games.js               Memory Match, Speed Round, Falling Words, Sentence Builder Race,
                         Odd One Out, Balloon Spelling, Escape the Souq, Boss Battle
  puzzles.js             the case, crossword + word search, escape room, guess the word +
                         What am I?
  app.js                 pages and router (Home, units in 4 steps, Review Pile, Progress…)
content/
  common.py              classroom-English bank, names and places, Learn Smarter tips,
                         Resources, irregular verbs
  a11/u01.py … u06.py    A1.1 units      a12/u07.py … u12.py   A1.2 units
  a21/u01.py … u07.py    A2.1 units      a22/u08.py … u14.py   A2.2 units
tests/smoke.mjs          Playwright test: every route, set, game and puzzle at 390×844, 360×740
                         and 1920×1080 Class mode; v1 → v2 progress migration (tests/fixtures/)
tests/screens.mjs        before/after screenshots for REVIEW.md (docs/screens/)
docs/notes/              the round-2 proofread change lists
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
* `GRAMMAR` — one `dict` per grammar card: `visual`, `pattern`, `en` (2–4 lines "In simple
  words", shown first; at A1.1 max 10 words a line and no grammar terms except verb / question /
  negative / one / more than one), `ar` (2–4 Arabic lines, hidden behind the عربي pill),
  `examples`, `watch` (wrong → right), `quick` (3-item quick check) and `sets` (4+ exercise sets).
* `ODD`, `CLASSROOM`, `READING`, `DIALOGUE`, `WQ` (write the question), `WRITING`, `CANDO`.
* `PUZZLES` — `case` (people, groups of values, clues with logic `("is"|"not", A, B)` and
  `need=False` for the red herring, question, reveal), `escape` (place, intro, ending) and
  `riddles` (6–8 × answer + 3 clues). The crossword, word search, escape-room locks and the
  guess-the-word list are built from the unit's words and grammar items.

To change an exercise line **without** losing learners' saved progress for it, keep its old ID:
add ` #id=<old id>` at the end of the line (the build's ID lock tells you which ID went missing).

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
accept contractions both ways (n't, 'm, 're, 've, 'll) and British or American spelling.
For **'s** the build adds the full form itself (*What's* → *What is*, *She's never used* →
*She has never used*), and a gate checks that every answer with 's lists it.
A fix-the-mistake item accepts the corrected word(s) or the whole corrected sentence.

## Quality gates (the build fails if any breaks)

1. Answer positions: seeded shuffles; no 3 in a row in one slot, no a-b-a-b, no rotation,
   no slot over 50%; True/False keys mixed (re-rolled until they pass).
2. Distractors: checked by hand while writing (the build can't judge meaning).
3. Article giveaway: `a ___` / `an ___` fails if options start with vowel and consonant sounds.
4. Level gate: no grammar from a later unit in any student-facing text (classroom chunks and
   word definitions are exempt).
5. Book-word coverage, 6. reading alignment (every question carries evidence from the text),
7. data integrity (no empty sets, no duplicates, enough data for every game),
8. ID lock: every item, set and word ID of the v1 apps still exists (saved progress keeps working),
9. spacing (no "I 'm"), complete pattern rows, full forms for 's, English box on every grammar
   card (A1.1: ≤ 10 words a line, no jargon), level gate on all English explanations and puzzle text,
10. puzzles: exactly one solution for every case (and every "needed" clue really needed, the
   answer never printed in a clue), crossword connected with no accidental words, every
   word-search word exactly once and no rude words, escape codes re-derived from the items and
   never visible, riddle answers from the unit's words, answer positions in puzzle choices,
11. browser smoke test at 390×844, 360×740 and 1920×1080 Class mode: no console errors, no
   horizontal scroll, every route, set, game and puzzle opens; scoring through the player;
   the unit test; fix-the-mistake with the full sentence; one count per wrong attempt; the
   Review Pile always empties; Falling Words tiles never overlap; Games is done only at an end
   screen; every puzzle solved through its test hook; the Arabic toggle; progress survives a
   reload; v1 saved progress loads (migration to v2); storage blocked; page heights.

Also checked on the built files: size under 4 MB, no network requests, no `<details>`,
no audio, no markdown/escaping leftovers, the "© Eid Almunajed" footer.
