# Models: your first dbt model — voice-over script and beat sheet

dbt + DuckDB in Rosetta DBT Studio · Module 2 · dbt basics · next: Lesson 2.4 · Dependencies & Jinja

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `lesson-2-2-end`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 1 · Lesson 2.3. Models: your first dbt model. dbt + DuckDB in Rosetta DBT Studio. Badges: Rosetta DBT Studio 1.7.6, dbt Core 1.12, DuckDB, NYC taxi 2025.

## s01 · slide — slide `model`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | In the last lesson, we pointed dbt at the raw taxi files. Now we build on top of them, with a model. A model is one select statement, saved in one .sql file, in the models folder. | Big statement: A model is one select, in one .sql file. A file card trips.sql with a select. | 37 | 13 |
| b02 @0:16 | When you run it, dbt builds a view or a table from that select, and names it after the file. So trips.sql becomes a view called trips. | An arrow from the file to a DuckDB object card: view main.trips, named after the file. | 28 | 10 |

## s02 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b03 @0:25 | Here is the project from the last lesson. Open it, right-click the models folder, choose New File, and call it trips.sql. | Open project **nyc_taxi** from Recent Projects<br>Right-click `models` → **New File** → `trips.sql` → **Save**<br>Zoom: explorer | 23 | 10 |
| b04 @0:35 | Start with a comment that says what one row is: one green taxi trip from 2025. Then, select. | Type 74 characters into the editor<br>Zoom: code-close | 18 | 8 |
| b05 @0:43 | Pick the columns we need, and give them clear names: the vendor, the pickup and drop-off times, and the pickup and drop-off zones. | Type 212 characters into the editor<br>Zoom: code-close | 25 | 8 |
| b06 @0:51 | Then the passenger count, the distance, how the rider paid, and the money: fare, tip, and total. | Type 108 characters into the editor<br>Zoom: code-close | 17 | 6 |
| b07 @0:58 | Read them from the raw green trips source. The source function points at the table we loaded and declared in the last lesson. | Type 40 characters into the editor<br>Zoom: code-close<br>Card: *source()* — **No file paths in the model** — sources.yml says where raw.green_trips lives. | 23 | 8 |
| b08 @1:05 | Finally, keep only trips that started in 2025, and drop the rows with no distance, or no charge. | Type 133 characters into the editor<br>Zoom: code-close | 18 | 8 |
| b09 @1:13 | That is the whole model. One select, and no create statement. Save it. | Click **Save**<br>(check: `models/trips.sql` equals `../snippets/3.3/trips.sql`) | 13 | 5 |

## s03 · slide — slide `flow`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b10 @1:19 | So what happens when you run it? First, dbt compiles the file. The Jinja in curly braces becomes plain SQL, and the source call becomes the real table name. | Step 1, Compile: the Jinja in curly braces becomes SQL; source('raw','green_trips') becomes "nyc_taxi_dev"."raw"."green_trips". | 29 | 11 |
| b11 @1:30 | Then dbt wraps your select in a create view statement. That is the part you never write. | Step 2, Wrap: create view trips as ( your select ). Label: dbt writes this. | 17 | 6 |
| b12 @1:36 | And it sends the statement to DuckDB, which saves the view in the dev database file. | Step 3, Execute: the statement goes to DuckDB; nyc_taxi_dev.duckdb now holds the view main.trips. | 16 | 6 |

## s04 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b13 @1:42 | Let's run it. Above the editor, open the Model menu, and choose Run. It runs just this model. | model_menu: Run<br>Zoom: model-menu | 18 | 7 |
| b14 @1:49 | The terminal shows one model, trips, created as a view in the main schema. One pass, no errors. | Wait for “OK created sql view model main.trips”<br>Zoom: terminal-close<br>Card: *dbt run* — **OK created sql view model main.trips** — PASS=1 ERROR=0 | 18 | 7 |

## s05 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b15 @1:56 | To look at the rows, open the Model menu again, and choose Preview. Studio compiles the model, runs its select, and opens the result. | model_menu: Preview<br>Wait for “^Preview: trips$”<br>Zoom: model-menu | 24 | 10 |
| b16 @2:06 | Eleven columns, and five hundred sixty-five thousand trips, out of five hundred ninety-one thousand raw rows. Scroll right for the distance, the payment type and the amounts. | dialog_scroll_right: None<br>Zoom: center-wide<br>Card: *2025 data, as of 9 Nov 2026* — **565,039 trips** — kept from 591,375 raw rows | 29 | 11 |
| b16b @2:17 | Close it. The same rows stay in the Query Results tab, next to the SQL that ran, and a history of your previews. | Click **Close**<br>Click **SQL tab**<br>Click **History tab**<br>Zoom: terminal | 23 | 8 |

## s06 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b17 @2:25 | Want to see exactly what dbt sends to DuckDB? Model menu, Compile. | model_menu: Compile<br>Wait for “^Compiled SQL: trips$”<br>Zoom: model-menu | 12 | 7 |
| b18 @2:32 | The Compiled SQL tab shows your select, with the source call replaced by the real table: nyc taxi dev, raw, green trips. | Click **Compiled SQL tab**<br>Zoom: center-wide<br>Card: *Compiled SQL* — **source() → raw.green_trips** — Jinja became plain SQL. | 22 | 10 |
| b19 @2:42 | Close it, and open Run History. Every dbt command Studio ran is here: dbt run, select trips, one of one passed. | Click **Close**<br>Click **Run History**<br>Zoom: terminal | 21 | 9 |

## s07 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b20 @2:51 | Last step: commit and push. Open the Git tab. Trips.sql is listed as a new file. The target and logs folders are not, because git ignores them. | Open the **Git** tab in the sidebar<br>Zoom: git-panel | 28 | 11 |
| b21 @3:02 | Stage it with the plus button, type a message, add the trips staging model, and click Commit. | Hover `trips.sql` and click **+** (Stage Changes)<br>Type the commit message “Add the trips staging model”<br>Click **Commit**<br>Zoom: git-panel | 17 | 9 |
| b22 @3:11 | Click Sync Changes, and the commit goes to GitHub. | git_push: None<br>Zoom: git-panel | 9 | 5 |

## s07b · browser — Browser

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b22b @3:16 | On GitHub, the models folder now holds trips dot sql, next to sources dot yml. | Browser: open https://github.com/Nuri1977/nyc-taxi-dbt/tree/main/models<br>Zoom: center-wide | 15 | 6 |

## s08 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b23 @3:22 | To recap. A model is one select in one file. dbt compiles it, wraps it in create view, and runs it in DuckDB. Preview shows the rows, and the Git tab sends it to GitHub. Next, we add two more models that build on trips. | Recap: A model is one select in one .sql file. Run: compile, wrap in create view, execute in DuckDB. Preview shows the rows, Compile the SQL, Run History the runs. Commit and push in the Git tab. | 45 | 16 |

## s09 · closing card (4 s, no voice)

Next · Lesson 2.4 · Dependencies & Jinja. Code: github.com/Nuri1977/nyc-taxi-dbt.

**Total: 545 spoken words, 3:42 rendered.**
