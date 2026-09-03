# Lesson 5 - Prompt and Assets Checklist

Lesson 5, "Create the example project", clones the built in Get Started project. The point it has to land is that a beginner gets a real project on screen in about a minute, with no credentials, no cloud account and no database to install, because the database is a DuckDB file that comes with the clone.

Format: screen recording, with full frame cards for the intro and the close. Concept text is composited on top of the footage in CapCut as transparent content cards. Same approach as lessons 1 to 4.

App version at time of production: **1.6.3**, read off the installed exe. The example clones from `https://github.com/rosettadb/dbtstudio_getting_started.git`.

## Assets in this folder

| Path | What it is | Status |
|---|---|---|
| `voiceover-script-85sec.md` | Plain script. Subtitle source. | Done |
| `voiceover-kokoro.txt` | Same words with Kokoro markup. | Done |
| `RECORDING-cue-sheet.md` | Beats, prep, and the dialog note. | Done |
| `video-presentation.html` | Reference deck, six slides. | Done |
| `slides/1.png` | Intro card, full frame. | Done |
| `slides/6.png` | Closing card, full frame. | Done |
| `overlays/1. card-get-started.png` | Content card, bottom right. | Done |
| `overlays/2. card-what-you-get.png` | Content card, bottom left. | Done |
| `overlays/3. card-create.png` | Content card, top right. | Done |
| `overlays/4. card-opens.png` | Content card, bottom right. | Done |
| `sounds/` | Kokoro MP3 per slide. | To generate |
| Screen recording | Get Started through to the project open. | To record |

## Card order

Numbered in the order they go on the timeline. Work down from 1.

## Overlay card placement

Each PNG is a full 1920x1080 frame with the card already positioned. Drop it at 0,0 with scale 100% in CapCut. Do not reposition or rescale.

Card 2 sits bottom left so it clears the Get Started dialog, which opens centred. The other three sit right, clear of the project list and the file explorer.

Fade each card in and out with CapCut Animation on the clip itself. Do not use a Transition between clips, since that dips the whole frame including the footage.

## The dialog claim, deliberately not repeated

The Get Started dialog lists "Sample DBT Models: Ready-to-run transformations showcasing common patterns" and "Example Analytics: Pre-built dashboards and visualizations".

The narration does not repeat either. The cloned repo ships raw data and an empty `models/` folder, which is the whole premise of lessons 6 and 7. Saying the app's line aloud would contradict the next two lessons.

Worth raising with the team as a product accuracy issue, separate from the course.

## Open items

- This lesson must be recorded with no existing `dbtstudio_getting_started` project. Not cosmetic: the Get Started button is hidden while a project of that name is in the list. The cue sheet has the full teardown.
- It needs internet, since it clones from GitHub. The only lesson so far that does.
- Time the clone. If it runs longer than slide 4 allows, ramp it and send the cut points for a refit.
- Audio target is minus 14 LUFS. Lesson 1 exported at minus 28 and needed a normalization pass afterwards.
- Kokoro pronunciation of "dbt" is still unverified across the series.