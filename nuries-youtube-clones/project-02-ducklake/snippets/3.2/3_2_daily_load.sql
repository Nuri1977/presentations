insert into raw.blocks select s.* exclude (logs_bloom, last_modified) from read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-11-02/*.parquet') as s where not exists (select 1 from raw.blocks as t where t.number = s.number);
select date, count(*) as blocks from raw.blocks where date >= date '2026-11-01' group by all order by 1;
select snapshot_id, changes from eth_lake.snapshots() order by 1 desc limit 3;
