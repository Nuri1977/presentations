# Properties: describe your models — voice-over script and beat sheet

dbt + DuckDB in Rosetta DBT Studio · Module 2 · dbt basics · next: Lesson 2.6 · Docs & the DAG

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `lesson-2-4-end`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 1 · Lesson 2.5. Properties: describe your models. Badges: schema.yml, seeds.yml, persist_docs.

## s01 · slide — slide `props`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | Properties are YAML files that sit next to your SQL. They describe models, seeds and sources: what a table is, what each column means, and later, the tests. | Properties = YAML beside your SQL: descriptions, columns, tests, config. | 28 | 10 |
| b02 @0:13 | We already have one: sources dot yml. Today we add schema dot yml for the models, and seeds dot yml for the zone lookup. | Three files: models/sources.yml (sources, done), models/schema.yml (models), seeds/seeds.yml (seeds). | 24 | 9 |

## s02 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b03 @0:22 | Open the project. In models, create a new file: schema dot yml. | Open project **nyc_taxi** from Recent Projects<br>Right-click `models` → **New File** → `schema.yml` → **Save**<br>Zoom: explorer | 12 | 10 |
| b04 @0:31 | It is long, so paste it. One entry per model: a name, a description, and the columns that need explaining. The code is in the repository. | paste: models:
  - name: trips
    description: Cleaned 2025 green taxi trips; one row per trip. Rows with no distance or no charge are removed.
    columns:
      - name: pickup_at
        description: When the meter started.
      - name: pickup_zone_id
        description: TLC taxi zone where the trip started (joins taxi_zone_lookup.LocationID).
      - name: payment_type
        description: TLC payment code; 1 is credit card (see the data dictionary).
      - name: total_amount
        description: Total charged to the rider, in US dollars.
  - name: trips_per_month
    description: Trips and average fare per month and pickup borough.
    columns:
      - name: month
        description: Month of pickup.
      - name: borough
        description: Pickup borough from the zone lookup.
      - name: trips
        description: Trips that month from that borough.
  - name: top_pickup_zones
    description: The ten busiest pickup zones of 2025.
    columns:
      - name: zone_id
        description: TLC zone id; the grain of this table.
      - name: trips
        description: Trips that started in the zone.
<br>Zoom: code-mid | 26 | 10 |
| b05 @0:41 | For example, payment type: one means credit card. Anyone reading the model learns that here, not from a PDF. Save. | Point at line 10<br>Click **Save**<br>(check: `models/schema.yml` equals `../snippets/2.5/schema.yml`)<br>Zoom: code-mid | 20 | 9 |
| b06 @0:50 | Now the seed. In seeds, a new file: seeds dot yml. | Close the editor tab for `models/schema.yml`<br>Right-click `seeds` → **New File** → `seeds.yml` → **Save**<br>Zoom: explorer | 11 | 8 |
| b07 @0:58 | This one is short: the zone lookup, where it comes from, and its key column, Location ID. Save. | Type 222 characters into the editor<br>Click **Save**<br>(check: `seeds/seeds.yml` equals `../snippets/2.5/seeds.yml`)<br>Zoom: code-close | 18 | 9 |

## s03 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b08 @1:08 | Descriptions can also go into the database itself. Open dbt project dot yml, and add a models block at the end. | Close the editor tab for `seeds/seeds.yml`<br>Open `dbt_project.yml` in the Explorer<br>Zoom: explorer | 21 | 9 |
| b09 @1:16 | Under nyc taxi, persist docs, with relation and columns set to true. Save. | At the end of the file, type 81 characters<br>Click **Save**<br>(check: `dbt_project.yml` equals `../snippets/2.5/dbt_project.yml`)<br>Zoom: code-mid | 13 | 7 |
| b10 @1:23 | Run the project from the Project menu, so dbt rebuilds the models with their comments. | Open the **Project** menu → **Run**<br>Zoom: project-menu | 15 | 6 |
| b11 @1:29 | Three models, no errors. | Wait for “PASS=3”<br>Zoom: terminal-close | 4 | 3 |

## s04 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b12 @1:33 | Let's look inside DuckDB. Open the SQL Editor, pick the nyc taxi dev connection, and ask DuckDB for the columns of trips per month, with their comments. | Left bar → **SQL Editor**<br>Pick the connection **nyc_taxi_dev**<br>Type 99 characters into the editor | 27 | 12 |
| b13 @1:45 | Run it with the green arrow. | Click the green run arrow next to line 1 | 6 | 4 |
| b14 @1:49 | Each column carries the description from schema dot yml. Average fare has none, because we didn't describe it. | Zoom: sql-results<br>Card: *persist_docs* — **Descriptions in the database** — Every SQL tool now sees them. | 18 | 7 |

## s05 · slide — slide `where`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b15 @1:56 | So one description shows up in three places: in the docs site, which we build next lesson, in the database, and for everyone who reads the code. | Three places: the docs site (next lesson), database comments, and every reviewer of the code. | 27 | 10 |

## s06 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b16 @2:06 | Back in the project, open the Git tab: two new YAML files, and the change to dbt project dot yml. | Left bar → **DBT Studio**<br>Open the **Git** tab in the sidebar<br>Zoom: git-panel | 20 | 8 |
| b17 @2:14 | Stage all, type a message, describe the models and the zone seed, and commit. | Hover CHANGES and click **+** (Stage All Changes)<br>Type the commit message “Describe the models and the zone seed”<br>Click **Commit**<br>Zoom: git-panel | 14 | 10 |
| b18 @2:23 | Sync Changes, and it's on GitHub. | git_push: None<br>Zoom: git-panel | 6 | 5 |

## s07 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b19 @2:28 | To recap: properties are YAML next to your SQL. Schema dot yml describes the models, seeds dot yml the seed, and persist docs copies the descriptions into DuckDB. Next, the docs site and the DAG. | Recap: schema.yml for models, seeds.yml for seeds, persist_docs puts descriptions in DuckDB; pushed. | 35 | 14 |

## s08 · closing card (4 s, no voice)

Next · Lesson 2.6 · Docs & the DAG. Code: github.com/Nuri1977/nyc-taxi-dbt.

**Total: 345 spoken words, 2:46 rendered.**
