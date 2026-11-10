# Docs & the DAG — voice-over script and beat sheet

dbt + DuckDB in Rosetta DBT Studio · Module 2 · dbt basics · next: Lesson 2.7 · Materializations

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `lesson-2-5-end`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 1 · Lesson 2.6. Docs & the DAG. Badges: ref() x2, lineage, dbt docs.

## s01 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | Open the project, and create one more model in models: monthly summary dot sql. | Open project **nyc_taxi** from Recent Projects<br>Right-click `models` → **New File** → `monthly_summary.sql` → **Save**<br>Zoom: explorer | 14 | 11 |
| b02 @0:13 | First, a block called totals: the trips per month, from ref trips per month. | Type 182 characters into the editor<br>Zoom: code-close | 14 | 7 |
| b03 @0:20 | Then a block called card: the trips paid by credit card each month, straight from ref trips. | Type 178 characters into the editor<br>Zoom: code-close | 17 | 7 |
| b04 @0:26 | Join them by month, and work out the percent paid by card. Save. | Type 161 characters into the editor<br>Click **Save**<br>(check: `models/monthly_summary.sql` equals `../snippets/2.6/monthly_summary.sql`)<br>Zoom: code-close | 13 | 7 |
| b05 @0:34 | Describe it too: at the end of schema dot yml, paste the entry for monthly summary, and save. | Open `models/schema.yml` in the Explorer<br>paste: {'text': "  - name: monthly_summary\n    description: One row per month of 2025 with total trips and the share paid by card.\n    columns:\n      - name: month\n        description: Month of pickup; the grain.\n      - name: pct_card\n        description: Percent of the month's trips paid by credit card.\n", 'end': True}<br>Click **Save**<br>(check: `models/schema.yml` equals `../snippets/2.6/schema.yml`)<br>Zoom: code-mid | 18 | 7 |

## s02 · slide — slide `dag`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b06 @0:40 | All those refs form a graph: the DAG. Directed, because every arrow points one way. Acyclic, because no model can depend on itself. | The project's DAG: raw.green_trips → trips → trips_per_month, top_pickup_zones; taxi_zone_lookup → both; trips_per_month + trips → monthly_summary. | 23 | 9 |
| b07 @0:49 | dbt uses it for the build order, to run independent models in parallel, and to show you what a change affects. | Three uses: build order; independent models run in parallel; impact: change trips, and you see everything downstream. | 21 | 8 |

## s03 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b08 @0:57 | Back in monthly summary, open the Model menu, and choose Run plus model, upstream. That runs this model, and everything it depends on. | Close the editor tab for `models/schema.yml`<br>model_menu: Run +model (Upstream)<br>Zoom: model-menu | 23 | 9 |
| b09 @1:06 | Three models, in DAG order: trips, trips per month, then monthly summary. | Wait for “PASS=3”<br>Zoom: terminal-close<br>Card: *+monthly_summary* — **3 models, in DAG order** — trips → trips_per_month → monthly_summary | 12 | 5 |

## s04 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b10 @1:11 | Now the docs. Open the Project menu, and choose Generate Docs. dbt reads the project and the database, and writes a small website into target. | Open the **Project** menu → **Generate Docs**<br>Wait for “Catalog written”<br>Zoom: project-menu | 25 | 11 |
| b11 @1:22 | Then Project, Serve Docs. Studio starts a local web server, on port eighty eighty. | Open the **Project** menu → **Serve Docs**<br>Wait for “Serving docs at”<br>Zoom: project-menu | 14 | 6 |

## s05 · browser — Browser

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b12 @1:29 | In the browser, open localhost, port eighty eighty, and pick monthly summary. Here is the description from schema dot yml, every column, and what the model depends on. | Browser: open http://127.0.0.1:8080/#!/model/model.nyc_taxi.monthly_summary | 28 | 11 |
| b13 @1:40 | The button at the bottom right opens the lineage graph: the whole DAG, from the raw source and the seed, to monthly summary. | Click **View Lineage Graph** | 23 | 8 |

## s06 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b14 @1:48 | Back in Studio, the Git tab shows the new model, and the change to schema dot yml. | Close the editor tab for `models/monthly_summary.sql`<br>Open the **Git** tab in the sidebar<br>Zoom: git-panel | 17 | 6 |
| b15 @1:54 | Stage all, type a message, add the monthly summary, and commit. | Hover CHANGES and click **+** (Stage All Changes)<br>Type the commit message “Add the monthly summary”<br>Click **Commit**<br>Zoom: git-panel | 11 | 9 |
| b16 @2:02 | Sync Changes, and it's on GitHub. | git_push: None<br>Zoom: git-panel | 6 | 5 |

## s07 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b17 @2:08 | To recap: refs form the DAG, and dbt uses it for order and impact. Run plus model builds a model with everything upstream. And two clicks give you a docs site, with descriptions and the lineage graph. Next, views or tables: materializations. | Recap: refs form the DAG; run +model runs everything upstream; Generate Docs + Serve Docs; lineage graph; pushed. | 42 | 17 |

## s08 · closing card (4 s, no voice)

Next · Lesson 2.7 · Materializations. Code: github.com/Nuri1977/nyc-taxi-dbt.

**Total: 321 spoken words, 2:28 rendered.**
