# Lesson 1.5 · The Ethereum data: blocks, transactions, gas

Data Lakes with DuckLake in Rosetta DBT Studio · Module 1 · Data lakes explained. Rendered 1:44, 3840x2160 H.264 + AAC, 18 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-1-5.mp4` | The 4K video for YouTube (not in git) |
| `lesson-1-5-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-1-5.srt`, `lesson-1-5.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-1-5-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- The browser shows the dataset's page on the AWS Open Data registry instead of the raw bucket listing (an XML page).

## Accuracy notes

- 1 October 2026 (from the bucket): 7,176 blocks (00:00:11 to 23:59:59), 284 transactions per block on average, average base fee 0.639 gwei, blocks 50.5% full, gas limit 60 million; 2,036,041 transactions, 98.9% succeeded. Measured 12 Nov 2026.
- 1 ether = 10^18 wei; 1 gwei = 10^9 wei (ethereum.org).
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../project-02-ducklake ../project-02-ducklake/lesson-1-5-ethereum-data
python3 scripts/tts.py ../project-02-ducklake ../project-02-ducklake/lesson-1-5-ethereum-data     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-02-ducklake ../project-02-ducklake/lesson-1-5-ethereum-data
python3 scripts/compose.py ../project-02-ducklake ../project-02-ducklake/lesson-1-5-ethereum-data
python3 scripts/package.py ../project-02-ducklake ../project-02-ducklake/lesson-1-5-ethereum-data
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
