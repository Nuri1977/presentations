"""Package a rendered lesson: YouTube text, PowerPoint export, human cue sheet, readme, timed beat sheet.

    python3 scripts/package.py <course_dir> <lesson_dir>

Needs timeline.json (from compose.py) and the rendered slide stills.
"""
import json, pathlib, re, subprocess, sys
import yaml
from PIL import Image

C, L = map(lambda p: pathlib.Path(p).resolve(), sys.argv[1:3])
course = yaml.safe_load((C / 'course.yaml').read_text())
lesson = yaml.safe_load((L / 'lesson.yaml').read_text())
tl = json.loads((L / 'timeline.json').read_text())
R = L / 'render'
lid = lesson['id']
fmt = lambda s: f"{int(s // 60)}:{int(s % 60):02d}"
scene_start = {s['id']: s['start'] for s in tl['scenes']}

# ---------------------------------------------------------------- youtube.md
chapters = []
for sc in lesson['scenes']:
    if sc.get('chapter'):
        chapters.append([scene_start[sc['id']], sc['chapter']])
chapters[0][0] = 0.0  # YouTube needs the first chapter at 0:00
num = re.search(r'(\d+)-(\d+)', lid)
title = f"{lesson['title']} | {course['title']} {num.group(1)}.{num.group(2)} | Rosetta DBT Studio"
desc = [lesson.get('summary', ''), '',
        f"Part of the free {course['title']} course on Rosetta Academy: {course['academy']}", '',
        'Chapters'] + [f"{fmt(t)} {n}" for t, n in chapters] + ['',
        f"Recorded in Rosetta DBT Studio {course['app']['version']} with dbt Core {course['runtime']['dbt_core']} "
        f"and dbt-duckdb {course['runtime']['dbt_duckdb']}.",
        'Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html',
        'Source code: https://github.com/rosettadb/dbt-studio']
tags = ['dbt', 'dbt core', 'dbt models', 'ref', 'DAG', 'data lineage', 'analytics engineering', 'ELT', 'DuckDB', 'Rosetta DBT Studio', 'SQL']
yt = [f"# YouTube upload: {lesson['title']}", '',
      f"- **File:** `{lid}.mp4` (3840x2160, {fmt(tl['total'])}). Upload the 4K file; YouTube shows HD and 4K only after processing finishes, which can take from minutes to an hour, so the first view may look blurry.",
      f"- **Visibility:** {course['youtube']['visibility']} (embedded only in Academy)",
      f"- **Captions:** upload `{lid}.srt` (English)", f"- **Thumbnail:** `thumbnail.png` (1280x720)",
      '- **End screen / cards:** none', '', '## Title', '', title, '', '## Description', '', '\n'.join(desc), '',
      '## Tags', '', ', '.join(tags), '']
(L / 'youtube.md').write_text('\n'.join(yt))

# ---------------------------------------------------------------- pptx (image per slide state + notes)
from pptx import Presentation
from pptx.util import Emu
prs = Presentation(); prs.slide_width, prs.slide_height = Emu(12192000), Emu(6858000)
blank = prs.slide_layouts[6]
tmp = R / 'pptx'; tmp.mkdir(exist_ok=True)
def add(img, notes):
    jp = tmp / (pathlib.Path(img).stem + '.jpg')
    Image.open(img).convert('RGB').resize((1920, 1080), Image.LANCZOS).save(jp, quality=90)
    s = prs.slides.add_slide(blank)
    s.shapes.add_picture(str(jp), 0, 0, prs.slide_width, prs.slide_height)
    s.notes_slide.notes_text_frame.text = notes
for sc in lesson['scenes']:
    if sc['kind'] in ('title', 'closing'):
        add(R / 'slides' / f"{sc['slide']}-all.png", sc.get('show', ''))
    elif sc['kind'] == 'slide':
        for b in sc['beats']:
            add(R / 'slides' / f"{sc['slide']}-{b['step']}.png", b['say'])
    else:  # app scene: one frame from the recording, with its narration, so the deck still tells the whole lesson
        mid = next(b for b in tl['beats'] if b['scene'] == sc['id'])
        ev = json.loads((R / 'app' / 'events.json').read_text())['beats']
        last = [s for b in sc['beats'] for s in ev[b['id']]['steps'] if s['k'] in ('still', 'type', 'live')][-1]
        img = last.get('img') or last['imgs'][-1]
        add(R / 'app' / 'frames' / img, 'APP DEMO (record in Rosetta DBT Studio, see RECORDING-cue-sheet.md):\n' + '\n'.join(b['say'] for b in sc['beats']))
prs.save(L / f'{lid}-slides.pptx')

# ---------------------------------------------------------------- human cue sheet
def act(a):
    k, v = (a, None) if isinstance(a, str) else next(iter(a.items()))
    table = {
        'open_project': lambda: f"On the home screen, click **{v}** under Recent Projects",
        'open_file': lambda: f"In the Explorer, open `{v}` (expand each folder on the way)",
        'new_file': lambda: f"Right-click `{v['folder'] if v else ''}` → **New File**, type `{v['name'] if v else ''}`, click **Save**",
        'type': lambda: 'Type:\n\n```sql\n' + (v or '').rstrip('\n') + '\n```',
        'click_save': lambda: 'Click **Save** (top right of the editor)',
        'project_menu': lambda: f"Open the **Project** menu (arrow next to Project, top right) → **{v}**",
        'wait_for': lambda: 'Wait for the terminal to finish and the green "dbt compile completed successfully" toast',
        'point': lambda: f"Point at line {v['editor_line']}" if isinstance(v, dict) else f"Point at {v}",
        'close_tab': lambda: f"Close the editor tab for `{v}` (its ×)",
        'bottom_tab': lambda: f"Click the **{v}** tab in the bottom panel (it appears after the compile, once the model file is active)",
        'lineage_depth': lambda: f"In the lineage panel, set **Depth** to {v}",
    }
    return table[k]() if k in table else f"{k}: {v}"
cue = [f"# {lesson['title']} — recording cue sheet", '',
       f"For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio {course['app']['version']}, dark theme, window 1920x1080.", '',
       '## Before you start', '',
       f"- Start state `{lesson['start_state']}`: project `dbt_course` with the Lab 1 data in `course.duckdb`, `models/staging` holding `_sources.yml` and the three staging models, and an empty `models/marts`.",
       '- No `target/` or `logs/` folders yet, so the compile in s04 creates them on camera.',
       '- Close every editor tab and start on the home screen (Workspace Overview).',
       '- Bottom panel open on TERMINAL.', '']
for sc in lesson['scenes']:
    if sc['kind'] != 'app':
        continue
    cue += [f"## {sc['id']} · {sc.get('chapter', '')}", '', '| Listen for | Do this |', '|---|---|']
    for b in sc['beats']:
        listen = ' '.join(b['say'].split()[:8]) + '…'
        dos = '<br>'.join(act(a).replace('\n', '<br>') for a in b.get('actions', [])) or 'Hold; nothing moves'
        cue.append(f"| \"{listen}\" | {dos} |")
    cue.append('')
(L / 'RECORDING-cue-sheet.md').write_text('\n'.join(cue))

# ---------------------------------------------------------------- readme
ff = json.loads(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration,size:stream=codec_name,width,height', '-of', 'json', str(L / f'{lid}.mp4')], capture_output=True, text=True).stdout)
size_mb = int(ff['format']['size']) / 1e6
rd = [f"# Lesson 3.2 · {lesson['title']}", '',
      f"{course['title']} · {lesson['module']}. Rendered {fmt(tl['total'])}, 3840x2160 H.264 + AAC, {size_mb:.0f} MB.", '',
      '## Files', '', '| File | What it is |', '|---|---|',
      f"| `lesson.yaml` | **The source.** Edit this, then re-render |",
      f"| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |",
      f"| `{lid}.mp4` | The video (not in git) |",
      f"| `{lid}.srt`, `{lid}.vtt` | Captions, one cue per sentence |",
      '| `voiceover-script.md` | Beat sheet with measured start times |',
      '| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |',
      '| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |',
      f"| `{lid}-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |",
      '| `youtube.md`, `thumbnail.png` | Upload package |', '| `timeline.json` | Start and length of every scene and beat |',
      '| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |', '',
      '## Versions', '', f"Rosetta DBT Studio {course['app']['version']} (official Linux release), dbt-core {course['runtime']['dbt_core']}, "
      f"dbt-duckdb {course['runtime']['dbt_duckdb']}, Python {course['runtime']['python']}. Voice: Kokoro `{course['voice']['voice']}` at {course['voice']['speed']}.", '',
      '## Changes from the draft', '',
      '- The draft\'s spoken lines are kept. Demo lines were added for the app scenes (opening stg_orders, writing fct_orders, Compile, the compiled copy, Lineage).',
      '- b06 mentions source() and defers it to Lesson 3.3.', '- b22 adds what "directed" and "acyclic" mean (matches the lesson\'s quiz answer).',
      '- The draft cue "lineage graph appears as models are added" is shown with Studio\'s LINEAGE tab at depth 1 and 2 rather than a growing diagram; the DAG slide builds the graph instead.', '',
      '## Accuracy notes', '',
      '- `ref(\'stg_orders\')` compiling to `"course"."main"."stg_orders"` is the real compiled output (target/compiled).',
      '- The `prod` line on the ref slide is an illustrative example and is marked as one.',
      '- Lineage at depth 2 showing the sources `orders` and `payments` was verified in this recording.',
      '- Listen once for pronunciation: dbt is read as "D B T", SQL as "sequel", DAG as "dag".', '',
      '## Re-render', '', '```sh', 'cd ../../_academy-video-tooling',
      'NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../dbt-Fundamentals-Course ../dbt-Fundamentals-Course/lesson-3-2-models-ref-dag',
      'python3 scripts/tts.py ../dbt-Fundamentals-Course ../dbt-Fundamentals-Course/lesson-3-2-models-ref-dag     # --human to use voice-human/<beat>.wav',
      'python3 scripts/render_stills.py ../dbt-Fundamentals-Course ../dbt-Fundamentals-Course/lesson-3-2-models-ref-dag',
      'python3 scripts/compose.py ../dbt-Fundamentals-Course ../dbt-Fundamentals-Course/lesson-3-2-models-ref-dag',
      'python3 scripts/package.py ../dbt-Fundamentals-Course ../dbt-Fundamentals-Course/lesson-3-2-models-ref-dag', '```', '',
      'Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.', '']
(L / 'readme.md').write_text('\n'.join(rd))
subprocess.run([sys.executable, str(pathlib.Path(__file__).parent / 'script_from_lesson.py'), str(L), '--timeline', str(L / 'timeline.json')], check=True)
print('packaged', lid)
