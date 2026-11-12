# Lesson 3.2 · Daily loads without duplicates

Data Lakes with DuckLake in Rosetta DBT Studio · Module 3 · Changing data. Rendered 2:08, 3840x2160 H.264 + AAC, 21 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-3-2.mp4` | The 4K video for YouTube (not in git) |
| `lesson-3-2-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-3-2.srt`, `lesson-3-2.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-3-2-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- MERGE is a slide: Studio's SQL Editor accepts only some statement types and rejects MERGE. The same idempotent load runs live as INSERT … WHERE NOT EXISTS; a real MERGE runs from dbt in Lesson 6.3.

## Accuracy notes

- 2 November 2026: 7,176 blocks. The second run inserts nothing and creates no snapshot (snapshot 11 is the only new one). Rehearsal 12 Nov 2026.
- Studio 1.7.6 shows DATE values as {days: n} in the result grid (20758 = 2026-11-01); later lessons format dates with strftime.
- MERGE INTO … WHEN MATCHED / WHEN NOT MATCHED: DuckLake docs, Upserting page, checked 11 Nov 2026.
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../project-02-ducklake ../project-02-ducklake/lesson-3-2-daily-loads
python3 scripts/tts.py ../project-02-ducklake ../project-02-ducklake/lesson-3-2-daily-loads     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-02-ducklake ../project-02-ducklake/lesson-3-2-daily-loads
python3 scripts/compose.py ../project-02-ducklake ../project-02-ducklake/lesson-3-2-daily-loads
python3 scripts/package.py ../project-02-ducklake ../project-02-ducklake/lesson-3-2-daily-loads
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
