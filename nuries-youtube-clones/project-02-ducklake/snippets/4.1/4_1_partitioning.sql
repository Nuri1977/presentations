create table raw.transactions (hash varchar, block_number bigint, block_timestamp timestamp, transaction_index bigint, from_address varchar, to_address varchar, value double, gas bigint, gas_price bigint, receipt_gas_used bigint, receipt_effective_gas_price bigint, receipt_status bigint, transaction_type bigint, max_fee_per_gas bigint, max_priority_fee_per_gas bigint, date date);
alter table raw.transactions set partitioned by (date);
insert into raw.transactions select hash, block_number, block_timestamp, transaction_index, from_address, to_address, value, gas, gas_price, receipt_gas_used, receipt_effective_gas_price, receipt_status, transaction_type, max_fee_per_gas, max_priority_fee_per_gas, date from read_parquet('s3://aws-public-blockchain/v1.0/eth/transactions/date=2026-10-0[1-7]/*.parquet');
select strftime(date, '%Y-%m-%d') as day, count(*) as transactions from raw.transactions group by all order by 1;
select regexp_extract(file, 'transactions/(.*)$', 1) as file from glob('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/raw/transactions/**/*.parquet');
select count(*) as transactions from raw.transactions where date = date '2026-10-03';
