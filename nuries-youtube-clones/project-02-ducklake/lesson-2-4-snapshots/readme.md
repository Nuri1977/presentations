# Lesson 2.4 · Snapshots: every change is a version

Data Lakes with DuckLake in Rosetta DBT Studio · Module 2 · Your first lake in Studio. Rendered 2:09, 3840x2160 H.264 + AAC, 21 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-2-4.mp4` | The 4K video for YouTube (not in git) |
| `lesson-2-4-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-2-4.srt`, `lesson-2-4.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-2-4-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- The BEGIN … COMMIT block with a commit message is a slide: Studio's SQL Editor runs one statement at a time and rejects BEGIN. Lesson 6.3 sets a commit message live from dbt.

## Accuracy notes

- Snapshots before the lesson: 0 schema main, 1 schema raw, 2 table created (August), 3 and 4 inserts. The insert of 1 Nov 2026 (7,176 blocks) is snapshot 5. Rehearsal 12 Nov 2026.
- set_commit_message(author, message) inside a transaction: DuckLake docs, Snapshots page, checked 11 Nov 2026.
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../project-02-ducklake ../project-02-ducklake/lesson-2-4-snapshots
python3 scripts/tts.py ../project-02-ducklake ../project-02-ducklake/lesson-2-4-snapshots     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-02-ducklake ../project-02-ducklake/lesson-2-4-snapshots
python3 scripts/compose.py ../project-02-ducklake ../project-02-ducklake/lesson-2-4-snapshots
python3 scripts/package.py ../project-02-ducklake ../project-02-ducklake/lesson-2-4-snapshots
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
