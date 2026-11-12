# Lesson 1.6 · Under the hood: DuckDB and DuckLake in Studio

Data Lakes with DuckLake in Rosetta DBT Studio · Module 1 · Data lakes explained. Rendered 2:18, 3840x2160 H.264 + AAC, 21 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-1-6.mp4` | The 4K video for YouTube (not in git) |
| `lesson-1-6-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-1-6.srt`, `lesson-1-6.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-1-6-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- The SQL Editor part (version and extension queries) is a slide with the real output: there is no lake yet in this lesson; Lesson 2.1 runs the first query on the lake.

## Accuracy notes

- Code quoted from the 1.7.6 tag of rosettadb/dbt-studio: src/main/services/duckdb.service.ts (DuckDBInstance.create, instance.connect), duckLake/adapters/duckdb.adapter.ts and base.adapter.ts (INSTALL/LOAD ducklake, ATTACH … AS "name" (DATA_PATH …, AUTOMATIC_MIGRATION TRUE), USE), release/app/package.json (@duckdb/node-api ^1.5.2-r.1).
- dbt runtime: dbt-duckdb 1.11.1 with Python DuckDB 1.5.6; reading and writing a lake made by Studio's 1.5.2 checked on 11 Nov 2026 (studio-notes.md).
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../project-02-ducklake ../project-02-ducklake/lesson-1-6-under-the-hood
python3 scripts/tts.py ../project-02-ducklake ../project-02-ducklake/lesson-1-6-under-the-hood     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-02-ducklake ../project-02-ducklake/lesson-1-6-under-the-hood
python3 scripts/compose.py ../project-02-ducklake ../project-02-ducklake/lesson-1-6-under-the-hood
python3 scripts/package.py ../project-02-ducklake ../project-02-ducklake/lesson-1-6-under-the-hood
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
