# Get the data — voice-over script and beat sheet

dbt + DuckDB in Rosetta DBT Studio · Module 2 · dbt basics · next: Lesson 2.3 · Models

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `lesson-2-1-end`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 1 · Lesson 2.2. Get the data. Badges: Parquet, sources.yml, Seed CSV.

## s01 · slide — slide `sources`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | Our raw data is twelve parquet files, one per month of 2025. They are too big for git, so they stay in a data folder that git ignores. We load them once into a DuckDB table, raw green trips, and a source, in sources dot yml, tells dbt about it. | Source card: big raw files stay outside git; 12 parquet files in data/raw, loaded once into the DuckDB table raw.green_trips; sources.yml declares it. | 50 | 18 |
| b02 @0:20 | The second file is small: a lookup of the 265 taxi zones. Small CSV files like this one are seeds. They live in the repository, and dbt loads them as tables. | Seed card: a small CSV that lives in the repo; seeds/taxi_zone_lookup.csv, 265 zones. | 31 | 13 |

## s02 · slide — slide `download`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b03 @0:33 | The files come from the New York City Taxi and Limousine Commission website. Under 2025, download Green Taxi Trip Records for each month, January to December. The links are in the description. | TLC Trip Record Data page path: 2025, each month, Green Taxi Trip Records; file URL pattern; target tree data/raw. | 32 | 13 |
| b04 @0:47 | Further down the same page, download the Taxi Zone Lookup Table, as CSV. | Taxi Zone Lookup Table, CSV link; the tree shows seeds/taxi_zone_lookup.csv. | 13 | 6 |

## s03 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b05 @0:52 | In Studio, open the nyc taxi project. Right-click the project, choose New Folder, and call it data. | Open project **nyc_taxi** from Recent Projects<br>new_root_folder: data | 18 | 10 |
| b06 @1:02 | Inside data, make a folder called raw. | Right-click `data` → **New Folder** → `raw` → **Save** | 7 | 6 |
| b07 @1:08 | Now move the twelve parquet files into data, raw, and the zone lookup CSV into seeds. Refresh the explorer, and there they are. | copy_in: {'from': '../.cache/data/raw', 'to': 'data/raw', 'settleMs': 500}<br>copy_in: {'from': '../.cache/data/taxi_zone_lookup.csv', 'to': 'seeds/taxi_zone_lookup.csv', 'settleMs': 500}<br>refresh_explorer: None<br>expand: data/raw<br>expand: seeds<br>Point at `data/raw/green_tripdata_2025-12.parquet` in the Explorer<br>Point at `seeds/taxi_zone_lookup.csv` in the Explorer<br>Zoom: explorer | 23 | 9 |

## s04 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b08 @1:17 | Now load the files into DuckDB. Open the SQL Editor, and pick the nyc taxi dev connection. | Left bar → **SQL Editor**<br>Pick the connection **nyc_taxi_dev**<br>Zoom: explorer | 17 | 9 |
| b09 @1:25 | Three statements, one per line. Create a schema called raw. Create the table raw green trips, from read parquet over all twelve files: use the full path of your data raw folder. Then count the rows. | Type 237 characters into the editor<br>Zoom: explorer | 36 | 13 |
| b10 @1:39 | Run them one by one, with the green arrow next to each line. Union by name lines up the columns, even if a month's file has them in a different order. | Click the green run arrow next to line 1<br>Click the green run arrow next to line 1<br>Click the green run arrow next to line 1<br>Zoom: explorer | 31 | 16 |
| b11 @1:55 | Five hundred ninety-one thousand, three hundred seventy-five trips in 2025, now in one DuckDB table. | Zoom: sql-results<br>Card: *raw.green_trips · 2025 data, as of 9 Nov 2026* — **591,375 trips** — all 12 files, loaded once | 17 | 9 |

## s05 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b12 @2:04 | Back in the project, tell dbt about the table. Right-click models, New File, and call it sources dot yml. | Left bar → **DBT Studio**<br>Right-click `models` → **New File** → `sources.yml` → **Save**<br>Zoom: explorer | 20 | 9 |
| b13 @2:13 | A source called raw, the schema we just made, with a short description. | Type 116 characters into the editor<br>Zoom: code-close | 13 | 5 |
| b13b @2:18 | It has one table, green trips: one row per green taxi trip. Save. In a model, source raw, green trips, now points at that table. | Type 112 characters into the editor<br>Click **Save**<br>(check: `models/sources.yml` equals `../snippets/2.2/sources.yml`)<br>Zoom: code-close<br>Card: *source('raw', 'green_trips')* — **nyc_taxi_dev.raw.green_trips** — No file paths in the models. | 25 | 10 |

## s06 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b14 @2:27 | Now the Git tab. Only two files changed: sources dot yml and the CSV. The parquet files are not here, because the gitignore leaves out the data folder. | Close the editor tab for `models/sources.yml`<br>Open the **Git** tab in the sidebar<br>Zoom: git-panel | 28 | 11 |
| b15 @2:38 | Stage all, type a message, declare the raw trips source and add the zone lookup, and commit. | Hover CHANGES and click **+** (Stage All Changes)<br>Type the commit message “Declare the raw trips source and add the zone lookup”<br>Click **Commit**<br>Zoom: git-panel | 17 | 9 |
| b16 @2:47 | Then click Sync Changes. Studio pushes the commit to GitHub. | git_push: None<br>Zoom: git-panel | 10 | 5 |

## s07 · browser — Browser

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b17 @2:52 | On GitHub, the repository now has the models and seeds folders, and the latest commit message. | Browser: open https://github.com/Nuri1977/nyc-taxi-dbt<br>Zoom: center-wide | 16 | 7 |

## s08 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b18 @2:59 | To recap: the trip files sit in data raw, outside git, and live in DuckDB as raw green trips. The zone lookup is a seed. And sources dot yml declares the source. Next, we build our first model on top of it. | Recap: trips in data/raw, loaded into raw.green_trips (591,375 rows); zones in seeds; sources.yml declares the source; two files in git; pushed with Sync Changes. | 42 | 15 |

## s09 · closing card (4 s, no voice)

Next · Lesson 2.3 · Models. Code: github.com/Nuri1977/nyc-taxi-dbt.

**Total: 446 spoken words, 3:17 rendered.**
