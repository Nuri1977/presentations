# Lesson 0 · Welcome: an Ethereum data lake on your laptop

Data Lakes with DuckLake in Rosetta DBT Studio · Welcome. Rendered 2:10, 3840x2160 H.264 + AAC, 17 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-0.mp4` | The 4K video for YouTube (not in git) |
| `lesson-0-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-0.srt`, `lesson-0.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-0-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- Three full months of blocks (August to October 2026, 92 days) instead of 90 days, so each month is one load.

## Accuracy notes

- Rows measured on 12 Nov 2026 from the AWS public blockchain bucket: blocks 2026-08-01 to 2026-10-31, 659,896 rows; transactions 2026-10-01 to 2026-10-07, 12,695,803 rows.
- Lake size after Module 4 in the rehearsal: about 1.9 GB (transactions 1.7 GB).
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
python3 scripts/tts.py ../project-02-ducklake ../project-02-ducklake/lesson-0-welcome     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-02-ducklake ../project-02-ducklake/lesson-0-welcome
python3 scripts/compose.py ../project-02-ducklake ../project-02-ducklake/lesson-0-welcome
python3 scripts/package.py ../project-02-ducklake ../project-02-ducklake/lesson-0-welcome
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
