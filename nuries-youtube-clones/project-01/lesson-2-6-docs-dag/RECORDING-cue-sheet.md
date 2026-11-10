# Docs & the DAG — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `lesson-2-5-end`: a clone of what Lesson 2.5 pushed, the parquet files in data/raw, the nyc_taxi_dev connection, and the database after dbt seed + dbt run (off camera).

## s01 · A model with two refs

| Listen for | Do this |
|---|---|
| "Open the project, and create one more model…" | On the home screen, click **nyc_taxi** under Recent Projects<br>Right-click `models` → **New File**, type `monthly_summary.sql`, click **Save** |
| "First, a block called totals: the trips per…" | Type:<br><br>```sql<br>-- one row per month: total trips and the share paid by card<br>with totals as (<br>    select month, sum(trips) as total_trips<br>    from {{ ref('trips_per_month') }}<br>    group by month<br>),<br>``` |
| "Then a block called card: the trips paid…" | Type:<br><br>```sql<br>card as (<br>    select date_trunc('month', pickup_at) as month, count(*) as card_trips<br>    from {{ ref('trips') }}<br>    where payment_type = 1   -- credit card<br>    group by month<br>)<br>``` |
| "Join them by month, and work out the…" | Type:<br><br>```sql<br>select<br>    month,<br>    total_trips,<br>    card_trips,<br>    round(100.0 * card_trips / total_trips, 1) as pct_card<br>from totals<br>join card using (month)<br>order by month<br>```<br>Click **Save** (top right of the editor)<br>(Check that `models/monthly_summary.sql` matches `../snippets/2.6/monthly_summary.sql`) |
| "Describe it too: at the end of schema…" | In the Explorer, open `models/schema.yml` (expand each folder on the way)<br>paste: {'text': "  - name: monthly_summary\n    description: One row per month of 2025 with total trips and the share paid by card.\n    columns:\n      - name: month\n        description: Month of pickup; the grain.\n      - name: pct_card\n        description: Percent of the month's trips paid by credit card.\n", 'end': True}<br>Click **Save** (top right of the editor)<br>(Check that `models/schema.yml` matches `../snippets/2.6/schema.yml`) |

## s03 · Run a model and everything upstream

| Listen for | Do this |
|---|---|
| "Back in monthly summary, open the Model menu,…" | Close the editor tab for `models/schema.yml` (its ×)<br>model_menu: Run +model (Upstream) |
| "Three models, in DAG order: trips, trips per…" | Wait for “PASS=3” |

## s04 · Generate and serve the docs

| Listen for | Do this |
|---|---|
| "Now the docs. Open the Project menu, and…" | Open the **Project** menu (arrow next to Project, top right) → **Generate Docs**<br>Wait for “Catalog written” |
| "Then Project, Serve Docs. Studio starts a local…" | Open the **Project** menu (arrow next to Project, top right) → **Serve Docs**<br>Wait for “Serving docs at” |

## s05 · The docs site

| Listen for | Do this |
|---|---|
| "In the browser, open localhost, port eighty eighty,…" | In the browser, open http://127.0.0.1:8080/#!/model/model.nyc_taxi.monthly_summary |
| "The button at the bottom right opens the…" | Click **View Lineage Graph** |

## s06 · Commit and push

| Listen for | Do this |
|---|---|
| "Back in Studio, the Git tab shows the…" | Close the editor tab for `models/monthly_summary.sql` (its ×)<br>Click the **Git** tab at the top of the sidebar |
| "Stage all, type a message, add the monthly…" | Hover CHANGES and click **+** (Stage All Changes)<br>Click the message box and type: Add the monthly summary<br>Click **Commit** |
| "Sync Changes, and it's on GitHub.…" | git_push: None |
