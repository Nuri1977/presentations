"""Helpers for writing slide content. Every text field goes through md()."""
import html
import re

# ---------------------------------------------------------------- inline markdown
def md(s):
    if s is None:
        return None
    parts = re.split(r'(`[^`]+`)', s)
    out = []
    for p in parts:
        if len(p) >= 2 and p.startswith('`') and p.endswith('`'):
            out.append('<code>' + html.escape(p[1:-1], quote=False) + '</code>')
        else:
            e = html.escape(p, quote=False)
            e = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', e)
            e = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', e)
            e = re.sub(r'==(.+?)==', r'<mark>\1</mark>', e)
            e = e.replace('\n', '<br>')
            for t in ('br', 'em', '/em'):
                e = e.replace('&lt;%s&gt;' % t, '<%s>' % t)
            out.append(e)
    return ''.join(out)


def mdl(items):
    return [md(x) if isinstance(x, str) else x for x in (items or [])]


# ---------------------------------------------------------------- code highlighting
SQL_KW = set("""select from where and or not as with join left right inner outer full cross on group by order having limit
case when then else end null is in create schema table replace if exists distinct union all over partition row_number
qualify cast interval true false coalesce count sum min max avg filter between like insert into values update set delete
view asc desc date timestamp decimal integer varchar boolean double round extract day month year hour minute""".split())

_SQL = re.compile(r"(?P<j>\{\{.*?\}\}|\{%-?.*?-?%\}|\{#.*?#\})|(?P<c>--[^\n]*)|(?P<s>'[^'\n]*'|\"[^\"\n]*\")|"
                  r"(?P<w>\b[A-Za-z_][A-Za-z_0-9]*\b)|(?P<n>\b\d+(?:\.\d+)?\b)", re.S)
_YAML = re.compile(r"(?P<j>\{\{.*?\}\}|\{%-?.*?-?%\})|(?P<c>(?<![\w\"'])#[^\n]*)|(?P<k>^[ \t]*(?:- )?)(?P<kk>[A-Za-z_+][\w\-+.]*)(?=:)|"
                   r"(?P<s>'[^'\n]*'|\"[^\"\n]*\")|(?P<n>(?<![\w.])\d+(?:\.\d+)?(?![\w.]))", re.M | re.S)
_MD = re.compile(r"(?P<h>^#{1,6} [^\n]*)|(?P<m>^---$)|(?P<k>^)(?P<kk>name|description)(?=:)|(?P<c>^- )", re.M)
_SH = re.compile(r"(?P<c>#[^\n]*)|(?P<s>'[^'\n]*'|\"[^\"\n]*\")|(?P<w>\b(?:dbt|git|select)\b)|(?P<y>--?[A-Za-z][\w-]*)|(?P<n>[+]\w+|\w+[+])", re.M)


def _span(cls, txt):
    return '<span class="tk-%s">%s</span>' % (cls, html.escape(txt, quote=False))


def hl(code, lang):
    code = code.strip('\n')
    esc = lambda t: html.escape(t, quote=False)
    if lang == 'csv':
        lines = code.split('\n')
        out = [_span('y', lines[0])] + [esc(l).replace(',', '<span class="tk-m">,</span>') for l in lines[1:]]
        return '\n'.join(out)
    pat = {'sql': _SQL, 'yaml': _YAML, 'md': _MD, 'sh': _SH}.get(lang)
    if pat is None:
        return esc(code)
    out, pos = [], 0
    for m in pat.finditer(code):
        out.append(esc(code[pos:m.start()]))
        g = m.groupdict()
        if g.get('kk') is not None:
            out.append(esc(g.get('k') or '') + _span('y', g['kk']))
        elif g.get('w') is not None:
            w = g['w']
            if lang == 'sql':
                out.append(_span('k', w) if w.lower() in SQL_KW else esc(w))
            else:
                out.append(_span('k', w))
        else:
            for name, cls in (('j', 'j'), ('c', 'c'), ('s', 's'), ('n', 'n'), ('h', 'h'), ('m', 'm'), ('y', 'y')):
                if g.get(name) is not None:
                    if lang == 'md' and name == 'c':
                        out.append(_span('m', g[name]))
                    else:
                        out.append(_span(cls, g[name]))
                    break
            else:
                out.append(esc(m.group(0)))
        pos = m.end()
    out.append(esc(code[pos:]))
    return ''.join(out)


def code_size(code, aside):
    lines = code.strip('\n').split('\n')
    n = len(lines)
    maxlen = max(len(l) for l in lines)
    avail_w = (1680 - 560 if aside else 1680) - 70
    size_w = avail_w / (0.61 * max(maxlen, 20))
    size_h = 600 / (1.5 * max(n, 6))
    return int(max(17, min(28, size_w, size_h)))


# ---------------------------------------------------------------- slide constructors
def _n(say, do):
    return {'say': mdl(say), 'do': mdl(do)}


def title(title, subtitle=None, chips=None, kicker=None, say=None, do=None):
    return dict(type='title', title=md(title), subtitle=md(subtitle), chips=mdl(chips), kicker=md(kicker), notes=_n(say, do))


def statement(text, sub=None, kicker=None, kclass=None, say=None, do=None):
    return dict(type='statement', text=md(text), sub=md(sub), kicker=md(kicker), kclass=kclass, notes=_n(say, do))


def bullets(title, items, kicker=None, cols=1, numbered=False, foot=None, say=None, do=None):
    its = []
    for it in items:
        if isinstance(it, tuple):
            its.append({'t': md(it[0]), 'd': md(it[1]) if len(it) > 1 else None})
        else:
            its.append(md(it))
    return dict(type='bullets', title=md(title), items=its, kicker=md(kicker), cols=cols, numbered=numbered, foot=md(foot), notes=_n(say, do))


def flow(title, steps, kicker=None, caption=None, foot=None, say=None, do=None):
    st = []
    for s in steps:
        s = dict(s)
        for k in ('label', 'sub', 'tag'):
            if s.get(k):
                s[k] = md(s[k])
        st.append(s)
    return dict(type='flow', title=md(title), steps=st, kicker=md(kicker), caption=md(caption), foot=md(foot), notes=_n(say, do))


def columns(title, cols, kicker=None, verdict=None, foot=None, say=None, do=None):
    cs = []
    for c in cols:
        c = dict(c)
        c['title'] = md(c['title'])
        if c.get('sub'):
            c['sub'] = md(c['sub'])
        if c.get('foot'):
            c['foot'] = md(c['foot'])
        if c.get('items'):
            c['items'] = mdl(c['items'])
        if c.get('code'):
            c['codeHtml'] = hl(c.pop('code'), c.pop('lang', 'sql'))
        cs.append(c)
    return dict(type='columns', title=md(title), cols=cs, kicker=md(kicker), verdict=md(verdict), foot=md(foot), notes=_n(say, do))


def code(title, file, src, lang, kicker=None, aside=None, aside_title=None, foot=None, size=None, say=None, do=None):
    return dict(type='code', title=md(title), file=html.escape(file or ''), lang=lang if lang != 'md' else 'markdown',
                codeHtml=hl(src, lang), size=size or code_size(src, bool(aside)), kicker=md(kicker),
                aside=mdl(aside) if aside else None, asideTitle=md(aside_title), foot=md(foot), notes=_n(say, do))


DOCS = 'https://docs.getdbt.com/'


def docs(page, path, points, quote=None, kicker=None, foot=None, say=None, do=None):
    url = DOCS + path + ('&' if '?' in path else '?') + 'version=1'
    return dict(type='docs', page=md(page), url=url, urlShow=html.escape(url.replace('https://', '')), points=mdl(points),
                quote=md(quote), kicker=md(kicker), foot=md(foot), notes=_n(say, do))


MODES = {'code': ('Code mode', 'code'), 'ask': ('Ask mode', 'ask'), 'sql': ('Code mode', 'sql')}


def prompt(text, where='AI chat · dbt project', mode='code', watch=None, habits=None, kicker='Prompt', say=None, do=None):
    n = len(text)
    base = 44 if n < 200 else 40 if n < 340 else 36 if n < 480 else 33 if n < 620 else 30
    if not watch:
        base = min(48, base + 3)
    label, key = MODES[mode]
    return dict(type='prompt', text=md(text), where=md(where), mode=label, modeKey=key, watch=mdl(watch) if watch else None,
                habits=habits or [], size=base, kicker=md(kicker), notes=_n(say, do))


def table(title, headers, rows, kicker=None, size=None, foot=None, hl_rows=None, say=None, do=None):
    rs = []
    for i, r in enumerate(rows):
        cells = [md(c) for c in r]
        rs.append({'cells': cells, 'hl': bool(hl_rows and i in hl_rows)})
    return dict(type='table', title=md(title), headers=mdl(headers), rows=rs, kicker=md(kicker), size=size, foot=md(foot), notes=_n(say, do))


def realdata(title, stats, kicker=None, foot=None, say=None, do=None):
    st = []
    for s in stats:
        st.append({'v': md(s[0]), 'label': md(s[1]), 'edit': s[2] if len(s) > 2 else None})
    return dict(type='realdata', title=md(title), stats=st, kicker=md(kicker), foot=md(foot), notes=_n(say, do))


# DAG nodes introduced per section (cumulative "built" is computed)
DAG_NEW = {
    1: ['src_trips'], 3: ['src_trips'], 4: ['seed_zones', 'seed_pay', 'seed_rate'], 5: ['stg_trips', 'stg_zones'],
    8: ['int', 'fct', 'dim_zones', 'agg'], 11: ['src_vendors', 'snap', 'dim_vendors'], 12: ['exp'],
}
ALL_NODES = ['src_trips', 'seed_zones', 'seed_pay', 'seed_rate', 'src_vendors', 'stg_trips', 'stg_zones', 'snap', 'int',
             'fct', 'dim_zones', 'dim_vendors', 'agg', 'exp']


def built_before(sec):
    b = []
    for s, ids in DAG_NEW.items():
        if s < sec and s != 1:
            b += ids
    return b


def dag(title, sec, new=None, all_built=False, kicker=None, files=None, foot=None, say=None, do=None):
    if all_built:
        built, nw = ALL_NODES, (new or [])
    else:
        nw = new if new is not None else DAG_NEW.get(sec, [])
        built = built_before(sec)
    return dict(type='dag', title=md(title), new=nw, built=built, kicker=md(kicker), files=[html.escape(f) for f in (files or [])],
                foot=md(foot), notes=_n(say, do))


def blocks(title, current=None, upto=None, kicker=None, foot=None, say=None, do=None):
    return dict(type='blocks', title=md(title), current=current or [], upto=upto, kicker=md(kicker), foot=md(foot), notes=_n(say, do))


def recap(title, items, tag, blocks=None, next=None, say=None, do=None):
    return dict(type='recap', title=md(title), items=mdl(items), tag=html.escape(tag), blocks=mdl(blocks) if blocks else [],
                next=md(next), notes=_n(say, do))


def habits(title, hl=None, kicker=None, foot=None, say=None, do=None):
    return dict(type='habits', title=md(title), hl=hl or [], kicker=md(kicker), foot=md(foot), notes=_n(say, do))


def steps(title, items, kicker=None, foot=None, say=None, do=None):
    its = []
    for it in items:
        if isinstance(it, tuple):
            its.append({'t': md(it[0]), 'cmd': html.escape(it[1]) if len(it) > 1 and it[1] else None})
        else:
            its.append({'t': md(it), 'cmd': None})
    return dict(type='steps', title=md(title), items=its, kicker=md(kicker), foot=md(foot), notes=_n(say, do))


BLOCKS = [
    {'name': 'models', 'sections': [5, 8, 10]},
    {'name': 'sources', 'sections': [3]},
    {'name': 'seeds', 'sections': [4]},
    {'name': 'data tests', 'sections': [6, 9]},
    {'name': 'macros', 'sections': [7]},
    {'name': 'analysis', 'sections': [7]},
    {'name': 'snapshots', 'sections': [11]},
    {'name': 'docs', 'sections': [12]},
    {'name': 'exposures', 'sections': [12]},
    {'name': 'metrics', 'sections': None},
    {'name': 'semantic models', 'sections': None},
    {'name': 'saved queries', 'sections': None},
    {'name': 'groups', 'sections': None},
    {'name': 'user-defined functions', 'sections': None},
]
