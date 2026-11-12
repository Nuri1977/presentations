# Staging models for blocks and transactions — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `lesson-6-1-end`: profiles.yml attaches the lake; Studio freshly opened, the lake not opened yet.

## s01 · Sources

| Listen for | Do this |
|---|---|
| "In DBT Studio, in the models folder, create…" | In the left bar, click **DBT Studio**<br>Right-click `models` → **New File**, type `sources.yml`, click **Save**<br>paste: {'text': 'sources:\n  - name: raw\n    database: eth_lake\n    schema: raw\n    tables:\n      - name: blocks\n      - name: transactions\n'}<br>Click **Save** (top right of the editor)<br>(Check that `models/sources.yml` matches `../snippets/6.2/sources.yml`) |

## s02 · stg_blocks

| Listen for | Do this |
|---|---|
| "Make a folder models, staging, and in it…" | Close the editor tab for `models/sources.yml` (its ×)<br>Right-click `models` → **New Folder**, type `staging`, click **Save**<br>Right-click `models/staging` → **New File**, type `stg_blocks.sql`, click **Save**<br>paste: {'text': "{{ config(materialized='view') }}\n\nselect\n    number as block_number,\n    date as block_date,\n    timestamp as block_time,\n    fee_recipient,\n    transaction_count,\n    gas_used,\n    gas_limit,\n    round(100.0 * gas_used / gas_limit, 2) as gas_used_pct,\n    base_fee_per_gas / 1e9 as base_fee_gwei\nfrom {{ source('raw', 'blocks') }}\n"}<br>Click **Save** (top right of the editor)<br>(Check that `models/staging/stg_blocks.sql` matches `../snippets/6.2/stg_blocks.sql`) |

## s03 · stg_transactions

| Listen for | Do this |
|---|---|
| "And stg transactions dot sequel: the value and…" | Close the editor tab for `models/staging/stg_blocks.sql` (its ×)<br>Right-click `models/staging` → **New File**, type `stg_transactions.sql`, click **Save**<br>paste: {'text': "{{ config(materialized='view') }}\n\nselect\n    hash as transaction_hash,\n    block_number,\n    date as block_date,\n    from_address,\n    to_address,\n    value / 1e18 as value_eth,\n    receipt_gas_used * receipt_effective_gas_price / 1e18 as fee_eth,\n    receipt_status = 1 as succeeded\nfrom {{ source('raw', 'transactions') }}\n"}<br>Click **Save** (top right of the editor)<br>(Check that `models/staging/stg_transactions.sql` matches `../snippets/6.2/stg_transactions.sql`) |

## s04 · Run and look

| Listen for | Do this |
|---|---|
| "In the command box, run dbt run, select…" | Close the editor tab for `models/staging/stg_transactions.sql` (its ×)<br>Click the command box under the terminal, type `dbt run --select staging`, press Enter |
| "Look at some rows with dbt show: each…" | Click the command box under the terminal, type `dbt show --select stg_transactions --limit 5`, press Enter |

## s06 · The views in Studio

| Listen for | Do this |
|---|---|
| "dbt is done, so now we can open…" | In the left bar, click **DataLake**<br>Click **eth_lake**<br>Click **Refresh** |

## s07 · Commit and push

| Listen for | Do this |
|---|---|
| "Commit the source and the staging models, and…" | In the left bar, click **DBT Studio**<br>Click the **Git** tab at the top of the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Click the message box and type: Staging models<br>Click **Commit**<br>git_push: None |
