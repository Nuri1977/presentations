"""Record 'pane' scenes: the GitHub website in the Claude desktop app's built-in browser (signed in as Nuri).

Claude drives the browser with its browser tools and calls this script between actions to capture the
visible pane with macOS `screencapture` and to log the same events record.cjs writes (still, glide, press,
type, live). compose.py merges render/pane/events.json with render/app/events.json.

    python3 scripts/pane.py <lesson_dir> init --rect X,Y,W,H     # pane rect on screen, in points (find it with a probe)
    python3 scripts/pane.py <lesson_dir> beat b05                # following events belong to beat b05
    python3 scripts/pane.py <lesson_dir> snap [--dt 0.4]         # one still
    python3 scripts/pane.py <lesson_dir> glide X Y [label]       # cursor glide to page coords (1920x1080 CSS px)
    python3 scripts/pane.py <lesson_dir> press X Y [label]       # click ripple at page coords
    python3 scripts/pane.py <lesson_dir> typesnap                # a still that is part of a typing run
    python3 scripts/pane.py <lesson_dir> typeend <chars> [label] # close the typing run
    python3 scripts/pane.py <lesson_dir> live --n 6 --every 0.8  # a short live clip (page loading)
    python3 scripts/pane.py <lesson_dir> done                    # write render/pane/events.json

Needs Screen Recording permission for Claude. The pane must stay visible and uncovered while recording.
"""
import json, pathlib, subprocess, sys, tempfile, time
from PIL import Image

L = pathlib.Path(sys.argv[1]).resolve()
cmd = sys.argv[2]
args = sys.argv[3:]
P = L / 'render' / 'pane'
STATE = P / 'state.json'


def load():
    return json.loads(STATE.read_text())


def save(s):
    STATE.write_text(json.dumps(s, indent=1))


def capture(s):
    x, y, w, h = s['rect']
    with tempfile.TemporaryDirectory() as d:
        tmp = pathlib.Path(d) / 'cap.png'
        subprocess.run(['screencapture', '-x', '-R', f'{x},{y},{w},{h}', '-t', 'png', str(tmp)], check=True)
        im = Image.open(tmp).convert('RGB')
    name = f"p{s['n']:05d}.jpg"
    s['n'] += 1
    im.save(P / 'frames' / name, quality=95, subsampling=0)
    return f'pane/frames/{name}'


def ev(s, e):
    s['beats'].setdefault(s['beat'], {'steps': [], 'cursorEnd': s['cursor']})
    s['beats'][s['beat']]['steps'].append(e)
    s['beats'][s['beat']]['cursorEnd'] = s['cursor']
    with open(P / 'events.jsonl', 'a') as f:
        f.write(json.dumps({'beat': s['beat'], 't': time.time(), **e}) + '\n')


if cmd == 'init':
    rect = [int(v) for v in args[args.index('--rect') + 1].split(',')]
    if P.exists():
        subprocess.run(['rm', '-rf', str(P)], check=True)
    (P / 'frames').mkdir(parents=True)
    save({'rect': rect, 'n': 0, 'cursor': [960, 300], 'beat': None, 'beats': {}, 'typing': []})
    print('pane init', rect)
    sys.exit(0)

s = load()
if cmd == 'beat':
    s['beat'] = args[0]
elif cmd == 'snap':
    dt = float(args[args.index('--dt') + 1]) if '--dt' in args else 0
    ev(s, {'k': 'still', 'img': capture(s), 'dt': dt})
elif cmd == 'glide':
    x, y = float(args[0]), float(args[1])
    ev(s, {'k': 'glide', 'from': s['cursor'], 'to': [x, y], 'label': ' '.join(args[2:])})
    s['cursor'] = [x, y]
elif cmd == 'press':
    x, y = float(args[0]), float(args[1])
    ev(s, {'k': 'press', 'at': [x, y], 'button': 'left', 'label': ' '.join(args[2:])})
elif cmd == 'typesnap':
    s['typing'].append(capture(s))
elif cmd == 'typeend':
    ev(s, {'k': 'type', 'imgs': s['typing'], 'chars': int(args[0]), 'label': ' '.join(args[1:])})
    s['typing'] = []
elif cmd == 'live':
    n = int(args[args.index('--n') + 1]) if '--n' in args else 6
    every = float(args[args.index('--every') + 1]) if '--every' in args else 0.8
    imgs, ts, t0 = [], [], time.time()
    for i in range(n):
        imgs.append(capture(s)); ts.append(round(time.time() - t0, 2))
        if i < n - 1:
            time.sleep(every)
    ev(s, {'k': 'live', 'imgs': imgs, 'ts': ts, 'label': 'pane live'})
elif cmd == 'done':
    (P / 'events.json').write_text(json.dumps({'size': [1920, 1080], 'source': 'pane', 'rect': s['rect'],
                                               'beats': s['beats'], 'frames': s['n']}, indent=1))
    print('pane events', len(s['beats']), 'beats,', s['n'], 'frames')
else:
    sys.exit('unknown command ' + cmd)
save(s)
