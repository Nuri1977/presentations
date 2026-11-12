# Lesson 4.1 · Partitioning

Data Lakes with DuckLake in Rosetta DBT Studio · Module 4 · Performance and upkeep. Rendered 7:03, 3840x2160 H.264 + AAC, 62 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-4-1.mp4` | The 4K video for YouTube (not in git) |
| `lesson-4-1-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-4-1.srt`, `lesson-4-1.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-4-1-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- CREATE TABLE, then ALTER TABLE … SET PARTITIONED BY (date) before the first insert (same effect as partitioning at create time).
- One insert for the whole week with a glob date=2026-10-0[1-7], instead of seven inserts.

## Accuracy notes

- Transactions 1 to 7 Oct 2026: 2,036,041 / 1,875,646 / 1,562,292 / 1,526,358 / 1,774,270 / 1,957,602 / 1,963,594; 12,695,803 in total; seven files, one per date= folder; about 1.7 GB. Rehearsal 12 Nov 2026.
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../project-02-ducklake ../project-02-ducklake/lesson-4-1-partitioning
python3 scripts/tts.py ../project-02-ducklake ../project-02-ducklake/lesson-4-1-partitioning     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-02-ducklake ../project-02-ducklake/lesson-4-1-partitioning
python3 scripts/compose.py ../project-02-ducklake ../project-02-ducklake/lesson-4-1-partitioning
python3 scripts/package.py ../project-02-ducklake ../project-02-ducklake/lesson-4-1-partitioning
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
