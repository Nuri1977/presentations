select count(*) as files from glob('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/**/*.parquet');
call ducklake_merge_adjacent_files('eth_lake');
select count(*) as files from glob('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/**/*.parquet');
select snapshot_id, changes from eth_lake.snapshots() where snapshot_id in (6, 7);
call ducklake_expire_snapshots('eth_lake', versions => [6, 7]);
call ducklake_cleanup_old_files('eth_lake', dry_run => true, cleanup_all => true);
call ducklake_cleanup_old_files('eth_lake', cleanup_all => true);
select count(*) as files from glob('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/**/*.parquet');
checkpoint;
