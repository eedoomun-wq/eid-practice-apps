/* ===== app.js: router and pages ===== */
var MAIN = document.getElementById('main');
var UNITS = DATA.units;
function unitByN(n) { for (var i = 0; i < UNITS.length; i++) if (UNITS[i].n === n) return UNITS[i]; return null; }

/* one lead accent per screen: teal = home and unit flow, purple = words and grammar,
   amber = games and puzzles, coral = tests and mistakes */
var SECTIONS = [
  { k: 'words', name: 'Words', ic: 'words', c: 'purple' },
  { k: 'grammar', name: 'Grammar', ic: 'grammar', c: 'purple' },
  { k: 'practice', name: 'Word practice', ic: 'match', c: 'teal' },
  { k: 'gpractice', name: 'Grammar practice', ic: 'gap', c: 'purple' },
  { k: 'classroom', name: 'Classroom English', ic: 'classroom', c: 'teal' },
  { k: 'wq', name: 'Write the question', ic: 'wq', c: 'teal' },
  { k: 'reading', name: 'Reading', ic: 'reading', c: 'teal' },
  { k: 'dialogue', name: 'Dialogue', ic: 'dialogue', c: 'teal' },
  { k: 'writing', name: 'Writing', ic: 'writing', c: 'teal' },
  { k: 'games', name: 'Games', ic: 'games', c: 'amber' },
  { k: 'puzzles', name: 'Puzzles', ic: 'puzzle', c: 'amber' },
  { k: 'test', name: 'Unit test', ic: 'test', c: 'coral' },
  { k: 'cando', name: 'I can…', ic: 'cando', c: 'teal' }
];
var STEPS = [
  { name: 'Learn', secs: ['words', 'grammar'] },
  { name: 'Practise', secs: ['practice', 'gpractice', 'classroom', 'wq'] },
  { name: 'Use it', secs: ['reading', 'dialogue', 'writing'] },
  { name: 'Play & check', secs: ['games', 'puzzles', 'test', 'cando'] }
];
function secByK(k) { for (var i = 0; i < SECTIONS.length; i++) if (SECTIONS[i].k === k) return SECTIONS[i]; return null; }
function hasSec(U, k) { return k !== 'puzzles' || !!(U.puzzles && U.puzzles.length); }
function unitSecs(U) { var a = []; STEPS.forEach(function (st) { st.secs.forEach(function (k) { if (hasSec(U, k)) a.push(k); }); }); return a; }

function unitSets(U, k) {
  switch (k) {
    case 'practice': return U.wsets;
    case 'grammar': return U.grammar.filter(function (g) { return g.quick; }).map(function (g) { return g.quick; });
    case 'gpractice': var a = []; U.grammar.forEach(function (g) { a = a.concat(g.sets); }); return a;
    case 'classroom': return U.cls.sets;
    case 'reading': return U.reading.sets;
    case 'dialogue': return U.dialogue.sets;
    case 'wq': return U.wq;
  }
  return [];
}
function setDone(s) { return !!(S.sets[s.id] && S.sets[s.id].done); }
function setsDone(sets) { return sets.length > 0 && sets.every(setDone); }
function secDone(U, k) {
  if (k === 'words') return U.words.every(function (w) { return S.words[w.id]; });
  if (k === 'writing') return U.writing.every(function (w) { return wordCount(S.drafts[w.id] || '') >= w.min; });
  if (k === 'games') return !!S.secs[U.n + ':games'];
  if (k === 'puzzles') return (U.puzzles || []).every(function (p) { return S.puzzles[p.id] && S.puzzles[p.id].done; });
  if (k === 'test') return S.tests[U.n] !== undefined;
  if (k === 'cando') return U.cando.every(function (_, i) { return S.cando[U.n + ':' + i]; });
  return setsDone(unitSets(U, k));
}
/* "3 / 7 sets" counters */
function secCount(U, k) {
  if (k === 'words') { var kn = U.words.filter(function (w) { return S.words[w.id] === 'know'; }).length; return kn + ' / ' + U.words.length + ' known'; }
  if (k === 'writing') return U.writing.filter(function (w) { return wordCount(S.drafts[w.id] || '') >= w.min; }).length + ' / ' + U.writing.length + ' tasks';
  if (k === 'games') return S.secs[U.n + ':games'] ? 'played' : U.games.list.length + ' games';
  if (k === 'puzzles') return (U.puzzles || []).filter(function (p) { return S.puzzles[p.id] && S.puzzles[p.id].done; }).length + ' / ' + (U.puzzles || []).length + ' solved';
  if (k === 'test') return S.tests[U.n] === undefined ? '25 questions' : 'best ' + S.tests[U.n] + '%';
  if (k === 'cando') return U.cando.filter(function (_, i) { return S.cando[U.n + ':' + i]; }).length + ' / ' + U.cando.length;
  var ss = unitSets(U, k);
  return ss.filter(setDone).length + ' / ' + ss.length + (k === 'grammar' ? ' checks' : ' sets');
}
function wordCount(s) { var m = String(s).match(/[A-Za-z0-9À-ɏ']+/g); return m ? m.length : 0; }

/* the exact next thing for this learner */
function nextIn(U, k) {
  var ss = unitSets(U, k);
  if (k === 'grammar') { for (var j = 0; j < U.grammar.length; j++) if (U.grammar[j].quick && !setDone(U.grammar[j].quick)) return { label: 'Grammar: ' + U.grammar[j].title, h: '#/u/' + U.n + '/grammar/' + U.grammar[j].id }; }
  for (var i = 0; i < ss.length; i++) if (!setDone(ss[i])) return { label: secByK(k).name + ' — set ' + (i + 1) + ' of ' + ss.length, h: '#/u/' + U.n + '/' + k + '/play/' + i };
  return { label: secByK(k).name + ' · ' + secCount(U, k), h: '#/u/' + U.n + '/' + k };
}
function nextForUnit(U) {
  var ks = unitSecs(U);
  for (var i = 0; i < ks.length; i++) if (!secDone(U, ks[i])) { var x = nextIn(U, ks[i]); x.U = U; x.k = ks[i]; return x; }
  return null;
}
function nextForMe() {
  for (var i = 0; i < UNITS.length; i++) { var x = nextForUnit(UNITS[i]); if (x) return x; }
  return null;
}
function unitPct(U) { var ks = unitSecs(U); return Math.round(100 * ks.filter(function (k) { return secDone(U, k); }).length / ks.length); }

/* ---------- shell ---------- */
function page(accent) {
  stopAllLoops(); REG = {}; SETREG = {}; clear(MAIN);
  document.body.setAttribute('data-acc', accent || 'teal');
  var w = el('div', { 'class': 'wrap' }); MAIN.appendChild(w); return w;
}
function crumbs(w, parts) {
  var c = el('nav', { 'class': 'crumb', 'aria-label': 'Back' });
  var p = parts[parts.length - 1];
  c.appendChild(el('button', { 'class': 'back-link', type: 'button', onclick: function () { go(p[1]); } }, p[1] === '#/' ? icon('home', 18) : icon('back', 18), p[0]));
  w.appendChild(c);
}
function secHead(w, title, color, iconName, sub) {
  var h = el('header', { 'class': 'page-head' }, el('div', { 'class': 'ph-ic ' + color }, icon(iconName, 26, INK[color] || INK.teal)), el('div', null, el('h1', null, title), sub ? el('p', { 'class': 'sec' }, sub) : null));
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

/* ---------- English first, Arabic on a toggle ---------- */
function setArBox(box, pill, open) {
  box.classList.toggle('open', open);
  pill.setAttribute('aria-pressed', String(open));
}
/* an Arabic block hidden behind a small عربي pill; the global switch opens or closes all of them */
function arToggle(lines) {
  var box = el('div', { 'class': 'arbox', dir: 'rtl', lang: 'ar' }, lines.map(arabicLine));
  var pill = el('button', { 'class': 'arpill', type: 'button', lang: 'ar', 'aria-pressed': 'false', 'aria-label': 'Arabic help: عربي' }, 'عربي');
  pill.addEventListener('click', function () { setArBox(box, pill, !box.classList.contains('open')); });
  box.__pill = pill;
  setArBox(box, pill, !!S.arHelp);
  return { pill: pill, box: box };
}
function enBlock(en, ar) {
  var wrap = el('div', { 'class': 'enbox' });
  var t = ar && ar.length ? arToggle(ar) : null;
  wrap.appendChild(el('div', { 'class': 'enbox-head' }, el('h4', null, 'In simple words'), t ? t.pill : null));
  if (en && en.length) wrap.appendChild(el('ul', { 'class': 'enlines' }, en.map(function (x) { return el('li', null, rich(x)); })));
  if (t) wrap.appendChild(t.box);
  return wrap;
}
function applyArabic() {
  var b = document.getElementById('arBtn');
  b.setAttribute('aria-pressed', String(!!S.arHelp));
  b.textContent = S.arHelp ? 'Arabic help: on' : 'Arabic help';
  b.hidden = !MAIN.querySelector('.arbox');
}
document.getElementById('arBtn').addEventListener('click', function () {
  S.arHelp = !S.arHelp; save();
  MAIN.querySelectorAll('.arbox').forEach(function (box) { if (box.__pill) setArBox(box, box.__pill, S.arHelp); });
  applyArabic();
});


/* ---------- home ---------- */
function unitStars(n) { var p = S.tests[n]; return p === undefined ? 0 : starsFor(p); }
function starsText(k) {
  var n = el('span', { 'class': 'stars', role: 'img', 'aria-label': k + ' of 3 stars' });
  for (var i = 0; i < 3; i++) n.appendChild(icon(i < k ? 'star' : 'starOff', 18));
  return n;
}
function streakPill() {
  var n = streakNow();
  return el('span', { 'class': 'streak', title: 'Days in a row' }, icon('flame', 18, INK.amber), n ? n + (n === 1 ? ' day' : ' days') : 'Start your streak today');
}
function pageHome() {
  var w = page('teal');
  w.appendChild(el('header', { 'class': 'home-head' },
    el('div', null, el('h1', null, DATA.title), el('p', { 'class': 'sec' }, DATA.book + ' · ' + DATA.unitsLabel)), streakPill()));
  if (!STORE_OK) w.appendChild(el('p', { 'class': 'note' }, 'Your browser is not saving progress here. Everything works, but your progress resets when you close the page.'));
  var nx = nextForMe();
  var cont = el('section', { 'class': 'continue' },
    el('p', { 'class': 'label' }, nx ? (Object.keys(S.sets).length ? 'Continue' : 'Start here') : 'All done!'),
    el('h2', null, nx ? 'Unit ' + nx.U.n + ' · ' + nx.label : 'You finished every unit. Try the Level Review!'),
    el('button', { 'class': 'btn primary', type: 'button', onclick: function () { go(nx ? nx.h : '#/review'); } }, nx ? 'Continue' : 'Level Review', icon('next', 18)));
  w.appendChild(cont);
  w.appendChild(el('h2', { 'class': 'label-h' }, 'Units'));
  var list = el('div', { 'class': 'unit-list' });
  UNITS.forEach(function (U) {
    var pct = unitPct(U), cur = nx && nx.U === U, st = unitStars(U.n);
    list.appendChild(el('button', { 'class': 'unit-row' + (cur ? ' current' : '') + (pct === 100 ? ' done' : ''), type: 'button', onclick: function () { go('#/u/' + U.n); } },
      el('span', { 'class': 'unit-num' }, pct === 100 ? icon('check', 22) : String(U.n)),
      el('span', { 'class': 'unit-info' }, el('b', null, U.title),
        el('span', { 'class': 'pbar thin' }, el('i', { style: 'width:' + pct + '%' }))),
      S.tests[U.n] !== undefined ? starsText(st) : el('span', { 'class': 'sec small-t' }, pct + '%')));
  });
  w.appendChild(list);
  w.appendChild(el('h2', { 'class': 'label-h' }, 'Tools'));
  var pileN = Object.keys(S.pile).length;
  var tools = [['pile', 'Review Pile', '#/pile', pileN], ['notebook', 'Mistakes', '#/mistakes', S.mistakes.length], ['review', 'Level Review', '#/review'],
    ['progress', 'Progress', '#/progress'], ['classroom', 'Classroom English', '#/classroom'], ['grammar', 'Grammar index', '#/grammar']];
  if (DATA.verbs.length) tools.push(['verbs', 'Irregular Verbs', '#/verbs']);
  tools.push(['smarter', 'Learn Smarter', '#/smarter'], ['resources', 'Resources', '#/resources']);
  var tg = el('div', { 'class': 'tool-chips' });
  tools.forEach(function (t) {
    tg.appendChild(el('button', { 'class': 'tool-chip', type: 'button', onclick: function () { go(t[2]); } },
      el('span', { 'class': 'tc-ic' }, icon(t[0], 24), t[3] ? el('span', { 'class': 'tc-n' }, String(t[3])) : null), el('span', null, t[1])));
  });
  w.appendChild(tg);
}
function grammarIndex() {
  var c = el('div', { 'id': 'grammar-index' });
  UNITS.forEach(function (U) {
    var d = el('section', { 'class': 'card gi-unit' }, el('h3', null, 'Unit ' + U.n + ' · ' + U.title));
    U.grammar.forEach(function (g) { d.appendChild(el('button', { 'class': 'list-row', type: 'button', onclick: function () { go('#/u/' + U.n + '/grammar/' + g.id); } }, el('span', null, g.title), icon('next', 18))); });
    c.appendChild(d);
  });
  return c;
}

/* ---------- unit: 4 numbered steps ---------- */
function pageUnit(U) {
  var w = page('teal');
  crumbs(w, [['Home', '#/']]);
  w.appendChild(el('header', { 'class': 'page-head' }, el('div', { 'class': 'ph-ic teal unit-badge' }, String(U.n)),
    el('div', null, el('h1', null, U.title), el('p', { 'class': 'sec' }, 'Unit ' + U.n + ' · book pages ' + U.pages + ' · ' + unitPct(U) + '% done'))));
  var nx = nextForUnit(U);
  if (nx) w.appendChild(el('section', { 'class': 'continue' }, el('p', { 'class': 'label' }, 'Next for you'), el('h2', null, nx.label),
    el('button', { 'class': 'btn primary', type: 'button', onclick: function () { go(nx.h); } }, 'Go', icon('next', 18))));
  else w.appendChild(el('section', { 'class': 'continue done' }, el('p', { 'class': 'label' }, 'Unit complete'), el('h2', null, 'Well done! Every part of this unit is done.')));
  STEPS.forEach(function (st, i) {
    var box = el('section', { 'class': 'step' }, el('h2', { 'class': 'step-h' }, el('span', { 'class': 'step-n' }, String(i + 1)), st.name));
    st.secs.forEach(function (k) {
      if (!hasSec(U, k)) return;
      var s = secByK(k), done = secDone(U, k), here = nx && nx.k === k;
      box.appendChild(el('button', { 'class': 'list-row sec-row' + (done ? ' done' : '') + (here ? ' here' : ''), type: 'button', onclick: function () { go('#/u/' + U.n + '/' + k); } },
        el('span', { 'class': 'ic ' + s.c }, icon(s.ic, 20, INK[s.c])), el('span', { 'class': 'sr-t' }, el('b', null, s.name), el('span', { 'class': 'sec small-t' }, secCount(U, k))),
        done ? el('span', { 'class': 'tick', 'aria-label': 'done' }, icon('check', 20)) : icon('next', 18)));
    });
    w.appendChild(box);
  });
}
function pager(w, U, k) {
  var ks = unitSecs(U), i = ks.indexOf(k);
  if (i < 0) return;
  var nk = ks[i + 1];
  w.appendChild(el('div', { 'class': 'pager' },
    el('button', { 'class': 'btn ghost', type: 'button', onclick: function () { go('#/u/' + U.n); } }, icon('back', 18), 'Unit ' + U.n),
    nk ? el('button', { 'class': 'btn ghost', type: 'button', onclick: function () { go('#/u/' + U.n + '/' + nk); } }, el('span', { 'class': 'ell' }, secByK(nk).name), icon('next', 18)) : null));
}

function pageSection(U, k, sub, sub2) {
  var s = secByK(k);
  if (sub === 'play') return pagePlay(U, k, +sub2 || 0);
  if (k === 'test' && sub === 'go') return pageTestRun(U);
  var w = page(s.c);
  crumbs(w, [['Unit ' + U.n, '#/u/' + U.n]]);
  if (k === 'grammar' && sub) { var g = U.grammar.filter(function (x) { return x.id === sub; })[0]; if (g) { pageGrammarTopic(w, U, g); return; } }
  secHead(w, s.name, s.c, s.ic, 'Unit ' + U.n + ' · ' + U.title);
  ({ words: secWords, practice: secSetList, gpractice: secSetList, grammar: secGrammar, classroom: secClassroom, reading: secReading, dialogue: secDialogue,
     wq: secSetList, writing: secWriting, games: secGames, puzzles: secPuzzles, test: secTest, cando: secCando })[k](w, U, k);
  pager(w, U, k);
}

/* the player page for set i of a section */
function pagePlay(U, k, i) {
  var s = secByK(k), sets = unitSets(U, k), set = sets[i];
  if (!set) { go('#/u/' + U.n + '/' + k); return; }
  var w = page(s.c);
  w.classList.add('play-wrap');
  var back = k === 'grammar' ? '#/u/' + U.n + '/grammar/' + U.grammar.filter(function (g) { return g.quick === set; })[0].id : '#/u/' + U.n + '/' + k;
  if (PLAY_FROM && PLAY_FROM.indexOf('#/u/' + U.n + '/grammar/') === 0 && k === 'gpractice') back = PLAY_FROM;
  var opts = { onClose: function () { go(back); } };
  if (k !== 'grammar' && i < sets.length - 1) opts.onNext = function () { go('#/u/' + U.n + '/' + k + '/play/' + (i + 1)); };
  if (k === 'reading') opts.text = { title: U.reading.title, text: U.reading.text };
  if (k === 'dialogue' && U.dialogue.intro) opts.intro = U.dialogue.intro;
  opts.onFinish = function () { touchStreak(); };
  w.appendChild(playSet(set, opts));
}
var PLAY_FROM = null;
function openPlay(U, k, i) { PLAY_FROM = location.hash; go('#/u/' + U.n + '/' + k + '/play/' + i); }

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
  var knownBadge = el('span', { 'class': 'badge purple' });
  function updKnown() { knownBadge.textContent = U.words.filter(function (x) { return S.words[x.id] === 'know'; }).length + ' / ' + U.words.length + ' known'; }
  updKnown();
  w.appendChild(el('div', { 'class': 'row between mb' }, seg, knownBadge));
  w.appendChild(body);
  function statusBtns(x, after) {
    return el('div', { 'class': 'half-btns' },
      el('button', { 'class': 'btn ' + (S.words[x.id] === 'learn' ? 'amber' : 'ghost'), type: 'button', onclick: function () { setWord(x.id, 'learn'); updKnown(); after(); } }, 'Still learning'),
      el('button', { 'class': 'btn ' + (S.words[x.id] === 'know' ? 'primary' : 'ghost'), type: 'button', onclick: function () { setWord(x.id, 'know'); updKnown(); after(); } }, icon('check', 18), 'I know it'));
  }
  if (mode === 'cards') {
    var i = 0;
    var draw = function () {
      clear(body);
      var x = U.words[i];
      var card = el('div', { 'class': 'wcard' + (S.words[x.id] ? ' ' + S.words[x.id] : '') },
        el('span', { 'class': 'badge purple cat' }, x.cat),
        el('div', { 'class': 'w' }, x.w),
        el('p', { 'class': 'def' }, rich(x.d)),
        el('p', { 'class': 'ex' }, rich(x.ex)));
      body.appendChild(card);
      body.appendChild(statusBtns(x, function () { if (i < U.words.length - 1) i++; draw(); }));
      body.appendChild(el('div', { 'class': 'row between mt8' },
        el('button', { 'class': 'icon-btn', type: 'button', 'aria-label': 'Previous word', disabled: i === 0, onclick: function () { i--; draw(); } }, icon('back', 22)),
        el('span', { 'class': 'sec' }, (i + 1) + ' / ' + U.words.length + ' · swipe'),
        el('button', { 'class': 'icon-btn', type: 'button', 'aria-label': 'Next word', disabled: i === U.words.length - 1, onclick: function () { i++; draw(); } }, icon('next', 22))));
      // swipe left / right
      var x0 = null;
      card.addEventListener('pointerdown', function (e) { x0 = e.clientX; });
      card.addEventListener('pointerup', function (e) {
        if (x0 === null) return; var dx = e.clientX - x0; x0 = null;
        if (dx < -50 && i < U.words.length - 1) { i++; draw(); } else if (dx > 50 && i > 0) { i--; draw(); }
      });
    };
    draw();
  } else {
    var lst = el('div', { 'class': 'wlist' });
    var cat = null;
    U.words.forEach(function (x) {
      if (x.cat !== cat) { cat = x.cat; lst.appendChild(el('h3', { 'class': 'label-h' }, cat)); }
      var row = el('div', { 'class': 'witem ' + (S.words[x.id] || '') });
      var fill = function () {
        clear(row); row.className = 'witem ' + (S.words[x.id] || '');
        row.appendChild(el('b', null, x.w)); row.appendChild(el('div', { 'class': 'sec small-t' }, rich(x.d)));
        row.appendChild(el('div', { 'class': 'small-t ex' }, rich(x.ex)));
        row.appendChild(statusBtns(x, fill));
      };
      fill();
      lst.appendChild(row);
    });
    body.appendChild(lst);
  }
}
function setList(w, U, k, sets, base) {
  var box = el('div', { 'class': 'set-list' });
  sets.forEach(function (s, i) { box.appendChild(setRow(s, i, function () { openPlay(U, k, (base || 0) + i); })); });
  w.appendChild(box);
}
function secSetList(w, U, k) {
  if (k === 'wq') w.appendChild(el('p', { 'class': 'sec' }, 'Read the answer. Write the question.'));
  setList(w, U, k, unitSets(U, k));
}

/* grammar */
function patternNode(rows) {
  var p = el('div', { 'class': 'pattern' + (rows.every(function (r) { return !r[0]; }) ? ' nocue' : '') });
  rows.forEach(function (r) {
    var row = el('div', { 'class': 'prow' });
    var cueName = r[0] === '+' ? 'positive' : r[0] === '?' ? 'question' : r[0] ? 'negative' : '';
    row.appendChild(el('span', { 'class': 'pcue' + (r[0] ? '' : ' empty'), 'aria-label': cueName || null }, r[0] === '+' ? icon('plus', 16) : r[0] === '?' ? '?' : r[0] ? icon('minus', 16) : ''));
    var blocks = el('span', { 'class': 'pblocks' });
    var first = r.slice(1).map(function (b) { return Array.isArray(b) ? b[0] : b; }).filter(Boolean)[0] || '';
    if (/^(Yes|No)\b/.test(first)) row.classList.add('short');
    var cls = ['s', 'v', 'r', 'r', 'r'];
    r.slice(1).forEach(function (b, i) {
      var txt = b, c = cls[i] || 'r';
      if (Array.isArray(b)) { txt = b[0]; c = b[1]; }
      if (txt) blocks.appendChild(el('span', { 'class': 'blk ' + c + (/^'/.test(txt) ? ' glue' : '') }, rich(txt)));
    });
    row.appendChild(blocks);
    p.appendChild(row);
  });
  return p;
}
function secGrammar(w, U) {
  var box = el('div', { 'class': 'set-list' });
  U.grammar.forEach(function (g) {
    var d = g.quick && setDone(g.quick);
    box.appendChild(el('button', { 'class': 'list-row sec-row' + (d ? ' done' : ''), type: 'button', onclick: function () { go('#/u/' + U.n + '/grammar/' + g.id); } },
      el('span', { 'class': 'ic purple' }, icon('grammar', 20, INK.purple)), el('span', { 'class': 'sr-t' }, el('b', null, g.title), el('span', { 'class': 'sec small-t' }, g.sets.length + ' practice sets')),
      d ? el('span', { 'class': 'tick' }, icon('check', 20)) : icon('next', 18)));
  });
  w.appendChild(box);
}
/* grammar card order: visual → pattern → In simple words (+ عربي) → examples → Watch out → Quick check → sets */
function pageGrammarTopic(w, U, g) {
  w.appendChild(el('header', { 'class': 'page-head' }, el('div', { 'class': 'ph-ic purple' }, icon('grammar', 26, INK.purple)),
    el('div', null, el('h1', null, g.title), el('p', { 'class': 'sec' }, 'Unit ' + U.n + ' · Grammar'))));
  var c = el('section', { 'class': 'gcard', id: 'gp-' + g.id });
  var v = renderVisual(g.visual); if (v) c.appendChild(v);
  if (g.pattern.length) { c.appendChild(el('h3', { 'class': 'label-h' }, 'The pattern')); c.appendChild(patternNode(g.pattern)); }
  if (g.note) c.appendChild(el('p', { 'class': 'sec' }, rich(g.note)));
  c.appendChild(enBlock(g.en, g.ar));
  c.appendChild(el('h3', { 'class': 'label-h' }, 'Examples'));
  c.appendChild(el('ul', { 'class': 'examples' }, g.examples.map(function (e) { return el('li', null, rich(e)); })));
  c.appendChild(el('div', { 'class': 'watch' }, el('h4', null, icon('cross', 18), 'Watch out!'), g.watch.map(function (x) {
    return el('div', { 'class': 'wr' }, el('span', { 'class': 'wrong-t' }, x[0]), el('span', { 'class': 'arrow', 'aria-hidden': 'true' }, '→'), el('span', { 'class': 'right-t' }, x[1]));
  })));
  w.appendChild(c);
  var qi = unitSets(U, 'grammar').indexOf(g.quick);
  if (g.quick) w.appendChild(el('button', { 'class': 'btn primary block', type: 'button', onclick: function () { openPlay(U, 'grammar', qi); } }, icon('choose', 20), 'Quick check · 3 questions', setDone(g.quick) ? el('span', { 'class': 'badge ok' }, fmtScore(S.sets[g.quick.id].best) + ' / 3') : null));
  w.appendChild(el('h2', { 'class': 'label-h mt' }, 'Practice sets'));
  var all = unitSets(U, 'gpractice'), base = all.indexOf(g.sets[0]);
  setList(w, U, 'gpractice', g.sets, base);
  var gi = U.grammar.indexOf(g), ng = U.grammar[gi + 1];
  w.appendChild(el('div', { 'class': 'pager' },
    el('button', { 'class': 'btn ghost', type: 'button', onclick: function () { go('#/u/' + U.n + '/grammar'); } }, icon('back', 18), 'Grammar'),
    ng ? el('button', { 'class': 'btn ghost', type: 'button', onclick: function () { go('#/u/' + U.n + '/grammar/' + ng.id); } }, el('span', { 'class': 'ell' }, 'Next: ' + ng.title), icon('next', 18)) : null));
}

/* classroom */
function phraseList(ps) { return el('ul', { 'class': 'phrases' }, ps.map(function (p) { return el('li', null, el('b', null, p.p), el('span', { 'class': 'sec small-t' }, p.s)); })); }
function secClassroom(w, U, k) {
  var st = U.cls.phrases.filter(function (p) { return p.who === 'S'; }), te = U.cls.phrases.filter(function (p) { return p.who === 'T'; });
  var c = el('section', { 'class': 'card' });
  if (st.length) { c.appendChild(el('h3', { 'class': 'label-h' }, 'You say')); c.appendChild(phraseList(st)); }
  if (te.length) { c.appendChild(el('h3', { 'class': 'label-h' }, 'Your teacher says')); c.appendChild(phraseList(te)); }
  w.appendChild(c);
  setList(w, U, k, U.cls.sets);
  w.appendChild(el('button', { 'class': 'list-row sec-row', type: 'button', onclick: function () { go('#/u/' + U.n + '/games/cls'); } },
    el('span', { 'class': 'ic amber' }, icon('games', 20, INK.amber)), el('span', { 'class': 'sr-t' }, el('b', null, 'Game: Classroom Speed Round'), el('span', { 'class': 'sec small-t' }, '60 seconds')), icon('next', 18)));
}

/* reading: Text / Questions switch on phones, side by side on wide screens */
function readingText(R) {
  var panel = el('article', { 'class': 'textpanel', tabindex: '0', 'aria-label': 'Reading text' }, el('h2', null, R.title));
  R.text.split(/\n\s*\n/).forEach(function (p) { panel.appendChild(el('p', null, rich(p.trim()))); });
  return panel;
}
function secReading(w, U, k) {
  var R = U.reading;
  var view = S.readView || 'text';
  var seg = el('div', { 'class': 'seg only-phone', role: 'group', 'aria-label': 'Show' });
  var lay = el('div', { 'class': 'read-lay show-' + view });
  ['text', 'questions'].forEach(function (m) {
    seg.appendChild(el('button', { type: 'button', 'aria-pressed': String(view === m), onclick: function () {
      view = m; S.readView = m; save(); lay.className = 'read-lay show-' + m;
      seg.querySelectorAll('button').forEach(function (b, j) { b.setAttribute('aria-pressed', String((j === 0) === (m === 'text'))); });
    } }, m === 'text' ? 'Text' : 'Questions'));
  });
  w.appendChild(seg);
  var qs = el('div', { 'class': 'read-q' }, el('h2', { 'class': 'label-h' }, 'Questions'));
  setList(qs, U, k, R.sets);
  lay.appendChild(readingText(R)); lay.appendChild(qs);
  w.appendChild(lay);
}

/* dialogue */
function secDialogue(w, U, k) {
  var D = U.dialogue;
  w.appendChild(el('section', { 'class': 'card' }, el('h2', null, D.title), D.intro ? el('p', { 'class': 'sec' }, rich(D.intro)) : null,
    el('p', { 'class': 'sec small-t' }, D.task === 'order' ? 'Put the lines in order.' : 'Complete the dialogue. Then read it with a partner.')));
  setList(w, U, k, D.sets);
}

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
    var c = el('section', { 'class': 'card' }, el('h2', null, 'Task ' + (i + 1)), el('p', null, rich(t2.task)));
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

/* games */
function secGames(w, U) {
  var g = el('div', { 'class': 'set-list' });
  U.games.list.forEach(function (k) {
    var info = GAME_INFO[k];
    var best = S.games[bestKey('u' + U.n, k)];
    g.appendChild(el('button', { 'class': 'list-row sec-row', type: 'button', onclick: function () { go('#/u/' + U.n + '/games/' + k); } },
      el('span', { 'class': 'ic amber' }, icon('games', 20, INK.amber)),
      el('span', { 'class': 'sr-t' }, el('b', null, info.name), el('span', { 'class': 'sec small-t' }, info.d)),
      best !== undefined ? el('span', { 'class': 'badge amber' }, bestLabel(k, best)) : icon('next', 18)));
  });
  w.appendChild(g);
  w.appendChild(el('p', { 'class': 'sec small-t mt' }, 'On a projector? Choose "2 teams". The teacher taps the team that answers. Memory and Balloon Spelling keep the score by themselves.'));
}
function pageGame(U, k) {
  var w = page('amber');
  crumbs(w, [k === 'cls' ? ['Classroom English', '#/u/' + U.n + '/classroom'] : ['Games', '#/u/' + U.n + '/games']]);
  w.appendChild(gameShell(k, 'u' + U.n, function (ctx) { GAMES[k](ctx, U); }));
}
function secPuzzles(w, U) {
  if (typeof puzzleList === 'function') puzzleList(w, U);
}

/* test: start screen, then the test player */
function secTest(w, U) {
  var best = S.tests[U.n];
  var c = el('section', { 'class': 'card test-intro' },
    el('p', { 'class': 'label' }, U.test.length + ' questions · no hints'),
    el('p', null, 'One question at a time. You can go back with the numbers. You see your score and your mistakes at the end.'));
  if (best !== undefined) c.appendChild(el('div', { 'class': 'row' }, el('span', { 'class': 'badge ok' }, 'Your best: ' + best + '%'), starsText(starsFor(best))));
  c.appendChild(el('button', { 'class': 'btn primary block mt', type: 'button', onclick: function () { go('#/u/' + U.n + '/test/go'); } }, best === undefined ? 'Start the test' : 'Take it again', icon('next', 18)));
  w.appendChild(c);
}
function pageTestRun(U) {
  var w = page('coral');
  w.classList.add('play-wrap');
  w.appendChild(renderTest(U.test, { title: 'Unit ' + U.n + ' test', onClose: function () { go('#/u/' + U.n + '/test'); },
    onDone: function (pct) { S.tests[U.n] = Math.max(S.tests[U.n] || 0, pct); touchStreak(); save(); } }));
}
function secCando(w, U) {
  var c = el('section', { 'class': 'card' }, el('h2', null, 'Tick what you can do now.'));
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
  var w = page('amber');
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
    } else {
      // a word with no question: the learner removes it by saying they know it
      card.appendChild(el('div', { 'class': 'wcard' }, el('div', { 'class': 'w' }, P.word.w), el('p', null, rich(P.word.d)),
        el('button', { 'class': 'btn', type: 'button', onclick: function () { delete S.pile[key]; S.words[P.word.id] = 'know'; save(); toast('Out of the pile!'); show(); } }, icon('check', 18), ' I know it now')));
    }
    var nextBtn = el('button', { 'class': 'btn mt8', type: 'button', disabled: !!P.item, onclick: function () { k++; show(); } }, 'Next', icon('next', 18));
    card.appendChild(nextBtn);
    box.appendChild(card);
  }
  show();
}
function pageMistakes(sub) {
  var w = page('coral');
  crumbs(w, sub ? [['Mistakes', '#/mistakes']] : [['Home', '#/']]);
  var ids = []; S.mistakes.forEach(function (m) { if (ITEMS[m.id] && ids.indexOf(m.id) < 0) ids.push(m.id); });
  if (sub === 'play' && ids.length) {
    w.classList.add('play-wrap');
    w.appendChild(playSet({ id: 'mistakes', k: 'mix', instr: 'Practise your mistakes.', items: ids.slice(0, 10) }, { noSave: true, onClose: function () { go('#/mistakes'); } }));
    return;
  }
  secHead(w, 'Mistake Notebook', 'coral', 'notebook', 'Your wrong answers and the right ones. Read them before a test.');
  if (!S.mistakes.length) { w.appendChild(el('div', { 'class': 'empty' }, icon('check', 32, INK.teal), el('p', null, 'No mistakes saved yet. When you get a question wrong, it comes here.'))); return; }
  if (ids.length) w.appendChild(el('button', { 'class': 'btn primary block mb', type: 'button', onclick: function () { go('#/mistakes/play'); } }, 'Practise my mistakes', icon('next', 18)));
  var clr = el('button', { 'class': 'btn ghost', type: 'button' }, 'Clear the notebook');
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
  if (sub === 'boss') {
    var wb = page('amber');
    crumbs(wb, [['Level Review', '#/review']]);
    wb.appendChild(gameShell('boss', 'level', function (ctx) { GAMES.boss(ctx, DATA.boss); }));
    return;
  }
  if (sub === 'go') {
    var wg = page('coral');
    wg.classList.add('play-wrap');
    wg.appendChild(renderTest(DATA.review, { title: 'Level Review', onClose: function () { go('#/review'); },
      onDone: function (pct) { S.tests.review = Math.max(S.tests.review || 0, pct); touchStreak(); save(); } }));
    return;
  }
  var w = page('coral');
  crumbs(w, [['Home', '#/']]);
  secHead(w, 'Level Review', 'coral', 'review', DATA.review.length + ' questions from every unit.');
  var best = S.tests.review;
  var c = el('section', { 'class': 'card test-intro' }, el('p', { 'class': 'label' }, DATA.review.length + ' questions · no hints'),
    el('p', null, 'Questions from all the units. You see your score and your mistakes at the end.'));
  if (best !== undefined) c.appendChild(el('div', { 'class': 'row' }, el('span', { 'class': 'badge ok' }, 'Your best: ' + best + '%'), starsText(starsFor(best))));
  c.appendChild(el('button', { 'class': 'btn primary block mt', type: 'button', onclick: function () { go('#/review/go'); } }, 'Start the Level Review', icon('next', 18)));
  w.appendChild(c);
  w.appendChild(el('button', { 'class': 'list-row sec-row', type: 'button', onclick: function () { go('#/review/boss'); } },
    el('span', { 'class': 'ic amber' }, icon('games', 20, INK.amber)), el('span', { 'class': 'sr-t' }, el('b', null, 'Boss Battle'), el('span', { 'class': 'sec small-t' }, 'Beat the Grammar Giant with questions from the whole level.')),
    S.games['level:boss'] !== undefined ? el('span', { 'class': 'badge amber' }, bestLabel('boss', S.games['level:boss'])) : icon('next', 18)));
}
function pageProgress() {
  var w = page('teal');
  crumbs(w, [['Home', '#/']]);
  secHead(w, 'Progress', 'teal', 'progress');
  var totalSets = 0, doneSets = 0;
  UNITS.forEach(function (U) { SECTIONS.forEach(function (s) { unitSets(U, s.k).forEach(function (st) { totalSets++; if (setDone(st)) doneSets++; }); }); });
  var known = 0; UNITS.forEach(function (U) { U.words.forEach(function (x) { if (S.words[x.id] === 'know') known++; }); });
  var nw = UNITS.reduce(function (a, U) { return a + U.words.length; }, 0);
  var pz = 0, pzN = 0; UNITS.forEach(function (U) { (U.puzzles || []).forEach(function (p) { pzN++; if (S.puzzles[p.id] && S.puzzles[p.id].done) pz++; }); });
  w.appendChild(el('div', { 'class': 'stat-grid mb' },
    el('div', { 'class': 'stat' }, el('b', null, String(streakNow())), 'days in a row'),
    el('div', { 'class': 'stat' }, el('b', null, doneSets + '/' + totalSets), 'sets done'),
    el('div', { 'class': 'stat' }, el('b', null, known + '/' + nw), 'words known'),
    pzN ? el('div', { 'class': 'stat' }, el('b', null, pz + '/' + pzN), 'puzzles solved') : null,
    el('div', { 'class': 'stat' }, el('b', null, String(Object.keys(S.pile).length)), 'in Review Pile')));
  UNITS.forEach(function (U) {
    var pct = unitPct(U);
    var c = el('section', { 'class': 'card' },
      el('div', { 'class': 'row between' }, el('b', null, 'Unit ' + U.n + ': ' + U.title), S.tests[U.n] !== undefined ? starsText(unitStars(U.n)) : el('span', { 'class': 'sec small-t' }, 'test not taken')),
      el('div', { 'class': 'pbar' }, el('i', { style: 'width:' + pct + '%' })),
      el('div', { 'class': 'chips mt8' }, unitSecs(U).map(function (k) { var d = secDone(U, k); return el('span', { 'class': 'chip' + (d ? ' on' : '') }, d ? icon('check', 14) : null, secByK(k).name); })));
    if (U.puzzles && U.puzzles.length) c.appendChild(el('div', { 'class': 'chips mt8' }, U.puzzles.map(function (p) { var r = S.puzzles[p.id]; return el('span', { 'class': 'chip' + (r && r.done ? ' on' : '') }, p.title, r && r.done ? ' · ' + r.stars + '★' : ''); })));
    w.appendChild(c);
  });
}

function pageVerbs() {
  var w = page('purple');
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
    var tb = el('table', { 'class': 'vtable card verbs' });
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
  var w = page('teal');
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
      var sl = el('div', { 'class': 'slide' }, el('h2', null, s.h), smartArt(s.v), el('p', null, rich(s.t)));
      if (s.ar) { var t = arToggle([s.ar]); sl.appendChild(el('div', { 'class': 'row', style: 'justify-content:center' }, t.pill)); sl.appendChild(t.box); }
      box.appendChild(sl);
      applyArabic();
      var dots = el('div', { 'class': 'dots' }); tip.slides.forEach(function (_, k) { dots.appendChild(el('i', { 'class': k === i ? 'on' : '' })); });
      box.appendChild(dots);
      box.appendChild(el('div', { 'class': 'row between mt8' },
        el('button', { 'class': 'btn ghost', type: 'button', disabled: i === 0, onclick: function () { i--; draw(); } }, icon('back', 18), 'Back'),
        i < tip.slides.length - 1 ? el('button', { 'class': 'btn', type: 'button', onclick: function () { i++; draw(); } }, 'Next', icon('next', 18))
          : el('button', { 'class': 'btn', type: 'button', onclick: function () { S.slides[tip.id] = 1; save(); go('#/smarter'); } }, 'Done', icon('check', 18))));
    };
    draw();
    return;
  }
  crumbs(w, [['Home', '#/']]);
  secHead(w, 'Learn Smarter', 'teal', 'smarter', 'Short tips with mini presentations.');
  var g = el('div', { 'class': 'set-list' });
  DATA.smarter.forEach(function (tip) {
    g.appendChild(el('button', { 'class': 'list-row sec-row', type: 'button', onclick: function () { go('#/smarter/' + tip.id); } },
      el('span', { 'class': 'ic teal' }, icon(tip.icon && ICON_PATHS[tip.icon] ? tip.icon : 'smarter', 20, INK.teal)), el('span', { 'class': 'sr-t' }, el('b', null, tip.title), el('span', { 'class': 'sec small-t' }, tip.summary)), S.slides[tip.id] ? el('span', { 'class': 'badge ok' }, icon('check', 14), 'seen') : null));
  });
  w.appendChild(g);
}
function pageResources() {
  var w = page('teal');
  crumbs(w, [['Home', '#/']]);
  secHead(w, 'Resources', 'teal', 'resources', 'Useful websites and apps. They open outside this app and need the internet.');
  DATA.resources.forEach(function (r) {
    w.appendChild(el('section', { 'class': 'card' }, el('div', { 'class': 'row between' }, el('b', null, r.name), el('span', { 'class': 'badge' }, r.kind)),
      el('p', { 'class': 'sec' }, r.what), el('a', { href: r.url, target: '_blank', rel: 'noopener noreferrer', 'class': 'btn small ghost' }, r.url.replace(/^https?:\/\//, ''))));
  });
}
function pageClassroom() {
  var w = page('teal');
  crumbs(w, [['Home', '#/']]);
  secHead(w, 'Classroom English', 'teal', 'classroom', 'All the classroom phrases for this level.');
  var seg = el('div', { 'class': 'seg mb', role: 'group', 'aria-label': 'Show' });
  var box = el('div');
  var tabs = [['S', 'You say'], ['T', 'Your teacher says']];
  function show(who) {
    seg.querySelectorAll('button').forEach(function (b, j) { b.setAttribute('aria-pressed', String(tabs[j][0] === who)); });
    clear(box);
    var seen = {};
    UNITS.forEach(function (U, k) {
      var ps = U.cls.phrases.filter(function (p) { return p.who === who && !seen[p.p]; });
      ps.forEach(function (p) { seen[p.p] = 1; });
      if (ps.length) box.appendChild(el('details', { 'class': 'card fold', open: k === 0 ? true : null }, el('summary', null, el('b', null, 'Unit ' + U.n + ' · ' + U.title), el('span', { 'class': 'badge' }, String(ps.length))), phraseList(ps)));
    });
    var rest = DATA.classroom.filter(function (p) { return p.who === who && !seen[p.p]; });
    if (rest.length) box.appendChild(el('details', { 'class': 'card fold' }, el('summary', null, el('b', null, 'More phrases'), el('span', { 'class': 'badge' }, String(rest.length))), phraseList(rest)));
  }
  tabs.forEach(function (t) { seg.appendChild(el('button', { type: 'button', onclick: function () { show(t[0]); } }, t[1])); });
  w.appendChild(seg); w.appendChild(box);
  show('S');
}

function pageGrammarIndex() {
  var w = page('purple');
  crumbs(w, [['Home', '#/']]);
  secHead(w, 'Grammar index', 'purple', 'grammar', 'Every grammar topic in this level.');
  w.appendChild(grammarIndex());
}

/* ---------- router ---------- */
function render() { renderPage(); applyArabic(); }
function renderPage() {
  var h = location.hash || '#/';
  var p = h.replace(/^#\/?/, '').split('/').filter(Boolean);
  window.scrollTo(0, 0);
  if (!p.length) return pageHome();
  if (p[0] === 'u') {
    var U = unitByN(+p[1]);
    if (!U) return pageHome();
    if (p.length === 2) { S.last = h; save(); return pageUnit(U); }
    if (p[2] === 'games' && p[3]) { S.last = h; save(); return pageGame(U, p[3]); }
    if (p[2] === 'puzzles' && p[3] && typeof pagePuzzle === 'function') { S.last = h; save(); return pagePuzzle(U, p[3]); }
    if (secByK(p[2]) && hasSec(U, p[2])) { S.last = h; save(); return pageSection(U, p[2], p[3], p[4]); }
    return pageUnit(U);
  }
  switch (p[0]) {
    case 'pile': return pagePile();
    case 'mistakes': return pageMistakes(p[1]);
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
var ALLSETS = {};
UNITS.forEach(function (U) { SECTIONS.forEach(function (s) { unitSets(U, s.k).forEach(function (st) { ALLSETS[st.id] = { set: st, U: U, k: s.k }; }); }); });
window.__APP = {
  data: DATA, norm: norm, matches: matches,
  go: function (h) { if (location.hash !== h) history.replaceState(null, '', h); render(); return MAIN.innerText.length; },
  state: function () { return JSON.parse(JSON.stringify(S)); },
  sets: function () { return Object.keys(ALLSETS); },
  setInfo: function (sid) { var x = ALLSETS[sid]; return x ? { unit: x.U.n, sec: x.k, i: unitSets(x.U, x.k).indexOf(x.set), n: x.set.items.length, k: x.set.k } : null; },
  // open a set in the player and answer it: mask(i) = right/wrong for answer i
  playSet: function (sid, wrongAt) {
    var x = ALLSETS[sid]; if (!x) return null;
    var i = unitSets(x.U, x.k).indexOf(x.set);
    this.go('#/u/' + x.U.n + '/' + x.k + '/play/' + i);
    var sc = SETREG[sid]; if (!sc) return 'no player';
    sc.autoplay(function (k) { return (wrongAt || []).indexOf(k) < 0; });
    return { finished: sc.finished, score: sc.score, n: x.set.items.length, saved: S.sets[sid] || null };
  },
  items: function () { return Object.keys(REG); },
  answer: function (id, ok) { var c = REG[id]; if (!c) return 'missing'; c.autoAnswer(ok); return c.done; },
  item: function (id) { var c = REG[id]; return c ? { done: c.done, score: c.score, tries: c.tries } : null; },
  setScore: function (id) { var s = SETREG[id]; return s ? { finished: !!s.finished, score: s.score, n: s.ctls.length } : null; },
  testBox: function () { var b = MAIN.querySelector('.player.test'); return b ? b.__ctls.map(function (c) { return c.id; }) : null; },
  testAnswer: function (k, ok) { var b = MAIN.querySelector('.player.test'); var c = b.__ctls[k]; c.autoAnswer(ok); return c.answered; },
  testFinish: function () { var b = MAIN.querySelector('.player.test'); b.__finish(); var h = document.querySelector('#test-results h2'); return h ? h.innerText : null; },
  sections: SECTIONS.map(function (s) { return s.k; }),
  storeOk: function () { return STORE_OK; },
  mount: function (id) { clear(MAIN); var c = makeItem(id, 1, 'practice', null); MAIN.appendChild(c.node); return true; },
  answerText: function (id, v) { var c = REG[id]; if (!c || !c.answerText) return 'no answerText'; c.answerText(v); return { done: c.done, score: c.score }; },
  attempts: function (id) { return S.items[id] ? JSON.parse(JSON.stringify(S.items[id])) : null; },
  itemData: function (id) { return ITEMS[id] || null; },
  findItem: function (t) { for (var id in ITEMS) if (ITEMS[id].t === t && !S.items[id]) return id; return null; },
  pileKeys: function () { return Object.keys(S.pile); },
  setPile: function (k, v) { if (v === undefined) delete S.pile[k]; else S.pile[k] = v; save(); },
  pilePrompt: function (k) { var p = pilePrompt(k); return p ? { item: p.item || null, word: p.word ? p.word.id : null } : null; },
  fixItem: function () { for (var id in ITEMS) if (ITEMS[id].t === 'fix' && ITEMS[id].fulls && ITEMS[id].fulls[0].split(' ').length > 3) return { id: id, full: ITEMS[id].fulls[0], acc: ITEMS[id].acc }; return null; }
};

/* B3: drop pile keys that point at nothing, so every key on the pile can be cleared */
(function () { var n = 0; Object.keys(S.pile).forEach(function (k) { if (!pilePrompt(k)) { delete S.pile[k]; n++; } }); if (n) save(); })();
applyClassMode();
render();
