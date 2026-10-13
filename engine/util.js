/* ===== util.js: DOM helpers, text, storage, icons ===== */
'use strict';
var DATA = JSON.parse(document.getElementById('app-data').textContent);
var ITEMS = DATA.items;

function el(tag, attrs) {
  var e = document.createElement(tag);
  if (attrs) {
    for (var k in attrs) {
      var v = attrs[k];
      if (v === null || v === undefined || v === false) continue;
      if (k === 'class') e.className = v;
      else if (k === 'text') e.textContent = v;
      else if (k.slice(0, 2) === 'on') e.addEventListener(k.slice(2), v);
      else e.setAttribute(k, v === true ? '' : v);
    }
  }
  for (var i = 2; i < arguments.length; i++) add(e, arguments[i]);
  return e;
}
function add(parent, c) {
  if (c === null || c === undefined || c === false) return parent;
  if (Array.isArray(c)) { c.forEach(function (x) { add(parent, x); }); return parent; }
  if (typeof c === 'string' || typeof c === 'number') parent.appendChild(document.createTextNode(String(c)));
  else parent.appendChild(c);
  return parent;
}
function clear(e) { while (e.firstChild) e.removeChild(e.firstChild); return e; }

var AR_RUN = /([؀-ۿ][؀-ۿ\s،؟0-9.,!?:()'"-]*[؀-ۿ.!?])/;
/* Rich text: {word} = highlighted word; Arabic runs get their own RTL span. Never uses innerHTML. */
function rich(text) {
  var frag = document.createDocumentFragment();
  String(text).split(/(\{[^{}]+\})/).forEach(function (part) {
    if (!part) return;
    if (part.charAt(0) === '{' && part.charAt(part.length - 1) === '}') {
      frag.appendChild(el('b', { 'class': 'hl' }, part.slice(1, -1)));
      return;
    }
    part.split(AR_RUN).forEach(function (p, i) {
      if (!p) return;
      if (i % 2 === 1) frag.appendChild(el('span', { dir: 'rtl', lang: 'ar', 'class': 'ar-inline' }, p));
      else frag.appendChild(document.createTextNode(p));
    });
  });
  return frag;
}
/* An Arabic line with English words inside: each English run is isolated LTR in the English font */
function arabicLine(text) {
  var d = el('div');
  String(text).split(/([A-Za-z](?:[A-Za-z0-9'’.,…?!=\/+\- ]*[A-Za-z0-9'’?!…])?)/).forEach(function (p, i) {
    if (!p) return;
    if (i % 2 === 1) d.appendChild(el('span', { 'class': 'en', dir: 'ltr', lang: 'en' }, p));
    else d.appendChild(document.createTextNode(p));
  });
  return d;
}
function plain(text) { return String(text).replace(/[{}]/g, ''); }

/* Same rules as buildlib/norm.py */
function norm(s) {
  s = String(s || '').toLowerCase();
  s = s.replace(/[‘’ʼ`´]/g, "'").replace(/[“”]/g, '"');
  s = s.replace(/[–—-]/g, ' ');
  s = s.replace(/\bcan't\b/g, 'can not').replace(/\bcannot\b/g, 'can not').replace(/\bwon't\b/g, 'will not').replace(/\bshan't\b/g, 'shall not');
  s = s.replace(/n't\b/g, ' not');
  s = s.replace(/'m\b/g, ' am').replace(/'re\b/g, ' are').replace(/'ve\b/g, ' have').replace(/'ll\b/g, ' will').replace(/'d like\b/g, ' would like');
  s = s.replace(/[.,!?;:"()…]/g, ' ');
  return s.replace(/\s+/g, ' ').trim();
}
function matches(input, acc) {
  var n = norm(input);
  if (!n) return false;
  for (var i = 0; i < acc.length; i++) if (norm(acc[i]) === n) return true;
  return false;
}

/* ---------- storage: one key per app, every access wrapped ---------- */
var STORE_OK = true;
function defaultState() {
  return { v: 1, words: {}, items: {}, pile: {}, mistakes: [], sets: {}, tests: {}, secs: {}, streak: { last: null, count: 0 },
           last: null, cando: {}, drafts: {}, games: {}, classMode: false, slides: {}, wordsView: 'cards' };
}
function loadState() {
  var s = null;
  try { var raw = window.localStorage.getItem(DATA.storageKey); if (raw) s = JSON.parse(raw); } catch (e) { STORE_OK = false; s = null; }
  var d = defaultState();
  if (s && typeof s === 'object') for (var k in d) if (s[k] !== undefined) d[k] = s[k];
  return d;
}
var S = loadState();
var saveTimer = null;
function save(now) {
  if (saveTimer) { clearTimeout(saveTimer); saveTimer = null; }
  var doit = function () {
    try { window.localStorage.setItem(DATA.storageKey, JSON.stringify(S)); } catch (e) { STORE_OK = false; }
  };
  if (now) doit(); else saveTimer = setTimeout(doit, 150);
}
window.addEventListener('pagehide', function () { save(true); });

function today() { var d = new Date(); return d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate(); }
function touchStreak() {
  var t = today();
  if (S.streak.last === t) return;
  var y = new Date(); y.setDate(y.getDate() - 1);
  var ys = y.getFullYear() + '-' + (y.getMonth() + 1) + '-' + y.getDate();
  S.streak.count = (S.streak.last === ys) ? S.streak.count + 1 : 1;
  S.streak.last = t;
  save();
}
function streakNow() {
  var t = today();
  var y = new Date(); y.setDate(y.getDate() - 1);
  var ys = y.getFullYear() + '-' + (y.getMonth() + 1) + '-' + y.getDate();
  return (S.streak.last === t || S.streak.last === ys) ? S.streak.count : 0;
}

var toastTimer = null;
function toast(msg) {
  var t = document.getElementById('toast');
  t.textContent = msg; t.classList.add('on');
  clearTimeout(toastTimer); toastTimer = setTimeout(function () { t.classList.remove('on'); }, 1800);
}
function anim(node, cls) { node.classList.remove(cls); void node.offsetWidth; node.classList.add(cls); }

function rnd(n) { return Math.floor(Math.random() * n); }
function shuffled(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = rnd(i + 1); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }

/* ---------- icons (inline SVG, one per exercise type / section) ---------- */
var ICON_PATHS = {
  choose: '<circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="2.4"/><circle cx="12" cy="12" r="3.5" fill="currentColor"/>',
  tf: '<path d="M4 12l4 4 7-8" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M15 15l5 5M20 15l-5 5" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>',
  gap: '<path d="M4 18h16" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/><path d="M14 4l4 4-8 8H6v-4z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/>',
  bank: '<rect x="3" y="4" width="8" height="7" rx="2" fill="currentColor"/><rect x="13" y="4" width="8" height="7" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M4 18h16" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/>',
  order: '<rect x="3" y="5" width="6" height="5" rx="1.5" fill="currentColor"/><rect x="11" y="5" width="10" height="5" rx="1.5" fill="none" stroke="currentColor" stroke-width="2"/><rect x="3" y="14" width="10" height="5" rx="1.5" fill="none" stroke="currentColor" stroke-width="2"/><rect x="15" y="14" width="6" height="5" rx="1.5" fill="currentColor"/>',
  fix: '<path d="M14.5 4a4.5 4.5 0 0 0-4.3 5.8L4 16v4h4l6.2-6.2A4.5 4.5 0 1 0 14.5 4z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/>',
  match: '<circle cx="5" cy="7" r="2.5" fill="currentColor"/><circle cx="5" cy="17" r="2.5" fill="currentColor"/><circle cx="19" cy="7" r="2.5" fill="currentColor"/><circle cx="19" cy="17" r="2.5" fill="currentColor"/><path d="M7.5 7l9 10M7.5 17l9-10" stroke="currentColor" stroke-width="2"/>',
  sort: '<path d="M3 6h7l2 2h9v11H3z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/><path d="M8 13h8" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>',
  transform: '<path d="M5 9a7 7 0 0 1 12-3l2 2M19 15a7 7 0 0 1-12 3l-2-2" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/><path d="M19 4v4h-4M5 20v-4h4" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>',
  short: '<path d="M4 5h16v10H9l-5 4z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/><path d="M8 10l2 2 4-4" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>',
  wq: '<path d="M9 9a3 3 0 1 1 4.5 2.6c-1 .6-1.5 1.3-1.5 2.4" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/><circle cx="12" cy="18" r="1.5" fill="currentColor"/>',
  numbers: '<path d="M7 5v14M4 8l3-3M12 8a3 3 0 1 1 5 2l-5 6h6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>',
  spell: '<path d="M4 18l4-12 4 12M5.5 14h5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/><path d="M15 18v-8h3a2 2 0 0 1 0 4h-3h3.5a2 2 0 0 1 0 4z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
  odd: '<circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="2.2"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="2.2"/><circle cx="12" cy="12" r="1.2" fill="currentColor"/>',
  dorder: '<path d="M6 5h12M6 12h12M6 19h12" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/><circle cx="3" cy="5" r="1.4" fill="currentColor"/><circle cx="3" cy="12" r="1.4" fill="currentColor"/><circle cx="3" cy="19" r="1.4" fill="currentColor"/>',
  words: '<rect x="4" y="5" width="13" height="15" rx="2" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M8 3h12v15" fill="none" stroke="currentColor" stroke-width="2.2"/>',
  grammar: '<rect x="3" y="7" width="5" height="10" rx="1.5" fill="currentColor"/><rect x="10" y="7" width="5" height="10" rx="1.5" fill="none" stroke="currentColor" stroke-width="2"/><rect x="17" y="7" width="4" height="10" rx="1.5" fill="currentColor" opacity=".5"/>',
  classroom: '<rect x="3" y="4" width="18" height="12" rx="2" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M7 20l3-4M17 20l-3-4M7 9h6" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>',
  reading: '<path d="M3 5c3-1 6-1 9 1 3-2 6-2 9-1v14c-3-1-6-1-9 1-3-2-6-2-9-1z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/><path d="M12 6v14" stroke="currentColor" stroke-width="2"/>',
  dialogue: '<path d="M3 4h12v8H7l-4 3z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/><path d="M9 15h7l4 3v-11h-3" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/>',
  writing: '<path d="M4 20h16M15 4l4 4-9 9H6v-4z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/>',
  games: '<rect x="2.5" y="7" width="19" height="11" rx="5" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M7 10.5v4M5 12.5h4" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/><circle cx="16" cy="11" r="1.4" fill="currentColor"/><circle cx="18" cy="14" r="1.4" fill="currentColor"/>',
  test: '<rect x="5" y="3" width="14" height="18" rx="2" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M8 9l2 2 4-4M8 16h8" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" fill="none"/>',
  cando: '<path d="M12 3l2.6 5.6 6 .7-4.5 4.1 1.2 6-5.3-3-5.3 3 1.2-6L3.4 9.3l6-.7z" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linejoin="round"/>',
  star: '<path d="M12 3l2.6 5.6 6 .7-4.5 4.1 1.2 6-5.3-3-5.3 3 1.2-6L3.4 9.3l6-.7z" fill="currentColor"/>',
  flame: '<path d="M12 21c-4 0-7-3-7-7 0-4 4-6 4-11 3 2 5 5 5 8 1-1 2-2 2-4 2 2 3 4 3 7 0 4-3 7-7 7z" fill="currentColor"/>',
  pile: '<rect x="4" y="13" width="16" height="6" rx="2" fill="currentColor" opacity=".45"/><rect x="5" y="8" width="14" height="6" rx="2" fill="currentColor" opacity=".7"/><rect x="6" y="3" width="12" height="6" rx="2" fill="currentColor"/>',
  notebook: '<rect x="5" y="3" width="14" height="18" rx="2" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M9 3v18M12 8h4M12 12h4" stroke="currentColor" stroke-width="2"/>',
  review: '<path d="M12 3l8 4v6c0 4-3.5 7-8 8-4.5-1-8-4-8-8V7z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/>',
  progress: '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>',
  verbs: '<path d="M4 6h10M4 12h16M4 18h8" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/><path d="M17 4l3 2-3 2" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>',
  smarter: '<path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-4 10.5c.8.8 1 1.5 1 2.5h6c0-1 .2-1.7 1-2.5A6 6 0 0 0 12 3z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/>',
  resources: '<circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18" fill="none" stroke="currentColor" stroke-width="1.8"/>',
  home: '<path d="M3 11l9-7 9 7v9h-6v-6H9v6H3z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/>',
  back: '<path d="M15 5l-7 7 7 7" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>',
  next: '<path d="M9 5l7 7-7 7" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>'
};
function icon(name, size, color) {
  var span = document.createElement('span');
  span.setAttribute('aria-hidden', 'true');
  span.style.display = 'inline-flex';
  span.style.color = color || 'currentColor';
  var s = size || 22;
  var p = ICON_PATHS[name] || ICON_PATHS.choose;
  // ICON_PATHS are constant strings from this file, never data
  span.innerHTML = '<svg width="' + s + '" height="' + s + '" viewBox="0 0 24 24">' + p + '</svg>';
  return span;
}
var TYPE_ICON = { choose: 'choose', tf: 'tf', odd: 'odd', gap: 'gap', transform: 'transform', short: 'short', wq: 'wq',
  numbers: 'numbers', spell: 'spell', bank: 'bank', order: 'order', fix: 'fix', match: 'match', sort: 'sort', dorder: 'dorder' };
var INK = { teal: '#166F68', coral: '#C23B3B', amber: '#8A5300', purple: '#6D4FD1' };

function escXml(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }
function svgNode(markup) {
  // markup is built by visuals.js, with every data string passed through escXml
  var d = document.createElement('div');
  d.innerHTML = markup;
  return d.firstChild;
}
