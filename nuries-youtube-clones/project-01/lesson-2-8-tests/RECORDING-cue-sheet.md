# Tests: trust your data — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `lesson-2-7-end`: a clone of what Lesson 2.7 pushed, the parquet files in data/raw, the nyc_taxi_dev connection, and the database after dbt seed + dbt run (off camera).

## s02 · Add tests in YAML

| Listen for | Do this |
|---|---|
| "Open the project, and open schema dot yml.…" | On the home screen, click **nyc_taxi** under Recent Projects<br>In the Explorer, open `models/schema.yml` (expand each folder on the way) |
| "Under borough, in trips per month: accepted values,…" | insert_at: {'line': 19, 'text': "\n        data_tests:\n          - accepted_values:\n              arguments:\n                values: ['Bronx', 'Brooklyn', 'EWR', 'Manhattan', 'Queens', 'Staten Island', 'Unknown']"} |
| "Zone id in top pickup zones is that…" | insert_at: {'line': 30, 'text': '\n        data_tests: [not_null, unique]'} |
| "The same for month in monthly summary. Save.…" | insert_at: {'line': 38, 'text': '\n        data_tests: [not_null, unique]'}<br>Click **Save** (top right of the editor)<br>(Check that `models/schema.yml` matches `../snippets/2.8/schema_fail.yml`) |
| "And in seeds dot yml, Location ID: not…" | Close the editor tab for `models/schema.yml` (its ×)<br>In the Explorer, open `seeds/seeds.yml` (expand each folder on the way)<br>insert_at: {'line': 6, 'text': '\n        data_tests: [not_null, unique]'}<br>Click **Save** (top right of the editor)<br>(Check that `seeds/seeds.yml` matches `../snippets/2.8/seeds.yml`) |

## s03 · Run the tests

| Listen for | Do this |
|---|---|
| "Run them all: Project menu, Test.…" | Close the editor tab for `seeds/seeds.yml` (its ×)<br>Open the **Project** menu (arrow next to Project, top right) → **Test** |
| "Six pass, one fails: accepted values on borough.…" | Wait for “ERROR=1” |
| "It is N A. The zone lookup has…" | Hold; nothing moves |

## s04 · Fix and test one model

| Listen for | Do this |
|---|---|
| "Add N A to the list, and save.…" | In the Explorer, open `models/schema.yml` (expand each folder on the way)<br>insert_at: {'line': 23, 'back': 1, 'text': ", 'N/A'"}<br>Click **Save** (top right of the editor)<br>(Check that `models/schema.yml` matches `../snippets/2.8/schema.yml`) |
| "To check just this model, open trips per…" | Close the editor tab for `models/schema.yml` (its ×)<br>In the Explorer, open `models/trips_per_month.sql` (expand each folder on the way)<br>model_menu: Test |
| "One test on this model, and it passes.…" | Wait for “PASS=1” |

## s06 · Build everything

| Listen for | Do this |
|---|---|
| "Project menu, Build.…" | Open the **Project** menu (arrow next to Project, top right) → **Build** |
| "One seed, four models, seven tests. Twelve passes,…" | Wait for “PASS=12” |

## s07 · Commit and push

| Listen for | Do this |
|---|---|
| "The Git tab: schema dot yml and seeds…" | Close the editor tab for `models/trips_per_month.sql` (its ×)<br>Click the **Git** tab at the top of the sidebar |
| "Stage all, type a message, add data tests,…" | Hover CHANGES and click **+** (Stage All Changes)<br>Click the message box and type: Add data tests<br>Click **Commit** |
| "Sync Changes. That's the end of dbt basics.…" | git_push: None |
