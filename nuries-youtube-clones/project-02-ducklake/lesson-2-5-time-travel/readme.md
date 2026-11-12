# Lesson 2.5 · Time travel

Data Lakes with DuckLake in Rosetta DBT Studio · Module 2 · Your first lake in Studio. Rendered 1:56, 3840x2160 H.264 + AAC, 17 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-2-5.mp4` | The 4K video for YouTube (not in git) |
| `lesson-2-5-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-2-5.srt`, `lesson-2-5.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-2-5-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- Time travel by timestamp and ATTACH … (SNAPSHOT_VERSION n) are on a slide: the start state's snapshots are all seconds old, and the SQL Editor does not accept ATTACH.

## Accuracy notes

- Counts: now 667,072; version 2: 222,412 (August); version 3: August 222,412 and September 215,033; the October copy from version 4: 222,451 rows. Rehearsal 12 Nov 2026.
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../project-02-ducklake ../project-02-ducklake/lesson-2-5-time-travel
python3 scripts/tts.py ../project-02-ducklake ../project-02-ducklake/lesson-2-5-time-travel     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-02-ducklake ../project-02-ducklake/lesson-2-5-time-travel
python3 scripts/compose.py ../project-02-ducklake ../project-02-ducklake/lesson-2-5-time-travel
python3 scripts/package.py ../project-02-ducklake ../project-02-ducklake/lesson-2-5-time-travel
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
