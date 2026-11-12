"""Build a lesson's slides.html from a short slides.yaml (white theme, same data-id / data-step contract).
  python3 tools/slides.py <lesson-folder>
slides.yaml: { number: "2.2", slides: [ {id, type, ...}, ... ] }
Types: title, statement, cards, steps, code, codes, table, recap, closing, html.
Any text field may hold inline HTML (<span class="accent">, <span class="mono">, code colour spans).
`step` on an item makes it appear at that beat step; `checked` adds the small source line.
"""
import sys, pathlib, html, yaml

L = pathlib.Path(sys.argv[1]).resolve()
spec = yaml.safe_load((L / 'slides.yaml').read_text())
N = str(spec['number'])
slides = spec['slides']
content = [s for s in slides if s['type'] not in ('title', 'closing')]


def st(x):
    return f' s" data-step="{x["step"]}' if isinstance(x, dict) and x.get('step') is not None else ''


def footer(i):
    w = round(100 * (i + 1) / max(1, len(content)))
    return (f'<div class="footer"><div class="bar" style="width:{w}%"></div><img src="../brand/logo_new.svg" alt="">'
            f'<div class="where">Project 2 · <b>Lesson {N}</b></div></div>')


def checked(s):
    return f'<div class="checked">{s["checked"]}</div>' if s.get('checked') else ''


def head(s):
    out = f'<div class="eyebrow">{s.get("eyebrow", "")}</div>'
    if s.get('h2'): out += f'<h2>{s["h2"]}</h2>'
    return out


def card(c):
    cls = c.get('cls', '')
    body = ''
    if c.get('k'): body += f'<div class="k">{c["k"]}</div>'
    if c.get('t'): body += f'<div class="t">{c["t"]}</div>'
    if c.get('d'): body += f'<div class="d">{c["d"]}</div>'
    if c.get('ticks'): body += '<ul class="ticks">' + ''.join(f'<li{" class=no" if t.startswith("!") else ""}>{t.lstrip("!")}</li>' for t in c['ticks']) + '</ul>'
    if c.get('mono'): body += f'<div class="mono" style="font-size:30px;margin-top:14px;color:var(--muted)">{c["mono"]}</div>'
    return f'<div class="card {cls}{st(c)}">{body}</div>'


def codecard(c, extra=''):
    return (f'<div class="codecard{st(c)}" style="{extra}"><div class="filetab"><span class="ic"></span>{c.get("file", "")}</div>'
            f'<div class="code" style="font-size:{c.get("size", 34)}px">{c["code"].rstrip()}</div></div>')


def note(n):
    if not n: return ''
    cls = n.get('cls', 'hot')
    return f'<div class="card {cls}{st(n)}" style="padding:26px 34px;font-size:{n.get("size", 36)}px;font-weight:700;line-height:1.3;margin-top:28px">{n["text"]}</div>'


def section(s, i):
    t = s['type']
    if t == 'title':
        badges = ''.join(f'<span class="badge">{b}</span>' for b in s.get('badges', []))
        return f'''<section class="stage" data-id="{s['id']}">
  <div class="bg hero"></div>
  <div class="title-grid"><div>
    <div class="eyebrow">Project 2 · Lesson {N}</div>
    <h1 style="margin-top:28px;font-size:{s.get('size', 124)}px">{s['h1']}</h1>
    <p class="lead">{s.get('lead', '')}</p>
    <div class="badges">{badges}</div>
  </div><img class="hero-icon" src="../brand/icon.svg" alt=""></div>
  <img class="lockup" src="../brand/logo_new.svg" alt="Rosetta DBT Studio">
</section>'''
    if t == 'closing':
        return f'''<section class="stage" data-id="{s['id']}">
  <div class="bg hero"></div>
  <div class="next-grid"><div>
    <div class="eyebrow">Next</div>
    <h1 style="margin-top:28px">{s.get('lesson', '')}</h1>
    <h2 style="font-size:{s.get('size', 88)}px">{s['h2']}</h2>
    <div class="repo">github.com/Nuri1977/ethereum-ducklake-dbt</div>
  </div><img class="logo-hero" src="../brand/icon.svg" alt="Rosetta DBT Studio"></div>
</section>'''
    idx = content.index(s)
    inner = head(s)
    if t == 'statement':
        pills = ''.join(f'<span class="pill {p.get("cls", "")}">{p["text"]}</span>' if isinstance(p, dict) else f'<span class="pill">{p}</span>' for p in s.get('pills', []))
        inner += f'<div class="statement"><div class="big{st(s.get("bigstep") and {"step": s["bigstep"]} or {})}">{s["big"]}</div>'
        if pills: inner += f'<div class="badges{st({"step": s.get("pillstep", 1)})}">{pills}</div>'
        inner += '</div>'
    elif t == 'cards':
        n = s.get('cols', len(s['cards']))
        inner += f'<div class="row {["", "one", "two", "three", "four"][n]}">' + ''.join(card(c) for c in s['cards']) + '</div>' + note(s.get('note'))
    elif t == 'steps':
        inner += '<div class="steps">' + ''.join(
            f'<div class="step{" hot" if x.get("hot") else ""}{st(x)}"><div class="num">{j + 1}</div><div><div class="t">{x["t"]}</div>'
            + (f'<div class="d">{x["d"]}</div>' if x.get('d') else '') + '</div></div>' for j, x in enumerate(s['steps'])) + '</div>' + note(s.get('note'))
    elif t == 'code':
        inner += codecard(s['codeblock'], 'margin-top:34px') + note(s.get('note'))
    elif t == 'codes':
        inner += '<div class="split">' + ''.join(codecard(c) for c in s['codes']) + '</div>' + note(s.get('note'))
    elif t == 'table':
        rows = s['rows']; hot = s.get('hotcol')
        def cell(tag, v, j): return f'<{tag}{" class=hot" if hot is not None and j == hot else ""}>{v}</{tag}>'
        inner += f'<table class="t{st(s)}"><tr>' + ''.join(cell('th', h, j) for j, h in enumerate(s['head'])) + '</tr>' + ''.join(
            '<tr>' + ''.join(cell('td', v, j) for j, v in enumerate(r)) + '</tr>' for r in rows) + '</table>' + note(s.get('note'))
    elif t == 'recap':
        inner = '<div class="eyebrow">Recap</div><h2>' + s.get('h2', 'What to remember') + '</h2><div class="recap s" data-step="1">' + ''.join(
            f'<div class="item"><div class="num">{j + 1}</div><div>{x}</div></div>' for j, x in enumerate(s['items'])) + '</div>'
    elif t == 'html':
        inner += s['html']
    return f'''<section class="stage" data-id="{s['id']}">
  <div class="bg"></div>
  <div class="pad">{inner}</div>
  {footer(idx)}
  {checked(s)}
</section>'''


title = spec.get('title', f'Lesson {N}')
out = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Lesson {N} · {html.escape(title)}</title>
<!-- Generated by tools/slides.py from slides.yaml. Theme: ../slides-theme (white). -->
<link rel="stylesheet" href="../slides-theme/theme.css">
<style>{spec.get('css', '')}</style>
</head>
<body>
<div id="viewport">
{chr(10).join(section(s, i) for i, s in enumerate(slides))}
</div>
<script src="../slides-theme/theme.js"></script>
</body>
</html>
'''
(L / 'slides.html').write_text(out)
print('wrote', L / 'slides.html', len(slides), 'slides')
