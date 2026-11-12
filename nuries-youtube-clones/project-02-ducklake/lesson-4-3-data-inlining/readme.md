# Lesson 4.3 · Data inlining for small writes

Data Lakes with DuckLake in Rosetta DBT Studio · Module 4 · Performance and upkeep. Rendered 1:58, 3840x2160 H.264 + AAC, 17 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-4-3.mp4` | The 4K video for YouTube (not in git) |
| `lesson-4-3-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-4-3.srt`, `lesson-4-3.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-4-3-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- Inlining is switched on for one table with set_option(…, schema => 'raw', table_name => 'watchlist') instead of a WITH clause on CREATE TABLE.

## Accuracy notes

- Two rows inserted with a table limit of 100: 0 data files; after ducklake_flush_inlined_data: 1 file, 2 rows flushed. Rehearsed with DuckDB 1.5.2 (ducklake 415a9ebd), 12 Nov 2026.
- Addresses: 0x00000000219ab540356cbb839cbe05303d7705fa is the Ethereum staking deposit contract; 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2 is WETH (wrapped ether).
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../project-02-ducklake ../project-02-ducklake/lesson-4-3-data-inlining
python3 scripts/tts.py ../project-02-ducklake ../project-02-ducklake/lesson-4-3-data-inlining     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-02-ducklake ../project-02-ducklake/lesson-4-3-data-inlining
python3 scripts/compose.py ../project-02-ducklake ../project-02-ducklake/lesson-4-3-data-inlining
python3 scripts/package.py ../project-02-ducklake ../project-02-ducklake/lesson-4-3-data-inlining
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
