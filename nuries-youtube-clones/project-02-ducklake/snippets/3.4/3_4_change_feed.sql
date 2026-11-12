select snapshot_id, change_type, count(*) as row_count from ducklake_table_changes('eth_lake', 'raw', 'blocks_day', 9, 10) group by all order by 1, 2;
select snapshot_id, change_type, number, extra_data from ducklake_table_changes('eth_lake', 'raw', 'blocks_day', 10, 10) order by number, change_type limit 4;
select count(*) as inserted from ducklake_table_insertions('eth_lake', 'raw', 'blocks_day', 8, 8);
select count(*) as deleted from ducklake_table_deletions('eth_lake', 'raw', 'blocks_day', 9, 9);
