# Models, ref() and the DAG — voice-over script and beat sheet

dbt Fundamentals · Module 3 · Building models · next: Lesson 3.3 · Sources and the staging layer

Recorded in Rosetta DBT Studio 1.7.5 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `lesson-3-2-start`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Module 3 · Lesson 3.2. Models, ref() and the DAG. dbt Fundamentals. Badges: Rosetta DBT Studio 1.7.5, dbt Core 1.12, DuckDB.

## s01 · slide — slide `model`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | A model is a select statement in a .sql file. | A file card, stg_orders.sql, holding its select statement. | 10 | 4 |
| b02 @0:07 | The file name becomes the name of the table or view it builds. | An arrow from the file to a database object card: view stg_orders. | 13 | 4 |
| b03 @0:11 | You never write create table, or create view. dbt writes that part for you. | Above the select, a struck-through line create view stg_orders as, labelled dbt writes this. | 14 | 6 |

## s02 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b04 @0:17 | Here is one in Rosetta DBT Studio. Open the project, then the models folder, then staging, and pick the staging orders model. | Open project **dbt_course** from Recent Projects<br>Open `models/staging/stg_orders.sql` in the Explorer | 22 | 9 |
| b05 @0:26 | It is a single select over the raw orders table: four columns, renamed and cast. There is no create statement, and no insert. | Zoom: editor-code<br>Card: *A model* — **One file, one select** — stg_orders.sql builds the view stg_orders. | 23 | 9 |
| b06 @0:35 | The source call on the last line points at the raw table. Sources are the next lesson. | Point at line 6 | 17 | 6 |

## s03 · slide — slide `ref`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b07 @0:40 | The second idea is ref. When one model needs another, you do not write the table name. | Two model boxes, stg_orders and fct_orders. Inside fct_orders, a hard-coded name main.stg_orders, crossed out. | 17 | 6 |
| b08 @0:46 | You write double curly braces, ref, and the model name. | The crossed-out name is replaced by {{ ref('stg_orders') }}, with the braces, ref and the model name each labelled. | 10 | 4 |
| b09 @0:50 | That does two things. It resolves to the right table in whichever environment you are running in. | Point 1, Resolves the name: dev compiles to "course"."main"."stg_orders", another target to its own schema (marked as an example). | 17 | 6 |
| b10 @0:57 | And it tells dbt that this model depends on that one. | Point 2, Records a dependency: an arrow draws from stg_orders to fct_orders. | 11 | 4 |

## s04 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b11 @1:01 | Let's use it. In the marts folder, create a new file for a model called fact orders. | Right-click `models/marts` → **New File** → `fct_orders.sql` → **Save** | 17 | 6 |
| b12 @1:07 | First the orders, straight from the staging orders model, through ref. | Type 62 characters into the editor | 11 | 5 |
| b13 @1:12 | Then the payments, added up per order, from the staging payments model. | Type 109 characters into the editor | 12 | 5 |
| b14 @1:16 | Finally, one row per order, with its total amount. Notice there is not a single hard-coded table name in this file. | Type 150 characters into the editor | 22 | 8 |
| b15 @1:24 | Save it. Then open the Project menu, and choose Compile. | Click **Save**<br>Open the **Project** menu → **Compile** | 10 | 5 |
| b16 @1:29 | Compile turns every model into plain SQL. Nothing runs in the database. | Wait for manifest<br>Zoom: terminal<br>Card: *Compile* — **Jinja in, SQL out** — The compiled SQL is written to the target folder. | 12 | 6 |
| b17 @1:34 | The result goes into the target folder. Open the compiled copy of fact orders, and look at what ref became. | Open `target/compiled/dbt_course/models/marts/fct_orders.sql` in the Explorer | 20 | 7 |
| b18 @1:41 | The curly braces are gone. In their place is the full name of the staging orders view: this database, this schema, this model. | Point at line 2<br>Zoom: editor-code<br>Card: *What ref became* — **"course"."main"."stg_orders"** — database · schema · model | 23 | 8 |
| b19 @1:50 | Point the project at another environment, and the same model compiles to that environment's table instead. | — | 16 | 7 |

## s05 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b20 @1:57 | Close the compiled copy, which takes you back to fact orders, and open the Lineage tab. | Close the editor tab for `target/compiled/dbt_course/models/marts/fct_orders.sql`<br>Open the **LINEAGE** tab in the bottom panel | 16 | 6 |
| b21 @2:03 | Studio draws this graph from your refs. The two staging models feed fact orders, and the panel on the right lists what it depends on. | Zoom: bottom-panel<br>Card: *Lineage* — **Drawn from your refs** — Nothing to keep up to date by hand. | 25 | 8 |
| b21b @2:12 | Raise the depth to two, and the raw tables appear behind the staging models. | Set lineage **Depth** to 2<br>Zoom: lineage-wide | 14 | 5 |

## s06 · slide — slide `dag`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b22 @2:17 | That graph is a directed acyclic graph, a DAG. Directed, because every dependency points one way. Acyclic, because nothing can depend on itself, even through other models. | The DAG builds left to right: raw.customers, raw.orders, raw.payments, then the three staging models, then fct_orders, then dim_customers dimmed and tagged Lab 3. | 27 | 11 |
| b23 @2:28 | dbt uses the graph to run models in a safe order. | Order numbers 1, 2, 3 appear above the layers. | 11 | 5 |
| b24 @2:33 | It runs independent models in parallel. | The three staging models highlight together, labelled in parallel. | 6 | 3 |
| b25 @2:36 | And it shows you lineage: where each number comes from, and what breaks if you change it. | The path from raw.payments through stg_payments to fct_orders lights up, labelled lineage. | 17 | 6 |

## s07 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b26 @2:42 | That is the pain from Lab 1, solved. You do not manage the order. You declare the dependencies, and dbt does the rest. | Recap: A model is one select in one file. ref() resolves the name and records the dependency. dbt builds the DAG and works out the order. | 23 | 8 |

## s08 · closing card (4 s, no voice)

Next · Lesson 3.3 · Sources and the staging layer, with the Rosetta logo.

**Total: 436 spoken words, 2:54 rendered.**
