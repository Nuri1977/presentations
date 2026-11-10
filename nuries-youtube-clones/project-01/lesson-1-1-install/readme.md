# Lesson 1.1 · Install Rosetta DBT Studio

dbt + DuckDB in Rosetta DBT Studio · Module 1 · Set up. Rendered 2:51, 3840x2160 H.264 + AAC, 47 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-1-1.mp4` | The 4K video for YouTube (not in git) |
| `lesson-1-1-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-1-1.srt`, `lesson-1-1.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-1-1-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- The DMG window and the macOS open prompt are shown on a slide built from the release's own DMG background (assets/dmg-background.png) and window layout (540x380, app left, Applications right). The recorder cannot capture Finder, and the recording Mac keeps its own Studio in /Applications.
- The download is started for real on the release page and cancelled in this rehearsal; the app used is the same 1.7.6 x64 build.
- The plan's home tour named New Project; Studio 1.7.6's home screen shows New Connection, Open Project and Settings, and projects start from the DBT Project card (Lesson 2.1).

## Accuracy notes

- Release page checked 9 Nov 2026: 1.7.6 is Latest; GitHub lists Rosetta-DBT-Studio-1.7.6-x64.dmg as 196 MB and -arm64.dmg as 187 MB, plus .exe, .deb, .rpm, .flatpak, .tar.gz and .zip builds.
- The 1.7.6 Mac app is signed and notarized (spctl: accepted, source=Notarized Developer ID), so macOS shows its standard open prompt for downloaded apps.
- First-run setup, recorded here: Step 1 of 2 asks for dbt 1.x (Recommended) or 2.x, the version (1.12.6 latest), adapters (all except DuckDB are checked by default), optional tools (Flowfile). Step 2 of 2 installs Python 3.10.17 and dbt 1.12.6 with 1 adapter (about 90 seconds here).
- After setup, Studio's folder holds python/cpython-3.10.17 (51 MB) and venv with dbt-core 1.12.6 + dbt-duckdb 1.11.1 (346 MB).
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../project-01 ../project-01/lesson-1-1-install
python3 scripts/tts.py ../project-01 ../project-01/lesson-1-1-install     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-01 ../project-01/lesson-1-1-install
python3 scripts/compose.py ../project-01 ../project-01/lesson-1-1-install
python3 scripts/package.py ../project-01 ../project-01/lesson-1-1-install
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
