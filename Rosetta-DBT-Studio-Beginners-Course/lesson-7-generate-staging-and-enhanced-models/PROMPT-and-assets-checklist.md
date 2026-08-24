# Lesson 7 - Prompt and Assets Checklist

Lesson 7, "Generate staging and enhanced models", fills the empty models folder using Rosetta's three layer commands. The point it has to land is that the generated files are ordinary SQL, that the three passes must run in order because each reads the last one's output, and that the enhanced layer arrives unfinished and has to be completed by hand.

Format: screen recording, with full frame cards for the intro and the close. Concept text is composited on top of the footage in CapCut as transparent content cards. Same approach as lessons 1 to 6.

App version at time of production: **1.6.3**, read off the installed exe. Rosetta CLI 2.10.0, dbt-core 1.12.0, dbt-duckdb 1.10.1.

## The Windows launcher is repaired

The corrupted `rosetta.bat` blocked all three layer buttons. It has been fixed on this machine and verified through the exact call the app makes, so the lesson is recordable. The original is kept as `rosetta.bat.broken-backup`.

The repair is local. The Rosetta CLI zip still ships the broken file, so this stays on the report-to-the-team list, and the fix has to be reapplied if Rosetta is reinstalled or updated.

## Assets in this folder

| Path | What it is | Status |
|---|---|---|
| `voiceover-script-240sec.md` | Plain script. Subtitle source. | Done |
| `voiceover-kokoro.txt` | Same words with Kokoro markup. | Done |
| `RECORDING-cue-sheet.md` | Beats, prep, the two edits, and the blocker. | Done |
| `video-presentation.html` | Reference deck, ten slides. | Done |
| `slides/1.png` | Intro card, full frame. | Done |
| `slides/10.png` | Closing card, full frame. | Done |
| `overlays/1. card-project-menu.png` | Content card, bottom right. | Done |
| `overlays/2. card-raw-layer.png` | Content card, bottom right. | Done |
| `overlays/3. card-sources.png` | Content card, top right, under the Save button. | Done |
| `overlays/4. card-staging-picker.png` | Content card, bottom right, narrow square. | Done |
| `overlays/5. card-staging-views.png` | Content card, bottom right. | Done |
| `overlays/6. card-why-not-students.png` | Content card, bottom right, narrow square. | Done |
| `overlays/7. card-placeholders.png` | Content card, top right, under the Save button. | Done |
| `overlays/8. card-first-run.png` | Content card, bottom right. | Done |
| `sounds/` | Kokoro MP3 per slide, ten of them. | To generate |
| Screen recording | Three generates, then two edits. | To record |

## Overlay card placement

Each PNG is a full 1920x1080 frame with the card already positioned. Drop it at 0,0 with scale 100% in CapCut. Do not reposition or rescale.

All eight sit on the **right**. Nothing is on the left any more, because the file tree lives there and every beat in this lesson happens in it.

Cards 3 and 7 sit **top right, below the Save button**, since on those two slides a file is open in the editor and the lower half is where you are reading.

Cards 4 and 6 are **narrow squares, 300 px wide instead of 380**. Those two land while a Rosetta dialog is open. The dialogs are centred and run to about x 1527, so a 380 wide card starting at 1448 overlaps them; a 300 wide card starts at 1528 and clears them exactly. Squaring them up was also a legibility call, since both carry longer copy than the rest.

Measured positions, from the rendered PNGs rather than the stylesheet:

| Card | Box | Size |
|---|---|---|
| 1, 8 | x 1448-1828, y 712-972 | 380x260 |
| 2, 5 | x 1448-1828, y 736-972 | 380x236 |
| 3, 7 | x 1448-1828, y 190-450 | 380x260 |
| 4 | x 1528-1828, y 677-972 | 300x295 |
| 6 | x 1528-1828, y 664-972 | 300x308 |

Positions were confirmed against real frames on 17 Aug 2026, including shots with the Staging and Incremental dialogs open, and every card was re-rendered to match. The numbers above are measured from those PNGs.

Fade each card with CapCut Animation on the clip itself, never a Transition.

## What is verified, and how

Every claim in this lesson came from running the real commands, not from the README or the UI copy. The Rosetta CLI was invoked through its Java entry point, `com.adaptivescale.rosetta.cli.Main`, with the same arguments the app builds in `utils.ts:377`, because the Windows `.bat` wrapper is broken.

- Menu contents and the three commands: `ProjectDbtSplitButton.tsx:105-186`.
- Default output paths `models/raw`, `models/staging`, `models/enhanced`: same file, lines 80-102.
- The picker is limited to one models subfolder per run: `stagingModal/index.tsx:158-232`.
- Raw writes sources with `not_null` on every column, staging writes passthrough selects, enhanced writes incremental models with placeholders: read off disk after running each.
- Timings 4.4s, 1.5s, 1.4s: measured.
- Staging does not run extract first: no extract step appeared in its output.
- 16 data tests, all passing: `dbt test`.
- The second `dbt run` fails on the placeholders, first one passes: ran it both ways.

## The editorial call on the enhanced layer

Rosetta will happily generate enhanced models for all four tables, and that leaves the viewer with a project that breaks the second time they run it. The lesson generates enhanced for **grades only**, and says why.

An earlier draft did students as well, using `enrollment_year` as the watermark. That was dropped: it is a year, not a timestamp, so a strict `>` silently misses anyone enrolling in the same year as the current maximum. Teaching a subtly wrong incremental pattern in a beginner course is worse than teaching one table properly. The nuance survives as card 6, which is where the objection belongs.

## No forward references

Nothing points at a later lesson. The placeholders are explained and fixed inside this lesson rather than deferred, and the only handoff is the closing line into lesson 8.

## Open items

- Record straight after lesson 6, from an empty `models/`.
- ~~Reapply the `rosetta.bat` repair if Rosetta is reinstalled or updated before the shoot.~~ Re-verified 12 Aug 2026 after the app went to 1.6.3: still intact, `--version` returns 2.10.0 through the app's own call path. Only a reinstall of the **CLI** would wipe it, not an app update.
- ~~Confirm card placement against one frame with a dialog open.~~ Done 17 Aug 2026. Cards 3 and 7 moved to top right under Save, cards 4 and 6 narrowed to 300 px squares and moved bottom right so they clear the dialogs, and nothing sits over the file tree any more.
- Audio target is minus 14 LUFS.
- Kokoro pronunciation of "dbt" and "SQL" still unverified. This script says "dbt" nine times.
- The script says no file names out loud. Cards carry `models/raw`, `UNIQUE_KEY_COLUMNS` and `INCREMENTAL_COLUMN`.
