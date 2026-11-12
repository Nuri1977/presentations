# Lesson 3.2 · Showcase: docs site, README and a public warehouse

dbt + DuckDB in Rosetta DBT Studio · Module 3 · Ship it. Rendered 2:07, 3840x2160 H.264 + AAC, 38 MB.

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

- Action pins: actions/upload-pages-artifact@v5, actions/deploy-pages@v5 (current majors on 10 Nov 2026).
- README is pasted in full (owner/repo filled in); no DAG image.
- The plan's s05 (attach the release in Studio's SQL Editor) is a slide: in Studio 1.7.6 each SQL Editor run uses a new connection, so an ATTACH does not carry over to the next statement (Binder Error: Catalog taxi does not exist), and only the first statement of a line runs. The query and its result were checked with DuckDB off camera.

## Accuracy notes

- The public attach was checked off camera on 10 Nov 2026: top_pickup_zones from the release prod.duckdb gives 74 East Harlem North, 143,115 trips.
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../project-01 ../project-01/lesson-3-2-showcase
python3 scripts/tts.py ../project-01 ../project-01/lesson-3-2-showcase     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-01 ../project-01/lesson-3-2-showcase
python3 scripts/compose.py ../project-01 ../project-01/lesson-3-2-showcase
python3 scripts/package.py ../project-01 ../project-01/lesson-3-2-showcase
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
