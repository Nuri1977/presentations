"""Re-screenshot chosen slides into an existing video build and re-run its saved encode commands.
usage: python3 refresh_frames.py <slides html dir> <video out dir> s00:1 s01:1 ...   (section:slide numbers, 1-based)
"""
import json
import os
import pathlib
import subprocess
import sys

from playwright.sync_api import sync_playwright

sys.path.insert(0, os.path.dirname(__file__))
import content_a  # noqa: E402
import content_b  # noqa: E402
import content_c  # noqa: E402

SRC, OUT = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
want = {}
for a in sys.argv[3:]:
    sec, sl = a.split(':')
    want.setdefault(sec, []).append(int(sl))
decks = {('s%02d' % d['num']): d for d in content_a.DECKS + content_b.DECKS + content_c.DECKS}
with sync_playwright() as p:
    b = p.chromium.launch(args=['--force-color-profile=srgb', '--hide-scrollbars'])
    ctx = b.new_context(viewport={'width': 1920, 'height': 1080}, device_scale_factor=2)
    nums = json.loads((OUT / 'numbers.json').read_text()) if (OUT / 'numbers.json').exists() else {}
    init = ''.join("try{localStorage.setItem(%s,%s)}catch(e){};" % (json.dumps('aidbt:%s:%s' % (sec, k)), json.dumps(v))
                   for sec, kv in nums.items() for k, v in kv.items())
    if init:
        ctx.add_init_script(init)
    pg = ctx.new_page()
    for sec, slides in want.items():
        d = decks[sec]
        pg.goto((SRC / (d['file'] + '.html')).resolve().as_uri(), wait_until='domcontentloaded')
        pg.add_style_tag(content='.slide{transition:none!important}#progress{display:none!important}')
        pg.wait_for_timeout(1200)
        for n in slides:
            pg.keyboard.press('Home')
            for _ in range(n - 1):
                pg.keyboard.press('ArrowRight')
            pg.wait_for_timeout(200)
            pg.screenshot(path=str(OUT / 'frames' / sec / f'{n:02d}.png'))
    b.close()
for sec in want:
    d = decks[sec]
    base = '%s-%s' % (sec, d['file'][4:])
    for name in (base, base + '-recap'):
        sh = OUT / 'encode' / f'{name}.sh'
        subprocess.run(['bash', str(sh)], check=True)
        print('re-encoded', name, flush=True)
