# Lesson 11 - Prompt and Assets Checklist

Lesson 11, "Lineage and the build order", closes the loop opened in lesson 8. The point it has to land is that the graph is inferred from `source()` and `ref()` alone, that it is read from the compiled manifest rather than from the SQL files, and that the shape of the graph is the reason the run behaved as it did.

Format: screen recording, with full frame cards for the intro and the close. Concept text is composited on top of the footage in CapCut as transparent content cards. Same approach as lessons 1 to 10.

App version at time of production: **1.7.3**.

## Assets in this folder

| Path | What it is | Status |
|---|---|---|
| `voiceover-script-170sec.md` | Plain script. Subtitle source. | Done |
| `voiceover-kokoro.txt` | Same words with Kokoro markup. | Done |
| `RECORDING-cue-sheet.md` | Beats, the real graph, and the depth note. | Done |
| `video-presentation.html` | Reference deck, ten slides. | Done |
| `slides/1.png` | Intro card, full frame. | Done |
| `slides/10.png` | Closing card, full frame. | Done |
| `overlays/1. card-lineage.png` | Content card, top right. | Done |
| `overlays/2. card-the-manifest.png` | Content card, top right. | Done |
| `overlays/3. card-reading-it.png` | Content card, top right. | Done |
| `overlays/4. card-arrows.png` | Content card, top right. | Done |
| `overlays/5. card-two-hop.png` | Content card, top right. | Done |
| `overlays/6. card-depth.png` | Content card, top right. | Done |
| `overlays/7. card-build-order.png` | Content card, top right. | Done |
| `overlays/8. card-why-it-matters.png` | Content card, top right. | Done |
| `sounds/` | Kokoro MP3 per slide, ten of them. | To generate |
| Screen recording | Two models, one depth change, one maximize. | To record |

## Overlay card placement

All eight at the top right, in the blank editor area, so none of them cover the file tree on the left. The lineage graph is in the bottom panel, so a bottom card would land on the thing being described.

Each PNG is a full 1920x1080 frame. Drop it at 0,0 with scale 100%. Fade with CapCut Animation on the clip, never a Transition.

## What is verified, and how

- The graph itself, every edge and every depth: read out of `target/manifest.json` after lesson 8's run, via `parent_map` and `child_map`.
- 21 nodes, 5 models, 16 tests, 4 sources, manifest schema v12, file size 638 KB: same source.
- Depth defaults to 1 with options 1, 2, 3, 4: `components/lineage/LineageToolbar.tsx:22` and `config/constants.ts:166-172`.
- Default orientation left to right: `constants.ts:170`.
- The LINEAGE tab only exists while a `.sql` model is open, so it is not visible with nothing selected: `components/terminal/index.tsx:127-131`. That is why the take opens `main_students.sql` before touching the tab. The "Select a model before opening lineage" message in `LineageView.tsx:296` is therefore not part of the take.
- The "dbt Manifest Not Found" state: `components/lineage/LineageView.tsx:215-240`. Only appears if a `.sql` model is open and `target/manifest.json` is missing. It tells you to run `dbt compile` or `dbt run` and has **no** button. The Refresh Manifest button belongs to a different state, "Model Not Found in Manifest" (`LineageView.tsx:243-284`), and only clears an in-memory cache and re-reads the file. It does not run dbt.
- Lineage needs `target/manifest.json` and nothing else. A full run is not required: `dbt compile` writes the manifest too, per the app's own message. `lineage.service.ts:88, 204, 232`.
- Lineage reads `target/manifest.json`: `main/services/lineage.service.ts:88`.
- `Maximize` and `Refresh lineage` tooltips: `LineageView.tsx:335`, `LineageToolbar.tsx:78`.
- The 4-then-1 build order: lesson 8's captured run log, which matches the graph exactly.

## The ordering trap between lessons 8 and 11

Lesson 8 must be filmed with **no** `target/` folder. Lesson 11 cannot be filmed **without** one. They are adjacent in the course and contradictory in setup.

Film 8 first, then simply run dbt again before filming 11. The cue sheets for both say so.

## No forward references

Slide 9 talks about what the graph is for later without naming a lesson. The closing hands off to lesson 12.

## Open items

- Record after lesson 8, with `target/` restored by a fresh run.
- Do not pre-select a model or pre-change the depth. Both are performed on camera.
- Audio target is minus 14 LUFS.
- Kokoro pronunciation of "dbt" and "DAG" both unverified. "DAG" is new to the series here and is likely to need markup, since it can read as three letters. Worth testing before generating the MP3s: the title card says DAG but the narration never speaks it, so only the file names are exposed.
