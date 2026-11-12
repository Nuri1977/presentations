# Lesson 4.4 · Maintenance

Data Lakes with DuckLake in Rosetta DBT Studio · Module 4 · Performance and upkeep. Rendered 2:33, 3840x2160 H.264 + AAC, 23 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-4-4.mp4` | The 4K video for YouTube (not in git) |
| `lesson-4-4-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-4-4.srt`, `lesson-4-4.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-4-4-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- Snapshots are expired by number (versions => [6, 7], the October copy of 2.5) instead of older_than: the start state's snapshots are all minutes old, and the other snapshots are still used in Module 5.

## Accuracy notes

- Files: 19 before; 20 after merge_adjacent_files (raw.blocks: 4 files merged into 1); 14 after expire + cleanup. Time travel to versions 3 and 5 still works after the merge and cleanup. Rehearsed with DuckDB 1.5.2, 12 Nov 2026.
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../project-02-ducklake ../project-02-ducklake/lesson-4-4-maintenance
python3 scripts/tts.py ../project-02-ducklake ../project-02-ducklake/lesson-4-4-maintenance     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-02-ducklake ../project-02-ducklake/lesson-4-4-maintenance
python3 scripts/compose.py ../project-02-ducklake ../project-02-ducklake/lesson-4-4-maintenance
python3 scripts/package.py ../project-02-ducklake ../project-02-ducklake/lesson-4-4-maintenance
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
