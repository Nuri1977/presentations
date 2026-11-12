# Inside the catalog: snapshots, tables, columns — voice-over script and beat sheet

Data Lakes with DuckLake in Rosetta DBT Studio · Module 5 · Inside the catalog · next: Lesson 5.2 · Inside the catalog: files, statistics, partitions

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `lesson-4-5-end`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 2 · Lesson 5.1. Inside the catalog: snapshots, tables, columns.

## s01 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | In the SQL Editor, on eth lake, list the databases this connection has attached. Two matter: eth lake, the lake, and underscore underscore ducklake metadata eth lake: the catalog file, as a plain DuckDB database. | Left bar → **SQL Editor**<br>Pick the connection **eth_lake**<br>paste: select database_name, type from duckdb_databases();
select table_name from duckdb_tables() where database_name = '__ducklake_metadata_eth_lake' order by 1;
select snapshot_id, schema_version from __ducklake_metadata_eth_lake.ducklake_snapshot order by 1;
select snapshot_id, changes_made from __ducklake_metadata_eth_lake.ducklake_snapshot_changes order by 1 desc limit 5;
select table_id, table_name, begin_snapshot, end_snapshot from __ducklake_metadata_eth_lake.ducklake_table order by 1;
select column_id, column_name, begin_snapshot, end_snapshot from __ducklake_metadata_eth_lake.ducklake_column where table_id = 2 and column_id = 3 order by begin_snapshot;<br>Click the green run arrow next to line 1<br>Zoom: sql-results | 35 | 15 |
| b02 @0:17 | Its tables all start with ducklake. These are the tables the DuckLake specification defines. Nothing else: the whole lake's metadata is in them. | Click the green run arrow next to line 1<br>Zoom: sql-results | 23 | 9 |

## s02 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b03 @0:27 | Ducklake snapshot has one row per snapshot, with its schema version. Six and seven are missing: we expired them in Lesson 4.4. | Click the green run arrow next to line 1<br>Zoom: sql-results | 23 | 9 |
| b04 @0:36 | Ducklake snapshot changes says what each snapshot did: the November file we added, the merge, the inlining flush. This is what Studio's History tab shows. A commit message would be stored here too. | Click the green run arrow next to line 1<br>Zoom: sql-results | 33 | 13 |

## s03 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b05 @0:49 | Ducklake table: one row per table, with an id, and the snapshot it was created in. Begin snapshot, end snapshot: a table that was dropped gets an end snapshot. | Click the green run arrow next to line 1<br>Zoom: sql-results | 29 | 11 |
| b06 @1:00 | And ducklake column, for column three of the blocks table. Two rows: miner, valid from snapshot two until fourteen, and fee recipient from fourteen on. That is the rename from Lesson 3.3. Same id, new name, and the old name is kept for time travel. | Click the green run arrow next to line 1<br>Zoom: sql-results<br>Card: *ducklake_column · column 3* — **miner 2 → 14 · fee_recipient 14 →** — a rename is a new row, same id | 46 | 17 |

## s04 · slide — slide `pattern`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b07 @1:17 | That is the whole trick of the catalog. Every row has a begin snapshot and an end snapshot. The lake at snapshot s is simply every row where begin is at most s, and end is after s, or empty. | Every catalog row has begin_snapshot and end_snapshot; 'valid at snapshot s' = begin <= s and (end > s or end is null). | 40 | 13 |

## s05 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b08 @1:30 | Save the queries as 5 underscore 1 catalog tables dot sequel, commit, and push. | Left bar → **DBT Studio**<br>Right-click `sql` → **New File** → `5_1_catalog_tables.sql` → **Save**<br>paste: select database_name, type from duckdb_databases();
select table_name from duckdb_tables() where database_name = '__ducklake_metadata_eth_lake' order by 1;
select snapshot_id, schema_version from __ducklake_metadata_eth_lake.ducklake_snapshot order by 1;
select snapshot_id, changes_made from __ducklake_metadata_eth_lake.ducklake_snapshot_changes order by 1 desc limit 5;
select table_id, table_name, begin_snapshot, end_snapshot from __ducklake_metadata_eth_lake.ducklake_table order by 1;
select column_id, column_name, begin_snapshot, end_snapshot from __ducklake_metadata_eth_lake.ducklake_column where table_id = 2 and column_id = 3 order by begin_snapshot;
<br>Click **Save**<br>(check: `sql/5_1_catalog_tables.sql` equals `../snippets/5.1/5_1_catalog_tables.sql`)<br>Close the editor tab for `sql/5_1_catalog_tables.sql`<br>Open the **Git** tab in the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Type the commit message “Catalog tables for snapshots, tables and columns”<br>Click **Commit**<br>git_push: None<br>Zoom: git-panel | 14 | 28 |

## s06 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b09 @1:58 | To recap: the catalog is a plain database of ducklake tables. Snapshots, tables and columns are rows, and begin and end snapshot version all of them. Next: the files, their statistics, and partitions. | Recap: the catalog is a DuckDB database; ducklake_snapshot, _snapshot_changes, _table, _column; begin and end snapshot on every row. | 33 | 14 |

## s07 · closing card (4 s, no voice)

Next · Lesson 5.2 · Files, statistics, partitions.

**Total: 276 spoken words, 2:16 rendered.**
