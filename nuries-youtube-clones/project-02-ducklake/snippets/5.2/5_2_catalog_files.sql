select data_file_id, record_count, file_size_bytes, path from __ducklake_metadata_eth_lake.ducklake_data_file where table_id = 5 and end_snapshot is null order by 1;
select f.data_file_id, s.min_value, s.max_value from __ducklake_metadata_eth_lake.ducklake_file_column_stats s join __ducklake_metadata_eth_lake.ducklake_data_file f using (data_file_id) join __ducklake_metadata_eth_lake.ducklake_column c on c.column_id = s.column_id and c.table_id = f.table_id where f.table_id = 5 and c.column_name = 'block_number' and f.end_snapshot is null and c.end_snapshot is null order by 1;
select data_file_id, partition_value from __ducklake_metadata_eth_lake.ducklake_file_partition_value where table_id = 5 order by 1;
select table_id, record_count, file_size_bytes from __ducklake_metadata_eth_lake.ducklake_table_stats order by 1;
select table_id, table_name from __ducklake_metadata_eth_lake.ducklake_inlined_data_tables;
