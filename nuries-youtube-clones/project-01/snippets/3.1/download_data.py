"""Download the 2025 NYC TLC green taxi trip files into data/raw/. Run from the repo root."""
import urllib.request
from pathlib import Path

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
print("done")
