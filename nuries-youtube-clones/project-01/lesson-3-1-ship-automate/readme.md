# Lesson 3.1 · Ship & Automate: CI with GitHub Actions

dbt + DuckDB in Rosetta DBT Studio · Module 3 · Ship it. Rendered 3:13, 3840x2160 H.264 + AAC, 43 MB.

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

- Action pins updated to the current majors (checked 10 Nov 2026): actions/checkout@v7, actions/setup-python@v7. Python 3.10 in CI to match Studio's runtime (3.10.17).
- The separate dbt seed step is left out: dbt build runs the seed.
- requirements.txt and ci/profiles.yml are typed; download_data.py and the workflow are pasted (plan D8).
- Final run: the workflow runs in the public Nuri1977/nyc-taxi-dbt.

## Accuracy notes

- scripts/download_data.py also loads raw.green_trips into the DuckDB file at DUCKDB_PATH (plan change of 10 Nov afternoon); checked off camera: loaded 591375 rows, dbt build PASS=12.
- ci/profiles.yml + DUCKDB_PATH checked off camera on 10 Nov 2026: dbt build --profiles-dir ci gives PASS=12 and writes prod.duckdb.
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../project-01 ../project-01/lesson-3-1-ship-automate
python3 scripts/tts.py ../project-01 ../project-01/lesson-3-1-ship-automate     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-01 ../project-01/lesson-3-1-ship-automate
python3 scripts/compose.py ../project-01 ../project-01/lesson-3-1-ship-automate
python3 scripts/package.py ../project-01 ../project-01/lesson-3-1-ship-automate
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
