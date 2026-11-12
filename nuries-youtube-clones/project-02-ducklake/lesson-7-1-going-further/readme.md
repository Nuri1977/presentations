# Lesson 7.1 · Going further, and recap

Data Lakes with DuckLake in Rosetta DBT Studio · Module 7 · Wrap-up. Rendered 1:45, 3840x2160 H.264 + AAC, 15 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-7-1.mp4` | The 4K video for YouTube (not in git) |
| `lesson-7-1-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-7-1.srt`, `lesson-7-1.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-7-1-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- The shared-lake slide mentions the tested S3-compatible storage (RustFS) result and that a later tutorial covers PostgreSQL with cloud S3.

## Accuracy notes

- PostgreSQL catalog ATTACH form, access control, backups, encryption, migration and unsupported features from the DuckLake docs, checked 11 Nov 2026.
- DuckLake on S3-compatible storage (RustFS) works from DuckDB and dbt with an S3 secret (endpoint, USE_SSL false, URL_STYLE path); Studio 1.7.6's DuckLake wizard cannot use it yet (studio-notes.md, 11 Nov 2026).
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
python3 scripts/tts.py ../project-02-ducklake ../project-02-ducklake/lesson-7-1-going-further     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-02-ducklake ../project-02-ducklake/lesson-7-1-going-further
python3 scripts/compose.py ../project-02-ducklake ../project-02-ducklake/lesson-7-1-going-further
python3 scripts/package.py ../project-02-ducklake ../project-02-ducklake/lesson-7-1-going-further
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
