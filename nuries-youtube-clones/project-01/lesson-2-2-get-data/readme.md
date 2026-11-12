# Lesson 2.2 · Get the data

dbt + DuckDB in Rosetta DBT Studio · Module 2 · dbt basics. Rendered 3:17, 3840x2160 H.264 + AAC, 37 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-2-2.mp4` | The 4K video for YouTube (not in git) |
| `lesson-2-2-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-2-2.srt`, `lesson-2-2.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-2-2-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- The plan downloaded the files on camera from the TLC page. The TLC site refuses automated browsers (Access Denied), so the download is a slide with the page path and the file links, and the links go in the YouTube description.
- Raw data is loaded into DuckDB (raw.green_trips) from the SQL Editor instead of a source with external_location over a relative path: Studio's Preview, Query Results and SQL Editor run DuckDB outside the project folder and cannot read relative paths (plan change of 10 Nov afternoon). The load uses the full path of the learner's data/raw folder.
- Push: after the commit Studio's Git tab offers Sync Changes (1↑), which pushes to origin/main.

## Accuracy notes

- Rows: 591,375 in green_tripdata_2025-01..12 (files downloaded 9 Nov 2026), counted in Studio's SQL Editor on 10 Nov 2026.
- taxi_zone_lookup.csv: 265 zones (LocationID, Borough, Zone, service_zone).
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../project-01 ../project-01/lesson-2-2-get-data
python3 scripts/tts.py ../project-01 ../project-01/lesson-2-2-get-data     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-01 ../project-01/lesson-2-2-get-data
python3 scripts/compose.py ../project-01 ../project-01/lesson-2-2-get-data
python3 scripts/package.py ../project-01 ../project-01/lesson-2-2-get-data
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
