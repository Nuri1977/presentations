# AI Agentic dbt Development: slides

Fourteen HTML decks, one per section of `COURSE-PLAN.md`, each with a talk track behind every slide. Open `index.html` to start.

## Presenting

1. Open a section, for example `s05-staging-models.html`, in Chrome.
2. Press **P**. A presenter window opens with the current slide, the next slide, the talk track ("Say"), the on-screen actions ("On screen") and a timer. The two windows stay in sync.
3. Share **only the slides window** in your recorder, and press **F** for fullscreen.

| Key | Action |
|---|---|
| → / Space, ← | Next / previous slide |
| Home / End | First / last slide |
| P | Presenter window |
| N | Notes drawer in the slides window (for rehearsal, not for recording) |
| S | Script view: every slide with its notes. Print it with Ctrl/Cmd + P |
| T | Light / dark theme |
| F | Fullscreen |
| ? | Keyboard help |

## Before recording

- **Real-data numbers.** Slides marked "Real-data moment" show amber `?` placeholders. After your dry run, click each one, type your number and press Esc. The numbers are saved in this browser for that deck.
- **Logo.** Put `logo_hero.svg` in this folder and it appears on every title slide. Without it, nothing is shown.
- **Fonts.** The decks load Inter and JetBrains Mono from Google Fonts and fall back to system fonts when offline.
- Every slide is designed at 1920×1080 and scales to the window. Record at 1080p.

## Editing the text

The decks are generated. To change a slide or its notes, edit `_source/content_a.py` (S00–S04), `content_b.py` (S05–S08) or `content_c.py` (S09–S13), then run:

```sh
cd _source
python3 build.py ..
```

`engine.css` and `engine.js` hold the shared design and the presenter logic.
