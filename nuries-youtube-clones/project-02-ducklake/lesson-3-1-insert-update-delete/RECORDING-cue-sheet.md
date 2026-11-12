# Insert, update, delete, and delete files — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `lesson-2-5-end`: raw.blocks with three months plus 1 November; snapshots 0 to 7.

## s02 · A small working copy

| Listen for | Do this |
|---|---|
| "In the SQL Editor, on eth lake, make…" | In the left bar, click **SQL Editor**<br>Open the connection list (top left) and pick **eth_lake**<br>paste: create table raw.blocks_day as select * from raw.blocks where date = date '2026-10-01';<br>select count(*) as blocks, count(*) filter (where transaction_count < 50) as small_blocks from raw.blocks_day;<br>delete from raw.blocks_day where transaction_count < 50;<br>update raw.blocks_day set extra_data = upper(extra_data) where number % 100 = 0;<br>select regexp_extract(data_file, '[^/]+$') as data_file, regexp_extract(delete_file, '[^/]+$') as delete_file from ducklake_list_files('eth_lake', 'blocks_day', schema => 'raw');<br>select distinct regexp_extract(file_path, '[^/]+$') as data_file, pos from read_parquet('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/raw/blocks_day/*-delete.parquet') order by pos limit 5;<br>Click the green ▶ arrow next to line 1<br>sql_wait: None |
| "Seven of those blocks hold fewer than fifty…" | Click the green ▶ arrow next to line 1 |

## s03 · Delete and update

| Listen for | Do this |
|---|---|
| "Delete those seven. Then update every hundredth block…" | Click the green ▶ arrow next to line 1<br>Click the green ▶ arrow next to line 1 |
| "Now list the table's files. The original data…" | Click the green ▶ arrow next to line 1 |
| "The delete file is Parquet too. It lists…" | Click the green ▶ arrow next to line 1 |

## s04 · The same in Studio

| Listen for | Do this |
|---|---|
| "In Data Lake, open eth lake, refresh, and…" | In the left bar, click **DataLake**<br>Click **eth_lake**<br>Click **Refresh**<br>Click **blocks_day**<br>Click **Data Files** |

## s06 · Commit and push

| Listen for | Do this |
|---|---|
| "Save the script as 3 underscore 1 update…" | In the left bar, click **DBT Studio**<br>Right-click `sql` → **New File**, type `3_1_update_delete.sql`, click **Save**<br>paste: create table raw.blocks_day as select * from raw.blocks where date = date '2026-10-01';<br>select count(*) as blocks, count(*) filter (where transaction_count < 50) as small_blocks from raw.blocks_day;<br>delete from raw.blocks_day where transaction_count < 50;<br>update raw.blocks_day set extra_data = upper(extra_data) where number % 100 = 0;<br>select regexp_extract(data_file, '[^/]+$') as data_file, regexp_extract(delete_file, '[^/]+$') as delete_file from ducklake_list_files('eth_lake', 'blocks_day', schema => 'raw');<br>select distinct regexp_extract(file_path, '[^/]+$') as data_file, pos from read_parquet('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/raw/blocks_day/*-delete.parquet') order by pos limit 5;<br><br>Click **Save** (top right of the editor)<br>(Check that `sql/3_1_update_delete.sql` matches `../snippets/3.1/3_1_update_delete.sql`)<br>Close the editor tab for `sql/3_1_update_delete.sql` (its ×)<br>Click the **Git** tab at the top of the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Click the message box and type: Update and delete in the lake<br>Click **Commit**<br>git_push: None |
