/* ===== exercises.js: items, sets, boards, test runner ===== */
var REG = {};       // item id -> live controller (test hook)
var SETREG = {};    // set id -> live set controller

function atom(it) { return (it.t === 'pair' || it.t === 'sortit' || it.t === 'bank') && it.alt ? it.alt : it; }
function rightText(it) {
  switch (it.t) {
    case 'choice': return it.o[it.a];
    case 'typed': case 'bank': return it.acc[0];
    case 'order': return it.acc[0];
    case 'fix': return it.full;
    case 'pair': return it.r;
    case 'sortit': return it.g;
    case 'lines': return it.lines.map(function (l) { return l[0] + ': ' + l[1]; }).join(' / ');
  }
  return '';
}
function promptText(it) {
  switch (it.t) {
    case 'choice': return it.q ? plain(it.q) : it.o.join(' · ');
    case 'typed': return plain(it.q) + (it.cue ? ' (' + it.cue + ')' : '');
    case 'bank': return (it.sp ? it.sp + ': ' : '') + plain(it.q);
    case 'order': return it.tiles.join(' / ');
    case 'fix': return it.tokens.join(' ');
    case 'pair': return it.l;
    case 'sortit': return it.x;
    case 'lines': return 'Put the dialogue in order';
  }
  return '';
}
function itemSource(id) {
  var m = /^a\d\du(\d+)-/.exec(id);
  return m ? 'Unit ' + m[1] : '';
}

/* ---------- recording ---------- */
function recordAttempt(id, ok, your, opts) {
  opts = opts || {};
  var r = S.items[id] || (S.items[id] = { r: 0, w: 0 });
  if (ok) r.r++; else r.w++;
  touchStreak();
  if (!ok && !opts.noMistake) {
    if (S.pile[id] === undefined) S.pile[id] = 0;
    var it = ITEMS[id];
    S.mistakes = S.mistakes.filter(function (m) { return m.id !== id; });
    S.mistakes.unshift({ id: id, your: String(your || '—').slice(0, 160), right: rightText(it), q: promptText(it).slice(0, 200), src: itemSource(id), t: Date.now() });
    if (S.mistakes.length > 300) S.mistakes.length = 300;
  }
  save();
}

/* ---------- cue pills (B5): say in words what to do ---------- */
var CUES = { '✓': ['Answer: Yes', 'check', 'ok'], '✗': ['Answer: No', 'cross', 'no'], '−': ['Make it negative', 'minus', 'neg'],
  '?': ['Make a question', 'wq', 'q'], '+': ['Make it positive', 'plus', 'pos'] };
function cuePill(c) {
  var d = CUES[c] || [c, 'choose', 'q'];
  return el('span', { 'class': 'cue cue-' + d[2] }, icon(d[1], 16), d[0]);
}

/* ---------- prompt rendering ---------- */
function promptNode(it, filled) {
  var q = it.t === 'choice' || it.t === 'typed' || it.t === 'bank' ? it.q : '';
  var span = el('span', { 'class': 'qt' });
  if (it.sp) span.appendChild(el('span', { 'class': 'speaker' }, it.sp + ':'));
  if (it.spell) { span.appendChild(el('span', { 'class': 'spellpat' }, q)); return span; }
  var parts = String(q || '').split('___');
  parts.forEach(function (p, i) {
    span.appendChild(rich(p));
    if (i < parts.length - 1) span.appendChild(el('span', { 'class': 'gapmark' }, filled || ' '));
  });
  if (it.cue) span.appendChild(cuePill(it.cue));
  return span;
}

/* Fill a gap mark; an answer like 'm or 's is glued to the word before (I'm, not I 'm) */
function fillGap(root, v) {
  var g = root.querySelector('.gapmark');
  if (!g) return;
  g.textContent = v;
  var prev = g.previousSibling;
  var glue = /^'(m|s|re|ve|ll|d)\b/.test(String(v));
  g.classList.toggle('glued', glue);
  if (prev && prev.nodeType === 3) {
    if (glue && /\s$/.test(prev.textContent)) { g.dataset.sp = '1'; prev.textContent = prev.textContent.replace(/\s+$/, ''); }
    else if (!glue && g.dataset.sp) { prev.textContent += ' '; delete g.dataset.sp; }
  }
}

/* ---------- single item controller ---------- */
function makeItem(id, num, mode, onDone, hooks) {
  var raw = ITEMS[id];
  var it = mode === 'practice' || mode === 'player' ? raw : atom(raw);
  var test = mode === 'test';
  // player mode: the answer is checked from the sticky Check bar, feedback goes to the sheet
  var deferred = mode === 'player';
  hooks = hooks || {};
  var root = el('div', { 'class': 'item', 'data-id': id });
  var ctl = { id: id, node: root, done: false, score: 0, tries: 0, item: it, ready: function () { return false; }, check: function () {} };
  var maxTries = test ? 1 : (it.t === 'choice' ? (it.o.length > 2 ? 2 : 1) : 2);
  var fb = el('div', { 'class': 'fb', 'aria-live': 'polite' });
  var qline = el('div', { 'class': 'qline' }, num ? el('span', { 'class': 'qn' }, String(num)) : null);
  root.appendChild(qline);

  function finish(ok, your, revealed) {
    ctl.done = true;
    ctl.score = ok ? (ctl.tries <= 1 ? 1 : 0.5) : 0;
    if (!test && !revealed && ok) recordAttempt(id, true, your, { noMistake: true }); // wrong tries were already recorded in wrongTry (B4)
    if (ok) { fb.className = 'fb ok'; fb.textContent = ctl.tries <= 1 ? 'Great!' : 'Yes, good.'; anim(root, 'glow'); }
    else { fb.className = 'fb no'; clear(fb); fb.appendChild(document.createTextNode(revealed ? 'Answer: ' : 'The answer is: ')); fb.appendChild(el('span', { 'class': 'ans' }, rightText(it))); }
    if (onDone) onDone(ctl);
  }
  function wrongTry(your, node) {
    ctl.tries++;
    if (!test) recordAttempt(id, false, your);
    anim(node || root, 'shake');
    if (ctl.tries >= maxTries) { finish(false, your); return true; }
    fb.className = 'fb no'; fb.textContent = 'Not quite. Try again.';
    if (hooks.onTry) hooks.onTry(ctl);
    return false;
  }

  if (it.t === 'choice') {
    if (it.q || it.sp) qline.appendChild(promptNode(it));
    else qline.appendChild(el('span', { 'class': 'qt' }, 'Find the odd one.'));
    var rows = deferred || test;
    var short = it.o.every(function (o) { return plain(o).length <= 12; });
    var opts = el('div', { 'class': 'opts' + (rows ? (short ? ' grid2' : ' rows') : '') });
    var btns = it.o.map(function (o, i) {
      var b = el('button', { 'class': 'opt', type: 'button', onclick: function () { pick(i); } }, rows ? el('span', { 'class': 'abc', 'aria-hidden': 'true' }, 'ABCDEF'.charAt(i)) : null, rich(o));
      opts.appendChild(b); return b;
    });
    root.appendChild(opts);
    var chosen = null, checking = false;
    function pick(i) {
      if (ctl.done) return;
      if (test || (deferred && !checking)) { if (btns[i].disabled) return; chosen = i; btns.forEach(function (b, k) { b.classList.toggle('sel', k === i); }); ctl.answered = true; if (hooks.onChange) hooks.onChange(); return; }
      btns.forEach(function (b) { b.classList.remove('sel'); });
      if (i === it.a) {
        ctl.tries++;
        btns[i].classList.add('right');
        btns.forEach(function (b) { b.disabled = true; });
        setGap(it.o[i]);
        finish(true, it.o[i]);
        if (it.fb) fb.appendChild(el('div', { 'class': 'sec small-t' }, rich(it.fb)));
      } else {
        btns[i].classList.add('wrong'); btns[i].disabled = true;
        if (wrongTry(it.o[i], btns[i])) { btns[it.a].classList.add('right'); btns.forEach(function (b) { b.disabled = true; }); setGap(it.o[it.a]); if (it.fb) fb.appendChild(el('div', { 'class': 'sec small-t' }, rich(it.fb))); }
      }
    }
    ctl.ready = function () { return chosen !== null; };
    ctl.check = function () { if (chosen === null) return; var c = chosen; chosen = null; checking = true; pick(c); checking = false; };
    ctl.autoAnswer = function (ok) {
      if (ok) pick(it.a);
      else { var w = it.o.map(function (_, k) { return k; }).filter(function (k) { return k !== it.a && !btns[k].disabled; })[0]; pick(w); }
      if (deferred) ctl.check();
    };
    ctl.result = function () { return { ok: chosen === it.a, your: chosen === null ? '—' : it.o[chosen] }; };
    ctl.reveal = function () { if (ctl.done) return; btns[it.a].classList.add('right'); btns.forEach(function (b) { b.disabled = true; }); setGap(it.o[it.a]); finish(false, null, true); };
  } else if (it.t === 'typed') {
    qline.appendChild(promptNode(it));
    if (it.spell && it.hint) root.appendChild(el('div', { 'class': 'hint' }, rich(it.hint)));
    else if (it.hint) root.appendChild(el('div', { 'class': 'hint' }, 'Starts with: ', el('b', null, it.hint)));
    var inp = el('input', { 'class': 'inp', type: 'text', autocomplete: 'off', autocapitalize: 'off', spellcheck: 'false', 'aria-label': 'Your answer' });
    var chk = el('button', { 'class': 'btn small', type: 'button' }, 'Check');
    var row = el('div', { 'class': 'inrow' }, inp, test || deferred ? null : chk);
    root.appendChild(row);
    inp.addEventListener('keydown', function (e) { if (e.key === 'Enter' && !test) { e.preventDefault(); if (deferred && hooks.submit) hooks.submit(); else check(); } });
    inp.addEventListener('input', function () { ctl.answered = !!inp.value.trim(); });
    chk.addEventListener('click', check);
    function check() {
      if (ctl.done) return;
      var v = inp.value;
      if (!v.trim()) { inp.focus(); return; }
      if (matches(v, it.acc)) { ctl.tries++; inp.classList.add('right'); inp.disabled = true; chk.disabled = true; setGap(v.trim()); finish(true, v); }
      else { inp.classList.add('wrong'); setTimeout(function () { inp.classList.remove('wrong'); }, 600);
        if (wrongTry(v, inp)) { inp.disabled = true; chk.disabled = true; setGap(it.acc[0]); } }
    }
    ctl.ready = function () { return !!inp.value.trim(); };
    ctl.check = check;
    ctl.focus = function () { try { inp.focus({ preventScroll: true }); } catch (e) { inp.focus(); } };
    ctl.autoAnswer = function (ok) { inp.value = ok ? it.acc[0] : 'zzz wrong'; check(); };
    ctl.result = function () { return { ok: matches(inp.value, it.acc), your: inp.value || '—' }; };
    ctl.reveal = function () { if (ctl.done) return; inp.value = it.acc[0]; inp.disabled = true; chk.disabled = true; setGap(it.acc[0]); finish(false, null, true); };
  } else if (it.t === 'order') {
    qline.appendChild(el('span', { 'class': 'qt' }, 'Make a sentence.' ));
    var line = el('div', { 'class': 'answer-line', 'aria-label': 'Your sentence' });
    var endp = it.end ? el('span', { 'class': 'chip' }, it.end) : null;
    var tilesBox = el('div', { 'class': 'tiles' });
    var placed = [];
    var tb = it.tiles.map(function (tk, i) {
      var b = el('button', { 'class': 'tile', type: 'button', onclick: function () { place(i); } }, tk);
      tilesBox.appendChild(b); return b;
    });
    var ochk = el('button', { 'class': 'btn small', type: 'button', onclick: function () { ocheck(); } }, 'Check');
    var oreset = el('button', { 'class': 'btn small ghost', type: 'button', onclick: function () { reset(); } }, 'Clear');
    root.appendChild(line); root.appendChild(tilesBox);
    if (!test && !deferred) root.appendChild(el('div', { 'class': 'inrow' }, ochk, oreset));
    else root.appendChild(el('div', { 'class': 'inrow' }, oreset));
    function drawLine() {
      clear(line);
      placed.forEach(function (i, k) {
        line.appendChild(el('button', { 'class': 'tile tok', type: 'button', onclick: function () { if (ctl.done) return; placed.splice(k, 1); tb[i].classList.remove('used'); drawLine(); } }, it.tiles[i]));
      });
      if (endp && placed.length) line.appendChild(endp);
      ctl.answered = placed.length === it.tiles.length;
    }
    function place(i) { if (ctl.done || placed.indexOf(i) >= 0) return; placed.push(i); tb[i].classList.add('used'); drawLine(); }
    function reset() { if (ctl.done) return; placed = []; tb.forEach(function (b) { b.classList.remove('used'); }); drawLine(); }
    function sentence() { return placed.map(function (i) { return it.tiles[i]; }).join(' ') + (it.end || ''); }
    function ocheck() {
      if (ctl.done) return;
      if (placed.length < it.tiles.length) { fb.className = 'fb no'; fb.textContent = 'Use all the words.'; return; }
      var s = sentence();
      if (matches(s, it.acc)) { ctl.tries++; ochk.disabled = true; finish(true, s); }
      else if (wrongTry(s, line)) { ochk.disabled = true; } else { reset(); }
    }
    ctl.autoAnswer = function (ok) {
      reset();
      if (ok) {
        var want = norm(it.acc[0]).split(' '), used = {};
        // place tiles in the order of the right sentence
        var toks = it.tiles.map(function (x) { return norm(x); });
        var seq = [];
        var w = 0;
        while (w < want.length) {
          var found = -1;
          for (var i = 0; i < toks.length; i++) {
            if (used[i]) continue;
            var tw = toks[i].split(' ');
            if (want.slice(w, w + tw.length).join(' ') === toks[i]) { found = i; w += tw.length; break; }
          }
          if (found < 0) break;
          used[found] = 1; seq.push(found);
        }
        seq.forEach(place);
      } else { var rev = it.tiles.map(function (_, i) { return i; }).reverse(); rev.forEach(place); if (matches(sentence(), it.acc)) { reset(); [1, 0].concat(it.tiles.map(function (_, i) { return i; }).slice(2)).forEach(place); } }
      ocheck();
    };
    ctl.ready = function () { return placed.length === it.tiles.length; };
    ctl.check = ocheck;
    ctl.result = function () { return { ok: placed.length === it.tiles.length && matches(sentence(), it.acc), your: placed.length ? sentence() : '—' }; };
    ctl.reveal = function () { if (ctl.done) return; clear(line); line.appendChild(el('span', { 'class': 'right-t' }, it.acc[0])); tilesBox.classList.add('x-hide'); ochk.disabled = true; finish(false, null, true); };
  } else if (it.t === 'fix') {
    qline.appendChild(el('span', { 'class': 'qt' }, 'Tap the mistake.'));
    var toksBox = el('div', { 'class': 'tiles' });
    var fixRow = el('div', { 'class': 'inrow x-hide' });
    var finp = el('input', { 'class': 'inp', type: 'text', autocomplete: 'off', autocapitalize: 'off', spellcheck: 'false', 'aria-label': 'Write the correct word(s)' });
    var fchk = el('button', { 'class': 'btn small', type: 'button' }, 'Check');
    fixRow.appendChild(el('span', { 'class': 'sec small-t', style: 'flex:0 0 100%' }, 'Write the correct word(s) — or the whole sentence:'));
    fixRow.appendChild(finp); if (!test && !deferred) fixRow.appendChild(fchk);
    var found = false;
    var tbtn = it.tokens.map(function (tk, i) {
      var b = el('button', { 'class': 'tile tok', type: 'button', onclick: function () { tap(i); } }, tk);
      toksBox.appendChild(b); return b;
    });
    root.appendChild(toksBox); root.appendChild(fixRow);
    function tap(i) {
      if (ctl.done) return;
      if (test) { tbtn.forEach(function (b, k) { b.classList.toggle('badsel', k === i); }); ctl.tapped = i; fixRow.classList.remove('x-hide'); return; }
      if (found) return;
      if (it.bad.indexOf(i) >= 0) {
        found = true;
        it.bad.forEach(function (k) { tbtn[k].classList.add('badsel'); });
        fixRow.classList.remove('x-hide'); finp.focus();
        fb.className = 'fb ok cue'; fb.textContent = 'Yes! Now write it correctly.';
      } else if (wrongTry(it.tokens[i], tbtn[i])) { showFix(); }
    }
    function showFix() { fixRow.classList.add('x-hide'); toksBox.classList.add('x-hide'); }
    function fcheck() {
      if (ctl.done || !found) return;
      var v = finp.value;
      if (!v.trim()) return;
      if (matches(v, it.acc.concat(it.fulls || []))) { ctl.tries++; finp.disabled = true; fchk.disabled = true; finish(true, v); fb.appendChild(el('div', { 'class': 'sec small-t' }, it.full)); }
      else if (wrongTry(v, finp)) { finp.disabled = true; fchk.disabled = true; }
    }
    fchk.addEventListener('click', fcheck);
    finp.addEventListener('keydown', function (e) { if (e.key === 'Enter' && !test) { e.preventDefault(); if (deferred && hooks.submit) hooks.submit(); else fcheck(); } });
    ctl.ready = function () { return found && !!finp.value.trim(); };
    ctl.check = fcheck;
    ctl.autoAnswer = function (ok) {
      if (ok) { tap(it.bad[0]); finp.value = it.acc[0]; fcheck(); }
      else { var w = it.tokens.map(function (_, k) { return k; }).filter(function (k) { return it.bad.indexOf(k) < 0; }); tap(w[0]); if (!ctl.done) tap(w[1] !== undefined ? w[1] : w[0]); }
    };
    ctl.answerText = function (v) { tap(it.bad[0]); finp.value = v; fcheck(); };
    ctl.result = function () { var ok = it.bad.indexOf(ctl.tapped) >= 0 && matches(finp.value, it.acc.concat(it.fulls || [])); return { ok: ok, your: (ctl.tapped !== undefined ? it.tokens[ctl.tapped] : '—') + ' → ' + (finp.value || '—') }; };
    ctl.reveal = function () { if (ctl.done) return; showFix(); finish(false, null, true); };
  } else if (it.t === 'lines') {
    qline.appendChild(el('span', { 'class': 'qt' }, 'Tap the lines in order.'));
    var lbox = el('div', { style: 'margin-left:36px' });
    var built = el('ol', { 'class': 'answer-line', style: 'display:block;padding-left:28px;margin-left:36px' });
    var picked = [];
    var lbtns = it.shuf.map(function (li) {
      var L = it.lines[li];
      var b = el('button', { 'class': 'opt', type: 'button', style: 'display:block;width:100%;margin:6px 0', onclick: function () { lpick(li, b); } }, el('span', { 'class': 'speaker' }, L[0] + ':'), rich(L[1]));
      lbox.appendChild(b); return b;
    });
    var lchk = el('button', { 'class': 'btn small', type: 'button', onclick: function () { lcheck(); } }, 'Check');
    var lclr = el('button', { 'class': 'btn small ghost', type: 'button', onclick: function () { lreset(); } }, 'Clear');
    root.appendChild(built); root.appendChild(lbox); root.appendChild(el('div', { 'class': 'inrow' }, deferred ? null : lchk, lclr));
    ctl.ready = function () { return picked.length === it.lines.length; };
    ctl.check = function () { lcheck(); };
    function ldraw() { clear(built); picked.forEach(function (li) { built.appendChild(el('li', { 'class': 'dl-line' }, el('span', { 'class': 'speaker' }, it.lines[li][0] + ':'), rich(it.lines[li][1]))); }); }
    function lpick(li, b) { if (ctl.done || picked.indexOf(li) >= 0) return; picked.push(li); b.classList.add('x-hide'); ldraw(); }
    function lreset() { if (ctl.done) return; picked = []; lbtns.forEach(function (b) { b.classList.remove('x-hide'); }); ldraw(); }
    function lcheck() {
      if (ctl.done) return;
      if (picked.length < it.lines.length) { fb.className = 'fb no'; fb.textContent = 'Use all the lines.'; return; }
      var ok = picked.every(function (li, k) { return li === k; });
      if (ok) { ctl.tries++; lchk.disabled = true; finish(true, 'order'); }
      else if (wrongTry('wrong order', built)) { lchk.disabled = true; picked = it.lines.map(function (_, k) { return k; }); ldraw(); lbox.classList.add('x-hide'); } else lreset();
    }
    ctl.autoAnswer = function (ok) {
      lreset();
      var seq = it.lines.map(function (_, k) { return k; });
      if (!ok) seq.reverse();
      seq.forEach(function (li) { lpick(li, lbtns[it.shuf.indexOf(li)]); });
      lcheck();
    };
    ctl.reveal = function () { if (ctl.done) return; picked = it.lines.map(function (_, k) { return k; }); ldraw(); lbox.classList.add('x-hide'); lchk.disabled = true; finish(false, null, true); };
    ctl.result = function () { return { ok: picked.length === it.lines.length && picked.every(function (li, k) { return li === k; }), your: 'order' }; };
  }
  function setGap(v) { fillGap(root, v); }
  root.appendChild(fb);
  REG[id] = ctl;
  return ctl;
}

/* ---------- boards: match, sort, bank ---------- */
function seededOrder(n, seed) {
  var a = []; for (var i = 0; i < n; i++) a.push(i);
  var h = 0; for (var k = 0; k < seed.length; k++) h = (h * 31 + seed.charCodeAt(k)) >>> 0;
  for (var j = n - 1; j > 0; j--) { h = (h * 1103515245 + 12345) >>> 0; var r = h % (j + 1); var t2 = a[j]; a[j] = a[r]; a[r] = t2; }
  return a;
}

function boardControllers(set, wrapNode, onItem) {
  var ctls = [];
  var k = set.k;
  if (k === 'match') {
    var ids = set.items, rights = seededOrder(ids.length, set.id);
    var board = el('div', { 'class': 'board' });
    var L = [], R = [], selected = null;
    ids.forEach(function (id, i) {
      var it = ITEMS[id];
      var c = { id: id, done: false, score: 0, tries: 0, item: it };
      var lb = el('button', { 'class': 'opt', type: 'button', onclick: function () { if (c.done) return; selected = i; L.forEach(function (b, j) { b.classList.toggle('sel', j === i); }); } }, rich(it.l));
      L.push(lb); c.lb = lb; ctls.push(c);
    });
    rights.forEach(function (i) {
      var it = ITEMS[ids[i]];
      var rb = el('button', { 'class': 'opt', type: 'button', onclick: function () { tryPair(i); } }, rich(it.r));
      R[i] = rb;
    });
    function lock(i, ok, revealed) {
      var c = ctls[i];
      c.done = true; c.score = ok ? (c.tries <= 1 ? 1 : 0.5) : 0;
      L[i].classList.remove('sel'); L[i].classList.add(ok ? 'matched' : 'right'); R[i].classList.add(ok ? 'matched' : 'right');
      L[i].disabled = true; R[i].disabled = true;
      if (!revealed && ok) recordAttempt(c.id, true, null, { noMistake: true }); // wrong tries already recorded (B4)
      selected = null; onItem(c);
    }
    function tryPair(ri) {
      if (selected === null || ctls[ri].done && ri !== selected) { if (selected === null) toast('Tap a word on the left first.'); return; }
      var c = ctls[selected];
      if (ri === selected) { c.tries++; lock(selected, true); anim(R[ri], 'glow'); }
      else { c.tries++; recordAttempt(c.id, false, ITEMS[ids[ri]].r); anim(R[ri], 'shake'); if (c.tries >= 2) lock(selected, false); }
    }
    for (var row = 0; row < ids.length; row++) { board.appendChild(L[row]); board.appendChild(R[rights[row]]); }
    wrapNode.appendChild(el('p', { 'class': 'sec small-t' }, 'Tap a box on the left, then its partner on the right.'));
    wrapNode.appendChild(board);
    ctls.forEach(function (c, i) {
      c.autoAnswer = function (ok) {
        selected = i;
        if (ok) { tryPair(i); return; }
        var w = -1;
        for (var j = 0; j < ids.length; j++) if (j !== i && !ctls[j].done) { w = j; break; }
        if (w < 0) { c.tries = 1; lock(i, false); return; }
        tryPair(w); if (!c.done) { selected = i; tryPair(w); }
      };
      c.reveal = function () { if (!c.done) lock(i, false, true); };
      REG[c.id] = c;
    });
  } else if (k === 'sort') {
    var sel = null;
    var chipsBox = el('div', { 'class': 'chips' });
    var bks = el('div', { 'class': 'buckets' });
    var bucketIn = {};
    set.groups.forEach(function (g) {
      var inner = el('div', { 'class': 'in' });
      bucketIn[g] = inner;
      bks.appendChild(el('button', { 'class': 'bucket', type: 'button', onclick: function () { drop(g); } }, rich(g), inner));
    });
    set.items.forEach(function (id, i) {
      var it = ITEMS[id];
      var c = { id: id, done: false, score: 0, tries: 0, item: it };
      c.b = el('button', { 'class': 'opt', type: 'button', onclick: function () { if (c.done) return; sel = i; ctls.forEach(function (x, j) { x.b.classList.toggle('sel', j === i); }); } }, rich(it.x));
      chipsBox.appendChild(c.b); ctls.push(c);
    });
    function place(i, ok, revealed) {
      var c = ctls[i];
      c.done = true; c.score = ok ? (c.tries <= 1 ? 1 : 0.5) : 0;
      c.b.classList.add('x-hide');
      bucketIn[c.item.g].appendChild(el('span', { style: ok ? null : 'border-color:#C62828;color:#C62828' }, c.item.x));
      if (!revealed && ok) recordAttempt(c.id, true, null, { noMistake: true }); // wrong tries already recorded (B4)
      sel = null; onItem(c);
    }
    function drop(g) {
      if (sel === null) { toast('Tap a word first.'); return; }
      var c = ctls[sel];
      c.tries++;
      if (c.item.g === g) place(sel, true);
      else { recordAttempt(c.id, false, g); anim(c.b, 'shake'); if (c.tries >= 2) place(sel, false); }
    }
    wrapNode.appendChild(el('p', { 'class': 'sec small-t' }, 'Tap a word, then tap its group.'));
    wrapNode.appendChild(chipsBox); wrapNode.appendChild(bks);
    ctls.forEach(function (c, i) {
      c.autoAnswer = function (ok) { sel = i; if (ok) drop(c.item.g); else { var w = set.groups.filter(function (g) { return g !== c.item.g; })[0]; drop(w); if (!c.done) { sel = i; drop(w); } } };
      c.reveal = function () { if (!c.done) place(i, false, true); };
      REG[c.id] = c;
    });
  } else if (k === 'bank') {
    var active = null;
    var bar = el('div', { 'class': 'bankbar' });
    set.bank.forEach(function (w) { bar.appendChild(el('button', { 'class': 'opt', type: 'button', onclick: function () { fill(w); } }, w)); });
    wrapNode.appendChild(el('p', { 'class': 'sec small-t' }, 'Tap a gap, then tap a word.'));
    wrapNode.appendChild(bar);
    var rows = set.lines ? set.lines : set.items.map(function (id) { return [null, null, id]; });
    var num = 0;
    rows.forEach(function (ln) {
      if (!ln[2]) { wrapNode.appendChild(el('div', { 'class': 'item dl-line' }, el('span', { 'class': 'speaker' }, ln[0] + ':'), rich(ln[1]))); return; }
      var id = ln[2], i = num++;
      var it = ITEMS[id];
      var c = { id: id, done: false, score: 0, tries: 0, item: it };
      var row = el('div', { 'class': 'item' });
      var line = el('div', { 'class': 'qline' }, el('span', { 'class': 'qn' }, String(i + 1)));
      var span = el('span', { 'class': 'qt' });
      if (it.sp) span.appendChild(el('span', { 'class': 'speaker' }, it.sp + ':'));
      var parts = it.q.split('___');
      span.appendChild(rich(parts[0]));
      c.g = el('button', { 'class': 'gapbtn', type: 'button', onclick: function () { activate(i); } }, '?');
      span.appendChild(c.g);
      span.appendChild(rich(parts[1] || ''));
      line.appendChild(span); row.appendChild(line);
      c.fb = el('div', { 'class': 'fb' }); row.appendChild(c.fb);
      wrapNode.appendChild(row);
      ctls.push(c);
    });
    function activate(i) { if (ctls[i].done) return; active = i; ctls.forEach(function (c, j) { c.g.classList.toggle('active', j === i); }); }
    function nextActive() { for (var j = 0; j < ctls.length; j++) if (!ctls[j].done) { activate(j); return; } active = null; }
    function done(i, ok, revealed) {
      var c = ctls[i];
      c.done = true; c.score = ok ? (c.tries <= 1 ? 1 : 0.5) : 0;
      c.g.textContent = c.item.acc[0]; c.g.classList.remove('active'); c.g.classList.add(ok ? 'right' : 'wrong'); c.g.disabled = true;
      if (!ok) { c.fb.className = 'fb no'; c.fb.textContent = revealed ? 'Answer shown.' : 'The answer is shown in the gap.'; c.g.classList.remove('wrong'); c.g.classList.add('right'); }
      if (!revealed && ok) recordAttempt(c.id, true, null, { noMistake: true }); // wrong tries already recorded (B4)
      onItem(c); nextActive();
    }
    function fill(w) {
      if (active === null) { nextActive(); if (active === null) return; }
      var c = ctls[active];
      c.tries++;
      if (matches(w, c.item.acc)) done(active, true);
      else { recordAttempt(c.id, false, w); anim(c.g, 'shake'); c.fb.className = 'fb no'; c.fb.textContent = 'Not "' + w + '". Try again.'; if (c.tries >= 2) done(active, false); }
    }
    ctls.forEach(function (c, i) {
      c.autoAnswer = function (ok) { activate(i); if (ok) fill(c.item.acc[0]); else { var w = set.bank.filter(function (b) { return !matches(b, c.item.acc); })[0]; fill(w); if (!c.done) { activate(i); fill(w); } } };
      c.reveal = function () { if (!c.done) done(i, false, true); };
      REG[c.id] = c;
    });
    nextActive();
  }
  return ctls;
}

/* ---------- the player: one question per screen ---------- */
function fmtScore(x) { return (Math.round(x * 10) / 10).toString(); }
function playSteps(set) {
  // boards are one step each; Match shows at most 6 pairs per screen
  if (set.k === 'match') {
    var out = [], per = set.items.length > 6 ? Math.ceil(set.items.length / Math.ceil(set.items.length / 6)) : 6;
    for (var i = 0; i < set.items.length; i += per) out.push({ board: { k: 'match', id: set.id + (i ? '#' + i : ''), items: set.items.slice(i, i + per) } });
    return out;
  }
  if (set.k === 'sort' || set.k === 'bank') return [{ board: set }];
  return set.items.map(function (id) { return { id: id }; });
}
/* opts: title, onClose, onNext (next set), text ({title, text} for reading), noSave, accent */
function playSet(set, opts) {
  opts = opts || {};
  var steps = playSteps(set), at = 0;
  var nItems = set.items.length;
  var sc = { id: set.id, ctls: [], set: set, score: 0, finished: false };
  var byId = {};
  var P = el('section', { 'class': 'player' + (opts.text ? ' has-text' : ''), 'data-set': set.id });
  var bar = el('div', { 'class': 'pbar' }, el('i', { style: 'width:0%' }));
  var count = el('span', { 'class': 'pl-count' });
  var closeB = el('button', { 'class': 'icon-btn', type: 'button', 'aria-label': 'Close', onclick: function () { if (opts.onClose) opts.onClose(); } }, icon('cross', 22));
  var top = el('div', { 'class': 'pl-top' }, closeB, bar, count);
  P.appendChild(top);
  var textBtn = null, textPanel = null;
  if (opts.text) {
    textPanel = el('div', { 'class': 'textpanel', tabindex: '0', 'aria-label': 'Reading text' }, el('h2', null, opts.text.title));
    opts.text.text.split(/\n\s*\n/).forEach(function (p) { textPanel.appendChild(el('p', null, rich(p.trim()))); });
    textBtn = el('button', { 'class': 'pill-btn pl-textbtn', type: 'button', 'aria-pressed': 'false', onclick: function () {
      var on = !P.classList.contains('show-text'); P.classList.toggle('show-text', on); textBtn.setAttribute('aria-pressed', String(on));
    } }, icon('reading', 18), 'Text');
    top.appendChild(textBtn);
  }
  var instr = el('p', { 'class': 'pl-instr' }, icon(TYPE_ICON[set.k] || 'choose', 20), set.instr);
  var stage = el('div', { 'class': 'pl-stage' });
  var body = el('div', { 'class': 'pl-body' }, instr, stage);
  P.appendChild(textPanel ? el('div', { 'class': 'pl-split' }, textPanel, body) : body);
  var reveal = el('button', { 'class': 'btn ghost reveal-btn', type: 'button' }, 'Reveal answer');
  var main = el('button', { 'class': 'btn primary', type: 'button' }, 'Check');
  var sbar = el('div', { 'class': 'pl-bar' }, el('div', { 'class': 'pl-bar-in' }, reveal, main));
  P.appendChild(sbar);
  var sheet = el('div', { 'class': 'sheet', role: 'status', 'aria-live': 'polite' });
  P.appendChild(sheet);
  var cur = null; // { ctl } or { board: ctls }

  function doneCount() { return sc.ctls.filter(function (c) { return c.done; }).length; }
  function progress() {
    var d = doneCount();
    bar.firstChild.style.width = Math.round(100 * d / nItems) + '%';
    var num = cur && cur.ctl ? set.items.indexOf(cur.ctl.id) + 1 : d;
    count.textContent = (sc.finished ? nItems : Math.max(num, 1)) + ' / ' + nItems;
  }
  function hideSheet() { sheet.className = 'sheet'; clear(sheet); sbar.classList.remove('x-hide'); }
  function showSheet(kind, title, lines, btnText, onBtn) {
    clear(sheet);
    sheet.className = 'sheet on ' + kind;
    sheet.appendChild(el('div', { 'class': 'sheet-in' },
      el('div', { 'class': 'sheet-head' }, icon(kind === 'ok' ? 'check' : kind === 'no' ? 'cross' : 'next', 24), el('b', null, title)),
      lines, el('button', { 'class': 'btn primary block', type: 'button', onclick: onBtn }, btnText)));
    sbar.classList.add('x-hide');
    var b = sheet.querySelector('button'); if (b) try { b.focus({ preventScroll: true }); } catch (e) { b.focus(); }
  }
  function refresh() {
    if (!cur) return;
    if (cur.ctl) {
      var c = cur.ctl;
      main.textContent = 'Check';
      main.disabled = c.done || !c.ready();
      reveal.disabled = c.done;
    } else {
      var all = cur.board.every(function (c) { return c.done; });
      main.textContent = at < steps.length - 1 ? 'Next' : 'Finish';
      main.disabled = !all;
      reveal.disabled = all;
    }
  }
  function afterItem(c) {
    progress();
    var it = c.item, lines = [];
    if (c.score > 0) {
      if (it.t === 'fix') lines.push(el('p', null, it.full));
      if (it.fb) lines.push(el('p', { 'class': 'sec' }, rich(it.fb)));
      showSheet('ok', c.tries <= 1 ? 'Great!' : 'Yes, good.', lines, at < steps.length - 1 ? 'Next' : 'Finish', next);
    } else {
      lines.push(el('p', null, 'The answer is: ', el('span', { 'class': 'ans' }, rich(rightText(it)))));
      if (it.fb) lines.push(el('p', { 'class': 'sec' }, rich(it.fb)));
      showSheet('no', c.revealed ? 'Here is the answer' : 'Not this time', lines, at < steps.length - 1 ? 'Next' : 'Finish', next);
    }
  }
  var hooks = {
    onChange: function () { refresh(); },
    onTry: function () { showSheet('try', 'Not quite. Try again.', [], 'Try again', function () { hideSheet(); refresh(); if (cur && cur.ctl && cur.ctl.focus) cur.ctl.focus(); }); },
    submit: function () { if (!main.disabled) main.click(); }
  };
  function show() {
    hideSheet();
    clear(stage);
    var st = steps[at];
    if (st.id) {
      var c = byId[st.id] || makeItem(st.id, 0, 'player', function (cc) { afterItem(cc); }, hooks);
      if (!byId[st.id]) { byId[st.id] = c; sc.ctls.push(c); }
      stage.appendChild(c.node);
      cur = { ctl: c };
      if (c.focus && !('ontouchstart' in window)) setTimeout(c.focus, 0);
    } else {
      var b = el('div', { 'class': 'pl-board' });
      var ctls = boardControllers(st.board, b, function () { progress(); refresh(); });
      ctls.forEach(function (c) { if (!byId[c.id]) { byId[c.id] = c; sc.ctls.push(c); } });
      stage.appendChild(b);
      cur = { board: ctls };
    }
    progress(); refresh();
  }
  function next() {
    if (at < steps.length - 1) { at++; show(); window.scrollTo(0, 0); return; }
    end();
  }
  function end() {
    sc.finished = true;
    var score = sc.ctls.reduce(function (a, c) { return a + c.score; }, 0);
    sc.score = score;
    if (!opts.noSave) {
      var prev = S.sets[set.id] || {};
      S.sets[set.id] = { s: score, n: nItems, best: Math.max(prev.best || 0, score), done: 1 };
      save();
    }
    progress();
    hideSheet();
    clear(stage); sbar.classList.add('x-hide'); instr.classList.add('x-hide');
    var wrong = sc.ctls.filter(function (c) { return c.score < 1; }).map(function (c) { return c.id; });
    var perfect = score === nItems;
    var box = el('div', { 'class': 'pl-end' + (perfect ? ' perfect' : '') });
    if (perfect) box.appendChild(celebrate());
    box.appendChild(el('p', { 'class': 'label' }, 'Your score'));
    box.appendChild(el('p', { 'class': 'score-big' }, fmtScore(score) + ' / ' + nItems));
    box.appendChild(el('p', { 'class': 'sec' }, perfect ? 'Perfect! Every answer is right.' : score >= nItems * 0.7 ? 'Good work!' : 'Keep going — practise your mistakes.'));
    var btns = el('div', { 'class': 'pl-end-btns' });
    if (wrong.length) btns.appendChild(el('button', { 'class': 'btn ' + (opts.onNext ? 'ghost' : 'primary') + ' block', type: 'button', onclick: function () {
      var ws = { id: set.id + ':again', k: set.k, instr: set.instr, items: wrong, groups: set.groups, bank: set.bank, lines: set.lines ? set.lines.filter(function (l) { return !l[2] || wrong.indexOf(l[2]) >= 0; }) : null };
      var n = playSet(ws, { onClose: opts.onClose, noSave: true, text: opts.text });
      P.parentNode.replaceChild(n, P);
    } }, 'Practise my mistakes'));
    if (opts.onNext) btns.appendChild(el('button', { 'class': 'btn primary block', type: 'button', onclick: opts.onNext }, 'Next set', icon('next', 18)));
    btns.appendChild(el('button', { 'class': 'btn ghost block', type: 'button', onclick: function () { if (opts.onClose) opts.onClose(); } }, 'Back to the list'));
    box.appendChild(btns);
    stage.appendChild(box);
    if (opts.onFinish) opts.onFinish(sc);
  }
  main.addEventListener('click', function () {
    if (!cur) return;
    if (cur.ctl) { if (!cur.ctl.done && cur.ctl.ready()) cur.ctl.check(); refresh(); return; }
    next();
  });
  reveal.addEventListener('click', function () {
    if (!cur) return;
    if (cur.ctl) { if (!cur.ctl.done) { cur.ctl.revealed = true; cur.ctl.reveal(); } return; }
    for (var i = 0; i < cur.board.length; i++) if (!cur.board[i].done) { cur.board[i].reveal(); break; }
    refresh();
  });
  P.addEventListener('click', function () { setTimeout(refresh, 0); });
  P.addEventListener('input', function () { setTimeout(refresh, 0); });
  // test hook: answer every step (ok(index) says right or wrong) and finish
  sc.autoplay = function (ok) {
    var k = 0, guard = 0;
    while (!sc.finished && guard++ < 200) {
      if (cur.ctl) {
        var c = cur.ctl, want = ok(k++), g2 = 0;
        if (!c.done) { c.autoAnswer(want); while (!c.done && g2++ < 4) c.autoAnswer(false); }
      } else cur.board.forEach(function (c) { var want = ok(k++), g2 = 0; if (!c.done) { c.autoAnswer(want); while (!c.done && g2++ < 4) c.autoAnswer(false); } });
      next();
    }
    return sc;
  };
  SETREG[set.id] = sc;
  show();
  return P;
}
function celebrate() {
  var b = '';
  var cols = ['#2EC4B6', '#A78BFA', '#FFB347', '#FF6B6B'];
  for (var i = 0; i < 18; i++) {
    var x = 20 + (i * 37) % 280, y = 10 + (i * 23) % 60, r = (i * 47) % 360;
    b += '<rect x="' + x + '" y="' + y + '" width="8" height="14" rx="2" fill="' + cols[i % 4] + '" transform="rotate(' + r + ' ' + (x + 4) + ' ' + (y + 7) + ')"/>';
  }
  return el('div', { 'class': 'confetti', 'aria-hidden': 'true' }, svgNode('<svg viewBox="0 0 320 80">' + b + '</svg>'));
}

/* ---------- set list rows (title, item count, best score) ---------- */
function setRow(set, n, onOpen) {
  var best = S.sets[set.id];
  var done = best && best.done;
  return el('button', { 'class': 'set-row' + (done ? ' done' : ''), type: 'button', onclick: onOpen },
    el('span', { 'class': 'ti' }, icon(TYPE_ICON[set.k] || 'choose', 22)),
    el('span', { 'class': 'set-row-t' }, el('b', null, set.instr)),
    done ? null : el('span', { 'class': 'sec small-t nowrap' }, set.items.length + ' Qs'),
    done ? el('span', { 'class': 'badge ok' }, fmtScore(best.best) + ' / ' + best.n) : el('span', { 'class': 'set-go' }, icon('next', 20)));
}

/* ---------- test player (unit test, level review): no feedback until the end ---------- */
function renderTest(ids, opts) {
  var box = el('div', { 'class': 'player test' });
  var ctls = ids.map(function (id, i) { return makeItem(id, 0, 'test', null); });
  var at = 0;
  var bar = el('div', { 'class': 'pbar coral' }, el('i', { style: 'width:0%' }));
  var count = el('span', { 'class': 'pl-count' });
  var closeB = el('button', { 'class': 'icon-btn', type: 'button', 'aria-label': 'Close', onclick: function () { if (opts.onClose) opts.onClose(); } }, icon('cross', 22));
  box.appendChild(el('div', { 'class': 'pl-top' }, closeB, bar, count));
  var strip = el('div', { 'class': 'qstrip', role: 'group', 'aria-label': 'Questions' });
  var sbtn = ids.map(function (_, i) { var b = el('button', { type: 'button', 'aria-label': 'Question ' + (i + 1), onclick: function () { at = i; show(); } }, String(i + 1)); strip.appendChild(b); return b; });
  box.appendChild(strip);
  box.appendChild(el('p', { 'class': 'pl-instr' }, icon('test', 20), (opts.title || 'Test') + ' — no hints. You see your score at the end.'));
  var stage = el('div', { 'class': 'pl-stage' });
  box.appendChild(stage);
  var back = el('button', { 'class': 'btn ghost', type: 'button', onclick: function () { if (at > 0) { at--; show(); } } }, icon('back', 18), 'Back');
  var fwd = el('button', { 'class': 'btn primary', type: 'button' }, 'Next');
  var sbar = el('div', { 'class': 'pl-bar' }, el('div', { 'class': 'pl-bar-in' }, back, fwd));
  box.appendChild(sbar);
  function answered(c) { return !!c.answered; }
  function marks() {
    var n = ctls.filter(answered).length;
    bar.firstChild.style.width = Math.round(100 * n / ids.length) + '%';
    count.textContent = (at + 1) + ' / ' + ids.length;
    sbtn.forEach(function (b, i) { b.className = (i === at ? 'cur ' : '') + (answered(ctls[i]) ? 'ans' : ''); b.setAttribute('aria-current', i === at ? 'step' : 'false'); });
    fwd.textContent = at < ids.length - 1 ? 'Next' : 'Finish';
    back.disabled = at === 0;
  }
  function show() {
    clear(stage);
    stage.appendChild(ctls[at].node);
    marks();
    var cb = sbtn[at]; if (cb && cb.scrollIntoView) try { cb.scrollIntoView({ block: 'nearest', inline: 'center' }); } catch (e) {}
  }
  box.addEventListener('click', function () { setTimeout(marks, 0); });
  box.addEventListener('input', function () { setTimeout(marks, 0); });
  fwd.addEventListener('click', function () {
    if (at < ids.length - 1) { at++; show(); return; }
    var empty = ctls.filter(function (c) { return !answered(c); }).length;
    if (empty && !fwd.dataset.sure) { fwd.dataset.sure = '1'; fwd.textContent = empty + ' not answered. Finish?'; return; }
    finish();
  });
  function finish() {
    var res = ctls.map(function (c) { var r = c.result(); return { id: c.id, ok: r.ok, your: r.your }; });
    var right = res.filter(function (r) { return r.ok; }).length;
    res.forEach(function (r) { recordAttempt(r.id, r.ok, r.your); });
    var pct = Math.round(100 * right / ids.length);
    if (opts.onDone) opts.onDone(pct, right);
    clear(box);
    var rc = el('section', { 'class': 'card', id: 'test-results' });
    if (pct === 100) rc.appendChild(celebrate());
    rc.appendChild(el('p', { 'class': 'label' }, opts.title || 'Test'));
    rc.appendChild(el('h2', null, 'Your score: ' + right + ' / ' + ids.length + ' (' + pct + '%)'));
    rc.appendChild(starsText(starsFor(pct)));
    var wrong = res.filter(function (r) { return !r.ok; });
    if (wrong.length) {
      rc.appendChild(el('h3', { 'class': 'mt' }, 'Check these:'));
      var ul = el('ul', { 'class': 'result-list' });
      wrong.forEach(function (r) {
        var it = atom(ITEMS[r.id]);
        ul.appendChild(el('li', null, el('div', { 'class': 'small-t sec' }, 'Question ' + (ids.indexOf(r.id) + 1)), el('div', null, rich(promptText(it))), el('div', { 'class': 'small-t' }, el('span', { 'class': 'wrong-t' }, r.your), '  →  ', el('span', { 'class': 'right-t' }, rightText(it)))));
      });
      rc.appendChild(ul);
    } else rc.appendChild(el('p', { 'class': 'right-t' }, 'Everything is right. Fantastic!'));
    var btns = el('div', { 'class': 'pl-end-btns' });
    if (wrong.length) btns.appendChild(el('button', { 'class': 'btn primary block', type: 'button', onclick: function () {
      var ws = { id: 'test:again', k: 'mix', instr: 'Practise your test mistakes.', items: wrong.map(function (r) { return r.id; }) };
      var n = playSet(ws, { onClose: opts.onClose, noSave: true });
      box.parentNode.replaceChild(n, box);
    } }, 'Practise my mistakes'));
    btns.appendChild(el('button', { 'class': 'btn ghost block', type: 'button', onclick: function () { var n = renderTest(ids, opts); box.parentNode.replaceChild(n, box); } }, 'Take it again'));
    rc.appendChild(btns);
    box.appendChild(rc);
    window.scrollTo(0, 0);
  }
  box.__ctls = ctls;
  box.__finish = function () { fwd.dataset.sure = '1'; at = ids.length - 1; finish(); };
  show();
  return box;
}
function starsFor(pct) { return pct >= 90 ? 3 : pct >= 70 ? 2 : pct >= 50 ? 1 : 0; }
