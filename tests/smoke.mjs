// Browser smoke test for the built apps. Run by build.py:  node tests/smoke.mjs "dist/A1.1 Practice.html" ...
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
const parity = JSON.parse(fs.readFileSync(path.join(here, '..', 'build', 'parity.json'), 'utf8'));
const files = process.argv.slice(2);
const fails = [];
const notes = [];
function fail(f, msg) { fails.push(`FAIL [browser] ${path.basename(f)}: ${msg}`); }

const exe = fs.existsSync('/opt/pw-browsers/chromium') ? undefined : undefined;
const browser = await chromium.launch(exe ? { executablePath: exe } : {});

async function newPage(viewport, opts = {}) {
  const ctx = await browser.newContext({ viewport, deviceScaleFactor: 1, hasTouch: viewport.width < 600 });
  if (opts.blockStorage) {
    await ctx.addInitScript(() => {
      const thrower = () => { throw new Error('storage blocked'); };
      Object.defineProperty(window, 'localStorage', { get: thrower, configurable: true });
    });
  }
  const page = await ctx.newPage();
  const errors = [];
  const external = [];
  page.on('console', (m) => { if (m.type() === 'error') errors.push(m.text()); });
  page.on('pageerror', (e) => errors.push(String(e)));
  page.on('request', (r) => { const u = r.url(); if (!u.startsWith('file:') && !u.startsWith('data:') && !u.startsWith('about:')) external.push(u); });
  return { ctx, page, errors, external };
}

async function overflow(page) {
  return page.evaluate(() => {
    const de = document.documentElement;
    return de.scrollWidth - de.clientWidth;
  });
}
async function leftovers(page) {
  return page.evaluate(() => {
    const t = document.getElementById('main').innerText;
    const bad = [];
    for (const [re, why] of [[/\{|\}/, 'curly brace'], [/\*\*/, '**'], [/___/, '___'], [/\bundefined\b/, 'undefined'], [/\bNaN\b/, 'NaN'], [/\[object/, '[object'], [/&amp;|&lt;|&gt;|&#\d+;/, 'HTML entity']]) {
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

for (const f of files) {
  const fileUrl = url.pathToFileURL(path.resolve(f)).href;
  const name = path.basename(f);
  // ---------------- phone
  const P = await newPage({ width: 375, height: 812 });
  await P.page.goto(fileUrl);
  await P.page.waitForFunction(() => window.__APP);
  const data = await P.page.evaluate(() => ({ units: window.__APP.data.units.map((u) => ({ n: u.n, games: u.games.list, grammar: u.grammar.map((g) => g.id) })), sections: window.__APP.sections, verbs: window.__APP.data.verbs.length, smarter: window.__APP.data.smarter.map((s) => s.id) }));
  // normaliser parity with Python
  const got = await P.page.evaluate((cases) => cases.map((c) => window.__APP.norm(c[0])), parity);
  parity.forEach((c, i) => { if (got[i] !== c[1]) fail(f, `norm() differs from Python for "${c[0]}": "${got[i]}" vs "${c[1]}"`); });

  let pages = 0;
  const small = new Set();
  const check = async (label) => {
    pages++;
    const o = await overflow(P.page);
    if (o > 1) fail(f, `horizontal scroll ${o}px at 375px on ${label}`);
    for (const b of await leftovers(P.page)) fail(f, `leftover markup on ${label}: ${b}`);
    for (const s of await smallTargets(P.page)) small.add(`${label}: ${s}`);
  };
  await check('home');
  for (const u of data.units) {
    await P.page.evaluate((h) => window.__APP.go(h), `#/u/${u.n}`);
    await check(`unit ${u.n}`);
    for (const s of data.sections) {
      await P.page.evaluate((h) => window.__APP.go(h), `#/u/${u.n}/${s}`);
      if (s === 'grammar') await P.page.evaluate(() => window.__APP.openAllGrammar());
      const txt = await P.page.evaluate(() => document.getElementById('main').innerText.length);
      if (txt < 80) fail(f, `unit ${u.n} section ${s} looks empty`);
      await check(`unit ${u.n} ${s}`);
    }
    for (const g of u.games.concat(['cls'])) {
      await P.page.evaluate((h) => window.__APP.go(h), `#/u/${u.n}/games/${g}`);
      await P.page.waitForTimeout(60);
      // play one move
      await P.page.evaluate(() => { const b = document.querySelector('#main .gopts .opt, #main .mcard, #main .key, #main .tile, #main .fall-tile'); if (b) b.click(); });
      await P.page.waitForTimeout(60);
      await check(`unit ${u.n} game ${g}`);
    }
  }
  for (const h of ['#/pile', '#/mistakes', '#/review', '#/review/boss', '#/progress', '#/smarter', '#/resources', '#/classroom', '#/grammar'].concat(data.verbs ? ['#/verbs'] : []).concat(data.smarter.map((s) => '#/smarter/' + s))) {
    await P.page.evaluate((x) => window.__APP.go(x), h);
    await check(h);
  }

  // scoring through the test hook: first grammar set of unit 1
  const u1 = data.units[0];
  await P.page.evaluate((h) => window.__APP.go(h), `#/u/${u1.n}/grammar`);
  await P.page.evaluate(() => window.__APP.openAllGrammar());
  const sc = await P.page.evaluate(() => {
    const A = window.__APP;
    const sets = A.sets().filter((s) => !s.includes('.q.'));
    const res = [];
    for (const sid of sets.slice(0, 6)) {
      const ids = Array.from(document.querySelectorAll(`[data-set="${sid}"] .item[data-id]`)).map((n) => n.getAttribute('data-id'));
      const boardIds = ids.length ? ids : A.items().filter((i) => document.querySelector(`[data-set="${sid}"]`) && false);
      if (!ids.length) continue;
      ids.forEach((id, k) => {
        if (k === 1) { let guard = 0; while (!A.item(id).done && guard++ < 5) A.answer(id, false); }
        else A.answer(id, true);
      });
      res.push({ sid, n: ids.length, s: A.setScore(sid), second: A.item(ids[1]) });
    }
    return res;
  });
  if (!sc.length) fail(f, 'scoring check found no sets');
  for (const r of sc) {
    if (!r.s || !r.s.finished) fail(f, `set ${r.sid} did not finish after answering every item`);
    else if (Math.abs(r.s.score - (r.n - 1)) > 0.001) fail(f, `set ${r.sid}: expected score ${r.n - 1}/${r.n}, got ${r.s.score}`);
    if (r.second && r.second.score !== 0) fail(f, `set ${r.sid}: wrong item scored ${r.second.score}`);
  }
  // board sets (match / sort / bank) in word practice
  await P.page.evaluate((h) => window.__APP.go(h), `#/u/${u1.n}/practice`);
  const bd = await P.page.evaluate(() => {
    const A = window.__APP, out = [];
    for (const sid of A.sets()) {
      const S = window.__APP.setScore(sid);
      const ids = A.items().filter((i) => document.querySelector(`[data-set="${sid}"]`));
      out.push(sid);
    }
    return out.length;
  });
  if (!bd) fail(f, 'no word practice sets rendered');
  // unit test: answer all right except two, finish
  await P.page.evaluate((h) => window.__APP.go(h), `#/u/${u1.n}/test`);
  const tr = await P.page.evaluate(() => {
    const A = window.__APP;
    const ids = Array.from(document.querySelectorAll('#main .item[data-id]')).map((n) => n.getAttribute('data-id'));
    ids.forEach((id, k) => A.answer(id, k > 1));
    document.querySelector('#main .btn.coral.block').click();
    document.querySelector('#main .btn.coral.block') && document.querySelector('#main .btn.coral.block').click();
    const h = document.querySelector('#test-results h2');
    return { n: ids.length, head: h ? h.innerText : null };
  });
  if (tr.n !== 25) fail(f, `unit test shows ${tr.n} items`);
  if (!tr.head || !tr.head.startsWith(`Your score: ${tr.n - 2} / ${tr.n}`)) fail(f, `unit test scoring wrong: ${tr.head}`);
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
    const A = window.__APP;
    const tid = A.findItem('typed');
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
  // progress survives a reload
  const before = await P.page.evaluate(() => { const s = window.__APP.state(); return { sets: Object.keys(s.sets).length, test: s.tests }; });
  await P.page.waitForTimeout(250);
  await P.page.reload();
  await P.page.waitForFunction(() => window.__APP);
  const after = await P.page.evaluate(() => { const s = window.__APP.state(); return { sets: Object.keys(s.sets).length, test: s.tests }; });
  if (!before.sets || after.sets !== before.sets) fail(f, `progress lost on reload (${before.sets} sets before, ${after.sets} after)`);
  if (JSON.stringify(after.test) !== JSON.stringify(before.test)) fail(f, 'unit test score lost on reload');
  if (P.errors.length) fail(f, `console errors at 375px: ${P.errors.slice(0, 3).join(' | ')}`);
  if (P.external.length) fail(f, `network requests: ${P.external.slice(0, 3).join(', ')}`);
  if (small.size) fail(f, `${small.size} tap targets under 44px, e.g. ${[...small].slice(0, 12).join('; ')}`);
  await P.ctx.close();

  // ---------------- B8 + B9: finish a real game (Escape) with a fake clock
  const G = await newPage({ width: 390, height: 844 });
  await G.ctx.clock.install();
  await G.page.goto(fileUrl);
  await G.page.waitForFunction(() => window.__APP);
  await G.page.evaluate((h) => window.__APP.go(h), `#/u/${u1.n}/games/escape`);
  await G.page.evaluate(() => { const q = document.querySelector('#main .gq'); const b = q && q.querySelectorAll('.gopts .opt')[window.__APP.itemData(q.getAttribute('data-id')).a]; if (b) b.click(); });
  const early = await G.page.evaluate((n) => !!window.__APP.state().secs[n + ':games'], u1.n);
  if (early) fail(f, 'B8 Games marked done before any game reached its end screen');
  await G.ctx.clock.runFor(1500);
  for (let k = 0; k < 40; k++) {
    const st = await G.page.evaluate(() => {
      const A = window.__APP, q = document.querySelector('#main .gq');
      if (!q) return 'none';
      const it = A.itemData(q.getAttribute('data-id'));
      const b = q.querySelectorAll('.gopts .opt')[it.a];
      if (b && !b.disabled) b.click();
      return 'q';
    });
    if (st === 'none') break;
    await G.ctx.clock.runFor(700);
  }
  const g8 = await G.page.evaluate((n) => { const s = window.__APP.state(); return { done: !!s.secs[n + ':games'], best: s.games['u' + n + ':escape'] }; }, u1.n);
  if (!g8.done) fail(f, 'B8 Games not marked done after finishing Escape');
  if (!g8.best || g8.best.w !== 0) fail(f, `B9 Escape best should be {w:0}, got ${JSON.stringify(g8.best)}`);
  await G.page.evaluate((h) => window.__APP.go(h), `#/u/${u1.n}/games`);
  const badge = await G.page.evaluate(() => document.getElementById('main').innerText);
  if (!badge.includes('✓ Escaped')) fail(f, 'B9 games list does not show "✓ Escaped"');
  if (G.errors.length) fail(f, `console errors in the game run: ${G.errors.slice(0, 3).join(' | ')}`);
  await G.ctx.close();

  // ---------------- 360 px: no horizontal scroll on main routes; B7 Falling Words tiles never overlap
  const N = await newPage({ width: 360, height: 740 });
  await N.ctx.clock.install();
  await N.page.goto(fileUrl);
  await N.page.waitForFunction(() => window.__APP);
  let fallChecks = 0;
  for (const u of data.units) {
    for (const s of [''].concat(data.sections.map((x) => '/' + x))) {
      await N.page.evaluate((h) => window.__APP.go(h), `#/u/${u.n}${s}`);
      const o = await overflow(N.page);
      if (o > 1) fail(f, `horizontal scroll ${o}px at 360px on unit ${u.n}${s}`);
    }
    if (!u.games.includes('falling')) continue;
    await N.page.evaluate((h) => window.__APP.go(h), `#/u/${u.n}/games/falling`);
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
  if (N.errors.length) fail(f, `console errors at 360px: ${N.errors.slice(0, 3).join(' | ')}`);
  await N.ctx.close();
  notes.push(`ok  [browser] ${name}: B1 full sentence ${JSON.stringify(b1.full)}, B3 pile, B4 single count, B8/B9 Escape finished, B7 ${fallChecks} Falling Words frames at 360px`);

  // ---------------- storage blocked
  const B = await newPage({ width: 375, height: 812 }, { blockStorage: true });
  await B.page.goto(fileUrl);
  await B.page.waitForFunction(() => window.__APP);
  await B.page.evaluate((h) => window.__APP.go(h), `#/u/${u1.n}/grammar`);
  await B.page.evaluate(() => { const A = window.__APP; A.openAllGrammar(); const id = document.querySelector('#main .item[data-id]').getAttribute('data-id'); A.answer(id, true); });
  await B.page.evaluate((h) => window.__APP.go(h), '#/');
  if (B.errors.length) fail(f, `errors with storage blocked: ${B.errors.slice(0, 3).join(' | ')}`);
  await B.ctx.close();

  // ---------------- projector, class mode
  const Q = await newPage({ width: 1920, height: 1080 });
  await Q.page.goto(fileUrl);
  await Q.page.waitForFunction(() => window.__APP);
  await Q.page.click('#classBtn');
  const zoom = await Q.page.evaluate(() => getComputedStyle(document.body).zoom);
  if (String(zoom) !== '1.75') fail(f, `class mode zoom at 1920px is ${zoom}, expected 1.75`);
  let qpages = 0;
  for (const u of data.units) {
    for (const s of [''].concat(data.sections.map((x) => '/' + x))) {
      await Q.page.evaluate((h) => window.__APP.go(h), `#/u/${u.n}${s}`);
      if (s === '/grammar') await Q.page.evaluate(() => window.__APP.openAllGrammar());
      qpages++;
      const o = await overflow(Q.page);
      if (o > 1) fail(f, `horizontal scroll ${o}px in class mode on unit ${u.n}${s}`);
    }
    for (const g of u.games) {
      await Q.page.evaluate((h) => window.__APP.go(h), `#/u/${u.n}/games/${g}`);
      const o = await overflow(Q.page);
      if (o > 1) fail(f, `horizontal scroll in class mode on game ${g}`);
      const tb = await Q.page.evaluate(() => !!document.querySelector('.teacher-bar') || !!document.querySelector('.teams'));
      if (!tb) fail(f, `team mode not on by default in class mode (game ${g})`);
    }
  }
  // reveal one item per click
  await Q.page.evaluate((h) => window.__APP.go(h), `#/u/${u1.n}/practice`);
  const rv = await Q.page.evaluate(() => {
    const card = document.querySelector('#main .set');
    const sid = card.getAttribute('data-set');
    const btn = Array.from(card.querySelectorAll('button')).find((b) => b.innerText.includes('Reveal next'));
    if (!btn || btn.offsetParent === null) return 'no visible reveal button';
    btn.click();
    const a = window.__APP.setScore(sid);
    const doneItems = Array.from(card.querySelectorAll('.fb')).filter((x) => x.innerText.trim()).length + card.querySelectorAll('.opt.right, .opt.matched, .gapbtn.right').length;
    btn.click();
    return { one: doneItems, sid };
  });
  if (typeof rv === 'string') fail(f, rv);
  if (Q.errors.length) fail(f, `console errors in class mode: ${Q.errors.slice(0, 3).join(' | ')}`);
  await Q.ctx.close();
  notes.push(`ok  [browser] ${name}: ${pages} views at 375×812 + ${qpages} views at 1920×1080 (class mode, zoom ${zoom}), parity ${parity.length} cases, scoring on ${sc.length} sets + unit test, reload kept ${after.sets} set scores, storage-blocked run clean`);
}
await browser.close();
for (const n of notes) console.log(n);
for (const x of fails) console.log(x);
console.log(fails.length ? `browser smoke test: ${fails.length} problems` : 'browser smoke test: passed');
process.exit(fails.length ? 1 : 0);
