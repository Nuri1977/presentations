# Lesson Welcome · About this course

dbt Fundamentals · Course landing page. Rendered 1:22, 3840x2160 H.264 + AAC, 23 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `course-welcome.mp4` | The 4K video for YouTube (not in git) |
| `course-welcome-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `course-welcome.srt`, `course-welcome.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `course-welcome-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.5 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- Two long sentences are split for the voice: "dbt works out the order ... and gives your team the same workflow" and "In this course you will learn ... your own organization" ("also" added to the second half).
- The draft cue "course title card, then a simple before/after diagram" is kept; three more slides illustrate the rest of the script, one of them with a real Rosetta DBT Studio 1.7.5 screenshot from the Lesson 3.2 recording.
- Course facts on the title card use the curriculum: 26 lessons, 6 labs and a capstone (the draft's landing text says "7 labs and a capstone", see draft-corrections.md).

## Accuracy notes

- "dbt is the most widely adopted answer" is the draft's claim and was not checked.
- The licensing split on the versions slide (dbt v1 and dbt OSS Apache 2.0, dbt v2 free but proprietary under the dbt Product Licensing Agreement, dbt platform paid) was checked against docs.getdbt.com/docs/dbt-licensing (updated 23 Oct 2026) on 5 Nov 2026.
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
python3 scripts/tts.py ../dbt-Fundamentals-Course ../dbt-Fundamentals-Course/lesson-0-about-this-course     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../dbt-Fundamentals-Course ../dbt-Fundamentals-Course/lesson-0-about-this-course
python3 scripts/compose.py ../dbt-Fundamentals-Course ../dbt-Fundamentals-Course/lesson-0-about-this-course
python3 scripts/package.py ../dbt-Fundamentals-Course ../dbt-Fundamentals-Course/lesson-0-about-this-course
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
