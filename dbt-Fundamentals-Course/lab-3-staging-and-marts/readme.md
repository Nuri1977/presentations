# Lesson Lab 3 · Staging and marts on DuckDB (walkthrough)

dbt Fundamentals · Module 3 · Building models. Rendered 4:36, 3840x2160 H.264 + AAC, 45 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lab-3-walkthrough.mp4` | The 4K video for YouTube (not in git) |
| `lab-3-walkthrough-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lab-3-walkthrough.srt`, `lab-3-walkthrough.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lab-3-walkthrough-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.5 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- The draft has no script for the lab walkthroughs (Appendix C plans them as optional 5 to 8 minute videos), so the narration is written from the Lab 3 steps.
- Step 5.3 runs `select customer_id, first_name, order_count, lifetime_value ... order by lifetime_value desc` instead of `select *`: these are the columns of the lab's Expected result table, and Studio 1.7.5's SQL Editor shows the date column first_order_date as {"days": N} (reported separately).
- Step 5.4 uses the LINEAGE tab, Maximize and Depth 3 to show the whole graph.
- The optional staging-layer generator mentioned in Step 2 is not shown.

## Accuracy notes

- The query result in the video (Ava 3 orders 102, Dmitri 55, Chloe 50, Ben 23, Elena 12, Farid 0) is the real output and matches the lab's Expected result table.
- `dbt run` built 3 view models and 2 table models, PASS=5, as narrated.
- Studio bug seen while preparing: the SQL Editor result grid renders DATE values as {"days": N}.
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../dbt-Fundamentals-Course ../dbt-Fundamentals-Course/lab-3-staging-and-marts
python3 scripts/tts.py ../dbt-Fundamentals-Course ../dbt-Fundamentals-Course/lab-3-staging-and-marts     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../dbt-Fundamentals-Course ../dbt-Fundamentals-Course/lab-3-staging-and-marts
python3 scripts/compose.py ../dbt-Fundamentals-Course ../dbt-Fundamentals-Course/lab-3-staging-and-marts
python3 scripts/package.py ../dbt-Fundamentals-Course ../dbt-Fundamentals-Course/lab-3-staging-and-marts
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
