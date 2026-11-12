# Connect a dbt project to the lake — voice-over script and beat sheet

Data Lakes with DuckLake in Rosetta DBT Studio · Module 6 · dbt on DuckLake · next: Lesson 6.2 · Staging models for blocks and transactions

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `lesson-5-3-end`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 2 · Lesson 6.1. Connect a dbt project to the lake.

## s01 · slide — slide `plan`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | In this module, dbt builds models on top of our lake. It reads the raw tables, and writes its models into the lake too, in the schema main. | dbt reads raw.blocks and raw.transactions and writes models into eth_lake.main. | 28 | 9 |
| b02 @0:12 | dbt runs its own DuckDB, inside dbt duckdb. So it needs to attach the lake itself. That is one change, in profiles dot yml. | dbt runs its own DuckDB (1.5.6); it attaches the lake through profiles.yml. | 24 | 11 |

## s02 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b03 @0:22 | In DBT Studio, open profiles dot yml. Today it points at the small dev database from Lesson 2.1. | Left bar → **DBT Studio**<br>Open `profiles.yml` in the Explorer<br>Zoom: code-mid | 19 | 8 |
| b04 @0:30 | Replace the output. Path is a small local DuckDB file for dbt's own session. Attach adds the lake: the ducklake prefix and the catalog file, as eth lake. Database eth lake makes the lake dbt's target, in schema main. And one thread, the safe choice with a single-file catalog: several dbt threads writing to one DuckLake can still trip over each other. | paste: {'replace': True, 'text': 'ethereum_lake:\n  target: dev\n  outputs:\n    dev:\n      type: duckdb\n      path: lake/dbt_session.duckdb\n      attach:\n        - path: "ducklake:lake/eth_catalog.duckdb"\n          alias: eth_lake\n      database: eth_lake\n      schema: main\n      threads: 1\n'}<br>Click **Save**<br>(check: `profiles.yml` equals `../snippets/6.1/profiles.yml`)<br>Zoom: code-mid | 63 | 25 |
| b05 @0:55 | Check it: in the command box under the terminal, run dbt debug. dbt finds the project and the profile, attaches the lake, and connects. All checks passed. | In the command box under the terminal, type `dbt debug` and press Enter<br>Zoom: terminal-close<br>Card: *dbt debug* — **All checks passed!** — dbt can open eth_lake | 27 | 13 |

## s03 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b06 @1:08 | Commit the profile: point dbt at the lake. And push. | Close the editor tab for `profiles.yml`<br>Open the **Git** tab in the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Type the commit message “Point dbt at the lake”<br>Click **Commit**<br>git_push: None<br>Zoom: git-panel | 10 | 17 |

## s04 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b07 @1:26 | Now the rule for this module. Open Data Lake, and the eth lake instance. Studio opens the lake, and keeps it open. | Left bar → **DataLake**<br>Click **eth_lake**<br>Zoom: center-wide | 22 | 8 |
| b08 @1:34 | Back in DBT Studio, run dbt debug again. This time it fails: conflicting lock is held in Rosetta DBT Studio. A DuckDB catalog file can be opened by one program at a time. | Left bar → **DBT Studio**<br>In the command box under the terminal, type `dbt debug` and press Enter<br>Zoom: terminal-close<br>Card: *dbt debug* — **Conflicting lock is held** — the lake is open in Studio | 33 | 16 |

## s05 · slide — slide `rule`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b09 @1:50 | So in this module, we always run dbt first, and open the lake in Studio afterwards, to look at the result. | Rule: run dbt first; open the Data Lake screens or the SQL Editor on the lake afterwards. | 21 | 8 |
| b10 @1:58 | Studio keeps the lake open until you quit it. To run dbt again after looking at the lake, quit Studio, and open it again. With a PostgreSQL catalog, this limit goes away. | To run dbt again after that: quit Studio and open it again. | 32 | 12 |

## s06 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b11 @2:10 | To recap: profiles dot yml attaches the lake and makes it dbt's database, and dbt debug passes. One program at a time: dbt first, then the lake screens. Next: staging models. | Recap: profiles.yml attaches the lake as dbt's database; dbt debug passes; one program at a time: dbt first, then Studio's lake screens. | 31 | 15 |

## s07 · closing card (4 s, no voice)

Next · Lesson 6.2 · Staging models.

**Total: 310 spoken words, 2:29 rendered.**
