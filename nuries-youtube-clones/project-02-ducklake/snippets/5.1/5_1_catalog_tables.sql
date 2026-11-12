select database_name, type from duckdb_databases();
select table_name from duckdb_tables() where database_name = '__ducklake_metadata_eth_lake' order by 1;
select snapshot_id, schema_version from __ducklake_metadata_eth_lake.ducklake_snapshot order by 1;
select snapshot_id, changes_made from __ducklake_metadata_eth_lake.ducklake_snapshot_changes order by 1 desc limit 5;
select table_id, table_name, begin_snapshot, end_snapshot from __ducklake_metadata_eth_lake.ducklake_table order by 1;
select column_id, column_name, begin_snapshot, end_snapshot from __ducklake_metadata_eth_lake.ducklake_column where table_id = 2 and column_id = 3 order by begin_snapshot;
