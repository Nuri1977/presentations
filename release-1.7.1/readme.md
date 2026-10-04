# Release roundup — Rosetta DBT Studio 1.6.82 → 1.7.1

Open `presentation-slides.html` in a browser. Every slide is a fixed 1920 × 1080 canvas that scales to the window, so a full-screen recording (press **F**) gives a clean 16:9 frame for CapCut.

## Controls

- **← / →** (or Space): previous / next slide. **Home / End**: first / last slide.
- **T**: open the transcript panel. Show the current slide's narration or **All**, then use **Copy** to paste it into CapCut text-to-speech or captions.
- **H**: hide the progress bar and controls before recording.
- The URL hash tracks the slide (`#7` opens slide 7).

`voice-over-script.txt` contains the same narration with the visual and an estimated duration for each slide. It runs about 740 words, or 5 minutes at 150 words per minute.

## Slides

| # | Release | Topic |
|---|---------|-------|
| 1 | — | Title |
| 2 | all | Release timeline |
| 3 | 1.7.0 | New dashboard and navigation |
| 4–5 | 1.7.0 | Python notebooks |
| 6 | 1.7.0 | Snowflake browser OAuth |
| 7 | 1.7.0 | SQL editor, schema and project fixes |
| 8–9 | 1.7.1 | MySQL connections, dbt-compatibility indicators |
| 10 | 1.7.1 | Schema tree context menu and drag & drop |
| 11 | 1.7.1 | Images in the AI agent chat |
| 12 | 1.7.1 | Iceberg on Windows, header/env fix, Playwright in image |
| 13 | 1.6.83 | dbt-Kinetica adapter |
| 14 | 1.6.82 | ZIP templates, Local Runner setup step, project fixes |
| 15 | — | Download / GitHub CTA (right half left empty for the speaking avatar) |

## Assets

Screenshot filenames start with their slide number. Full-window screenshots were cropped to the app window, without the macOS shadow. `slide-15-rosetta-logo.png` is copied from `../iceberg-step-by-step/assets/icons/`, and `linear-white-bg.svg` from `../analytics-jaffle-shop-demo/assets/`. `slide-07-snowflake-form.png`, `slide-09-mysql-form.png` and `slide-13-kinetica-detail.png` are spare close-ups that the deck doesn't use.

## Accuracy notes

The content comes from the GitHub release notes. A few items had only a PR title to go on, so check them before publishing:

- **dbt-compatibility indicators** (1.7.1, #462): described generally as showing which connection types work with dbt.
- **Header AI icon and environment variables** (1.7.1, #479): described only as a fix.
- **Project picker** (1.7.0, #471): the PR title is cut off, so "takes you directly to the project" is an assumption.
- **Schema tree drag & drop** (1.7.1, #458): the screenshots show the context menu but not dragging.
