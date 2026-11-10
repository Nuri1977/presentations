# Lesson 2.1 · Create the dbt project

dbt + DuckDB in Rosetta DBT Studio · Module 2 · dbt basics. Rendered 3:15, 3840x2160 H.264 + AAC, 42 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-2-1.mp4` | The 4K video for YouTube (not in git) |
| `lesson-2-1-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-2-1.srt`, `lesson-2-1.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-2-1-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- Connection first, then project: Studio's New Connection page returns to the connections list on Save, so the lesson creates the DuckDB connection from Home, then picks it in Setup New Project.
- The dev database file lives next to the project folder (projects/nyc_taxi_dev.duckdb), so it is never committed.
- Studio's template creates an `analysis` folder while dbt_project.yml says `analyses`; shown as is.
- Rehearsal cut: the GitHub scene shows nyc-taxi-dbt-rehearsal (Private), recorded in Lesson 1.2.

## Accuracy notes

- Setup New Project fields, the DuckDB form (Connection Name, Database File Path, Schema, Test Connection) and the Git tab flow (Initialize Repository, Commit, Publish Branch → Add git remote) checked in Studio 1.7.6 on 10 Nov 2026.
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../project-01 ../project-01/lesson-2-1-create-project
python3 scripts/tts.py ../project-01 ../project-01/lesson-2-1-create-project     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-01 ../project-01/lesson-2-1-create-project
python3 scripts/compose.py ../project-01 ../project-01/lesson-2-1-create-project
python3 scripts/package.py ../project-01 ../project-01/lesson-2-1-create-project
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
