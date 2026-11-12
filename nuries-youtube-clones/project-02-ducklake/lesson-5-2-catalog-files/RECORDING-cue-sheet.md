# Inside the catalog: files and statistics — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `lesson-5-1-end`.

## s01 · Data files

| Listen for | Do this |
|---|---|
| "In the SQL Editor, on eth lake. Ducklake…" | In the left bar, click **SQL Editor**<br>Open the connection list (top left) and pick **eth_lake**<br>paste: select data_file_id, record_count, file_size_bytes, path from __ducklake_metadata_eth_lake.ducklake_data_file where table_id = 5 and end_snapshot is null order by 1;<br>select f.data_file_id, s.min_value, s.max_value from __ducklake_metadata_eth_lake.ducklake_file_column_stats s join __ducklake_metadata_eth_lake.ducklake_data_file f using (data_file_id) join __ducklake_metadata_eth_lake.ducklake_column c on c.column_id = s.column_id and c.table_id = f.table_id where f.table_id = 5 and c.column_name = 'block_number' and f.end_snapshot is null and c.end_snapshot is null order by 1;<br>select data_file_id, partition_value from __ducklake_metadata_eth_lake.ducklake_file_partition_value where table_id = 5 order by 1;<br>select table_id, record_count, file_size_bytes from __ducklake_metadata_eth_lake.ducklake_table_stats order by 1;<br>select table_id, table_name from __ducklake_metadata_eth_lake.ducklake_inlined_data_tables;<br>Click the green ▶ arrow next to line 1 |

## s02 · Statistics per file

| Listen for | Do this |
|---|---|
| "Ducklake file column stats holds the min and…" | Click the green ▶ arrow next to line 1 |

## s03 · Partitions, table stats, inlined rows

| Listen for | Do this |
|---|---|
| "Ducklake file partition value: the date each file…" | Click the green ▶ arrow next to line 1 |
| "Ducklake table stats keeps totals per table, so…" | Click the green ▶ arrow next to line 1 |
| "And ducklake inlined data tables: the watchlist from…" | Click the green ▶ arrow next to line 1 |

## s05 · Commit and push

| Listen for | Do this |
|---|---|
| "Save the queries as 5 underscore 2 catalog…" | In the left bar, click **DBT Studio**<br>Right-click `sql` → **New File**, type `5_2_catalog_files.sql`, click **Save**<br>paste: select data_file_id, record_count, file_size_bytes, path from __ducklake_metadata_eth_lake.ducklake_data_file where table_id = 5 and end_snapshot is null order by 1;<br>select f.data_file_id, s.min_value, s.max_value from __ducklake_metadata_eth_lake.ducklake_file_column_stats s join __ducklake_metadata_eth_lake.ducklake_data_file f using (data_file_id) join __ducklake_metadata_eth_lake.ducklake_column c on c.column_id = s.column_id and c.table_id = f.table_id where f.table_id = 5 and c.column_name = 'block_number' and f.end_snapshot is null and c.end_snapshot is null order by 1;<br>select data_file_id, partition_value from __ducklake_metadata_eth_lake.ducklake_file_partition_value where table_id = 5 order by 1;<br>select table_id, record_count, file_size_bytes from __ducklake_metadata_eth_lake.ducklake_table_stats order by 1;<br>select table_id, table_name from __ducklake_metadata_eth_lake.ducklake_inlined_data_tables;<br><br>Click **Save** (top right of the editor)<br>(Check that `sql/5_2_catalog_files.sql` matches `../snippets/5.2/5_2_catalog_files.sql`)<br>Close the editor tab for `sql/5_2_catalog_files.sql` (its ×)<br>Click the **Git** tab at the top of the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Click the message box and type: Catalog tables for files, statistics and partitions<br>Click **Commit**<br>git_push: None |
