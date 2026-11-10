# Studio notes: real labels and surprises (Project 1)

Checked in Rosetta DBT Studio **1.7.6** (official Mac x64 release), dbt-core 1.12.6, dbt-duckdb 1.11.1,
Python 3.10.17, on 9 Nov 2026, while making the Lesson 3.3 review video (fast path, stills recorder).

## Needs a decision (affects several lessons)

**Views over relative parquet paths cannot be queried inside Studio.**
`models/sources.yml` (A2) reads `read_parquet('data/raw/green_tripdata_2025-*.parquet', ...)`. dbt runs in the
project folder, so `dbt run`, `dbt build` and `dbt show` work. But Studio's **SQL Editor**, the **Execute Query**
lens above a model and **Model ▸ Preview** run DuckDB inside Studio, whose working folder is `/` when the app is
opened from Finder. Every query that reads the `trips` view fails with
`IO Error: No files found that match the pattern "data/raw/green_tripdata_2025-*.parquet"`.

- Lesson 3.3 (this video) uses `dbt show --select trips --limit 10` in the command box under Studio's terminal instead.
- Plan scenes affected: 3.2 s06 (`count(*)` over `read_parquet('data/raw/*.parquet')` in the SQL Editor), and any
  SQL Editor query on `trips` or on the marts **before 3.7** (they are views until then). Queries on
  `information_schema` / `duckdb_columns()` (3.5 s04, 3.7 s02) read only metadata and should work. After 3.7 the
  marts are tables, so the SQL Editor works on them.
- Not a fix: Jinja in `sources.yml` cannot see the project folder (`invocation_args_dict` is undefined there).
- Options: (a) keep `dbt show` for looking at view rows (used here); (b) put an absolute path in `sources.yml`
  (breaks CI and other machines); (c) make `trips` a table from 3.3 (changes the 3.7 story).

## Real labels and behaviour (1.7.6)

| Plan says | Studio 1.7.6 shows / does |
|---|---|
| Source Control | **Git** tab at the top of the sidebar (Explorer, Search, Git, Database). Header "CHANGES", branch `main`. |
| Commit | Message box "Message (⌘+Enter to commit)", **Commit** button. Commit stays disabled until a file is staged: hover the file in CHANGES and click **+** (Stage Changes); the section header also has Stage All. |
| Project → Run | **Project** split button (top right) ▸ arrow ▸ Rosetta Raw/Staging/Incremental Layer, **Run, Test, Build, Compile, Debug, Generate Docs, Serve Docs, Clean, Deps, Seed**, Run Pipeline (Local Runner). |
| (model actions) | **Model** split button on an open model: Run, Run model+/+model/+model+, Build Model (+variants), Test (+variants), Compile, **Preview**. |
| Terminal | Bottom panel tabs TERMINAL, QUERY RESULTS (after a query), RUN HISTORY. Command box "Type a rosetta or dbt command..." under the terminal runs dbt in the project folder. |
| Run output | `1 of 1 OK created sql view model main.trips`; toast "dbt run completed successfully". |
| target/run | `target/run/nyc_taxi/models/trips.sql` holds `create view "dev"."main"."trips__dbt_tmp" as ( … )`. |
| Explorer | Shows `.git`, `logs`, `target` folders; git badges after file names (e.g. "+ U"). |
| Status bar | `v1.7.6`, branch `main`, `dbt: 1.12.6`, `Python: 3.10.17`, `DuckDB: 1.5.2-r.1`. |
| `dbt --version` | dbt 1.12.6 prints a note that "dbt v2 is available, and is the default for new installations". Check what a fresh Studio 1.7.6 install picks before 2.1 (plan D3). |

## First run and install (Lesson 1.1 rehearsal, 9 Nov 2026)

- Release page: 1.7.6 is "Latest", **26 assets**; GitHub shows x64.dmg 196 MB, arm64.dmg 187 MB, plus .exe, .deb, .rpm, .flatpak, .tar.gz, .zip and rosetta-runner binaries. All assets are listed (no "Show all").
- The Mac app is signed and **notarized** (`spctl`: accepted, Notarized Developer ID), so macOS shows its normal "downloaded from the Internet" open prompt.
- DMG: 540x380 window with `assets/dmg-background.png` ("Rosetta Studio — Drag the Rosetta Studio icon to the Applications folder to install"), app at (127,214), Applications link at (412,214).
- First launch with an empty profile takes about 60 s before the window appears, then **"Rosetta Studio - Setup"**:
  - Step 1 of 2: dbt version (**dbt 1.x** Recommended / dbt 2.x) → version list (**1.12.6 latest** … 1.11.10) → **Adapters**: dbt-core (fixed) plus postgres, snowflake, bigquery, redshift, databricks, kinetica **checked by default**, **dbt-duckdb unchecked** → Continue → **Optional tools** (Flowfile) → Continue → **Install** (also "Skip Setup").
  - Step 2 of 2: Python v3.10.17 (seconds), then "dbt 1.12.6 and 1 adapters" (dbt Core, then dbt-duckdb). With only dbt-duckdb: **73–85 s** here. Then **Finish**.
  - Result in Studio's folder: `python/cpython-3.10.17-x86_64-apple-darwin` (51 MB), `venv` with dbt-core 1.12.6 + dbt-duckdb 1.11.1 (346 MB).
- **Finish restarts Studio** (`app.relaunch()`); the recorder stops the detached copy and starts Studio again on the same profile, which looks the same on screen.
- After setup, the home screen (Workspace Overview) shows Recent Projects (0) and Configured Connections (0), no dialogs. Status bar: `dbt: 1.12.6`, `Python: 3.10.17`, `DuckDB: 1.5.2-r.1`, `Rosetta: 2.10.1`.

## Recording on this Mac (fast path)

- This Mac: Intel i7-9750H, 16 GB, macOS 15.7.9; one 1920x1080 display (Dell SE2422H) during recording.
- A titled window is clipped to 1920x1027 by the menu bar; the recorder puts Studio in simple full screen to get
  exactly 1920x1080 at scale 2 (3840x2160 frames).
- `app.getPath('home')` stays `/Users/nuri` even with `HOME` set; userData and the project are under
  `/Users/Shared/academy/learner`. No personal path appeared in the frames checked.

## Lessons 2.2–3.1 rehearsal (10 Nov 2026, Studio 1.7.6)

- **TLC site blocks automated browsers** (Akamai "Access Denied" for headless Chromium). Lesson 2.2 shows the download path and file links on a slide; links go in the description. Not worked around.
- **Explorer and Git tab do not watch the disk.** Files added outside Studio appear after the Explorer's refresh button (right of "Search files or folders...", no accessible name) or when the Git tab is opened. `target/` appears after a refresh, too.
- **Push after a commit:** with an upstream set, the Git tab's button reads **Sync Changes 1↑**; it pushes to origin/main.
- **Model menu** (split button above an open model): Run, Run model+ / +model / +model+, Build Model (+variants), Test (+variants), Compile, Preview.
- **Model ▸ Compile** opens a **"Compiled SQL: <model>"** window with tabs ORIGINAL SQL / COMPILED SQL (MUI tabs, role tab, names "Original SQL" / "Compiled SQL") and a Close button.
- **Command box quoting works:** `dbt show --inline "select count(*) as trips from {{ source('raw', 'green_trips') }}"` → 591375. `dbt show --select top_pickup_zones --limit 10` fails on a model that has its own `limit` (dbt wraps it); use `--inline "select * from {{ ref(...) }}"`.
- **SQL Editor** works for metadata and tables: `duckdb_columns()` comments (persist_docs) and `information_schema.tables`. Run the dbt command before opening the SQL Editor (it holds the DuckDB file open).
- **persist_docs** works with dbt-duckdb 1.11.1: relation and column comments land in DuckDB.
- **Serve Docs** runs `dbt docs serve` (port 8080, IPv4 127.0.0.1 only) and dbt opens the system browser. The recorder sets `BROWSER=/usr/bin/true` for Studio and opens `http://127.0.0.1:8080` in the recording browser. The server keeps running after Studio closes; record.cjs stops it at the end.
- **LINEAGE tab** appears in the bottom panel only after a run/build in the session (seen in 2.7 and 2.8, not in 2.6 right after opening). Lesson 2.6 shows lineage in the docs site instead.
- **accepted_values** on dbt Core 1.12.6: list under `arguments: values:` parses with no warning. Real boroughs in trips_per_month: Manhattan, Queens, Brooklyn, Bronx, Unknown, N/A, Staten Island, EWR (N/A = zone 265, Outside of NYC).
- **CI:** the stored token can push workflow files (3.1 push of `.github/workflows/dbt_build.yml` worked). First run: Success in 40 s; release `warehouse` with prod.duckdb (1.26 MB).
