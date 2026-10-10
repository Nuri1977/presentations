"""Render a deck's NARRATION to an MP4 with a local Kokoro voice.
  python3 build_video.py --deck deck.html --out outdir --voice af_heart
  add --measure to synthesize the voice only and print the projected length
"""
import argparse, json, re, subprocess, pathlib
import numpy as np, soundfile as sf
from kokoro_onnx import Kokoro

ap = argparse.ArgumentParser()
ap.add_argument('--deck', required=True); ap.add_argument('--out', required=True)
ap.add_argument('--voice', default='af_heart', help="voice name, or a blend like 'af_heart+af_bella'"); ap.add_argument('--speed', type=float, default=1.0)
ap.add_argument('--name', default='rosetta-dbt-studio-release')
ap.add_argument('--lead', type=float, default=0.7); ap.add_argument('--tail', type=float, default=0.9)
ap.add_argument('--gap', type=float, default=0.28); ap.add_argument('--xf', type=float, default=0.5)
ap.add_argument('--end-hold', type=float, default=0.0)
ap.add_argument('--scale', type=int, default=2, help='2 = 3840x2160 (4K, default), 1 = 1080p')
ap.add_argument('--crf', type=int, default=16)
ap.add_argument('--measure', action='store_true')
args = ap.parse_args()
HERE = pathlib.Path(__file__).parent
OUT = pathlib.Path(args.out); OUT.mkdir(parents=True, exist_ok=True)
FR = OUT / 'frames'; FR.mkdir(exist_ok=True)
SR = 24000; LEAD, TAIL, GAP, XF = args.lead, args.tail, args.gap, args.xf

html = pathlib.Path(args.deck).read_text()
narr = re.findall(r'\{ title: "(.*?)", text: "(.*?)" \}', html)
assert narr, 'NARRATION array not found'
SAY = [  # spoken forms; extend per release
    (r'\b1\.7\.2\b', 'one point seven point two'),
    (r'\b1\.7\.1\b', 'one point seven point one'), (r'\b1\.7\.0\b', 'one point seven point oh'),
    (r'\b1\.7\b', 'one point seven'), (r'\b1\.8\b', 'one point eight'),
    (r'ChatGPT', 'Chat G P T'), (r'GPT-(\d)\.(\d)', r'G P T \1 point \2'), (r'GPT-(\d)', r'G P T \1'),
    (r'per-token', 'per token'), (r'\bAPI\b', 'A P I'), (r'\bS3\b', 'S three'), (r'\bCSV\b', 'C S V'),
    (r'rosettadb\.io', 'rosetta D B dot I O'), (r'\brosettadb\b', 'rosetta D B'), (r'\bdbt\b', 'D B T'), (r'\bDBT\b', 'D B T'),
    (r'\bdf\b', 'D F'), (r'\bDDL\b', 'D D L'), (r'\bSSL\b', 'S S L'), (r'\bTLS\b', 'T L S'),
    (r'\bSQL\b', 'sequel'), (r'\bSQLite\b', 'sequel-lite'), (r'\bMySQL\b', 'My sequel'), (r'\bPyPI\b', 'pie pie'),
    (r'\bOAuth\b', 'oh auth'), (r'\bETL\b', 'E T L'), (r'\bCOUNT\b', 'count'), (r'\bINSERT\b', 'insert'),
    (r'\bAI\b', 'A I'), (r'\bDuckDB\b', 'duck D B'), (r'’', "'"),
]
def spoken(t):
    for a, b in SAY: t = re.sub(a, b, t)
    return t
def sentences(t):
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+(?=[A-Z0-9])', t) if s.strip()]

k = Kokoro(str(HERE / 'kokoro-v1.0.onnx'), str(HERE / 'voices-v1.0.bin'))
VOICE = args.voice if '+' not in args.voice else np.mean([k.get_voice_style(v) for v in args.voice.split('+')], axis=0)
clips = []
for i, (title, text) in enumerate(narr, 1):
    parts, cues, t = [], [], 0.0
    for s in sentences(text):
        a, sr = k.create(spoken(s), voice=VOICE, speed=args.speed, lang='en-us')
        parts += [a, np.zeros(int(GAP * SR), dtype=np.float32)]
        cues.append((t, t + len(a) / SR, s)); t += len(a) / SR + GAP
    audio = np.concatenate(parts[:-1]); clips.append((audio, cues))
    sf.write(OUT / f'slide-{i:02d}.wav', audio, SR)
    print(f'voice slide {i:2d} {len(audio)/SR:5.1f}s {len(text.split()):3d}w {title}')

durs = [LEAD + len(a) / SR + TAIL for a, _ in clips]; durs[-1] += args.end_hold
starts, t = [], 0.0
for d in durs: starts.append(t); t += d - XF
total = starts[-1] + durs[-1]
if args.measure:
    print(f'projected total {total:.1f}s, {sum(len(x.split()) for _, x in narr)} words'); raise SystemExit

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(args=['--force-color-profile=srgb', '--hide-scrollbars'])
    pg = b.new_page(viewport={'width': 1920, 'height': 1080}, device_scale_factor=args.scale)
    pg.goto(pathlib.Path(args.deck).resolve().as_uri() + '#1'); pg.wait_for_load_state('networkidle')
    pg.evaluate("document.body.classList.add('clean')")
    for i in range(len(narr)):
        pg.evaluate(f'show({i})'); pg.wait_for_timeout(900); pg.screenshot(path=str(FR / f'{i+1:02d}.png'))
    b.close()

track = np.zeros(int(total * SR) + SR, dtype=np.float32); srt, n = [], 1
fmt = lambda s: f'{int(s//3600):02d}:{int(s%3600//60):02d}:{int(s%60):02d},{int(s*1000%1000):03d}'
for (a, cues), st in zip(clips, starts):
    o = int((st + LEAD) * SR); track[o:o + len(a)] += a
    for c0, c1, s in cues:
        srt.append(f'{n}\n{fmt(st+LEAD+c0)} --> {fmt(st+LEAD+c1)}\n{s}\n'); n += 1
peak = np.abs(track).max(); track = track / peak * 0.89 if peak else track
sf.write(OUT / 'narration.wav', track, SR)
(OUT / f'{args.name}.srt').write_text('\n'.join(srt))
json.dump({'voice': args.voice, 'speed': args.speed, 'slides': [{'slide': i+1, 'start': round(s, 2), 'duration': round(d, 2)}
           for i, (s, d) in enumerate(zip(starts, durs))]}, open(OUT / 'timeline.json', 'w'), indent=2)

inp, flt, prev = [], [], '[0:v]'
for i, d in enumerate(durs):
    inp += ['-loop', '1', '-framerate', '30', '-t', f'{d:.3f}', '-i', str(FR / f'{i+1:02d}.png')]
for i in range(1, len(durs)):
    flt.append(f'{prev}[{i}:v]xfade=transition=fade:duration={XF}:offset={starts[i]:.3f}[v{i}]'); prev = f'[v{i}]'
W, H = 1920 * args.scale, 1080 * args.scale
flt.append(f'{prev}scale={W}:{H}:flags=lanczos,format=yuv420p[vout]')
cmd = ['ffmpeg', '-y', '-loglevel', 'error', *inp, '-i', str(OUT / 'narration.wav'),
    '-filter_complex', ';'.join(flt), '-map', '[vout]', '-map', f'{len(durs)}:a',
    '-c:v', 'libx264', '-preset', 'slow', '-crf', str(args.crf), '-tune', 'stillimage',
    '-profile:v', 'high', '-level', '5.1', '-r', '30', '-g', '60',
    '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709',
    '-c:a', 'aac', '-b:a', '384k', '-ar', '48000', '-t', f'{total:.3f}', '-movflags', '+faststart',
    str(OUT / f'{args.name}.mp4')]
(OUT / 'encode.sh').write_text('#!/bin/bash\n# Re-encode from frames/ + narration.wav (paths relative to this folder)\ncd "$(dirname "$0")"\n' +
    ' '.join(("'" + c.replace(str(OUT) + '/', '') + "'") for c in cmd) + '\n')
subprocess.run(cmd, check=True)
print(f'done {total:.1f}s')
