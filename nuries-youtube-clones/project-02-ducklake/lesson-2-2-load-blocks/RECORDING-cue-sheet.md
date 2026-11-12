# Load three months of blocks from S3 — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `lesson-2-1-end`: the project as 2.1 pushed it, the ethereum_lake_dev connection, and the empty lake eth_lake (snapshot 0) registered in Studio.

## s02 · Load the blocks

| Listen for | Do this |
|---|---|
| "Open the SQL Editor, and pick the eth…" | In the left bar, click **SQL Editor**<br>Open the connection list (top left) and pick **eth_lake**<br>paste: call eth_lake.set_option('data_inlining_row_limit', 0);<br>create schema raw;<br>create table raw.blocks as select * exclude (logs_bloom, last_modified) from read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-08-*/*.parquet');<br>insert into raw.blocks select * exclude (logs_bloom, last_modified) from read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-09-*/*.parquet');<br>insert into raw.blocks select * exclude (logs_bloom, last_modified) from read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-10-*/*.parquet');<br>select strftime(date, '%Y-%m') as month, count(*) as blocks from raw.blocks group by all order by 1; |
| "Run the first two lines: inlining off, and…" | Click the green ▶ arrow next to line 1<br>Click the green ▶ arrow next to line 1 |
| "Line three creates raw dot blocks from every…" | Click the green ▶ arrow next to line 1<br>sql_wait: None |
| "Then September, and October, with insert into.…" | Click the green ▶ arrow next to line 1<br>sql_wait: None<br>Click the green ▶ arrow next to line 1<br>sql_wait: None |
| "Check the result: blocks per month. About two…" | Click the green ▶ arrow next to line 1 |

## s03 · The table in Studio

| Listen for | Do this |
|---|---|
| "Now open Data Lake, and the eth lake…" | In the left bar, click **DataLake**<br>Click **eth_lake**<br>Click **Refresh**<br>Point at **blocks table** |
| "And History has four new snapshots: the schema,…" | Click **History** |

## s04 · Keep the script, commit, push

| Listen for | Do this |
|---|---|
| "Keep the script in the project. In DBT…" | In the left bar, click **DBT Studio**<br>new_root_folder: sql<br>Right-click `sql` → **New File**, type `2_2_load_blocks.sql`, click **Save**<br>paste: call eth_lake.set_option('data_inlining_row_limit', 0);<br>create schema raw;<br>create table raw.blocks as select * exclude (logs_bloom, last_modified) from read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-08-*/*.parquet');<br>insert into raw.blocks select * exclude (logs_bloom, last_modified) from read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-09-*/*.parquet');<br>insert into raw.blocks select * exclude (logs_bloom, last_modified) from read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-10-*/*.parquet');<br>select strftime(date, '%Y-%m') as month, count(*) as blocks from raw.blocks group by all order by 1;<br><br>Click **Save** (top right of the editor)<br>(Check that `sql/2_2_load_blocks.sql` matches `../snippets/2.2/2_2_load_blocks.sql`) |
| "Git tab: stage all, commit with load three…" | Close the editor tab for `sql/2_2_load_blocks.sql` (its ×)<br>Click the **Git** tab at the top of the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Click the message box and type: Load three months of blocks<br>Click **Commit**<br>git_push: None |
