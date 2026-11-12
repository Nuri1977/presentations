copy (select * exclude (logs_bloom, last_modified, miner), miner as fee_recipient, round(100.0 * gas_used / gas_limit, 2) as gas_used_pct from read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-11-03/*.parquet')) to '/Users/Shared/academy/learner/projects/ethereum_lake/lake/landing/blocks_2026-11-03.parquet';
create temp table added_files as select * from ducklake_add_data_files('eth_lake', 'blocks', '/Users/Shared/academy/learner/projects/ethereum_lake/lake/landing/blocks_2026-11-03.parquet', schema => 'raw');
select strftime(date, '%Y-%m-%d') as day, count(*) as blocks from raw.blocks where date >= date '2026-11-01' group by all order by 1;
select data_file from ducklake_list_files('eth_lake', 'blocks', schema => 'raw');
