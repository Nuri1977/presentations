select snapshot_id, schema_version, changes from eth_lake.snapshots() order by 1;
select * from eth_lake.current_snapshot();
insert into raw.blocks select * exclude (logs_bloom, last_modified) from read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-11-01/*.parquet');
select snapshot_id, changes from eth_lake.snapshots() order by 1 desc limit 2;
