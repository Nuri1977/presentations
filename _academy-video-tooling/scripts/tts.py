"""Voice every beat of a lesson with Kokoro, locally.

    python3 scripts/tts.py <course_dir> <lesson_dir>

Writes <lesson_dir>/render/audio/<beat>.wav, render/audio/beats.json (duration + sentence cues per beat)
and <lesson_dir>/voiceover-kokoro.txt (the exact spoken forms). Human voice: put <beat>.wav files in
<lesson_dir>/voice-human/ and run with --human to measure those instead of generating.
"""
import argparse, json, pathlib, re, sys
import numpy as np, soundfile as sf, yaml

HERE = pathlib.Path(__file__).resolve().parent.parent
SR = 24000
GAP = 0.28

ap = argparse.ArgumentParser()
ap.add_argument('course_dir'); ap.add_argument('lesson_dir'); ap.add_argument('--human', action='store_true')
a = ap.parse_args()
C, L = pathlib.Path(a.course_dir), pathlib.Path(a.lesson_dir)
course = yaml.safe_load((C / 'course.yaml').read_text())
lesson = yaml.safe_load((L / 'lesson.yaml').read_text())
out = L / 'render' / 'audio'; out.mkdir(parents=True, exist_ok=True)
rules = [(re.compile(p), r) for p, r in course.get('pronunciation', [])]


def spoken(t):
    for p, r in rules:
        t = p.sub(r, t)
    return re.sub(r'\s+', ' ', t.replace('’', "'")).strip()


def sentences(t):
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+(?=[A-Z0-9"])', t) if s.strip()]


beats = [b for sc in lesson['scenes'] for b in sc.get('beats', [])]
meta, kokoro_txt = {}, []
k = None
if not a.human:
    from kokoro_onnx import Kokoro
    k = Kokoro(str(HERE / '.cache/tts/kokoro-v1.0.onnx'), str(HERE / '.cache/tts/voices-v1.0.bin'))
v = course['voice']
for b in beats:
    if a.human:
        f = L / 'voice-human' / f"{b['id']}.wav"
        audio, sr = sf.read(f, dtype='float32')
        if audio.ndim > 1: audio = audio.mean(axis=1)
        if sr != SR:
            idx = np.linspace(0, len(audio) - 1, int(len(audio) * SR / sr)); audio = np.interp(idx, np.arange(len(audio)), audio).astype(np.float32)
        sents = sentences(b['say'])
        dur = len(audio) / SR; per = dur / max(1, sum(len(s) for s in sents)); t = 0; cues = []
        for s in sents:  # approximate cue split by characters for a human take
            cues.append({'t0': round(t, 3), 't1': round(t + len(s) * per, 3), 'text': s}); t += len(s) * per
    else:
        parts, cues, t = [], [], 0.0
        for s in sentences(b['say']):
            sp = spoken(s)
            kokoro_txt.append(f"{b['id']}\t{sp}")
            au, _ = k.create(sp, voice=v['voice'], speed=v['speed'], lang='en-us')
            au = np.asarray(au, dtype=np.float32)
            # trim leading/trailing near-silence so beats line up tightly
            nz = np.where(np.abs(au) > 0.004)[0]
            if len(nz): au = au[max(0, nz[0] - 240): min(len(au), nz[-1] + 1200)]
            parts += [au, np.zeros(int(GAP * SR), dtype=np.float32)]
            cues.append({'t0': round(t, 3), 't1': round(t + len(au) / SR, 3), 'text': s}); t += len(au) / SR + GAP
        audio = np.concatenate(parts[:-1])
    sf.write(out / f"{b['id']}.wav", audio, SR)
    meta[b['id']] = {'dur': round(len(audio) / SR, 3), 'cues': cues}
    print(f"{b['id']:5s} {len(audio) / SR:5.1f}s  {b['say'][:70]}", flush=True)
(out / 'beats.json').write_text(json.dumps({'sr': SR, 'voice': v, 'human': a.human, 'beats': meta}, indent=1))
if kokoro_txt:
    (L / 'voiceover-kokoro.txt').write_text('# Spoken forms sent to Kokoro (beat<TAB>text). Generated from lesson.yaml + course.yaml pronunciation.\n' + '\n'.join(kokoro_txt) + '\n')
print('total voice', round(sum(m['dur'] for m in meta.values()), 1), 's')
