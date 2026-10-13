/* ===== app.js: router and pages ===== */
var MAIN = document.getElementById('main');
var UNITS = DATA.units;
function unitByN(n) { for (var i = 0; i < UNITS.length; i++) if (UNITS[i].n === n) return UNITS[i]; return null; }

var SECTIONS = [
  { k: 'words', name: 'Words', ic: 'words', c: 'purple' },
  { k: 'practice', name: 'Word practice', ic: 'match', c: 'teal' },
  { k: 'grammar', name: 'Grammar', ic: 'grammar', c: 'purple' },
  { k: 'classroom', name: 'Classroom English', ic: 'classroom', c: 'teal' },
  { k: 'reading', name: 'Reading', ic: 'reading', c: 'teal' },
  { k: 'dialogue', name: 'Dialogue', ic: 'dialogue', c: 'teal' },
  { k: 'wq', name: 'Write the question', ic: 'wq', c: 'teal' },
  { k: 'writing', name: 'Writing', ic: 'writing', c: 'coral' },
  { k: 'games', name: 'Games', ic: 'games', c: 'amber' },
  { k: 'test', name: 'Unit test', ic: 'test', c: 'coral' },
  { k: 'cando', name: 'I can…', ic: 'cando', c: 'purple' }
];
function secByK(k) { for (var i = 0; i < SECTIONS.length; i++) if (SECTIONS[i].k === k) return SECTIONS[i]; return null; }

function unitSets(U, k) {
  switch (k) {
    case 'practice': return U.wsets;
    case 'grammar': var a = []; U.grammar.forEach(function (g) { if (g.quick) a.push(g.quick); a = a.concat(g.sets); }); return a;
    case 'classroom': return U.cls.sets;
    case 'reading': return U.reading.sets;
    case 'dialogue': return U.dialogue.sets;
    case 'wq': return U.wq;
  }
  return [];
}
function setsDone(sets) { return sets.length > 0 && sets.every(function (s) { return S.sets[s.id] && S.sets[s.id].done; }); }
function secDone(U, k) {
  if (k === 'words') return U.words.every(function (w) { return S.words[w.id]; });
  if (k === 'writing') return U.writing.every(function (w) { return wordCount(S.drafts[w.id] || '') >= w.min; });
  if (k === 'games') return !!S.secs[U.n + ':games'];
  if (k === 'test') return S.tests[U.n] !== undefined;
  if (k === 'cando') return U.cando.every(function (_, i) { return S.cando[U.n + ':' + i]; });
  return setsDone(unitSets(U, k));
}
function wordCount(s) { var m = String(s).match(/[A-Za-z0-9À-ɏ']+/g); return m ? m.length : 0; }

/* ---------- shell ---------- */
function page() { stopAllLoops(); REG = {}; SETREG = {}; clear(MAIN); var w = el('div', { 'class': 'wrap' }); MAIN.appendChild(w); return w; }
function crumbs(w, parts) {
  var c = el('nav', { 'class': 'crumb', 'aria-label': 'Back' });
  parts.forEach(function (p) { c.appendChild(el('button', { 'class': 'btn small ghost', type: 'button', onclick: function () { go(p[1]); } }, p[1] === '#/' ? icon('home', 18) : icon('back', 18), p[0])); });
  w.appendChild(c);
}
function secHead(w, title, color, iconName, sub) {
  var h = el('div', { 'class': 'sec-head ' + color }, el('div', { 'class': 'row' }, icon(iconName, 28, INK[color] || INK.teal), el('h1', null, title)));
  if (sub) h.appendChild(el('p', { 'class': 'sec', style: 'margin:6px 0 0' }, sub));
  w.appendChild(h);
}
function go(h) { if (location.hash === h) render(); else location.hash = h; }

function applyClassMode() {
  document.body.classList.toggle('class-mode', !!S.classMode);
  var b = document.getElementById('classBtn');
  b.setAttribute('aria-pressed', String(!!S.classMode));
  b.textContent = S.classMode ? 'Class mode: on' : 'Class mode';
}
document.getElementById('classBtn').addEventListener('click', function () { S.classMode = !S.classMode; save(); applyClassMode(); });
document.getElementById('homeBtn').addEventListener('click', function () { go('#/'); });

/* ---------- home ---------- */
function unitStars(n) { var p = S.tests[n]; return p === undefined ? 0 : starsFor(p); }
function starsText(k) { return '★★★'.slice(0, k) + '☆☆☆'.slice(0, 3 - k); }
function pageHome() {
  var w = page();
  var hero = el('div', { 'class': 'hero' },
    el('h1', null, DATA.title),
    el('p', { 'class': 'sec' }, DATA.book + ' · ' + DATA.unitsLabel),
    el('div', { 'class': 'row' },
      el('span', { 'class': 'streak', title: 'Days in a row' }, icon('flame', 20, '#8A5300'), streakNow() + (streakNow() === 1 ? ' day' : ' days')),
      S.last ? el('button', { 'class': 'btn', type: 'button', onclick: function () { go(S.last); } }, 'Continue where I stopped', icon('next', 18)) : el('button', { 'class': 'btn', type: 'button', onclick: function () { go('#/u/' + UNITS[0].n); } }, 'Start Unit ' + UNITS[0].n, icon('next', 18))));
  if (!STORE_OK) hero.appendChild(el('p', { 'class': 'small-t sec mt8' }, 'Your browser is not saving progress here. Everything still works, but your stars will reset when you close the page.'));
  w.appendChild(hero);
  w.appendChild(el('h2', null, 'Units'));
  var list = el('div', { 'class': 'unit-list' });
  UNITS.forEach(function (U) {
    var done = SECTIONS.filter(function (s) { return secDone(U, s.k); }).length;
    list.appendChild(el('button', { 'class': 'unit-card', type: 'button', onclick: function () { go('#/u/' + U.n); } },
      el('span', { 'class': 'unit-num' }, String(U.n)),
      el('span', { 'class': 'unit-info' }, el('b', null, U.title), el('span', { 'class': 'sec small-t' }, 'Book pages ' + U.pages + ' · ' + done + '/' + SECTIONS.length + ' sections')),
      el('span', { 'class': 'stars', 'aria-label': unitStars(U.n) + ' stars' }, starsText(unitStars(U.n)))));
  });
  w.appendChild(list);
  var big = el('div', { 'class': 'big-cards' });
  if (DATA.verbs.length) big.appendChild(el('button', { 'class': 'big-card purple', type: 'button', onclick: function () { go('#/verbs'); } }, icon('verbs', 30, INK.purple), el('b', null, 'Irregular Verbs'), el('span', { 'class': 'sec small-t' }, 'go – went, see – saw… Learn and test them.')));
  big.appendChild(el('button', { 'class': 'big-card teal', type: 'button', onclick: function () { go('#/smarter'); } }, icon('smarter', 30, INK.teal), el('b', null, 'Learn Smarter'), el('span', { 'class': 'sec small-t' }, 'Tips and tricks for learning English.')));
  big.appendChild(el('button', { 'class': 'big-card amber', type: 'button', onclick: function () { go('#/resources'); } }, icon('resources', 30, INK.amber), el('b', null, 'Resources'), el('span', { 'class': 'sec small-t' }, 'Useful websites and apps.')));
  w.appendChild(big);

  w.appendChild(el('h2', { 'class': 'mt' }, 'Practise everything'));
  var pileN = Object.keys(S.pile).length;
  var tools = el('div', { 'class': 'tool-grid' },
    tool('pile', 'Review Pile', pileN ? String(pileN) : '', '#/pile', 'amber'),
    tool('notebook', 'Mistake Notebook', S.mistakes.length ? String(S.mistakes.length) : '', '#/mistakes', 'coral'),
    tool('review', 'Level Review', '', '#/review', 'purple'),
    tool('progress', 'Progress', '', '#/progress', 'teal'),
    tool('classroom', 'Classroom English', '', '#/classroom', 'teal'),
    tool('grammar', 'Grammar index', '', '#/grammar', 'purple'));
  w.appendChild(tools);
  function tool(ic, name, cnt, h, c) { return el('button', { 'class': 'tool', type: 'button', onclick: function () { go(h); } }, icon(ic, 24, INK[c]), name, cnt ? el('span', { 'class': 'badge cnt ' + c }, cnt) : null); }
  w.appendChild(grammarIndex(true));
}
function grammarIndex(compact) {
  var c = el('section', { 'class': 'card accent-purple mt', id: 'grammar-index' }, el('h2', null, icon('grammar', 24, INK.purple), 'Grammar index'));
  UNITS.forEach(function (U) {
    var d = el('div', { 'class': 'gi-unit' }, el('b', null, 'Unit ' + U.n + ' · ' + U.title));
    U.grammar.forEach(function (g) { d.appendChild(el('button', { 'class': 'gi-link', type: 'button', onclick: function () { go('#/u/' + U.n + '/grammar/' + g.id); } }, g.title)); });
    c.appendChild(d);
  });
  return c;
}

/* ---------- unit ---------- */
function pageUnit(U) {
  var w = page();
  crumbs(w, [['Home', '#/']]);
  var h = el('div', { 'class': 'sec-head teal' }, el('h1', null, 'Unit ' + U.n + ': ' + U.title),
    el('p', { 'class': 'sec', style: 'margin:6px 0 0' }, 'Book pages ' + U.pages + ' · ', el('span', { 'class': 'stars' }, starsText(unitStars(U.n)))));
  w.appendChild(h);
  var g = el('div', { 'class': 'sec-grid' });
  SECTIONS.forEach(function (s) {
    var done = secDone(U, s.k);
    g.appendChild(el('button', { 'class': 'sec-btn' + (done ? ' done' : ''), type: 'button', onclick: function () { go('#/u/' + U.n + '/' + s.k); } },
      el('span', { 'class': 'ic ' + s.c }, icon(s.ic, 22, INK[s.c])), s.name, done ? el('span', { 'class': 'tick', 'aria-label': 'done' }, '✓') : null));
  });
  w.appendChild(g);
}
function pager(w, U, k) {
  var i = SECTIONS.findIndex(function (s) { return s.k === k; });
  var p = el('div', { 'class': 'pager' });
  if (i > 0) p.appendChild(el('button', { 'class': 'btn ghost', type: 'button', onclick: function () { go('#/u/' + U.n + '/' + SECTIONS[i - 1].k); } }, icon('back', 18), SECTIONS[i - 1].name));
  else p.appendChild(el('span'));
  if (i < SECTIONS.length - 1) p.appendChild(el('button', { 'class': 'btn', type: 'button', onclick: function () { go('#/u/' + U.n + '/' + SECTIONS[i + 1].k); } }, SECTIONS[i + 1].name, icon('next', 18)));
  else p.appendChild(el('button', { 'class': 'btn', type: 'button', onclick: function () { go('#/u/' + U.n); } }, 'Unit ' + U.n, icon('next', 18)));
  w.appendChild(p);
}

function pageSection(U, k, sub) {
  var w = page();
  var s = secByK(k);
  crumbs(w, [['Home', '#/'], ['Unit ' + U.n, '#/u/' + U.n]]);
  secHead(w, s.name, s.c, s.ic, 'Unit ' + U.n + ' · ' + U.title);
  ({ words: secWords, practice: secPractice, grammar: secGrammar, classroom: secClassroom, reading: secReading, dialogue: secDialogue,
     wq: secWQ, writing: secWriting, games: secGames, test: secTest, cando: secCando })[k](w, U, sub);
  pager(w, U, k);
  if (sub && k === 'grammar') { var t = document.getElementById('gp-' + sub); if (t) setTimeout(function () { t.scrollIntoView({ block: 'start' }); }, 0); }
}

/* words */
function setWord(id, st) {
  S.words[id] = st;
  if (st === 'learn') { if (S.pile['w:' + id] === undefined) S.pile['w:' + id] = 0; }
  else delete S.pile['w:' + id];
  touchStreak(); save();
}
function secWords(w, U) {
  var mode = S.wordsView || 'cards';
  var seg = el('div', { 'class': 'seg', role: 'group', 'aria-label': 'View' });
  var body = el('div', { 'class': 'mt8' });
  ['cards', 'list'].forEach(function (m) {
    seg.appendChild(el('button', { type: 'button', 'aria-pressed': String(mode === m), onclick: function () { S.wordsView = m; save(); render(); } }, m === 'cards' ? 'Cards' : 'List'));
  });
  var known = U.words.filter(function (x) { return S.words[x.id] === 'know'; }).length;
  w.appendChild(el('div', { 'class': 'row between mb' }, seg, el('span', { 'class': 'badge purple' }, known + ' / ' + U.words.length + ' known')));
  w.appendChild(body);
  function statusBtns(x, after) {
    return el('div', { 'class': 'row', style: 'justify-content:center' },
      el('button', { 'class': 'btn small' + (S.words[x.id] === 'know' ? '' : ' ghost'), type: 'button', onclick: function () { setWord(x.id, 'know'); after(); } }, '✓ I know it'),
      el('button', { 'class': 'btn small' + (S.words[x.id] === 'learn' ? ' amber' : ' ghost'), type: 'button', onclick: function () { setWord(x.id, 'learn'); after(); } }, 'Still learning'));
  }
  if (mode === 'cards') {
    var i = 0;
    var draw = function () {
      clear(body);
      var x = U.words[i];
      body.appendChild(el('div', { 'class': 'wcard' },
        el('span', { 'class': 'badge purple cat' }, x.cat),
        el('div', { 'class': 'w' }, x.w),
        el('p', { 'class': 'sec' }, rich(x.d)),
        el('p', null, el('i', null, rich(x.ex))),
        statusBtns(x, function () { if (i < U.words.length - 1) i++; draw(); })));
      body.appendChild(el('div', { 'class': 'row between mt8' },
        el('button', { 'class': 'btn ghost', type: 'button', disabled: i === 0, onclick: function () { i--; draw(); } }, icon('back', 18), 'Back'),
        el('span', { 'class': 'sec' }, (i + 1) + ' / ' + U.words.length),
        el('button', { 'class': 'btn ghost', type: 'button', disabled: i === U.words.length - 1, onclick: function () { i++; draw(); } }, 'Next', icon('next', 18))));
    };
    draw();
  } else {
    var lst = el('div', { 'class': 'wlist' });
    var cat = null;
    U.words.forEach(function (x) {
      if (x.cat !== cat) { cat = x.cat; lst.appendChild(el('h3', { 'class': 'mt8' }, cat)); }
      var row = el('div', { 'class': 'witem ' + (S.words[x.id] || '') });
      var fill = function () {
        clear(row); row.className = 'witem ' + (S.words[x.id] || '');
        row.appendChild(el('b', null, x.w)); row.appendChild(el('div', { 'class': 'sec small-t' }, rich(x.d)));
        row.appendChild(el('div', { 'class': 'small-t' }, el('i', null, rich(x.ex))));
        var sb = statusBtns(x, fill); sb.style.justifyContent = 'flex-start'; sb.classList.add('mt8'); row.appendChild(sb);
      };
      fill();
      lst.appendChild(row);
    });
    body.appendChild(lst);
  }
}
function setsList(w, sets) { sets.forEach(function (s) { w.appendChild(renderSet(s)); }); }
function secPractice(w, U) { setsList(w, U.wsets); }

/* grammar */
function patternNode(rows) {
  var p = el('div', { 'class': 'pattern' });
  rows.forEach(function (r) {
    var row = el('div', { 'class': 'prow' });
    if (r[0]) row.appendChild(el('span', { 'class': 'pcue', 'aria-label': r[0] === '+' ? 'positive' : r[0] === '?' ? 'question' : 'negative' }, r[0]));
    var cls = ['s', 'v', 'r', 'r', 'r'];
    r.slice(1).forEach(function (b, i) {
      var txt = b, c = cls[i] || 'r';
      if (Array.isArray(b)) { txt = b[0]; c = b[1]; }
      if (txt) row.appendChild(el('span', { 'class': 'blk ' + c }, rich(txt)));
    });
    p.appendChild(row);
  });
  return p;
}
function grammarCard(U, g) {
  var c = el('section', { 'class': 'card gcard', id: 'gp-' + g.id });
  c.appendChild(el('h2', null, icon('grammar', 24, INK.purple), g.title));
  var v = renderVisual(g.visual); if (v) c.appendChild(v);
  if (g.pattern.length) { c.appendChild(el('h3', null, 'The pattern')); c.appendChild(patternNode(g.pattern)); }
  if (g.note) c.appendChild(el('p', { 'class': 'sec' }, rich(g.note)));
  c.appendChild(el('h3', { 'class': 'mt8' }, 'Examples'));
  c.appendChild(el('ul', { 'class': 'examples' }, g.examples.map(function (e) { return el('li', null, rich(e)); })));
  c.appendChild(el('div', { 'class': 'arbox', dir: 'rtl', lang: 'ar' }, g.ar.map(arabicLine)));
  c.appendChild(el('div', { 'class': 'watch' }, el('h4', null, 'Watch out!'), g.watch.map(function (x) {
    return el('div', { 'class': 'wr' }, el('span', { 'class': 'wrong-t' }, x[0]), el('span', { 'aria-hidden': 'true' }, '→'), el('span', { 'class': 'right-t' }, x[1]));
  })));
  if (g.quick) { c.appendChild(el('h3', { 'class': 'mt' }, 'Quick check')); c.appendChild(renderSet(g.quick)); }
  c.appendChild(el('h3', { 'class': 'mt' }, 'Practice'));
  var holder = el('div');
  g.sets.forEach(function (s, i) {
    var best = S.sets[s.id];
    var slot = el('div');
    var b = el('button', { 'class': 'btn ghost block mt8', type: 'button', 'aria-expanded': 'false', style: 'justify-content:flex-start' },
      icon(TYPE_ICON[s.k] || 'choose', 20, INK.teal), 'Practice ' + (i + 1) + ': ' + s.instr, best && best.done ? el('span', { 'class': 'badge ok', style: 'margin-left:auto' }, (Math.round(best.best * 10) / 10) + '/' + best.n) : null);
    b.addEventListener('click', function () {
      if (slot.firstChild) { clear(slot); b.setAttribute('aria-expanded', 'false'); return; }
      slot.appendChild(renderSet(s)); b.setAttribute('aria-expanded', 'true');
    });
    holder.appendChild(b); holder.appendChild(slot);
  });
  c.appendChild(holder);
  return c;
}
function secGrammar(w, U) {
  if (U.grammar.length > 1) w.appendChild(el('div', { 'class': 'row mb' }, U.grammar.map(function (g) { return el('button', { 'class': 'btn small purple', type: 'button', onclick: function () { var t = document.getElementById('gp-' + g.id); if (t) t.scrollIntoView({ block: 'start', behavior: 'smooth' }); } }, g.title); })));
  U.grammar.forEach(function (g) { w.appendChild(grammarCard(U, g)); });
}

/* classroom */
function secClassroom(w, U) {
  var c = el('section', { 'class': 'card accent-teal' }, el('h2', null, 'Phrases for this unit'));
  var st = U.cls.phrases.filter(function (p) { return p.who === 'S'; }), te = U.cls.phrases.filter(function (p) { return p.who === 'T'; });
  if (st.length) { c.appendChild(el('h3', null, 'You say')); c.appendChild(el('ul', { 'class': 'examples' }, st.map(function (p) { return el('li', null, el('b', null, p.p), el('div', { 'class': 'sec small-t' }, p.s)); }))); }
  if (te.length) { c.appendChild(el('h3', { 'class': 'mt8' }, 'Your teacher says')); c.appendChild(el('ul', { 'class': 'examples' }, te.map(function (p) { return el('li', null, el('b', null, p.p), el('div', { 'class': 'sec small-t' }, p.s)); }))); }
  w.appendChild(c);
  setsList(w, U.cls.sets);
  w.appendChild(el('button', { 'class': 'btn amber block', type: 'button', onclick: function () { go('#/u/' + U.n + '/games/cls'); } }, icon('games', 22), 'Game round: Classroom Speed Round'));
}

/* reading */
function secReading(w, U) {
  var R = U.reading;
  var panel = el('div', { 'class': 'textpanel', tabindex: '0', 'aria-label': 'Reading text' }, el('h2', null, R.title));
  R.text.split(/\n\s*\n/).forEach(function (p) { panel.appendChild(el('p', null, rich(p.trim()))); });
  w.appendChild(panel);
  setsList(w, R.sets);
}

/* dialogue */
function secDialogue(w, U) {
  var D = U.dialogue;
  w.appendChild(el('section', { 'class': 'card accent-teal' }, el('h2', null, D.title), D.intro ? el('p', { 'class': 'sec' }, rich(D.intro)) : null,
    D.task === 'order' ? el('p', { 'class': 'sec small-t' }, 'Read the lines below and put them in order.') : el('p', { 'class': 'sec small-t' }, 'Complete the dialogue. Then read it with a partner.')));
  setsList(w, D.sets);
}
function secWQ(w, U) {
  w.appendChild(el('p', { 'class': 'sec' }, 'Read the answer. Write the question.'));
  setsList(w, U.wq);
}

/* writing */
function copyText(txt) {
  function fallback() {
    var ta = el('textarea', { style: 'position:fixed;left:-9999px;top:0' }); ta.value = txt; document.body.appendChild(ta); ta.select();
    var ok = false; try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
    ta.remove(); toast(ok ? 'Copied!' : 'Select the text and copy it.');
  }
  try {
    if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(txt).then(function () { toast('Copied!'); }, fallback);
    else fallback();
  } catch (e) { fallback(); }
}
function secWriting(w, U) {
  U.writing.forEach(function (t2, i) {
    var c = el('section', { 'class': 'card accent-coral' }, el('h2', null, 'Task ' + (i + 1)), el('p', null, rich(t2.task)));
    if (t2.tip) c.appendChild(el('p', { 'class': 'sec small-t' }, rich(t2.tip)));
    var ta = el('textarea', { 'class': 'draft', 'aria-label': 'Your text', placeholder: 'Write here…' });
    ta.value = S.drafts[t2.id] || '';
    var cnt = el('span', { 'class': 'badge' });
    function upd() { var n = wordCount(ta.value); cnt.textContent = n + ' words (aim: ' + t2.min + '–' + t2.max + ')'; cnt.className = 'badge ' + (n >= t2.min ? 'ok' : 'amber'); }
    ta.addEventListener('input', function () { S.drafts[t2.id] = ta.value; save(); upd(); });
    upd();
    c.appendChild(ta);
    var model = el('div', { 'class': 'model x-hide' }, el('b', null, 'Model answer'), t2.model.split('\n').map(function (p) { return el('p', null, rich(p)); }));
    c.appendChild(el('div', { 'class': 'row between mt8' }, cnt, el('div', { 'class': 'row' },
      el('button', { 'class': 'btn small ghost', type: 'button', onclick: function () { copyText(ta.value); } }, 'Copy my text'),
      el('button', { 'class': 'btn small', type: 'button', onclick: function (e) { model.classList.toggle('x-hide'); e.currentTarget.textContent = model.classList.contains('x-hide') ? 'Show model answer' : 'Hide model answer'; } }, 'Show model answer'))));
    c.appendChild(model);
    c.appendChild(el('h3', { 'class': 'mt' }, 'Check your writing'));
    var ul = el('ul', { 'class': 'checklist' });
    t2.check.forEach(function (ck, j) {
      var key = t2.id + ':ck' + j;
      var cb = el('input', { type: 'checkbox' }); cb.checked = !!S.drafts[key];
      cb.addEventListener('change', function () { S.drafts[key] = cb.checked; save(); });
      ul.appendChild(el('li', null, el('label', { 'class': 'ck' }, cb, el('span', null, rich(ck)))));
    });
    c.appendChild(ul);
    w.appendChild(c);
  });
}

/* games */
function secGames(w, U) {
  var g = el('div', { 'class': 'big-cards', style: 'margin-top:0' });
  U.games.list.forEach(function (k) {
    var info = GAME_INFO[k];
    var best = S.games[bestKey('u' + U.n, k)];
    g.appendChild(el('button', { 'class': 'big-card amber', type: 'button', onclick: function () { go('#/u/' + U.n + '/games/' + k); } },
      el('b', null, info.name), el('span', { 'class': 'sec small-t' }, info.d), best !== undefined ? el('span', { 'class': 'badge amber' }, 'Best: ' + best) : null));
  });
  w.appendChild(g);
  w.appendChild(el('p', { 'class': 'sec small-t mt' }, 'On a projector? Choose "2 teams" in any game. The teacher taps ✅ for the team that answers.'));
}
function pageGame(U, k) {
  var w = page();
  crumbs(w, [['Home', '#/'], ['Unit ' + U.n, '#/u/' + U.n], ['Games', '#/u/' + U.n + (k === 'cls' ? '/classroom' : '/games')]]);
  S.secs[U.n + ':games'] = 1; save();
  w.appendChild(gameShell(k, 'u' + U.n, function (ctx) { GAMES[k](ctx, U); }));
}

/* test */
function secTest(w, U) {
  var best = S.tests[U.n];
  if (best !== undefined) w.appendChild(el('p', null, el('span', { 'class': 'badge ok' }, 'Your best: ' + best + '%'), ' ', el('span', { 'class': 'stars' }, starsText(starsFor(best)))));
  w.appendChild(renderTest(U.test, { title: 'Unit ' + U.n + ' test', onDone: function (pct) { S.tests[U.n] = Math.max(S.tests[U.n] || 0, pct); save(); } }));
}
function secCando(w, U) {
  var c = el('section', { 'class': 'card accent-purple' }, el('h2', null, 'Tick what you can do now.'));
  var ul = el('ul', { 'class': 'checklist' });
  U.cando.forEach(function (s, i) {
    var key = U.n + ':' + i;
    var cb = el('input', { type: 'checkbox' }); cb.checked = !!S.cando[key];
    cb.addEventListener('change', function () { S.cando[key] = cb.checked; touchStreak(); save(); });
    ul.appendChild(el('li', null, el('label', { 'class': 'ck' }, cb, el('span', null, 'I can ' + s))));
  });
  c.appendChild(ul);
  w.appendChild(c);
}

/* ---------- level-wide ---------- */
function pilePrompt(key) {
  if (key.slice(0, 2) === 'w:') {
    var wid = key.slice(2);
    for (var i = 0; i < UNITS.length; i++) for (var j = 0; j < UNITS[i].words.length; j++) { var x = UNITS[i].words[j]; if (x.id === wid) return x.qid ? { item: x.qid, word: x } : { word: x }; }
    return null;
  }
  return ITEMS[key] ? { item: key } : null;
}
function pagePile() {
  var w = page();
  crumbs(w, [['Home', '#/']]);
  secHead(w, 'Review Pile', 'amber', 'pile', 'Words you are still learning and questions you got wrong. Get each one right twice.');
  var keys = Object.keys(S.pile).filter(function (k) { return pilePrompt(k); });
  if (!keys.length) { w.appendChild(el('div', { 'class': 'card' }, el('p', null, 'Your pile is empty. Great! Mark words as "Still learning", or do some exercises.'))); return; }
  w.appendChild(el('p', null, el('span', { 'class': 'badge amber' }, keys.length + ' in your pile')));
  var box = el('div');
  w.appendChild(box);
  var order = shuffled(keys), k = 0;
  function show() {
    clear(box);
    order = order.filter(function (x) { return S.pile[x] !== undefined; });
    if (!order.length) { box.appendChild(el('div', { 'class': 'card' }, el('h2', null, 'All done!'), el('p', null, 'Your Review Pile is empty.'))); return; }
    if (k >= order.length) k = 0;
    var key = order[k], P = pilePrompt(key);
    var card = el('section', { 'class': 'card set accent-amber' }, el('div', { 'class': 'set-head' }, el('h3', null, 'Right ' + (S.pile[key] || 0) + ' / 2'), el('span', { 'class': 'set-prog' }, (k + 1) + ' / ' + order.length)));
    if (P.item) {
      var c = makeItem(P.item, 0, 'pile', function (cc) {
        if (cc.score > 0) { S.pile[key] = (S.pile[key] || 0) + 1; if (S.pile[key] >= 2) { delete S.pile[key]; if (P.word) S.words[P.word.id] = 'know'; toast('Out of the pile!'); } }
        else S.pile[key] = 0;
        save();
        nextBtn.disabled = false;
      });
      card.appendChild(c.node);
    } else card.appendChild(el('div', { 'class': 'wcard' }, el('div', { 'class': 'w' }, P.word.w), el('p', null, rich(P.word.d))));
    var nextBtn = el('button', { 'class': 'btn mt8', type: 'button', disabled: !!P.item, onclick: function () { k++; show(); } }, 'Next', icon('next', 18));
    card.appendChild(nextBtn);
    box.appendChild(card);
  }
  show();
}
function pageMistakes() {
  var w = page();
  crumbs(w, [['Home', '#/']]);
  secHead(w, 'Mistake Notebook', 'coral', 'notebook', 'Your wrong answers and the right ones. Read them before a test.');
  if (!S.mistakes.length) { w.appendChild(el('div', { 'class': 'card' }, el('p', null, 'No mistakes saved yet.'))); return; }
  var clr = el('button', { 'class': 'btn small coral', type: 'button' }, 'Clear the notebook');
  clr.addEventListener('click', function () {
    if (!clr.dataset.sure) { clr.dataset.sure = '1'; clr.textContent = 'Sure? Tap again to clear'; return; }
    S.mistakes = []; save(); render();
  });
  w.appendChild(el('div', { 'class': 'row between mb' }, el('span', { 'class': 'badge coral' }, S.mistakes.length + ' mistakes'), clr));
  var ul = el('ul', { 'class': 'result-list card' });
  S.mistakes.forEach(function (m) {
    ul.appendChild(el('li', null, el('div', { 'class': 'small-t sec' }, m.src), el('div', null, rich(m.q)),
      el('div', null, el('span', { 'class': 'wrong-t' }, m.your), '  →  ', el('span', { 'class': 'right-t' }, m.right))));
  });
  w.appendChild(ul);
}
function pageReview(sub) {
  var w = page();
  crumbs(w, sub ? [['Home', '#/'], ['Level Review', '#/review']] : [['Home', '#/']]);
  if (sub === 'boss') { secHead(w, 'Boss Battle', 'amber', 'games', 'Questions from the whole level.'); w.appendChild(gameShell('boss', 'level', function (ctx) { GAMES.boss(ctx, DATA.boss); })); return; }
  secHead(w, 'Level Review', 'purple', 'review', DATA.review.length + ' questions from every unit.');
  w.appendChild(el('button', { 'class': 'btn amber block mb', type: 'button', onclick: function () { go('#/review/boss'); } }, icon('games', 22), 'Play the Boss Battle'));
  var best = S.tests.review;
  if (best !== undefined) w.appendChild(el('p', null, el('span', { 'class': 'badge ok' }, 'Your best: ' + best + '%')));
  w.appendChild(renderTest(DATA.review, { title: 'Level Review', onDone: function (pct) { S.tests.review = Math.max(S.tests.review || 0, pct); save(); } }));
}
function pageProgress() {
  var w = page();
  crumbs(w, [['Home', '#/']]);
  secHead(w, 'Progress', 'teal', 'progress');
  var totalSets = 0, doneSets = 0;
  UNITS.forEach(function (U) { SECTIONS.forEach(function (s) { unitSets(U, s.k).forEach(function (st) { totalSets++; if (S.sets[st.id] && S.sets[st.id].done) doneSets++; }); }); });
  var known = 0; UNITS.forEach(function (U) { U.words.forEach(function (x) { if (S.words[x.id] === 'know') known++; }); });
  var nw = UNITS.reduce(function (a, U) { return a + U.words.length; }, 0);
  w.appendChild(el('div', { 'class': 'stat-grid mb' },
    el('div', { 'class': 'stat' }, el('b', null, String(streakNow())), 'days in a row'),
    el('div', { 'class': 'stat' }, el('b', null, doneSets + '/' + totalSets), 'exercise sets done'),
    el('div', { 'class': 'stat' }, el('b', null, known + '/' + nw), 'words known'),
    el('div', { 'class': 'stat' }, el('b', null, String(Object.keys(S.pile).length)), 'in Review Pile')));
  UNITS.forEach(function (U) {
    var done = SECTIONS.filter(function (s) { return secDone(U, s.k); });
    var pct = Math.round(100 * done.length / SECTIONS.length);
    w.appendChild(el('section', { 'class': 'card' },
      el('div', { 'class': 'row between' }, el('b', null, 'Unit ' + U.n + ': ' + U.title), el('span', { 'class': 'stars' }, starsText(unitStars(U.n)))),
      el('p', { 'class': 'sec small-t' }, 'Unit test best: ' + (S.tests[U.n] === undefined ? 'not taken' : S.tests[U.n] + '%') + ' · Sections done: ' + done.length + '/' + SECTIONS.length),
      el('div', { 'class': 'pbar' }, el('i', { style: 'width:' + pct + '%' })),
      el('div', { 'class': 'chips mt8' }, SECTIONS.map(function (s) { return el('span', { 'class': 'chip', style: secDone(U, s.k) ? 'border-color:#4CAF50;color:#388E3C' : 'color:#798D96' }, (secDone(U, s.k) ? '✓ ' : '') + s.name); }))));
  });
}
function pageVerbs() {
  var w = page();
  crumbs(w, [['Home', '#/']]);
  secHead(w, 'Irregular Verbs', 'purple', 'verbs', DATA.pp ? 'Base form · past simple · past participle' : 'Base form and past simple');
  var V = DATA.verbs;
  var modes = el('div', { 'class': 'row mb' });
  var box = el('div');
  var mk = function (name, fn) { modes.appendChild(el('button', { 'class': 'btn small purple', type: 'button', onclick: fn }, name)); };
  mk('List', list); mk('Flashcards', cards); mk('Type the past', function () { typer(false); }); if (DATA.pp) mk('Type the past participle', function () { typer(true); });
  w.appendChild(modes); w.appendChild(box);
  function list() {
    clear(box);
    var tb = el('table', { 'class': 'vtable card' });
    tb.appendChild(el('tr', null, el('th', null, 'base'), el('th', null, 'past'), DATA.pp ? el('th', null, 'past participle') : null));
    V.forEach(function (v) { tb.appendChild(el('tr', null, el('td', { 'class': 'c-teal' }, v[0]), el('td', { 'class': 'c-purple' }, v[1]), DATA.pp ? el('td', { 'class': 'c-amber' }, v[2]) : null)); });
    box.appendChild(tb);
  }
  function cards() {
    clear(box);
    var deck = shuffled(V), i = 0;
    var c = el('div', { 'class': 'wcard' }); box.appendChild(c);
    function draw(show) {
      clear(c);
      var v = deck[i];
      c.appendChild(el('div', { 'class': 'w' }, v[0]));
      if (show) c.appendChild(el('p', { 'class': 'right-t', style: 'font-size:1.4rem' }, v[1] + (DATA.pp ? '  ·  ' + v[2] : '')));
      c.appendChild(el('div', { 'class': 'row', style: 'justify-content:center' },
        el('button', { 'class': 'btn small ghost', type: 'button', onclick: function () { draw(true); } }, 'Show'),
        el('button', { 'class': 'btn small', type: 'button', onclick: function () { i = (i + 1) % deck.length; draw(false); } }, 'Next', icon('next', 18))));
    }
    draw(false);
  }
  function typer(pp) {
    clear(box);
    var deck = shuffled(V).slice(0, 10), score = 0;
    var card = el('section', { 'class': 'card set accent-purple' }, el('h3', null, pp ? 'Write the past participle.' : 'Write the past simple.'));
    deck.forEach(function (v, n) {
      var acc = (pp ? v[2] : v[1]).split(' / ');
      var row = el('div', { 'class': 'item' });
      var inp = el('input', { 'class': 'inp', type: 'text', autocomplete: 'off', autocapitalize: 'off', spellcheck: 'false', 'aria-label': v[0] });
      var fb = el('div', { 'class': 'fb' });
      var tries = 0, done = false;
      var chk = el('button', { 'class': 'btn small', type: 'button', onclick: check }, 'Check');
      inp.addEventListener('keydown', function (e) { if (e.key === 'Enter') check(); });
      function check() {
        if (done || !inp.value.trim()) return;
        tries++;
        if (matches(inp.value, acc)) { done = true; inp.classList.add('right'); score += tries === 1 ? 1 : 0.5; fb.className = 'fb ok'; fb.textContent = 'Great!'; touchStreak(); }
        else if (tries >= 2) { done = true; inp.classList.add('wrong'); fb.className = 'fb no'; fb.textContent = 'The answer is: ' + acc.join(' / '); }
        else { anim(inp, 'shake'); fb.className = 'fb no'; fb.textContent = 'Not quite. Try again.'; }
        if (done) { inp.disabled = true; chk.disabled = true; sc.textContent = 'Score: ' + score + ' / ' + deck.length; }
      }
      row.appendChild(el('div', { 'class': 'qline' }, el('span', { 'class': 'qn' }, String(n + 1)), el('span', { 'class': 'qt' }, v[0])));
      row.appendChild(el('div', { 'class': 'inrow' }, inp, chk)); row.appendChild(fb);
      card.appendChild(row);
    });
    var sc = el('p', { 'class': 'score-big' }, 'Score: 0 / ' + deck.length);
    card.appendChild(sc);
    card.appendChild(el('button', { 'class': 'btn ghost', type: 'button', onclick: function () { typer(pp); } }, 'New verbs'));
    box.appendChild(card);
  }
  list();
}
function pageSmarter(id) {
  var w = page();
  if (id) {
    var tip = DATA.smarter.filter(function (x) { return x.id === id; })[0];
    if (!tip) { go('#/smarter'); return; }
    crumbs(w, [['Home', '#/'], ['Learn Smarter', '#/smarter']]);
    secHead(w, tip.title, 'teal', 'smarter', tip.summary);
    var i = 0, box = el('div');
    w.appendChild(box);
    var draw = function () {
      clear(box);
      var s = tip.slides[i];
      box.appendChild(el('div', { 'class': 'slide' }, el('h2', null, s.h), smartArt(s.v), el('p', null, rich(s.t))));
      var dots = el('div', { 'class': 'dots' }); tip.slides.forEach(function (_, k) { dots.appendChild(el('i', { 'class': k === i ? 'on' : '' })); });
      box.appendChild(dots);
      box.appendChild(el('div', { 'class': 'row between mt8' },
        el('button', { 'class': 'btn ghost', type: 'button', disabled: i === 0, onclick: function () { i--; draw(); } }, icon('back', 18), 'Back'),
        i < tip.slides.length - 1 ? el('button', { 'class': 'btn', type: 'button', onclick: function () { i++; draw(); } }, 'Next', icon('next', 18))
          : el('button', { 'class': 'btn', type: 'button', onclick: function () { S.slides[tip.id] = 1; save(); go('#/smarter'); } }, 'Done ✓')));
    };
    draw();
    return;
  }
  crumbs(w, [['Home', '#/']]);
  secHead(w, 'Learn Smarter', 'teal', 'smarter', 'Short tips with mini presentations.');
  var g = el('div', { 'class': 'big-cards', style: 'margin-top:0' });
  DATA.smarter.forEach(function (tip) {
    g.appendChild(el('button', { 'class': 'big-card teal', type: 'button', onclick: function () { go('#/smarter/' + tip.id); } },
      el('b', null, tip.title), el('span', { 'class': 'sec small-t' }, tip.summary), S.slides[tip.id] ? el('span', { 'class': 'badge ok' }, '✓ seen') : null));
  });
  w.appendChild(g);
}
function pageResources() {
  var w = page();
  crumbs(w, [['Home', '#/']]);
  secHead(w, 'Resources', 'amber', 'resources', 'Useful websites and apps. They open outside this app and need the internet.');
  DATA.resources.forEach(function (r) {
    w.appendChild(el('section', { 'class': 'card' }, el('div', { 'class': 'row between' }, el('b', null, r.name), el('span', { 'class': 'badge amber' }, r.kind)),
      el('p', { 'class': 'sec' }, r.what), el('a', { href: r.url, target: '_blank', rel: 'noopener noreferrer', 'class': 'btn small ghost' }, r.url.replace(/^https?:\/\//, ''))));
  });
}
function pageClassroom() {
  var w = page();
  crumbs(w, [['Home', '#/']]);
  secHead(w, 'Classroom English', 'teal', 'classroom', 'All the classroom phrases for this level.');
  [['S', 'You say'], ['T', 'Your teacher says']].forEach(function (g) {
    var c = el('section', { 'class': 'card accent-teal' }, el('h2', null, g[1]));
    c.appendChild(el('ul', { 'class': 'examples' }, DATA.classroom.filter(function (p) { return p.who === g[0]; }).map(function (p) { return el('li', null, el('b', null, p.p), el('div', { 'class': 'sec small-t' }, p.s)); })));
    w.appendChild(c);
  });
}
function pageGrammarIndex() {
  var w = page();
  crumbs(w, [['Home', '#/']]);
  w.appendChild(grammarIndex(false));
}

/* ---------- router ---------- */
function render() {
  var h = location.hash || '#/';
  var p = h.replace(/^#\/?/, '').split('/').filter(Boolean);
  window.scrollTo(0, 0);
  if (!p.length) return pageHome();
  if (p[0] === 'u') {
    var U = unitByN(+p[1]);
    if (!U) return pageHome();
    if (p.length === 2) { S.last = h; save(); return pageUnit(U); }
    if (p[2] === 'games' && p[3]) { S.last = h; save(); return pageGame(U, p[3]); }
    if (secByK(p[2])) { S.last = h; save(); return pageSection(U, p[2], p[3]); }
    return pageUnit(U);
  }
  switch (p[0]) {
    case 'pile': return pagePile();
    case 'mistakes': return pageMistakes();
    case 'review': return pageReview(p[1]);
    case 'progress': return pageProgress();
    case 'verbs': return DATA.verbs.length ? pageVerbs() : pageHome();
    case 'smarter': return pageSmarter(p[1]);
    case 'resources': return pageResources();
    case 'classroom': return pageClassroom();
    case 'grammar': return pageGrammarIndex();
  }
  return pageHome();
}
window.addEventListener('hashchange', render);
document.addEventListener('visibilitychange', function () { if (document.hidden) save(true); });

/* ---------- test hook for the smoke test ---------- */
window.__APP = {
  data: DATA, norm: norm, matches: matches,
  go: function (h) { if (location.hash !== h) { location.hash = h; } render(); return MAIN.innerText.length; },
  state: function () { return JSON.parse(JSON.stringify(S)); },
  sets: function () { return Object.keys(SETREG); },
  items: function () { return Object.keys(REG); },
  answer: function (id, ok) { var c = REG[id]; if (!c) return 'missing'; c.autoAnswer(ok); return c.done; },
  item: function (id) { var c = REG[id]; return c ? { done: c.done, score: c.score, tries: c.tries } : null; },
  setScore: function (id) { var s = SETREG[id]; return s ? { finished: !!s.finished, score: s.score, n: s.ctls.length } : null; },
  openAllGrammar: function () { var n = 0; MAIN.querySelectorAll('button[aria-expanded=false]').forEach(function (b) { b.click(); n++; }); return n; },
  sections: SECTIONS.map(function (s) { return s.k; }),
  storeOk: function () { return STORE_OK; }
};

applyClassMode();
render();
