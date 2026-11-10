"""Render slide build states, overlay cards and the thumbnail as 4K stills.

    python3 scripts/render_stills.py <course_dir> <lesson_dir>

Writes <lesson_dir>/render/slides/<slide>-<step>.png, render/cards/<beat>.png (transparent) and
<lesson_dir>/thumbnail.png (1280x720).
"""
import html, pathlib, re, sys
import yaml
from playwright.sync_api import sync_playwright

C, L = map(pathlib.Path, sys.argv[1:3])
lesson = yaml.safe_load((L / 'lesson.yaml').read_text())
R = L / 'render'
(R / 'slides').mkdir(parents=True, exist_ok=True)
(R / 'cards').mkdir(parents=True, exist_ok=True)

needed = []  # (slide, step)
for sc in lesson['scenes']:
    if sc['kind'] in ('title', 'closing'):
        needed.append((sc['slide'], None))
    elif sc['kind'] == 'slide':
        for b in sc['beats']:
            needed.append((sc['slide'], b.get('step')))

CARD = """<!doctype html><html><head><meta charset="utf-8"><style>
html,body{margin:0;width:1920px;height:1080px;background:transparent;font-family:Inter,system-ui,sans-serif}
.content{position:absolute;width:380px;padding:30px 32px;border:1px solid rgba(255,255,255,.16);border-radius:6px;
 background:rgba(6,8,13,.72);box-shadow:0 32px 90px rgba(0,0,0,.54);backdrop-filter:blur(20px);color:#fff}
.top-right{right:92px;top:108px}.top-left{left:92px;top:108px}.bottom-left{left:55px;bottom:140px}.bottom-right{right:92px;bottom:140px}
.eyebrow{display:flex;align-items:center;gap:8px;margin-bottom:12px;color:#ff9a3d;font-size:13px;font-weight:850;text-transform:uppercase;letter-spacing:.12em}
.eyebrow::before{content:"";width:24px;height:3px;border-radius:99px;background:linear-gradient(90deg,#ff7a1a,#ff9a3d)}
h2{margin:0;font-size:34px;line-height:1.02;font-weight:920;text-wrap:balance}
h2.mono{font-family:"JetBrains Mono",monospace;font-size:21px;line-height:1.3;font-weight:700;color:#ffd166;word-break:break-all}
p{margin:14px 0 0;color:#d7dce8;font-size:17px;line-height:1.4;font-weight:620}
</style></head><body><div class="content __POS__"><div class="eyebrow">__EYEBROW__</div><h2 class="__CLS__">__TITLE__</h2><p>__SUB__</p></div></body></html>"""

# Slides v2 courses (course.yaml: slides_theme: v2) get bigger cards set in the course's own fonts.
course = yaml.safe_load((C / 'course.yaml').read_text())
if course.get('slides_theme') == 'v2':
    import base64
    fonts = C / 'slides-theme' / 'fonts'
    face = lambda fam, f, w: (f"@font-face{{font-family:'{fam}';font-weight:{w};src:url(data:font/woff2;base64,"
                              + base64.b64encode((fonts / f).read_bytes()).decode() + ") format('woff2')}")
    CARD = (CARD.replace('<style>', '<style>' + face('Inter', 'Inter-Variable.woff2', '100 900') + face('JetBrains Mono', 'JetBrainsMono-Variable.woff2', '100 800'))
            .replace('width:380px;padding:30px 32px', 'width:500px;padding:36px 40px')
            .replace('font-size:13px;font-weight:850', 'font-size:18px;font-weight:850')
            .replace('h2{margin:0;font-size:34px', 'h2{margin:0;font-size:44px')
            .replace('font-size:21px;line-height:1.3', 'font-size:28px;line-height:1.3')
            .replace('p{margin:14px 0 0;color:#d7dce8;font-size:17px', 'p{margin:16px 0 0;color:#d7dce8;font-size:24px')
            .replace('.top-right{right:92px;top:108px}', '.top-right{right:72px;top:96px}'))

with sync_playwright() as p:
    b = p.chromium.launch(args=['--force-color-profile=srgb', '--hide-scrollbars'])
    pg = b.new_page(viewport={'width': 1920, 'height': 1080}, device_scale_factor=2)
    pg.goto((L / 'slides.html').resolve().as_uri() + '?render=1')
    pg.wait_for_load_state('networkidle')
    pg.evaluate('document.fonts.ready')
    for slide, step in dict.fromkeys(needed):
        pg.evaluate(f"show({slide!r}, {('undefined' if step is None else step)})")
        pg.wait_for_timeout(250)
        name = f"{slide}-{'all' if step is None else step}.png"
        pg.screenshot(path=str(R / 'slides' / name))
        print('slide', name)
    # thumbnail from the title slide
    pg.evaluate("show('title')"); pg.wait_for_timeout(250)
    pg.screenshot(path=str(R / 'slides' / '_thumb-4k.png'))
    cp = b.new_page(viewport={'width': 1920, 'height': 1080}, device_scale_factor=2)
    for sc in lesson['scenes']:
        for bt in sc.get('beats', []):
            c = bt.get('card')
            if not c:
                continue
            mono = bool(re.fullmatch(r'[^\s]+', c['title'])) and ('.' in c['title'] or '"' in c['title'])
            doc = (CARD.replace('__POS__', c.get('pos', 'top-right')).replace('__EYEBROW__', html.escape(c['eyebrow']))
                   .replace('__TITLE__', html.escape(c['title'])).replace('__SUB__', html.escape(c.get('sub', ''))).replace('__CLS__', 'mono' if mono else ''))
            cp.set_content(doc); cp.evaluate('document.fonts.ready'); cp.wait_for_timeout(100)
            cp.screenshot(path=str(R / 'cards' / f"{bt['id']}.png"), omit_background=True)
            print('card', bt['id'])
    b.close()

from PIL import Image
Image.open(R / 'slides' / '_thumb-4k.png').convert('RGB').resize((1280, 720), Image.LANCZOS).save(L / 'thumbnail.png')
print('thumbnail.png')
