# Ship & Automate: CI with GitHub Actions — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `lesson-2-8-end`: a clone of what Lesson 2.8 pushed, the parquet files in data/raw, the nyc_taxi_dev connection, and the database after dbt build (off camera).

## s02 · Four files

| Listen for | Do this |
|---|---|
| "Open the project. First, requirements dot text in…" | On the home screen, click **nyc_taxi** under Recent Projects<br>Right-click the project root → **New File** → `requirements.txt` → **Save**<br>Type:<br><br>```sql<br>dbt-core==1.12.6<br>dbt-duckdb==1.11.1<br>```<br>Click **Save** (top right of the editor)<br>(Check that `requirements.txt` matches `../snippets/3.1/requirements.txt`) |
| "Next, a folder called c i, with its…" | Close the editor tab for `requirements.txt` (its ×)<br>new_root_folder: ci<br>Right-click `ci` → **New File**, type `profiles.yml`, click **Save** |
| "Type the profile: nyc taxi, target prod, type…" | Type:<br><br>```sql<br>nyc_taxi:<br>  target: prod<br>  outputs:<br>    prod:<br>      type: duckdb<br>      path: "{{ env_var('DUCKDB_PATH') }}"<br>      threads: 4<br>```<br>Click **Save** (top right of the editor)<br>(Check that `ci/profiles.yml` matches `../snippets/3.1/profiles.yml`) |
| "The parquet files are not in git, so…" | Close the editor tab for `ci/profiles.yml` (its ×)<br>new_root_folder: scripts<br>Right-click `scripts` → **New File**, type `download_data.py`, click **Save** |
| "Paste the script. It downloads the twelve files…" | paste: """Download the 2025 NYC TLC green taxi trip files into data/raw/ and load them into<br>raw.green_trips in the DuckDB file at DUCKDB_PATH. Run from the repo root."""<br>import os<br>import urllib.request<br>from pathlib import Path<br><br>import duckdb<br><br>BASE = "https://d37ci6vzurychx.cloudfront.net/trip-data"<br>RAW = Path("data/raw")<br><br>RAW.mkdir(parents=True, exist_ok=True)<br>for month in range(1, 13):<br>    name = f"green_tripdata_2025-{month:02d}.parquet"<br>    target = RAW / name<br>    if target.exists():<br>        print("have", name)<br>        continue<br>    print("downloading", name)<br>    request = urllib.request.Request(f"{BASE}/{name}", headers={"User-Agent": "nyc-taxi-dbt-course"})<br>    with urllib.request.urlopen(request) as response:<br>        target.write_bytes(response.read())<br><br>con = duckdb.connect(os.environ["DUCKDB_PATH"])<br>con.execute("create schema if not exists raw")<br>con.execute("create or replace table raw.green_trips as "<br>            "select * from read_parquet('data/raw/green_tripdata_2025-*.parquet', union_by_name = true)")<br>print("loaded", con.execute("select count(*) from raw.green_trips").fetchone()[0], "rows")<br>con.close()<br><br>Click **Save** (top right of the editor)<br>(Check that `scripts/download_data.py` matches `../snippets/3.1/download_data.py`) |
| "And the workflow. GitHub looks for it in…" | Close the editor tab for `scripts/download_data.py` (its ×)<br>new_root_folder: .github<br>Right-click `.github` → **New Folder**, type `workflows`, click **Save**<br>Right-click `.github/workflows` → **New File**, type `dbt_build.yml`, click **Save** |
| "Paste the workflow, and save.…" | paste: name: dbt build & publish<br>on:<br>  push:<br>    branches: [main]<br>  schedule:<br>    - cron: '23 5 * * 1'     # every Monday<br>  workflow_dispatch:<br>permissions:<br>  contents: write<br>jobs:<br>  build:<br>    runs-on: ubuntu-latest<br>    env:<br>      DUCKDB_PATH: ${{ github.workspace }}/data/prod.duckdb<br>    steps:<br>      - uses: actions/checkout@v7<br>      - uses: actions/setup-python@v7<br>        with:<br>          python-version: '3.10'<br>          cache: pip<br>      - run: pip install -r requirements.txt<br>      - run: python scripts/download_data.py<br>      - run: dbt build --profiles-dir ci<br>      - name: Publish the warehouse<br>        run: |<br>          gh release create warehouse --title "Warehouse" --notes "Built by dbt on every push" || true<br>          gh release upload warehouse data/prod.duckdb --clobber<br>        env:<br>          GH_TOKEN: ${{ github.token }}<br><br>Click **Save** (top right of the editor)<br>(Check that `.github/workflows/dbt_build.yml` matches `../snippets/3.1/dbt_build.yml`) |

## s04 · Commit and push

| Listen for | Do this |
|---|---|
| "Open the Git tab: four new files.…" | Close the editor tab for `.github/workflows/dbt_build.yml` (its ×)<br>Click the **Git** tab at the top of the sidebar |
| "Stage all, type a message, add CI: build,…" | Hover CHANGES and click **+** (Stage All Changes)<br>Click the message box and type: Add CI: build, test and publish the warehouse<br>Click **Commit** |
| "Sync Changes. This push starts the first run.…" | git_push: None |

## s05 · The run on GitHub

| Listen for | Do this |
|---|---|
| "On GitHub, open the Actions tab. The run…" | In the browser, open https://github.com/Nuri1977/nyc-taxi-dbt/actions |
| "Open it, and wait. A fresh machine installs…" | Wait for “Add CI: build, test and publish the warehouse”<br>Click **the run**<br>Wait for “^Success$” |
| "And under Releases, the warehouse release, with prod…" | In the browser, open https://github.com/Nuri1977/nyc-taxi-dbt/releases/tag/warehouse |
