---
name: "rosetta-academy-video"
description: "Produce Rosetta Academy lesson videos from a course draft: beat sheet for approval, automated Rosetta DBT Studio recording, HTML slides, Kokoro voice, a 4K MP4 for YouTube plus a phone-playable 1080p copy, captions and YouTube package."
---

# Rosetta Academy lesson videos

Use when Nuri asks for an Academy (academy.rosettadb.io) tutorial or course video: a lesson from a course
request/draft that combines HTML slides, recordings of the Rosetta DBT Studio Electron app, and a voice.
For release promos from GitHub release notes use `rosetta-release-video` instead.

This is content tooling in the `presentations/` repo, not dbt-studio product code, so it is fine to build
and run here. Pilot (approved 5 Nov 2026): dbt Fundamentals Lesson 3.2, 2:54, 4K.

## Hard rules

- **Never change anything in `dbt-studio/`** (the codebase). Read-only reference at most (e.g. `e2e/page-objects`).
- **`presentations/` is its own git repo** (github.com/Nuri1977/presentations). Write files only. Never stage,
  commit, branch or push; Nuri does that. Offer a commit message when asked.
- **One approval gate:** send the beat sheet (and slide stills) and wait for "approved" before recording or
  rendering the final video. After approval, render and deliver without further questions.
- **Voice first:** narration is generated and measured first; app actions and slide builds are paced to it.
- **UI labels vs facts:** when the app's label differs from the draft, use the real label and log it in
  `draft-corrections.md`. When a *factual claim* differs (versions, product names, licensing), flag it there
  and hold that lesson for Nuri's decision; continue other lessons.
- **Check current facts on the web** (docs.getdbt.com etc.) before putting version/licensing/product claims on
  a slide; note the source and date in the lesson's `accuracy_notes`.
- **One runner per course** so all lessons look the same (saved in `course.yaml` → `runner`).
- **Every lesson ships two videos** (see "Two video files"). Anything Nuri watches or shares uses the 1080p copy.
- Claude cannot hear audio: always ask Nuri to listen once for pronunciation.

## Visual rules (Nuri's review of Project 2, 12 Nov 2026; apply from Project 3 on)

Project 2 (DuckLake) is finished and stays as it is. Every course from Project 3 on follows these rules.

### Slides: icons on every content slide

- **Every content slide shows icons or logos** for the things it names: DuckLake, DuckDB, dbt, Parquet,
  Iceberg, Delta Lake, PostgreSQL, SQLite, S3, GitHub, Python, Rosetta DBT Studio, and so on. A slide with
  only text and plain boxes is not finished.
- **Where icons come from, in this order:**
  1. **Studio's own assets** (read only, copy them into the course's `brand/icons/`; never edit `dbt-studio/`):
     `dbt-studio/assets/icons/` (`duck-lake.svg`, `duckdb.svg`, `dbt-bit_tm.svg`, `dbt-black.svg`,
     `data-lake.svg`, `apache-iceberg-lake.png`, `apache-hudi-lake.png`, `delta-lake.png`, `rosetta.png`) and
     `dbt-studio/assets/connectionIcons/` (`ducklake.png`, `duckdb.png`, `postgresql.png`, `sqlite.png`,
     `s3.png`, `snowflake.png`, `lakekeeper.png`).
  2. **Free, open-license icon sets**, downloaded into `brand/icons/`: Simple Icons (CC0, brand logos),
     Lucide (ISC), Tabler Icons (MIT), Material Symbols (Apache 2.0), and each project's own brand kit
     (e.g. the DuckDB and DuckLake logos from duckdb.org / ducklake.select).
  3. **An existing web URL** only when a download is not possible. Prefer a local copy: renders must work
     offline, and a URL can change or disappear.
- Write each downloaded icon's source and licence in `brand/icons/SOURCES.md`.
- Use icons at a readable size (at least 64 px on a 1920x1080 slide; 96 to 160 px on cards and diagrams).
  Keep one style per slide (all logos, or all line icons).

### Slides: no empty pages

- **Cards, diagrams and code together cover more than 60% of the content area** (the space between the
  heading and the footer). No half-empty slides, no small cards floating in white space.
- When there is little to say, make the cards bigger: larger titles and text, an icon on each card, a
  diagram, or a real Studio screenshot. Do not leave the space empty.
- Check this on the contact sheet of slide stills before the approval gate: any slide where more than about
  40% of the content area is empty gets fixed.

### App recordings: one UI zoom, full screen first

- **Readability comes from Studio's own zoom (Cmd +/-), not from cropping the video.** Claude chooses the
  zoom level once per course and saves it in `course.yaml` (`ui_zoom`, e.g. 1.25; `browser_zoom` for web
  pages). Check at that level that the sidebar, header, editor, terminal and status bar all fit and are
  readable on a phone in the 1080p copy. Never change the zoom level in the middle of a course.
- **The default is no crop zoom at all** (`zoom: none` on every app beat): the viewer sees the whole Studio
  window.
- **Always show the full screen first.** Every app scene, and every return from a slide, starts on the full,
  unzoomed window and holds it for at least 1.5 to 2 seconds, so the viewer knows where they are.
- **Only then zoom, once, into one region**, and only when a detail is too small to read even with the UI
  zoom (one line of terminal output, a single result cell). Zoom back out to the full screen before moving to
  another region.
- **Never:** start a beat already zoomed; zoom from one cropped region straight to another; stack a crop
  zoom on top of a crop zoom; or show a crop where the sidebar, header or terminal are cut in half.
  These are what made the Project 2 videos confusing.
- **Tooling to change before Project 3** (not done yet): `compose.py` should default to no crop, insert a
  full-screen hold at the start of every app scene, and force a full-screen step between two zoomed beats.
  Until then, write `zoom: none` explicitly in `lesson.yaml`.

## Two video files

| File | For | Format |
|---|---|---|
| `<id>.mp4` | YouTube upload (master) | 3840x2160 H.264 High level 5.1, CRF 16, AAC mono, faststart |
| `<id>-1080p.mp4` | Phones, chat preview, sharing (CEO/CTO, Slack, WhatsApp, email) | 1920x1080 H.264 High **level 4.0**, yuv420p, CRF 20, **stereo** AAC 160k 48 kHz, faststart |

Why: many phones, and the Claude mobile app's player, cannot decode 4K H.264 (level 5.1) and show
"Can't play video". Level 4.0 1080p plays on practically every phone and is small (about 3 MB per minute).
YouTube still gets the 4K master and makes its own mobile versions.

`package.py` writes the 1080p copy automatically (and redoes it when the 4K file is newer). To make one by hand:

```sh
ffmpeg -y -i <id>.mp4 -vf "scale=1920:1080:flags=lanczos,format=yuv420p" -c:v libx264 -preset veryfast -crf 20 \
  -profile:v high -level 4.0 -c:a aac -b:a 160k -ac 2 -ar 48000 -movflags +faststart <id>-1080p.mp4
```

## Where things live

Connected folder on the Mac: `/Users/nuri/Documents/Projects/Adaptivescale/combined-dbt-project`
(in device_bash: `$HOME/mnt/combined-dbt-project`).

```
presentations/
  Academy-course-request-01/dbt_course_draft.docx.md   course draft (source of the scripts)
  _academy-video-tooling/      the pipeline (DESIGN.md has every decision and pilot finding)
    lib/studio.cjs  lib/actions.cjs  record.cjs  run-headless.sh  setup-runtime.sh
    scripts/{script_from_lesson,tts,render_stills,compose,package}.py
  <Course>/                    e.g. dbt-Fundamentals-Course/
    course.yaml  draft-corrections.md  downloads/*.sql  states/<recipe>/  .gitignore
    lesson-<n>-<slug>/  lesson.yaml  slides.html  logo_hero.svg  assets/  (+ generated files)
```

If `_academy-video-tooling/` is missing or broken, **stop and ask** rather than rewriting it from memory.

## Files

**course.yaml**: `title`, `subtitle`, `academy`, `source_draft`, `app` (name, pinned `version`, release
assets), `runner` (`linux-cloud` | `mac-desktop`), `theme` (dark), `runtime` (python, python_build_tag,
dbt_core, dbt_duckdb), `voice` (kokoro, af_heart, 1.0), `video` (3840x2160, 30 fps, crf 16, title 3 s,
closing 4 s), `youtube` (visibility unlisted, tags), `pronunciation` list of `[regex, spoken]`
(dbt → "D B T", DBT, SQL → "sequel", .sql → " dot sequel", DuckDB → "duck D B", YAML → "yammel",
DAG → "dag", CTE, Jinja, ETL, ELT, CI, v1/v2, "Lab 1" → "lab one"; extend per course).

**lesson.yaml** (the only file anyone edits; everything else is generated):

```yaml
id: lesson-3-2            # file stem for mp4/srt/vtt/pptx
number: "3.2"             # or "Welcome"
title: "Models, ref() and the DAG"
youtube_title: ...        # optional; default "<title> | <course> <number> | Rosetta DBT Studio"
module: "Module 3 · Building models"
draft_section: "Lesson 3.2: ..."
next: "Lesson 3.3 · Sources and the staging layer"
start_state: lesson-3-2-start   # only when there are app scenes
summary: "..."            # YouTube description first paragraph
tags: [...]
start_notes: [...]        # cue-sheet "Before you start" for a human retake
draft_changes: [...]      # readme: how the video differs from the draft script
accuracy_notes: [...]     # readme: what was verified, what was not, sources
scenes:
  - { id: s00, kind: title, slide: title, show: "..." }
  - id: s01
    kind: slide           # slide | app | title | closing
    slide: model          # section data-id in slides.html
    chapter: "What a model is"   # YouTube chapter (first forced to 0:00; chapters under 10 s are merged)
    beats:
      - { id: b01, step: 1, show: "what appears", say: "Spoken line." }
  - id: s02
    kind: app
    chapter: "..."
    beats:
      - id: b04
        say: "..."
        actions: [ { open_project: dbt_course }, { open_file: models/staging/stg_orders.sql } ]
        zoom: none          # default from Project 3 on; a crop zoom only after the full screen (see Visual rules)
        card: { eyebrow: "A model", title: "One file, one select", sub: "...", pos: top-right }
  - { id: s08, kind: closing, slide: closing, show: "..." }
```

App actions (implemented in `record.cjs`): `open_project: <name>` (Recent Projects on home),
`open_file: <path>` (expands folders as needed), `new_file: {folder, name}` (right-click → New File → name →
Save), `type: |` (editor, exact text), `click_save`, `project_menu: <item>` (Run, Test, Build, Compile,
Generate Docs, …), `wait_for: manifest`, `point: {editor_line: N}`, `close_tab: <path>`,
`bottom_tab: <LABEL>` (e.g. LINEAGE), `lineage_depth: N`. New actions go in `record.cjs` ACTIONS plus a
line in the describers in `script_from_lesson.py` and `package.py`.

**Writing beats.** Keep the draft's spoken lines; split long sentences; add plain demo lines for app scenes
("Open the Project menu, and choose Compile.") using real labels. Code names are said as words
("fact orders" for `fct_orders`) and shown exactly on screen. Captions keep the written form. Put typing in
the beat whose sentence describes it, split long code over several beats. Cards say the one thing the voice
does not. Draft cues that name Studio become app scenes; everything else becomes slides (slide-only lessons
need no start state and skip recording).

**Start states** (`states/<name>/recipe.yaml`: project_name, database_file, sql list, project_dir) are built
from the draft's appendix data and the lab files. A lab's finished state doubles as its reference-project
download. Keep continuity (e.g. no `.gitignore` before the lab that creates it; `.gitkeep` files are skipped).

**slides.html**: copy the `<style>` and `<script>` blocks from an existing lesson (house style: dark,
Inter, orange #ff7a1a/#ff9a3d, eyebrow bar, translucent cards, `logo_hero.svg`). Each `<section
class="stage" data-id=...>` matches `slide:` in lesson.yaml; elements with `class="s" data-step="n"`
appear at step n (`data-until` hides after a step); use `.pad.v` to center vertically; renderer calls
`window.show(id, step)`. Animated SVG for diagrams. Real 4K Studio frames from a lesson's
`render/app/frames/` can be reused as slide assets (`assets/`). Keep content inside the 120 px side margins
(check the right edge of wide flow diagrams).

## Workflow for one lesson

1. Read the lesson in the course draft. Write `lesson.yaml` (and a start-state recipe if it has app scenes).
2. If there are app scenes, explore first: launch the release with the start state and screenshot the screens
   you will use, to get real labels and behaviour (see Pitfalls). Write `slides.html`.
3. Generate the beat sheet and slide stills:
   `python3 scripts/script_from_lesson.py <lesson>` and `python3 scripts/render_stills.py <course> <lesson>`.
   Make a contact sheet of the slide states and view it (check overlaps, clipped text, empty halves, icons
   on every content slide, cards covering more than 60% of the content area).
4. **Send the beat sheet (`voiceover-script.md`) + slide contact sheet; wait for approval.**
5. Record (app scenes only): `NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs <course> <lesson>`
   (run in the background; ~2.5 min for 3.2; it exits 2 and names the beat on failure; fix and rerun).
6. Voice: `python3 scripts/tts.py <course> <lesson>` (`--human` uses `voice-human/<beat>.wav`).
7. Render: `python3 scripts/compose.py <course> <lesson> --preview 45` first, look at frames, then the full
   render (background; ~6 min compositing on 2 CPUs for a 3-minute lesson; ~2 min for slide-only lessons).
8. Package: `python3 scripts/package.py <course> <lesson>` → youtube.md, `<id>-slides.pptx`,
   RECORDING-cue-sheet.md, readme.md, timed beat sheet, **and `<id>-1080p.mp4`**.
9. Verify:
   - 4K: `ffprobe` shows 3840x2160 h264 + aac and duration = timeline total.
   - 1080p: `ffprobe` shows 1920x1080, h264 profile High, level 40 (never above 41), aac with 2 channels,
     same duration; size about 3 MB per minute.
   - `ebur128` loudness about -16 LUFS, peak about -1.5 dBFS.
   - Extract ~10 frames across all scenes into a contact sheet and view it (typing, menus, zooms, cards,
     lineage, every slide build). Fix and re-render only the stage that changed (narration only: skip record).
10. Deliver (below), then a short reply: what came out, length, which file plays on phones, what to check
    (pronunciation, pace, flagged facts), next step.

## Runner setup

**linux-cloud (default for dbt Fundamentals):** the Claude cloud workspace (root, GTK 3, Xvfb, ffmpeg,
Node 22, Playwright preinstalled). The workspace is ephemeral, so in a new session:

1. Bring sources in: `device_stage_files` (≤50 files per call) for `_academy-video-tooling/**` (not
   `.cache`, `node_modules`) and the course folder sources; copy them from `/mnt/user-data/uploads/...` to a
   work dir, e.g. `/home/claude/academy/{tooling,course}`.
2. `apt-get install -y libxss1 gnome-keyring dbus-x11 fonts-inter fonts-jetbrains-mono`
3. In tooling: `npm install --omit=dev` (js-yaml only; use the global Playwright via `NODE_PATH=$(npm root -g)`;
   never install another Playwright here).
4. App: download `Rosetta-DBT-Studio-<version>-x64.tar.gz` from
   `https://github.com/rosettadb/dbt-studio/releases/download/<version>/` into `.cache/app/` and extract.
5. Runtime: `./setup-runtime.sh 3.10.17 20250409 1.12.6 1.11.1` (Studio's own python-build-standalone
   CPython + pinned dbt; check Studio's defaults again when the pinned app version changes).
6. Voice: `pip install --break-system-packages kokoro-onnx soundfile python-pptx pyyaml`; download
   `kokoro-v1.0.onnx` and `voices-v1.0.bin` from
   `https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/` into `.cache/tts/`.

The Linux VM inside the Mac (device_bash) cannot run Electron (no GTK 3/libsecret, no root, 3 GB RAM).

**mac-desktop (documented, not yet run):** Claude Desktop on the Mac. `npm install` (includes Playwright
1.57 dev dependency) and `npx playwright install chromium`; use the Mac release zip (`-x64` or `-arm64`);
`record.cjs` needs its `appBin` pointed at `Rosetta DBT Studio.app/Contents/MacOS/Rosetta DBT Studio`;
no `run-headless.sh`. Try live capture there only if it holds 30 fps; otherwise keep the per-change stills.

## Delivery

- Copy outputs into `/mnt/user-data/outputs/presentations/...` and write them to the Mac with
  `device_commit_files` (stagedPath → `/Users/nuri/Documents/Projects/Adaptivescale/combined-dbt-project/presentations/...`, ≤50 files per call).
- **Videos:** MP4s cannot be committed by stagedPath. `SendUserFile` **both** files in one call, the
  `<id>-1080p.mp4` first (it is the one that plays in the chat and on phones), with a caption saying
  "1080p plays on phones; the 4K file is for YouTube". Then `device_commit_files` both with their `fileUuid`s.
  Never send only the 4K file for viewing.
- Do not copy `render/` (frames, audio, composites stay in the workspace). `.gitignore` already excludes
  renders, MP4, WAV, PPTX, zips and caches.
- Tell Nuri: share the 1080p copy; upload the 4K MP4 to YouTube as unlisted with the `.srt`; HD/4K appears
  only after YouTube finishes processing (minutes to an hour), so the first view may look blurry.
- **Commit message requests:** read the repo state without writing anything, e.g.
  `GIT_OPTIONAL_LOCKS=0 git -c safe.directory=* --no-optional-locks diff --cached --name-status` and
  `... status --porcelain` in device_bash (plain `git status` can leave `.lock` files the connected folder
  cannot delete). Flag junk such as `.DS_Store` with the unstage command, then give the message.

## Pitfalls learned in the pilot (keep these)

- Launch the packaged release with `executablePath`, `--user-data-dir=<throwaway>`, `--no-sandbox`,
  `--force-device-scale-factor=2`, and a fake `HOME=/home/learner` so terminal paths look clean. Do **not** set
  `E2E_TESTING` for the packaged app (it makes it look for dev renderer files).
- Seed `database.json` with `isSetup`, `pythonPath`, `pythonBinary`, `pythonVersion`, `dbtPath`, `dbtVersion`,
  the project and a DuckDB connection; symlink `userData/venv` and `userData/python/cpython-*` to the runtime.
- localStorage: `dbt-studio-theme-mode` must be JSON (`"dark"` with quotes); `dbt-studio-quickstart-tour-seen`.
- keytar needs a Secret Service: run under `dbus-run-session` with an unlocked gnome-keyring (run-headless.sh).
- Studio resizes its window after load: keep applying 1920x1080 until it holds (`sizeWindow`).
- Live screencast at 4K on 2 CPUs gave 4.9 fps, so record a 4K still after each visible change and draw
  cursor glide, click ripples, zooms and cards in `compose.py`.
- Typing: real keystrokes with the editor's helpers off (`tameEditor` wraps `updateOptions`: no auto-close,
  auto-indent, suggestions, blink). Inserting via `executeEdits` scrambles text in Studio's React editor.
- Explorer rows are `treeitem` with `level` = depth + 1; file rows start with an icon glyph, so match the
  name at the end. Editor tabs have the file's full path as `aria-label` and a close button inside.
  The Project split-button arrow is the button after "Project". The "Create new file" dialog field needs a
  click before typing; then click its Save.
- LINEAGE appears only for a SQL model in `target/manifest.json`, and the lookup is cached: after Compile,
  switch to another file and back. Depth 1 shows direct parents; depth 2 adds sources.
- `dbt compile` prints no final "Done" line; wait for `target/manifest.json` and the
  "dbt compile completed successfully" toast.
- Kokoro af_heart at 1.0 runs about 185 words per minute (estimates assume 150).
- Frames: `compose.py` dedupes identical states; slide crossfade 0.4 s, scene crossfade 0.5 s, zoom ease 0.7 s.
- 4K H.264 level 5.1 does not play on many phones ("Can't play video"): always make and send the 1080p copy.
- YouTube ignores all chapters if any chapter is under 10 s; `package.py` merges short ones and drops the
  list if fewer than 3 remain.