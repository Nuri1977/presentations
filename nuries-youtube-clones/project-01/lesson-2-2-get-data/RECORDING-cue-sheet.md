# Get the data — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `lesson-2-1-end`: a clone of what Lesson 2.1 pushed (nyc-taxi-dbt-rehearsal, main at be0f093), the empty template folders, and the nyc_taxi_dev DuckDB connection.
- The data files are copied into data/raw and seeds off camera, at the point where the learner moves the downloaded files.

## s03 · Put the files in the project

| Listen for | Do this |
|---|---|
| "In Studio, open the nyc taxi project. Right-click…" | On the home screen, click **nyc_taxi** under Recent Projects<br>new_root_folder: data |
| "Inside data, make a folder called raw.…" | Right-click `data` → **New Folder**, type `raw`, click **Save** |
| "Now move the twelve parquet files into data,…" | copy_in: {'from': '../.cache/data/raw', 'to': 'data/raw', 'settleMs': 500}<br>copy_in: {'from': '../.cache/data/taxi_zone_lookup.csv', 'to': 'seeds/taxi_zone_lookup.csv', 'settleMs': 500}<br>refresh_explorer: None<br>expand: data/raw<br>expand: seeds<br>Point at `data/raw/green_tripdata_2025-12.parquet` in the Explorer<br>Point at `seeds/taxi_zone_lookup.csv` in the Explorer |

## s04 · Declare the source

| Listen for | Do this |
|---|---|
| "Next, tell dbt about the raw files. Right-click…" | Right-click `models` → **New File**, type `sources.yml`, click **Save** |
| "A source called raw, with a short description.…" | Type:<br><br>```sql<br>sources:<br>  - name: raw<br>    description: NYC TLC green taxi trip records for 2025, read in place from data/raw.<br>``` |
| "It has one table, green trips: one row…" | Type:<br><br>```sql<br>    tables:<br>      - name: green_trips<br>        description: One row per green taxi trip, as reported to the TLC.<br>``` |
| "And where the table lives: external location, a…" | Type:<br><br>```sql<br>        config:<br>          external_location: "read_parquet('data/raw/green_tripdata_2025-*.parquet', union_by_name = true)"<br>```<br>Click **Save** (top right of the editor)<br>(Check that `models/sources.yml` matches `../snippets/2.2/sources.yml`) |

## s05 · Check the source

| Listen for | Do this |
|---|---|
| "Does dbt find the data? In the command…" | Click the command box under the terminal, type `dbt show --inline "select count(*) as trips from {{ source('raw', 'green_trips') }}"`, press Enter |
| "dbt turns the source into the read parquet…" | Hold; nothing moves |

## s06 · Commit and push

| Listen for | Do this |
|---|---|
| "Now the Git tab. Only two files changed:…" | Close the editor tab for `models/sources.yml` (its ×)<br>Click the **Git** tab at the top of the sidebar |
| "Stage all, type a message, declare the raw…" | Hover CHANGES and click **+** (Stage All Changes)<br>Click the message box and type: Declare the raw trips source and add the zone lookup<br>Click **Commit** |
| "Then click Sync Changes. Studio pushes the commit…" | git_push: None |

## s07 · On GitHub

| Listen for | Do this |
|---|---|
| "On GitHub, the repository now has the models…" | In the browser, open https://github.com/Nuri1977/nyc-taxi-dbt-rehearsal |
