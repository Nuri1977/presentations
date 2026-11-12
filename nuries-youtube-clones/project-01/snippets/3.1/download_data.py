"""Download the 2025 NYC TLC green taxi trip files into data/raw/ and load them into
raw.green_trips in the DuckDB file at DUCKDB_PATH. Run from the repo root."""
import os
import urllib.request
from pathlib import Path

import duckdb

BASE = "https://d37ci6vzurychx.cloudfront.net/trip-data"
RAW = Path("data/raw")

RAW.mkdir(parents=True, exist_ok=True)
for month in range(1, 13):
    name = f"green_tripdata_2025-{month:02d}.parquet"
    target = RAW / name
    if target.exists():
        print("have", name)
        continue
    print("downloading", name)
    request = urllib.request.Request(f"{BASE}/{name}", headers={"User-Agent": "nyc-taxi-dbt-course"})
    with urllib.request.urlopen(request) as response:
        target.write_bytes(response.read())

con = duckdb.connect(os.environ["DUCKDB_PATH"])
con.execute("create schema if not exists raw")
con.execute("create or replace table raw.green_trips as "
            "select * from read_parquet('data/raw/green_tripdata_2025-*.parquet', union_by_name = true)")
print("loaded", con.execute("select count(*) from raw.green_trips").fetchone()[0], "rows")
con.close()
