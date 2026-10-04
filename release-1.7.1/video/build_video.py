"""Render presentation-slides.html + its built-in narration to an MP4 with a local voice.

  python3 build_video.py --deck ../presentation-slides.html --out ../video --voice af_heart

Needs: kokoro-onnx (+ kokoro-v1.0.onnx, voices-v1.0.bin next to this script),
Playwright with Chromium, ffmpeg. Everything runs offline once the model files exist.
"""
import argparse, json, os, re, subprocess, pathlib
import numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
from playwright.sync_api import sync_playwright

ap = argparse.ArgumentParser()
ap.add_argument('--deck', required=True)
ap.add_argument('--out', required=True)
ap.add_argument('--voice', default='af_heart')
ap.add_argument('--speed', type=float, default=1.0)
ap.add_argument('--name', default='rosetta-dbt-studio-release-1.7.1')
ap.add_argument('--lead', type=float, default=0.7)
ap.add_argument('--tail', type=float, default=0.9)
ap.add_argument('--gap', type=float, default=0.28)
ap.add_argument('--xf', type=float, default=0.5)
ap.add_argument('--end-hold', type=float, default=0.0, help='extra seconds on the last slide')
args = ap.parse_args()

HERE = pathlib.Path(__file__).parent
OUT = pathlib.Path(args.out); OUT.mkdir(parents=True, exist_ok=True)
FR = OUT / 'frames'; FR.mkdir(exist_ok=True)
SR = 24000
LEAD, TAIL, GAP, XF = args.lead, args.tail, args.gap, args.xf   # seconds: before speech, after speech, between sentences, crossfade

# ---- 1. Narration from the deck ------------------------------------------------
html = pathlib.Path(args.deck).read_text()
narr = re.findall(r'\{ title: "(.*?)", text: "(.*?)" \}', html)
assert narr, 'NARRATION array not found'

# Spoken forms so the voice reads versions, acronyms and URLs naturally (display text stays unchanged).
SAY = [
    (r'\b1\.6\.82\b', 'one point six point eighty-two'), (r'\b1\.6\.83\b', 'one point six point eighty-three'),
    (r'\b1\.7\.0\b', 'one point seven point oh'), (r'\b1\.7\.1\b', 'one point seven point one'),
    (r'\b1\.8\b', 'one point eight'), (r'\b1\.7\b', 'one point seven'),
    (r'rosettadb\.io', 'rosetta D B dot I O'), (r'kinetica-dbt-adapter', 'kinetica D B T adapter'),
    (r'\brosettadb\b', 'rosetta D B'), (r'\bdbt\b', 'D B T'), (r'\bdf\b', 'D F'), (r'\bDDL\b', 'D D L'),
    (r'\bSSL\b', 'S S L'), (r'\bTLS\b', 'T L S'), (r'\bSQL\b', 'sequel'), (r'\bSQLite\b', 'sequel-lite'),
    (r'\bMySQL\b', 'My sequel'), (r'\bPyPI\b', 'pie pie'), (r'\bOAuth\b', 'oh auth'), (r'\bETL\b', 'E T L'),
    (r'SELECT star', 'select star'), (r'\bCOUNT\b', 'count'), (r'\bINSERT\b', 'insert'),
    (r'\bAI\b', 'A I'), (r'\bDuckDB\b', 'duck D B'), (r'17th', 'seventeenth'), (r'22nd', 'twenty-second'),
    (r'29th', 'twenty-ninth'), (r'2nd', 'second'), (r'’', "'"),
]
def spoken(t):
    for a, b in SAY: t = re.sub(a, b, t)
    return t

def sentences(t):
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+(?=[A-Z0-9])', t) if s.strip()]

# ---- 2. Voice --------------------------------------------------------------------
k = Kokoro(str(HERE / 'kokoro-v1.0.onnx'), str(HERE / 'voices-v1.0.bin'))
clips = []   # per slide: (audio array, [(start, end, display sentence)])
for i, (title, text) in enumerate(narr, 1):
    parts, cues, t = [], [], 0.0
    for s in sentences(text):
        a, sr = k.create(spoken(s), voice=args.voice, speed=args.speed, lang='en-us')
        assert sr == SR
        parts += [a, np.zeros(int(GAP * SR), dtype=np.float32)]
        cues.append((t, t + len(a) / SR, s)); t += len(a) / SR + GAP
    audio = np.concatenate(parts[:-1])
    clips.append((audio, cues))
    sf.write(OUT / f'slide-{i:02d}.wav', audio, SR)
    print(f'voice  slide {i:2d}  {len(audio)/SR:5.1f}s  {title}')

# ---- 3. Slide frames -------------------------------------------------------------
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': 1920, 'height': 1080}, device_scale_factor=1)
    pg.goto(pathlib.Path(args.deck).resolve().as_uri() + '#1')
    pg.wait_for_load_state('networkidle')
    pg.evaluate("document.body.classList.add('clean')")
    for i in range(len(narr)):
        pg.evaluate(f'show({i})'); pg.wait_for_timeout(900)
        pg.screenshot(path=str(FR / f'{i+1:02d}.png'))
    b.close()

# ---- 4. Timeline, audio track, subtitles -----------------------------------------
durs = [LEAD + len(a) / SR + TAIL for a, _ in clips]
durs[-1] += args.end_hold
starts, t = [], 0.0
for d in durs: starts.append(t); t += d - XF
total = starts[-1] + durs[-1]
track = np.zeros(int(total * SR) + SR, dtype=np.float32)
srt, n = [], 1
fmt = lambda s: f'{int(s//3600):02d}:{int(s%3600//60):02d}:{int(s%60):02d},{int(s*1000%1000):03d}'
for (a, cues), st in zip(clips, starts):
    o = int((st + LEAD) * SR); track[o:o + len(a)] += a
    for c0, c1, s in cues:
        srt.append(f'{n}\n{fmt(st+LEAD+c0)} --> {fmt(st+LEAD+c1)}\n{s}\n'); n += 1
peak = np.abs(track).max(); track = track / peak * 0.89 if peak else track
sf.write(OUT / 'narration.wav', track, SR)
(OUT / f'{args.name}.srt').write_text('\n'.join(srt))
json.dump({'voice': args.voice, 'slides': [{'slide': i+1, 'start': round(s, 2), 'duration': round(d, 2)} for i, (s, d) in enumerate(zip(starts, durs))]},
          open(OUT / 'timeline.json', 'w'), indent=2)

# ---- 5. Video: stills + crossfades + narration ------------------------------------
inp, flt = [], []
for i, d in enumerate(durs):
    inp += ['-loop', '1', '-framerate', '30', '-t', f'{d:.3f}', '-i', str(FR / f'{i+1:02d}.png')]
prev = '[0:v]'
for i in range(1, len(durs)):
    lab = f'[v{i}]'
    flt.append(f'{prev}[{i}:v]xfade=transition=fade:duration={XF}:offset={starts[i]:.3f}{lab}')
    prev = lab
flt.append(f'{prev}format=yuv420p[vout]')
cmd = ['ffmpeg', '-y', '-loglevel', 'error', *inp, '-i', str(OUT / 'narration.wav'),
       '-filter_complex', ';'.join(flt), '-map', '[vout]', '-map', f'{len(durs)}:a',
       '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-tune', 'stillimage', '-r', '30',
       '-c:a', 'aac', '-b:a', '192k', '-t', f'{total:.3f}', '-movflags', '+faststart', str(OUT / f'{args.name}.mp4')]
subprocess.run(cmd, check=True)
print(f'done  {total:.1f}s  ->  {OUT / (args.name + ".mp4")}')
