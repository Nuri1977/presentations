# Lesson 6.3 · Marts, built incrementally

Data Lakes with DuckLake in Rosetta DBT Studio · Module 6 · dbt on DuckLake. Rendered 2:19, 3840x2160 H.264 + AAC, 29 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-6-3.mp4` | The 4K video for YouTube (not in git) |
| `lesson-6-3-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-6-3.srt`, `lesson-6-3.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-6-3-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- The second run of daily_gas re-merges the last day instead of loading a new day of raw data: it shows the MERGE without a load between two dbt runs.

## Accuracy notes

- incremental_strategy='merge' compiles to MERGE INTO "eth_lake"."main"."daily_gas" in target/run (dbt-duckdb 1.11.1); the post_hook call eth_lake.set_commit_message('dbt', …) sets author and message on dbt's snapshot. Rehearsal 12 Nov 2026.
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../project-02-ducklake ../project-02-ducklake/lesson-6-3-marts
python3 scripts/tts.py ../project-02-ducklake ../project-02-ducklake/lesson-6-3-marts     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-02-ducklake ../project-02-ducklake/lesson-6-3-marts
python3 scripts/compose.py ../project-02-ducklake ../project-02-ducklake/lesson-6-3-marts
python3 scripts/package.py ../project-02-ducklake ../project-02-ducklake/lesson-6-3-marts
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
