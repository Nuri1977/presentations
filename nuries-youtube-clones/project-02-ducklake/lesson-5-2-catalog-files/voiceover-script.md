# Inside the catalog: files and statistics — voice-over script and beat sheet

Data Lakes with DuckLake in Rosetta DBT Studio · Module 5 · Inside the catalog · next: Lesson 5.3 · Read the lake by hand

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `lesson-5-1-end`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 2 · Lesson 5.2. Inside the catalog: files, statistics, partitions.

## s01 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | In the SQL Editor, on eth lake. Ducklake data file has one row per Parquet file. Here are the files of transactions, table five: one per day, with its row count, its size, and its path, relative to the data folder. | Left bar → **SQL Editor**<br>Pick the connection **eth_lake**<br>paste: select data_file_id, record_count, file_size_bytes, path from __ducklake_metadata_eth_lake.ducklake_data_file where table_id = 5 and end_snapshot is null order by 1;
select f.data_file_id, s.min_value, s.max_value from __ducklake_metadata_eth_lake.ducklake_file_column_stats s join __ducklake_metadata_eth_lake.ducklake_data_file f using (data_file_id) join __ducklake_metadata_eth_lake.ducklake_column c on c.column_id = s.column_id and c.table_id = f.table_id where f.table_id = 5 and c.column_name = 'block_number' and f.end_snapshot is null and c.end_snapshot is null order by 1;
select data_file_id, partition_value from __ducklake_metadata_eth_lake.ducklake_file_partition_value where table_id = 5 order by 1;
select table_id, record_count, file_size_bytes from __ducklake_metadata_eth_lake.ducklake_table_stats order by 1;
select table_id, table_name from __ducklake_metadata_eth_lake.ducklake_inlined_data_tables;<br>Click the green run arrow next to line 1<br>Zoom: sql-results | 41 | 15 |

## s02 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b02 @0:17 | Ducklake file column stats holds the min and max of every column of every file. For block number, each file covers its own narrow range, one day after the other. This is exactly what let the query in Lesson 4.2 skip six files out of seven. | Click the green run arrow next to line 1<br>Zoom: sql-results<br>Card: *ducklake_file_column_stats* — **min and max per file** — the data behind file pruning (4.2) | 47 | 16 |

## s03 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b03 @0:34 | Ducklake file partition value: the date each file belongs to, from the partitioning in Lesson 4.1. | Click the green run arrow next to line 1<br>Zoom: sql-results | 17 | 8 |
| b04 @0:41 | Ducklake table stats keeps totals per table, so counting rows needs no file at all. Transactions: twelve point seven million rows, one point seven gigabytes. | Click the green run arrow next to line 1<br>Zoom: sql-results | 25 | 11 |
| b05 @0:53 | And ducklake inlined data tables: the watchlist from Lesson 4.3 has a table inside the catalog, where inlined rows wait to be flushed. | Click the green run arrow next to line 1<br>Zoom: sql-results | 24 | 10 |

## s04 · slide — slide `tables`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b06 @1:03 | So these are the file tables: data files and delete files, statistics per file, partition values, table totals, inlined rows, and files scheduled for deletion by maintenance. | Table: ducklake_data_file, ducklake_delete_file, ducklake_file_column_stats, ducklake_file_partition_value, ducklake_table_stats, ducklake_inlined_data_tables, ducklake_files_scheduled_for_deletion. | 27 | 13 |

## s05 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b07 @1:15 | Save the queries as 5 underscore 2 catalog files dot sequel, commit, and push. | Left bar → **DBT Studio**<br>Right-click `sql` → **New File** → `5_2_catalog_files.sql` → **Save**<br>paste: select data_file_id, record_count, file_size_bytes, path from __ducklake_metadata_eth_lake.ducklake_data_file where table_id = 5 and end_snapshot is null order by 1;
select f.data_file_id, s.min_value, s.max_value from __ducklake_metadata_eth_lake.ducklake_file_column_stats s join __ducklake_metadata_eth_lake.ducklake_data_file f using (data_file_id) join __ducklake_metadata_eth_lake.ducklake_column c on c.column_id = s.column_id and c.table_id = f.table_id where f.table_id = 5 and c.column_name = 'block_number' and f.end_snapshot is null and c.end_snapshot is null order by 1;
select data_file_id, partition_value from __ducklake_metadata_eth_lake.ducklake_file_partition_value where table_id = 5 order by 1;
select table_id, record_count, file_size_bytes from __ducklake_metadata_eth_lake.ducklake_table_stats order by 1;
select table_id, table_name from __ducklake_metadata_eth_lake.ducklake_inlined_data_tables;
<br>Click **Save**<br>(check: `sql/5_2_catalog_files.sql` equals `../snippets/5.2/5_2_catalog_files.sql`)<br>Close the editor tab for `sql/5_2_catalog_files.sql`<br>Open the **Git** tab in the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Type the commit message “Catalog tables for files, statistics and partitions”<br>Click **Commit**<br>git_push: None<br>Zoom: git-panel | 14 | 28 |

## s06 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b08 @1:43 | To recap: every file is a row, with its statistics and partition value, and tables keep totals. Next, the final proof: we read the lake by hand, with nothing but these tables and read parquet. | Recap: every file is a row; min and max per column per file; partition values; table totals; inlined rows. | 35 | 13 |

## s07 · closing card (4 s, no voice)

Next · Lesson 5.3 · Read the lake by hand.

**Total: 230 spoken words, 2:00 rendered.**
