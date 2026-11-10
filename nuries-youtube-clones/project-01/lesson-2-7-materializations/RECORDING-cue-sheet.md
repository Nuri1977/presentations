# Materializations: views and tables — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `lesson-2-6-end`: a clone of what Lesson 2.6 pushed, the parquet files in data/raw, the nyc_taxi_dev connection, and the database after dbt seed + dbt run (off camera): every model is a view.

## s02 · One line for the whole project

| Listen for | Do this |
|---|---|
| "Open the project, and open dbt project dot…" | On the home screen, click **nyc_taxi** under Recent Projects<br>In the Explorer, open `dbt_project.yml` (expand each folder on the way) |
| "Under nyc taxi, add plus materialized, table. Every…" | Click at the end of the file and type:<br><br>```yaml<br>    +materialized: table<br>```<br>Click **Save** (top right of the editor)<br>(Check that `dbt_project.yml` matches `../snippets/2.7/dbt_project.yml`) |

## s03 · Keep trips a view

| Listen for | Do this |
|---|---|
| "But trips should stay a view. Open trips…" | Close the editor tab for `dbt_project.yml` (its ×)<br>In the Explorer, open `models/trips.sql` (expand each folder on the way)<br>type_start: {{ config(materialized='view') }}<br><br><br>Click **Save** (top right of the editor)<br>(Check that `models/trips.sql` matches `../snippets/2.7/trips.sql`) |

## s04 · Run and check

| Listen for | Do this |
|---|---|
| "Run the project: Project menu, Run.…" | Open the **Project** menu (arrow next to Project, top right) → **Run** |
| "The log now says sql view model for…" | Wait for “PASS=4” |
| "Let's check in DuckDB. Open the SQL Editor,…" | In the left bar, click **SQL Editor**<br>Open the connection list (top left) and pick **nyc_taxi_dev**<br>Type:<br><br>```sql<br>select table_name, table_type from information_schema.tables where table_schema = 'main' order by 1;<br>``` |
| "Run it.…" | Click the green ▶ arrow next to line 1 |
| "Trips is a view. The three marts are…" | Hold; nothing moves |

## s05 · Commit and push

| Listen for | Do this |
|---|---|
| "Back in the project, the Git tab shows…" | In the left bar, click **DBT Studio**<br>Click the **Git** tab at the top of the sidebar |
| "Stage all, type a message, materialize the marts…" | Hover CHANGES and click **+** (Stage All Changes)<br>Click the message box and type: Materialize the marts as tables<br>Click **Commit** |
| "Sync Changes, and it's on GitHub.…" | git_push: None |
