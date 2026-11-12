# Lesson 1.2 · Parquet: why lakes use column files

Data Lakes with DuckLake in Rosetta DBT Studio · Module 1 · Data lakes explained. Rendered 1:50, 3840x2160 H.264 + AAC, 14 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-1-2.mp4` | The 4K video for YouTube (not in git) |
| `lesson-1-2-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-1-2.srt`, `lesson-1-2.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-1-2-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- The SQL Editor demo became slides with the real output: there is no DuckDB connection or lake yet at this point in the course.

## Accuracy notes

- One file per day: s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-10-01/part-00000-….snappy.parquet; 7,176 rows; 1 row group; SNAPPY; column number min 26,093,738 max 26,100,913; transaction_count 2 to 1,087; 5.6 MB compressed, 6.7 MB uncompressed; largest column logs_bloom, 3.0 MB. Read with parquet_metadata on 12 Nov 2026.
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
python3 scripts/tts.py ../project-02-ducklake ../project-02-ducklake/lesson-1-2-parquet     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-02-ducklake ../project-02-ducklake/lesson-1-2-parquet
python3 scripts/compose.py ../project-02-ducklake ../project-02-ducklake/lesson-1-2-parquet
python3 scripts/package.py ../project-02-ducklake ../project-02-ducklake/lesson-1-2-parquet
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
