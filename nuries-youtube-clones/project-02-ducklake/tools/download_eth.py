"""Download the course's Ethereum data once into .cache/data/eth (one Parquet file per day).
blocks: 2026-08-01 .. 2026-10-31 (92 days, three months) plus 2026-11-01..03 for the later lessons, without logs_bloom.
transactions: 2026-10-01 .. 2026-10-07, without the large `input` column.
Run with the pinned runtime: _academy-video-tooling/.cache/dbt-env/bin/python tools/download_eth.py"""
import datetime as dt, pathlib, time, duckdb
ROOT = pathlib.Path(__file__).resolve().parents[1] / '.cache' / 'data' / 'eth'
B = 's3://aws-public-blockchain/v1.0/eth'
con = duckdb.connect(); con.execute("install httpfs; load httpfs; set s3_region='us-east-2';")
def days(a, n): return [a + dt.timedelta(days=i) for i in range(n)]
TX = ("hash, block_number, block_timestamp, transaction_index, from_address, to_address, value, gas, gas_price, "
      "receipt_gas_used, receipt_effective_gas_price, receipt_status, transaction_type, max_fee_per_gas, "
      "max_priority_fee_per_gas, date")
jobs = [('blocks', d, '* exclude (logs_bloom, last_modified)') for d in days(dt.date(2026, 8, 1), 92) + days(dt.date(2026, 11, 1), 3)]
jobs += [('transactions', d, TX) for d in days(dt.date(2026, 10, 1), 7)]
for table, d, cols in jobs:
    out = ROOT / table / f'{table}_{d}.parquet'
    if out.exists(): continue
    t0 = time.time()
    con.execute(f"copy (select {cols} from read_parquet('{B}/{table}/date={d}/*.parquet')) to '{out}.tmp' (format parquet, compression zstd)")
    pathlib.Path(f'{out}.tmp').rename(out)
    print(table, d, f'{out.stat().st_size/1e6:.1f} MB', f'{time.time()-t0:.0f}s', flush=True)
print('done')
