# Marts, built incrementally — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `lesson-6-2-end`: staging models in the project; Studio freshly opened, the lake not opened yet. The marts folder exists (empty).

## s01 · Two table marts

| Listen for | Do this |
|---|---|
| "In the marts folder, daily network activity: per…" | In the left bar, click **DBT Studio**<br>Right-click `models/marts` → **New File**, type `daily_network_activity.sql`, click **Save**<br>paste: {'text': "{{ config(materialized='table') }}\n\nselect\n    block_date,\n    count(*) as blocks,\n    sum(transaction_count) as transactions,\n    round(avg(gas_used_pct), 1) as avg_gas_used_pct,\n    round(avg(base_fee_gwei), 3) as avg_base_fee_gwei\nfrom {{ ref('stg_blocks') }}\ngroup by block_date\n"}<br>Click **Save** (top right of the editor)<br>(Check that `models/marts/daily_network_activity.sql` matches `../snippets/6.3/daily_network_activity.sql`) |
| "And top senders: the hundred addresses that sent…" | Close the editor tab for `models/marts/daily_network_activity.sql` (its ×)<br>Right-click `models/marts` → **New File**, type `top_senders.sql`, click **Save**<br>paste: {'text': "{{ config(materialized='table') }}\n\nselect\n    from_address,\n    count(*) as transactions,\n    round(sum(fee_eth), 4) as fees_paid_eth\nfrom {{ ref('stg_transactions') }}\ngroup by from_address\norder by transactions desc\nlimit 100\n"}<br>Click **Save** (top right of the editor)<br>(Check that `models/marts/top_senders.sql` matches `../snippets/6.3/top_senders.sql`) |

## s02 · An incremental merge

| Listen for | Do this |
|---|---|
| "Now daily gas, incremental, with the merge strategy…" | Close the editor tab for `models/marts/top_senders.sql` (its ×)<br>Right-click `models/marts` → **New File**, type `daily_gas.sql`, click **Save**<br>paste: {'text': '{{ config(\n    materialized=\'incremental\',\n    incremental_strategy=\'merge\',\n    unique_key=\'block_date\',\n    post_hook="call eth_lake.set_commit_message(\'dbt\', \'daily_gas: incremental merge\')"\n) }}\n\nselect\n    block_date,\n    count(*) as transactions,\n    round(sum(fee_eth), 4) as total_fee_eth,\n    round(median(fee_eth), 8) as median_fee_eth,\n    round(100.0 * avg(succeeded::int), 2) as success_pct\nfrom {{ ref(\'stg_transactions\') }}\n{% if is_incremental() %}\nwhere block_date >= (select max(block_date) from {{ this }})\n{% endif %}\ngroup by block_date\n'}<br>Click **Save** (top right of the editor)<br>(Check that `models/marts/daily_gas.sql` matches `../snippets/6.3/daily_gas.sql`) |

## s03 · Run, twice

| Listen for | Do this |
|---|---|
| "Run everything: dbt run. Two views, two tables,…" | Close the editor tab for `models/marts/daily_gas.sql` (its ×)<br>Click the command box under the terminal, type `dbt run`, press Enter |
| "Run daily gas again. This time it is…" | Click the command box under the terminal, type `dbt run --select daily_gas`, press Enter |
| "Here is what dbt ran, in the target…" | refresh_explorer: None<br>In the Explorer, open `target/run/ethereum_lake/models/marts/daily_gas.sql` (expand each folder on the way) |
| "And the result, with dbt show: one row…" | Close the editor tab for `target/run/ethereum_lake/models/marts/daily_gas.sql` (its ×)<br>Click the command box under the terminal, type `dbt show --select daily_network_activity --limit 5`, press Enter |

## s04 · dbt's snapshots

| Listen for | Do this |
|---|---|
| "dbt is done, so open the lake in…" | In the left bar, click **DataLake**<br>Click **eth_lake**<br>Click **History** |

## s05 · Commit and push

| Listen for | Do this |
|---|---|
| "Commit the marts, and push.…" | In the left bar, click **DBT Studio**<br>Click the **Git** tab at the top of the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Click the message box and type: Marts on the lake<br>Click **Commit**<br>git_push: None |
