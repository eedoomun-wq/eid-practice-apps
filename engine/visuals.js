/* ===== visuals.js: drawn grammar visuals (inline SVG + CSS diagrams) ===== */
var COL = { teal: ['#E8FAF8', '#2EC4B6', '#166F68'], purple: ['#F3EFFF', '#A78BFA', '#6D4FD1'],
  amber: ['#FFF8EC', '#FFB347', '#8A5300'], coral: ['#FFF0F0', '#FF6B6B', '#C23B3B'], grey: ['#FAFAFA', '#C9D3DB', '#2D3436'],
  ok: ['#EAF6EA', '#4CAF50', '#388E3C'] };
function C(name, i) { return (COL[name] || COL.teal)[i]; }
var TX = 'font-family="Nunito, Varela Round, system-ui, sans-serif" font-weight="800"';

function svgWrap(w, h, body, label) {
  return '<svg viewBox="0 0 ' + w + ' ' + h + '" role="img" aria-label="' + escXml(label || 'diagram') + '" xmlns="http://www.w3.org/2000/svg">' + body + '</svg>';
}
function t(x, y, s, size, fill, anchor, weight) {
  return '<text x="' + x + '" y="' + y + '" ' + TX + ' font-size="' + (size || 15) + '" fill="' + (fill || '#2D3436') + '" text-anchor="' + (anchor || 'middle') + '"' + (weight ? ' font-weight="' + weight + '"' : '') + '>' + escXml(s) + '</text>';
}
function wrapText(s, max) {
  var words = String(s).split(' '), lines = [], cur = '';
  words.forEach(function (w) { if ((cur + ' ' + w).trim().length > max) { if (cur) lines.push(cur); cur = w; } else cur = (cur + ' ' + w).trim(); });
  if (cur) lines.push(cur);
  return lines;
}
function tLines(x, y, s, max, size, fill, anchor) {
  return wrapText(s, max).map(function (l, i) { return t(x, y + i * (size + 3), l, size, fill, anchor); }).join('');
}
function person(x, y, c) {
  return '<circle cx="' + x + '" cy="' + (y - 34) + '" r="11" fill="' + C(c, 0) + '" stroke="' + C(c, 2) + '" stroke-width="2.5"/>' +
    '<path d="M' + (x - 14) + ' ' + y + ' q14 -32 28 0" fill="' + C(c, 1) + '" stroke="' + C(c, 2) + '" stroke-width="2.5"/>';
}
function thing(x, y, kind, c) {
  c = c || 'amber';
  if (kind === 'cup') return '<path d="M' + (x - 9) + ' ' + (y - 16) + 'h18l-2 16h-14z" fill="' + C(c, 1) + '" stroke="' + C(c, 2) + '" stroke-width="2"/>';
  if (kind === 'book') return '<rect x="' + (x - 9) + '" y="' + (y - 18) + '" width="18" height="18" rx="2" fill="' + C(c, 1) + '" stroke="' + C(c, 2) + '" stroke-width="2"/>';
  return '<rect x="' + (x - 10) + '" y="' + (y - 16) + '" width="20" height="16" rx="4" fill="' + C(c, 1) + '" stroke="' + C(c, 2) + '" stroke-width="2"/><path d="M' + (x - 5) + ' ' + (y - 16) + 'q5 -8 10 0" fill="none" stroke="' + C(c, 2) + '" stroke-width="2"/>';
}

var VIS = {};

VIS.table = function (v) {
  // wide tables (3+ columns with sentences) become labelled cards on phones
  var longest = 0;
  v.rows.forEach(function (r) { r.forEach(function (c) { longest = Math.max(longest, plain(c).length); }); });
  var stack = (v.rows[0] || []).length >= 3 && longest > 14;
  var tb = el('table', { 'class': 'vtable' + (stack ? ' stack' : '') });
  if (v.head) tb.appendChild(el('tr', { 'class': 'vhead' }, v.head.map(function (h) { return el('th', null, rich(h)); })));
  v.rows.forEach(function (r) {
    tb.appendChild(el('tr', null, r.map(function (cell, i) {
      var c = (v.colors && v.colors[i]) || 'white';
      var h = v.head && v.head[i] ? plain(v.head[i]) : '';
      return el('td', { 'class': 'c-' + c + (cell ? '' : ' empty'), 'data-h': h || null }, rich(cell));
    })));
  });
  return tb;
};

VIS.compare = function (v) {
  var g = el('div', { 'class': 'cmp-cols' });
  v.cols.forEach(function (c) {
    g.appendChild(el('div', { 'class': 'col-box', style: 'border-color:' + C(c.color || 'teal', 1) + ';background:' + C(c.color || 'teal', 0) },
      el('h4', { style: 'color:' + C(c.color || 'teal', 2) }, rich(c.title)),
      c.note ? el('div', { 'class': 'small-t sec' }, rich(c.note)) : null,
      el('div', { 'class': 'chips mt8' }, (c.items || []).map(function (x) { return el('span', { 'class': 'chip' + (plain(x).length > 16 ? ' long' : '') }, rich(x)); }))));
  });
  return g;
};

VIS.chips = function (v) {
  var d = el('div');
  v.groups.forEach(function (gr) {
    d.appendChild(el('div', { style: 'margin-bottom:8px' }, el('b', { style: 'color:' + C(gr.color || 'purple', 2) }, rich(gr.title || '')),
      el('div', { 'class': 'chips', style: 'margin-top:4px' }, gr.items.map(function (x) {
        return el('span', { 'class': 'chip', style: 'border-color:' + C(gr.color || 'purple', 1) }, rich(x)); }))));
  });
  return d;
};

VIS.hands = function (v) {
  var o = v.obj || 'bag', L = v.labels || {};
  var panels = [['this', 1, true], ['these', 3, true], ['that', 1, false], ['those', 3, false]];
  var body = '';
  panels.forEach(function (p, i) {
    var ox = (i % 2) * 180, oy = Math.floor(i / 2) * 130;
    body += '<rect x="' + (ox + 4) + '" y="' + (oy + 4) + '" width="172" height="122" rx="14" fill="#fff" stroke="#E3E8EE" stroke-width="2"/>';
    body += person(ox + 34, oy + 98, 'teal');
    var near = p[2], cx = near ? ox + 72 : ox + 140;
    body += '<path d="M' + (ox + 44) + ' ' + (oy + 74) + ' L' + (cx - 14) + ' ' + (oy + 74) + '" stroke="#166F68" stroke-width="3" stroke-linecap="round"' + (near ? '' : ' stroke-dasharray="5 5"') + '/>';
    for (var k = 0; k < p[1]; k++) body += thing(cx + (p[1] > 1 ? (k - 1) * 14 : 0), oy + 84 - (p[1] > 1 && k === 1 ? 6 : 0), o, 'amber');
    body += t(ox + 90, oy + 26, p[0], 20, near ? '#166F68' : '#6D4FD1');
    body += t(ox + 90, oy + 116, (near ? 'near' : 'far') + ' · ' + (p[1] > 1 ? 'more than one' : 'one'), 12, '#636E72');
  });
  var box = el('div');
  box.appendChild(svgNode(svgWrap(360, 264, body, 'this, these, that, those: near and far')));
  var caps = panels.filter(function (p) { return L[p[0]]; }).map(function (p) { return el('div', null, el('b', null, p[0] + ': '), rich(L[p[0]])); });
  if (caps.length) box.appendChild(el('div', { 'class': 'vcap', style: 'text-align:left' }, caps));
  return box;
};

VIS.street = function (v) {
  var top = v.top || [], bot = v.bottom || [];
  var n = Math.max(top.length, bot.length), w = 360, bw = Math.floor((w - 16) / n);
  var body = '<rect x="0" y="0" width="360" height="250" rx="16" fill="#F5F7FA"/>';
  body += '<rect x="0" y="108" width="360" height="40" fill="#C9D3DB"/>';
  for (var i = 0; i < 9; i++) body += '<rect x="' + (i * 42 + 6) + '" y="126" width="22" height="4" rx="2" fill="#fff"/>';
  body += t(350, 122, v.street || 'Main Street', 12, '#2D3436', 'end');
  var cols = ['teal', 'purple', 'amber', 'coral', 'teal', 'purple'];
  function row(names, y, h) {
    names.forEach(function (nm, i) {
      if (!nm) return;
      var x = 8 + i * bw, c = cols[(i + (y > 100 ? 2 : 0)) % cols.length];
      body += '<rect x="' + (x + 2) + '" y="' + y + '" width="' + (bw - 4) + '" height="' + h + '" rx="8" fill="' + C(c, 0) + '" stroke="' + C(c, 1) + '" stroke-width="2.5"/>';
      body += '<rect x="' + (x + bw / 2 - 8) + '" y="' + (y + h - (y > 100 ? h : 0) - (y > 100 ? 0 : 22)) + '" width="16" height="22" rx="3" fill="' + C(c, 1) + '"/>';
      wrapText(nm, Math.max(6, Math.floor(bw / 9))).forEach(function (l, k) { body += t(x + bw / 2, y + (y > 100 ? 44 : 30) + k * 15, l, 13, C(c, 2)); });
    });
  }
  row(top, 12, 90);
  row(bot, 154, 90);
  var box = el('div');
  box.appendChild(svgNode(svgWrap(360, 250, body, 'street map')));
  if (v.notes) box.appendChild(el('div', { 'class': 'vcap', style: 'text-align:left' }, v.notes.map(function (s) { return el('div', null, rich(s)); })));
  return box;
};

VIS.box = function (v) {
  var pos = { 'in': [0, 0], 'on': [0, -30], 'under': [0, 34], 'next to': [32, 0], 'behind': [12, -12], 'in front of': [-6, 18], 'near': [50, 0], 'between': [0, 0], 'opposite': [0, 0] };
  var items = v.items, cols = 3, cw = 120, ch = 120, rows = Math.ceil(items.length / cols);
  var body = '';
  items.forEach(function (it, i) {
    var x = (i % cols) * cw, y = Math.floor(i / cols) * ch, k = it[0], cx = x + 50, cy = y + 66;
    body += '<rect x="' + (x + 3) + '" y="' + (y + 3) + '" width="' + (cw - 6) + '" height="' + (ch - 6) + '" rx="12" fill="#fff" stroke="#E3E8EE" stroke-width="2"/>';
    var ball = function (bx, by) { return '<circle cx="' + bx + '" cy="' + by + '" r="9" fill="#FF6B6B" stroke="#C23B3B" stroke-width="2"/>'; };
    var boxs = function (bx) { return '<rect x="' + (bx - 22) + '" y="' + (cy - 18) + '" width="44" height="36" rx="4" fill="#E8FAF8" stroke="#22A99D" stroke-width="2.5"/>'; };
    if (k === 'between') {
      body += boxs(cx - 22) + boxs(cx + 42) + ball(cx + 10, cy);
    } else if (k === 'opposite') {
      body += boxs(cx - 18) + '<path d="M' + (x + 8) + ' ' + (cy + 24) + 'h' + (cw - 16) + '" stroke="#C9D3DB" stroke-width="6"/>' + ball(cx + 46, cy + 36) + '<rect x="' + (cx + 34) + '" y="' + (cy + 30) + '" width="1" height="1" fill="none"/>';
    } else if (k === 'behind') {
      body += ball(cx + 14, cy - 14) + boxs(cx);
    } else {
      var p = pos[k] || [0, 0];
      if (k === 'in') body += boxs(cx) + ball(cx, cy + 4);
      else body += boxs(cx) + ball(cx + p[0], cy + p[1]);
    }
    body += t(x + cw / 2, y + 24, k, 16, '#6D4FD1');
  });
  var box = el('div');
  box.appendChild(svgNode(svgWrap(cols * cw, rows * ch, body, 'prepositions of place')));
  if (v.notes) box.appendChild(el('div', { 'class': 'vcap', style: 'text-align:left' }, v.notes.map(function (s) { return el('div', null, rich(s)); })));
  return box;
};

VIS.scale = function (v) {
  var body = '<defs><linearGradient id="sg" x1="0" x2="1"><stop offset="0" stop-color="#FFF0F0"/><stop offset="1" stop-color="#E8FAF8"/></linearGradient></defs>';
  body += '<rect x="20" y="40" width="320" height="26" rx="13" fill="url(#sg)" stroke="#C9D3DB" stroke-width="2"/>';
  body += t(20, 30, '0%', 13, '#636E72', 'start') + t(340, 30, '100%', 13, '#636E72', 'end');
  v.items.forEach(function (it, i) {
    var x = 20 + 320 * it[1] / 100, y = 92 + (i % 2) * 34;
    body += '<circle cx="' + x + '" cy="53" r="7" fill="#7C5CE8"/><path d="M' + x + ' 60 V' + (y - 14) + '" stroke="#A78BFA" stroke-width="2"/>';
    body += t(Math.min(330, Math.max(30, x)), y, it[0], 14, '#6D4FD1') + t(Math.min(330, Math.max(30, x)), y + 14, it[1] + '%', 11, '#636E72');
  });
  return svgNode(svgWrap(360, 150, body, 'frequency scale from 0 to 100 percent'));
};

VIS.timeline = function (v) {
  var X = function (a) { return 180 + a * 50; };
  var body = '<path d="M14 80 H346" stroke="#2D3436" stroke-width="3"/><path d="M346 80 l-10 -6 v12z" fill="#2D3436"/>';
  body += t(24, 104, 'past', 13, '#636E72', 'start') + t(336, 104, 'future', 13, '#636E72', 'end');
  body += '<rect x="168" y="62" width="24" height="36" rx="6" fill="#FFB347"/>' + t(180, 118, v.now || 'now', 14, '#8A5300');
  if (v.span) {
    var a = X(v.span.from), b = X(v.span.to);
    body += '<rect x="' + Math.min(a, b) + '" y="70" width="' + Math.abs(b - a) + '" height="20" rx="10" fill="#A78BFA" opacity=".55"/>';
    body += t((a + b) / 2, 58, v.span.label || '', 13, '#6D4FD1');
  }
  (v.marks || []).slice().sort(function (a, b) { return a.at - b.at; }).forEach(function (m, i) {
    var x = X(m.at), up = i % 2 === 0;
    body += '<circle cx="' + x + '" cy="80" r="8" fill="' + (m.at < 0 ? '#FF6B6B' : m.at > 0 ? '#2EC4B6' : '#FFB347') + '" stroke="#2D3436" stroke-width="2"/>';
    var ty = up ? 36 : 140;
    body += '<path d="M' + x + ' ' + (up ? 70 : 90) + ' V' + (up ? ty + 6 : ty - 18) + '" stroke="#C9D3DB" stroke-width="2"/>';
    body += t(Math.min(340, Math.max(26, x)), up ? ty - 12 : ty, m.label, 13, '#2D3436');
    if (m.text) body += t(Math.min(300, Math.max(60, x)), up ? ty + 4 : ty + 15, m.text, 12, '#636E72');
  });
  return svgNode(svgWrap(360, 170, body, 'timeline: past, now, future'));
};

VIS.bars = function (v) {
  var max = Math.max.apply(null, v.items.map(function (i) { return i[1]; }));
  var h = 40 + v.items.length * 44, body = '';
  var cs = ['teal', 'purple', 'amber', 'coral'];
  v.items.forEach(function (it, i) {
    var y = 20 + i * 44, w = 200 * it[1] / max, c = cs[i % cs.length];
    body += t(10, y + 21, it[0], 14, '#2D3436', 'start');
    body += '<rect x="110" y="' + (y + 4) + '" width="' + w + '" height="26" rx="8" fill="' + C(c, 1) + '"/>';
    if (it[2]) body += t(Math.min(350, 116 + w), y + 22, it[2], 13, C(c, 2), w > 150 ? 'end' : 'start');
  });
  var box = el('div');
  box.appendChild(svgNode(svgWrap(360, h, body, 'size bars')));
  if (v.cap) box.appendChild(el('div', { 'class': 'vcap' }, rich(v.cap)));
  return box;
};

VIS.jars = function (v) {
  var body = '';
  [v.left, v.right].forEach(function (j, i) {
    var x = i * 180 + 20, c = i ? 'purple' : 'teal';
    body += '<path d="M' + (x + 20) + ' 40 h100 v12 q20 10 20 40 v120 q0 18 -18 18 h-104 q-18 0 -18 -18 v-120 q0 -30 20 -40z" fill="' + C(c, 0) + '" stroke="' + C(c, 1) + '" stroke-width="3"/>';
    body += '<rect x="' + (x + 14) + '" y="26" width="112" height="16" rx="5" fill="' + C(c, 1) + '"/>';
    body += t(x + 70, 18, j.title, 15, C(c, 2));
    j.items.slice(0, 7).forEach(function (s, k) { body += t(x + 70, 82 + k * 20, s, 13, '#2D3436'); });
  });
  return svgNode(svgWrap(360, 236, body, 'two jars: ' + v.left.title + ' and ' + v.right.title));
};

VIS.tree = function (v) {
  var gens = v.gen, H = gens.length * 92 + 10, body = '', centers = [];
  gens.forEach(function (row, gi) {
    var n = row.length, w = 360 / n, cs = [];
    row.forEach(function (p, i) {
      var cx = w * i + w / 2, y = 14 + gi * 92, c = p.c || (gi === 0 ? 'amber' : gi === 1 ? 'teal' : 'purple');
      cs.push(cx);
      body += '<rect x="' + (cx - Math.min(56, w / 2 - 4)) + '" y="' + y + '" width="' + Math.min(112, w - 8) + '" height="54" rx="12" fill="' + C(c, 0) + '" stroke="' + C(c, 1) + '" stroke-width="2.5"/>';
      body += t(cx, y + 23, p.name, 14, '#2D3436');
      if (p.cap) body += t(cx, y + 42, p.cap, 11, C(c, 2));
    });
    centers.push(cs);
  });
  for (var g = 1; g < gens.length; g++) {
    var pc = centers[g - 1], mid = (pc[0] + pc[pc.length > 1 ? 1 : 0]) / 2, y0 = 14 + (g - 1) * 92 + 54, y1 = 14 + g * 92;
    if (pc.length > 1) body += '<path d="M' + pc[0] + ' ' + (y0 - 27) + ' H' + pc[1] + '" stroke="#C9D3DB" stroke-width="3"/>';
    body += '<path d="M' + mid + ' ' + y0 + ' V' + (y0 + 14) + '" stroke="#C9D3DB" stroke-width="3"/>';
    var cs2 = centers[g];
    body += '<path d="M' + cs2[0] + ' ' + (y0 + 14) + ' H' + cs2[cs2.length - 1] + '" stroke="#C9D3DB" stroke-width="3"/>';
    cs2.forEach(function (x) { body += '<path d="M' + x + ' ' + (y0 + 14) + ' V' + y1 + '" stroke="#C9D3DB" stroke-width="3"/>'; });
  }
  var box = el('div');
  box.appendChild(svgNode(svgWrap(360, H, body, 'family tree')));
  if (v.notes) box.appendChild(el('div', { 'class': 'vcap', style: 'text-align:left' }, v.notes.map(function (s) { return el('div', null, rich(s)); })));
  return box;
};

function clockFace(cx, cy, r, hh, mm, c) {
  var s = '<circle cx="' + cx + '" cy="' + cy + '" r="' + r + '" fill="#fff" stroke="' + C(c, 1) + '" stroke-width="4"/>';
  for (var i = 0; i < 12; i++) {
    var a = i * Math.PI / 6, x1 = cx + Math.sin(a) * (r - 6), y1 = cy - Math.cos(a) * (r - 6), x2 = cx + Math.sin(a) * (r - (i % 3 ? 10 : 14)), y2 = cy - Math.cos(a) * (r - (i % 3 ? 10 : 14));
    s += '<path d="M' + x1.toFixed(1) + ' ' + y1.toFixed(1) + ' L' + x2.toFixed(1) + ' ' + y2.toFixed(1) + '" stroke="#2D3436" stroke-width="' + (i % 3 ? 1.5 : 3) + '"/>';
  }
  var ha = ((hh % 12) + mm / 60) * Math.PI / 6, ma = mm * Math.PI / 30;
  s += '<path d="M' + cx + ' ' + cy + ' L' + (cx + Math.sin(ha) * r * .5).toFixed(1) + ' ' + (cy - Math.cos(ha) * r * .5).toFixed(1) + '" stroke="#2D3436" stroke-width="5" stroke-linecap="round"/>';
  s += '<path d="M' + cx + ' ' + cy + ' L' + (cx + Math.sin(ma) * r * .78).toFixed(1) + ' ' + (cy - Math.cos(ma) * r * .78).toFixed(1) + '" stroke="' + C(c, 2) + '" stroke-width="3.5" stroke-linecap="round"/>';
  return s + '<circle cx="' + cx + '" cy="' + cy + '" r="4" fill="#2D3436"/>';
}
VIS.clocks = function (v) {
  var n = v.times.length, per = Math.min(3, n), rows = Math.ceil(n / per), w = 360 / per, body = '';
  var cs = ['teal', 'purple', 'amber', 'coral'];
  var maxc = Math.floor(w / 7.2);
  var lines = Math.max.apply(null, v.times.map(function (tm) { return wrapText(tm[1], maxc).length; }));
  var rowH = 146 + lines * 15;
  v.times.forEach(function (tm, i) {
    var p = tm[0].split(':'), cx = (i % per) * w + w / 2, y = Math.floor(i / per) * rowH;
    var h12 = (+p[0]) % 12 || 12;
    body += clockFace(cx, y + 62, 52, +p[0], +p[1], cs[i % 4]);
    body += t(cx, y + 136, h12 + ':' + p[1], 16, '#2D3436');
    body += tLines(cx, y + 154, tm[1], maxc, 12, '#636E72');
  });
  return svgNode(svgWrap(360, rows * rowH + 4, body, 'clocks: ' + v.times.map(function (x) { return x[0] + ' ' + x[1]; }).join(', ')));
};

VIS.letters = function (v) {
  var d = el('div', { 'class': 'pattern' });
  var cs = ['teal', 'purple', 'amber', 'coral', 'teal', 'purple', 'amber'];
  v.groups.forEach(function (g, i) {
    d.appendChild(el('div', { 'class': 'prow' },
      g[0].split(' ').map(function (L) { return el('span', { 'class': 'blk', style: 'background:' + C(cs[i], 0) + ';border:2px solid ' + C(cs[i], 1) + ';min-width:40px;justify-content:center;font-size:1.2rem' }, L); }),
      el('span', { 'class': 'blk r' }, rich(g[1]))));
  });
  return d;
};

VIS.faces = function (v) {
  var n = v.items.length, w = 360 / n, body = '';
  v.items.forEach(function (it, i) {
    var cx = w * i + w / 2, mood = it[1], c = mood === 'happy' ? 'teal' : mood === 'sad' ? 'coral' : 'amber';
    body += '<circle cx="' + cx + '" cy="50" r="34" fill="' + C(c, 0) + '" stroke="' + C(c, 1) + '" stroke-width="3"/>';
    body += '<circle cx="' + (cx - 11) + '" cy="42" r="4" fill="#2D3436"/><circle cx="' + (cx + 11) + '" cy="42" r="4" fill="#2D3436"/>';
    var m = mood === 'happy' ? 'q14 14 28 0' : mood === 'sad' ? 'q14 -12 28 0' : 'h28';
    body += '<path d="M' + (cx - 14) + ' ' + (mood === 'sad' ? 68 : 60) + ' ' + m + '" fill="none" stroke="#2D3436" stroke-width="3" stroke-linecap="round"/>';
    body += t(cx, 108, it[0], 14, C(c, 2));
  });
  return svgNode(svgWrap(360, 120, body, v.items.map(function (x) { return x[0]; }).join(', ')));
};

VIS.calendar = function (v) {
  var body = '<rect x="20" y="10" width="320" height="200" rx="14" fill="#fff" stroke="#A78BFA" stroke-width="3"/>' +
    '<rect x="20" y="10" width="320" height="40" rx="14" fill="#A78BFA"/>' + t(180, 37, v.title || '', 18, '#2D3436');
  var days = v.days || [];
  days.forEach(function (d, i) {
    var x = 40 + (i % 7) * 42, y = 70 + Math.floor(i / 7) * 34, on = v.mark && v.mark.indexOf(d) >= 0;
    if (on) body += '<circle cx="' + (x + 7) + '" cy="' + (y - 5) + '" r="14" fill="#FFB347"/>';
    body += t(x + 7, y, d, 13, on ? '#2D3436' : '#636E72');
  });
  var box = el('div');
  box.appendChild(svgNode(svgWrap(360, 220, body, 'calendar')));
  if (v.notes) box.appendChild(el('div', { 'class': 'vcap' }, v.notes.map(function (s) { return el('div', null, rich(s)); })));
  return box;
};

function renderVisual(v) {
  if (!v) return null;
  var f = VIS[v.type];
  var box = el('div', { 'class': 'visual' });
  if (!f) return null;
  box.appendChild(f(v));
  if (v.cap && v.type !== 'bars') box.appendChild(el('div', { 'class': 'vcap' }, rich(v.cap)));
  return box;
}

/* Small drawings for the Learn Smarter slides */
function smartArt(name) {
  var b = '';
  switch (name) {
    case 'card': b = '<rect x="60" y="20" width="200" height="120" rx="14" fill="#F3EFFF" stroke="#A78BFA" stroke-width="3"/>' + t(160, 75, 'bakery', 28, '#6D4FD1') + t(160, 110, 'a shop that sells bread', 14, '#636E72'); break;
    case 'flip': b = '<rect x="30" y="30" width="120" height="90" rx="12" fill="#E8FAF8" stroke="#2EC4B6" stroke-width="3"/>' + t(90, 82, 'word', 20, '#166F68') + '<path d="M160 75 h30" stroke="#FFB347" stroke-width="5" stroke-linecap="round"/><path d="M185 64 l12 11 -12 11" fill="none" stroke="#FFB347" stroke-width="5" stroke-linecap="round"/><rect x="200" y="30" width="120" height="90" rx="12" fill="#F3EFFF" stroke="#A78BFA" stroke-width="3"/>' + t(260, 82, 'meaning', 18, '#6D4FD1'); break;
    case 'boxes': ['#FFF0F0', '#FFF8EC', '#E8FAF8'].forEach(function (c, i) { b += '<rect x="' + (20 + i * 100) + '" y="40" width="80" height="80" rx="12" fill="' + c + '" stroke="#C9D3DB" stroke-width="3"/>' + t(60 + i * 100, 88, 'Box ' + (i + 1), 16, '#2D3436'); }); break;
    case 'curve': b = '<path d="M30 130 V20 M30 130 H310" stroke="#2D3436" stroke-width="3"/><path d="M30 30 C70 110 110 120 150 125" fill="none" stroke="#FF6B6B" stroke-width="4"/><path d="M30 30 C60 50 90 40 110 35 C150 50 190 45 220 40 C260 50 290 48 310 46" fill="none" stroke="#2EC4B6" stroke-width="4"/>' + t(250, 30, 'with reviews', 13, '#166F68') + t(200, 120, 'no review', 13, '#C23B3B'); break;
    case 'calendar': for (var i = 0; i < 14; i++) b += '<rect x="' + (30 + (i % 7) * 40) + '" y="' + (30 + Math.floor(i / 7) * 50) + '" width="32" height="40" rx="8" fill="' + (i < 10 ? '#E8FAF8' : '#fff') + '" stroke="#2EC4B6" stroke-width="2"/>' + (i < 10 ? '<path d="M' + (38 + (i % 7) * 40) + ' ' + (52 + Math.floor(i / 7) * 50) + ' l6 6 10 -12" fill="none" stroke="#166F68" stroke-width="3"/>' : ''); break;
    case 'streak': b = '<path d="M160 140c-30 0-50-22-50-50 0-30 30-45 30-80 22 15 36 36 36 58 8-8 14-15 14-28 15 15 22 30 22 50 0 28-22 50-52 50z" fill="#FFB347" stroke="#8A5300" stroke-width="3"/>' + t(160, 112, '7', 34, '#2D3436'); break;
    case 'smile': b = '<circle cx="160" cy="80" r="56" fill="#E8FAF8" stroke="#2EC4B6" stroke-width="4"/><circle cx="140" cy="66" r="6" fill="#2D3436"/><circle cx="180" cy="66" r="6" fill="#2D3436"/><path d="M130 96 q30 26 60 0" fill="none" stroke="#2D3436" stroke-width="4" stroke-linecap="round"/>'; break;
    case 'notebook': b = '<rect x="90" y="16" width="140" height="130" rx="10" fill="#fff" stroke="#A78BFA" stroke-width="3"/><path d="M114 16 v130" stroke="#FF6B6B" stroke-width="2"/>' + [0, 1, 2, 3].map(function (k) { return '<path d="M124 ' + (48 + k * 24) + ' h90" stroke="#C9D3DB" stroke-width="3"/>'; }).join(''); break;
    case 'pattern': b = t(160, 60, 'He go ✗', 24, '#C62828') + t(160, 110, 'He goes ✓', 24, '#388E3C'); break;
    case 'chunks': b = '<rect x="30" y="50" width="90" height="50" rx="10" fill="#F3EFFF" stroke="#A78BFA" stroke-width="3"/>' + t(75, 81, 'take', 18, '#6D4FD1') + '<rect x="130" y="50" width="50" height="50" rx="10" fill="#E8FAF8" stroke="#2EC4B6" stroke-width="3"/>' + t(155, 81, 'a', 18, '#166F68') + '<rect x="190" y="50" width="100" height="50" rx="10" fill="#FFF8EC" stroke="#FFB347" stroke-width="3"/>' + t(240, 81, 'photo', 18, '#8A5300'); break;
    case 'three': [0, 1, 2].forEach(function (k) { b += '<circle cx="' + (90 + k * 70) + '" cy="80" r="26" fill="#E8FAF8" stroke="#2EC4B6" stroke-width="3"/>' + t(90 + k * 70, 88, String(k + 1), 22, '#166F68'); }); break;
    case 'slots': b = '<rect x="20" y="50" width="80" height="50" rx="10" fill="#E8FAF8" stroke="#2EC4B6" stroke-width="3"/>' + t(60, 81, 'I', 18) + '<rect x="110" y="50" width="80" height="50" rx="10" fill="#F3EFFF" stroke="#A78BFA" stroke-width="3"/>' + t(150, 81, 'am', 18, '#6D4FD1') + '<rect x="200" y="50" width="110" height="50" rx="10" fill="#fff" stroke="#C9D3DB" stroke-width="3"/>' + t(255, 81, 'a student.', 16); break;
    case 'swap': b = t(160, 60, 'I have 20 years ✗', 20, '#C62828') + t(160, 110, "I'm 20 ✓", 24, '#388E3C'); break;
    case 'list': b = '<rect x="90" y="16" width="140" height="130" rx="10" fill="#FFF0F0" stroke="#FF6B6B" stroke-width="3"/>' + [0, 1, 2].map(function (k) { return '<path d="M110 ' + (52 + k * 30) + ' l6 6 10 -12 M136 ' + (52 + k * 30) + ' h70" fill="none" stroke="#C23B3B" stroke-width="3"/>'; }).join(''); break;
    case 'walk': b = person(100, 130, 'teal') + '<path d="M130 50 h150 v50 h-110 l-20 16 v-16 h-20z" fill="#F3EFFF" stroke="#A78BFA" stroke-width="3"/>' + t(205, 82, "I'm at the bakery.", 13, '#6D4FD1'); break;
    case 'phone': b = '<rect x="125" y="14" width="70" height="132" rx="14" fill="#fff" stroke="#2D3436" stroke-width="4"/><circle cx="160" cy="80" r="18" fill="#FF6B6B"/>'; break;
    case 'shadow': b = '<rect x="40" y="30" width="140" height="90" rx="10" fill="#E8FAF8" stroke="#2EC4B6" stroke-width="3"/><path d="M100 60 l24 15 -24 15z" fill="#166F68"/>' + person(250, 130, 'purple'); break;
    case 'book': b = '<path d="M40 30 c40 -10 80 -10 120 10 c40 -20 80 -20 120 -10 v110 c-40 -10 -80 -10 -120 10 c-40 -20 -80 -20 -120 -10z" fill="#F3EFFF" stroke="#A78BFA" stroke-width="3"/><path d="M160 40 v110" stroke="#A78BFA" stroke-width="3"/>'; break;
    case 'stairs': b = '<path d="M30 140 h60 v-30 h60 v-30 h60 v-30 h60 v-30" fill="none" stroke="#2EC4B6" stroke-width="5"/>' + t(60, 132, 'A1', 14, '#166F68') + t(120, 102, 'A2', 14, '#166F68') + t(180, 72, 'B1', 14, '#166F68') + t(240, 42, 'B2', 14, '#166F68'); break;
    case 'magnifier': b = '<circle cx="140" cy="70" r="42" fill="#FFF8EC" stroke="#FFB347" stroke-width="6"/><path d="M170 100 l50 46" stroke="#8A5300" stroke-width="10" stroke-linecap="round"/>' + t(140, 78, '?', 34, '#8A5300'); break;
    case 'target': b = [56, 40, 24, 9].map(function (r, k) { return '<circle cx="160" cy="80" r="' + r + '" fill="' + (k % 2 ? '#fff' : '#FFF0F0') + '" stroke="#FF6B6B" stroke-width="3"/>'; }).join(''); break;
    case 'moon': b = '<path d="M190 30 a55 55 0 1 0 0 100 a45 45 0 1 1 0 -100z" fill="#F3EFFF" stroke="#7C5CE8" stroke-width="3"/>' + t(230, 50, 'z', 20, '#6D4FD1') + t(250, 30, 'z', 16, '#6D4FD1'); break;
    case 'check': b = '<circle cx="160" cy="80" r="56" fill="#EAF6EA" stroke="#4CAF50" stroke-width="4"/><path d="M130 82 l20 20 40 -44" fill="none" stroke="#388E3C" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>'; break;
    case 'pile': b = '<rect x="80" y="100" width="160" height="34" rx="10" fill="#FFF8EC" stroke="#FFB347" stroke-width="3"/><rect x="90" y="64" width="140" height="34" rx="10" fill="#F3EFFF" stroke="#A78BFA" stroke-width="3"/><rect x="100" y="28" width="120" height="34" rx="10" fill="#E8FAF8" stroke="#2EC4B6" stroke-width="3"/>'; break;
    default: b = '<circle cx="160" cy="80" r="50" fill="#F3EFFF"/>';
  }
  return svgNode(svgWrap(320, 160, b, name));
}
