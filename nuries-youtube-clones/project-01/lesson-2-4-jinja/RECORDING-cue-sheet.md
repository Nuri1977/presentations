# Dependencies & Jinja — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `lesson-2-3-end`: a clone of what Lesson 2.3 pushed (adds models/trips.sql), the 12 parquet files in data/raw, and the nyc_taxi_dev connection. The trips view is built again by Project ▸ Run in this lesson.

## s01 · Load the seed

| Listen for | Do this |
|---|---|
| "Open the nyc taxi project. First, load the…" | On the home screen, click **nyc_taxi** under Recent Projects<br>Open the **Project** menu (arrow next to Project, top right) → **Seed** |
| "dbt reads the CSV, and inserts two hundred…" | Wait for “OK loaded seed file main.taxi_zone_lookup” |

## s03 · Trips per month

| Listen for | Do this |
|---|---|
| "Right-click models, New File: trips per month dot…" | Right-click `models` → **New File**, type `trips_per_month.sql`, click **Save** |
| "Count the trips and the average fare for…" | Type:<br><br>```sql<br>-- trips per month and pickup borough<br>select<br>    date_trunc('month', t.pickup_at) as month,<br>    z.Borough                        as borough,<br>    count(*)                         as trips,<br>    round(avg(t.fare_amount), 2)     as avg_fare<br>``` |
| "From ref trips, joined to ref taxi zone…" | Type:<br><br>```sql<br>from {{ ref('trips') }} as t<br>left join {{ ref('taxi_zone_lookup') }} as z<br>    on t.pickup_zone_id = z.LocationID<br>group by all<br>order by month, borough<br>```<br>Click **Save** (top right of the editor)<br>(Check that `models/trips_per_month.sql` matches `../snippets/2.4/trips_per_month.sql`) |

## s04 · Top pickup zones, with a Jinja variable

| Listen for | Do this |
|---|---|
| "A second model: top pickup zones dot sql.…" | Close the editor tab for `models/trips_per_month.sql` (its ×)<br>Right-click `models` → **New File**, type `top_pickup_zones.sql`, click **Save** |
| "This time, start with a Jinja variable: set…" | Type:<br><br>```sql<br>-- the busiest pickup zones of 2025<br>{% set top_n = 10 %}<br>``` |
| "Then count the trips for each pickup zone,…" | Type:<br><br>```sql<br>select<br>    t.pickup_zone_id as zone_id,<br>    z.Zone           as zone,<br>    z.Borough        as borough,<br>    count(*)         as trips<br>from {{ ref('trips') }} as t<br>join {{ ref('taxi_zone_lookup') }} as z<br>    on t.pickup_zone_id = z.LocationID<br>``` |
| "Order by trips, busiest first, and limit to…" | Type:<br><br>```sql<br>group by all<br>order by trips desc<br>limit {{ top_n }}<br>```<br>Click **Save** (top right of the editor)<br>(Check that `models/top_pickup_zones.sql` matches `../snippets/2.4/top_pickup_zones.sql`) |

## s06 · Compile: see the plain SQL

| Listen for | Do this |
|---|---|
| "With top pickup zones open, open the Model…" | model_menu: Compile<br>Wait for “Compiled node” |
| "Studio opens the compiled SQL in a window.…" | Wait 0.8 s |
| "Switch to Compiled SQL. Both refs became full…" | Click **Compiled SQL tab** |
| "This is the SQL DuckDB will run. Close…" | Click **Close** |

## s07 · Run in dependency order

| Listen for | Do this |
|---|---|
| "Now run the whole project: Project menu, Run.…" | Open the **Project** menu (arrow next to Project, top right) → **Run** |
| "dbt builds trips first, and only then the…" | Wait for “PASS=3” |

## s08 · Commit and push

| Listen for | Do this |
|---|---|
| "Open the Git tab. The two new models…" | Close the editor tab for `models/top_pickup_zones.sql` (its ×)<br>Click the **Git** tab at the top of the sidebar |
| "Stage all, type a message, add trips per…" | Hover CHANGES and click **+** (Stage All Changes)<br>Click the message box and type: Add trips per month and top pickup zones<br>Click **Commit** |
| "Sync Changes pushes it to GitHub.…" | git_push: None |
