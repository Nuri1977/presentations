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
        'lineage_depth': lambda: f"Set lineage **Depth** to {v}",
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
    label = f"slide `{sc['slide']}`" if kind == 'slide' else 'Rosetta DBT Studio'
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
