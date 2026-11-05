# Lesson 3.2 · Models, ref() and the DAG

dbt Fundamentals · Module 3 · Building models. Rendered 2:54, 3840x2160 H.264 + AAC, 39 MB.

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

Rosetta DBT Studio 1.7.5 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- The draft's spoken lines are kept. Demo lines were added for the app scenes (opening stg_orders, writing fct_orders, Compile, the compiled copy, Lineage).
- b06 mentions source() and defers it to Lesson 3.3.
- b22 adds what "directed" and "acyclic" mean (matches the lesson's quiz answer).
- The draft cue "lineage graph appears as models are added" is shown with Studio's LINEAGE tab at depth 1 and 2 rather than a growing diagram; the DAG slide builds the graph instead.

## Accuracy notes

- `ref('stg_orders')` compiling to `"course"."main"."stg_orders"` is the real compiled output (target/compiled).
- The `prod` line on the ref slide is an illustrative example and is marked as one.
- Lineage at depth 2 showing the sources `orders` and `payments` was verified in this recording.
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../dbt-Fundamentals-Course ../dbt-Fundamentals-Course/lesson-3-2-models-ref-dag
python3 scripts/tts.py ../dbt-Fundamentals-Course ../dbt-Fundamentals-Course/lesson-3-2-models-ref-dag     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../dbt-Fundamentals-Course ../dbt-Fundamentals-Course/lesson-3-2-models-ref-dag
python3 scripts/compose.py ../dbt-Fundamentals-Course ../dbt-Fundamentals-Course/lesson-3-2-models-ref-dag
python3 scripts/package.py ../dbt-Fundamentals-Course ../dbt-Fundamentals-Course/lesson-3-2-models-ref-dag
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
