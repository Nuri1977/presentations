# Lesson 3 - Prompt and Assets Checklist

Lesson 3, "Installing Rosetta DBT Studio", walks through downloading the app, installing it, and opening it for the first time. The point it has to land is that Rosetta brings its own Python and installs dbt for you, so there is no terminal work and no dependency wrangling.

Structure: two complete walkthroughs rather than one platform-agnostic pass. Windows start to finish, a full frame divider card, then Mac start to finish. A viewer follows their own platform without mentally filtering shots that do not apply to them.

Format: screen recording, with full frame cards for the intro, the platform divider and the close. Concept text is composited on top of the footage in CapCut as transparent content cards. Same approach as lessons 1 and 2.

App version at time of production: 1.6.1, released 24 July 2026. Download source: rosettadb.io, via Download Now then Choose your build, which shows a card each for Windows, Linux and macOS. The README points at the GitHub releases page instead, but the site is the path a beginner actually takes.

## Assets in this folder

| Path | What it is | Status |
|---|---|---|
| `voiceover-script-170sec.md` | Plain script. Subtitle source. | Done |
| `voiceover-kokoro.txt` | Same words with Kokoro markup. | Done |
| `RECORDING-cue-sheet.md` | Both passes, prep, and retake notes. | Done |
| `video-presentation.html` | Reference deck, fourteen slides. | Done |
| `slides/1.png` | Intro card, full frame. | Done |
| `slides/7.png` | Mac divider card, full frame. | Done |
| `slides/14.png` | Closing card, full frame. | Done |
| `overlays/windows/1. card-download-win.png` | Content card, bottom right. | Done |
| `overlays/windows/2. card-install-win.png` | Content card, bottom left. | Done |
| `overlays/windows/3. card-setup.png` | Content card, bottom left. | Done |
| `overlays/windows/4. card-finish.png` | Content card, bottom right. | Done |
| `overlays/windows/5. card-tour.png` | Content card, bottom right. | Done |
| `overlays/mac/1. card-download-mac.png` | Content card, bottom right. | Done |
| `overlays/mac/2. card-install-mac.png` | Content card, top right. | Done |
| `overlays/mac/3. card-first-open.png` | Mac only. What first launch is doing behind the splash. Filename kept as `first-open` because it is already placed in CapCut. | Done |
| `overlays/mac/4. card-setup.png` | Mac only now. Says Setup Wizard, not First Launch, so it does not collide with card 3. | Done |
| `overlays/mac/5. card-finish.png` | Same card as the Windows pass. | Done |
| `overlays/mac/6. card-tour.png` | Same card as the Windows pass. | Done |
| `sounds/` | Kokoro MP3 per slide, fourteen of them. | Slides 1 to 7 done, **8 to 14 need regenerating** |
| Windows recording | Download, install, first launch. | To record |
| Mac recording | Two dmg files, drag to Applications, brief wizard. | To record |

## Card order

Cards are split into `overlays/windows` and `overlays/mac`, and numbered in the order they go on the timeline. Use the folder for the pass you are editing and work down from 1.

The setup, finish and tour cards are byte identical in both folders. Those three screens are the same on either platform, and repeating the same card reinforces that rather than implying a difference.

## Overlay card placement

Each PNG is a full 1920x1080 frame with the card already positioned. Drop it at 0,0 with scale 100% in CapCut. Do not reposition or rescale.

Corners were chosen so a card never covers what the narration points at. Bottom left is the safe corner whenever a Rosetta panel is open, since the app's chat and detail panels sit on the right.

Fade each card in and out with CapCut Animation on the clip itself. Do not use a Transition between clips, since that dips the whole frame including the footage.

## Open items

- The Mac pass needs a Mac. Two beats genuinely differ, so the footage is short.
- The published 1.6.1 installer predates the Electron 31.7.6 pin, since the release is dated 24 July and the fix merged 29 July. An antivirus false positive on camera is likely. Ask whether a newer build can be published before filming.
- Kokoro pronunciation of "rosettadb.io" is marked up in the Kokoro script but untested. Check it on the first generation, since the URL is spoken in the second line of the lesson.
- `feature/dbt-core-v2-support` merged after this was written and may change the adapter step. Re-check the wizard before recording.
- Audio target is minus 14 LUFS. Lesson 1 exported at minus 28 and needed a normalization pass afterwards.
- Kokoro pronunciation of "dbt" is still unverified across the series.