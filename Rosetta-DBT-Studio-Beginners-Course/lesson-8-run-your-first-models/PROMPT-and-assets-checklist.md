# Lesson 8 - Prompt and Assets Checklist

Lesson 8, "Run your first models", runs `dbt run` on the models generated in lesson 7. The point it has to land is that dbt compiles SQL and sends it to the database, that nothing was copied or moved, and that the log's last line is the one that matters.

Format: screen recording, with full frame cards for the intro and the close. Concept text is composited on top of the footage in CapCut as transparent content cards. Same approach as lessons 1 to 7.

App version at time of production: **1.6.4**. dbt-core 1.12.0, dbt-duckdb 1.10.1.

## Assets in this folder

| Path | What it is | Status |
|---|---|---|
| `voiceover-script-180sec.md` | Plain script. Subtitle source. | Done |
| `voiceover-kokoro.txt` | Same words with Kokoro markup. | Done |
| `RECORDING-cue-sheet.md` | Beats, prep, and the verbatim log. | Done |
| `video-presentation.html` | Reference deck, ten slides. | Done |
| `slides/1.png` | Intro card, full frame. | Done |
| `slides/10.png` | Closing card, full frame. | Done |
| `overlays/1. card-where-run-lives.png` | Content card, bottom left. | Done |
| `overlays/2. card-what-it-does.png` | Content card, top right. | Done |
| `overlays/3. card-slow-first-run.png` | Content card, bottom left. | Done |
| `overlays/4. card-reading-the-log.png` | Content card, top right. | **Text still says "Reading The Log", deck now says "Reading The Terminal". Needs re-export.** |
| `overlays/5. card-views-and-tables.png` | Content card, top right. | Done |
| `overlays/6. card-where-it-landed.png` | Content card, top right. | Done |
| `overlays/7. card-target-folder.png` | Content card, top right. | Done |
| `overlays/8. card-run-history.png` | Content card, top right. | Done |
| `sounds/` | Kokoro MP3 per slide, ten of them. | To generate |
| Screen recording | One dbt run, then the Run History tab. | To record |

## Overlay card placement

Placement was revised on 19 Aug 2026. Panels are all 380px wide. Positions below are the **panel** rect, excluding the soft shadow, in the 1920x1080 frame.

| Card | Position | Panel rect |
|---|---|---|
| 1. where-run-lives | bottom left | x55-434 y670-940 |
| 2. what-it-does | top right | x1448-1827 y108-308 |
| 3. slow-first-run | bottom left | x55-434 y681-940 |
| 4. reading-the-terminal | top right | x1448-1827 y108-308 |
| 5. views-and-tables | top right | x1448-1827 y108-343 |
| 6. where-it-landed | top right | x1448-1827 y80-339 |
| 7. target-folder | top right | x1448-1827 y80-339 |
| 8. run-history | top right | x1448-1827 y108-308 |

The two bottom-left cards sit above the **Create Pipeline** button and stop at x434, clear of the terminal panel which starts near x450. That is why they are at x55 rather than the x92 the top-left cards used: a 380 wide panel at x92 reaches x472 and would clip the terminal.

Cards 6 and 7 sit 28px above the other right-hand cards, in the gap between the **Project** button row (which ends near y69) and the terminal's first output line (near y341 with the panel dragged tall). Do not raise them further: at y40 the panel covers the Project button. Their soft shadow does reach past y339, which is fine, it is barely visible. If they still crowd the terminal, shrink the bottom panel for slides 7 and 8 rather than moving the cards. Both are file-tree slides and neither needs the terminal tall.

Card 7 deliberately does not mention `logs`. The voiceover names both folders and dismisses both; the card exists to say the one thing the voice does not, which is what `compiled` and `run` hold.

Each PNG is a full 1920x1080 frame. Drop it at 0,0 with scale 100%. Do not reposition or rescale. Fade with CapCut Animation on the clip, never a Transition.

## What is verified, and how

- The full run log, model counts, timings and the `Done.` line: captured by running `dbt run` on this project in the exact state lesson 7 leaves it in.
- 4 views plus 1 incremental table, 9 objects total, all 100 rows: queried out of the DuckDB file afterwards.
- `target/` holds `compiled` and `run`, 23 files: read off disk.
- 486 macros, 16 data tests, 4 sources: from the `Found ...` line.
- `Concurrency: 4 threads` traces back to `threads: 4` in `profiles.yml`, which lesson 6 already showed the viewer.
- Run History behaviour, the 50 entry cap, per project localStorage and invocation id deduplication: `presentations/dbt-sql-results-and-run-history.md/plan-presentation.md`, the 1.6.1 feature write up, cross checked against a real screenshot of the panel.
- The default `view` materialization: the staging models declare none, and the log calls all four `view model`.

## The one thing to check on the take

The Run History facts came from the 1.6.1 feature document, not from source. The panel layout, the parent row summary and the child rows are confirmed by a real screenshot, but the 50 entry cap is documentation rather than something I ran. Card 8 is the only asset that depends on it. If you would rather not state a number, say so and I will re-render that card without it.

## No forward references

Slide 9 comes close, since Run History pays off mostly when something fails. It is phrased as "the day something breaks" rather than as a pointer to lesson 21, which keeps it inside the rule.

## Open items

- Record straight after lesson 7. Delete `target/`, `logs/` and `.user.yml`, and drop the five generated objects from the database first.
- Do not film a second run. It passes, it is just not interesting.
- Audio target is minus 14 LUFS.
- Kokoro pronunciation of "dbt" still unverified. This script opens on "dbt run" in the first ten words, so it is the most exposed script in the series so far.
