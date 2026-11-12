# Lesson 5.2 · Inside the catalog: files and statistics

Data Lakes with DuckLake in Rosetta DBT Studio · Module 5 · Inside the catalog. Rendered 2:00, 3840x2160 H.264 + AAC, 20 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-5-2.mp4` | The 4K video for YouTube (not in git) |
| `lesson-5-2-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-5-2.srt`, `lesson-5-2.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-5-2-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft


## Accuracy notes

- raw.transactions (table id 5): data files 11 to 17, one per day; block_number min and max per file 26,093,738–26,100,913 (file 11) to 26,136,783–26,143,955 (file 17); partition values 2026-10-01 to 2026-10-07. Inlined data table for watchlist (id 8). Rehearsed with DuckDB 1.5.2, 12 Nov 2026.
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../project-02-ducklake ../project-02-ducklake/lesson-5-2-catalog-files
python3 scripts/tts.py ../project-02-ducklake ../project-02-ducklake/lesson-5-2-catalog-files     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-02-ducklake ../project-02-ducklake/lesson-5-2-catalog-files
python3 scripts/compose.py ../project-02-ducklake ../project-02-ducklake/lesson-5-2-catalog-files
python3 scripts/package.py ../project-02-ducklake ../project-02-ducklake/lesson-5-2-catalog-files
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
