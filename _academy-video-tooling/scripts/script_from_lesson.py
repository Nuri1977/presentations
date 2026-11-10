"""Generate the human-readable beat sheet / voice-over script from lesson.yaml.

    python3 scripts/script_from_lesson.py <lesson_dir> [--course <course.yaml>] [--timeline timeline.json]

Writes <lesson_dir>/voiceover-script.md. Before rendering, durations are estimates at 150 wpm;
after rendering, pass --timeline to print the measured start time of every beat.
"""
import argparse, json, pathlib, re
import yaml

ap = argparse.ArgumentParser()
ap.add_argument('lesson_dir')
ap.add_argument('--course')
ap.add_argument('--timeline')
a = ap.parse_args()
L = pathlib.Path(a.lesson_dir)
lesson = yaml.safe_load((L / 'lesson.yaml').read_text())
course = yaml.safe_load(pathlib.Path(a.course or L.parent / 'course.yaml').read_text())
tl = json.loads(pathlib.Path(a.timeline).read_text()) if a.timeline else None
starts = {b['id']: b['start'] for b in tl['beats']} if tl else {}
measured = {b['id']: b['dur'] for b in tl['beats']} if tl else {}

WPM = 150
TYPE_CPS = 18  # recorded typing speed used for estimates


def words(s):
    return len(re.findall(r"[A-Za-z0-9']+", s))


def fmt(t):
    return f"{int(t // 60)}:{int(t % 60):02d}"


def describe(act):
    (k, v), = act.items() if isinstance(act, dict) else ((act, None),)
    return {
        'open_project': lambda: f"Open project **{v}** from Recent Projects",
        'open_file': lambda: f"Open `{v}` in the Explorer",
        'new_file': lambda: f"Right-click `{v['folder']}` → **New File** → `{v['name']}` → **Save**",
        'type': lambda: f"Type {len(v)} characters into the editor",
        'click_save': lambda: "Click **Save**",
        'project_menu': lambda: f"Open the **Project** menu → **{v}**",
        'wait_for': lambda: f"Wait for {v}",
        'point': lambda: f"Point at line {v.get('editor_line')}" if isinstance(v, dict) else f"Point at {v}",
        'close_active_tab': lambda: "Close the active editor tab",
        'close_tab': lambda: f"Close the editor tab for `{v}`",
        'bottom_tab': lambda: f"Open the **{v}** tab in the bottom panel",
        'new_folder': lambda: f"Right-click `{v['parent']}` → **New Folder** → `{v['name']}` → **Save**",
        'type_end': lambda: f"At the end of the file, type {len(v)} characters",
        'nav': lambda: f"Left bar → **{v}**",
        'sql_connection': lambda: f"Pick the connection **{v}**",
        'sql_run': lambda: "Click the green run arrow next to line 1",
        'lineage_maximize': lambda: "Click **Maximize** on the lineage panel",
        'lineage_fit': lambda: "Fit the graph to the view",
        'point_tree': lambda: f"Point at `{v}` in the Explorer",
        'lineage_depth': lambda: f"Set lineage **Depth** to {v}",
        'expect_file': lambda: f"(check: `{v['path']}` equals `{v['snippet']}`)",
        'terminal': lambda: f"In the command box under the terminal, type `{v['cmd']}` and press Enter",
        'git_tab': lambda: "Open the **Git** tab in the sidebar",
        'explorer_tab': lambda: "Open the **Explorer** tab in the sidebar",
        'git_stage': lambda: f"Hover `{v}` and click **+** (Stage Changes)",
        'git_message': lambda: f"Type the commit message “{v}”",
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
        'wait_enabled': lambda: f"Wait until **{v['name']}** is enabled (sped up)",
        'follow_window': lambda: "Studio opens its main window",
        'goto': lambda: f"Browser: open {v}",
        'scroll_to': lambda: f"Scroll to **{v.get('label') or v.get('text') or v.get('selector')}**",
        'click_download': lambda: f"Click the download link **{v.get('label') or v.get('text') or v.get('selector')}**",
    }.get(k, lambda: f"{k}: {v}")()


out = [f"# {lesson['title']} — voice-over script and beat sheet", '',
       f"{course['title']} · {lesson['module']} · next: {lesson['next']}", '',
       f"App: {course['app']['name']} {course['app']['version']} (dbt-core {course['runtime']['dbt_core']}, "
       f"dbt-duckdb {course['runtime']['dbt_duckdb']}, Python {course['runtime']['python']}), {course['theme']} theme. "
       f"Voice: Kokoro `{course['voice']['voice']}` at {course['voice']['speed']}. Start state: `{lesson.get('start_state', 'none (slides only)')}`.", '',
       'Spoken lines are plain words. Code names are said as words and shown exactly on screen. '
       + ('Start times (@m:ss) and lengths are measured from the rendered video.' if tl else 'Times are estimates at 150 words per minute until the video is rendered.'), '']
total_words, est = 0, 0.0
for sc in lesson['scenes']:
    kind = sc['kind']
    if kind in ('title', 'closing'):
        secs = course['video']['title_card_s' if kind == 'title' else 'closing_card_s']
        out += [f"## {sc['id']} · {kind} card ({secs} s, no voice)", '', sc.get('show', ''), '']
        est += secs
        continue
    label = f"slide `{sc['slide']}`" if kind == 'slide' else ('Browser' if kind in ('browser', 'pane') else 'Rosetta DBT Studio')
    out += [f"## {sc['id']} · {kind} — {label}", '', '| Beat | Spoken | On screen | Words | ~s |', '|---|---|---|---|---|']
    for b in sc['beats']:
        w = words(b['say']); total_words += w
        voice_s = w / WPM * 60
        act_s = sum(len(list(x.values())[0]) / TYPE_CPS for x in b.get('actions', []) if isinstance(x, dict) and 'type' in x)
        secs = measured.get(b['id'], max(voice_s + 0.8, act_s + 0.8))
        est += secs
        screen = []
        if kind == 'slide':
            screen.append(b.get('show') or f"Build step {b.get('step')}")
        screen += [describe(x) for x in b.get('actions', [])]
        if b.get('zoom'): screen.append(f"Zoom: {b['zoom']}")
        if b.get('card'):
            c = b['card']; screen.append(f"Card: *{c['eyebrow']}* — **{c['title']}** — {c['sub']}")
        if b.get('verify'): screen.append(f"⚠ {b['verify']}")
        t = f" @{fmt(starts[b['id']])}" if b['id'] in starts else ''
        out.append(f"| {b['id']}{t} | {b['say']} | {'<br>'.join(screen) or '—'} | {w} | {secs:.0f} |")
    out.append('')
out += [f"**Total: {total_words} spoken words, " + (f"{fmt(tl['total'])} rendered.**" if tl else f"about {fmt(est)} estimated.**"), '']
(L / 'voiceover-script.md').write_text('\n'.join(out))
print(f"wrote {L / 'voiceover-script.md'}: {total_words} words, ~{fmt(est)}")
