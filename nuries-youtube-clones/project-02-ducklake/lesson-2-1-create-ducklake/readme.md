# Lesson 2.1 · Create a DuckLake in Studio

Data Lakes with DuckLake in Rosetta DBT Studio · Module 2 · Your first lake in Studio. Rendered 4:21, 3840x2160 H.264 + AAC, 40 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-2-1.mp4` | The 4K video for YouTube (not in git) |
| `lesson-2-1-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-2-1.srt`, `lesson-2-1.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-2-1-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- The Studio project is a dbt project from the start (Studio's template), with its own small DuckDB connection; Module 6 points dbt at the lake. The lake lives in the project's lake/ folder, which git ignores.
- Studio 1.7.6 offers only the DuckDB catalog (SQLite and PostgreSQL say Soon), and the catalog file must end in .duckdb or .db: lake/eth_catalog.duckdb.
- The SQL the wizard stands for (INSTALL, ATTACH, USE) is a slide: Studio's SQL Editor does not accept ATTACH or USE.

## Accuracy notes

- Wizard steps and field names, the instance page tabs and the snapshot 0 row checked in Studio 1.7.6 on 11 Nov 2026 (studio-notes.md).
- A new lake has one snapshot, number 0, which creates the schema main.
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../project-02-ducklake ../project-02-ducklake/lesson-2-1-create-ducklake
python3 scripts/tts.py ../project-02-ducklake ../project-02-ducklake/lesson-2-1-create-ducklake     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-02-ducklake ../project-02-ducklake/lesson-2-1-create-ducklake
python3 scripts/compose.py ../project-02-ducklake ../project-02-ducklake/lesson-2-1-create-ducklake
python3 scripts/package.py ../project-02-ducklake ../project-02-ducklake/lesson-2-1-create-ducklake
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
