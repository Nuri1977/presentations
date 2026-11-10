# Lesson 1.2 · Git and GitHub

dbt + DuckDB in Rosetta DBT Studio · Module 1 · Set up. Rendered 2:01, 3840x2160 H.264 + AAC, 33 MB.

## Files

| File | What it is |
|---|---|
| `lesson.yaml` | **The source.** Edit this, then re-render |
| `slides.html` | Slide scenes (open in a browser: arrows step through builds) |
| `lesson-1-2.mp4` | The 4K video for YouTube (not in git) |
| `lesson-1-2-1080p.mp4` | 1080p copy for phones and sharing (not in git) |
| `lesson-1-2.srt`, `lesson-1-2.vtt` | Captions, one cue per sentence |
| `voiceover-script.md` | Beat sheet with measured start times |
| `voiceover-kokoro.txt` | Exact spoken forms sent to the voice |
| `RECORDING-cue-sheet.md` | Steps for a human retake of the app scenes |
| `lesson-1-2-slides.pptx` | One image per slide state, narration in speaker notes (not in git) |
| `youtube.md`, `thumbnail.png` | Upload package |
| `timeline.json` | Start and length of every scene and beat |
| `render/` | Frames, audio and intermediates; kept only on the machine that rendered (not in git) |

## Versions

Rosetta DBT Studio 1.7.6 (official release), dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17. Voice: Kokoro `af_heart` at 1.0.

## Changes from the draft

- Rehearsal cut: creates Nuri1977/nyc-taxi-dbt-rehearsal (Private). The final take creates Nuri1977/nyc-taxi-dbt (Public) after the placeholder repo is deleted; narration b08 changes with it.
- The scene starts on the public rosettadb/dbt-studio page (not the GitHub dashboard), so no personal repositories or activity appear on screen.
- The plan's token page mock is a short slide; creating and storing the token happens off camera, by Nuri, after this lesson.

## Accuracy notes

- GitHub does not accept account passwords for Git over HTTPS; it needs a personal access token (or SSH key). Fine-grained tokens can be limited to one repository with Contents and Workflows permissions (checked on the token page, 9 Nov 2026).
- Listen once for pronunciation (see `voiceover-kokoro.txt` for the exact spoken forms).

## Re-render

```sh
cd ../../_academy-video-tooling
NODE_PATH=$(npm root -g) ./run-headless.sh record.cjs ../project-01 ../project-01/lesson-1-2-git-github
python3 scripts/tts.py ../project-01 ../project-01/lesson-1-2-git-github     # --human to use voice-human/<beat>.wav
python3 scripts/render_stills.py ../project-01 ../project-01/lesson-1-2-git-github
python3 scripts/compose.py ../project-01 ../project-01/lesson-1-2-git-github
python3 scripts/package.py ../project-01 ../project-01/lesson-1-2-git-github
```

Only the narration changed: skip `record.cjs`. Only a slide changed: run `render_stills.py`, `compose.py`, `package.py`.
