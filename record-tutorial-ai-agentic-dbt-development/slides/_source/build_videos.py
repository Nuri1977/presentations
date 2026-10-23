"""Narrated videos for the crash course, one per section, with a local Kokoro voice.

Per section it writes:
  sNN-<name>.mp4         slides 1..N-1 with voiceover (your demo recording goes after this)
  sNN-<name>-recap.mp4   the recap slide (goes after your demo)
  matching .srt files, plus audio/ and frames/ for re-encoding

usage:
  python3 build_videos.py --slides <html dir> --out <dir> --models <dir with kokoro files> [--sections 0,1,2]
Optional numbers.json in --out: {"s01": {"neg_fare": "12,345", ...}} fills the amber real-data values.
"""
import argparse
import json
import os
import pathlib
import re
import subprocess
import sys
import time

import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro
from playwright.sync_api import sync_playwright

sys.path.insert(0, os.path.dirname(__file__))
import content_a  # noqa: E402
import content_b  # noqa: E402
import content_c  # noqa: E402
from tts import TTS  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument('--slides', required=True)
ap.add_argument('--out', required=True)
ap.add_argument('--models', required=True)
ap.add_argument('--sections', default='')
ap.add_argument('--voice', default='af_heart')
ap.add_argument('--speed', type=float, default=1.0)
ap.add_argument('--scale', type=int, default=2, help='2 = 3840x2160 (4K), 1 = 1080p')
ap.add_argument('--crf', type=int, default=16)
ap.add_argument('--preset', default='veryfast')
ap.add_argument('--gop', type=int, default=300, help='keyframe interval in frames; static slides need few keyframes')
ap.add_argument('--lead', type=float, default=0.7)
ap.add_argument('--tail', type=float, default=0.9)
ap.add_argument('--gap', type=float, default=0.28)
ap.add_argument('--xf', type=float, default=0.5)
args = ap.parse_args()

DECKS = content_a.DECKS + content_b.DECKS + content_c.DECKS
if args.sections:
    keep = {int(x) for x in args.sections.split(',')}
    DECKS = [d for d in DECKS if d['num'] in keep]
OUT = pathlib.Path(args.out)
OUT.mkdir(parents=True, exist_ok=True)
SR = 24000
NUMBERS = json.loads((OUT / 'numbers.json').read_text()) if (OUT / 'numbers.json').exists() else {}

SAY = [
    (r'\bdbt\b', 'D B T'), (r'\bSQL\b', 'sequel'), (r'\bDuckDB\b', 'duck D B'), (r'\bYAML\b', 'yammel'),
    (r'\byml\b', 'yammel'), (r'\bParquet\b', 'par-kay'), (r'\bCSV\b', 'C S V'), (r'\bAI\b', 'A I'),
    (r'\bIDs\b', 'I Ds'), (r'\bID\b', 'I D'), (r'\bAPIs\b', 'A P Is'), (r'\bVeriFone\b', 'Veri-Fone'),
    (r'\bMyle\b', 'Mile'), (r'\bJinja\b', 'Jin-ja'), (r'’', "'"),
]


def spoken(t):
    for a, b in SAY:
        t = re.sub(a, b, t)
    return t


def sentences(t):
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+(?=[A-Z0-9])', t) if s.strip()]


def fmt(s):
    return f'{int(s // 3600):02d}:{int(s % 3600 // 60):02d}:{int(s % 60):02d},{int(s * 1000 % 1000):03d}'


def assemble(clips, frames, name, end_hold=0.0):
    """clips: list of (audio, cues); frames: list of png paths. Writes name.mp4/.srt."""
    lead, tail, xf = args.lead, args.tail, args.xf
    durs = [lead + len(a) / SR + tail for a, _ in clips]
    durs[-1] += end_hold
    starts, t = [], 0.0
    for d in durs:
        starts.append(t)
        t += d - xf
    total = starts[-1] + durs[-1]
    track = np.zeros(int(total * SR) + SR, dtype=np.float32)
    srt, n = [], 1
    for (a, cues), st in zip(clips, starts):
        o = int((st + lead) * SR)
        track[o:o + len(a)] += a
        for c0, c1, s in cues:
            srt.append(f'{n}\n{fmt(st + lead + c0)} --> {fmt(st + lead + c1)}\n{s}\n')
            n += 1
    peak = np.abs(track).max()
    track = track / peak * 0.89 if peak else track
    wav = OUT / 'audio' / f'{name}.wav'
    sf.write(wav, track, SR)
    (OUT / f'{name}.srt').write_text('\n'.join(srt))
    inp, flt = [], []
    for i, d in enumerate(durs):
        inp += ['-i', str(frames[i])]
        nf = int(round(d * 30))
        # decode each slide once and repeat it in memory (re-decoding a 4K PNG per frame is the slow part)
        flt.append(f'[{i}:v]format=yuv420p,loop=loop={nf - 1}:size=1:start=0,setpts=N/30/TB[s{i}]')
    prev = '[s0]'
    for i in range(1, len(durs)):
        flt.append(f'{prev}[s{i}]xfade=transition=fade:duration={xf}:offset={starts[i]:.3f}[v{i}]')
        prev = f'[v{i}]'
    flt.append(f'{prev}format=yuv420p[vout]')
    cmd = ['ffmpeg', '-y', '-loglevel', 'error', *inp, '-i', str(wav), '-filter_complex', ';'.join(flt),
           '-map', '[vout]', '-map', f'{len(durs)}:a', '-c:v', 'libx264', '-preset', args.preset, '-crf', str(args.crf),
           '-tune', 'stillimage', '-profile:v', 'high', '-level', '5.1', '-r', '30', '-g', str(args.gop),
           '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709',
           '-c:a', 'aac', '-b:a', '384k', '-ar', '48000', '-t', f'{total:.3f}', '-movflags', '+faststart',
           str(OUT / f'{name}.mp4')]
    (OUT / 'encode').mkdir(exist_ok=True)
    (OUT / 'encode' / f'{name}.sh').write_text(' '.join("'%s'" % c if (' ' in c or ';' in c or '[' in c) else c for c in cmd) + '\n')
    subprocess.run(cmd, check=True)
    return total, durs, starts


def render_frames(d, fdir):
    fdir.mkdir(parents=True, exist_ok=True)
    code = 's%02d' % d['num']
    nums = NUMBERS.get(code, {})
    init = ''.join("try{localStorage.setItem(%s,%s)}catch(e){};" % (json.dumps('aidbt:%s:%s' % (code, k)), json.dumps(v))
                   for k, v in nums.items())
    with sync_playwright() as p:
        b = p.chromium.launch(args=['--force-color-profile=srgb', '--hide-scrollbars'])
        ctx = b.new_context(viewport={'width': 1920, 'height': 1080}, device_scale_factor=args.scale)
        if init:
            ctx.add_init_script(init)
        pg = ctx.new_page()
        pg.goto(pathlib.Path(args.slides, d['file'] + '.html').resolve().as_uri(), wait_until='domcontentloaded')
        pg.add_style_tag(content='.slide{transition:none!important}#progress{display:none!important}')
        pg.wait_for_timeout(1200)
        pg.keyboard.press('Home')
        for i in range(len(d['slides'])):
            if i:
                pg.keyboard.press('ArrowRight')
            pg.wait_for_timeout(150)
            pg.screenshot(path=str(fdir / f'{i + 1:02d}.png'))
        b.close()


k = Kokoro(str(pathlib.Path(args.models) / 'kokoro-v1.0.onnx'), str(pathlib.Path(args.models) / 'voices-v1.0.bin'))
(OUT / 'audio').mkdir(exist_ok=True)
report = json.loads((OUT / 'report.json').read_text()) if (OUT / 'report.json').exists() else {}
for d in DECKS:
    t0 = time.time()
    code = 's%02d' % d['num']
    base = '%s-%s' % (code, d['file'][4:])
    scripts = TTS[d['num']]
    assert len(scripts) == len(d['slides'])
    fdir = OUT / 'frames' / code
    render_frames(d, fdir)
    clips = []
    for i, text in enumerate(scripts, 1):
        parts, cues, t = [], [], 0.0
        for s in sentences(text):
            a, _ = k.create(spoken(s), voice=args.voice, speed=args.speed, lang='en-us')
            parts += [a, np.zeros(int(args.gap * SR), dtype=np.float32)]
            cues.append((t, t + len(a) / SR, s))
            t += len(a) / SR + args.gap
        clips.append((np.concatenate(parts[:-1]), cues))
    frames = [fdir / f'{i + 1:02d}.png' for i in range(len(scripts))]
    main_total, _, _ = assemble(clips[:-1], frames[:-1], base, end_hold=0.6)
    recap_total, _, _ = assemble(clips[-1:], frames[-1:], base + '-recap', end_hold=0.6)
    report[code] = {'main_s': round(main_total, 1), 'recap_s': round(recap_total, 1), 'build_s': round(time.time() - t0)}
    (OUT / 'report.json').write_text(json.dumps(report, indent=2))
    print(f'{base}: main {main_total:.1f}s, recap {recap_total:.1f}s, built in {time.time() - t0:.0f}s', flush=True)
print('done', flush=True)
