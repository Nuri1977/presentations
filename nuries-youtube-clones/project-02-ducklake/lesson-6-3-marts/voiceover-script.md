# Marts, built incrementally — voice-over script and beat sheet

Data Lakes with DuckLake in Rosetta DBT Studio · Module 6 · dbt on DuckLake · next: Lesson 6.4 · Tests and docs on the lake

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `lesson-6-2-end`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 2 · Lesson 6.3. Marts, built incrementally.

## s01 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | In the marts folder, daily network activity: per day, the number of blocks and transactions, how full the blocks were, and the average base fee. A table. | Left bar → **DBT Studio**<br>Right-click `models/marts` → **New File** → `daily_network_activity.sql` → **Save**<br>paste: {'text': "{{ config(materialized='table') }}\n\nselect\n    block_date,\n    count(*) as blocks,\n    sum(transaction_count) as transactions,\n    round(avg(gas_used_pct), 1) as avg_gas_used_pct,\n    round(avg(base_fee_gwei), 3) as avg_base_fee_gwei\nfrom {{ ref('stg_blocks') }}\ngroup by block_date\n"}<br>Click **Save**<br>(check: `models/marts/daily_network_activity.sql` equals `../snippets/6.3/daily_network_activity.sql`)<br>Zoom: code-mid | 27 | 13 |
| b02 @0:15 | And top senders: the hundred addresses that sent the most transactions, with the fees they paid. | Close the editor tab for `models/marts/daily_network_activity.sql`<br>Right-click `models/marts` → **New File** → `top_senders.sql` → **Save**<br>paste: {'text': "{{ config(materialized='table') }}\n\nselect\n    from_address,\n    count(*) as transactions,\n    round(sum(fee_eth), 4) as fees_paid_eth\nfrom {{ ref('stg_transactions') }}\ngroup by from_address\norder by transactions desc\nlimit 100\n"}<br>Click **Save**<br>(check: `models/marts/top_senders.sql` equals `../snippets/6.3/top_senders.sql`)<br>Zoom: code-mid | 16 | 10 |

## s02 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b03 @0:25 | Now daily gas, incremental, with the merge strategy and block date as the unique key. On later runs it only processes days from the last one it has, and merges them in. The post hook calls set commit message, so the snapshots daily gas makes get an author and a message. | Close the editor tab for `models/marts/top_senders.sql`<br>Right-click `models/marts` → **New File** → `daily_gas.sql` → **Save**<br>paste: {'text': '{{ config(\n    materialized=\'incremental\',\n    incremental_strategy=\'merge\',\n    unique_key=\'block_date\',\n    post_hook="call eth_lake.set_commit_message(\'dbt\', \'daily_gas: incremental merge\')"\n) }}\n\nselect\n    block_date,\n    count(*) as transactions,\n    round(sum(fee_eth), 4) as total_fee_eth,\n    round(median(fee_eth), 8) as median_fee_eth,\n    round(100.0 * avg(succeeded::int), 2) as success_pct\nfrom {{ ref(\'stg_transactions\') }}\n{% if is_incremental() %}\nwhere block_date >= (select max(block_date) from {{ this }})\n{% endif %}\ngroup by block_date\n'}<br>Click **Save**<br>(check: `models/marts/daily_gas.sql` equals `../snippets/6.3/daily_gas.sql`)<br>Zoom: code-mid | 51 | 17 |

## s03 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b04 @0:43 | Run everything: dbt run. Two views, two tables, and the incremental model, built in the lake. | Close the editor tab for `models/marts/daily_gas.sql`<br>In the command box under the terminal, type `dbt run` and press Enter<br>Zoom: terminal-close | 16 | 10 |
| b05 @0:53 | Run daily gas again. This time it is incremental: dbt recomputes the last day into a temporary table, and merges it into daily gas. | In the command box under the terminal, type `dbt run --select daily_gas` and press Enter<br>Zoom: terminal-close | 24 | 12 |
| b06 @1:05 | Here is what dbt ran, in the target folder: merge into eth lake dot main dot daily gas. The merge Studio's SQL Editor could not run in Lesson 3.2, running on our lake. | refresh_explorer: None<br>Open `target/run/ethereum_lake/models/marts/daily_gas.sql` in the Explorer<br>Zoom: code-mid<br>Card: *target/run/…/daily_gas.sql* — **MERGE INTO** — run by dbt on the lake | 34 | 13 |
| b07 @1:18 | And the result, with dbt show: one row per day, from August to early November. | Close the editor tab for `target/run/ethereum_lake/models/marts/daily_gas.sql`<br>In the command box under the terminal, type `dbt show --select daily_network_activity --limit 5` and press Enter<br>Zoom: terminal-close | 15 | 11 |

## s04 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b08 @1:29 | dbt is done, so open the lake in Studio: Data Lake, eth lake, History. dbt's work is a series of snapshots. And the incremental merge has an author, dbt, and our commit message. | Left bar → **DataLake**<br>Click **eth_lake**<br>Click **History**<br>Zoom: center-wide<br>Card: *eth_lake · History* — **Author: dbt** — daily_gas: incremental merge | 33 | 13 |

## s05 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b09 @1:42 | Commit the marts, and push. | Left bar → **DBT Studio**<br>Open the **Git** tab in the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Type the commit message “Marts on the lake”<br>Click **Commit**<br>git_push: None<br>Zoom: git-panel | 5 | 18 |

## s06 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b10 @2:00 | To recap: two table marts, and an incremental model whose merge strategy runs a real merge into on the lake. A post hook adds a commit message, and every dbt run shows up as snapshots. Next: tests and docs. | Recap: table marts; incremental merge = MERGE INTO on the lake; post_hook sets a commit message; dbt runs are snapshots. | 39 | 15 |

## s07 · closing card (4 s, no voice)

Next · Lesson 6.4 · Tests and docs.

**Total: 260 spoken words, 2:19 rendered.**
