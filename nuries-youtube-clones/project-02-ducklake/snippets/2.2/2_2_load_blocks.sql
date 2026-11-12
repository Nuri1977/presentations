call eth_lake.set_option('data_inlining_row_limit', 0);
create schema raw;
create table raw.blocks as select * exclude (logs_bloom, last_modified) from read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-08-*/*.parquet');
insert into raw.blocks select * exclude (logs_bloom, last_modified) from read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-09-*/*.parquet');
insert into raw.blocks select * exclude (logs_bloom, last_modified) from read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-10-*/*.parquet');
select strftime(date, '%Y-%m') as month, count(*) as blocks from raw.blocks group by all order by 1;
