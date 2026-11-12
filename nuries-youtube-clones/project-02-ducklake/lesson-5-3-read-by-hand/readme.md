# Lesson 5.3 · Read the lake by hand

Data Lakes with DuckLake in Rosetta DBT Studio · Module 5 · Inside the catalog. Rendered 2:12, 3840x2160 H.264 + AAC, 19 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-5-3.mp4` | The 4K video for YouTube (not in git) |
| `lesson-5-3-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-5-3.srt`, `lesson-5-3.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-5-3-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- The files are read with a glob plus a filter on the file names the catalog lists: DuckDB does not accept a subquery as a table function argument.
- raw.transactions is used (no delete files), so reading its data files gives the full answer; a table with delete files would also need ducklake_delete_file.

## Accuracy notes

- Current snapshot 24; transactions table id 5, path transactions/; data_path is the absolute data folder (the rehearsal's own lake stored it as data/, relative); 7 files valid at 24; 12,695,803 rows by hand and from raw.transactions. Rehearsed with DuckDB 1.5.2, 12 Nov 2026.
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../project-02-ducklake ../project-02-ducklake/lesson-5-3-read-by-hand
python3 scripts/tts.py ../project-02-ducklake ../project-02-ducklake/lesson-5-3-read-by-hand     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-02-ducklake ../project-02-ducklake/lesson-5-3-read-by-hand
python3 scripts/compose.py ../project-02-ducklake ../project-02-ducklake/lesson-5-3-read-by-hand
python3 scripts/package.py ../project-02-ducklake ../project-02-ducklake/lesson-5-3-read-by-hand
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
