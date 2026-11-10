# Tests: trust your data — voice-over script and beat sheet

dbt + DuckDB in Rosetta DBT Studio · Module 2 · dbt basics · next: Lesson 3.1 · Ship & Automate

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `lesson-2-7-end`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Times are estimates at 150 words per minute until the video is rendered.

## s00 · title card (3 s, no voice)

Project 1 · Lesson 2.8. Tests: trust your data. Badges: unique, not_null, accepted_values, dbt build.

## s01 · slide — slide `tests`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 | A dbt data test is a query that looks for bad rows. If it returns nothing, the test passes. If it returns rows, it fails. | A data test is a query that returns the bad rows. Zero rows = pass. | 25 | 11 |
| b02 | dbt has four built in: unique, not null, accepted values, and relationships. Start with the grain: the column that should be unique and never empty, like the month in monthly summary. | Four built-in tests: unique, not_null, accepted_values, relationships. Grain: one row per month, per zone. | 31 | 13 |

## s02 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b03 | Open the project, and open schema dot yml. Tests go right under the column they check. | Open project **nyc_taxi** from Recent Projects<br>Open `models/schema.yml` in the Explorer<br>Zoom: explorer | 16 | 7 |
| b04 | Under borough, in trips per month: accepted values, with the boroughs we expect. | insert_at: {'line': 19, 'text': "\n        data_tests:\n          - accepted_values:\n              arguments:\n                values: ['Bronx', 'Brooklyn', 'EWR', 'Manhattan', 'Queens', 'Staten Island', 'Unknown']"}<br>Zoom: code-mid | 13 | 6 |
| b05 | Zone id in top pickup zones is that table's grain: not null and unique. | insert_at: {'line': 30, 'text': '\n        data_tests: [not_null, unique]'}<br>Zoom: code-mid | 14 | 6 |
| b06 | The same for month in monthly summary. Save. | insert_at: {'line': 38, 'text': '\n        data_tests: [not_null, unique]'}<br>Click **Save**<br>(check: `models/schema.yml` equals `../snippets/2.8/schema_fail.yml`)<br>Zoom: code-mid | 8 | 4 |
| b07 | And in seeds dot yml, Location ID: not null and unique. Save. | Close the editor tab for `models/schema.yml`<br>Open `seeds/seeds.yml` in the Explorer<br>insert_at: {'line': 6, 'text': '\n        data_tests: [not_null, unique]'}<br>Click **Save**<br>(check: `seeds/seeds.yml` equals `../snippets/2.8/seeds.yml`)<br>Zoom: code-close | 12 | 6 |

## s03 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b08 | Run them all: Project menu, Test. | Close the editor tab for `seeds/seeds.yml`<br>Open the **Project** menu → **Test**<br>Zoom: project-menu | 6 | 3 |
| b09 | Six pass, one fails: accepted values on borough. Got one result, so one borough is not in our list. | Wait for “ERROR=1”<br>Zoom: terminal-close<br>Card: *dbt test* — **FAIL 1: accepted_values** — PASS=6 ERROR=1 | 19 | 8 |
| b10 | It is N A. The zone lookup has a zone two sixty-five, outside of New York City, with the borough N A, and about two hundred fifty trips in 2025 started there. The data is right; our list was wrong. | Zoom: terminal-close<br>Card: *The failing value* — **borough = 'N/A'** — Zone 265, Outside of NYC: 255 trips in 2025 | 41 | 17 |

## s04 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b11 | Add N A to the list, and save. | Open `models/schema.yml` in the Explorer<br>insert_at: {'line': 23, 'back': 1, 'text': ", 'N/A'"}<br>Click **Save**<br>(check: `models/schema.yml` equals `../snippets/2.8/schema.yml`)<br>Zoom: code-mid | 8 | 4 |
| b12 | To check just this model, open trips per month, and in the Model menu choose Test. | Close the editor tab for `models/schema.yml`<br>Open `models/trips_per_month.sql` in the Explorer<br>model_menu: Test<br>Zoom: model-menu | 16 | 7 |
| b13 | One test on this model, and it passes. | Wait for “PASS=1”<br>Zoom: terminal-close | 8 | 4 |

## s05 · slide — slide `build`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b14 | One more command: build. It seeds, runs and tests, in DAG order, so a failing test stops the models that depend on bad data. | build = seed + run + test, in DAG order. A failing test stops the models downstream of it. | 24 | 10 |

## s06 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b15 | Project menu, Build. | Open the **Project** menu → **Build**<br>Zoom: project-menu | 3 | 2 |
| b16 | One seed, four models, seven tests. Twelve passes, no errors. | Wait for “PASS=12”<br>Zoom: terminal-close<br>Card: *dbt build* — **PASS=12** — 1 seed · 4 models · 7 tests | 10 | 5 |

## s07 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b17 | The Git tab: schema dot yml and seeds dot yml changed. | Close the editor tab for `models/trips_per_month.sql`<br>Open the **Git** tab in the sidebar<br>Zoom: git-panel | 11 | 5 |
| b18 | Stage all, type a message, add data tests, and commit. | Hover CHANGES and click **+** (Stage All Changes)<br>Type the commit message “Add data tests”<br>Click **Commit**<br>Zoom: git-panel | 10 | 5 |
| b19 | Sync Changes. That's the end of dbt basics. | git_push: None<br>Zoom: git-panel | 8 | 4 |

## s08 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b20 | To recap: tests live in YAML next to the columns. A failing test told us something true about the data. And build runs and tests everything, in order. That's dbt basics. Next, we ship it: GitHub Actions builds the project on every push. | Recap: tests in YAML; a failure that taught us about the data; Model ▸ Test for one model; Project ▸ Build = run + test in order; pushed. | 43 | 18 |

## s09 · closing card (4 s, no voice)

Next · Lesson 3.1 · Ship & Automate. Code: github.com/Nuri1977/nyc-taxi-dbt.

**Total: 326 spoken words, about 2:33 estimated.**
