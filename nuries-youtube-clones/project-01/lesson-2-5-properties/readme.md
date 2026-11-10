# Lesson 2.5 · Properties: describe your models

dbt + DuckDB in Rosetta DBT Studio · Module 2 · dbt basics. Rendered 2:46, 3840x2160 H.264 + AAC, 43 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-2-5.mp4` | The 4K video for YouTube (not in git) |
| `lesson-2-5-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-2-5.srt`, `lesson-2-5.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-2-5-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- schema.yml is pasted (long YAML, plan D8); seeds.yml and the persist_docs lines are typed.
- The plan's s04 (comments in duckdb_columns()) is kept: dbt-duckdb 1.11.1 persists relation and column comments, checked off camera on 10 Nov 2026.

## Accuracy notes

- persist_docs checked with dbt-core 1.12.6 / dbt-duckdb 1.11.1: duckdb_columns().comment holds the column descriptions of trips_per_month; avg_fare has none because schema.yml does not describe it.
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../project-01 ../project-01/lesson-2-5-properties
python3 scripts/tts.py ../project-01 ../project-01/lesson-2-5-properties     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-01 ../project-01/lesson-2-5-properties
python3 scripts/compose.py ../project-01 ../project-01/lesson-2-5-properties
python3 scripts/package.py ../project-01 ../project-01/lesson-2-5-properties
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
