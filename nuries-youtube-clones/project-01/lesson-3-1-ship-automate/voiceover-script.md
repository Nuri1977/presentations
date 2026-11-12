# Ship & Automate: CI with GitHub Actions — voice-over script and beat sheet

dbt + DuckDB in Rosetta DBT Studio · Module 3 · Ship it · next: Lesson 3.2 · Showcase

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `lesson-2-8-end`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 1 · Lesson 3.1. Ship & Automate. Badges: GitHub Actions, prod target, release.

## s01 · slide — slide `devprod`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | So far, everything ran on our laptop, in the dev target. Production should be built somewhere clean, only from what is in git. | dev: your laptop, Studio, nyc_taxi_dev.duckdb. prod: a clean machine, built from git, prod.duckdb. | 23 | 8 |
| b02 @0:11 | That is what CI does. On every push, GitHub Actions starts a fresh machine, installs dbt, downloads the data, runs dbt build, and publishes the warehouse. | CI: on every push, GitHub Actions installs dbt, downloads the data, runs dbt build, publishes prod.duckdb. | 26 | 12 |

## s02 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b03 @0:23 | Open the project. First, requirements dot text in the project root: the same dbt versions Studio uses. | Open project **nyc_taxi** from Recent Projects<br>Right-click the project root → **New File** → `requirements.txt` → **Save**<br>Type 36 characters into the editor<br>Click **Save**<br>(check: `requirements.txt` equals `../snippets/3.1/requirements.txt`)<br>Zoom: explorer | 17 | 14 |
| b04 @0:37 | Next, a folder called c i, with its own profiles dot yml: a prod target, and the database path from an environment variable. | Close the editor tab for `requirements.txt`<br>new_root_folder: ci<br>Right-click `ci` → **New File** → `profiles.yml` → **Save**<br>Zoom: explorer | 23 | 14 |
| b05 @0:51 | Type the profile: nyc taxi, target prod, type duckdb, and the path from env var duckdb path. | Type 125 characters into the editor<br>Click **Save**<br>(check: `ci/profiles.yml` equals `../snippets/3.1/profiles.yml`)<br>Zoom: code-close | 17 | 8 |
| b06 @0:59 | The parquet files are not in git, so CI has to get the data itself. A folder called scripts, and download data dot py. | Close the editor tab for `ci/profiles.yml`<br>new_root_folder: scripts<br>Right-click `scripts` → **New File** → `download_data.py` → **Save**<br>Zoom: explorer | 24 | 14 |
| b07 @1:13 | Paste the script. It downloads the twelve files into data raw, then loads them into raw green trips in the DuckDB file, the same load we did by hand in the SQL Editor. Save. | paste: """Download the 2025 NYC TLC green taxi trip files into data/raw/ and load them into
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
<br>Click **Save**<br>(check: `scripts/download_data.py` equals `../snippets/3.1/download_data.py`)<br>Zoom: code-mid | 34 | 13 |
| b08 @1:26 | And the workflow. GitHub looks for it in dot github, workflows. Make both folders, and a file: dbt build dot yml. | Close the editor tab for `scripts/download_data.py`<br>new_root_folder: .github<br>Right-click `.github` → **New Folder** → `workflows` → **Save**<br>Right-click `.github/workflows` → **New File** → `dbt_build.yml` → **Save**<br>Zoom: explorer | 21 | 21 |
| b09 @1:46 | Paste the workflow, and save. | paste: name: dbt build & publish
on:
  push:
    branches: [main]
  schedule:
    - cron: '23 5 * * 1'     # every Monday
  workflow_dispatch:
permissions:
  contents: write
jobs:
  build:
    runs-on: ubuntu-latest
    env:
      DUCKDB_PATH: ${{ github.workspace }}/data/prod.duckdb
    steps:
      - uses: actions/checkout@v7
      - uses: actions/setup-python@v7
        with:
          python-version: '3.10'
          cache: pip
      - run: pip install -r requirements.txt
      - run: python scripts/download_data.py
      - run: dbt build --profiles-dir ci
      - name: Publish the warehouse
        run: |
          gh release create warehouse --title "Warehouse" --notes "Built by dbt on every push" || true
          gh release upload warehouse data/prod.duckdb --clobber
        env:
          GH_TOKEN: ${{ github.token }}
<br>Click **Save**<br>(check: `.github/workflows/dbt_build.yml` equals `../snippets/3.1/dbt_build.yml`)<br>Zoom: code-mid | 5 | 3 |

## s03 · slide — slide `workflow`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b10 @1:49 | It runs on every push to main, every Monday morning, or by hand. It may write releases. | Triggers: push to main, every Monday, or by hand. Permission: write releases. | 17 | 6 |
| b11 @1:55 | The steps: check out the code, set up Python, install dbt, download and load the data, run dbt build with the c i profile, and upload prod dot duckdb to a release called warehouse. | Steps: checkout; Python 3.10; pip install -r requirements.txt; download and load the data; dbt build --profiles-dir ci; publish prod.duckdb to the release called warehouse. | 34 | 14 |

## s04 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b12 @2:09 | Open the Git tab: four new files. | Close the editor tab for `.github/workflows/dbt_build.yml`<br>Open the **Git** tab in the sidebar<br>Zoom: git-panel | 7 | 5 |
| b13 @2:14 | Stage all, type a message, add CI: build, test and publish the warehouse. Commit. | Hover CHANGES and click **+** (Stage All Changes)<br>Type the commit message “Add CI: build, test and publish the warehouse”<br>Click **Commit**<br>Zoom: git-panel | 14 | 8 |
| b14 @2:23 | Sync Changes. This push starts the first run. | git_push: None<br>Zoom: git-panel | 8 | 5 |

## s05 · browser — Browser

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b15 @2:28 | On GitHub, open the Actions tab. The run for our commit is there. | Browser: open https://github.com/Nuri1977/nyc-taxi-dbt/actions | 13 | 5 |
| b16 @2:33 | Open it, and wait. A fresh machine installs dbt, downloads and loads the files, and builds the project. Under a minute later: success. | Wait for “Add CI: build, test and publish the warehouse”<br>Click **the run**<br>Wait for “^Success$” | 23 | 15 |
| b17 @2:48 | And under Releases, the warehouse release, with prod dot duckdb attached: the whole warehouse, built by CI. | Browser: open https://github.com/Nuri1977/nyc-taxi-dbt/releases/tag/warehouse | 17 | 7 |

## s06 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b18 @2:56 | To recap: a prod profile, pinned versions, a download script, and one workflow. From now on, every push builds and tests the project on a clean machine, and publishes the warehouse. Next, we make it a showcase. | Recap: prod profile; pinned requirements; download script; workflow; every push builds, tests and publishes prod.duckdb. | 37 | 14 |

## s07 · closing card (4 s, no voice)

Next · Lesson 3.2 · Showcase. Code: github.com/Nuri1977/nyc-taxi-dbt.

**Total: 360 spoken words, 3:13 rendered.**
