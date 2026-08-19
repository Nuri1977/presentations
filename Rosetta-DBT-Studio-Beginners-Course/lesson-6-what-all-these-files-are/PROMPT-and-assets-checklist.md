# Lesson 6 - Prompt and Assets Checklist

Lesson 6, "What all these files are", walks the project that lesson 5 cloned. The point it has to land is that a dbt project is mostly empty folders on purpose, that the two YAML files are already filled in for you, and that `models` is the only folder the viewer will actually work in.

Format: screen recording, with full frame cards for the intro and the close. Concept text is composited on top of the footage in CapCut as transparent content cards. Same approach as lessons 1 to 5.

App version at time of production: **1.6.3**, read off the installed exe.

## Assets in this folder

| Path | What it is | Status |
|---|---|---|
| `voiceover-script-200sec.md` | Plain script. Subtitle source. | Done |
| `voiceover-kokoro.txt` | Same words with Kokoro markup. | Done |
| `RECORDING-cue-sheet.md` | Beats, prep, and the verified file list. | Done |
| `video-presentation.html` | Reference deck, ten slides. | Done |
| `slides/1.png` | Intro card, full frame. | Done |
| `slides/10.png` | Closing card, full frame. | Done |
| `overlays/1. card-project-file.png` | Content card, bottom right. | Done |
| `overlays/2. card-connection.png` | Content card, bottom right. | Done |
| `overlays/3. card-models.png` | Content card, bottom right. | Done |
| `overlays/4. card-seeds.png` | Content card, bottom right. | Done |
| `overlays/5. card-optional.png` | Content card, bottom right. | Done |
| `overlays/6. card-rosetta.png` | Content card, bottom right. | Done |
| `overlays/7. card-target.png` | Content card, bottom right. | Done |
| `overlays/8. card-where.png` | Content card, bottom right. | Done |
| `sounds/` | Kokoro MP3 per slide, ten of them. | To generate |
| Screen recording | The file tree, plus the two YAML files opened. | To record |

## Card order

Numbered in the order they go on the timeline. Work down from 1. Card N belongs to slide N plus one, since slide 1 is the full frame intro.

## Overlay card placement

Each PNG is a full 1920x1080 frame with the card already positioned. Drop it at 0,0 with scale 100% in CapCut. Do not reposition or rescale.

Everything the viewer looks at in this lesson is in the file tree on the left, so all eight cards sit bottom right. Cards 1 and 2 were originally top right and were moved down, so every card lands in the same place.

Placement was decided before any footage existed. It needs one frame from the real take to confirm, and re-rendering a card is a two minute job.

Fade each card in and out with CapCut Animation on the clip itself. Do not use a Transition between clips, since that dips the whole frame including the footage.

## What is verified, and how

Everything the narration and the cards claim about the project was checked against disk, not against the README.

- The file and folder list, and which folders are empty: read from `C:\Users\Edon\rosetta-dbt-studio-projects\dbtstudio_getting_started`.
- `type: duckdb`, `schema: main`, `threads: 4`: read from `profiles.yml`.
- Four tables, 100 rows each, and the column names: queried directly out of `university_sample.duckdb` with Rosetta's own bundled Python.
- 1.3 MB: the file is 1,323,008 bytes.
- Rosetta deletes `.git` after cloning the example: `src/main/services/git.service.ts`, reached with `removeGit: true` from `GetStartedModal`.
- Rosetta writes `profiles.yml` and `rosetta/main.conf` itself: `src/main/services/connectors.service.ts`.

## No forward references

The narration never says a later lesson will cover something. `models` being empty is explained on its own terms, and the only handoff is the closing line into lesson 7.

## Product issue found while writing this

`dbt_project.yml` sets `analysis-paths: [analyses]` while the folder in the repo is called `analysis`. Harmless today, confusing to a beginner who reads both. Send it to the team alongside the Get Started dialog wording from lesson 5.

## Open items

- Record after lesson 5, with `models/` still empty and no `target/` folder on disk.
- Confirm card placement against one real frame before rendering the rest of the edit.
- Audio target is minus 14 LUFS.
- Kokoro pronunciation of "dbt" and "DuckDB" is still unverified across the series. This script says both often, so it is a good one to test on.
- The script deliberately never says a file name out loud. The cards carry `dbt_project.yml`, `profiles.yml` and `university_sample.duckdb` instead, which keeps the TTS off strings it reads badly and gives the cards something the voice does not do.
