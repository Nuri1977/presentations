"""Compose a lesson video: voice-paced timeline over recorded 4K stills, slides, cards, cursor and zooms.

    python3 scripts/compose.py <course_dir> <lesson_dir> [--workers 2] [--preview SECONDS]

Inputs (in <lesson_dir>/render): audio/beats.json + wavs, app/events.json + frames, slides/*.png, cards/*.png.
Outputs (in <lesson_dir>): <id>.mp4 (3840x2160 H.264 + AAC), <id>.srt, <id>.vtt, timeline.json,
render/narration.wav, render/composite/*.jpg, render/frames.txt.
"""
import argparse, functools, hashlib, json, math, os, pathlib, subprocess
from multiprocessing import Pool
import numpy as np, soundfile as sf, yaml
from PIL import Image, ImageDraw, ImageFilter

ap = argparse.ArgumentParser()
ap.add_argument('course_dir'); ap.add_argument('lesson_dir')
ap.add_argument('--workers', type=int, default=2)
ap.add_argument('--preview', type=float, default=0, help='only render the first N seconds (quick check)')
args = ap.parse_args()
C, L = pathlib.Path(args.course_dir).resolve(), pathlib.Path(args.lesson_dir).resolve()
R = L / 'render'
course = yaml.safe_load((C / 'course.yaml').read_text())
lesson = yaml.safe_load((L / 'lesson.yaml').read_text())
audio = json.loads((R / 'audio' / 'beats.json').read_text())
events = json.loads((R / 'app' / 'events.json').read_text()) if (R / 'app' / 'events.json').exists() else {'beats': {}}
# pane scenes (GitHub in the built-in browser, captured by scripts/pane.py) add their beats too
if (R / 'pane' / 'events.json').exists():
    events.setdefault('beats', {}).update(json.loads((R / 'pane' / 'events.json').read_text())['beats'])
FPS = course['video']['fps']; OW, OH = course['video']['width'], course['video']['height']
S = OW / 1920  # pixels per DIP
LEAD, TAIL, ACT0 = 0.35, 0.6, 0.25
XF_SCENE, XF_STEP, ZOOM_T = 0.5, 0.4, 0.7
FULL = (0.0, 0.0, 1920.0, 1080.0)
ZOOMS = {  # DIP rects, 16:9, about 1.6x
    'editor-code': (360, 75, 1200, 675), 'terminal': (356, 405, 1200, 675), 'bottom-panel': (705, 405, 1200, 675),
    'lineage-wide': (480, 405, 1200, 675), 'sql-results': (360, 300, 1360, 765),
    'git-panel': (0, 0, 960, 540),
    'explorer': (0, 40, 1280, 720), 'project-menu': (960, 0, 960, 540), 'model-menu': (1040, 20, 880, 495),
    'code-close': (372, 96, 800, 450), 'code-mid': (372, 100, 960, 540), 'terminal-close': (360, 562, 920, 518),
    'setup': (0, 20, 960, 540), 'statusbar': (1280, 720, 640, 360), 'home-header': (960, 0, 960, 540), 'center-wide': (320, 120, 1280, 720), 'gh-form': (300, 140, 1350, 760),
}

# ------------------------------------------------------------------ timeline
def ease(x):
    x = min(1.0, max(0.0, x)); return x * x * (3 - 2 * x)

scenes, beats_tl, t = [], [], 0.0
prev_zoom = FULL
for sc in lesson['scenes']:
    kind = sc['kind']
    scn = {'id': sc['id'], 'kind': kind, 'start': t, 'beats': []}
    if kind in ('title', 'closing'):
        d = course['video']['title_card_s' if kind == 'title' else 'closing_card_s']
        scn.update(img=str(R / 'slides' / f"{sc['slide']}-all.png"), dur=d)
        t += d; scenes.append(scn); prev_zoom = FULL; continue
    prev_zoom = FULL
    for b in sc['beats']:
        V = audio['beats'][b['id']]['dur']
        A = LEAD + V + TAIL
        bt = {'id': b['id'], 'scene': sc['id'], 'kind': kind, 'start': t, 'voice_start': t + LEAD, 'voice': V,
              'card': (str(R / 'cards' / f"{b['id']}.png") if b.get('card') else None), 'cues': audio['beats'][b['id']]['cues']}
        if kind == 'slide':
            bt.update(img=str(R / 'slides' / f"{sc['slide']}-{b.get('step')}.png"), dur=A)
        else:
            steps = events['beats'][b['id']]['steps']
            flex = [s for s in steps if s['k'] == 'type' and s['chars'] >= 40]
            # pass 1: fixed time
            def layout(type_dur):
                tau, img_changes, glides, presses, last_press = ACT0, [], [], [], None
                cur = None
                for s in steps:
                    k = s['k']
                    if k == 'still':
                        if s['dt'] > 0 and last_press is not None:
                            at = last_press + s['dt']; tau = max(tau, at)
                        else:
                            at = tau
                        img_changes.append((at, s['img']))
                    elif k == 'glide':
                        (x0, y0), (x1, y1) = s['from'], s['to']
                        g = min(0.75, max(0.32, 0.32 + math.hypot(x1 - x0, y1 - y0) / 2400))
                        glides.append((tau, tau + g, (x0, y0), (x1, y1))); tau += g
                    elif k == 'press':
                        tau += 0.08; presses.append((tau, tuple(s['at']))); last_press = tau; tau += 0.04
                    elif k == 'type':
                        n = len(s['imgs'])
                        dur = type_dur if s in flex else n / 14
                        for i, im in enumerate(s['imgs']):
                            img_changes.append((tau + (i + 1) * dur / max(1, n), im))
                        tau += dur
                    elif k == 'live':
                        ts = s['ts']; kf = min(1.0, max(2.5, A - ACT0 - 0.8) / max(0.01, ts[-1]))
                        for ti, im in zip(ts, s['imgs']):
                            img_changes.append((tau + ti * kf, im))
                        tau += ts[-1] * kf
                return tau, img_changes, glides, presses
            fixed_end, *_ = layout(0.0)
            tdur = 0.0
            if flex:
                n = sum(len(s['imgs']) for s in flex)
                tdur = min(n / 9, max(n / 30, A - fixed_end - 0.45))
            end, img_changes, glides, presses = layout(tdur)
            d = max(A, end + 0.45)
            z = ZOOMS[b['zoom']] if b.get('zoom') else FULL
            bt.update(dur=d, img_changes=sorted(img_changes, key=lambda x: x[0]), glides=glides, presses=presses,
                      zoom_from=prev_zoom, zoom_to=z, cursor_end=tuple(events['beats'][b['id']]['cursorEnd']))
            prev_zoom = z
        t += bt['dur']; scn['beats'].append(bt); beats_tl.append(bt)
    scn['dur'] = t - scn['start']; scenes.append(scn)
TOTAL = t
print(f'timeline {TOTAL:.1f}s, {len(beats_tl)} beats')

# carry app image + cursor across beats/scenes
app_img, cursor = None, tuple(events.get('initialCursor', (1180, 640)))
for bt in beats_tl:
    if bt['kind'] not in ('app', 'browser', 'pane'):
        continue
    # a glide starts where the cursor was on that surface (Studio or browser keep separate cursors)
    if bt['glides']:
        cursor = tuple(bt['glides'][0][2])
    bt['img0'], bt['cursor0'] = app_img, cursor
    if bt['img_changes']:
        app_img = bt['img_changes'][-1][1]
    cursor = bt['glides'][-1][3] if bt['glides'] else cursor
    if bt['img0'] is None and bt['img_changes']:
        bt['img0'] = bt['img_changes'][0][1]

# ------------------------------------------------------------------ state per frame
def r2(v, q=0.5):
    return round(v / q) * q

def app_state(bt, tl):
    img = bt['img0']
    for at, im in bt['img_changes']:
        if at <= tl: img = im
        else: break
    cx, cy = bt['cursor0']
    for g0, g1, p0, p1 in bt['glides']:
        if tl >= g1: cx, cy = p1
        elif tl >= g0:
            u = ease((tl - g0) / (g1 - g0))
            mx, my = (p0[0] + p1[0]) / 2 + (p1[1] - p0[1]) * 0.08, (p0[1] + p1[1]) / 2 - (p1[0] - p0[0]) * 0.08
            cx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * mx + u * u * p1[0]
            cy = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * my + u * u * p1[1]
            break
        else: break
    rip = None
    for pt, at in bt['presses']:
        if 0 <= tl - pt < 0.45: rip = (r2(at[0]), r2(at[1]), round((tl - pt) / 0.45, 2))
    zf, zt = bt['zoom_from'], bt['zoom_to']
    u = ease(tl / ZOOM_T) if zf != zt else 1.0
    z = tuple(r2(zf[i] + (zt[i] - zf[i]) * u) for i in range(4))
    card = None
    if bt['card']:
        a = min(ease((tl - 0.4) / 0.3), ease((bt['dur'] - 0.35 - tl) / 0.3))
        if a > 0: card = (bt['card'], round(a, 2))
    return ('app', img, z, (r2(cx), r2(cy)), rip, card)

def scene_at(t):
    for sc in scenes:
        if sc['start'] <= t < sc['start'] + sc['dur'] + 1e-9: return sc
    return scenes[-1]

def beat_at(sc, t):
    for bt in sc['beats']:
        if bt['start'] <= t < bt['start'] + bt['dur'] + 1e-9: return bt
    return sc['beats'][-1]

def raw_state(t):
    sc = scene_at(t)
    if sc['kind'] in ('title', 'closing'):
        return ('img', sc['img'])
    bt = beat_at(sc, t)
    if sc['kind'] == 'slide':
        i = sc['beats'].index(bt)
        if i > 0 and t - bt['start'] < XF_STEP and sc['beats'][i - 1]['img'] != bt['img']:
            return ('blend', ('img', sc['beats'][i - 1]['img']), ('img', bt['img']), round(ease((t - bt['start']) / XF_STEP), 2))
        return ('img', bt['img'])
    return app_state(bt, t - bt['start'])

def state(t):
    sc = scene_at(t)
    st = raw_state(t)
    k = scenes.index(sc)
    if k > 0 and t - sc['start'] < XF_SCENE:
        prev = raw_state(sc['start'] - 1e-6)
        st = ('blend', prev, st, round(ease((t - sc['start']) / XF_SCENE), 2))
    fade = 1.0
    if t < 0.5: fade = ease(t / 0.5)
    if TOTAL - t < 0.8: fade = min(fade, ease((TOTAL - t) / 0.8))
    return ('final', st, round(fade, 2))

# ------------------------------------------------------------------ rendering
@functools.lru_cache(maxsize=24)
def load(path):
    im = Image.open(path)
    im = im.convert('RGBA' if 'cards' in path else 'RGB')
    if im.size != (OW, OH): im = im.resize((OW, OH), Image.LANCZOS)
    return im

def cursor_sprite():
    s = int(14 * S)  # DIP 28 px tall at 2x
    pts = [(4, 2), (4, 22), (9.5, 16.8), (13.2, 25), (16.4, 23.6), (12.8, 15.6), (20, 15.6)]
    im = Image.new('RGBA', (int(34 * S), int(34 * S)), (0, 0, 0, 0))
    sh = Image.new('RGBA', im.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).polygon([((x + 1) * S, (y + 2) * S) for x, y in pts], fill=(0, 0, 0, 130))
    sh = sh.filter(ImageFilter.GaussianBlur(2.2 * S))
    d = ImageDraw.Draw(im)
    d.polygon([(x * S, y * S) for x, y in pts], fill=(255, 255, 255, 255), outline=(17, 17, 17, 255), width=int(1.6 * S))
    return Image.alpha_composite(sh, im)
CURSOR = None

def render(st):
    global CURSOR
    kind = st[0]
    if kind == 'img':
        return load(st[1])
    if kind == 'blend':
        a, b = render(st[1]).convert('RGB'), render(st[2]).convert('RGB')
        return Image.blend(a, b, st[3])
    if kind == 'final':
        im = render(st[1]).convert('RGB')
        if st[2] < 1: im = Image.blend(Image.new('RGB', im.size, (0, 0, 0)), im, st[2])
        return im
    # app
    _, img, z, cur, rip, card = st
    base = load(str(R / img) if '/' in img else str(R / 'app' / 'frames' / img))
    x, y, w, h = z
    if (float(x), float(y), float(w), float(h)) != FULL:
        base = base.crop((int(x * S), int(y * S), int((x + w) * S), int((y + h) * S))).resize((OW, OH), Image.BICUBIC)
    im = base.convert('RGBA')
    def tx(px, py): return ((px - x) / w * OW, (py - y) / h * OH)
    if rip:
        rx, ry = tx(rip[0], rip[1]); ph = rip[2]
        r = (10 + 26 * ph) * S; a = int(240 * (1 - ph))
        ov = Image.new('RGBA', im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
        d.ellipse((rx - r, ry - r, rx + r, ry + r), outline=(249, 115, 22, a), width=int(3 * S), fill=(249, 115, 22, a // 5))
        im = Image.alpha_composite(im, ov)
    if card:
        c = load(card[0])
        if card[1] < 1:
            c = c.copy(); c.putalpha(c.getchannel('A').point(lambda v, k=card[1]: int(v * k)))
        im = Image.alpha_composite(im, c)
    if cur:
        if CURSOR is None: CURSOR = cursor_sprite()
        px, py = tx(cur[0], cur[1])
        if -40 < px < OW + 40 and -40 < py < OH + 40:
            im.alpha_composite(CURSOR, (int(px - 3 * S), int(py - 2 * S)))
    return im

OUTDIR = R / 'composite'

# Cached composites are keyed by state; the salt changes whenever a slide or card image is re-rendered,
# so a changed card (same path, new content) never reuses an old composite.
SALT = hashlib.sha1(''.join(f"{p.name}{p.stat().st_mtime_ns}" for d in ('slides', 'cards') if (R / d).exists()
                            for p in sorted((R / d).iterdir())).encode()).hexdigest()[:8]

def key_name(st):
    return hashlib.sha1((json.dumps(st) + SALT).encode()).hexdigest()[:16] + '.jpg'

def render_to_file(st):
    p = OUTDIR / key_name(st)
    if not p.exists():
        render(st).convert('RGB').save(p, quality=94, subsampling=0)
    return p.name

if __name__ == '__main__':
    OUTDIR.mkdir(parents=True, exist_ok=True)
    end = min(TOTAL, args.preview) if args.preview else TOTAL
    nfr = int(round(end * FPS))
    runs = []
    for i in range(nfr):
        st = state((i + 0.5) / FPS)
        if runs and runs[-1][0] == st: runs[-1][1] += 1
        else: runs.append([st, 1])
    uniq = list(dict.fromkeys(json.dumps(s) for s, _ in runs))
    print(f'{nfr} frames, {len(runs)} runs, {len(uniq)} unique states', flush=True)
    with Pool(args.workers) as pool:
        for k, _ in enumerate(pool.imap(render_to_file, [json.loads(u) for u in uniq], chunksize=4)):
            if k % 100 == 0: print(f'  composite {k}/{len(uniq)}', flush=True)
    lines = []
    for st, n in runs:
        lines += [f"file '{OUTDIR / key_name(json.loads(json.dumps(st)))}'", f'duration {n / FPS:.6f}']
    lines.append(lines[-2])
    (R / 'frames.txt').write_text('\n'.join(lines) + '\n')

    # narration track
    SR = audio['sr']
    track = np.zeros(int((end + 1) * SR), dtype=np.float32)
    for bt in beats_tl:
        a, _ = sf.read(R / 'audio' / f"{bt['id']}.wav", dtype='float32')
        o = int(bt['voice_start'] * SR)
        if o >= len(track): continue
        a = a[: len(track) - o]; track[o:o + len(a)] += a
    track = track[: int(end * SR)]
    peak = float(np.abs(track).max() or 1); track = track / peak * 0.89
    sf.write(R / 'narration.wav', track, SR)

    # captions (written form) and timeline
    def ts(s, sep):
        return f"{int(s // 3600):02d}:{int(s % 3600 // 60):02d}:{int(s % 60):02d}{sep}{int(round(s * 1000)) % 1000:03d}"
    srt, vtt, n = [], ['WEBVTT', ''], 1
    for bt in beats_tl:
        for c in bt['cues']:
            a0, a1 = bt['voice_start'] + c['t0'], bt['voice_start'] + c['t1']
            if a0 >= end: continue
            srt.append(f"{n}\n{ts(a0, ',')} --> {ts(a1, ',')}\n{c['text']}\n"); vtt.append(f"{ts(a0, '.')} --> {ts(a1, '.')}\n{c['text']}\n"); n += 1
    name = lesson['id']
    (L / f'{name}.srt').write_text('\n'.join(srt)); (L / f'{name}.vtt').write_text('\n'.join(vtt))
    tl = {'total': round(TOTAL, 2), 'fps': FPS, 'size': [OW, OH],
          'scenes': [{'id': s['id'], 'kind': s['kind'], 'start': round(s['start'], 2), 'dur': round(s['dur'], 2)} for s in scenes],
          'beats': [{'id': b['id'], 'scene': b['scene'], 'start': round(b['start'], 2), 'dur': round(b['dur'], 2),
                     'voice_start': round(b['voice_start'], 2), 'voice': b['voice']} for b in beats_tl]}
    (L / 'timeline.json').write_text(json.dumps(tl, indent=1))

    out = L / (f'{name}.mp4' if not args.preview else f'{name}-preview.mp4')
    tmp = out.with_name(out.stem + '.part.mp4')
    v = course['video']
    cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', str(R / 'frames.txt'), '-i', str(R / 'narration.wav'),
           '-vf', f'fps={FPS},format=yuv420p', '-af', 'loudnorm=I=-16:TP=-1.5:LRA=11', '-c:v', 'libx264', '-preset', 'veryfast',
           '-crf', str(v['crf']), '-tune', 'stillimage', '-profile:v', 'high', '-level', '5.1', '-g', str(FPS * 2),
           '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709',
           '-c:a', 'aac', '-b:a', '384k', '-ar', '48000', '-t', f'{end:.3f}', '-movflags', '+faststart', str(tmp)]
    subprocess.run(cmd, check=True)
    tmp.rename(out)
    print('wrote', out, f'{end:.1f}s')
