# Inside the catalog: snapshots, tables, columns — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `lesson-4-5-end`: the lake after Module 4.

## s01 · The catalog is a database

| Listen for | Do this |
|---|---|
| "In the SQL Editor, on eth lake, list…" | In the left bar, click **SQL Editor**<br>Open the connection list (top left) and pick **eth_lake**<br>paste: select database_name, type from duckdb_databases();<br>select table_name from duckdb_tables() where database_name = '__ducklake_metadata_eth_lake' order by 1;<br>select snapshot_id, schema_version from __ducklake_metadata_eth_lake.ducklake_snapshot order by 1;<br>select snapshot_id, changes_made from __ducklake_metadata_eth_lake.ducklake_snapshot_changes order by 1 desc limit 5;<br>select table_id, table_name, begin_snapshot, end_snapshot from __ducklake_metadata_eth_lake.ducklake_table order by 1;<br>select column_id, column_name, begin_snapshot, end_snapshot from __ducklake_metadata_eth_lake.ducklake_column where table_id = 2 and column_id = 3 order by begin_snapshot;<br>Click the green ▶ arrow next to line 1 |
| "Its tables all start with ducklake. These are…" | Click the green ▶ arrow next to line 1 |

## s02 · Snapshots and changes

| Listen for | Do this |
|---|---|
| "Ducklake snapshot has one row per snapshot, with…" | Click the green ▶ arrow next to line 1 |
| "Ducklake snapshot changes says what each snapshot did:…" | Click the green ▶ arrow next to line 1 |

## s03 · Tables and columns

| Listen for | Do this |
|---|---|
| "Ducklake table: one row per table, with an…" | Click the green ▶ arrow next to line 1 |
| "And ducklake column, for column three of the…" | Click the green ▶ arrow next to line 1 |

## s05 · Commit and push

| Listen for | Do this |
|---|---|
| "Save the queries as 5 underscore 1 catalog…" | In the left bar, click **DBT Studio**<br>Right-click `sql` → **New File**, type `5_1_catalog_tables.sql`, click **Save**<br>paste: select database_name, type from duckdb_databases();<br>select table_name from duckdb_tables() where database_name = '__ducklake_metadata_eth_lake' order by 1;<br>select snapshot_id, schema_version from __ducklake_metadata_eth_lake.ducklake_snapshot order by 1;<br>select snapshot_id, changes_made from __ducklake_metadata_eth_lake.ducklake_snapshot_changes order by 1 desc limit 5;<br>select table_id, table_name, begin_snapshot, end_snapshot from __ducklake_metadata_eth_lake.ducklake_table order by 1;<br>select column_id, column_name, begin_snapshot, end_snapshot from __ducklake_metadata_eth_lake.ducklake_column where table_id = 2 and column_id = 3 order by begin_snapshot;<br><br>Click **Save** (top right of the editor)<br>(Check that `sql/5_1_catalog_tables.sql` matches `../snippets/5.1/5_1_catalog_tables.sql`)<br>Close the editor tab for `sql/5_1_catalog_tables.sql` (its ×)<br>Click the **Git** tab at the top of the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Click the message box and type: Catalog tables for snapshots, tables and columns<br>Click **Commit**<br>git_push: None |
