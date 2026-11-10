# Lesson 0 · Welcome: build a dbt + DuckDB project

dbt + DuckDB in Rosetta DBT Studio · Welcome. Rendered 3:00, 3840x2160 H.264 + AAC, 44 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-0.mp4` | The 4K video for YouTube (not in git) |
| `lesson-0-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-0.srt`, `lesson-0.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-0-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- Merges the plan's Lesson 1.1 (project and data) into the new Lesson 0, as agreed on 9 Nov 2026. Lesson 0 is recorded first, so the finished project is drawn on slides instead of shown in Studio.
- Adds how to use the course repo: one public repository, one commit per lesson (changed 10 Nov 2026 from one pull request per lesson). Git and GitHub basics are assumed.

## Accuracy notes

- Data measured on 9 Nov 2026 from the TLC 2025 Green Taxi files downloaded that day: 12 files, 14.5 MB in total (1.1 to 1.3 MB each), 591,375 rows. Taxi zone lookup: 265 zones.
- Busiest 2025 pickup zone in these files: 74, East Harlem North, Manhattan (145,092 pickups).
- Rosetta DBT Studio is open source under AGPL-3.0 (LICENSE in rosettadb/dbt-studio); releases exist for Mac, Windows and Linux (1.7.6 assets).
- Course repo github.com/Nuri1977/nyc-taxi-dbt does not exist yet; the slide shows its planned address.
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
python3 scripts/tts.py ../project-01 ../project-01/lesson-0-welcome     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-01 ../project-01/lesson-0-welcome
python3 scripts/compose.py ../project-01 ../project-01/lesson-0-welcome
python3 scripts/package.py ../project-01 ../project-01/lesson-0-welcome
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
