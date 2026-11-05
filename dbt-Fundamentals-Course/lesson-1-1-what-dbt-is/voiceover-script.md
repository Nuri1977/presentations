# What dbt is (and is not) — voice-over script and beat sheet

dbt Fundamentals · Module 1 · From ETL to ELT: why dbt exists · next: Lesson 1.2 · ETL versus ELT

App: Rosetta DBT Studio 1.7.5 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `none (slides only)`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Module 1 · Lesson 1.1. What dbt is (and is not). dbt Fundamentals. Line: dbt is the T in ELT. Badges: Video + reading, 15 min, Concepts.

## s01 · slide — slide `flow`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | Let's start with the simplest possible definition. dbt is the T in ELT. | Data flow: Sources → Extract and load tool → Warehouse (dbt inside) → BI tools and apps, with E, L and T labels; dbt is the T. | 13 | 7 |
| b02 @0:09 | It transforms data that is already sitting in your warehouse. | Inside the warehouse: raw tables → dbt → clean tables, labelled already in your warehouse. | 10 | 4 |

## s02 · slide — slide `model`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b03 @0:13 | You write a select statement. That's a model. | A file card, models/customer_orders.sql, with one plain select statement. Label: that's a model. | 8 | 3 |
| b04 @0:17 | dbt wraps it in the right create table or create view statement, runs it in the right order, and tells you if something breaks. | dbt wraps it in create view customer_orders as ( … ) (marked dbt adds this), and three chips: wraps it, runs it in order, tells you if it breaks. | 24 | 9 |

## s03 · slide — slide `not`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b05 @0:25 | Notice what dbt does not do. It does not extract data from source systems. | Column dbt does not: row 1, Extract data from source systems (crossed). | 14 | 6 |
| b06 @0:31 | It does not load data into your warehouse. | Row 2: Load raw data into the warehouse (crossed). | 8 | 3 |
| b07 @0:34 | It is not a database, and it does not run your queries itself. | Row 3: Store your data or run your queries (crossed), with the note: your warehouse does that. | 13 | 4 |
| b08 @0:38 | Your warehouse does the work. dbt writes and orders the SQL, and adds the engineering around it. | Column dbt does appears: writes the SQL, orders it, adds the engineering around it. | 17 | 7 |

## s04 · slide — slide `adds`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b09 @0:45 | That engineering is the real value. | Heading: the engineering is the real value. Three icon cards, dimmed. | 6 | 3 |
| b10 @0:48 | Tests that run on every build. | Card 1 lights up: Testing, tests run on every build. | 6 | 3 |
| b11 @0:51 | Documentation generated from the code. | Card 2 lights up: Documentation, generated from the code. | 5 | 3 |
| b12 @0:54 | Everything in Git, so every change is reviewed. | Card 3 lights up: Version control, everything in Git, every change reviewed. | 8 | 4 |

## s05 · slide — slide `short`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b13 @0:58 | In short, dbt brings software engineering practice to SQL. | dbt in one sentence: dbt compiles SQL select statements and Jinja into runnable code, executes it in dependency order inside your data platform, and adds testing, documentation and lineage. | 9 | 5 |
| b14 @1:03 | A useful comparison: dbt is to SQL what a build system is to source code. You describe what each piece should look like, and dbt works out the order and builds it. | Below it: dbt is to SQL what a build system is to source code. | 32 | 11 |

## s06 · closing card (4 s, no voice)

Next · Lesson 1.2 · ETL versus ELT, with the Rosetta logo.

**Total: 173 spoken words, 1:18 rendered.**
