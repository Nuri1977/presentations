# Staging models for blocks and transactions — voice-over script and beat sheet

Data Lakes with DuckLake in Rosetta DBT Studio · Module 6 · dbt on DuckLake · next: Lesson 6.3 · Marts, built incrementally

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `lesson-6-1-end`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 2 · Lesson 6.2. Staging models.

## s01 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | In DBT Studio, in the models folder, create sources dot yml. A source called raw, in database eth lake, schema raw, with the two tables we loaded: blocks and transactions. | Left bar → **DBT Studio**<br>Right-click `models` → **New File** → `sources.yml` → **Save**<br>paste: {'text': 'sources:\n  - name: raw\n    database: eth_lake\n    schema: raw\n    tables:\n      - name: blocks\n      - name: transactions\n'}<br>Click **Save**<br>(check: `models/sources.yml` equals `../snippets/6.2/sources.yml`)<br>Zoom: code-mid | 30 | 12 |

## s02 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b02 @0:15 | Make a folder models, staging, and in it stg blocks dot sequel. A view that renames the columns clearly, computes gas used in percent, and turns the base fee from wei into gwei. | Close the editor tab for `models/sources.yml`<br>Right-click `models` → **New Folder** → `staging` → **Save**<br>Right-click `models/staging` → **New File** → `stg_blocks.sql` → **Save**<br>paste: {'text': "{{ config(materialized='view') }}\n\nselect\n    number as block_number,\n    date as block_date,\n    timestamp as block_time,\n    fee_recipient,\n    transaction_count,\n    gas_used,\n    gas_limit,\n    round(100.0 * gas_used / gas_limit, 2) as gas_used_pct,\n    base_fee_per_gas / 1e9 as base_fee_gwei\nfrom {{ source('raw', 'blocks') }}\n"}<br>Click **Save**<br>(check: `models/staging/stg_blocks.sql` equals `../snippets/6.2/stg_blocks.sql`)<br>Zoom: code-mid | 33 | 16 |

## s03 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b03 @0:31 | And stg transactions dot sequel: the value and the fee paid in ether, and a success flag from the receipt status. | Close the editor tab for `models/staging/stg_blocks.sql`<br>Right-click `models/staging` → **New File** → `stg_transactions.sql` → **Save**<br>paste: {'text': "{{ config(materialized='view') }}\n\nselect\n    hash as transaction_hash,\n    block_number,\n    date as block_date,\n    from_address,\n    to_address,\n    value / 1e18 as value_eth,\n    receipt_gas_used * receipt_effective_gas_price / 1e18 as fee_eth,\n    receipt_status = 1 as succeeded\nfrom {{ source('raw', 'transactions') }}\n"}<br>Click **Save**<br>(check: `models/staging/stg_transactions.sql` equals `../snippets/6.2/stg_transactions.sql`)<br>Zoom: code-mid | 21 | 10 |

## s04 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b04 @0:42 | In the command box, run dbt run, select staging. Two views, created in the lake, in a second. | Close the editor tab for `models/staging/stg_transactions.sql`<br>In the command box under the terminal, type `dbt run --select staging` and press Enter<br>Zoom: terminal-close | 18 | 12 |
| b05 @0:53 | Look at some rows with dbt show: each transaction with its block, date, addresses, and value in ether. The terminal shows the columns that fit; the fee and the success flag are further right. | In the command box under the terminal, type `dbt show --select stg_transactions --limit 5` and press Enter<br>Zoom: terminal-close | 34 | 13 |

## s05 · slide — slide `views`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b06 @1:06 | A view in a DuckLake is only a row in the catalog, in ducklake view: its SQL text, and no data files at all. So staging views cost nothing to keep, and are always up to date. | A view in DuckLake is a row in ducklake_view: SQL text, no Parquet files. | 37 | 12 |

## s06 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b07 @1:18 | dbt is done, so now we can open the lake in Studio. In Data Lake, eth lake, refresh: the two staging views are listed, in schema main, with type view. | Left bar → **DataLake**<br>Click **eth_lake**<br>Click **Refresh**<br>Zoom: center-wide | 30 | 11 |

## s07 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b08 @1:28 | Commit the source and the staging models, and push. | Left bar → **DBT Studio**<br>Open the **Git** tab in the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Type the commit message “Staging models”<br>Click **Commit**<br>git_push: None<br>Zoom: git-panel | 9 | 18 |

## s08 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b09 @1:46 | To recap: sources point dbt at the raw tables, two staging views clean them up, and in a lake a view is just a row in the catalog. Next: marts, built incrementally, with a real merge. | Recap: sources for raw tables; stg_blocks and stg_transactions as views; dbt run, dbt show; views are catalog rows. | 36 | 13 |

## s09 · closing card (4 s, no voice)

Next · Lesson 6.3 · Marts, built incrementally.

**Total: 248 spoken words, 2:03 rendered.**
