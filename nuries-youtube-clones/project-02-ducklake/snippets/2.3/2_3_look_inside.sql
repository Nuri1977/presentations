select data_file, data_file_size_bytes from ducklake_list_files('eth_lake', 'blocks', schema => 'raw');
select file from glob('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/**/*.parquet');
select count(*) as blocks from read_parquet('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/raw/blocks/*.parquet');
