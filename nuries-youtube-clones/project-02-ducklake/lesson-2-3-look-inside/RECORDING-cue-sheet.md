# Look inside: data files and tables — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `lesson-2-2-end`: project as pushed by 2.2; the lake rebuilt from snippets/2.2 (raw.blocks, three files, snapshots 0 to 4).

## s01 · The table in Studio

| Listen for | Do this |
|---|---|
| "Open Data Lake, then eth lake, and click…" | In the left bar, click **DataLake**<br>Click **eth_lake**<br>Click **blocks** |
| "The Schema tab lists the columns and their…" | Click **Schema** |
| "And Data Files: three Parquet files, one per…" | Click **Data Files** |

## s02 · The same in SQL

| Listen for | Do this |
|---|---|
| "The same list is one function in SQL.…" | In the left bar, click **SQL Editor**<br>Open the connection list (top left) and pick **eth_lake**<br>paste: select data_file, data_file_size_bytes from ducklake_list_files('eth_lake', 'blocks', schema => 'raw');<br>select file from glob('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/**/*.parquet');<br>select count(*) as blocks from read_parquet('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/raw/blocks/*.parquet');<br>Click the green ▶ arrow next to line 1 |
| "The files are on your disk. Glob lists…" | Click the green ▶ arrow next to line 1 |
| "And they are plain Parquet. Read them directly,…" | Click the green ▶ arrow next to line 1 |

## s04 · Commit and push

| Listen for | Do this |
|---|---|
| "Save the queries as sql, 2 underscore 3…" | In the left bar, click **DBT Studio**<br>Right-click `sql` → **New File**, type `2_3_look_inside.sql`, click **Save**<br>paste: select data_file, data_file_size_bytes from ducklake_list_files('eth_lake', 'blocks', schema => 'raw');<br>select file from glob('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/**/*.parquet');<br>select count(*) as blocks from read_parquet('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/raw/blocks/*.parquet');<br><br>Click **Save** (top right of the editor)<br>(Check that `sql/2_3_look_inside.sql` matches `../snippets/2.3/2_3_look_inside.sql`)<br>Close the editor tab for `sql/2_3_look_inside.sql` (its ×)<br>Click the **Git** tab at the top of the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Click the message box and type: Look inside the lake<br>Click **Commit**<br>git_push: None |
