# Lesson 1.3 · Table formats: Iceberg, Delta Lake, DuckLake

Data Lakes with DuckLake in Rosetta DBT Studio · Module 1 · Data lakes explained. Rendered 2:07, 3840x2160 H.264 + AAC, 17 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-1-3.mp4` | The 4K video for YouTube (not in git) |
| `lesson-1-3-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-1-3.srt`, `lesson-1-3.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-1-3-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft


## Accuracy notes

- Iceberg: table metadata files (JSON) point to manifest lists and manifests (Avro) in the table location; a catalog stores the pointer to the current metadata file (Iceberg spec).
- Delta Lake: a transaction log of JSON commit files in _delta_log, with Parquet checkpoints (Delta protocol).
- DuckLake: all metadata in a SQL database (DuckDB, SQLite, PostgreSQL, MySQL); data in Parquet (DuckLake docs, checked 11 Nov 2026).
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
python3 scripts/tts.py ../project-02-ducklake ../project-02-ducklake/lesson-1-3-table-formats     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-02-ducklake ../project-02-ducklake/lesson-1-3-table-formats
python3 scripts/compose.py ../project-02-ducklake ../project-02-ducklake/lesson-1-3-table-formats
python3 scripts/package.py ../project-02-ducklake ../project-02-ducklake/lesson-1-3-table-formats
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
