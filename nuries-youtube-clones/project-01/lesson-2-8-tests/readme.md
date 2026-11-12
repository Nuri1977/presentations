# Lesson 2.8 · Tests: trust your data

dbt + DuckDB in Rosetta DBT Studio · Module 2 · dbt basics. Rendered 2:32, 3840x2160 H.264 + AAC, 44 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-2-8.mp4` | The 4K video for YouTube (not in git) |
| `lesson-2-8-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-2-8.srt`, `lesson-2-8.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-2-8-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- The deliberate failure is the plan's own accepted_values list: it misses 'N/A', which the 2025 data has (zone 265, Outside of NYC, 255 trips). The failing rows are explained with a card rather than the SQL Editor.
- Dropdowns: Project ▸ Test, Model ▸ Test on trips_per_month, Project ▸ Build.
- accepted_values takes its list under arguments: on dbt Core 1.12.6 (parses with no warning).

## Accuracy notes

- Checked off camera on 10 Nov 2026: first dbt test gives PASS=6 ERROR=1 (accepted_values, Got 1 result); after adding 'N/A', dbt build gives PASS=12 (1 seed, 4 models, 7 tests). Boroughs in trips_per_month: Manhattan, Queens, Brooklyn, Bronx, Unknown, N/A, Staten Island, EWR.
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../project-01 ../project-01/lesson-2-8-tests
python3 scripts/tts.py ../project-01 ../project-01/lesson-2-8-tests     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-01 ../project-01/lesson-2-8-tests
python3 scripts/compose.py ../project-01 ../project-01/lesson-2-8-tests
python3 scripts/package.py ../project-01 ../project-01/lesson-2-8-tests
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
