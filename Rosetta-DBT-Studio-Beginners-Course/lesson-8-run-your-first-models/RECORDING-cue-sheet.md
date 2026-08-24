# Lesson 8 - Recording Cue Sheet

One command, `dbt run`, and the models generated in lesson 7 become views and a table inside the DuckDB file. The point it has to land is that dbt compiles SQL and sends it, that nothing moved or was copied anywhere, and that the terminal output is readable if you know what the last line means.

Full frame cards are `slides/1.png` (intro) and `slides/10.png` (closing).

App version: **1.6.4**. dbt-core 1.12.0, dbt-duckdb 1.10.1.

## Before you hit F9

- **Start from lesson 7's end state.** `models/raw` with 4 YAML, `models/staging` with 4 SQL, `models/enhanced` with the one edited grades model.
- **Delete `target/` and `logs/` first.** This lesson makes a point of the slow first parse and of the folders appearing, and neither reads if they are already there.
- **Delete `.user.yml` too.** A viewer following along has never run dbt, so they do not have this file. Starting with it on screen is a visible "why is mine different" moment. dbt rewrites it during the run (`dbt/tracking.py`, `get_cookie` calls `set_cookie` when the file is absent and `profiles.yml` is beside it), so it reappears at slide 8's refresh alongside `target` and `logs` — on their machine too, at the same moment. Expected, and deliberately not narrated: the line says "the folders logs and target", and `.user.yml` is a file, so nothing is contradicted. Do not loosen that wording to "two new things".
- **The database must have only the four original tables.** If you have run dbt while testing, drop the four `main_*` views and `enh_main_grades` first, or slide 7's count is wrong.
- **One deliberate difference from lesson 7's final frame.** That video ended with `models` expanded all the way to the nine files. Lesson 8 starts one level shallower, on purpose, see below. Everything else matches, including no `.user.yml`.
- **Expand `models` one level only**, so `enhanced`, `raw` and `staging` show with their files still closed. That is fifteen rows, going to eighteen after the run and twenty once `target` is opened, all of which fit the sidebar with room to spare. Do NOT expand to the nine files as lesson 7 ended: twenty-five rows pushes slide 8's reveal off screen. One level also matches the gesture used on `target` later in the lesson.
- **Close every editor tab.** This lesson never opens a file, so lesson 7's open models are clutter, and an empty tab strip gives the terminal panel the height it needs.
- Bottom panel open, on the **Terminal** tab, before you start. If it is closed, clicking Run opens it for you, and that jump lands on slide 4's "watch the first two lines".
- **Drag the terminal divider up so about 22 lines fit.** The run is 21 lines including the echoed command. Slides 5 and 6 both point at lines near the top and the bottom, so nothing may scroll off.
- Dark theme, app maximized, taskbar auto-hidden.

## Beats

| Listen for | Do this |
|---|---|
| "Open the Project menu and Run is right there" | Open the **Project** menu, scroll to **Run**, hold a moment |
| "Then it sends that SQL to your database" | Click **Run** |
| "Watch the two lines about parsing" | Point at `Unable to do partial parsing ... Starting full parse.` then `Found 5 models, 16 data tests, 4 sources, 486 macros`. The ~5s gap between their timestamps is the wait this slide is about. NOT the first two lines, which are just the dbt and adapter versions |
| "Each model got a start line" | Nothing is moving, the run finished back on slide 4. Three named things, three moves: the `START ... [RUN]` block, then the `OK created ...` block below it, then slide right onto one `[OK in 0.24s]`. Use the blocks, not one model's own pair, since the OK order shuffles per take |
| "The line that matters is the last one" | Point at `Completed successfully`, then move to the `Done.` line and land on `PASS=5` and `TOTAL=5` as you say "five passed out of five" |
| "Look at the labels" | Sweep the `view model` lines, then drop to the `incremental model` line. The narration counts **models, not lines**, so it does not matter which lines the cursor crosses: every model prints both a START and an OK, so the screen shows 8 `view model` and 2 `incremental model` lines while there are only 4 view models and 1 incremental. Do not reword this to count lines. The OK order is completion order across 4 threads and shuffles per take, so aim at the block, not a remembered position |
| "Your database file is still one file" | Explorer tab, point at the `rosetta` folder and the `university_sample.duckdb` inside it. Stay here for the whole slide. Do NOT go looking for the table list: the sidebar's Database tab only shows the connection card, and the schema tree lives in the SQL Editor, which is lesson 9 and which slide 10 promises. The contents stay spoken, not shown |
| "Refresh the file tree" | Click the **Refresh directories** icon above the tree. Point at `logs`, then down to `target`, top to bottom, and leave the cursor there |
| "Target is what makes the next run quick" | Expand `target` **one level only**, so `compiled` and `run` are both visible. Do not open them |
| "And the run is remembered" | Move the cursor down to the bottom panel, do not click yet |
| "Run History" | Click the **RUN HISTORY** tab, so it opens on the word |
| "Open it up and you get every model inside it" | Click anywhere on the `dbt run` row, the whole row toggles, not just the chevron. Rows start collapsed on every fresh mount of the panel, so it will be closed when you get there. The five model rows appear beneath with their own times and OK |

## The output, verbatim

This is a real capture of the first run in this exact project state. Times will differ, everything else should not.

```
cd "C:\Users\Edon\rosetta-dbt-studio-projects\dbtstudio_getting_started" && "C:\Users\Edon\AppData\Roaming\rosetta-dbt-studio\venv\Scripts\dbt.exe" run
12:36:19  Running with dbt=1.12.0
12:36:19  Registered adapter: duckdb=1.10.1
12:36:20  Unable to do partial parsing because saved manifest not found. Starting full parse.
12:36:25  Found 5 models, 16 data tests, 4 sources, 486 macros
12:36:25
12:36:25  Concurrency: 4 threads (target='dev')
12:36:25
12:36:26  1 of 5 START sql view model main.main_courses ............ [RUN]
12:36:26  2 of 5 START sql view model main.main_enrollments ........ [RUN]
12:36:26  3 of 5 START sql view model main.main_grades ............. [RUN]
12:36:26  4 of 5 START sql view model main.main_students ........... [RUN]
12:36:26  4 of 5 OK created sql view model main.main_students ...... [OK in 0.24s]
12:36:26  1 of 5 OK created sql view model main.main_courses ....... [OK in 0.24s]
12:36:26  2 of 5 OK created sql view model main.main_enrollments ... [OK in 0.25s]
12:36:26  3 of 5 OK created sql view model main.main_grades ........ [OK in 0.25s]
12:36:26  5 of 5 START sql incremental model main.enh_main_grades .. [RUN]
12:36:26  5 of 5 OK created sql incremental model main.enh_main_grades . [OK in 0.09s]
12:36:26
12:36:26  Finished running 1 incremental model, 4 view models in 0 hours 0 minutes and 1.63 seconds (1.63s).
12:36:26
12:36:26  Completed successfully
12:36:26
12:36:26  Done. PASS=5 WARN=0 ERROR=0 SKIP=0 NO-OP=0 REUSED=0 TOTAL=5
```

About **7 seconds** of terminal output from first line to last, of which the models themselves are 1.63s. The rest is dbt starting up and parsing. No speed ramp needed, but do not cut the pause either, because slide 4 is about exactly that wait.

**Two lines per model, and the OK order looks wrong.** All four views START before any of them finishes, because of the 4 threads, and they then report OK in completion order, here 4, 1, 2, 3. The incremental model waits and runs alone. This is what slide 5's "a start line, a finish line" refers to, so do not be thrown by the ordering on camera.

## What the database looks like afterwards

Nine objects in `university_sample.duckdb`, all in schema `main`, all 100 rows:

| Kind | Names |
|---|---|
| Original tables | `courses`, `enrollments`, `grades`, `students` |
| Views, from staging | `main_courses`, `main_enrollments`, `main_grades`, `main_students` |
| Incremental table, from enhanced | `enh_main_grades` |

`target/` contains two folders, `compiled` and `run`, and 23 files. Expand it one level on camera and stop
there. `compiled` and `run` are what the card names, and each holds the same five model files under
`models/staging` and `models/enhanced`, which is a wall of repeated filenames that teaches nothing new.
The loose files alongside them include `manifest.json`, `run_results.json` and `partial_parse.msgpack`.
That last one is literally the cache slide 8's narration is talking about, if you ever want to point at it.

## Why four views and one table

The staging models never declared a materialization, so they got dbt's default, which is `view`. A view stores no rows, it is a saved query.

The enhanced model declares `materialized='incremental'`, which has to be a real table, because an incremental model compares what is arriving against what it already holds.

## Do not run it twice on camera

The second run is clean now that the placeholders are filled in, and it is faster because the parse is cached. It is still not worth filming: the terminal looks identical apart from timings, and nothing new is explained.

If you do run it twice by accident, no harm. Both runs pass. That was verified.

## Timing

The script runs about 180 seconds of speech against a 180 second budget. The only stretch you do not control is the run itself, and it is 7 seconds.

## Recording

F9, wait 3 seconds, start the Kokoro MP3 on your phone, perform the beats in sync. Let it run 3 seconds past the last word before F9 again.
