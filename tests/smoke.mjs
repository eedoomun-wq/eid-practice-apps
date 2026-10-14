// Browser smoke test for the built apps. Run by build.py:  node tests/smoke.mjs "dist/A1.1 Practice.html" ...
// Phone 390×844 and 360×740, projector 1920×1080 in Class mode. Writes page heights to build/heights-<code>.json.
import { createRequire } from 'module';
import fs from 'fs';
import path from 'path';
import url from 'url';

const require = createRequire(import.meta.url);
let chromium;
try { ({ chromium } = require('playwright')); } catch (e) {
  console.log('SKIP browser smoke test: Playwright is not installed');
  process.exit(0);
}

const here = path.dirname(url.fileURLToPath(import.meta.url));
const root = path.join(here, '..');
const parity = JSON.parse(fs.readFileSync(path.join(root, 'build', 'parity.json'), 'utf8'));
const files = process.argv.slice(2);
const fails = [];
const notes = [];
function fail(f, msg) { fails.push(`FAIL [browser] ${path.basename(f)}: ${msg}`); }

const browser = await chromium.launch();

async function newPage(viewport, opts = {}) {
  const ctx = await browser.newContext({ viewport, deviceScaleFactor: 1, hasTouch: viewport.width < 600 });
  if (opts.blockStorage) {
    await ctx.addInitScript(() => {
      const thrower = () => { throw new Error('storage blocked'); };
      Object.defineProperty(window, 'localStorage', { get: thrower, configurable: true });
    });
  }
  if (opts.seed) await ctx.addInitScript((s) => { if (!sessionStorage.getItem('seeded')) { localStorage.setItem(s.key, s.value); sessionStorage.setItem('seeded', '1'); } }, opts.seed);
  if (opts.clock) await ctx.clock.install();
  const page = await ctx.newPage();
  const errors = [];
  const external = [];
  page.on('console', (m) => { if (m.type() === 'error') errors.push(m.text()); });
  page.on('pageerror', (e) => errors.push(String(e)));
  page.on('request', (r) => { const u = r.url(); if (!u.startsWith('file:') && !u.startsWith('data:') && !u.startsWith('about:')) external.push(u); });
  return { ctx, page, errors, external };
}
const go = (page, h) => page.evaluate((x) => window.__APP.go(x), h);
async function overflow(page) {
  return page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
}
async function leftovers(page) {
  return page.evaluate(() => {
    const t = document.getElementById('main').innerText;
    const bad = [];
    for (const [re, why] of [[/\{|\}/, 'curly brace'], [/\*\*/, '**'], [/___/, '___'], [/\bundefined\b/, 'undefined'], [/\bNaN\b/, 'NaN'], [/\[object/, '[object'], [/&amp;|&lt;|&gt;|&#\d+;/, 'HTML entity'], [/#id=/, '#id= pin']]) {
      const m = re.exec(t); if (m) bad.push(why + ' near "' + t.slice(Math.max(0, m.index - 30), m.index + 30).replace(/\s+/g, ' ') + '"');
    }
    return bad;
  });
}
async function smallTargets(page) {
  return page.evaluate(() => {
    const out = [];
    document.querySelectorAll('#main button, #main input, #main a, #main label.ck, header button').forEach((b) => {
      const r = b.getBoundingClientRect();
      const cs = getComputedStyle(b);
      if (r.width === 0 || r.height === 0 || cs.visibility === 'hidden') return;
      if (b.type === 'checkbox') return; // the label is the target
      if (r.height < 43.5 || r.width < 43.5) out.push((b.innerText || b.getAttribute('aria-label') || b.tagName).slice(0, 30) + ` ${Math.round(r.width)}x${Math.round(r.height)}`);
    });
    return out;
  });
}
const height = (page) => page.evaluate(() => document.documentElement.scrollHeight);

for (const f of files) {
  const fileUrl = url.pathToFileURL(path.resolve(f)).href;
  const name = path.basename(f);
  // ---------------- phone 390×844
  const P = await newPage({ width: 390, height: 844 });
  await P.page.goto(fileUrl);
  await P.page.waitForFunction(() => window.__APP);
  const data = await P.page.evaluate(() => ({
    key: window.__APP.data.storageKey,
    units: window.__APP.data.units.map((u) => ({ n: u.n, games: u.games.list, grammar: u.grammar.map((g) => g.id), puzzles: (u.puzzles || []).map((p) => p.id) })),
    sections: window.__APP.sections, verbs: window.__APP.data.verbs.length, smarter: window.__APP.data.smarter.map((s) => s.id),
    sets: window.__APP.sets().map((s) => [s, window.__APP.setInfo(s)])
  }));
  const code = (/eid-practice-(\w+)-v1/.exec(data.key) || [])[1];
  const got = await P.page.evaluate((cases) => cases.map((c) => window.__APP.norm(c[0])), parity);
  parity.forEach((c, i) => { if (got[i] !== c[1]) fail(f, `norm() differs from Python for "${c[0]}": "${got[i]}" vs "${c[1]}"`); });
  const arHome = await P.page.evaluate(() => document.getElementById('arBtn').hidden);
  if (!arHome) fail(f, 'Arabic help switch shows on Home (no Arabic there)');

  let pages = 0;
  const small = new Set();
  const heights = {};
  const tall = [];
  const check = async (label, h) => {
    pages++;
    const o = await overflow(P.page);
    if (o > 1) fail(f, `horizontal scroll ${o}px at 390px on ${label}`);
    for (const b of await leftovers(P.page)) fail(f, `leftover markup on ${label}: ${b}`);
    for (const s of await smallTargets(P.page)) small.add(`${label}: ${s}`);
    if (h) {
      const H = await height(P.page);
      heights[h] = H;
      if (H > 844 * 3.2 && !/\/words$|^#\/verbs$|^#\/mistakes$/.test(h)) tall.push(`${h} ${H}px`);
    }
  };
  await check('home', '#/');
  for (const u of data.units) {
    await go(P.page, `#/u/${u.n}`);
    await check(`unit ${u.n}`, `#/u/${u.n}`);
    for (const s of data.sections) {
      if (s === 'puzzles' && !u.puzzles.length) continue;
      await go(P.page, `#/u/${u.n}/${s}`);
      const txt = await P.page.evaluate(() => document.getElementById('main').innerText.length);
      if (txt < 80) fail(f, `unit ${u.n} section ${s} looks empty`);
      await check(`unit ${u.n} ${s}`, `#/u/${u.n}/${s}`);
    }
    for (const g of u.grammar) { await go(P.page, `#/u/${u.n}/grammar/${g}`); await check(`unit ${u.n} grammar ${g}`, `#/u/${u.n}/grammar/${g}`); }
    for (const g of u.games.concat(['cls'])) {
      await go(P.page, `#/u/${u.n}/games/${g}`);
      await P.page.waitForTimeout(40);
      await P.page.evaluate(() => { const b = document.querySelector('#main .gopts .opt, #main .mcard, #main .key, #main .tile, #main .fall-tile'); if (b) b.click(); });
      await P.page.waitForTimeout(40);
      await check(`unit ${u.n} game ${g}`, `#/u/${u.n}/games/${g}`);
    }
    for (const p of u.puzzles) { await go(P.page, `#/u/${u.n}/puzzles/${p}`); await check(`unit ${u.n} puzzle ${p}`, `#/u/${u.n}/puzzles/${p}`); }
  }
  // every set opens in the player
  let played = 0;
  for (const [sid, info] of data.sets) {
    await go(P.page, `#/u/${info.unit}/${info.sec}/play/${info.i}`);
    const ok = await P.page.evaluate((s) => !!document.querySelector(`.player[data-set="${s}"] .pl-stage`), sid);
    if (!ok) { fail(f, `set ${sid} does not open in the player`); continue; }
    played++;
    if (played % 7 === 1) await check(`player ${sid}`, `#/u/${info.unit}/${info.sec}/play/${info.i}`);
  }
  for (const h of ['#/pile', '#/mistakes', '#/review', '#/review/go', '#/review/boss', '#/progress', '#/smarter', '#/resources', '#/classroom', '#/grammar'].concat(data.verbs ? ['#/verbs'] : []).concat(data.smarter.map((s) => '#/smarter/' + s))) {
    await go(P.page, h);
    await check(h, h);
  }

  // scoring through the player: one wrong answer per set (answer index 1), one set of each kind per section of unit 1
  const sc = await P.page.evaluate(() => {
    const A = window.__APP, res = [], seen = {};
    for (const sid of A.sets()) {
      const info = A.setInfo(sid);
      if (info.unit !== A.data.units[0].n || seen[info.sec + info.k]) continue;
      seen[info.sec + info.k] = 1;
      res.push(Object.assign({ sid, k: info.k }, A.playSet(sid, [info.n > 1 ? 1 : 0])));
    }
    return res;
  });
  if (sc.length < 6) fail(f, `scoring check covered only ${sc.length} sets`);
  for (const r of sc) {
    if (!r.finished) fail(f, `set ${r.sid} (${r.k}) did not finish in the player`);
    else if (Math.abs(r.score - (r.n - 1)) > 0.001) fail(f, `set ${r.sid} (${r.k}): expected ${r.n - 1}/${r.n}, got ${r.score}`);
    if (!r.saved || !r.saved.done) fail(f, `set ${r.sid}: score not saved`);
  }
  // end screen: "Practise my mistakes"
  const endS = await P.page.evaluate(() => Array.from(document.querySelectorAll('#main .pl-end button')).map((b) => b.innerText.trim()));
  if (!endS.some((t) => /Practise my mistakes/.test(t))) fail(f, `end screen has no "Practise my mistakes" (${endS.join(' | ')})`);
  // one question per screen + sticky Check + feedback sheet (first grammar practice set)
  const flow = await P.page.evaluate(async () => {
    const A = window.__APP, u = A.data.units[0];
    A.go(`#/u/${u.n}/gpractice/play/0`);
    const items = document.querySelectorAll('#main .pl-stage .item').length;
    const btn = document.querySelector('#main .pl-bar .btn.primary');
    const before = btn.disabled;
    const opt = document.querySelector('#main .pl-stage .opt');
    const inp = document.querySelector('#main .pl-stage .inp');
    if (opt) opt.click(); else if (inp) { inp.value = 'zzz'; inp.dispatchEvent(new Event('input', { bubbles: true })); }
    await new Promise((r) => setTimeout(r, 20));
    const after = btn.disabled;
    btn.click();
    await new Promise((r) => setTimeout(r, 20));
    const sheet = document.querySelector('#main .sheet.on');
    return { items, before, after, sheet: sheet ? sheet.className : null };
  });
  if (flow.items !== 1) fail(f, `player shows ${flow.items} questions at once`);
  if (!flow.before || flow.after) fail(f, `Check bar not enabled by answering (${JSON.stringify(flow)})`);
  if (!flow.sheet) fail(f, 'no feedback sheet after Check');
  // unit test in the test player: all right but two
  await go(P.page, `#/u/${data.units[0].n}/test/go`);
  const tr = await P.page.evaluate(() => {
    const A = window.__APP, ids = A.testBox();
    ids.forEach((_, k) => A.testAnswer(k, k > 1));
    const strip = document.querySelectorAll('#main .qstrip button').length;
    return { n: ids.length, strip, head: A.testFinish(), wrongList: document.querySelectorAll('#test-results .result-list li').length };
  });
  if (tr.n !== 25) fail(f, `unit test has ${tr.n} items`);
  if (tr.strip !== tr.n) fail(f, `question strip has ${tr.strip} numbers`);
  if (!tr.head || !tr.head.startsWith(`Your score: ${tr.n - 2} / ${tr.n}`)) fail(f, `unit test scoring wrong: ${tr.head}`);
  if (tr.wrongList !== 2) fail(f, `test results list ${tr.wrongList} wrong items (expected 2)`);

  // B1: a fix-the-mistake item accepts the full corrected sentence
  const b1 = await P.page.evaluate(() => {
    const A = window.__APP, fx = A.fixItem();
    if (!fx) return 'no fix item';
    A.mount(fx.id);
    return Object.assign({ full: fx.full }, A.answerText(fx.id, fx.full));
  });
  if (typeof b1 === 'string' || !b1.done || b1.score !== 1) fail(f, `B1 full corrected sentence not accepted: ${JSON.stringify(b1)}`);
  // B4: each wrong attempt is recorded once
  const b4 = await P.page.evaluate(() => {
    const A = window.__APP, tid = A.findItem('typed');
    if (!tid) return 'no typed item';
    A.mount(tid); A.answer(tid, false); const one = A.attempts(tid); A.answer(tid, false); const two = A.attempts(tid);
    return { one: one && one.w, two: two && two.w };
  });
  if (typeof b4 === 'string') notes.push(`note [browser] ${name}: B4 check skipped (${b4})`);
  else if (b4.one !== 1 || b4.two !== 2) fail(f, `B4 wrong attempts counted ${b4.one} then ${b4.two} (expected 1 then 2)`);
  // B3: a word with no question can still leave the Review Pile
  const b3 = await P.page.evaluate(() => {
    const A = window.__APP, u = A.data.units[0];
    const missing = [];
    A.data.units.forEach((uu) => uu.words.forEach((w) => { if (!w.qid) missing.push(w.w); }));
    const w = u.words[0], saved = w.qid;
    w.qid = null;
    const keep = A.pileKeys().map((k) => [k, A.state().pile[k]]);
    keep.forEach((k) => A.setPile(k[0]));
    A.setPile('w:' + w.id, 0);
    A.go('#/pile');
    const btn = Array.from(document.querySelectorAll('#main button')).find((b) => b.innerText.includes('I know it now'));
    if (btn) btn.click();
    const left = A.pileKeys().includes('w:' + w.id);
    w.qid = saved;
    keep.forEach((k) => A.setPile(k[0], k[1]));
    const dead = A.pileKeys().filter((k) => !A.pilePrompt(k));
    return { missing, clicked: !!btn, left, dead };
  });
  if (b3.missing.length) fail(f, `B3 words without a question: ${b3.missing.slice(0, 5).join(', ')}`);
  if (!b3.clicked || b3.left) fail(f, 'B3 a word with no question could not be removed from the pile');
  if (b3.dead.length) fail(f, `B3 pile keys that can never be cleared: ${b3.dead.slice(0, 3).join(', ')}`);
  // English first, Arabic on a toggle
  const g0 = data.units[0];
  await go(P.page, `#/u/${g0.n}/grammar/${g0.grammar[0]}`);
  const ar = await P.page.evaluate(() => {
    const vis = () => Array.from(document.querySelectorAll('#main .arbox')).map((b) => b.offsetParent !== null);
    const en = document.querySelectorAll('#main .enbox .enlines li').length;
    const first = vis();
    const pill = document.querySelector('#main .arpill');
    pill.click();
    const afterPill = vis();
    const pressed = pill.getAttribute('aria-pressed');
    pill.click();
    const sw = document.getElementById('arBtn');
    const swShown = !sw.hidden;
    sw.click();
    return { en, first, afterPill, pressed, swShown, all: vis(), state: window.__APP.state().arHelp };
  });
  if (!ar.en) fail(f, 'grammar card has no "In simple words" lines');
  if (ar.first.some(Boolean)) fail(f, 'Arabic is open by default');
  if (!ar.afterPill[0] || ar.pressed !== 'true') fail(f, 'the عربي pill does not open the Arabic');
  if (!ar.swShown) fail(f, 'Arabic help switch hidden on a page with Arabic');
  if (!ar.all.every(Boolean) || ar.state !== true) fail(f, 'Arabic help switch does not open all Arabic / not saved');

  // progress survives a reload
  const before = await P.page.evaluate(() => { const s = window.__APP.state(); return { sets: Object.keys(s.sets).length, test: s.tests }; });
  await P.page.waitForTimeout(250);
  await P.page.reload();
  await P.page.waitForFunction(() => window.__APP);
  const after = await P.page.evaluate(() => { const s = window.__APP.state(); return { sets: Object.keys(s.sets).length, test: s.tests, ar: s.arHelp, open: Array.from(document.querySelectorAll('#main .arbox')).every((b) => b.offsetParent !== null) }; });
  if (!before.sets || after.sets !== before.sets) fail(f, `progress lost on reload (${before.sets} sets before, ${after.sets} after)`);
  if (JSON.stringify(after.test) !== JSON.stringify(before.test)) fail(f, 'unit test score lost on reload');
  if (after.ar !== true || !after.open) fail(f, 'Arabic help setting lost on reload');
  if (P.errors.length) fail(f, `console errors at 390px: ${P.errors.slice(0, 3).join(' | ')}`);
  if (P.external.length) fail(f, `network requests: ${P.external.slice(0, 3).join(', ')}`);
  if (small.size) fail(f, `${small.size} tap targets under 44px, e.g. ${[...small].slice(0, 12).join('; ')}`);
  if (tall.length) fail(f, `pages taller than about 3 screens: ${tall.slice(0, 8).join(', ')}`);
  fs.mkdirSync(path.join(root, 'build'), { recursive: true });
  fs.writeFileSync(path.join(root, 'build', `heights-${code}.json`), JSON.stringify(heights, null, 1));
  await P.ctx.close();

  // ---------------- v1 saved progress still loads (migration to v2, same key)
  const fx = path.join(root, 'tests', 'fixtures', `v1-state-${code}.json`);
  let migrated = 'no fixture';
  if (fs.existsSync(fx)) {
    const raw = fs.readFileSync(fx, 'utf8');
    const v1 = JSON.parse(raw);
    const M = await newPage({ width: 390, height: 844 }, { seed: { key: data.key, value: raw } });
    await M.page.goto(fileUrl);
    await M.page.waitForFunction(() => window.__APP);
    const m = await M.page.evaluate(() => window.__APP.state());
    if (m.v !== 2) fail(f, `v1 state not migrated (v=${m.v})`);
    for (const k of ['items', 'words', 'sets', 'tests', 'cando', 'drafts', 'pile']) {
      const a = Object.keys(v1[k] || {}).length, b = Object.keys(m[k] || {}).length;
      if (b < a) fail(f, `v1 migration lost ${k}: ${a} → ${b}`);
    }
    if (m.mistakes.length < (v1.mistakes || []).length) fail(f, 'v1 migration lost mistakes');
    for (const h of ['#/', '#/progress', '#/pile', '#/mistakes']) await go(M.page, h);
    if (M.errors.length) fail(f, `errors after loading v1 progress: ${M.errors.slice(0, 3).join(' | ')}`);
    migrated = `${Object.keys(m.items).length} items, ${Object.keys(m.sets).length} sets, ${Object.keys(m.words).length} words kept`;
    await M.ctx.close();
  }

  // ---------------- storage blocked
  const B = await newPage({ width: 390, height: 844 }, { blockStorage: true });
  await B.page.goto(fileUrl);
  await B.page.waitForFunction(() => window.__APP);
  await B.page.evaluate(() => { const A = window.__APP; A.playSet(A.sets()[0], []); A.go('#/'); });
  if (B.errors.length) fail(f, `errors with storage blocked: ${B.errors.slice(0, 3).join(' | ')}`);
  await B.ctx.close();

  // ---------------- B8 + B9: finish a real game (Escape) with a fake clock
  const u1 = data.units[0];
  const G = await newPage({ width: 390, height: 844 }, { clock: true });
  await G.page.goto(fileUrl);
  await G.page.waitForFunction(() => window.__APP);
  await go(G.page, `#/u/${u1.n}/games/escape`);
  const clickRight = () => G.page.evaluate(() => {
    const A = window.__APP, q = document.querySelector('#main .gq');
    if (!q) return 'none';
    const b = q.querySelectorAll('.gopts .opt')[A.itemData(q.getAttribute('data-id')).a];
    if (b && !b.disabled) b.click();
    return 'q';
  });
  await clickRight();
  const early = await G.page.evaluate((n) => !!window.__APP.state().secs[n + ':games'], u1.n);
  if (early) fail(f, 'B8 Games marked done before any game reached its end screen');
  await G.ctx.clock.runFor(1500);
  for (let k = 0; k < 40; k++) { if (await clickRight() === 'none') break; await G.ctx.clock.runFor(700); }
  const g8 = await G.page.evaluate((n) => { const s = window.__APP.state(); return { done: !!s.secs[n + ':games'], best: s.games['u' + n + ':escape'] }; }, u1.n);
  if (!g8.done) fail(f, 'B8 Games not marked done after finishing Escape');
  if (!g8.best || g8.best.w !== 0) fail(f, `B9 Escape best should be {w:0}, got ${JSON.stringify(g8.best)}`);
  await go(G.page, `#/u/${u1.n}/games`);
  const badge = await G.page.evaluate(() => document.getElementById('main').innerText);
  if (!badge.includes('✓ Escaped')) fail(f, 'B9 games list does not show "✓ Escaped"');
  if (G.errors.length) fail(f, `console errors in the game run: ${G.errors.slice(0, 3).join(' | ')}`);
  await G.ctx.close();

  // ---------------- 360 px: no horizontal scroll; B7 Falling Words tiles never overlap
  const N = await newPage({ width: 360, height: 740 }, { clock: true });
  await N.page.goto(fileUrl);
  await N.page.waitForFunction(() => window.__APP);
  let fallChecks = 0, n360 = 0;
  const o360 = async (label) => { n360++; const o = await overflow(N.page); if (o > 1) fail(f, `horizontal scroll ${o}px at 360px on ${label}`); };
  await o360('home');
  for (const u of data.units) {
    for (const s of [''].concat(data.sections.filter((x) => x !== 'puzzles' || u.puzzles.length).map((x) => '/' + x))) {
      await go(N.page, `#/u/${u.n}${s}`);
      await o360(`unit ${u.n}${s}`);
    }
    for (const g of u.grammar) { await go(N.page, `#/u/${u.n}/grammar/${g}`); await o360(`grammar ${g}`); }
    for (const g of u.games) { await go(N.page, `#/u/${u.n}/games/${g}`); await o360(`game ${g}`); }
    for (const p of u.puzzles) { await go(N.page, `#/u/${u.n}/puzzles/${p}`); await o360(`puzzle ${p}`); }
    if (!u.games.includes('falling')) continue;
    await go(N.page, `#/u/${u.n}/games/falling`);
    for (let r = 0; r < 4; r++) {
      for (const t of [100, 2500]) {
        await N.ctx.clock.runFor(t);
        const bad = await N.page.evaluate(() => {
          const st = document.querySelector('#main .fall-stage');
          if (!st) return null;
          const S = st.getBoundingClientRect();
          const R = Array.from(st.querySelectorAll('.fall-tile')).map((b) => b.getBoundingClientRect());
          const out = [];
          R.forEach((a, i) => {
            if (a.left < S.left - 0.5 || a.right > S.right + 0.5) out.push('tile ' + i + ' outside the stage');
            R.forEach((b, j) => { if (j > i && a.left < b.right - 0.5 && b.left < a.right - 0.5 && a.top < b.bottom - 0.5 && b.top < a.bottom - 0.5) out.push('tiles ' + i + ' and ' + j + ' overlap'); });
          });
          return out;
        });
        if (bad === null) break;
        fallChecks++;
        if (bad.length) { fail(f, `B7 Falling Words at 360px, unit ${u.n}: ${bad.join(', ')}`); break; }
      }
      await N.page.evaluate(() => { const b = document.querySelector('#main .fall-tile'); if (b) b.click(); });
      await N.ctx.clock.runFor(1000);
    }
  }
  for (const [sid, info] of data.sets.filter((_, i) => i % 5 === 0)) { await go(N.page, `#/u/${info.unit}/${info.sec}/play/${info.i}`); await o360(`player ${sid}`); }
  if (N.errors.length) fail(f, `console errors at 360px: ${N.errors.slice(0, 3).join(' | ')}`);
  await N.ctx.close();

  // ---------------- projector, class mode
  const Q = await newPage({ width: 1920, height: 1080 });
  await Q.page.goto(fileUrl);
  await Q.page.waitForFunction(() => window.__APP);
  await Q.page.click('#classBtn');
  const zoom = await Q.page.evaluate(() => getComputedStyle(document.body).zoom);
  if (String(zoom) !== '1.75') fail(f, `class mode zoom at 1920px is ${zoom}, expected 1.75`);
  let qpages = 0;
  for (const u of data.units) {
    for (const s of [''].concat(data.sections.filter((x) => x !== 'puzzles' || u.puzzles.length).map((x) => '/' + x))) {
      await go(Q.page, `#/u/${u.n}${s}`);
      qpages++;
      const o = await overflow(Q.page);
      if (o > 1) fail(f, `horizontal scroll ${o}px in class mode on unit ${u.n}${s}`);
    }
    for (const g of u.games) {
      await go(Q.page, `#/u/${u.n}/games/${g}`);
      qpages++;
      const o = await overflow(Q.page);
      if (o > 1) fail(f, `horizontal scroll in class mode on game ${g}`);
      const tb = await Q.page.evaluate(() => !!document.querySelector('.teacher-bar') || !!document.querySelector('.teams'));
      if (!tb) fail(f, `team mode not on by default in class mode (game ${g})`);
    }
    for (const p of u.puzzles) { await go(Q.page, `#/u/${u.n}/puzzles/${p}`); qpages++; const o = await overflow(Q.page); if (o > 1) fail(f, `horizontal scroll in class mode on puzzle ${p}`); }
  }
  // Reveal answer: only the current question
  await go(Q.page, `#/u/${u1.n}/gpractice/play/0`);
  const rv = await Q.page.evaluate(() => {
    const btn = document.querySelector('#main .reveal-btn');
    if (!btn || btn.offsetParent === null) return 'no visible Reveal answer button in class mode';
    const sid = document.querySelector('#main .player').getAttribute('data-set');
    btn.click();
    const s = window.__APP.setScore(sid);
    return { sheets: document.querySelectorAll('#main .sheet.on').length, made: s.n, done: window.__APP.setScore(sid) && document.querySelectorAll('#main .pl-stage .item').length };
  });
  if (typeof rv === 'string') fail(f, rv);
  else if (rv.sheets !== 1 || rv.made !== 1) fail(f, `Reveal answer should show exactly one answer (${JSON.stringify(rv)})`);
  if (Q.errors.length) fail(f, `console errors in class mode: ${Q.errors.slice(0, 3).join(' | ')}`);
  await Q.ctx.close();
  notes.push(`ok  [browser] ${name}: ${pages} views at 390×844 (${played} sets opened in the player), ${n360} views at 360×740, ${qpages} views at 1920×1080 class mode (zoom ${zoom}); parity ${parity.length}; scoring on ${sc.length} sets + unit test; B1 ${JSON.stringify(b1.full)}; B3 pile; B4 single count; B7 ${fallChecks} Falling Words frames; B8/B9 Escape finished; Arabic toggle; reload kept ${after.sets} set scores; v1 progress: ${migrated}; storage-blocked run clean`);
}
await browser.close();
for (const n of notes) console.log(n);
for (const x of fails) console.log(x);
console.log(fails.length ? `browser smoke test: ${fails.length} problems` : 'browser smoke test: passed');
process.exit(fails.length ? 1 : 0);
