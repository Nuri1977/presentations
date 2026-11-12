# Lesson 3.3 · Schema evolution

Data Lakes with DuckLake in Rosetta DBT Studio · Module 3 · Changing data. Rendered 2:11, 3840x2160 H.264 + AAC, 21 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-3-3.mp4` | The 4K video for YouTube (not in git) |
| `lesson-3-3-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-3-3.srt`, `lesson-3-3.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-3-3-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- No type change in the demo: transaction_count and size are already BIGINT in this data; type promotion is on the slide.
- COMMENT ON is not run: Studio's SQL Editor rejects it.

## Accuracy notes

- Snapshots: 12 add column, 13 update (7,176 rows), 14 rename, 15 set not null. AT (VERSION => 11) still has the column miner. Rehearsal 12 Nov 2026.
- In the catalog, the renamed column keeps its column id (two rows in ducklake_column: miner 2→14, fee_recipient from 14). Seen again in 5.1.
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../project-02-ducklake ../project-02-ducklake/lesson-3-3-schema-evolution
python3 scripts/tts.py ../project-02-ducklake ../project-02-ducklake/lesson-3-3-schema-evolution     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-02-ducklake ../project-02-ducklake/lesson-3-3-schema-evolution
python3 scripts/compose.py ../project-02-ducklake ../project-02-ducklake/lesson-3-3-schema-evolution
python3 scripts/package.py ../project-02-ducklake ../project-02-ducklake/lesson-3-3-schema-evolution
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
