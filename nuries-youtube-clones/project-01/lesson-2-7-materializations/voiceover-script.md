# Materializations: views and tables — voice-over script and beat sheet

dbt + DuckDB in Rosetta DBT Studio · Module 2 · dbt basics · next: Lesson 2.8 · Tests

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `lesson-2-6-end`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 1 · Lesson 2.7. Materializations: views and tables. Badges: view, table, config().

## s01 · slide — slide `compare`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | dbt can build a model as a view or as a table. A view stores only the query, so it is always fresh, but every read runs it again. A table stores the rows: fast to read, and as fresh as the last run. | View: stores only the query; always fresh; slower to read. Table: stores the rows; fast to read; fresh as of the last run. | 44 | 14 |
| b02 @0:17 | Right now every model is a view, the default. We keep trips a view, a thin layer over the files, and make the three marts tables, because people query those. Incremental and ephemeral models come later. | Right now: every model is a view (dbt's default). Plan: trips stays a view, the three marts become tables. Later: incremental, ephemeral. | 36 | 13 |

## s02 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b03 @0:29 | Open the project, and open dbt project dot yml. | Open project **nyc_taxi** from Recent Projects<br>Open `dbt_project.yml` in the Explorer<br>Zoom: explorer | 9 | 6 |
| b04 @0:35 | Under nyc taxi, add plus materialized, table. Every model in the project becomes a table. Save. | At the end of the file, type 25 characters<br>Click **Save**<br>(check: `dbt_project.yml` equals `../snippets/2.7/dbt_project.yml`)<br>Zoom: code-mid | 16 | 8 |

## s03 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b05 @0:43 | But trips should stay a view. Open trips dot sql. At the very top, add a config block: materialized equals view. A setting in the model wins over the project file. Save. | Close the editor tab for `dbt_project.yml`<br>Open `models/trips.sql` in the Explorer<br>type_start: {{ config(materialized='view') }}

<br>Click **Save**<br>(check: `models/trips.sql` equals `../snippets/2.7/trips.sql`)<br>Zoom: code-close | 32 | 12 |

## s04 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b06 @0:55 | Run the project: Project menu, Run. | Open the **Project** menu → **Run**<br>Zoom: project-menu | 6 | 3 |
| b07 @0:59 | The log now says sql view model for trips, and sql table model for the other three. | Wait for “PASS=4”<br>Zoom: terminal-close<br>Card: *dbt run* — **1 view, 3 tables** — PASS=4 ERROR=0 | 17 | 6 |
| b08 @1:05 | Let's check in DuckDB. Open the SQL Editor, pick nyc taxi dev, and list the tables in the main schema, with their type. | Left bar → **SQL Editor**<br>Pick the connection **nyc_taxi_dev**<br>Type 100 characters into the editor<br>Zoom: explorer | 23 | 12 |
| b09 @1:17 | Run it. | Click the green run arrow next to line 1<br>Zoom: explorer | 2 | 4 |
| b10 @1:21 | Trips is a view. The three marts are base tables, and so is the seed. | Zoom: sql-results<br>Card: *information_schema.tables* — **trips: VIEW** — marts and seed: BASE TABLE | 15 | 5 |

## s05 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b11 @1:26 | Back in the project, the Git tab shows the two changed files. | Left bar → **DBT Studio**<br>Open the **Git** tab in the sidebar<br>Zoom: git-panel | 12 | 6 |
| b12 @1:32 | Stage all, type a message, materialize the marts as tables, and commit. | Hover CHANGES and click **+** (Stage All Changes)<br>Type the commit message “Materialize the marts as tables”<br>Click **Commit**<br>Zoom: git-panel | 12 | 9 |
| b13 @1:41 | Sync Changes, and it's on GitHub. | git_push: None<br>Zoom: git-panel | 6 | 5 |

## s06 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b14 @1:46 | To recap: views store the query, tables store the rows. One line in dbt project dot yml sets the default, and a config block in a model overrides it. Next, we test the data. | Recap: view vs table; +materialized in dbt_project.yml for the project; config() in the model wins; check in information_schema; pushed. | 34 | 13 |

## s07 · closing card (4 s, no voice)

Next · Lesson 2.8 · Tests. Code: github.com/Nuri1977/nyc-taxi-dbt.

**Total: 264 spoken words, 2:03 rendered.**
