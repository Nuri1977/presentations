# Lesson 6.1 · Connect a dbt project to the lake

Data Lakes with DuckLake in Rosetta DBT Studio · Module 6 · dbt on DuckLake. Rendered 2:29, 3840x2160 H.264 + AAC, 24 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-6-1.mp4` | The 4K video for YouTube (not in git) |
| `lesson-6-1-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-6-1.srt`, `lesson-6-1.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-6-1-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- Relative paths (lake/…) and no data_path option: dbt runs in the project folder, and the lake keeps its data path in the catalog.
- The lock demo is the end of this lesson (promised in 3.5): open the lake in Studio, then dbt debug fails.

## Accuracy notes

- dbt-duckdb 1.11.1 with DuckDB 1.5.6 attaches the lake made by Studio's 1.5.2; dbt debug passes; models build (rehearsal 12 Nov 2026).
- With the lake open in Studio: IO Error … Could not set lock on file …eth_catalog.duckdb: Conflicting lock is held in … Rosetta DBT Studio (studio-notes.md).
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../project-02-ducklake ../project-02-ducklake/lesson-6-1-connect-dbt
python3 scripts/tts.py ../project-02-ducklake ../project-02-ducklake/lesson-6-1-connect-dbt     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-02-ducklake ../project-02-ducklake/lesson-6-1-connect-dbt
python3 scripts/compose.py ../project-02-ducklake ../project-02-ducklake/lesson-6-1-connect-dbt
python3 scripts/package.py ../project-02-ducklake ../project-02-ducklake/lesson-6-1-connect-dbt
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
