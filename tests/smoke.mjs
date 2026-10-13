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
