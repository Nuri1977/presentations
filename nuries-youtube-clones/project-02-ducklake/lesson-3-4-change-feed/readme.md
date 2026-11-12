# Lesson 3.4 · The data change feed

Data Lakes with DuckLake in Rosetta DBT Studio · Module 3 · Changing data. Rendered 2:09, 3840x2160 H.264 + AAC, 18 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-3-4.mp4` | The 4K video for YouTube (not in git) |
| `lesson-3-4-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-3-4.srt`, `lesson-3-4.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-3-4-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- The schema-qualified functions are used (ducklake_table_changes('eth_lake', 'raw', 'blocks_day', …)): the short form eth_lake.table_changes('blocks_day', …) looks in schema main.

## Accuracy notes

- Snapshots 9 to 10 with DuckDB 1.5.6 (dbt runtime): 7 deletes at 9; 72 update_preimage and 72 update_postimage at 10. With Studio's DuckDB 1.5.2 (ducklake 415a9ebd), on a lake written by 1.5.2 too: 79 deletes at 9 and 72 inserts at 10. table_insertions(8,8) = 7,176 and table_deletions(9,9) = 7 in both. Checked 12 Nov 2026.
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../project-02-ducklake ../project-02-ducklake/lesson-3-4-change-feed
python3 scripts/tts.py ../project-02-ducklake ../project-02-ducklake/lesson-3-4-change-feed     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-02-ducklake ../project-02-ducklake/lesson-3-4-change-feed
python3 scripts/compose.py ../project-02-ducklake ../project-02-ducklake/lesson-3-4-change-feed
python3 scripts/package.py ../project-02-ducklake ../project-02-ducklake/lesson-3-4-change-feed
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
