# Properties: describe your models — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `lesson-2-4-end`: a clone of what Lesson 2.4 pushed, the parquet files in data/raw, the nyc_taxi_dev connection, and the database after dbt seed + dbt run (off camera), as 2.4 left it.

## s02 · schema.yml and seeds.yml

| Listen for | Do this |
|---|---|
| "Open the project. In models, create a new…" | On the home screen, click **nyc_taxi** under Recent Projects<br>Right-click `models` → **New File**, type `schema.yml`, click **Save** |
| "It is long, so paste it. One entry…" | paste: models:<br>  - name: trips<br>    description: Cleaned 2025 green taxi trips; one row per trip. Rows with no distance or no charge are removed.<br>    columns:<br>      - name: pickup_at<br>        description: When the meter started.<br>      - name: pickup_zone_id<br>        description: TLC taxi zone where the trip started (joins taxi_zone_lookup.LocationID).<br>      - name: payment_type<br>        description: TLC payment code; 1 is credit card (see the data dictionary).<br>      - name: total_amount<br>        description: Total charged to the rider, in US dollars.<br>  - name: trips_per_month<br>    description: Trips and average fare per month and pickup borough.<br>    columns:<br>      - name: month<br>        description: Month of pickup.<br>      - name: borough<br>        description: Pickup borough from the zone lookup.<br>      - name: trips<br>        description: Trips that month from that borough.<br>  - name: top_pickup_zones<br>    description: The ten busiest pickup zones of 2025.<br>    columns:<br>      - name: zone_id<br>        description: TLC zone id; the grain of this table.<br>      - name: trips<br>        description: Trips that started in the zone.<br> |
| "For example, payment type: one means credit card.…" | Point at line 10<br>Click **Save** (top right of the editor)<br>(Check that `models/schema.yml` matches `../snippets/2.5/schema.yml`) |
| "Now the seed. In seeds, a new file:…" | Close the editor tab for `models/schema.yml` (its ×)<br>Right-click `seeds` → **New File**, type `seeds.yml`, click **Save** |
| "This one is short: the zone lookup, where…" | Type:<br><br>```sql<br>seeds:<br>  - name: taxi_zone_lookup<br>    description: TLC taxi zones, from the Taxi Zone Lookup Table on the TLC site.<br>    columns:<br>      - name: LocationID<br>        description: Zone id used by PULocationID and DOLocationID.<br>```<br>Click **Save** (top right of the editor)<br>(Check that `seeds/seeds.yml` matches `../snippets/2.5/seeds.yml`) |

## s03 · Keep the descriptions in the database

| Listen for | Do this |
|---|---|
| "Descriptions can also go into the database itself.…" | Close the editor tab for `seeds/seeds.yml` (its ×)<br>In the Explorer, open `dbt_project.yml` (expand each folder on the way) |
| "Under nyc taxi, persist docs, with relation and…" | Click at the end of the file and type:<br><br>```yaml<br><br>models:<br>  nyc_taxi:<br>    +persist_docs:<br>      relation: true<br>      columns: true<br>```<br>Click **Save** (top right of the editor)<br>(Check that `dbt_project.yml` matches `../snippets/2.5/dbt_project.yml`) |
| "Run the project from the Project menu, so…" | Open the **Project** menu (arrow next to Project, top right) → **Run** |
| "Three models, no errors.…" | Wait for “PASS=3” |

## s04 · Descriptions inside DuckDB

| Listen for | Do this |
|---|---|
| "Let's look inside DuckDB. Open the SQL Editor,…" | In the left bar, click **SQL Editor**<br>Open the connection list (top left) and pick **nyc_taxi_dev**<br>Type:<br><br>```sql<br>select table_name, column_name, comment from duckdb_columns() where table_name = 'trips_per_month';<br>``` |
| "Run it with the green arrow.…" | Click the green ▶ arrow next to line 1 |
| "Each column carries the description from schema dot…" | Hold; nothing moves |

## s06 · Commit and push

| Listen for | Do this |
|---|---|
| "Back in the project, open the Git tab:…" | In the left bar, click **DBT Studio**<br>Click the **Git** tab at the top of the sidebar |
| "Stage all, type a message, describe the models…" | Hover CHANGES and click **+** (Stage All Changes)<br>Click the message box and type: Describe the models and the zone seed<br>Click **Commit** |
| "Sync Changes, and it's on GitHub.…" | git_push: None |
