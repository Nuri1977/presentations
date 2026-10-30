import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from lib import BLOCKS, md  # noqa: E402
import content_a  # noqa: E402
import content_b  # noqa: E402
import content_c  # noqa: E402

HERE = os.path.dirname(__file__)
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, '..', 'out', 'ai-agentic-dbt-slides')
os.makedirs(OUT, exist_ok=True)

CSS = open(os.path.join(HERE, 'engine.css')).read()
JS = open(os.path.join(HERE, 'engine.js')).read()

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
__CSS__
</style>
</head>
<body>
<div id="app"></div>
<script type="application/json" id="deck-data">__DATA__</script>
<script>
__JS__
</script>
</body>
</html>
"""

DECKS = content_a.DECKS + content_b.DECKS + content_c.DECKS
total = 0
index_rows = []
for d in DECKS:
    num = d['num']
    code = 'S%02d' % num
    data = {
        'id': 's%02d' % num, 'num': '%02d' % num, 'code': code, 'title': md(d['title']), 'short': md(d.get('short', d['title'])),
        'part': md(d['part']), 'minutes': d['minutes'], 'blocks': BLOCKS, 'slides': d['slides'],
    }
    js = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
    page = TEMPLATE.replace('__TITLE__', code + ' · ' + d['title']).replace('__CSS__', CSS).replace('__DATA__', js).replace('__JS__', JS)
    fn = d['file'] + '.html'
    with open(os.path.join(OUT, fn), 'w', encoding='utf-8') as f:
        f.write(page)
    total += len(d['slides'])
    index_rows.append((code, d['title'], d['part'], d['minutes'], len(d['slides']), fn, d.get('blurb', '')))

# ---------------------------------------------------------------- index
cards = []
last_part = None
for code, t, part, mins, n, fn, blurb in index_rows:
    if part != last_part:
        cards.append('<h2>%s</h2>' % part)
        last_part = part
    cards.append(
        '<div class="row"><a class="main" href="%s"><span class="code">%s</span><span class="t">%s</span><span class="b">%s</span></a>'
        '<span class="meta">%d min · %d slides</span><a class="btn" href="%s?script">Script</a><a class="btn pri" href="%s">Present</a></div>'
        % (fn, code, md(t), md(blurb), mins, n, fn, fn))

INDEX = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Agentic dbt Development · Slides</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>
:root{--bg:#0A1020;--panel:rgba(255,255,255,.05);--line:rgba(255,255,255,.11);--text:#E8EEF8;--muted:#9AA8BF;--accent:#38BDF8;--amber:#FBBF24}
@media (prefers-color-scheme: light){:root:not([data-theme="dark"]){--bg:#F6F8FC;--panel:#fff;--line:rgba(15,23,42,.13);--text:#0D1526;--muted:#4A5872;--accent:#0278B8;--amber:#B45309}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font-family:Inter,system-ui,-apple-system,Segoe UI,Roboto,sans-serif}
.wrap{max-width:1040px;margin:0 auto;padding:48px 16px 80px}
.k{font-size:13px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent);font-weight:700}
h1{font-size:40px;line-height:1.1;margin:10px 0 12px;letter-spacing:-.02em}
p.lead{color:var(--muted);font-size:17px;line-height:1.55;margin:0 0 26px}
h2{font-size:14px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin:34px 0 12px}
.row{display:flex;align-items:center;gap:12px;background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:12px 14px;margin:10px 0}
.row a.main{flex:1;min-width:0;display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 12px;color:inherit;text-decoration:none}
.code{font-family:"JetBrains Mono",monospace;color:var(--accent);font-weight:500}
.t{font-weight:700;font-size:17px}.b{flex-basis:100%;color:var(--muted);font-size:14px}
.meta{color:var(--muted);font-size:13px;white-space:nowrap}
.btn{font-size:13px;font-weight:700;text-decoration:none;color:var(--text);border:1px solid var(--line);border-radius:999px;padding:6px 12px;white-space:nowrap}
.btn.pri{background:var(--accent);color:#06101F;border-color:transparent}
.keys{display:grid;grid-template-columns:auto 1fr;gap:6px 16px;font-size:15px;color:var(--muted);background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:16px 18px}
kbd{font-family:"JetBrains Mono",monospace;font-size:13px;color:var(--text);border:1px solid var(--line);border-radius:6px;padding:1px 7px}
@media (max-width:640px){.row{flex-wrap:wrap}.meta{order:3;flex-basis:100%}}
</style></head><body><div class="wrap">
<div class="k">Rosetta dbt Studio · dbt v1</div>
<h1>Agentic dbt Development: crash course slides</h1>
<p class="lead">__N__ sections, __TOTAL__ slides. Each slide carries a talk track ("Say") and on-screen actions ("On screen"). Open a section, press <kbd>P</kbd> for the presenter window, then share only the slides window.</p>
<div class="keys"><kbd>→ / Space</kbd><span>Next slide (<kbd>←</kbd> back)</span><kbd>P</kbd><span>Presenter window: current + next slide, talk track, timer. Stays in sync with the slides.</span><kbd>N</kbd><span>Notes drawer inside the slides window (for rehearsal only)</span><kbd>S</kbd><span>Script: every slide with its notes, printable</span><kbd>T</kbd><span>Light / dark theme</span><kbd>F</kbd><span>Fullscreen</span><kbd>Amber numbers</kbd><span>On real-data slides, click a number, type your dry-run result, press Esc. It is saved in this browser.</span></div>
__CARDS__
</div></body></html>"""
with open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(INDEX.replace('__CARDS__', '\n'.join(cards)).replace('__N__', str(len(DECKS))).replace('__TOTAL__', str(total)))

print('decks:', len(DECKS), 'slides:', total)
for r in index_rows:
    print(r[0], r[4], r[5])
