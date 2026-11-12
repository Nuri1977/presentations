# Lesson 2.2 · Load three months of blocks from S3

Data Lakes with DuckLake in Rosetta DBT Studio · Module 2 · Your first lake in Studio. Rendered 3:33, 3840x2160 H.264 + AAC, 32 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-2-2.mp4` | The 4K video for YouTube (not in git) |
| `lesson-2-2-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-2-2.srt`, `lesson-2-2.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-2-2-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- Three full months (August to October, 92 days) instead of 90 days: one statement per month.
- The Import Data screen is not used: the SQL shows what happens and gives three separate snapshots.

## Accuracy notes

- Rows: August 222,412, September 215,033, October 222,451; 659,896 in total (rehearsal 12 Nov 2026, same files as S3).
- set_option does not create a snapshot; create schema is snapshot 1, the August table snapshot 2, September 3, October 4.
- Studio reads the public bucket without any secret; the region is found automatically.
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../project-02-ducklake ../project-02-ducklake/lesson-2-2-load-blocks
python3 scripts/tts.py ../project-02-ducklake ../project-02-ducklake/lesson-2-2-load-blocks     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-02-ducklake ../project-02-ducklake/lesson-2-2-load-blocks
python3 scripts/compose.py ../project-02-ducklake ../project-02-ducklake/lesson-2-2-load-blocks
python3 scripts/package.py ../project-02-ducklake ../project-02-ducklake/lesson-2-2-load-blocks
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
