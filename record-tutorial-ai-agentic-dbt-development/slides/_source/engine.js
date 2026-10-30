(function () {
  'use strict';
  var DECK = JSON.parse(document.getElementById('deck-data').textContent);
  var SLIDES = DECK.slides;
  var N = SLIDES.length;
  var qs = new URLSearchParams(location.search);
  var MODE = qs.has('presenter') ? 'presenter' : (qs.has('script') ? 'script' : 'main');
  var app = document.getElementById('app');
  var cur = 0;
  var peer = null;

  /* ---------- storage (best effort) ---------- */
  function sget(k) { try { return localStorage.getItem('aidbt:' + k); } catch (e) { return null; } }
  function sset(k, v) { try { localStorage.setItem('aidbt:' + k, v); } catch (e) { /* ignore */ } }
  function applyTheme(t) { document.documentElement.setAttribute('data-theme', t); }
  applyTheme(sget('theme') || 'dark');

  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

  var HABITS = [
    ['Context over memory', 'Give the agent files: the data dictionary, the skill, the docs.'],
    ['Plan before act', 'For multi-file work, ask for the plan first and approve it.'],
    ['One task per chat', 'Start a new chat each section. Watch the context ring.'],
    ['Read every diff', 'Before you click Keep. The review is the lesson.'],
    ['dbt is the judge', 'Run, test, look at rows. "Done" is a claim, not proof.'],
    ['Correct twice → skill', 'If you fix the same thing twice, write it into the skill.']
  ];

  /* ---------- DAG ---------- */
  var NW = 300, NH = 58, COLX = [10, 360, 710, 1060, 1410];
  function nd(label, type, c, y) { return { label: label, type: type, x: COLX[c], y: y }; }
  var NODES = {
    src_trips: nd('tlc.yellow_trips', 'source', 0, 10),
    seed_pay: nd('payment_types', 'seed', 0, 120),
    seed_rate: nd('rate_codes', 'seed', 0, 230),
    seed_zones: nd('taxi_zone_lookup', 'seed', 0, 340),
    src_vendors: nd('tlc.vendor_registry', 'source', 0, 450),
    stg_trips: nd('stg_tlc__yellow_trips', 'model', 1, 10),
    stg_zones: nd('stg_tlc__taxi_zones', 'model', 1, 340),
    snap: nd('snap_tlc__vendors', 'snapshot', 1, 450),
    int: nd('int_trips__enriched', 'model', 2, 65),
    fct: nd('fct_trips', 'model', 3, 10),
    dim_zones: nd('dim_zones', 'model', 3, 340),
    dim_vendors: nd('dim_vendors', 'model', 3, 450),
    agg: nd('agg_zone_daily', 'model', 4, 120),
    exp: nd('CBD fee analysis', 'exposure', 4, 285)
  };
  var EDGES = [['src_trips', 'stg_trips'], ['seed_zones', 'stg_zones'], ['src_vendors', 'snap'], ['stg_trips', 'int'],
    ['seed_pay', 'int'], ['seed_rate', 'int'], ['int', 'fct'], ['stg_zones', 'dim_zones'], ['snap', 'dim_vendors'],
    ['fct', 'agg'], ['dim_zones', 'agg'], ['fct', 'exp'], ['dim_zones', 'exp']];
  var TCOL = { source: 'var(--good)', seed: 'var(--teal)', model: 'var(--blue)', snapshot: 'var(--violet)', exposure: 'var(--orange)' };

  function dagSVG(newIds, builtIds) {
    var state = function (id) { return newIds.indexOf(id) >= 0 ? 'new' : (builtIds.indexOf(id) >= 0 ? 'built' : 'future'); };
    var out = '<svg viewBox="0 0 1720 520" xmlns="http://www.w3.org/2000/svg">';
    out += '<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" style="fill:var(--dim)"/></marker>' +
      '<marker id="ahn" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" style="fill:var(--accent)"/></marker></defs>';
    EDGES.forEach(function (e) {
      var a = NODES[e[0]], b = NODES[e[1]];
      var sa = state(e[0]), sb = state(e[1]);
      var cls = (sb === 'new') ? 'new' : ((sa === 'future' || sb === 'future') ? 'future' : '');
      var x1 = a.x + NW, y1 = a.y + NH / 2, x2 = b.x - 6, y2 = b.y + NH / 2, mx = (x1 + x2) / 2;
      out += '<path class="edge ' + cls + '" marker-end="url(#' + (cls === 'new' ? 'ahn' : 'ah') + ')" d="M' + x1 + ',' + y1 + ' C' + mx + ',' + y1 + ' ' + mx + ',' + y2 + ' ' + x2 + ',' + y2 + '"/>';
    });
    Object.keys(NODES).forEach(function (id) {
      var n = NODES[id], st = state(id), c = TCOL[n.type];
      out += '<g class="node ' + st + '"><rect x="' + n.x + '" y="' + n.y + '" width="' + NW + '" height="' + NH + '" rx="14" style="fill:color-mix(in srgb,' + c + ' 16%, transparent);stroke:' + c + '"/>' +
        '<text x="' + (n.x + NW / 2) + '" y="' + (n.y + NH / 2 + 7) + '" text-anchor="middle">' + esc(n.label) + '</text></g>';
    });
    return out + '</svg>';
  }
  function dagLegend() {
    var t = [['source', 'Source'], ['seed', 'Seed'], ['model', 'Model'], ['snapshot', 'Snapshot'], ['exposure', 'Exposure']];
    return '<div class="dag-legend">' + t.map(function (x) { return '<span style="color:' + TCOL[x[0]] + '"><i></i><b style="color:var(--muted);font-weight:500">' + x[1] + '</b></span>'; }).join('') +
      '<span style="color:var(--accent)"><i style="box-shadow:0 0 10px var(--glow);border-width:3px"></i><b style="color:var(--muted);font-weight:500">New in this section</b></span>' +
      '<span style="color:var(--dim)"><i style="border-style:dashed;opacity:.5"></i><b style="color:var(--muted);font-weight:500">Comes later</b></span></div>';
  }

  /* ---------- renderers ---------- */
  function kick(s, cls) { return s.kicker ? '<div class="kicker ' + (cls || '') + '">' + s.kicker + '</div>' : ''; }
  function h2(s) { return s.title ? '<h2>' + s.title + '</h2>' : ''; }
  function head(s, cls) { return kick(s, cls) + h2(s); }
  function foot(s) { return s.foot ? '<div class="foot">' + s.foot + '</div>' : ''; }
  function list(items) { return items.map(function (x) { return '<li>' + x + '</li>'; }).join(''); }
  function editable(k, def) {
    var v = sget(DECK.id + ':' + k);
    var shown = (v !== null && v !== '') ? esc(v) : def;
    return '<span class="editable" data-k="' + esc(k) + '"' + (MODE === 'main' ? ' contenteditable="true" spellcheck="false"' : '') + '>' + shown + '</span>';
  }
  function habitStrip(on) {
    on = on || [];
    return '<div class="habit-strip">' + HABITS.map(function (h, i) { return '<span class="' + (on.indexOf(i + 1) >= 0 ? 'on' : '') + '">' + (i + 1) + ' · ' + h[0] + '</span>'; }).join('') + '</div>';
  }

  var R = {
    title: function (s) {
      return '<img class="logo" src="logo_hero.svg" alt="" onerror="this.remove()">' +
        '<div class="title-num">' + DECK.num + '</div>' +
        '<div class="kicker">' + (s.kicker || DECK.part) + '</div><h1>' + s.title + '</h1>' +
        (s.subtitle ? '<p class="subtitle">' + s.subtitle + '</p>' : '') +
        (s.chips ? '<div class="chips">' + s.chips.map(function (c) { return '<span class="chip">' + c + '</span>'; }).join('') + '</div>' : '');
    },
    statement: function (s) {
      return kick(s, s.kclass) + '<div class="statement"><div class="big">' + s.text + '</div>' + (s.sub ? '<div class="sub">' + s.sub + '</div>' : '') + '</div>';
    },
    bullets: function (s) {
      return head(s) + '<ul class="bl ' + (s.cols === 2 ? 'two ' : '') + (s.numbered ? 'num' : '') + '">' + s.items.map(function (it, i) {
        var body = (typeof it === 'string') ? it : ('<strong>' + it.t + '</strong>' + (it.d ? '<span class="d">' + it.d + '</span>' : ''));
        return '<li>' + (s.numbered ? '<span class="n">' + (i + 1) + '</span>' : '') + '<div>' + body + '</div></li>';
      }).join('') + '</ul>' + foot(s);
    },
    flow: function (s) {
      return head(s) + '<div class="flow n' + s.steps.length + '">' + s.steps.map(function (st, i) {
        return (i ? '<div class="arrow">→</div>' : '') + '<div class="step ' + (st.hl ? 'hl ' : '') + (st.dim ? 'dim' : '') + '"' + (st.color ? ' style="--c:var(--' + st.color + ')"' : '') + '>' +
          (st.tag ? '<div class="tag">' + st.tag + '</div>' : '') + '<div class="lbl">' + st.label + '</div>' + (st.sub ? '<div class="sub">' + st.sub + '</div>' : '') + '</div>';
      }).join('') + '</div>' + (s.caption ? '<div class="caption">' + s.caption + '</div>' : '') + foot(s);
    },
    columns: function (s) {
      return head(s) + '<div class="cols c' + s.cols.length + '">' + s.cols.map(function (c) {
        return '<div class="card col ' + (c.mark || '') + '" style="--c:var(--' + (c.color || 'accent') + ')"><div class="col-t">' + c.title + '</div>' +
          (c.sub ? '<div class="col-s">' + c.sub + '</div>' : '') +
          (c.items ? '<ul>' + list(c.items) + '</ul>' : '') +
          (c.codeHtml ? '<pre style="font-size:' + (c.size || 24) + 'px">' + c.codeHtml + '</pre>' : '') +
          (c.foot ? '<div class="col-f">' + c.foot + '</div>' : '') + '</div>';
      }).join('') + '</div>' + (s.verdict ? '<div class="verdict">' + s.verdict + '</div>' : '') + foot(s);
    },
    code: function (s) {
      return head(s) + '<div class="code-row"><div class="codebox"><div class="code-h"><span class="dots"><i></i><i></i><i></i></span><span class="fname">' + (s.file || '') + '</span><span class="lang">' + (s.lang || '') + '</span></div>' +
        '<pre style="font-size:' + s.size + 'px">' + s.codeHtml + '</pre></div>' +
        (s.aside ? '<div class="aside">' + (s.asideTitle ? '<div class="aside-t">' + s.asideTitle + '</div>' : '') + '<ul>' + list(s.aside) + '</ul></div>' : '') + '</div>' + foot(s);
    },
    docs: function (s) {
      return '<div class="kicker">' + (s.kicker || 'The docs say') + '</div><div class="browser"><div class="bar"><span class="dots"><i></i><i></i><i></i></span><span class="url">' + s.urlShow + '</span><span class="v1">v1</span></div>' +
        '<div class="page"><div class="page-t">' + s.page + '</div><ol class="pts">' + s.points.map(function (p) { return '<li><span>' + p + '</span></li>'; }).join('') + '</ol>' + (s.quote ? '<blockquote>' + s.quote + '</blockquote>' : '') + '</div></div>' + foot(s);
    },
    prompt: function (s) {
      return kick(s, 'k-ai') + '<div class="prompt-head"><span class="where">' + s.where + '</span><span class="mode m-' + s.modeKey + '">' + s.mode + '</span></div>' +
        '<div class="prompt-row"><div class="bubble" style="font-size:' + s.size + 'px">' + s.text + '</div>' +
        (s.watch ? '<div class="watch"><div class="aside-t">Watch for</div><ul>' + list(s.watch) + '</ul></div>' : '') + '</div>' + habitStrip(s.habits);
    },
    table: function (s) {
      return head(s) + '<table class="tbl" style="font-size:' + (s.size || 28) + 'px"><thead><tr>' + s.headers.map(function (h) { return '<th>' + h + '</th>'; }).join('') + '</tr></thead><tbody>' +
        s.rows.map(function (r) { var cells = r.cells || r; return '<tr class="' + (r.hl ? 'hl' : '') + '">' + cells.map(function (c) { return '<td>' + c + '</td>'; }).join('') + '</tr>'; }).join('') +
        '</tbody></table>' + foot(s);
    },
    realdata: function (s) {
      return '<div class="kicker k-real">' + (s.kicker || 'Real-data moment') + '</div>' + h2(s) + '<div class="stats c' + s.stats.length + '">' + s.stats.map(function (st) {
        return '<div class="stat"><div class="val">' + (st.edit ? editable(st.edit, st.v) : st.v) + '</div><div class="lab">' + st.label + '</div></div>';
      }).join('') + '</div>' + foot(s);
    },
    dag: function (s) {
      return head(s) + '<div class="dag">' + dagSVG(s.new || [], s.built || []) + '</div>' + dagLegend() +
        (s.files ? '<div class="files">' + s.files.map(function (f) { return '<span class="file">' + f + '</span>'; }).join('') + '</div>' : '') + foot(s);
    },
    blocks: function (s) {
      var curB = s.current || [], upto = (s.upto == null ? -1 : s.upto);
      return head(s) + '<div class="blocks">' + DECK.blocks.map(function (b) {
        var cls = 'blk';
        if (!b.sections) cls += ' out';
        else if (curB.indexOf(b.name) >= 0) cls += ' cur';
        else if (Math.min.apply(null, b.sections) <= upto) cls += ' done';
        var secs = b.sections ? b.sections.map(function (n) { return '<span>S' + (n < 10 ? '0' : '') + n + '</span>'; }).join('') : '<span>Part 3?</span>';
        return '<div class="' + cls + '"><div class="bn">' + b.name + '</div><div class="bs">' + secs + '</div></div>';
      }).join('') + '</div>' + foot(s);
    },
    recap: function (s) {
      return '<div class="kicker">Recap</div>' + h2(s) + '<div class="recap"><ul class="checks">' + list(s.items) + '</ul><div class="recap-side">' +
        '<div class="card"><div class="cp-t">Checkpoint</div><code class="cp-c">git tag ' + s.tag + '</code></div>' +
        (s.blocks && s.blocks.length ? '<div class="card"><div class="cp-t">Blocks covered</div><div class="chips">' + s.blocks.map(function (b) { return '<span class="chip ok">✓ ' + b + '</span>'; }).join('') + '</div></div>' : '') +
        (s.next ? '<div class="card"><div class="cp-t">Next</div><div class="next-t">' + s.next + '</div></div>' : '') + '</div></div>';
    },
    habits: function (s) {
      return head(s) + '<div class="habits">' + HABITS.map(function (h, i) {
        return '<div class="habit ' + (s.hl && s.hl.indexOf(i + 1) >= 0 ? 'hl' : '') + '"><div class="hn">' + (i + 1) + '</div><div><div class="ht">' + h[0] + '</div><div class="hd">' + h[1] + '</div></div></div>';
      }).join('') + '</div>' + foot(s);
    },
    steps: function (s) {
      return head(s) + '<ol class="steps">' + s.items.map(function (it) {
        return '<li><div><div class="st">' + it.t + '</div>' + (it.cmd ? '<span class="cmd">' + it.cmd + '</span>' : '') + '</div></li>';
      }).join('') + '</ol>' + foot(s);
    }
  };

  function footerHTML(i) {
    return '<div class="footer"><span>' + DECK.code + ' · ' + DECK.short + '</span><span class="brand">Agentic dbt Development · Rosetta dbt Studio</span><span><span class="v1b">dbt v1</span>' + (i + 1) + ' / ' + N + '</span></div>';
  }
  function slideHTML(s, i, active) {
    var body = R[s.type] ? R[s.type](s) : '<h2>Unknown slide type ' + esc(s.type) + '</h2>';
    return '<section class="slide t-' + s.type + (active ? ' active' : '') + '" data-i="' + i + '"><div class="content"><div class="inner">' + body + '</div></div>' + footerHTML(i) + '</section>';
  }
  function notesHTML(s) {
    var n = s.notes || { say: [], do: [] };
    var h = '';
    if (n.say && n.say.length) h += '<div class="nt-h">Say</div><div class="nt-say">' + n.say.map(function (p) { return '<p>' + p + '</p>'; }).join('') + '</div>';
    if (n.do && n.do.length) h += '<div class="nt-h">On screen</div><div class="nt-do"><ul>' + list(n.do) + '</ul></div>';
    return h || '<div class="nt-say"><p>No notes.</p></div>';
  }

  /* ---------- fit content into the slide ---------- */
  function fit(slide) {
    var c = slide.querySelector('.content'), inner = c && c.firstElementChild;
    if (!inner) return;
    inner.style.transform = ''; inner.style.width = '';
    var k = 1;
    for (var t = 0; t < 6; t++) {
      var h = inner.scrollHeight, H = c.clientHeight;
      if (h <= H + 1) break;
      k = Math.max(0.55, k * (H / h) * 0.995);
      inner.style.width = (100 / k) + '%';
      inner.style.transform = 'scale(' + k + ')';
    }
    slide.setAttribute('data-fit', k.toFixed(3));
  }

  /* ---------- thumbnails ---------- */
  function thumb(el, i) {
    if (i >= N) { el.innerHTML = '<div class="end">End of section</div>'; el.style.height = (el.clientWidth * 1080 / 1920) + 'px'; return; }
    el.innerHTML = '<div class="thumb-inner">' + slideHTML(SLIDES[i], i, true) + '</div>';
    var w = el.clientWidth;
    el.style.height = (w * 1080 / 1920) + 'px';
    el.firstElementChild.style.transform = 'scale(' + (w / 1920) + ')';
    fit(el.querySelector('.slide'));
  }

  /* ---------- sync between main and presenter ---------- */
  function send(i) { try { if (peer && !peer.closed) peer.postMessage({ aidbt: DECK.id, i: i }, '*'); } catch (e) { /* ignore */ } }
  window.addEventListener('message', function (e) {
    var d = e.data;
    if (d && d.aidbt === DECK.id && typeof d.i === 'number' && d.i !== cur) go(d.i, true);
  });

  var go = function () {};

  /* ---------- MAIN ---------- */
  function mountMain() {
    document.title = DECK.code + ' · ' + DECK.title;
    app.innerHTML = '<div id="stage"><div id="canvas">' + SLIDES.map(function (s, i) { return slideHTML(s, i, false); }).join('') + '</div></div>' +
      '<div id="progress"><i></i></div><div id="notes" class="hidden"></div>' +
      '<div id="help" class="hidden"><div class="box"><h3>Keyboard</h3><table>' +
      '<tr><td><kbd>→</kbd> <kbd>Space</kbd></td><td>Next slide</td></tr><tr><td><kbd>←</kbd></td><td>Previous slide</td></tr>' +
      '<tr><td><kbd>Home</kbd> <kbd>End</kbd></td><td>First / last</td></tr><tr><td><kbd>P</kbd></td><td>Presenter window (notes, next slide, timer)</td></tr>' +
      '<tr><td><kbd>N</kbd></td><td>Notes drawer in this window</td></tr><tr><td><kbd>S</kbd></td><td>Script: all slides + notes (printable)</td></tr>' +
      '<tr><td><kbd>T</kbd></td><td>Light / dark theme</td></tr><tr><td><kbd>F</kbd></td><td>Fullscreen</td></tr>' +
      '<tr><td><kbd>?</kbd></td><td>This help</td></tr></table><p style="color:#94A3B8;margin:14px 0 0">Amber numbers on real-data slides are editable: click, type, press Esc.</p></div></div>';
    var canvas = document.getElementById('canvas');
    var slides = Array.prototype.slice.call(canvas.querySelectorAll('.slide'));
    function scale() { var s = Math.min(innerWidth / 1920, innerHeight / 1080); canvas.style.transform = 'translate(-50%,-50%) scale(' + s + ')'; }
    scale(); window.addEventListener('resize', scale);
    function fitAll() { slides.forEach(fit); }
    fitAll();
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(fitAll);
    window.addEventListener('load', fitAll);

    canvas.addEventListener('input', function (e) {
      var t = e.target;
      if (t.classList && t.classList.contains('editable')) sset(DECK.id + ':' + t.getAttribute('data-k'), t.textContent.trim());
    });

    var notes = document.getElementById('notes');
    go = function (i, fromPeer) {
      i = Math.max(0, Math.min(N - 1, i));
      slides[cur].classList.remove('active');
      cur = i;
      slides[cur].classList.add('active');
      document.querySelector('#progress i').style.width = ((cur + 1) / N * 100) + '%';
      notes.innerHTML = '<div class="nt-h">Slide ' + (cur + 1) + ' / ' + N + '</div>' + notesHTML(SLIDES[cur]);
      try { history.replaceState(null, '', '#' + (cur + 1)); } catch (e) { /* ignore */ }
      if (!fromPeer) send(cur);
    };
    var start = parseInt((location.hash || '').slice(1), 10);
    slides[0].classList.add('active');
    go(isNaN(start) ? 0 : start - 1, true);

    document.addEventListener('keydown', function (e) {
      var t = e.target;
      if (t && t.isContentEditable) { if (e.key === 'Escape' || e.key === 'Enter') { e.preventDefault(); t.blur(); } return; }
      if (e.metaKey || e.ctrlKey || e.altKey) return;
      var k = e.key;
      if (k === 'ArrowRight' || k === 'PageDown' || k === ' ' || k === 'ArrowDown') { e.preventDefault(); go(cur + 1); }
      else if (k === 'ArrowLeft' || k === 'PageUp' || k === 'ArrowUp' || k === 'Backspace') { e.preventDefault(); go(cur - 1); }
      else if (k === 'Home') go(0);
      else if (k === 'End') go(N - 1);
      else if (k === 'n' || k === 'N') notes.classList.toggle('hidden');
      else if (k === 'p' || k === 'P') {
        peer = window.open(location.pathname + '?presenter#' + (cur + 1), 'aidbt-presenter-' + DECK.id, 'width=1280,height=860');
        setTimeout(function () { send(cur); }, 600);
      }
      else if (k === 's' || k === 'S') window.open(location.pathname + '?script', '_blank');
      else if (k === 't' || k === 'T') { var nt = document.documentElement.getAttribute('data-theme') === 'light' ? 'dark' : 'light'; applyTheme(nt); sset('theme', nt); fitAll(); }
      else if (k === 'f' || k === 'F') { if (!document.fullscreenElement) { document.documentElement.requestFullscreen && document.documentElement.requestFullscreen(); } else { document.exitFullscreen && document.exitFullscreen(); } }
      else if (k === '?' || k === 'h' || k === 'H') document.getElementById('help').classList.toggle('hidden');
      else if (k === 'Escape') { document.getElementById('help').classList.add('hidden'); }
    });
    document.getElementById('help').addEventListener('click', function () { this.classList.add('hidden'); });
  }

  /* ---------- PRESENTER ---------- */
  function mountPresenter() {
    document.body.classList.add('presenter');
    document.title = 'Presenter · ' + DECK.code + ' · ' + DECK.short;
    peer = window.opener || null;
    app.innerHTML = '<div class="pv"><header><div class="pv-title">' + DECK.code + ' · ' + DECK.title + '</div><span class="pv-count"></span>' +
      '<button id="pv-timer" title="Click to reset">00:00</button><button data-a="prev">◀ Prev</button><button data-a="next">Next ▶</button></header>' +
      '<div class="pv-main"><div class="pv-left"><div><div class="pv-lab">Now</div><div class="pv-cur thumb"></div></div>' +
      '<div class="pv-next-wrap"><div class="pv-lab">Next</div><div class="pv-next thumb"></div></div></div><div class="pv-notes"></div></div></div>';
    var t0 = Date.now(), timer = document.getElementById('pv-timer');
    setInterval(function () { var s = Math.floor((Date.now() - t0) / 1000); timer.textContent = String(Math.floor(s / 60)).padStart(2, '0') + ':' + String(s % 60).padStart(2, '0'); }, 500);
    timer.addEventListener('click', function () { t0 = Date.now(); });
    var curEl = app.querySelector('.pv-cur'), nextEl = app.querySelector('.pv-next'), notesEl = app.querySelector('.pv-notes'), countEl = app.querySelector('.pv-count');
    go = function (i, fromPeer) {
      cur = Math.max(0, Math.min(N - 1, i));
      thumb(curEl, cur); thumb(nextEl, cur + 1);
      notesEl.innerHTML = notesHTML(SLIDES[cur]); notesEl.scrollTop = 0;
      countEl.textContent = (cur + 1) + ' / ' + N;
      if (!fromPeer) send(cur);
    };
    app.querySelector('[data-a=prev]').addEventListener('click', function () { go(cur - 1); });
    app.querySelector('[data-a=next]').addEventListener('click', function () { go(cur + 1); });
    document.addEventListener('keydown', function (e) {
      var k = e.key;
      if (k === 'ArrowRight' || k === 'PageDown' || k === ' ') { e.preventDefault(); go(cur + 1); }
      else if (k === 'ArrowLeft' || k === 'PageUp' || k === 'Backspace') { e.preventDefault(); go(cur - 1); }
    });
    var start = parseInt((location.hash || '').slice(1), 10);
    go(isNaN(start) ? 0 : start - 1, true);
    window.addEventListener('resize', function () { go(cur, true); });
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { go(cur, true); });
  }

  /* ---------- SCRIPT ---------- */
  function mountScript() {
    document.body.classList.add('script');
    document.title = 'Script · ' + DECK.code + ' · ' + DECK.short;
    app.innerHTML = '<header class="sc-h"><h1>' + DECK.code + ' · ' + DECK.title + '</h1><p>' + N + ' slides · talk track (Say) and actions (On screen) · print with Ctrl/Cmd + P</p></header>' +
      SLIDES.map(function (s, i) { return '<div class="sc-row"><div class="sc-thumb thumb" data-i="' + i + '"></div><div class="sc-notes"><div class="sc-n">Slide ' + (i + 1) + '</div>' + notesHTML(s) + '</div></div>'; }).join('');
    function all() { Array.prototype.forEach.call(app.querySelectorAll('.sc-thumb'), function (el) { thumb(el, +el.getAttribute('data-i')); }); }
    all();
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(all);
    window.addEventListener('beforeprint', all);
    window.addEventListener('afterprint', all);
  }

  if (MODE === 'presenter') mountPresenter();
  else if (MODE === 'script') mountScript();
  else mountMain();
})();
