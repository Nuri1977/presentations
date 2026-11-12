# Lesson 2.6 · Docs & the DAG

dbt + DuckDB in Rosetta DBT Studio · Module 2 · dbt basics. Rendered 2:32, 3840x2160 H.264 + AAC, 38 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-2-6.mp4` | The 4K video for YouTube (not in git) |
| `lesson-2-6-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-2-6.srt`, `lesson-2-6.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-2-6-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- Run: Model ▸ Run +model (Upstream) on monthly_summary; docs: Project ▸ Generate Docs and Project ▸ Serve Docs (dropdown rule, 10 Nov).
- Lineage is shown in the docs site's lineage graph. Studio 1.7.6 showed no LINEAGE tab in the bottom panel in this project.
- Serve Docs: dbt opens the system browser by default. The recording sets BROWSER to a no-op for Studio and opens the docs in the recording browser at 127.0.0.1:8080 (dbt listens on IPv4 only).

## Accuracy notes

- monthly_summary checked off camera on 10 Nov 2026: January 2025 has 45,507 trips, 71.4% paid by card.
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../project-01 ../project-01/lesson-2-6-docs-dag
python3 scripts/tts.py ../project-01 ../project-01/lesson-2-6-docs-dag     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-01 ../project-01/lesson-2-6-docs-dag
python3 scripts/compose.py ../project-01 ../project-01/lesson-2-6-docs-dag
python3 scripts/package.py ../project-01 ../project-01/lesson-2-6-docs-dag
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
