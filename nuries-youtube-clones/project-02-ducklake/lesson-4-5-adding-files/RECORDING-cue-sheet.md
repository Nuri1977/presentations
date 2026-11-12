# Adding existing Parquet files — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `lesson-4-4-end`: raw.blocks has 1 and 2 November; the table has fee_recipient and gas_used_pct since 3.3.

## s02 · A file in a landing folder

| Listen for | Do this |
|---|---|
| "In the project, inside the lake folder, make…" | In the left bar, click **DBT Studio**<br>Right-click `lake` → **New Folder**, type `landing`, click **Save** |
| "In the SQL Editor, on eth lake: copy…" | In the left bar, click **SQL Editor**<br>Open the connection list (top left) and pick **eth_lake**<br>paste: copy (select * exclude (logs_bloom, last_modified, miner), miner as fee_recipient, round(100.0 * gas_used / gas_limit, 2) as gas_used_pct from read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-11-03/*.parquet')) to '/Users/Shared/academy/learner/projects/ethereum_lake/lake/landing/blocks_2026-11-03.parquet';<br>create temp table added_files as select * from ducklake_add_data_files('eth_lake', 'blocks', '/Users/Shared/academy/learner/projects/ethereum_lake/lake/landing/blocks_2026-11-03.parquet', schema => 'raw');<br>select strftime(date, '%Y-%m-%d') as day, count(*) as blocks from raw.blocks where date >= date '2026-11-01' group by all order by 1;<br>select data_file from ducklake_list_files('eth_lake', 'blocks', schema => 'raw');<br>Click the green ▶ arrow next to line 1<br>sql_wait: None |

## s03 · Register it

| Listen for | Do this |
|---|---|
| "Now ducklake add data files: the lake, the…" | Click the green ▶ arrow next to line 1<br>sql_wait: None |
| "Blocks per day: the third of November is…" | Click the green ▶ arrow next to line 1 |
| "And the table's file list now includes the…" | Click the green ▶ arrow next to line 1 |

## s05 · Commit and push

| Listen for | Do this |
|---|---|
| "Save the script as 4 underscore 5 add…" | In the left bar, click **DBT Studio**<br>In the Explorer, open `sql/4_5_add_files.sql` (expand each folder on the way)<br>paste: {'replace': True, 'text': "copy (select * exclude (logs_bloom, last_modified, miner), miner as fee_recipient, round(100.0 * gas_used / gas_limit, 2) as gas_used_pct from read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-11-03/*.parquet')) to '/Users/Shared/academy/learner/projects/ethereum_lake/lake/landing/blocks_2026-11-03.parquet';\ncreate temp table added_files as select * from ducklake_add_data_files('eth_lake', 'blocks', '/Users/Shared/academy/learner/projects/ethereum_lake/lake/landing/blocks_2026-11-03.parquet', schema => 'raw');\nselect strftime(date, '%Y-%m-%d') as day, count(*) as blocks from raw.blocks where date >= date '2026-11-01' group by all order by 1;\nselect data_file from ducklake_list_files('eth_lake', 'blocks', schema => 'raw');\n"}<br>Click **Save** (top right of the editor)<br>(Check that `sql/4_5_add_files.sql` matches `../snippets/4.5/4_5_add_files.sql`)<br>Close the editor tab for `sql/4_5_add_files.sql` (its ×)<br>Click the **Git** tab at the top of the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Click the message box and type: Register the landing file once<br>Click **Commit**<br>git_push: None |
