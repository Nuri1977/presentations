# Read the lake by hand — voice-over script and beat sheet

Data Lakes with DuckLake in Rosetta DBT Studio · Module 5 · Inside the catalog · next: Lesson 6.1 · Connect a dbt project to the lake

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `lesson-5-2-end`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 2 · Lesson 5.3. Read the lake by hand.

## s01 · slide — slide `recipe`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | To end the catalog module, let's read the lake without the lake. The DuckLake specification describes the steps: find the current snapshot, find the table, find the data path, list the files valid at that snapshot, and read them. | Steps: current snapshot → table → data path → files valid at that snapshot → read them. | 39 | 14 |

## s02 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b02 @0:17 | In the SQL Editor, on eth lake. Step one: the current snapshot is the largest snapshot id. Twenty-four. | Left bar → **SQL Editor**<br>Pick the connection **eth_lake**<br>paste: select max(snapshot_id) as current_snapshot from __ducklake_metadata_eth_lake.ducklake_snapshot;
select table_id, table_name, path from __ducklake_metadata_eth_lake.ducklake_table where table_name = 'transactions' and end_snapshot is null;
select value as data_path from __ducklake_metadata_eth_lake.ducklake_metadata where key = 'data_path';
select path from __ducklake_metadata_eth_lake.ducklake_data_file where table_id = 5 and begin_snapshot <= 24 and (end_snapshot > 24 or end_snapshot is null) order by 1;
select count(*) as transactions from read_parquet('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/raw/transactions/**/*.parquet', filename = true) where regexp_extract(filename, 'transactions/(.*)$', 1) in (select path from __ducklake_metadata_eth_lake.ducklake_data_file where table_id = 5 and begin_snapshot <= 24 and (end_snapshot > 24 or end_snapshot is null));
select count(*) as transactions from raw.transactions;<br>Click the green run arrow next to line 1<br>Zoom: sql-results | 19 | 12 |
| b03 @0:29 | Step two: the transactions table, valid now. Table id five, and its folder, transactions. | Click the green run arrow next to line 1<br>Zoom: sql-results | 14 | 7 |
| b04 @0:36 | Step three: the lake's data path, from ducklake metadata: our data folder. Each file's path is relative to it, under the schema and the table's folder. | Click the green run arrow next to line 1<br>Zoom: sql-results | 26 | 10 |
| b05 @0:46 | Step four: the data files of table five that are valid at snapshot twenty-four: begin snapshot at most twenty-four, end snapshot after it, or empty. Seven files. | Click the green run arrow next to line 1<br>Zoom: sql-results | 29 | 12 |

## s03 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b06 @0:58 | Step five: read exactly those files with read parquet, and count. Twelve million six hundred ninety-five thousand eight hundred three. | Click the green run arrow next to line 1<br>sql_wait: None<br>Zoom: sql-results | 21 | 9 |
| b07 @1:06 | And the same count, the normal way, from raw transactions. Identical. The lake is nothing but these tables and these files. | Click the green run arrow next to line 1<br>Zoom: sql-results<br>Card: *by hand = through the lake* — **12,695,803** — raw.transactions | 21 | 8 |

## s04 · slide — slide `why`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b08 @1:15 | With deletes, one more step: read the delete files too, and skip the positions they list. | With delete files: also read ducklake_delete_file and skip those positions. | 16 | 6 |
| b09 @1:21 | And that is all any engine needs to read DuckLake: some SQL against the catalog, and a Parquet reader. Nothing is hidden. | This is all a new engine has to implement: SQL against the catalog, plus a Parquet reader. | 22 | 8 |

## s05 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b10 @1:29 | Save the queries as 5 underscore 3 read by hand dot sequel, commit, and push. | Left bar → **DBT Studio**<br>Right-click `sql` → **New File** → `5_3_read_by_hand.sql` → **Save**<br>paste: select max(snapshot_id) as current_snapshot from __ducklake_metadata_eth_lake.ducklake_snapshot;
select table_id, table_name, path from __ducklake_metadata_eth_lake.ducklake_table where table_name = 'transactions' and end_snapshot is null;
select value as data_path from __ducklake_metadata_eth_lake.ducklake_metadata where key = 'data_path';
select path from __ducklake_metadata_eth_lake.ducklake_data_file where table_id = 5 and begin_snapshot <= 24 and (end_snapshot > 24 or end_snapshot is null) order by 1;
select count(*) as transactions from read_parquet('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/raw/transactions/**/*.parquet', filename = true) where regexp_extract(filename, 'transactions/(.*)$', 1) in (select path from __ducklake_metadata_eth_lake.ducklake_data_file where table_id = 5 and begin_snapshot <= 24 and (end_snapshot > 24 or end_snapshot is null));
select count(*) as transactions from raw.transactions;
<br>Click **Save**<br>(check: `sql/5_3_read_by_hand.sql` equals `../snippets/5.3/5_3_read_by_hand.sql`)<br>Close the editor tab for `sql/5_3_read_by_hand.sql`<br>Open the **Git** tab in the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Type the commit message “Read the lake by hand”<br>Click **Commit**<br>git_push: None<br>Zoom: git-panel | 15 | 28 |

## s06 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b11 @1:57 | To recap: snapshot, table, data path, valid files, read parquet. Same answer as the lake. That ends Module 5. Next, we put dbt on top of the lake. | Recap: snapshot → table → data path → valid files → read_parquet; same result as the lake. | 28 | 11 |

## s07 · closing card (4 s, no voice)

Next · Lesson 6.1 · Connect a dbt project to the lake.

**Total: 250 spoken words, 2:12 rendered.**
