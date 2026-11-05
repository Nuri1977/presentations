# Lesson 1.1 · What dbt is (and is not)

dbt Fundamentals · Module 1 · From ETL to ELT: why dbt exists. Rendered 1:18, 3840x2160 H.264 + AAC, 20 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-1-1.mp4` | The 4K video for YouTube (not in git) |
| `lesson-1-1-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-1-1.srt`, `lesson-1-1.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-1-1-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.5 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- The draft's spoken lines are kept, split into one beat per sentence group.
- b14 adds the lesson's "analogy for customers" from the LMS text (dbt is to SQL what a build system is to source code), so the one-sentence definition on the recap slide is on screen long enough to read.
- The draft cues (data flow; three icons for testing, documentation, version control) are kept. Two more slides illustrate "that's a model" and what dbt does not do, using the lesson's dbt does / does not table.

## Accuracy notes

- The model example is plain SQL on purpose; source() and ref() come in Module 3.
- No version-specific claims in this lesson.
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
python3 scripts/tts.py ../dbt-Fundamentals-Course ../dbt-Fundamentals-Course/lesson-1-1-what-dbt-is     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../dbt-Fundamentals-Course ../dbt-Fundamentals-Course/lesson-1-1-what-dbt-is
python3 scripts/compose.py ../dbt-Fundamentals-Course ../dbt-Fundamentals-Course/lesson-1-1-what-dbt-is
python3 scripts/package.py ../dbt-Fundamentals-Course ../dbt-Fundamentals-Course/lesson-1-1-what-dbt-is
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
