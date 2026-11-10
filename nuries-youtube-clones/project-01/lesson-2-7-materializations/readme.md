# Lesson 2.7 · Materializations: views and tables

dbt + DuckDB in Rosetta DBT Studio · Module 2 · dbt basics. Rendered 2:03, 3840x2160 H.264 + AAC, 34 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-2-7.mp4` | The 4K video for YouTube (not in git) |
| `lesson-2-7-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-2-7.srt`, `lesson-2-7.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-2-7-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- The plan's s02 queried information_schema before the change. Studio's SQL Editor holds the DuckDB file open, which can block dbt's write, so the lesson changes the config and runs first, then queries once; the slide shows the before state (all views).
- +materialized: table is added at the end of the nyc_taxi block (after +persist_docs), the same settings as plan A8 in a different order.

## Accuracy notes

- Checked off camera on 10 Nov 2026: after the change, trips is VIEW; trips_per_month, top_pickup_zones and monthly_summary are BASE TABLE; the seed taxi_zone_lookup is BASE TABLE.
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../project-01 ../project-01/lesson-2-7-materializations
python3 scripts/tts.py ../project-01 ../project-01/lesson-2-7-materializations     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-01 ../project-01/lesson-2-7-materializations
python3 scripts/compose.py ../project-01 ../project-01/lesson-2-7-materializations
python3 scripts/package.py ../project-01 ../project-01/lesson-2-7-materializations
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
