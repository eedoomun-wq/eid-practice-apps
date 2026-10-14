// Screenshots for REVIEW.md: phone 390×844 (full page) and projector 1920×1080 in Class mode (first screen).
//   node tests/screens.mjs after  "dist/A1.1 Practice.html" [more apps…]   → docs/screens/after/
//   node tests/screens.mjs before old-app.html                               → docs/screens/before/ (1920 class-mode shots)
// Writes <dir>/heights.json with the full page height of every phone screenshot.
import { createRequire } from 'module';
import fs from 'fs';
import path from 'path';
import url from 'url';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
const here = path.dirname(url.fileURLToPath(import.meta.url));
const [mode, ...files] = process.argv.slice(2);
const out = path.join(here, '..', 'docs', 'screens', mode);
fs.mkdirSync(out, { recursive: true });
const hfile = path.join(out, 'heights.json');
const heights = fs.existsSync(hfile) ? JSON.parse(fs.readFileSync(hfile, 'utf8')) : {};

// [name, route, action]; actions run in the page after the route renders
const AFTER = (u) => [
  ['home', '#/'],
  ['unit', `#/u/${u}`],
  ['setlist', `#/u/${u}/gpractice`],
  ['player-question', `#/u/${u}/gpractice/play/0`],
  ['player-checked', `#/u/${u}/gpractice/play/0`, 'check'],
  ['grammar', `#/u/${u}/grammar/g1`],
  ['reading', `#/u/${u}/reading`],
  ['game', `#/u/${u}/games/memory`],
  ['test', `#/u/${u}/test/go`],
  ['puzzle-case', `#/u/${u}/puzzles/case`],
  ['puzzle-words', `#/u/${u}/puzzles/words`],
  ['puzzle-escape', `#/u/${u}/puzzles/escape`],
  ['puzzle-guess', `#/u/${u}/puzzles/guess`]
];
const BEFORE = (u) => [
  ['home', '#/'], ['unit', `#/u/${u}`], ['setlist', `#/u/${u}/practice`], ['grammar', `#/u/${u}/grammar`],
  ['reading', `#/u/${u}/reading`], ['game', `#/u/${u}/games/memory`], ['test', `#/u/${u}/test`]
];

async function act(page, a) {
  if (a !== 'check') return;
  await page.evaluate(() => {
    const A = window.__APP, q = document.querySelector('#main .pl-stage .item');
    const it = A.itemData(q.getAttribute('data-id'));
    const opts = q.querySelectorAll('.opt');
    if (opts.length && it.t === 'choice') opts[it.a].click();
    else { const i = q.querySelector('.inp'); if (i) { i.value = it.acc ? it.acc[0] : ''; i.dispatchEvent(new Event('input', { bubbles: true })); } }
  });
  await page.waitForTimeout(50);
  await page.click('#main .pl-bar .btn.primary');
  await page.waitForTimeout(400);
}

const browser = await chromium.launch();
for (const f of files) {
  const fileUrl = url.pathToFileURL(path.resolve(f)).href;
  const app = path.basename(f).replace(' Practice.html', '').replace('.html', '');
  const first = files.indexOf(f) === 0;
  for (const [vw, vh, cls] of [[390, 844, false], [1920, 1080, true]]) {
    if (mode === 'before' && !cls) continue; // phone "before" shots were taken from the round-1 apps
    if (!first && cls) continue;
    const ctx = await browser.newContext({ viewport: { width: vw, height: vh }, hasTouch: vw < 600 });
    const page = await ctx.newPage();
    await page.goto(fileUrl);
    await page.waitForFunction(() => window.__APP);
    if (cls) await page.click('#classBtn');
    const u = await page.evaluate(() => window.__APP.data.units[0].n);
    const routes = mode === 'before' ? BEFORE(u) : AFTER(u);
    for (const [nm, h, a] of routes) {
      const ok = await page.evaluate((x) => { window.__APP.go(x); return !!document.querySelector('#main .wrap') && location.hash === x; }, h);
      if (!ok && nm.startsWith('puzzle')) continue;
      await page.waitForTimeout(150);
      if (a) await act(page, a);
      const H = await page.evaluate(() => document.documentElement.scrollHeight);
      if (!cls) heights[`${app} ${nm}`] = H;
      if (first) await page.screenshot({ path: path.join(out, `${nm}-${vw}.png`), fullPage: !cls });
    }
    await ctx.close();
  }
}
await browser.close();
fs.writeFileSync(hfile, JSON.stringify(heights, null, 1));
console.log('screens written to', out);
