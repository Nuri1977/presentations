"""Phase 2 rehearsal: run every lesson's SQL (Modules 2 to 5) in order on a scratch lake and print the results.
Reads from the local cache instead of S3 (same files). Run with the pinned runtime:
  _academy-video-tooling/.cache/dbt-env/bin/python tools/rehearse.py <scratch_dir> [first_lesson]
"""
import sys, pathlib, shutil, time
import duckdb
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from s3cache import to_cache

ROOT = pathlib.Path(sys.argv[1]).resolve()
shutil.rmtree(ROOT, ignore_errors=True)
(ROOT / 'lake' / 'data').mkdir(parents=True)
LAKE = ROOT / 'lake'
B = 's3://aws-public-blockchain/v1.0/eth/blocks'

con = duckdb.connect()
con.execute(f"attach 'ducklake:{LAKE}/eth_catalog.duckdb' as eth_lake (data_path '{LAKE}/data/')")
con.execute("use eth_lake")


def run(sql, show=8):
    s = to_cache(sql.replace('{LAKE}', str(LAKE)))
    t0 = time.time()
    try:
        cur = con.execute(s)
        rows = cur.fetchall() if cur.description else []
        cols = [d[0] for d in cur.description] if cur.description else []
        print(f'  > {sql.strip()[:150]}   [{time.time()-t0:.1f}s]')
        if cols:
            print('    ', cols)
            for r in rows[:show]:
                print('    ', tuple(str(x)[:70] for x in r))
            if len(rows) > show: print(f'     … {len(rows)} rows')
    except Exception as e:
        print(f'  ! {sql.strip()[:150]}\n    ERROR {str(e)[:400]}')


def lesson(n, *stmts):
    print(f'\n=== {n}')
    for s in stmts: run(s)


lesson('2.1', "select snapshot_id, changes from eth_lake.snapshots()")
lesson('2.2',
       "call eth_lake.set_option('data_inlining_row_limit', 0)",
       "create schema raw",
       f"create table raw.blocks as select * exclude (logs_bloom, last_modified) from read_parquet('{B}/date=2026-08-*/*.parquet')",
       f"insert into raw.blocks select * exclude (logs_bloom, last_modified) from read_parquet('{B}/date=2026-09-*/*.parquet')",
       f"insert into raw.blocks select * exclude (logs_bloom, last_modified) from read_parquet('{B}/date=2026-10-*/*.parquet')",
       "select strftime(date, '%Y-%m') as month, count(*) as blocks, min(number) as first_block, max(number) as last_block from raw.blocks group by all order by 1",
       "select count(*) as blocks, count(distinct date) as days from raw.blocks",
       "describe raw.blocks")
lesson('2.3',
       "select * from ducklake_list_files('eth_lake', 'blocks', schema => 'raw')",
       "select count(*) as files from glob('{LAKE}/data/**/*.parquet')",
       "select file from glob('{LAKE}/data/**/*.parquet')",
       "select number, date, transaction_count from read_parquet('{LAKE}/data/raw/blocks/*.parquet') order by number limit 3",
       "select count(*) from read_parquet('{LAKE}/data/raw/blocks/*.parquet')")
lesson('2.4',
       "select snapshot_id, strftime(snapshot_time, '%H:%M:%S') as time, changes from eth_lake.snapshots() order by 1",
       "select * from eth_lake.current_snapshot()",
       f"insert into raw.blocks select * exclude (logs_bloom, last_modified) from read_parquet('{B}/date=2026-11-01/*.parquet')",
       "select snapshot_id, changes from eth_lake.snapshots() order by 1 desc limit 2",
       "select count(*) as blocks from raw.blocks")
lesson('2.5',
       "select count(*) as blocks from raw.blocks at (version => 3)",
       "select count(*) as blocks from raw.blocks at (version => 4)",
       "select count(*) as blocks from raw.blocks at (version => 5)",
       "select count(*) as blocks from raw.blocks at (version => 6)",
       "select strftime(date, '%Y-%m') as month, count(*) as blocks from raw.blocks at (version => 4) group by all order by 1",
       "select count(*) as blocks from raw.blocks at (timestamp => now() - interval '1 second')",
       "create table raw.blocks_october as select * from raw.blocks at (version => 5) where date >= date '2026-10-01'",
       "select count(*) from raw.blocks_october",
       "drop table raw.blocks_october")
lesson('3.1',
       "create table raw.blocks_day as select * from raw.blocks where date = date '2026-10-01'",
       "select count(*) as blocks, count(*) filter (where transaction_count < 50) as small from raw.blocks_day",
       "delete from raw.blocks_day where transaction_count < 50",
       "update raw.blocks_day set extra_data = upper(extra_data) where number % 100 = 0",
       "select data_file, data_file_size_bytes, delete_file from ducklake_list_files('eth_lake', 'blocks_day', schema => 'raw')",
       "select * from read_parquet('{LAKE}/data/raw/blocks_day/*-delete.parquet') limit 3",
       "select count(*) from read_parquet('{LAKE}/data/raw/blocks_day/*-delete.parquet')",
       "select snapshot_id, changes from eth_lake.snapshots() order by 1 desc limit 4")
lesson('3.2',
       f"insert into raw.blocks select s.* exclude (logs_bloom, last_modified) from read_parquet('{B}/date=2026-11-02/*.parquet') as s where not exists (select 1 from raw.blocks as t where t.number = s.number)",
       f"insert into raw.blocks select s.* exclude (logs_bloom, last_modified) from read_parquet('{B}/date=2026-11-02/*.parquet') as s where not exists (select 1 from raw.blocks as t where t.number = s.number)",
       "select date, count(*) as blocks from raw.blocks where date >= date '2026-11-01' group by all order by 1",
       "select snapshot_id, changes from eth_lake.snapshots() order by 1 desc limit 2")
lesson('3.3',
       "alter table raw.blocks add column gas_used_pct double",
       "update raw.blocks set gas_used_pct = round(100.0 * gas_used / gas_limit, 2) where date = date '2026-11-02'",
       "alter table raw.blocks rename miner to fee_recipient",
       "select typeof(transaction_count), typeof(size) from raw.blocks limit 1",
       "alter table raw.blocks alter transaction_count set type bigint",
       "alter table raw.blocks alter number set not null",
       "comment on table raw.blocks is 'One row per Ethereum block, from the AWS public blockchain dataset'",
       "select number, fee_recipient, gas_used_pct from raw.blocks where date = date '2026-11-02' limit 3",
       "select number, miner from raw.blocks at (version => 6) limit 3",
       "select snapshot_id, changes from eth_lake.snapshots() order by 1 desc limit 6")
lesson('3.4',
       "select snapshot_id, rowid, change_type, number, extra_data from eth_lake.table_changes('blocks_day', 0, 1000) where change_type <> 'insert' order by snapshot_id, rowid limit 6",
       "select change_type, count(*) from eth_lake.table_changes('blocks_day', 0, 1000) group by all order by 1",
       "select snapshot_id, rowid, change_type from ducklake_table_changes('eth_lake', 'raw', 'blocks_day', 0, 1000) limit 2")
lesson('3.5',
       "select 1")
TX = ("hash, block_number, block_timestamp, transaction_index, from_address, to_address, value, gas, gas_price, "
      "receipt_gas_used, receipt_effective_gas_price, receipt_status, transaction_type, max_fee_per_gas, max_priority_fee_per_gas, date")
lesson('4.1',
       "create table raw.transactions (hash varchar, block_number bigint, block_timestamp timestamp, transaction_index bigint, from_address varchar, to_address varchar, value double, gas bigint, gas_price bigint, receipt_gas_used bigint, receipt_effective_gas_price bigint, receipt_status bigint, transaction_type bigint, max_fee_per_gas bigint, max_priority_fee_per_gas bigint, date date)",
       "alter table raw.transactions set partitioned by (date)",
       f"insert into raw.transactions select {TX} from read_parquet('s3://aws-public-blockchain/v1.0/eth/transactions/date=2026-10-0[1-7]/*.parquet')",
       "select date, count(*) as transactions from raw.transactions group by all order by 1",
       "select count(*) as files from glob('{LAKE}/data/raw/transactions/**/*.parquet')",
       "select file from glob('{LAKE}/data/raw/transactions/**/*.parquet') limit 4",
       "explain analyze select count(*) from raw.transactions where date = date '2026-10-03'")
lesson('4.2',
       "select min(block_number), max(block_number) from raw.transactions",
       "alter table raw.transactions set sorted by (block_number asc)",
       "call ducklake_rewrite_data_files('eth_lake', 'transactions', schema => 'raw')",
       "call ducklake_merge_adjacent_files('eth_lake', 'transactions', schema => 'raw')",
       "select count(*) as files from ducklake_list_files('eth_lake', 'transactions', schema => 'raw')",
       "select option_name, value, scope from eth_lake.options()",
       "explain analyze select count(*) from raw.transactions where block_number between 26100000 and 26100100")
lesson('4.3',
       "create table raw.watchlist (address varchar, label varchar)",
       "call eth_lake.set_option('data_inlining_row_limit', 100, schema => 'raw', table_name => 'watchlist')",
       "insert into raw.watchlist values ('0x00000000219ab540356cbb839cbe05303d7705fa', 'staking deposit'), ('0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2', 'wrapped ether')",
       "select * from raw.watchlist",
       "select * from ducklake_list_files('eth_lake', 'watchlist', schema => 'raw')",
       "call ducklake_flush_inlined_data('eth_lake', schema_name => 'raw', table_name => 'watchlist')",
       "select * from ducklake_list_files('eth_lake', 'watchlist', schema => 'raw')")
lesson('4.4',
       "select count(*) as files, round(sum(size) / 1e6, 1) as mb from (select file, (select 0) as size from glob('{LAKE}/data/**/*.parquet'))",
       "select count(*) as files from glob('{LAKE}/data/**/*.parquet')",
       "call ducklake_merge_adjacent_files('eth_lake')",
       "select count(*) as files from glob('{LAKE}/data/**/*.parquet')",
       "call ducklake_expire_snapshots('eth_lake', dry_run => true, older_than => now())",
       "call ducklake_expire_snapshots('eth_lake', older_than => now())",
       "select count(*) as snapshots from eth_lake.snapshots()",
       "call ducklake_cleanup_old_files('eth_lake', dry_run => true, cleanup_all => true)",
       "call ducklake_cleanup_old_files('eth_lake', cleanup_all => true)",
       "select count(*) as files from glob('{LAKE}/data/**/*.parquet')",
       "checkpoint",
       "select count(*) as files from glob('{LAKE}/data/**/*.parquet')")
lesson('4.5',
       f"copy (select * exclude (logs_bloom, last_modified, miner), miner as fee_recipient, round(100.0 * gas_used / gas_limit, 2) as gas_used_pct from read_parquet('{B}/date=2026-11-03/*.parquet')) to '{{LAKE}}/landing/blocks_2026-11-03.parquet'",
       "call ducklake_add_data_files('eth_lake', 'blocks', '{LAKE}/landing/blocks_2026-11-03.parquet', schema => 'raw')",
       "select date, count(*) from raw.blocks where date >= date '2026-11-01' group by all order by 1",
       "select data_file from ducklake_list_files('eth_lake', 'blocks', schema => 'raw') where data_file like '%landing%'")
lesson('5.1',
       "select database_name from duckdb_databases()",
       "select snapshot_id, schema_version, strftime(snapshot_time, '%H:%M') from __ducklake_metadata_eth_lake.ducklake_snapshot order by 1",
       "select * from __ducklake_metadata_eth_lake.ducklake_snapshot_changes order by snapshot_id limit 4",
       "select table_id, table_name, schema_id, begin_snapshot, end_snapshot from __ducklake_metadata_eth_lake.ducklake_table order by 1",
       "select column_id, column_name, column_type, begin_snapshot, end_snapshot from __ducklake_metadata_eth_lake.ducklake_column where table_id = 2 and column_name in ('miner', 'fee_recipient', 'transaction_count') order by 1, 4",
       "select key, value from __ducklake_metadata_eth_lake.ducklake_metadata")
lesson('5.2',
       "select data_file_id, table_id, record_count, file_size_bytes, path from __ducklake_metadata_eth_lake.ducklake_data_file where end_snapshot is null limit 5",
       "select f.path, s.min_value, s.max_value from __ducklake_metadata_eth_lake.ducklake_file_column_stats s join __ducklake_metadata_eth_lake.ducklake_data_file f using (data_file_id) join __ducklake_metadata_eth_lake.ducklake_column c on c.column_id = s.column_id and c.table_id = f.table_id where c.column_name = 'block_number' and f.end_snapshot is null limit 8",
       "select * from __ducklake_metadata_eth_lake.ducklake_file_partition_value limit 5",
       "select * from __ducklake_metadata_eth_lake.ducklake_table_stats",
       "select * from __ducklake_metadata_eth_lake.ducklake_inlined_data_tables")
lesson('5.3',
       "select max(snapshot_id) from __ducklake_metadata_eth_lake.ducklake_snapshot",
       "select table_id, table_name from __ducklake_metadata_eth_lake.ducklake_table where table_name = 'blocks' and end_snapshot is null",
       "select path, path_is_relative from __ducklake_metadata_eth_lake.ducklake_data_file where table_id = 2 and end_snapshot is null",
       "select count(*) from raw.blocks")
print('\nsnapshots:', con.execute('select max(snapshot_id) from eth_lake.snapshots()').fetchone())
