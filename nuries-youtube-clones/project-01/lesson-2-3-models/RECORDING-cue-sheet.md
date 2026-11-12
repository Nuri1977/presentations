# Models: your first dbt model — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `lesson-2-2-end`: a clone of what Lesson 2.2 pushed to nyc-taxi-dbt (`.gitignore`, README, `models/sources.yml`, `seeds/taxi_zone_lookup.csv`), the 12 Green Taxi 2025 parquet files in `data/raw`, and the nyc_taxi_dev connection.
- No `target/` or `logs/` folders yet, so the run in s04 creates them on camera.
- Start on the home screen with no editor tabs open. Bottom panel open on TERMINAL.

## s02 · Write trips.sql in Rosetta DBT Studio

| Listen for | Do this |
|---|---|
| "Here is the project from the last lesson.…" | On the home screen, click **nyc_taxi** under Recent Projects<br>Right-click `models` → **New File**, type `trips.sql`, click **Save** |
| "Start with a comment that says what one…" | Type:<br><br>```sql<br>-- one row per 2025 green taxi trip, obviously broken rows removed<br>select<br>``` |
| "Pick the columns we need, and give them…" | Type:<br><br>```sql<br>    VendorID              as vendor_id,<br>    lpep_pickup_datetime  as pickup_at,<br>    lpep_dropoff_datetime as dropoff_at,<br>    PULocationID          as pickup_zone_id,<br>    DOLocationID          as dropoff_zone_id,<br>``` |
| "Then the passenger count, the distance, how the…" | Type:<br><br>```sql<br>    passenger_count,<br>    trip_distance,<br>    payment_type,<br>    fare_amount,<br>    tip_amount,<br>    total_amount<br>``` |
| "Read them from the raw green trips source.…" | Type:<br><br>```sql<br>from {{ source('raw', 'green_trips') }}<br>``` |
| "Finally, keep only trips that started in 2025,…" | Type:<br><br>```sql<br>where lpep_pickup_datetime >= '2025-01-01'<br>  and lpep_pickup_datetime <  '2026-01-01'<br>  and trip_distance > 0<br>  and total_amount > 0<br>``` |
| "That is the whole model. One select, and…" | Click **Save** (top right of the editor)<br>(Check that `models/trips.sql` matches `../snippets/3.3/trips.sql`) |

## s04 · Run the model

| Listen for | Do this |
|---|---|
| "Let's run it. Above the editor, open the…" | model_menu: Run |
| "The terminal shows one model, trips, created as…" | Wait for “OK created sql view model main.trips” |

## s05 · Preview the rows

| Listen for | Do this |
|---|---|
| "To look at the rows, open the Model…" | model_menu: Preview<br>Wait for “^Preview: trips$” |
| "Eleven columns, and five hundred sixty-five thousand trips,…" | dialog_scroll_right: None |
| "Close it. The same rows stay in the…" | Click **Close**<br>Click **SQL tab**<br>Click **History tab** |

## s06 · The SQL dbt wrote, and the run history

| Listen for | Do this |
|---|---|
| "Want to see exactly what dbt sends to…" | model_menu: Compile<br>Wait for “^Compiled SQL: trips$” |
| "The Compiled SQL tab shows your select, with…" | Click **Compiled SQL tab** |
| "Close it, and open Run History. Every dbt…" | Click **Close**<br>Click **Run History** |

## s07 · Commit the model

| Listen for | Do this |
|---|---|
| "Last step: commit and push. Open the Git…" | Click the **Git** tab at the top of the sidebar |
| "Stage it with the plus button, type a…" | Hover `trips.sql` in Changes and click its **+** (Stage Changes)<br>Click the message box and type: Add the trips staging model<br>Click **Commit** |
| "Click Sync Changes, and the commit goes to…" | git_push: None |

## s07b · On GitHub

| Listen for | Do this |
|---|---|
| "On GitHub, the models folder now holds trips…" | In the browser, open https://github.com/Nuri1977/nyc-taxi-dbt/tree/main/models |
