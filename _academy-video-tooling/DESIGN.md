# Academy video tooling: design

Confirmed with Nuri on 5 Nov 2026. This folder is the code behind the `rosetta-academy-video` skill.
It turns one Academy lesson script into a narrated, YouTube-ready video that combines HTML slides
with automated recordings of Rosetta DBT Studio. Pilot: dbt Fundamentals, Lesson 3.2.

## Sources
- `course.yaml`: title, pinned app version, runner, runtime versions, voice, pronunciation list.
- `lesson.yaml`, one per lesson, generated from the course draft: scenes, then beats (spoken line,
  on-screen cue, slide build step or app actions, overlay card, zoom target) and the start state.
  **Edit only this file.** Everything else is generated from it.
- `states/<name>/`: start-state recipes (project files, SQL to load into DuckDB). The finished project
  of each lab doubles as the reference-project download.

## Lesson shape
Title card (3 s), then scenes, then "Next lesson" card (4 s). No on-screen presenter.
A draft cue that names Studio becomes an app scene; everything else becomes a slide.
Diagrams are animated SVG inside the HTML slides, revealing per sentence. Lineage is Studio's own view.

## Voice and timing
Kokoro `af_heart`, speed 1.0, course pronunciation list. Code names are spoken as words.
Voice first: every beat is voiced and measured, then app actions are paced to land on the words.
Your own voice later: one file per beat in `voice-human/<beat-id>.wav`; footage is reused and each
beat's ending hold is stretched or trimmed.

## App recording
- The official release of the course's pinned version, downloaded into `.cache/app`, launched by
  Playwright `_electron` with `executablePath`, a throwaway profile (`--user-data-dir`) under a fake
  home (`/home/learner`) so on-screen paths are clean. Never reads from or builds in `dbt-studio/`.
- Seeded `database.json`: `isSetup`, `pythonPath`, `pythonBinary`, `pythonVersion`, `dbtPath`,
  `dbtVersion`, project, DuckDB connection. `userData/venv` and `userData/python/cpython-*` are
  symlinks to the pinned runtime from `setup-runtime.sh` (Studio's own CPython build + dbt).
- localStorage: `dbt-studio-theme-mode` = JSON `"dark"`, `dbt-studio-quickstart-tour-seen` = `true`.
- Window: Studio resizes itself after load, so `sizeWindow` keeps applying 1920x1080 until it holds.
  Device scale 2, so every frame is 3840x2160.
- **Typing:** real keystrokes with the editor's helpers switched off (auto-close, auto-indent,
  autocomplete, suggestions, cursor blink). Studio's React wrapper re-applies options on re-render,
  so `tameEditor` wraps `updateOptions` for the whole recording. Inserting through `executeEdits`
  does NOT work: the controlled component resets the cursor and drops characters.
- **Lineage:** the LINEAGE bottom tab appears only for a SQL model that is in `target/manifest.json`,
  and Studio caches the lookup, so after Compile switch to another file and back.
- **Capture:** on the Linux runner (2 CPUs), live screencast frames averaged 4.9 fps at 4K, so this
  runner uses the agreed fallback for every stretch: a 4K still after each visible change (each typed
  character, each menu or panel change, each cursor arrival). The cursor glide, click ripple, zooms
  and overlay cards are drawn in afterwards on the timeline. A full 4K screenshot takes about 0.2 s,
  a clipped one about 0.14 s. The Mac runner may use live capture if it holds 30 fps.
- Playwright `recordVideo`, the trace and `events.jsonl` are kept only as a debugging record.
- Selectors: Explorer rows are `treeitem` with `level` = path depth + 1 (project root is level 1); file
  rows start with an icon glyph, so match the name at the end. Editor tabs carry the file's full path as
  `aria-label` and hold a close button. The Project split-button arrow is the button after "Project".

## Pilot results (Lesson 3.2, 5 Nov 2026)
- Recording: 420 stills in about 150 s of app time. Compose: 1,398 unique composited frames, about
  6 minutes on 2 CPUs. Final: 2:54, 3840x2160 H.264 CRF 16 + AAC, 39 MB, -16.4 LUFS, peak -1.5 dBFS.
- Kokoro `af_heart` at 1.0 speaks about 185 words per minute, faster than the 150 wpm estimate.
- Timing rules in `compose.py`: 0.35 s before the voice, 0.6 s after it, actions start at 0.25 s,
  glides 0.32 to 0.75 s by distance, typing fills the voice of its beat (9 to 30 characters per second),
  scene crossfade 0.5 s, slide build crossfade 0.4 s, zoom ease 0.7 s, cards fade 0.3 s.

## Runners
- `linux-cloud` (this course): the Claude cloud workspace. Needs root for `apt-get install libxss1
  gnome-keyring dbus-x11 fonts-inter fonts-jetbrains-mono`; Xvfb, ffmpeg, Node 22, Playwright present.
  The Linux VM inside the Mac cannot run Electron (no GTK 3 / libsecret, no root, 3 GB RAM).
- `mac-desktop`: Claude Desktop on the Mac runs the same scripts against the Mac release zip.
- One course is recorded on one runner so lessons look consistent.

## Slides
HTML in the Beginners Course house style (dark, Inter, orange #ff7a1a / #ff9a3d, eyebrow bar,
translucent cards) is the original. Rendered straight to 4K frames. Bullets and diagram parts appear
per sentence. `.pptx` export: one full-slide image per slide, narration in the speaker notes.

## Outputs per lesson
4K MP4 (3840x2160 H.264, CRF 16, AAC), `.srt` + `.vtt`, `voiceover-script.md`,
`voiceover-kokoro.txt`, `timeline.json`, `RECORDING-cue-sheet.md`, `.pptx`, `youtube.md` (unlisted,
title, description with chapters, tags), 1280x720 thumbnail, readme (versions, changes from draft).
Per course: reference-project zips, starter `.sql` files, `draft-corrections.md`.

## Draft mismatches
UI labels are fixed automatically and logged. Factual claims are flagged and that lesson waits.

## Git
`presentations/` is its own git repo; Claude writes files only and never commits.
Renders, MP4s, WAVs, frames and caches are ignored.
