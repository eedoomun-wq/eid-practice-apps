/* ===== puzzles.js: the case, word puzzles, escape room, guess the word + What am I? ===== */
var PUZ_ICON = { case: 'review', words: 'words', escape: 'lock', guess: 'bulb' };
var PZ_CUR = null; // live puzzle controller (test hook)

function puzzleStars(uid) { var r = S.puzzles[uid]; return r ? r.stars || 0 : 0; }
/* a puzzle (or one part of it) is solved with n stars; the puzzle keeps the best */
function savePuzzle(P, part, stars, parts) {
  var r = S.puzzles[P.uid] || (S.puzzles[P.uid] = { done: 0, stars: 0, parts: {} });
  r.parts = r.parts || {};
  var key = part || 'main';
  r.parts[key] = Math.max(r.parts[key] || 0, stars);
  var need = parts || ['main'];
  if (need.every(function (k) { return r.parts[k] !== undefined; })) {
    r.done = 1;
    r.stars = Math.min.apply(null, need.map(function (k) { return r.parts[k]; }));
  }
  touchStreak(); save();
}
function puzzleHash(s) {
  var h = 5381, t = String(s).toUpperCase();
  for (var i = 0; i < t.length; i++) h = ((h * 33) + t.charCodeAt(i)) >>> 0;
  return h;
}

/* ---------- Puzzles section: 4 cards ---------- */
function puzzleList(w, U) {
  var box = el('div', { 'class': 'set-list' });
  (U.puzzles || []).forEach(function (P) {
    var r = S.puzzles[P.uid];
    box.appendChild(el('button', { 'class': 'list-row sec-row' + (r && r.done ? ' done' : ''), type: 'button', onclick: function () { go('#/u/' + U.n + '/puzzles/' + P.id); } },
      el('span', { 'class': 'ic amber' }, icon(PUZ_ICON[P.kind] || 'puzzle', 20, INK.amber)),
      el('span', { 'class': 'sr-t' }, el('b', null, P.title), el('span', { 'class': 'sec small-t' }, P.type)),
      r && r.done ? starsText(r.stars) : icon('next', 18)));
  });
  w.appendChild(box);
  w.appendChild(el('p', { 'class': 'sec small-t' }, 'Each puzzle has 2 hints. A hint costs a star.'));
}

function pagePuzzle(U, id) {
  var P = (U.puzzles || []).filter(function (p) { return p.id === id; })[0];
  if (!P) { go('#/u/' + U.n + '/puzzles'); return; }
  var w = page('amber');
  crumbs(w, [['Puzzles', '#/u/' + U.n + '/puzzles']]);
  w.appendChild(puzzleShell(P, U));
}

/* shell: title, Solo / 2 teams, stars and hints */
function puzzleShell(P, U) {
  var card = el('section', { 'class': 'card puzzle', id: 'pz-' + P.id });
  var team = !!S.classMode;
  var seg = el('div', { 'class': 'seg', role: 'group', 'aria-label': 'Mode' });
  var bSolo = el('button', { type: 'button', 'aria-pressed': String(!team) }, 'Solo');
  var bTeam = el('button', { type: 'button', 'aria-pressed': String(team) }, '2 teams');
  seg.appendChild(bSolo); seg.appendChild(bTeam);
  card.appendChild(el('div', { 'class': 'game-bar' }, el('div', null, el('p', { 'class': 'label', style: 'margin:0' }, P.type), el('h2', { style: 'margin:0' }, P.title)), seg));
  var stage = el('div');
  card.appendChild(stage);
  var T = { a: 0, b: 0, turn: 'a' };
  var ctx = { P: P, U: U, stage: stage, T: T };
  ctx.drawTeams = function () {
    if (!ctx.team) return null;
    var n = el('div', { 'class': 'teams' },
      el('div', { 'class': 'team a' + (T.turn === 'a' ? ' turn' : '') }, 'Team A', el('span', null, String(T.a))),
      el('div', { 'class': 'team b' + (T.turn === 'b' ? ' turn' : '') }, 'Team B', el('span', null, String(T.b))));
    if (ctx.teamsNode && ctx.teamsNode.parentNode) ctx.teamsNode.parentNode.replaceChild(n, ctx.teamsNode);
    ctx.teamsNode = n;
    return n;
  };
  ctx.point = function (t, n) { T[t] += (n || 1); T.turn = t === 'a' ? 'b' : 'a'; ctx.drawTeams(); };
  /* the minimal teacher bar: one tick per team and one cross */
  ctx.teacherBar = function (onPick, label) {
    return el('div', { 'class': 'teacher-bar', 'aria-label': 'Teacher bar' },
      label ? el('span', { 'class': 'sec small-t', style: 'flex:0 0 100%;text-align:center' }, label) : null,
      el('button', { 'class': 'btn', type: 'button', onclick: function () { onPick('a'); } }, icon('check', 18), ' Team A'),
      el('button', { 'class': 'btn purple', type: 'button', onclick: function () { onPick('b'); } }, icon('check', 18), ' Team B'),
      el('button', { 'class': 'btn ghost', type: 'button', 'aria-label': 'Nobody', onclick: function () { onPick(null); } }, icon('cross', 18), ' Nobody'));
  };
  /* hints: 2 per puzzle (or per part), each costs a star */
  ctx.hintsUsed = {};
  ctx.stars = function (part) { return 3 - (ctx.hintsUsed[part || 'main'] || 0); };
  ctx.hintButton = function (part, onHint) {
    var key = part || 'main';
    var starBox = el('span', { 'class': 'pz-stars' });
    var b = el('button', { 'class': 'btn ghost small', type: 'button' }, icon('bulb', 18), 'Hint');
    function draw() {
      clear(starBox); starBox.appendChild(starsText(ctx.stars(key)));
      var left = 2 - (ctx.hintsUsed[key] || 0);
      b.disabled = left <= 0;
      b.lastChild.textContent = left > 0 ? 'Hint (' + left + ' left)' : 'No hints left';
    }
    b.addEventListener('click', function () {
      if ((ctx.hintsUsed[key] || 0) >= 2) return;
      if (!b.dataset.sure) { b.dataset.sure = '1'; b.lastChild.textContent = 'A hint costs a star. Tap again.'; return; }
      delete b.dataset.sure;
      ctx.hintsUsed[key] = (ctx.hintsUsed[key] || 0) + 1;
      draw();
      onHint(ctx.hintsUsed[key]);
    });
    draw();
    return el('div', { 'class': 'pz-hintbar' }, starBox, b);
  };
  function start() {
    clear(stage); T.a = 0; T.b = 0; T.turn = 'a'; ctx.team = team; ctx.hintsUsed = {}; ctx.teamsNode = null;
    PUZZLES[P.kind](ctx);
  }
  bSolo.addEventListener('click', function () { team = false; bSolo.setAttribute('aria-pressed', 'true'); bTeam.setAttribute('aria-pressed', 'false'); start(); });
  bTeam.addEventListener('click', function () { team = true; bTeam.setAttribute('aria-pressed', 'true'); bSolo.setAttribute('aria-pressed', 'false'); start(); });
  ctx.restart = start;
  start();
  return card;
}
function solvedBox(title, lines, stars, again) {
  var b = el('div', { 'class': 'pz-solved' }, celebrate(), el('h3', null, title));
  lines.forEach(function (l) { if (l) b.appendChild(typeof l === 'string' ? el('p', null, rich(l)) : l); });
  if (stars !== undefined) b.appendChild(starsText(stars));
  if (again) b.appendChild(el('button', { 'class': 'btn ghost mt8', type: 'button', onclick: again }, 'Play again'));
  return b;
}

var PUZZLES = {};

/* ---------- P1 the case: elimination grid ---------- */
PUZZLES.case = function (ctx) {
  var P = ctx.P, st = ctx.stage;
  if (ctx.team) st.appendChild(ctx.drawTeams());
  st.appendChild(el('p', { 'class': 'pz-story' }, rich(P.story)));
  var clues = el('ol', { 'class': 'pz-clues' });
  P.clues.forEach(function (c) {
    var li = el('li', null, el('button', { type: 'button', 'class': 'clue-btn', 'aria-pressed': 'false', onclick: function (e) {
      var on = e.currentTarget.getAttribute('aria-pressed') !== 'true'; e.currentTarget.setAttribute('aria-pressed', String(on));
    } }, rich(c)));
    clues.appendChild(li);
  });
  st.appendChild(el('h3', { 'class': 'label-h' }, 'Clues'));
  st.appendChild(clues);
  st.appendChild(el('p', { 'class': 'sec small-t' }, 'Tap a box: blank → ✗ → ✓. A ✓ greys out its row and column.'));
  // one block per group: people × values
  var cells = {}; // key person|value -> {b, s}
  var gridBox = el('div', { 'class': 'pz-grids' });
  P.groups.forEach(function (g, gi) {
    var tb = el('table', { 'class': 'pz-grid' });
    var head = el('tr', null, el('th', { scope: 'col' }, P.gnames[gi] || ''));
    g.forEach(function (v) { head.appendChild(el('th', { scope: 'col' }, v)); });
    tb.appendChild(head);
    P.people.forEach(function (p) {
      var tr = el('tr', null, el('th', { scope: 'row' }, p));
      g.forEach(function (v) {
        var c = { s: 0, p: p, v: v, g: gi };
        c.b = el('button', { type: 'button', 'class': 'gcell', 'aria-label': p + ' and ' + v + ': blank', onclick: function () { c.s = (c.s + 1) % 3; draw(); } });
        cells[p + '|' + v] = c;
        tr.appendChild(el('td', null, c.b));
      });
      tb.appendChild(tr);
    });
    gridBox.appendChild(tb);
  });
  st.appendChild(gridBox);
  function draw() {
    var ticks = Object.keys(cells).map(function (k) { return cells[k]; }).filter(function (c) { return c.s === 2; });
    Object.keys(cells).forEach(function (k) {
      var c = cells[k];
      var grey = c.s === 0 && ticks.some(function (t) { return t.g === c.g && (t.p === c.p || t.v === c.v); });
      c.b.className = 'gcell' + (c.s === 1 ? ' x' : c.s === 2 ? ' ok' : '') + (grey ? ' grey' : '');
      clear(c.b);
      if (c.s === 1) c.b.appendChild(icon('cross', 18)); else if (c.s === 2) c.b.appendChild(icon('check', 20));
      c.b.setAttribute('aria-label', c.p + ' and ' + c.v + ': ' + (c.s === 1 ? 'no' : c.s === 2 ? 'yes' : grey ? 'no (greyed out)' : 'blank'));
    });
  }
  draw();
  st.appendChild(ctx.hintButton('main', function (n) {
    var h = P.hints[n - 1]; if (!h) return;
    var pv = h.split(' → '), c = cells[pv[0] + '|' + pv[1]];
    if (c) { c.s = 2; draw(); }
    toast('Hint: ' + h);
    hintLine.textContent = 'Hints: ' + P.hints.slice(0, n).join(' · ');
  }));
  var hintLine = el('p', { 'class': 'sec small-t' });
  st.appendChild(hintLine);
  // the final question
  var q = el('div', { 'class': 'pz-final' }, el('h3', null, rich(P.q)));
  var opts = el('div', { 'class': 'opts grid2' });
  var res = el('div');
  var done = false;
  P.opts.o.forEach(function (o, i) {
    var b = el('button', { 'class': 'opt', type: 'button', onclick: function () { answer(i, b); } }, el('span', { 'class': 'abc' }, 'ABCD'.charAt(i)), o);
    opts.appendChild(b);
  });
  q.appendChild(opts); q.appendChild(res);
  st.appendChild(q);
  if (ctx.team) st.appendChild(ctx.teacherBar(function (t) { if (t) ctx.point(t, 3); else { T.turn = T.turn === 'a' ? 'b' : 'a'; ctx.drawTeams(); } }, 'Who solved the case?'));
  var T = ctx.T;
  function answer(i, b) {
    if (done) return;
    if (i !== P.opts.a) { b.classList.add('wrong'); anim(b, 'shake'); toast('Not yet. Check the grid again.'); return; }
    done = true;
    b.classList.add('right');
    var stars = ctx.stars();
    savePuzzle(P, 'main', stars);
    clear(res);
    res.appendChild(solvedBox('Case solved!', [P.reveal], stars));
  }
  PZ_CUR = { solve: function () { answer(P.opts.a, opts.children[P.opts.a]); return done; } };
};

/* ---------- P2 word puzzles: crossword + word search ---------- */
PUZZLES.words = function (ctx) {
  var P = ctx.P, st = ctx.stage;
  if (ctx.team) st.appendChild(ctx.drawTeams());
  var seg = el('div', { 'class': 'seg mb', role: 'group', 'aria-label': 'Puzzle' });
  var box = el('div');
  var parts = [['cw', 'Crossword'], ['ws', 'Word search']];
  var api = {};
  function show(k) {
    seg.querySelectorAll('button').forEach(function (b, j) { b.setAttribute('aria-pressed', String(parts[j][0] === k)); });
    clear(box);
    (k === 'cw' ? crossword : wordsearch)(box);
  }
  parts.forEach(function (p) { seg.appendChild(el('button', { type: 'button', onclick: function () { show(p[0]); } }, p[1])); });
  st.appendChild(seg); st.appendChild(box);
  if (ctx.team) st.appendChild(ctx.teacherBar(function (t) { if (t) ctx.point(t); }, 'A team finds a word? Give a point.'));

  function crossword(host) {
    var cw = P.cw, grid = {}, active = 0, done = false;
    cw.entries.forEach(function (e, k) {
      for (var i = 0; i < e.ans.length; i++) {
        var r = e.r + (e.d === 'd' ? i : 0), c = e.c + (e.d === 'a' ? i : 0), key = r + ',' + c;
        var g = grid[key] || (grid[key] = { r: r, c: c, ch: e.ans[i], v: '', ents: [] });
        g.ents.push(k);
      }
    });
    var cellPx = 'min(' + (100 / cw.w) + 'cw, 40px)';
    var gEl = el('div', { 'class': 'cw-grid', style: 'grid-template-columns:repeat(' + cw.w + ',minmax(0,1fr));max-width:' + (cw.w * 40) + 'px' });
    for (var r = 0; r < cw.h; r++) for (var c = 0; c < cw.w; c++) {
      var g = grid[r + ',' + c];
      if (!g) { gEl.appendChild(el('span', { 'class': 'cw-x', 'aria-hidden': 'true' })); continue; }
      var num = cw.entries.filter(function (e) { return e.r === r && e.c === c; })[0];
      g.el = el('span', { 'class': 'cw-c', 'data-k': r + ',' + c }, num ? el('i', null, String(num.n)) : null, el('b'));
      (function (gg) { gg.el.addEventListener('click', function () { var k = gg.ents.indexOf(active) >= 0 && gg.ents.length > 1 ? gg.ents[(gg.ents.indexOf(active) + 1) % gg.ents.length] : gg.ents[0]; pick(k); }); })(g);
      gEl.appendChild(g.el);
    }
    host.appendChild(el('div', { 'class': 'cw-wrap' }, gEl));
    var cur = el('p', { 'class': 'cw-cur' });
    host.appendChild(cur);
    var kb = keyboard(function (L) { type(L); }, function () { back(); }, null);
    host.appendChild(kb);
    var chk = el('button', { 'class': 'btn primary', type: 'button', onclick: check }, 'Check');
    host.appendChild(el('div', { 'class': 'row between mt8' }, ctx.hintButton('cw', function () { hint(); }), chk));
    var lists = el('div', { 'class': 'cw-clues' });
    [['a', 'Across'], ['d', 'Down']].forEach(function (dd) {
      var ul = el('div', null, el('h3', { 'class': 'label-h' }, dd[1]));
      cw.entries.forEach(function (e, k) {
        if (e.d !== dd[0]) return;
        e.btn = el('button', { type: 'button', 'class': 'clue-btn', onclick: function () { pick(k); } }, el('b', null, e.n + ' '), rich(e.clue), el('span', { 'class': 'sec' }, ' (' + e.enum + ')'));
        ul.appendChild(e.btn);
      });
      lists.appendChild(ul);
    });
    host.appendChild(lists);
    function cellsOf(k) { var e = cw.entries[k], out = []; for (var i = 0; i < e.ans.length; i++) out.push(grid[(e.r + (e.d === 'd' ? i : 0)) + ',' + (e.c + (e.d === 'a' ? i : 0))]); return out; }
    function draw() {
      Object.keys(grid).forEach(function (k) { var g = grid[k]; g.el.lastChild.textContent = g.v; g.el.classList.toggle('on', g.ents.indexOf(active) >= 0); });
      cw.entries.forEach(function (e, k) { e.btn.classList.toggle('on', k === active); });
      var e = cw.entries[active];
      clear(cur); cur.appendChild(el('b', null, e.n + (e.d === 'a' ? ' across: ' : ' down: '))); cur.appendChild(rich(e.clue));
    }
    function pick(k) { active = k; draw(); }
    function type(L) {
      if (done) return;
      var cs = cellsOf(active), g = cs.filter(function (x) { return !x.v; })[0] || cs[cs.length - 1];
      g.v = L; g.el.classList.remove('right', 'wrong'); draw();
    }
    function back() {
      var cs = cellsOf(active), f = cs.filter(function (x) { return x.v; });
      if (f.length) { f[f.length - 1].v = ''; draw(); }
    }
    function hint() {
      var cs = cellsOf(active), g = cs.filter(function (x) { return x.v !== x.ch; })[0];
      if (!g) { for (var k = 0; k < cw.entries.length && !g; k++) { g = cellsOf(k).filter(function (x) { return x.v !== x.ch; })[0]; if (g) active = k; } }
      if (g) { g.v = g.ch; g.el.classList.add('right'); draw(); }
    }
    function check() {
      var all = true;
      Object.keys(grid).forEach(function (k) { var g = grid[k]; g.el.classList.remove('right', 'wrong'); if (g.v) g.el.classList.add(g.v === g.ch ? 'right' : 'wrong'); if (g.v !== g.ch) all = false; });
      if (all && !done) {
        done = true;
        savePuzzle(P, 'cw', ctx.stars('cw'), ['cw', 'ws']);
        host.appendChild(solvedBox('Crossword done!', [S.puzzles[P.uid].done ? 'You finished both word puzzles.' : 'Now try the word search.'], ctx.stars('cw')));
      } else if (!all) toast('Green letters are right. Fix the red ones.');
    }
    host.tabIndex = -1;
    host.addEventListener('keydown', function (e) { if (/^[a-z]$/i.test(e.key)) { type(e.key.toUpperCase()); e.preventDefault(); } else if (e.key === 'Backspace') { back(); e.preventDefault(); } });
    draw();
    api.cwSolve = function () { Object.keys(grid).forEach(function (k) { grid[k].v = grid[k].ch; }); draw(); check(); return done; };
  }

  function wordsearch(host) {
    var ws = P.ws, n = ws.size, first = null, found = {}, done = false;
    var cellEls = [];
    var g = el('div', { 'class': 'ws-grid', style: 'grid-template-columns:repeat(' + n + ',44px)' });
    for (var r = 0; r < n; r++) for (var c = 0; c < n; c++) {
      (function (rr, cc) {
        var b = el('button', { type: 'button', 'class': 'ws-c', 'aria-label': 'row ' + (rr + 1) + ' column ' + (cc + 1) + ': ' + ws.rows[rr][cc], onclick: function () { tap(rr, cc); } }, ws.rows[rr][cc]);
        cellEls.push(b); g.appendChild(b);
      })(r, c);
    }
    host.appendChild(el('p', { 'class': 'sec small-t' }, 'Tap the first letter of a word, then its last letter.' + (ws.places.some(function (p) { return p.dr && p.dc; }) ? ' Words go across, down and diagonally.' : ' Words go across and down.')));
    host.appendChild(el('div', { 'class': 'ws-wrap', tabindex: '0', 'aria-label': 'Word search grid' }, g));
    var list = el('div', { 'class': 'chips mt8' });
    ws.words.forEach(function (w) { w.chip = el('span', { 'class': 'chip' }, w.show); list.appendChild(w.chip); });
    host.appendChild(list);
    host.appendChild(el('div', { 'class': 'mt8' }, ctx.hintButton('ws', function () { hint(); })));
    function at(r, c) { return cellEls[r * n + c]; }
    function cellsOf(p) { var out = []; for (var i = 0; i < p.w.length; i++) out.push([p.r + p.dr * i, p.c + p.dc * i]); return out; }
    function tap(r, c) {
      if (done) return;
      if (!first) { first = [r, c]; at(r, c).classList.add('sel'); return; }
      at(first[0], first[1]).classList.remove('sel');
      var a = first; first = null;
      var hit = ws.places.filter(function (p) {
        var e = [p.r + p.dr * (p.w.length - 1), p.c + p.dc * (p.w.length - 1)];
        return (p.r === a[0] && p.c === a[1] && e[0] === r && e[1] === c) || (e[0] === a[0] && e[1] === a[1] && p.r === r && p.c === c);
      })[0];
      if (!hit || found[hit.w]) { if (!hit) { anim(at(r, c), 'shake'); } return; }
      found[hit.w] = 1;
      cellsOf(hit).forEach(function (x) { at(x[0], x[1]).classList.add('found'); });
      ws.words.forEach(function (w) { if (w.w === hit.w) w.chip.classList.add('on'); });
      if (ctx.team) toast('Found! Teacher: give the point.');
      if (Object.keys(found).length === ws.words.length) {
        done = true;
        savePuzzle(P, 'ws', ctx.stars('ws'), ['cw', 'ws']);
        host.appendChild(solvedBox('Word search done!', [S.puzzles[P.uid].done ? 'You finished both word puzzles.' : 'Now try the crossword.'], ctx.stars('ws')));
      }
    }
    function hint() {
      var p = ws.places.filter(function (x) { return !found[x.w]; })[0];
      if (p) { var b = at(p.r, p.c); b.classList.add('hinted'); toast('A word starts at the yellow letter.'); }
    }
    api.wsSolve = function () { ws.places.forEach(function (p) { if (found[p.w]) return; var e = cellsOf(p).pop(); tap(p.r, p.c); tap(e[0], e[1]); }); return done; };
  }
  show('cw');
  PZ_CUR = { solve: function () { show('cw'); api.cwSolve(); show('ws'); api.wsSolve(); return !!(S.puzzles[P.uid] && S.puzzles[P.uid].done); } };
};

/* on-screen keyboard: A–Z in alphabetical order (every key at least 44 px), delete, optional enter */
function keyboard(onKey, onBack, onEnter) {
  var kb = el('div', { 'class': 'kb' });
  'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('').forEach(function (L) {
    kb.appendChild(el('button', { type: 'button', 'class': 'kb-k', 'data-l': L, onclick: function () { onKey(L); } }, L));
  });
  kb.appendChild(el('button', { type: 'button', 'class': 'kb-k', 'aria-label': 'Delete', onclick: onBack }, icon('back', 18)));
  if (onEnter) kb.appendChild(el('button', { type: 'button', 'class': 'kb-k wide', onclick: onEnter }, 'Enter'));
  return kb;
}

/* ---------- P3 escape room ---------- */
function escapeScene(open, total) {
  var b = '<rect width="360" height="200" rx="16" fill="#FFF8EC"/>';
  b += '<path d="M0 60 Q180 0 360 60 V70 Q180 12 0 70z" fill="#E89A2E" opacity=".35"/>';
  b += '<rect x="40" y="150" width="280" height="40" rx="8" fill="#F3EFFF"/>';
  b += '<path d="M130 190 V100 Q180 50 230 100 V190z" fill="' + (open === total ? '#E8FAF8' : '#C9A27A') + '" stroke="#8A5300" stroke-width="4"/>';
  if (open === total) {
    b += '<circle cx="180" cy="150" r="22" fill="#2EC4B6" opacity=".5"/><path d="M168 150 l8 8 16 -18" fill="none" stroke="#166F68" stroke-width="5" stroke-linecap="round"/>';
    for (var k = 0; k < 7; k++) b += '<circle cx="' + (60 + k * 40) + '" cy="40" r="5" fill="' + ['#FF6B6B', '#FFB347', '#A78BFA', '#2EC4B6'][k % 4] + '"/>';
  } else for (var i = 0; i < total; i++) {
    var y = 105 + i * (70 / Math.max(1, total - 1)), on = i < open;
    b += '<rect x="' + 196 + '" y="' + (y - 7) + '" width="16" height="14" rx="3" fill="' + (on ? '#4CAF50' : '#8A5300') + '"/>';
    b += '<path d="M199 ' + (y - 7) + ' v-5 a5 5 0 0 1 10 0 ' + (on ? 'v-2' : 'v5') + '" fill="none" stroke="' + (on ? '#4CAF50' : '#8A5300') + '" stroke-width="2.5"/>';
  }
  b += '<circle cx="70" cy="120" r="18" fill="#2EC4B6" opacity=".35"/><rect x="66" y="120" width="8" height="40" fill="#166F68" opacity=".5"/>';
  b += '<circle cx="290" cy="118" r="20" fill="#A78BFA" opacity=".35"/><rect x="286" y="118" width="8" height="42" fill="#6D4FD1" opacity=".5"/>';
  return svgNode('<svg viewBox="0 0 360 200" role="img" aria-label="' + (open === total ? 'the door is open' : open + ' of ' + total + ' locks open') + '">' + b + '</svg>');
}
PUZZLES.escape = function (ctx) {
  var P = ctx.P, st = ctx.stage, k = 0, wrong = 0;
  if (ctx.team) st.appendChild(ctx.drawTeams());
  var scene = el('div', { 'class': 'scene pz-scene' });
  st.appendChild(scene);
  st.appendChild(el('p', { 'class': 'pz-story' }, rich(P.intro)));
  var box = el('div');
  st.appendChild(box);
  var hb = ctx.hintButton('main', function () { toast('Hint: ' + P.locks[k].hint); hintText.textContent = 'Hint: ' + P.locks[k].hint; });
  hb.classList.add('x-hide');
  var hintText = el('p', { 'class': 'note mt8 x-hide' });
  st.appendChild(hb); st.appendChild(hintText);
  if (ctx.team) st.appendChild(ctx.teacherBar(function (t) { if (t) ctx.point(t); }, 'A team opens a lock? Give a point.'));
  function draw() {
    clear(scene); scene.appendChild(escapeScene(k, P.locks.length));
    clear(box);
    if (k >= P.locks.length) {
      hb.classList.add('x-hide'); hintText.classList.add('x-hide');
      var stars = ctx.stars();
      savePuzzle(P, 'main', stars);
      box.appendChild(solvedBox('You escaped!', [P.ending], stars, ctx.restart));
      return;
    }
    var L = P.locks[k];
    wrong = 0;
    hintText.classList.add('x-hide');
    var c = el('div', { 'class': 'lock' }, el('p', { 'class': 'label' }, 'Lock ' + (k + 1) + ' of ' + P.locks.length), el('h3', null, icon('lock', 20), L.title), el('p', { 'class': 'sec' }, L.instr));
    if (L.lines) c.appendChild(el('ol', { 'class': 'lock-lines' }, L.lines.map(function (s) { return el('li', null, rich(s)); })));
    if (L.qs) c.appendChild(el('ol', { 'class': 'lock-lines' }, L.qs.map(function (q) {
      return el('li', null, rich(q.q), el('div', { 'class': 'lock-opts' }, q.o.map(function (o, j) { return el('span', { 'class': 'chip' }, el('b', null, (j + 1) + ' '), o); })));
    })));
    var slots = el('div', { 'class': 'code-slots', 'aria-live': 'polite' });
    var val = '';
    function drawSlots() { clear(slots); for (var i = 0; i < L.len; i++) slots.appendChild(el('span', { 'class': 'slot' }, val.charAt(i) || '')); }
    function key(ch) { if (val.length < L.len) { val += ch; drawSlots(); } }
    function del() { val = val.slice(0, -1); drawSlots(); }
    function tryOpen() {
      if (val.length < L.len) { toast('The code has ' + L.len + (L.kind === 'password' ? ' letters.' : ' numbers.')); return; }
      if (puzzleHash(val) === L.h) { toast('Click! The lock opens.'); k++; draw(); return; }
      wrong++; anim(c, 'shake'); val = ''; drawSlots();
      if (wrong >= 3) { hb.classList.remove('x-hide'); toast('Need help? Use a hint.'); }
    }
    drawSlots();
    c.appendChild(slots);
    if (L.kind === 'password') c.appendChild(keyboard(key, del, tryOpen));
    else {
      var pad = el('div', { 'class': 'keypad' });
      '1234567890'.split('').forEach(function (d) { pad.appendChild(el('button', { type: 'button', 'class': 'kb-k', onclick: function () { key(d); } }, d)); });
      pad.appendChild(el('button', { type: 'button', 'class': 'kb-k', 'aria-label': 'Delete', onclick: del }, icon('back', 18)));
      c.appendChild(pad);
      c.appendChild(el('button', { 'class': 'btn primary block mt8', type: 'button', onclick: tryOpen }, icon('lock', 18), 'Open the lock'));
    }
    if (L.kind === 'password') c.appendChild(el('button', { 'class': 'btn primary block mt8', type: 'button', onclick: tryOpen }, icon('lock', 18), 'Open the lock'));
    c.__enter = function (code) { val = code; tryOpen(); };
    box.appendChild(c);
  }
  draw();
  PZ_CUR = {
    solve: function () {
      var guard = 0;
      while (k < P.locks.length && guard++ < 20) {
        var L = P.locks[k], code = escapeCode(L);
        box.querySelector('.lock').__enter(code);
      }
      return !!(S.puzzles[P.uid] && S.puzzles[P.uid].done);
    }
  };
};
/* re-derives a lock's code from the item data (used by the test hook, like the build gate) */
function escapeCode(L) {
  if (L.kind === 'numbers') return L.src.map(function (id) { return String(ITEMS[id].a + 1); }).join('');
  if (L.kind === 'password') return L.src.map(function (id) { return norm(ITEMS[id].acc[0]).charAt(0).toUpperCase(); }).join('');
  var right = [];
  L.src.forEach(function (id, n) { if ((ITEMS[id].fulls || [ITEMS[id].full]).some(function (f) { return norm(f) === norm(L.lines[n]); })) right.push(n + 1); });
  return L.kind === 'count' ? String(right.length) : right.join('');
}

/* ---------- P4 guess the word + What am I? ---------- */
PUZZLES.guess = function (ctx) {
  var P = ctx.P, st = ctx.stage;
  if (ctx.team) st.appendChild(ctx.drawTeams());
  var seg = el('div', { 'class': 'seg mb', role: 'group', 'aria-label': 'Game' });
  var box = el('div');
  var parts = [['wd', 'Guess the word'], ['rd', 'What am I?']];
  var api = {};
  function show(k) {
    seg.querySelectorAll('button').forEach(function (b, j) { b.setAttribute('aria-pressed', String(parts[j][0] === k)); });
    clear(box);
    (k === 'wd' ? wordle : riddles)(box);
  }
  parts.forEach(function (p) { seg.appendChild(el('button', { type: 'button', onclick: function () { show(p[0]); } }, p[1])); });
  st.appendChild(seg); st.appendChild(box);

  var allowed = {};
  (DATA.guessWords || []).forEach(function (x) { if (x[1] <= ctx.U.n) allowed[x[0].toUpperCase()] = 1; });
  P.targets.forEach(function (t) { allowed[t.w.toUpperCase()] = 1; });
  var order = shuffled(P.targets), ti = 0;

  function wordle(host) {
    var t = order[ti % order.length], W = t.w.toUpperCase(), rows = [], cur = '', done = false, lost = false;
    host.appendChild(el('p', { 'class': 'sec small-t' }, 'Guess the ' + W.length + '-letter word from this unit. 6 tries. ',
      el('span', { 'class': 'wl-key' }, el('span', { 'class': 'wl-c hit' }, 'A', el('i', { 'class': 'wl-mark' }, '✓')), ' right place  ', el('span', { 'class': 'wl-c near' }, 'B', el('i', { 'class': 'wl-mark' }, '•')), ' in the word  ', el('span', { 'class': 'wl-c miss' }, 'C', el('i', { 'class': 'wl-mark' }, '×')), ' not in the word')));
    var g = el('div', { 'class': 'wl-grid', style: 'grid-template-columns:repeat(' + W.length + ',minmax(0,52px))' });
    var cellsArr = [];
    for (var i = 0; i < 6 * W.length; i++) { var c = el('span', { 'class': 'wl-c' }); cellsArr.push(c); g.appendChild(c); }
    host.appendChild(g);
    var msg = el('div', { 'aria-live': 'polite' });
    host.appendChild(msg);
    var kb = keyboard(function (L) { if (done || lost || cur.length >= W.length) return; cur += L; draw(); }, function () { cur = cur.slice(0, -1); draw(); }, enter);
    host.appendChild(kb);
    host.appendChild(el('div', { 'class': 'row between mt8' }, ctx.hintButton('wd', function (n) {
      if (n === 1) { msg.appendChild(el('p', { 'class': 'note' }, 'Hint: ' + t.d)); }
      else msg.appendChild(el('p', { 'class': 'note' }, 'Hint: it starts with ' + W.charAt(0) + '.'));
    }), el('button', { 'class': 'btn ghost', type: 'button', onclick: function () { ti++; clear(host); wordle(host); } }, 'New word')));
    function marks(guess) {
      var res = [], left = {};
      for (var i = 0; i < W.length; i++) if (guess[i] !== W[i]) left[W[i]] = (left[W[i]] || 0) + 1;
      for (var j = 0; j < W.length; j++) {
        if (guess[j] === W[j]) res.push('hit');
        else if (left[guess[j]]) { res.push('near'); left[guess[j]]--; } else res.push('miss');
      }
      return res;
    }
    function draw() {
      cellsArr.forEach(function (c, i) {
        var r = Math.floor(i / W.length), k = i % W.length;
        var row = rows[r];
        clear(c);
        c.className = 'wl-c';
        if (row) {
          c.classList.add(row.m[k]);
          c.appendChild(document.createTextNode(row.g[k]));
          c.appendChild(el('i', { 'class': 'wl-mark', 'aria-hidden': 'true' }, row.m[k] === 'hit' ? '✓' : row.m[k] === 'near' ? '•' : '×'));
          c.setAttribute('aria-label', row.g[k] + ': ' + (row.m[k] === 'hit' ? 'right place' : row.m[k] === 'near' ? 'in the word' : 'not in the word'));
        } else if (r === rows.length) { c.textContent = cur.charAt(k); if (cur.charAt(k)) c.classList.add('typed'); }
      });
      kb.querySelectorAll('[data-l]').forEach(function (b) {
        var L = b.getAttribute('data-l'), best = '';
        rows.forEach(function (row) { row.g.split('').forEach(function (ch, i) { if (ch === L) { var m = row.m[i]; if (m === 'hit' || (m === 'near' && best !== 'hit') || (!best)) best = m; } }); });
        b.className = 'kb-k' + (best ? ' ' + best : '');
      });
    }
    function enter() {
      if (done || lost) return;
      if (cur.length !== W.length) { toast('Use ' + W.length + ' letters.'); return; }
      if (!allowed[cur]) { toast('Not in the word list. Try a word from this level.'); anim(g, 'shake'); return; }
      rows.push({ g: cur, m: marks(cur) });
      var win = cur === W;
      cur = '';
      draw();
      if (win) {
        done = true;
        savePuzzle(P, 'wd', ctx.stars('wd'), ['wd', 'rd']);
        msg.appendChild(solvedBox('You got it: ' + t.w + '!', [t.d, el('p', null, el('i', null, rich(t.ex)))], ctx.stars('wd')));
        if (ctx.team) msg.appendChild(ctx.teacherBar(function (tm) { if (tm) ctx.point(tm, 7 - rows.length); }, 'Which team guessed it?'));
      } else if (rows.length >= 6) {
        lost = true;
        msg.appendChild(el('div', { 'class': 'pz-solved' }, el('h3', null, 'The word was: ' + t.w), el('p', null, rich(t.d)), el('p', null, el('i', null, rich(t.ex)))));
      }
    }
    host.tabIndex = -1;
    host.addEventListener('keydown', function (e) {
      if (/^[a-z]$/i.test(e.key)) { if (cur.length < W.length) { cur += e.key.toUpperCase(); draw(); } e.preventDefault(); }
      else if (e.key === 'Backspace') { cur = cur.slice(0, -1); draw(); e.preventDefault(); }
      else if (e.key === 'Enter') { enter(); e.preventDefault(); }
    });
    draw();
    api.wdSolve = function () { cur = W; enter(); return done; };
  }

  function riddles(host) {
    var R = P.riddles, k = 0, score = 0, max = R.length * 3;
    var T = ctx.T;
    var box2 = el('div');
    host.appendChild(box2);
    function one() {
      clear(box2);
      if (k >= R.length) {
        var pct = score / max, stars = pct >= .8 ? 3 : pct >= .5 ? 2 : pct > 0 ? 1 : 0;
        savePuzzle(P, 'rd', stars, ['wd', 'rd']);
        box2.appendChild(solvedBox('All riddles done!', ['Points: ' + score + ' / ' + max], stars, function () { clear(host); riddles(host); }));
        return;
      }
      var r = R[k], shown = 1, over = false;
      var c = el('div', { 'class': 'riddle' }, el('p', { 'class': 'label' }, 'What am I? · ' + (k + 1) + ' / ' + R.length + (ctx.team ? ' · Team ' + T.turn.toUpperCase() : '')));
      var ul = el('ol', { 'class': 'rd-clues' });
      var pts = el('span', { 'class': 'badge amber' });
      c.appendChild(ul);
      function drawClues() { clear(ul); r.clues.slice(0, shown).forEach(function (x) { ul.appendChild(el('li', null, rich(x))); }); pts.textContent = (4 - shown) + (4 - shown === 1 ? ' point' : ' points'); }
      var more = el('button', { 'class': 'btn ghost', type: 'button', onclick: function () { if (shown < 3) { shown++; drawClues(); more.disabled = shown >= 3; } } }, 'Next clue');
      c.appendChild(el('div', { 'class': 'row between' }, pts, more));
      var fb = el('div', { 'aria-live': 'polite' });
      function finish(ok) {
        over = true;
        var p = ok ? 4 - shown : 0;
        if (!ctx.team) score += p;
        clear(fb);
        fb.appendChild(el('p', { 'class': ok ? 'right-t' : 'wrong-t' }, ok ? 'Yes! ' + (p === 1 ? '1 point.' : p + ' points.') : 'The answer is: ' + (r.acc ? r.acc[0] : r.o[r.a])));
        if (ctx.team) fb.appendChild(ctx.teacherBar(function (tm) { if (tm) { ctx.point(tm, 4 - shown); score += 4 - shown; } else { T.turn = T.turn === 'a' ? 'b' : 'a'; ctx.drawTeams(); } k++; one(); }, 'Give the points (' + (4 - shown) + ')'));
        else fb.appendChild(el('button', { 'class': 'btn primary mt8', type: 'button', onclick: function () { k++; one(); } }, 'Next', icon('next', 18)));
      }
      if (r.o) {
        var opts = el('div', { 'class': 'opts grid2' });
        r.o.forEach(function (o, i) {
          var b = el('button', { 'class': 'opt', type: 'button', onclick: function () {
            if (over) return;
            if (i === r.a) { b.classList.add('right'); finish(true); }
            else { b.classList.add('wrong'); b.disabled = true; anim(b, 'shake'); if (shown < 3) { shown++; drawClues(); more.disabled = shown >= 3; } else finish(false); }
          } }, el('span', { 'class': 'abc' }, 'ABCD'.charAt(i)), o);
          opts.appendChild(b);
        });
        c.appendChild(opts);
        c.__ok = function () { opts.children[r.a].click(); };
      } else {
        var inp = el('input', { 'class': 'inp', type: 'text', autocomplete: 'off', autocapitalize: 'off', spellcheck: 'false', 'aria-label': 'Your answer' });
        var chk = el('button', { 'class': 'btn primary', type: 'button', onclick: tryIt }, 'Check');
        function tryIt() {
          if (over || !inp.value.trim()) return;
          if (matches(inp.value, r.acc)) { inp.classList.add('right'); finish(true); }
          else { anim(inp, 'shake'); inp.value = ''; if (shown < 3) { shown++; drawClues(); more.disabled = shown >= 3; } else finish(false); }
        }
        inp.addEventListener('keydown', function (e) { if (e.key === 'Enter') tryIt(); });
        c.appendChild(el('div', { 'class': 'inrow' }, inp, chk));
        c.__ok = function () { inp.value = r.acc[0]; tryIt(); };
      }
      c.appendChild(fb);
      drawClues();
      box2.appendChild(c);
      api.rdStep = function () { if (!over) c.__ok(); var nb = fb.querySelector('.btn.primary, .teacher-bar .btn'); if (nb) nb.click(); };
    }
    one();
    api.rdSolve = function () { var g = 0; while (k < R.length && g++ < 20) api.rdStep(); return !!S.puzzles[P.uid] && S.puzzles[P.uid].parts.rd !== undefined; };
  }
  show('wd');
  PZ_CUR = { solve: function () { show('wd'); api.wdSolve(); show('rd'); api.rdSolve(); return !!(S.puzzles[P.uid] && S.puzzles[P.uid].done); } };
};
