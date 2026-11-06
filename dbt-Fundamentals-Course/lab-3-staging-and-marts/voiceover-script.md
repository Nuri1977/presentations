# Staging and marts on DuckDB (walkthrough) — voice-over script and beat sheet

dbt Fundamentals · Module 3 · Building models · next: Module 4 · Lesson 4.1 · Data tests

App: Rosetta DBT Studio 1.7.5 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `lab-1-end`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Lab 3 walkthrough. Staging and marts on DuckDB. dbt Fundamentals, Module 3. Badges: Rosetta DBT Studio 1.7.5, DuckDB, Hands-on.

## s01 · slide — slide `plan`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | In this walkthrough we do Lab 3 in Rosetta DBT Studio. We declare the raw tables as sources, build three staging models and two marts, and run them on DuckDB. | The target graph: three raw sources → three staging models → fct_orders and dim_customers. | 30 | 11 |
| b02 @0:14 | You need the end of Lab 1: the raw customers, orders and payments tables in your DuckDB file, and the dbt course project with an empty models folder. | Before you start: the Lab 1 data in course.duckdb, and an empty dbt_course project. | 28 | 11 |

## s02 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b03 @0:25 | Open the dbt course project. The models folder is still empty. | Open project **dbt_course** from Recent Projects<br>Point at `models` in the Explorer | 11 | 5 |
| b04 @0:30 | Right-click models, choose New Folder, and name it staging. Then make a second folder, called marts. | Right-click `models` → **New Folder** → `staging` → **Save**<br>Right-click `models` → **New Folder** → `marts` → **Save** | 17 | 11 |
| b05 @0:41 | In staging, create the sources file. Its name starts with an underscore, so it stays at the top of the folder. | Right-click `models/staging` → **New File** → `_sources.yml` → **Save** | 21 | 7 |
| b06 @0:48 | It declares one source called raw, in the schema raw, with three tables: customers, orders and payments. | Type 131 characters into the editor | 17 | 7 |
| b07 @0:55 | Save the file. From now on, models read raw data through source, and dbt can trace lineage all the way back to these tables. | Click **Save**<br>Zoom: editor-code<br>Card: *Sources* — **Declare once** — Then read raw tables with source('raw', 'orders'). | 24 | 9 |

Open the dbt course project. The models folder is still empty. Right-click models, choose New Folder, and name it staging. Then make a second folder, called marts. In staging, create the sources file. Its name starts with an underscore, so it stays at the top of the folder. It declares one source called raw, in the schema raw, with three tables: customers, orders and payments. Save the file. From now on, models read raw data through source, and dbt can trace lineage all the way back to these tables.

## s03 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b08 @1:04 | Next, one staging model per source table, starting with staging customers. | Right-click `models/staging` → **New File** → `stg_customers.sql` → **Save** | 11 | 7 |
| b09 @1:11 | Light cleanup only. Rename id to customer id, and cast created at to a date. No joins, and no business logic. Save it. | Type 153 characters into the editor<br>Click **Save** | 23 | 10 |
| b10 @1:21 | Staging orders follows the same pattern: rename the id, cast the order date, and save. | Right-click `models/staging` → **New File** → `stg_orders.sql` → **Save**<br>Type 134 characters into the editor<br>Click **Save** | 15 | 12 |
| b11 @1:33 | Staging payments renames the method, and turns cents into dollars. Save that one too. | Right-click `models/staging` → **New File** → `stg_payments.sql` → **Save**<br>Type 145 characters into the editor<br>Click **Save** | 14 | 13 |

Save the file. From now on, models read raw data through source, and dbt can trace lineage all the way back to these tables. Next, one staging model per source table, starting with staging customers. Light cleanup only. Rename id to customer id, and cast created at to a date. No joins, and no business logic. Save it. Staging orders follows the same pattern: rename the id, cast the order date, and save. Staging payments renames the method, and turns cents into dollars. Save that one too.


## s04 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b12 @1:46 | Now the marts. In the marts folder, create fact orders. | Right-click `models/marts` → **New File** → `fct_orders.sql` → **Save** | 10 | 7 |
| b13 @1:53 | It is the model from Lesson 3.2. First the orders, from staging, through ref. | Type 62 characters into the editor | 15 | 6 |
| b14 @1:59 | Then the payments, added up per order. | Type 109 characters into the editor | 7 | 4 |
| b15 @2:03 | And one row per order, with its amount. Save the model. | Type 150 characters into the editor<br>Click **Save** | 11 | 7 |
| b16 @2:10 | Next, dim customers: one row per customer. | Right-click `models/marts` → **New File** → `dim_customers.sql` → **Save** | 7 | 7 |
| b17 @2:17 | It keeps the customer columns, and adds the first order date, the number of orders, and the lifetime value. | Type 204 characters into the editor | 19 | 8 |
| b18 @2:24 | Those come from fact orders, joined on customer id. Because of this ref, dbt will always build fact orders first. Save it. | Type 110 characters into the editor<br>Click **Save** | 22 | 9 |

## s05 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b19 @2:33 | Open dbt project dot yml, and go to the end of the file. | Open `dbt_project.yml` in the Explorer | 13 | 5 |
| b20 @2:39 | Add a models block. Everything in staging becomes a view, and everything in marts becomes a table. | At the end of the file, type 100 characters | 17 | 7 |
| b21 @2:45 | Save it. These are folder defaults, and a single model can still override them. | Click **Save**<br>Zoom: editor-code | 14 | 6 |

## s06 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b22 @2:51 | Now open the Project menu, and choose Compile. | Open the **Project** menu → **Compile**<br>Wait for manifest | 8 | 5 |
| b23 @2:56 | In target, compiled, open fact orders. Every ref has become a real table name in your DuckDB file. | Open `target/compiled/dbt_course/models/marts/fct_orders.sql` in the Explorer<br>Point at line 2<br>Zoom: editor-code | 18 | 8 |
| b24 @3:04 | Then the Project menu again, and Run. | Open the **Project** menu → **Run**<br>Wait for run | 7 | 5 |
| b25 @3:09 | Five models, built in dependency order: three views and two tables. The last line says pass five, error zero. | Zoom: terminal<br>Card: *dbt run* — **3 views · 2 tables** — Built in dependency order. PASS=5, ERROR=0. | 19 | 8 |

## s07 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b26 @3:16 | Let's check the data. Open the SQL Editor, pick the course connection, and ask for each customer's order count and lifetime value. | Left bar → **SQL Editor**<br>Pick the connection **course**<br>Type 108 characters into the editor | 22 | 13 |
| b27 @3:29 | Run it with the green arrow next to the line. | Click the green run arrow next to line 1 | 10 | 4 |
| b28 @3:33 | Ava comes first, with three orders and one hundred and two dollars. Farid has none. That is exactly the expected result on the lab page. | Zoom: sql-results<br>Card: *Expected result* — **It matches** — Ava 102 · Dmitri 55 · Chloe 50 · Ben 23 · Elena 12 · Farid 0 | 25 | 9 |

## s08 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b29 @3:42 | Last, the lineage. Back in the project, open dim customers, and the Lineage tab. | Left bar → **DBT Studio**<br>Open `models/marts/dim_customers.sql` in the Explorer<br>Open the **LINEAGE** tab in the bottom panel | 14 | 10 |
| b30 @3:53 | Maximize it, and set the depth to three. | Click **Maximize** on the lineage panel<br>Set lineage **Depth** to 3<br>Fit the graph to the view | 8 | 10 |
| b31 @4:03 | That is the whole lab in one picture: the raw sources on the left, the staging views in the middle, and the two marts on the right. | — | 27 | 8 |

## s09 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b32 @4:11 | That is Lab 3. The raw data stayed untouched, the staging layer cleaned it once, and the marts were built in the right order by one command. | Checklist: sources declared; staging views; marts as tables; built in order by one command; result matches. | 27 | 9 |
| b33 @4:20 | Before you move on, answer the reflection questions on the lab page. Try changing staging orders, and run it with a plus sign after the name, to rebuild everything downstream. | Reflection: compare customer_summary from Lab 1 with dim_customers; which models are views and which are tables; change stg_orders and run dbt run --select stg_orders+. | 30 | 12 |

## s10 · closing card (4 s, no voice)

Next · Module 4 · Data tests, with the Rosetta logo.

**Total: 561 spoken words, 4:36 rendered.**
