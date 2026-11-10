# Dependencies & Jinja — voice-over script and beat sheet

dbt + DuckDB in Rosetta DBT Studio · Module 2 · dbt basics · next: Lesson 2.5 · Properties

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `lesson-2-3-end`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 1 · Lesson 2.4. Dependencies & Jinja. Badges: dbt seed, ref(), Jinja.

## s01 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | Open the nyc taxi project. First, load the zone lookup into DuckDB: open the Project menu, and choose Seed. | Open project **nyc_taxi** from Recent Projects<br>Open the **Project** menu → **Seed**<br>Zoom: project-menu | 19 | 9 |
| b02 @0:11 | dbt reads the CSV, and inserts two hundred sixty-five rows into a table called taxi zone lookup. | Wait for “OK loaded seed file main.taxi_zone_lookup”<br>Zoom: terminal-close<br>Card: *dbt seed* — **INSERT 265** — main.taxi_zone_lookup | 18 | 8 |

## s02 · slide — slide `ref`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b03 @0:19 | To use one model inside another, write ref, and the name of the model or seed. Not the table name: dbt fills that in, for whichever database you run against. | ref('trips') → "nyc_taxi_dev"."main"."trips": name the model or seed, not the table. | 30 | 11 |
| b04 @0:30 | Each ref is also a dependency. dbt draws the graph from them, and always builds trips before the models that use it. | A small graph: raw.green_trips → trips → trips_per_month and top_pickup_zones; taxi_zone_lookup → both. | 22 | 9 |

## s03 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b05 @0:39 | Right-click models, New File: trips per month dot sql. | Right-click `models` → **New File** → `trips_per_month.sql` → **Save**<br>Zoom: explorer | 10 | 7 |
| b06 @0:46 | Count the trips and the average fare for each month and pickup borough. | Type 237 characters into the editor<br>Zoom: code-close | 13 | 9 |
| b07 @0:55 | From ref trips, joined to ref taxi zone lookup, to get the borough of each pickup zone. Group by all, and save. | Type 150 characters into the editor<br>Click **Save**<br>(check: `models/trips_per_month.sql` equals `../snippets/2.4/trips_per_month.sql`)<br>Zoom: code-close | 22 | 8 |

## s04 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b08 @1:02 | A second model: top pickup zones dot sql. | Close the editor tab for `models/trips_per_month.sql`<br>Right-click `models` → **New File** → `top_pickup_zones.sql` → **Save**<br>Zoom: explorer | 8 | 9 |
| b09 @1:11 | This time, start with a Jinja variable: set top n to ten. | Type 58 characters into the editor<br>Zoom: code-close | 12 | 5 |
| b10 @1:16 | Then count the trips for each pickup zone, with the zone's name and borough, from the same two refs. | Type 241 characters into the editor<br>Zoom: code-close | 19 | 9 |
| b11 @1:25 | Order by trips, busiest first, and limit to top n. Save. | Type 51 characters into the editor<br>Click **Save**<br>(check: `models/top_pickup_zones.sql` equals `../snippets/2.4/top_pickup_zones.sql`)<br>Zoom: code-close | 11 | 5 |

## s05 · slide — slide `jinja`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b12 @1:30 | Jinja has three kinds of braces. Double curly braces print a value. Curly brace and percent run logic, like set. And curly brace and hash is a comment. | Three kinds of braces: {{ }} prints a value, {% %} runs logic, {# #} is a comment. | 28 | 10 |
| b13 @1:40 | When dbt compiles a model, all of it turns into plain SQL. Let's see that. | Compile turns Jinja into plain SQL: limit {{ top_n }} → limit 10; ref('trips') → "nyc_taxi_dev"."main"."trips". | 15 | 6 |

## s06 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b14 @1:46 | With top pickup zones open, open the Model menu, and choose Compile. | model_menu: Compile<br>Wait for “Compiled node”<br>Zoom: model-menu | 12 | 6 |
| b15 @1:52 | Studio opens the compiled SQL in a window. The first tab shows what we wrote, with the Jinja. | Wait 0.8 s<br>Zoom: center-wide | 18 | 6 |
| b16 @1:58 | Switch to Compiled SQL. Both refs became full table names in the dev database, and limit top n became limit ten. | Click **Compiled SQL tab**<br>Zoom: center-wide<br>Card: *Compiled SQL* — **limit 10** — Jinja is gone; plain SQL is left. | 21 | 8 |
| b17 @2:07 | This is the SQL DuckDB will run. Close the window. | Click **Close**<br>Zoom: center-wide | 10 | 4 |

## s07 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b18 @2:11 | Now run the whole project: Project menu, Run. | Open the **Project** menu → **Run**<br>Zoom: project-menu | 8 | 4 |
| b19 @2:15 | dbt builds trips first, and only then the two models that depend on it. Three models, no errors. | Wait for “PASS=3”<br>Zoom: terminal-close<br>Card: *dbt run* — **trips first, then the marts** — PASS=3 ERROR=0 | 18 | 7 |

## s08 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b20 @2:22 | Open the Git tab. The two new models are listed. | Close the editor tab for `models/top_pickup_zones.sql`<br>Open the **Git** tab in the sidebar<br>Zoom: git-panel | 10 | 5 |
| b21 @2:27 | Stage all, type a message, add trips per month and top pickup zones, and commit. | Hover CHANGES and click **+** (Stage All Changes)<br>Type the commit message “Add trips per month and top pickup zones”<br>Click **Commit**<br>Zoom: git-panel | 15 | 8 |
| b22 @2:35 | Sync Changes pushes it to GitHub. | git_push: None<br>Zoom: git-panel | 6 | 5 |

## s09 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b23 @2:40 | To recap: a seed loads a CSV. Ref names a model and records the dependency, so dbt runs things in the right order. Jinja adds variables and logic, and compile shows the plain SQL. Next, we describe our models with properties. | Recap: seed loaded; ref() names models and draws the graph; Jinja {{ }} {% %} {# #}; compile shows plain SQL; run in dependency order; pushed. | 41 | 16 |

## s10 · closing card (4 s, no voice)

Next · Lesson 2.5 · Properties. Code: github.com/Nuri1977/nyc-taxi-dbt.

**Total: 386 spoken words, 3:00 rendered.**
