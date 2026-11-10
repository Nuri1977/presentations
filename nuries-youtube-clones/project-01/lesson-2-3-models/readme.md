# Lesson 2.3 · Models: your first dbt model

dbt + DuckDB in Rosetta DBT Studio · Module 2 · dbt basics. Rendered 3:41, 3840x2160 H.264 + AAC, 54 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-2-3.mp4` | The 4K video for YouTube (not in git) |
| `lesson-2-3-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-2-3.srt`, `lesson-2-3.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-2-3-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- The plan's s05 queried `trips` in the SQL Editor. In Studio 1.7.6 the SQL Editor, Execute Query and Model > Preview all run DuckDB from Studio's own folder, so the view's relative parquet path fails ("No files found"). The lesson uses `dbt show` in Studio's terminal instead, which runs in the project folder. Logged in studio-notes.md.
- dbt commands from Studio's dropdowns (Nuri, 10 Nov): the model runs from Model ▸ Run. Model ▸ Preview cannot read the view's relative parquet path in 1.7.6, so the rows still come from dbt show in the terminal.
- Ends with commit + Sync Changes (push to main) and the models folder on GitHub (rehearsal repo).
- The Source Control panel is the Git tab in the Explorer sidebar in 1.7.6; a new file must be staged with + before Commit is enabled.

## Accuracy notes

- Measured on 9 Nov 2026 from the TLC files downloaded that day: 591,375 raw rows in green_tripdata_2025-01..12; 565,039 rows in `trips` after the filter.
- Run output `OK created sql view model main.trips` and the `create view "nyc_taxi_dev"."main"."trips__dbt_tmp"` statement in target/run are the real outputs of this recording (dbt-core 1.12.6, dbt-duckdb 1.11.1).
- dbt's view materialization creates the view under a temporary name and then renames it, which is why target/run shows trips__dbt_tmp.
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../project-01 ../project-01/lesson-2-3-models
python3 scripts/tts.py ../project-01 ../project-01/lesson-2-3-models     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-01 ../project-01/lesson-2-3-models
python3 scripts/compose.py ../project-01 ../project-01/lesson-2-3-models
python3 scripts/package.py ../project-01 ../project-01/lesson-2-3-models
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
