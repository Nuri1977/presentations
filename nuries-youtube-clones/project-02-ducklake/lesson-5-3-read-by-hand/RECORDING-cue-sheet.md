# Read the lake by hand — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `lesson-5-2-end`: current snapshot 24.

## s02 · Step by step

| Listen for | Do this |
|---|---|
| "In the SQL Editor, on eth lake. Step…" | In the left bar, click **SQL Editor**<br>Open the connection list (top left) and pick **eth_lake**<br>paste: select max(snapshot_id) as current_snapshot from __ducklake_metadata_eth_lake.ducklake_snapshot;<br>select table_id, table_name, path from __ducklake_metadata_eth_lake.ducklake_table where table_name = 'transactions' and end_snapshot is null;<br>select value as data_path from __ducklake_metadata_eth_lake.ducklake_metadata where key = 'data_path';<br>select path from __ducklake_metadata_eth_lake.ducklake_data_file where table_id = 5 and begin_snapshot <= 24 and (end_snapshot > 24 or end_snapshot is null) order by 1;<br>select count(*) as transactions from read_parquet('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/raw/transactions/**/*.parquet', filename = true) where regexp_extract(filename, 'transactions/(.*)$', 1) in (select path from __ducklake_metadata_eth_lake.ducklake_data_file where table_id = 5 and begin_snapshot <= 24 and (end_snapshot > 24 or end_snapshot is null));<br>select count(*) as transactions from raw.transactions;<br>Click the green ▶ arrow next to line 1 |
| "Step two: the transactions table, valid now. Table…" | Click the green ▶ arrow next to line 1 |
| "Step three: the lake's data path, from ducklake…" | Click the green ▶ arrow next to line 1 |
| "Step four: the data files of table five…" | Click the green ▶ arrow next to line 1 |

## s03 · Read the files

| Listen for | Do this |
|---|---|
| "Step five: read exactly those files with read…" | Click the green ▶ arrow next to line 1<br>sql_wait: None |
| "And the same count, the normal way, from…" | Click the green ▶ arrow next to line 1 |

## s05 · Commit and push

| Listen for | Do this |
|---|---|
| "Save the queries as 5 underscore 3 read…" | In the left bar, click **DBT Studio**<br>Right-click `sql` → **New File**, type `5_3_read_by_hand.sql`, click **Save**<br>paste: select max(snapshot_id) as current_snapshot from __ducklake_metadata_eth_lake.ducklake_snapshot;<br>select table_id, table_name, path from __ducklake_metadata_eth_lake.ducklake_table where table_name = 'transactions' and end_snapshot is null;<br>select value as data_path from __ducklake_metadata_eth_lake.ducklake_metadata where key = 'data_path';<br>select path from __ducklake_metadata_eth_lake.ducklake_data_file where table_id = 5 and begin_snapshot <= 24 and (end_snapshot > 24 or end_snapshot is null) order by 1;<br>select count(*) as transactions from read_parquet('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/raw/transactions/**/*.parquet', filename = true) where regexp_extract(filename, 'transactions/(.*)$', 1) in (select path from __ducklake_metadata_eth_lake.ducklake_data_file where table_id = 5 and begin_snapshot <= 24 and (end_snapshot > 24 or end_snapshot is null));<br>select count(*) as transactions from raw.transactions;<br><br>Click **Save** (top right of the editor)<br>(Check that `sql/5_3_read_by_hand.sql` matches `../snippets/5.3/5_3_read_by_hand.sql`)<br>Close the editor tab for `sql/5_3_read_by_hand.sql` (its ×)<br>Click the **Git** tab at the top of the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Click the message box and type: Read the lake by hand<br>Click **Commit**<br>git_push: None |
