# Lesson 6.2 · Staging models for blocks and transactions

Data Lakes with DuckLake in Rosetta DBT Studio · Module 6 · dbt on DuckLake. Rendered 2:03, 3840x2160 H.264 + AAC, 23 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-6-2.mp4` | The 4K video for YouTube (not in git) |
| `lesson-6-2-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-6-2.srt`, `lesson-6-2.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-6-2-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- Rows are shown with dbt show in the terminal instead of Model ▸ Preview: Preview runs on Studio's own connection, and opening the lake in Studio would block dbt (6.1).
- No extra day of raw data: 6.3 shows the incremental model with a second run instead.

## Accuracy notes

- dbt run builds main.stg_blocks and main.stg_transactions as views in eth_lake; views are catalog entries only (ducklake_view). Rehearsal 12 Nov 2026.
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../project-02-ducklake ../project-02-ducklake/lesson-6-2-staging
python3 scripts/tts.py ../project-02-ducklake ../project-02-ducklake/lesson-6-2-staging     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-02-ducklake ../project-02-ducklake/lesson-6-2-staging
python3 scripts/compose.py ../project-02-ducklake ../project-02-ducklake/lesson-6-2-staging
python3 scripts/package.py ../project-02-ducklake ../project-02-ducklake/lesson-6-2-staging
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
