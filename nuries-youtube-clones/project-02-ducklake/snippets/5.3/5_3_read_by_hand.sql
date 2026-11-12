select max(snapshot_id) as current_snapshot from __ducklake_metadata_eth_lake.ducklake_snapshot;
select table_id, table_name, path from __ducklake_metadata_eth_lake.ducklake_table where table_name = 'transactions' and end_snapshot is null;
select value as data_path from __ducklake_metadata_eth_lake.ducklake_metadata where key = 'data_path';
select path from __ducklake_metadata_eth_lake.ducklake_data_file where table_id = 5 and begin_snapshot <= 24 and (end_snapshot > 24 or end_snapshot is null) order by 1;
select count(*) as transactions from read_parquet('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/raw/transactions/**/*.parquet', filename = true) where regexp_extract(filename, 'transactions/(.*)$', 1) in (select path from __ducklake_metadata_eth_lake.ducklake_data_file where table_id = 5 and begin_snapshot <= 24 and (end_snapshot > 24 or end_snapshot is null));
select count(*) as transactions from raw.transactions;
