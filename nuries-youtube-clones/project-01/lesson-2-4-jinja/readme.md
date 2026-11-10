# Lesson 2.4 · Dependencies & Jinja

dbt + DuckDB in Rosetta DBT Studio · Module 2 · dbt basics. Rendered 3:00, 3840x2160 H.264 + AAC, 37 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-2-4.mp4` | The 4K video for YouTube (not in git) |
| `lesson-2-4-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-2-4.srt`, `lesson-2-4.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-2-4-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- dbt commands from Studio's dropdowns: Project ▸ Seed, Model ▸ Compile on top_pickup_zones, Project ▸ Run.
- The plan's lineage view (s07) moves to Lesson 2.6, which is about the DAG.
- Model ▸ Compile opens a Compiled SQL window (Original SQL / Compiled SQL tabs) in Studio 1.7.6; the lesson shows it there instead of opening target/compiled.

## Accuracy notes

- Measured with dbt-core 1.12.6 / dbt-duckdb 1.11.1 on 10 Nov 2026 (files downloaded 9 Nov 2026): seed INSERT 265; busiest pickup zone 74 East Harlem North with 143,115 trips; Manhattan 344,997 trips in trips_per_month.
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../project-01 ../project-01/lesson-2-4-jinja
python3 scripts/tts.py ../project-01 ../project-01/lesson-2-4-jinja     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-01 ../project-01/lesson-2-4-jinja
python3 scripts/compose.py ../project-01 ../project-01/lesson-2-4-jinja
python3 scripts/package.py ../project-01 ../project-01/lesson-2-4-jinja
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
