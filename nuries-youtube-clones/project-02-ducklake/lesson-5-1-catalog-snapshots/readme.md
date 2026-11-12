# Lesson 5.1 · Inside the catalog: snapshots, tables, columns

Data Lakes with DuckLake in Rosetta DBT Studio · Module 5 · Inside the catalog. Rendered 2:16, 3840x2160 H.264 + AAC, 20 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-5-1.mp4` | The 4K video for YouTube (not in git) |
| `lesson-5-1-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-5-1.srt`, `lesson-5-1.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-5-1-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- The catalog is read through the database Studio already attaches, __ducklake_metadata_eth_lake, instead of opening the catalog file as a second connection.
- No commit message in the catalog: Studio's SQL Editor cannot set one (2.4); the snapshot changes column is shown instead.

## Accuracy notes

- duckdb_databases() on the lake connection lists __ducklake_metadata_eth_lake (duckdb) and eth_lake (ducklake). ducklake_table: blocks (id 2, from snapshot 2), blocks_day (4, 8), transactions (5, 16), watchlist (8, 20); id 3 (the October copy) is gone after 4.4. ducklake_column: column 3 is miner from 2 to 14, fee_recipient from 14. Rehearsed with DuckDB 1.5.2, 12 Nov 2026.
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../project-02-ducklake ../project-02-ducklake/lesson-5-1-catalog-snapshots
python3 scripts/tts.py ../project-02-ducklake ../project-02-ducklake/lesson-5-1-catalog-snapshots     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-02-ducklake ../project-02-ducklake/lesson-5-1-catalog-snapshots
python3 scripts/compose.py ../project-02-ducklake ../project-02-ducklake/lesson-5-1-catalog-snapshots
python3 scripts/package.py ../project-02-ducklake ../project-02-ducklake/lesson-5-1-catalog-snapshots
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
