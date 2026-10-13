/* ===== games.js: reusable game engines fed by unit data ===== */
var ACTIVE_LOOPS = [];
function stopAllLoops() { ACTIVE_LOOPS.forEach(function (l) { l.stop(); }); ACTIVE_LOOPS = []; }

/* rAF for smooth frames + a setTimeout watchdog: rAF stops in hidden tabs, the watchdog keeps state moving */
function gameLoop(step) {
  var alive = true, last = performance.now(), lastRun = last;
  function run(now) {
    var dt = Math.min(120, Math.max(0, now - last));
    last = now; lastRun = now;
    if (document.hidden) return;
    step(dt);
  }
  function frame(now) { if (!alive) return; run(now); requestAnimationFrame(frame); }
  function watchdog() { if (!alive) return; var now = performance.now(); if (now - lastRun > 150) run(now); setTimeout(watchdog, 120); }
  requestAnimationFrame(frame); setTimeout(watchdog, 120);
  var l = { stop: function () { alive = false; } };
  ACTIVE_LOOPS.push(l);
  return l;
}

var GAME_INFO = {
  memory: { name: 'Memory Match', d: 'Flip two cards. Find the pairs.', c: 'amber' },
  speed: { name: 'Speed Round', d: '60 seconds. How many can you get right?', c: 'amber' },
  falling: { name: 'Falling Words', d: 'Tap the right answer before it reaches the bottom. 3 lives.', c: 'amber' },
  builder: { name: 'Sentence Builder Race', d: 'Build the sentences as fast as you can.', c: 'amber' },
  odd: { name: 'Odd One Out', d: 'Find the word that is different.', c: 'amber' },
  balloon: { name: 'Balloon Spelling', d: 'Spell the word. A wrong letter pops a balloon.', c: 'amber' },
  escape: { name: 'Escape the Souq', d: 'Open 5 doors in the old souq. 3 right answers open a door.', c: 'amber' },
  boss: { name: 'Boss Battle', d: 'Beat the friendly boss. Right answers hit, wrong answers cost a heart.', c: 'amber' },
  cls: { name: 'Classroom Speed Round', d: 'What do you say? 60 seconds.', c: 'amber' }
};

function bestKey(scope, g) { return scope + ':' + g; }
function setBest(scope, g, val, lowerIsBetter) {
  var k = bestKey(scope, g), cur = S.games[k];
  if (cur === undefined || (lowerIsBetter ? val < cur : val > cur)) { S.games[k] = val; save(); return true; }
  return false;
}

/* Shell with Solo / Team mode and the minimal teacher bar */
function gameShell(g, scope, start) {
  var info = GAME_INFO[g];
  var card = el('section', { 'class': 'card game', id: 'game-' + g });
  var team = !!S.classMode;
  var head = el('div', { 'class': 'game-bar' },
    el('h2', { style: 'margin:0' }, info.name),
    el('div', { 'class': 'seg', role: 'group', 'aria-label': 'Mode' }));
  var seg = head.lastChild;
  var bSolo = el('button', { type: 'button', 'aria-pressed': String(!team) }, 'Solo');
  var bTeam = el('button', { type: 'button', 'aria-pressed': String(team) }, '2 teams');
  seg.appendChild(bSolo); seg.appendChild(bTeam);
  card.appendChild(head);
  card.appendChild(el('p', { 'class': 'sec' }, info.d));
  var best = S.games[bestKey(scope, g)];
  if (best !== undefined) card.appendChild(el('p', null, el('span', { 'class': 'badge amber' }, 'Your best: ' + best + (g === 'builder' ? ' s' : g === 'memory' ? ' moves' : ''))));
  var stage = el('div');
  card.appendChild(stage);
  var T = { a: 0, b: 0, turn: 'a' };
  var ctx = { card: card, stage: stage, team: team, T: T, scope: scope };
  function teamsBar() {
    var tA = el('div', { 'class': 'team a' + (T.turn === 'a' ? ' turn' : '') }, 'Team A', el('span', null, String(T.a)));
    var tB = el('div', { 'class': 'team b' + (T.turn === 'b' ? ' turn' : '') }, 'Team B', el('span', null, String(T.b)));
    return el('div', { 'class': 'teams' }, tA, tB);
  }
  ctx.teamsNode = null;
  ctx.drawTeams = function () {
    if (!ctx.team) return;
    var n = teamsBar();
    if (ctx.teamsNode && ctx.teamsNode.parentNode) ctx.teamsNode.parentNode.replaceChild(n, ctx.teamsNode);
    ctx.teamsNode = n;
    return n;
  };
  ctx.point = function (team, n) { T[team] += (n || 1); ctx.drawTeams(); };
  ctx.teacherBar = function (onPick) {
    var bar = el('div', { 'class': 'teacher-bar', 'aria-label': 'Teacher bar' },
      el('button', { 'class': 'btn', type: 'button', onclick: function () { ctx.point('a'); onPick('a'); } }, '✅ Team A'),
      el('button', { 'class': 'btn purple', type: 'button', onclick: function () { ctx.point('b'); onPick('b'); } }, '✅ Team B'),
      el('button', { 'class': 'btn ghost', type: 'button', onclick: function () { onPick(null); } }, '❌'));
    return bar;
  };
  function restart() { stopAllLoops(); clear(stage); T.a = 0; T.b = 0; T.turn = 'a'; ctx.team = team; start(ctx); }
  bSolo.addEventListener('click', function () { team = false; bSolo.setAttribute('aria-pressed', 'true'); bTeam.setAttribute('aria-pressed', 'false'); restart(); });
  bTeam.addEventListener('click', function () { team = true; bTeam.setAttribute('aria-pressed', 'true'); bSolo.setAttribute('aria-pressed', 'false'); restart(); });
  ctx.restart = restart;
  ctx.endScreen = function (title, lines) {
    stopAllLoops();
    clear(stage);
    var b = el('div', { 'class': 'card soft', style: 'text-align:center' }, el('h2', null, title));
    (lines || []).forEach(function (l) { b.appendChild(el('p', null, l)); });
    if (ctx.team) b.appendChild(el('p', { 'class': 'score-big' }, 'Team A: ' + T.a + '   ·   Team B: ' + T.b + (T.a === T.b ? '  — a draw!' : '  — Team ' + (T.a > T.b ? 'A' : 'B') + ' wins!')));
    b.appendChild(el('button', { 'class': 'btn amber', type: 'button', onclick: restart }, 'Play again'));
    stage.appendChild(b);
  };
  start(ctx);
  return card;
}

/* Generic question view for game decks (choice items) */
function gameQuestion(ctx, id, onResult, opts) {
  opts = opts || {};
  var it = ITEMS[id];
  var box = el('div');
  var prompt = it.q ? promptNode(it) : el('span', null, 'Find the odd one.');
  box.appendChild(el('div', { 'class': 'gprompt' }, prompt));
  var gopts = el('div', { 'class': 'gopts' });
  var answered = false;
  var btns = it.o.map(function (o, i) {
    var b = el('button', { 'class': 'opt', type: 'button', onclick: function () {
      if (answered) return;
      answered = true;
      var ok = i === it.a;
      b.classList.add(ok ? 'right' : 'wrong');
      if (!ok) { anim(b, 'shake'); btns[it.a].classList.add('right'); }
      var g = box.querySelector('.gapmark'); if (g) g.textContent = it.o[it.a];
      if (it.fb) box.appendChild(el('p', { 'class': 'sec', style: 'text-align:center' }, rich(it.fb)));
      if (!ctx.team) onResult(ok);
      else if (bar) bar.classList.remove('x-hide');
    } }, rich(o));
    gopts.appendChild(b); return b;
  });
  box.appendChild(gopts);
  var bar = null;
  if (ctx.team) {
    bar = ctx.teacherBar(function (team) { onResult(!!team, team); });
    box.appendChild(bar);
  }
  box.__btns = btns;
  return box;
}

var GAMES = {};

GAMES.memory = function (ctx, U) {
  var pool = shuffled(U.games.memory), pairs = [], usedSyn = {}, seen = {};
  for (var i = 0; i < pool.length && pairs.length < 6; i++) {
    var p = pool[i];
    if ((p[2] && usedSyn[p[2]]) || seen[norm(p[0])] || seen[norm(p[1])]) continue;
    if (p[2]) usedSyn[p[2]] = 1;
    seen[norm(p[0])] = 1; seen[norm(p[1])] = 1; pairs.push(p);
  }
  var cards = [];
  pairs.forEach(function (p, k) { cards.push({ k: k, t: p[0], side: 0 }); cards.push({ k: k, t: p[1], side: 1 }); });
  cards = shuffled(cards);
  var grid = el('div', { 'class': 'mem-grid' }), open = [], moves = 0, found = 0, lock = false;
  var info = el('p', { 'class': 'sec' }, 'Moves: 0');
  if (ctx.team) ctx.stage.appendChild(ctx.drawTeams());
  ctx.stage.appendChild(info);
  cards.forEach(function (c) {
    c.b = el('button', { 'class': 'mcard', type: 'button', 'aria-label': 'card', onclick: function () { flip(c); } }, '?');
    grid.appendChild(c.b);
  });
  ctx.stage.appendChild(grid);
  function flip(c) {
    if (lock || c.done || open.indexOf(c) >= 0) return;
    c.b.classList.add('up'); clear(c.b); c.b.appendChild(rich(c.t));
    open.push(c);
    if (open.length === 2) {
      moves++; info.textContent = 'Moves: ' + moves;
      var a = open[0], b = open[1];
      if (a.k === b.k) {
        a.done = b.done = true; a.b.classList.add('done'); b.b.classList.add('done'); open = []; found++;
        touchStreak();
        if (ctx.team) ctx.point(ctx.T.turn);
        if (found === pairs.length) {
          var nb = !ctx.team && setBest(ctx.scope, 'memory', moves, true);
          setTimeout(function () { ctx.endScreen('All pairs found!', ['Moves: ' + moves + (nb ? ' — a new best!' : '')]); }, 500);
        }
      } else {
        lock = true;
        setTimeout(function () { [a, b].forEach(function (x) { x.b.classList.remove('up'); clear(x.b); x.b.textContent = '?'; }); open = []; lock = false;
          if (ctx.team) { ctx.T.turn = ctx.T.turn === 'a' ? 'b' : 'a'; ctx.drawTeams(); } }, 900);
      }
    }
  }
  if (ctx.team) ctx.stage.appendChild(ctx.teacherBar(function () {}));
};

function deckRunner(ctx, deck, opts) {
  // runs choice questions from a gated deck in order, starting at a random point
  var start = rnd(deck.length), k = 0;
  return function next() { var id = deck[(start + k) % deck.length]; k++; return id; };
}

GAMES.speed = function (ctx, U, deckName, scopeName) {
  var deck = U.games[deckName || 'speed'];
  var next = deckRunner(ctx, deck);
  var score = 0, left = 60000, ended = false;
  var timer = el('span', { 'class': 'timer' }, '60');
  var sc = el('span', { 'class': 'badge amber' }, 'Score: 0');
  var bar = el('div', { 'class': 'pbar amber' }, el('i', { style: 'width:100%' }));
  ctx.stage.appendChild(el('div', { 'class': 'game-bar' }, timer, sc));
  ctx.stage.appendChild(bar);
  if (ctx.team) ctx.stage.appendChild(ctx.drawTeams());
  var qbox = el('div', { 'class': 'mt8' });
  ctx.stage.appendChild(qbox);
  function show() {
    if (ended) return;
    clear(qbox);
    qbox.appendChild(gameQuestion(ctx, next(), function (ok) {
      if (ok) { score++; sc.textContent = 'Score: ' + score; touchStreak(); }
      setTimeout(show, ok ? 350 : 900);
    }));
  }
  show();
  gameLoop(function (dt) {
    if (ended) return;
    left -= dt;
    timer.textContent = String(Math.max(0, Math.ceil(left / 1000)));
    bar.firstChild.style.width = Math.max(0, left / 600) + '%';
    if (left <= 0) {
      ended = true;
      var nb = !ctx.team && setBest(ctx.scope, deckName === 'cls' ? 'cls' : 'speed', score);
      ctx.endScreen("Time's up!", ['You got ' + score + ' right.' + (nb ? ' A new best!' : '')]);
    }
  });
};

GAMES.cls = function (ctx, U) { GAMES.speed(ctx, U, 'cls'); };

GAMES.falling = function (ctx, U) {
  var deck = U.games.falling, next = deckRunner(ctx, deck);
  var lives = 3, score = 0, speed = 34, y = 0, cur = null, busy = false, ended = false;
  var livesEl = el('span', { 'class': 'lives', 'aria-label': 'lives' }, '♥♥♥');
  var sc = el('span', { 'class': 'badge amber' }, 'Score: 0');
  ctx.stage.appendChild(el('div', { 'class': 'game-bar' }, livesEl, sc));
  if (ctx.team) ctx.stage.appendChild(ctx.drawTeams());
  var prompt = el('div', { 'class': 'gprompt' });
  var stageEl = el('div', { 'class': 'fall-stage' }, el('div', { 'class': 'fall-floor' }));
  ctx.stage.appendChild(prompt); ctx.stage.appendChild(stageEl);
  var tbar = null;
  if (ctx.team) { tbar = ctx.teacherBar(function (team) { if (team) score++; newRound(); }); ctx.stage.appendChild(tbar); }
  function newRound() {
    if (ended) return;
    busy = false;
    stageEl.querySelectorAll('.fall-tile').forEach(function (n) { n.remove(); });
    var id = next(), it = ITEMS[id];
    cur = { it: it, tiles: [] };
    clear(prompt); prompt.appendChild(promptNode(it));
    var lanes = it.o.length;
    it.o.forEach(function (o, i) {
      var b = el('button', { 'class': 'fall-tile', type: 'button', onclick: function () { hit(i, b); } }, o);
      b.style.left = (4 + i * (92 / lanes)) + '%';
      stageEl.appendChild(b); cur.tiles.push(b);
    });
    y = 0;
  }
  function lose(msg) {
    lives--; livesEl.textContent = '♥♥♥'.slice(0, Math.max(0, lives)) + '♡♡♡'.slice(0, 3 - Math.max(0, lives));
    anim(stageEl, 'shake');
    if (lives <= 0) { end(); return; }
  }
  function end() {
    ended = true;
    var nb = !ctx.team && setBest(ctx.scope, 'falling', score);
    ctx.endScreen('Game over', ['Score: ' + score + (nb ? ' — a new best!' : '')]);
  }
  function hit(i, b) {
    if (busy || ended) return;
    busy = true;
    var ok = i === cur.it.a;
    b.classList.add(ok ? 'right' : 'wrong');
    cur.tiles[cur.it.a].classList.add('right');
    var g = prompt.querySelector('.gapmark'); if (g) g.textContent = cur.it.o[cur.it.a];
    if (ctx.team) return; // teacher bar decides
    if (ok) { score++; sc.textContent = 'Score: ' + score; speed += 3; touchStreak(); setTimeout(newRound, 450); }
    else { lose(); if (!ended) setTimeout(newRound, 900); }
  }
  newRound();
  gameLoop(function (dt) {
    if (ended || busy || !cur) return;
    y += speed * dt / 1000 * (ctx.team ? 0.6 : 1);
    var maxY = stageEl.clientHeight - 56;
    cur.tiles.forEach(function (b) { b.style.transform = 'translateY(' + Math.min(y, maxY) + 'px)'; });
    if (y >= maxY) {
      busy = true;
      cur.tiles[cur.it.a].classList.add('right');
      if (ctx.team) return;
      lose(); if (!ended) setTimeout(newRound, 900);
    }
  });
};

GAMES.builder = function (ctx, U) {
  var deck = shuffled(U.games.builder).slice(0, 5), k = 0, t0 = performance.now(), elapsed = 0, ended = false;
  var timer = el('span', { 'class': 'timer' }, '0 s');
  var pr = el('span', { 'class': 'badge amber' }, '1 / ' + deck.length);
  ctx.stage.appendChild(el('div', { 'class': 'game-bar' }, timer, pr));
  if (ctx.team) ctx.stage.appendChild(ctx.drawTeams());
  var qbox = el('div');
  ctx.stage.appendChild(qbox);
  function show() {
    clear(qbox);
    if (k >= deck.length) {
      ended = true;
      var secs = Math.round(elapsed / 1000);
      var nb = !ctx.team && setBest(ctx.scope, 'builder', secs, true);
      ctx.endScreen('Finished!', ['Your time: ' + secs + ' seconds.' + (nb ? ' A new best!' : '')]);
      return;
    }
    pr.textContent = (k + 1) + ' / ' + deck.length;
    var c = makeItem(deck[k], 0, 'game', function (cc) { touchStreak(); if (!ctx.team) setTimeout(function () { k++; show(); }, cc.score ? 500 : 1300); });
    qbox.appendChild(c.node);
    if (ctx.team) qbox.appendChild(ctx.teacherBar(function () { k++; show(); }));
  }
  show();
  gameLoop(function (dt) { if (ended) return; elapsed += dt; timer.textContent = Math.floor(elapsed / 1000) + ' s'; });
};

GAMES.odd = function (ctx, U) {
  var deck = U.games.odd, k = 0, score = 0;
  var pr = el('span', { 'class': 'badge amber' });
  ctx.stage.appendChild(el('div', { 'class': 'game-bar' }, pr));
  if (ctx.team) ctx.stage.appendChild(ctx.drawTeams());
  var qbox = el('div');
  ctx.stage.appendChild(qbox);
  function show() {
    clear(qbox);
    if (k >= deck.length) { var nb = !ctx.team && setBest(ctx.scope, 'odd', score); ctx.endScreen('Well done!', ['Score: ' + score + ' / ' + deck.length + (nb ? ' — a new best!' : '')]); return; }
    pr.textContent = (k + 1) + ' / ' + deck.length + '  ·  Score: ' + score;
    qbox.appendChild(gameQuestion(ctx, deck[k], function (ok) { if (ok) { score++; touchStreak(); } k++; setTimeout(show, ctx.team ? 50 : 1400); }));
  }
  show();
};

GAMES.balloon = function (ctx, U) {
  var words = shuffled(U.games.balloon), wi = 0, solved = 0;
  var box = el('div');
  if (ctx.team) ctx.stage.appendChild(ctx.drawTeams());
  ctx.stage.appendChild(box);
  function balloonsSvg(n) {
    var b = '';
    for (var i = 0; i < 6; i++) {
      var x = 30 + i * 52, on = i < n, c = ['#2EC4B6', '#A78BFA', '#FFB347', '#FF6B6B', '#2EC4B6', '#A78BFA'][i];
      b += '<path d="M' + x + ' 92 q-4 20 6 40" stroke="#798D96" stroke-width="2" fill="none"/>';
      b += on ? '<ellipse cx="' + x + '" cy="58" rx="20" ry="26" fill="' + c + '"/><path d="M' + (x - 4) + ' 84 h8 l-4 6z" fill="' + c + '"/>'
              : '<path d="M' + (x - 10) + ' 70 l6 -8 4 10 6 -12 4 12" stroke="' + c + '" stroke-width="3" fill="none"/>';
    }
    return svgNode('<svg viewBox="0 0 340 140" role="img" aria-label="' + n + ' balloons left">' + b + '</svg>');
  }
  function play() {
    clear(box);
    if (wi >= Math.min(words.length, 8)) { var nb = !ctx.team && setBest(ctx.scope, 'balloon', solved); ctx.endScreen('Great spelling!', ['Words spelled: ' + solved + (nb ? ' — a new best!' : '')]); return; }
    var w = words[wi][0], clue = words[wi][1], left = 6, got = {}, over = false;
    var scene = el('div', { 'class': 'scene' }, balloonsSvg(6));
    var slots = el('div', { 'class': 'slots', 'aria-label': 'word' });
    var keys = el('div', { 'class': 'keys' });
    box.appendChild(el('p', { 'class': 'gprompt' }, rich(clue)));
    box.appendChild(scene); box.appendChild(slots); box.appendChild(keys);
    var msg = el('p', { 'class': 'fb', style: 'margin-left:0;text-align:center' });
    box.appendChild(msg);
    function draw() {
      clear(slots);
      w.split('').forEach(function (ch) { slots.appendChild(el('span', { 'class': ch === ' ' ? 'sp' : '' }, (ch === ' ' || got[ch]) ? ch : '')); });
    }
    function done() { return w.split('').every(function (ch) { return ch === ' ' || got[ch]; }); }
    'abcdefghijklmnopqrstuvwxyz'.split('').forEach(function (L) {
      var kb = el('button', { 'class': 'key', type: 'button', onclick: function () {
        if (over || kb.disabled) return;
        kb.disabled = true;
        if (w.indexOf(L) >= 0) { got[L] = 1; kb.classList.add('hit'); draw(); if (ctx.team) ctx.point(ctx.T.turn); }
        else { left--; kb.classList.add('miss'); clear(scene); scene.appendChild(balloonsSvg(left)); if (ctx.team) { ctx.T.turn = ctx.T.turn === 'a' ? 'b' : 'a'; ctx.drawTeams(); } }
        if (done()) { over = true; solved++; touchStreak(); msg.className = 'fb ok'; msg.textContent = 'Yes! "' + w + '"'; setTimeout(function () { wi++; play(); }, 1200); }
        else if (left <= 0) { over = true; msg.className = 'fb no'; msg.textContent = 'The word was "' + w + '".'; w.split('').forEach(function (ch) { got[ch] = 1; }); draw(); setTimeout(function () { wi++; play(); }, 1800); }
      } }, L);
      keys.appendChild(kb);
    });
    draw();
  }
  play();
  if (ctx.team) ctx.stage.appendChild(ctx.teacherBar(function () {}));
};

function souqSvg(opened, current, progress) {
  var b = '<rect x="0" y="0" width="360" height="190" rx="14" fill="#FFF8EC"/>';
  b += '<path d="M0 30 Q180 -10 360 30 V44 Q180 4 0 44z" fill="#E89A2E" opacity=".5"/>';
  for (var l = 0; l < 6; l++) b += '<path d="M' + (30 + l * 60) + ' 34 v14" stroke="#8A5300" stroke-width="2"/><circle cx="' + (30 + l * 60) + '" cy="54" r="7" fill="#FFB347" stroke="#8A5300" stroke-width="2"/>';
  for (var i = 0; i < 5; i++) {
    var x = 14 + i * 68, open = i < opened, cur = i === current;
    b += '<path d="M' + x + ' 170 V100 Q' + (x + 30) + ' 66 ' + (x + 60) + ' 100 V170z" fill="' + (open ? '#E8FAF8' : '#C9A27A') + '" stroke="' + (cur ? '#C23B3B' : '#8A5300') + '" stroke-width="' + (cur ? 4 : 2.5) + '"/>';
    if (!open) b += '<rect x="' + (x + 24) + '" y="128" width="12" height="14" rx="3" fill="#8A5300"/><path d="M' + (x + 26) + ' 128 v-5 a4 4 0 0 1 8 0 v5" fill="none" stroke="#8A5300" stroke-width="2"/>';
    else b += '<path d="M' + (x + 18) + ' 140 l8 8 16 -18" fill="none" stroke="#388E3C" stroke-width="4" stroke-linecap="round"/>';
    if (cur) for (var p = 0; p < 3; p++) b += '<circle cx="' + (x + 18 + p * 12) + '" cy="182" r="4" fill="' + (p < progress ? '#4CAF50' : '#C9D3DB') + '"/>';
    b += '<text x="' + (x + 30) + '" y="96" font-family="Nunito, sans-serif" font-weight="900" font-size="12" fill="#8A5300" text-anchor="middle">' + (i + 1) + '</text>';
  }
  return svgNode('<svg viewBox="0 0 360 190" role="img" aria-label="souq with ' + opened + ' of 5 doors open">' + b + '</svg>');
}

GAMES.escape = function (ctx, U) {
  var next = deckRunner(ctx, U.games.escape), door = 0, prog = 0;
  var scene = el('div', { 'class': 'scene' });
  ctx.stage.appendChild(scene);
  if (ctx.team) ctx.stage.appendChild(ctx.drawTeams());
  var qbox = el('div', { 'class': 'mt8' });
  ctx.stage.appendChild(qbox);
  function draw() { clear(scene); scene.appendChild(souqSvg(door, door, prog)); }
  function show() {
    draw();
    clear(qbox);
    if (door >= 5) { touchStreak(); setBest(ctx.scope, 'escape', 1); ctx.endScreen('You escaped the souq!', ['All 5 doors are open. Well done!']); return; }
    qbox.appendChild(el('p', { 'class': 'sec', style: 'text-align:center' }, 'Door ' + (door + 1) + ': ' + prog + ' / 3'));
    qbox.appendChild(gameQuestion(ctx, next(), function (ok) {
      if (ok) { prog++; if (prog >= 3) { door++; prog = 0; toast('A door opens!'); } }
      setTimeout(show, ok ? 500 : 1200);
    }));
  }
  show();
};

function bossSvg(hpPct, hit) {
  var c = hit ? '#FF6B6B' : '#A78BFA';
  var b = '<ellipse cx="180" cy="168" rx="90" ry="10" fill="#E3E8EE"/>';
  b += '<path d="M110 150 q-10 -80 70 -100 q80 20 70 100z" fill="' + c + '" stroke="#6D4FD1" stroke-width="4"/>';
  b += '<path d="M180 50 q-6 -24 10 -34" fill="none" stroke="#6D4FD1" stroke-width="4" stroke-linecap="round"/><circle cx="192" cy="14" r="7" fill="#FFB347"/>';
  b += '<circle cx="155" cy="100" r="12" fill="#fff"/><circle cx="205" cy="100" r="12" fill="#fff"/><circle cx="158" cy="102" r="5" fill="#2D3436"/><circle cx="208" cy="102" r="5" fill="#2D3436"/>';
  b += hpPct > 30 ? '<path d="M160 126 q20 14 40 0" fill="none" stroke="#2D3436" stroke-width="4" stroke-linecap="round"/>' : '<ellipse cx="180" cy="130" rx="10" ry="8" fill="#2D3436"/>';
  b += '<path d="M110 120 q-30 0 -30 -20M250 120 q30 0 30 -20" fill="none" stroke="#6D4FD1" stroke-width="5" stroke-linecap="round"/>';
  return svgNode('<svg viewBox="0 0 360 180" role="img" aria-label="the Grammar Giant">' + b + '</svg>');
}

GAMES.boss = function (ctx, deck) {
  var next = deckRunner(ctx, deck), hp = 100, hearts = 5, ended = false;
  var scene = el('div', { 'class': 'scene' });
  var hpBar = el('div', { 'class': 'hp' }, el('i', { style: 'width:100%' }));
  var heartsEl = el('span', { 'class': 'lives' });
  ctx.stage.appendChild(el('p', { style: 'text-align:center;font-weight:900' }, 'The Grammar Giant'));
  ctx.stage.appendChild(scene); ctx.stage.appendChild(hpBar);
  ctx.stage.appendChild(el('div', { 'class': 'game-bar mt8' }, heartsEl));
  if (ctx.team) ctx.stage.appendChild(ctx.drawTeams());
  var qbox = el('div', { 'class': 'mt8' });
  ctx.stage.appendChild(qbox);
  function draw(hit) { clear(scene); scene.appendChild(bossSvg(hp, hit)); hpBar.firstChild.style.width = hp + '%'; heartsEl.textContent = '♥♥♥♥♥'.slice(0, hearts) + '♡♡♡♡♡'.slice(0, 5 - hearts); }
  function show() {
    if (ended) return;
    clear(qbox);
    qbox.appendChild(gameQuestion(ctx, next(), function (ok) {
      if (ok) { hp = Math.max(0, hp - 10); draw(true); anim(scene, 'shake'); touchStreak(); }
      else { hearts--; draw(false); }
      if (hp <= 0) { ended = true; setBest(ctx.scope, 'boss', 1); setTimeout(function () { ctx.endScreen('You beat the Grammar Giant!', ['Fantastic work. You know this level!']); }, 600); return; }
      if (hearts <= 0) { ended = true; setTimeout(function () { ctx.endScreen('The Giant wins this time', ['Practise your Review Pile and try again!']); }, 600); return; }
      setTimeout(show, ok ? 600 : 1200);
    }));
  }
  draw(false);
  show();
};
