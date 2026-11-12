# Lesson 3.1 · Insert, update, delete, and delete files

Data Lakes with DuckLake in Rosetta DBT Studio · Module 3 · Changing data. Rendered 2:20, 3840x2160 H.264 + AAC, 23 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-3-1.mp4` | The 4K video for YouTube (not in git) |
| `lesson-3-1-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-3-1.srt`, `lesson-3-1.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-3-1-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- The update changes extra_data on every hundredth block (miner is already lower case in the data).
- Studio's row edit screens are not used: the SQL shows the same thing more clearly.

## Accuracy notes

- blocks_day (1 Oct 2026): 7,176 rows; 7 blocks with fewer than 50 transactions deleted; 72 rows updated (number % 100 = 0). After the update: one data file with a delete file, plus a new data file for the updated rows. Snapshots 8, 9, 10. Rehearsal 12 Nov 2026.
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../project-02-ducklake ../project-02-ducklake/lesson-3-1-insert-update-delete
python3 scripts/tts.py ../project-02-ducklake ../project-02-ducklake/lesson-3-1-insert-update-delete     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-02-ducklake ../project-02-ducklake/lesson-3-1-insert-update-delete
python3 scripts/compose.py ../project-02-ducklake ../project-02-ducklake/lesson-3-1-insert-update-delete
python3 scripts/package.py ../project-02-ducklake ../project-02-ducklake/lesson-3-1-insert-update-delete
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
