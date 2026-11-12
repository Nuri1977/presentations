create table raw.blocks_day as select * from raw.blocks where date = date '2026-10-01';
select count(*) as blocks, count(*) filter (where transaction_count < 50) as small_blocks from raw.blocks_day;
delete from raw.blocks_day where transaction_count < 50;
update raw.blocks_day set extra_data = upper(extra_data) where number % 100 = 0;
select regexp_extract(data_file, '[^/]+$') as data_file, regexp_extract(delete_file, '[^/]+$') as delete_file from ducklake_list_files('eth_lake', 'blocks_day', schema => 'raw');
select distinct regexp_extract(file_path, '[^/]+$') as data_file, pos from read_parquet('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/raw/blocks_day/*-delete.parquet') order by pos limit 5;
