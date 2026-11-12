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
# YouTube drops all chapters if any is shorter than 10 s: merge short ones into the previous chapter
def _merge(ch):
    out = []
    for i, (t0, n) in enumerate(ch):
        t1 = ch[i + 1][0] if i + 1 < len(ch) else tl['total']
        if out and t1 - t0 < 10: continue
        out.append([t0, n])
    if len(out) > 1 and tl['total'] - out[-1][0] < 10: out.pop()
    return out
chapters = _merge(chapters)
# the app name is added only when the course title does not already carry it; YouTube titles stop at 100 characters
title = lesson.get('youtube_title') or (f"{lesson['title']} | {course['title']} {lesson['number']}" + ('' if 'Rosetta DBT Studio' in course['title'] else ' | Rosetta DBT Studio'))
assert len(title) <= 100, f'YouTube title too long ({len(title)}): {title}'
desc = [lesson.get('summary', ''), '',
        f"Part of the free {course['title']} course on Rosetta Academy: {course['academy']}", '',
        ] + ((['Chapters'] + [f"{fmt(t)} {n}" for t, n in chapters] + ['']) if len(chapters) >= 3 else []) + [
        (f"Recorded in Rosetta DBT Studio {course['app']['version']} with dbt Core {course['runtime']['dbt_core']} "
         f"and dbt-duckdb {course['runtime']['dbt_duckdb']}." if any(sc['kind'] == 'app' for sc in lesson['scenes'])
         else f"Screens from Rosetta DBT Studio {course['app']['version']}."),
        'Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html',
        'Source code: https://github.com/rosettadb/dbt-studio'] + ([course['credit_line']] if course.get('credit_line') else [])
if course.get('code_repo'):
    desc += ['', f"Code for this course (one commit per lesson): {course['code_repo']}"]
if lesson.get('links'):
    desc += ['', 'Links for this lesson'] + [f"- {h['title']}: {h['url']}" for h in lesson['links']]
help_links = lesson.get('help_links', course.get('help_links') if lesson.get('show_help_links') else None) or []
if help_links:
    desc += ['', course.get('help_links_title', 'Useful links')] + [f"- {h['title']}: {h['url']}" for h in help_links]
tags = list(dict.fromkeys(lesson.get('tags', []) + course.get('youtube', {}).get('tags', [])))
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
        ev = json.loads((R / 'app' / 'events.json').read_text())['beats'] if (R / 'app' / 'events.json').exists() else {}
        if (R / 'pane' / 'events.json').exists():
            ev.update(json.loads((R / 'pane' / 'events.json').read_text())['beats'])
        last = [s for b in sc['beats'] for s in ev[b['id']]['steps'] if s['k'] in ('still', 'type', 'live')][-1]
        img = last.get('img') or last['imgs'][-1]
        add((R / img) if '/' in img else (R / 'app' / 'frames' / img), 'APP DEMO (record in Rosetta DBT Studio, see RECORDING-cue-sheet.md):\n' + '\n'.join(b['say'] for b in sc['beats']))
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
        'new_folder': lambda: f"Right-click `{v['parent']}` → **New Folder**, type `{v['name']}`, click **Save**",
        'type_end': lambda: 'Click at the end of the file and type:<br><br>```yaml\n' + (v or '').rstrip('\n') + '\n```',
        'nav': lambda: f"In the left bar, click **{v}**",
        'sql_connection': lambda: f"Open the connection list (top left) and pick **{v}**",
        'sql_run': lambda: "Click the green ▶ arrow next to line 1",
        'lineage_maximize': lambda: "Click **Maximize** (top right of the lineage panel)",
        'lineage_fit': lambda: "Click the fit-view button (bottom left of the graph)",
        'point_tree': lambda: f"Point at `{v}` in the Explorer",
        'lineage_depth': lambda: f"In the lineage panel, set **Depth** to {v}",
        'expect_file': lambda: f"(Check that `{v['path']}` matches `{v['snippet']}`)",
        'terminal': lambda: f"Click the command box under the terminal, type `{v['cmd']}`, press Enter",
        'git_tab': lambda: "Click the **Git** tab at the top of the sidebar",
        'explorer_tab': lambda: "Click the **Explorer** tab at the top of the sidebar",
        'git_stage': lambda: f"Hover `{v}` in Changes and click its **+** (Stage Changes)",
        'git_message': lambda: f"Click the message box and type: {v}",
        'git_commit': lambda: "Click **Commit**",
        'type_text': lambda: f"Click **{v.get('label') or v.get('name')}** and type `{v['text']}`",
        'pause': lambda: f"Wait {v/1000:.1f} s",
        'press_keys': lambda: f"Press {v}",
        'type_keys': lambda: f"Type `{v}`",
        'new_root_file': lambda: f"Right-click the project root → **New File** → `{v}` → **Save**",
        'wait_text': lambda: f"Wait for “{v['text']}”",
        'git_init': lambda: "Click **Initialize Repository**",
        'git_stage_all': lambda: "Hover CHANGES and click **+** (Stage All Changes)",
        'publish_branch': lambda: f"Click **Publish Branch**, paste `{v['url']}`, add the remote",
        'point_tree': lambda: f"Point at `{v}` in the Explorer",
        'web': lambda: f"GitHub (built-in browser): {v}",
        'click_at': lambda: f"Click **{v.get('label') or v.get('name') or v.get('text') or v}**" if isinstance(v, dict) else f"Click **{v}**",
        'point_at': lambda: f"Point at **{v.get('label') or v.get('name') or v.get('text') or v}**" if isinstance(v, dict) else f"Point at **{v}**",
        'check': lambda: f"Check {', '.join(v) if isinstance(v, list) else v}",
        'uncheck': lambda: f"Uncheck {', '.join(v) if isinstance(v, list) else v}",
        'wait_enabled': lambda: f"Wait until **{v['name']}** is enabled (this takes a while)",
        'follow_window': lambda: "Studio opens its main window",
        'goto': lambda: f"In the browser, open {v}",
        'scroll_to': lambda: f"Scroll to **{v.get('label') or v.get('text') or v.get('selector')}**",
        'click_download': lambda: f"Click the download link **{v.get('label') or v.get('text') or v.get('selector')}**",
    }
    return table[k]() if k in table else f"{k}: {v}"
app_scenes = [sc for sc in lesson['scenes'] if sc['kind'] in ('app', 'browser', 'pane')]
cue = [f"# {lesson['title']} — recording cue sheet", '']
if not app_scenes:
    cue += ['This lesson has no app scenes, so there is nothing to record. A human voice-over only needs `voiceover-script.md`.', '']
else:
    cue += [f"For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio {course['app']['version']}, {course['theme']} theme, window 1920x1080.", '',
            '## Before you start', ''] + [f"- {n}" for n in lesson.get('start_notes', [])] + ['']
for sc in lesson['scenes']:
    if sc['kind'] not in ('app', 'browser', 'pane'):
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
rel = f"../{C.name}/{L.name}"
rd = [f"# Lesson {lesson['number']} · {lesson['title']}", '',
      f"{course['title']} · {lesson['module']}. Rendered {fmt(tl['total'])}, 3840x2160 H.264 + AAC, {size_mb:.0f} MB.", '',
      '## Files', '', '| File | What it is |', '|---|---|',
      f"| `lesson.yaml` | **The source.** Edit this, then re-render |",
      f"| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |",
      f"| `{lid}.mp4` | The 4K video for YouTube (not in git) |",
      f"| `{lid}-1080p.mp4` | 1080p copy for phones and sharing (not in git) |",
      f"| `{lid}.srt`, `{lid}.vtt` | Captions, one cue per sentence |",
      '| `voiceover-script.md` | Beat sheet with measured start times |',
      '| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |',
      '| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |',
      f"| `{lid}-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |",
      '| `youtube.md`, `thumbnail.png` | Upload package |', '| `timeline.json` | Start and length of every scene and beat |',
      '| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |', '',
      '## Versions', '', f"Rosetta DBT Studio {course['app']['version']} (official release), dbt-core {course['runtime']['dbt_core']}, "
      f"dbt-duckdb {course['runtime']['dbt_duckdb']}, Python {course['runtime']['python']}. Voice: Kokoro `{course['voice']['voice']}` at {course['voice']['speed']}.", '',
      '## Changes from the draft', ''] + [f"- {x}" for x in lesson.get('draft_changes', ['None.'])] + ['',
      '## Accuracy notes', ''] + [f"- {x}" for x in lesson.get('accuracy_notes', [])] + [
      '- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).', '',
      '## Re-render', '', '```sh', 'cd ../../_academy-video-tooling'] + (
      [f'NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../{C.name} {rel}'] if app_scenes else []) + [
      f'python3 scripts/tts.py ../{C.name} {rel}     # --human to use voice-human/<beat>.wav',
      f'python3 scripts/render_stills.py ../{C.name} {rel}',
      f'python3 scripts/compose.py ../{C.name} {rel}',
      f'python3 scripts/package.py ../{C.name} {rel}', '```', '',
      'Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.', '']
(L / 'readme.md').write_text('\n'.join(rd))
# 1080p copy for phones and sharing (many phones cannot decode 4K H.264 level 5.1; YouTube gets the 4K file)
src, prev = L / f'{lid}.mp4', L / f'{lid}-1080p.mp4'
if not prev.exists() or prev.stat().st_mtime < src.stat().st_mtime:
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(src), '-vf', 'scale=1920:1080:flags=lanczos,format=yuv420p',
                    '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-profile:v', 'high', '-level', '4.0',
                    '-c:a', 'aac', '-b:a', '160k', '-ac', '2', '-ar', '48000', '-movflags', '+faststart', str(prev)], check=True)
subprocess.run([sys.executable, str(pathlib.Path(__file__).parent / 'script_from_lesson.py'), str(L), '--timeline', str(L / 'timeline.json')], check=True)
print('packaged', lid)
