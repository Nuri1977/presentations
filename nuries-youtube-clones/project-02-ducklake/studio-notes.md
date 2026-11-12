# Studio notes: DuckLake course (Project 2)

Phase 0 checks, 11 Nov 2026. Rosetta DBT Studio 1.7.6 (Mac x64), `@duckdb/node-api` 1.5.2-r.1, DuckLake
extension build `415a9ebd`; pinned dbt runtime: dbt-core 1.12.6, dbt-duckdb 1.11.1, DuckDB 1.5.6.

## Data (downloaded with tools/download_eth.py into .cache/data/eth)

| Table | Days | Rows | On disk (zstd Parquet) |
|---|---|---|---|
| blocks, without `logs_bloom` | 93 (2026-08-01 .. 10-29, plus 11-01 .. 11-03) | 667,086 | 126 MB, about 1.4 MB a day |
| transactions, without `input` | 7 (2026-10-01 .. 10-07) | 12,695,803 | 886 MB, 105 to 149 MB a day |

- Transactions per day: 2,036,041 / 1,875,646 / 1,562,292 / 1,526,358 / 1,774,270 / 1,957,602 / 1,963,594.
- Block numbers in that week: 26,093,738 to 26,143,955.
- Download time here: blocks about 3 s a day, transactions about 53 s a day (S3 → local, columns trimmed).

## Data Lake screens

- Sidebar **DataLake** → DataLake Dashboard; **New DataLake** → DuckLake (Apache Iceberg BETA; Delta Lake and
  Apache Hudi "Soon").
- Wizard: Instance Details → Storage Configuration (local / s3 / azure / Google Cloud; local path must be
  absolute) → Catalog Configuration → Runtime Options (Max Memory 4GB, Thread Count 4, query optimizer,
  temp dir) → Review & Create → **Create Instance**.
- Catalog: **DuckDB only** (SQLite and PostgreSQL are "Soon"). The file must end in `.db` or `.duckdb`.
  Default offered: `/tmp/ducklake/<name>.duckdb`.
- Instance page tabs: **Tables & Views, Overview, History, Activity**; buttons Refresh, Edit, Delete,
  **Import Data**.
- Creating the instance writes the catalog file (+ `.wal`) and leaves the data folder empty.

## SQL Editor on a lake

- Connection list has a **DuckLake Instances** group. With `eth_lake` selected, `current_database()` is
  `eth_lake` and the schema is `main`, so `raw.blocks` works without the lake name.
- **Works:** `select`, `create schema`, `create table … as select … from read_parquet('s3://…')` (S3 reads
  need no setup), `alter table … set sorted by`, `call eth_lake.set_option(…)`,
  `call ducklake_merge_adjacent_files('eth_lake')`, `select … from eth_lake.snapshots()`, `glob()`.
- **Rejected by Studio before DuckDB sees it** ("Query must be a SELECT or WITH or EXPLAIN or INSERT or UPDATE
  or DELETE or CREATE or DROP or ALTER or TRUNCATE or RENAME or DESCRIBE or PRAGMA or SHOW or COPY or VACUUM
  or CALL or CHECKPOINT statement"):
  - statements that start with `FROM` → always write `select * from …`;
  - `SET …` → no session settings (use `call <lake>.set_option`, or table options);
  - `BEGIN … COMMIT` → **no explicit transactions and no commit messages** in the SQL Editor. Not listed
    either, and tested as rejected: `MERGE`, `ATTACH`, `USE`, `LOAD`.
- Also works (second battery): `insert`, `update`, `delete` ("1 row affected"), `with … select`,
  `describe`, `show tables`, `pragma database_list`, `checkpoint`, `copy (…) to '<file>'`.
- **Long lines:** a statement wider than the editor scrolls sideways and the run arrow click misses; the
  result pane then still shows the previous statement's "Command executed successfully". The recorder must
  reset the scroll (Cmd+Up, Home) before clicking, and lesson SQL should use short paths or several lines.
- Studio appends `LIMIT 10` to a select for the result grid.
- Snapshot numbering: creating a schema is snapshot 1, so the first table is snapshot 2.

## dbt on the lake

- A lake created by Studio (DuckDB 1.5.2) attaches and is written by dbt's DuckDB 1.5.6 with **no catalog
  migration**. Studio reads it again afterwards: the Data Lake page lists dbt's table and view, and
  `snapshots()` shows dbt's snapshots.
- Profile that works: `attach: [{ path: "ducklake:<abs>/lake/eth_catalog.duckdb", alias: eth_lake,
  options: { data_path: "<abs>/lake/data/" } }]`, `database: eth_lake`, `schema: main`, `threads: 1`.
- A view and an incremental model (`unique_key`) both build; a second run is clean. dbt's view swap creates
  several snapshots per run (`__dbt_tmp`, `__dbt_backup` views appear in `snapshots().changes`).
- **The catalog stores the data folder's absolute path.** Attaching with a different `DATA_PATH` fails
  ("does not match existing data path … set OVERRIDE_DATA_PATH"). A lake folder cannot simply be copied or
  moved; start states must build the lake at the learner path, or attach with `override_data_path: true`.

## One writer at a time (the catalog file lock)

- Studio connects to a lake lazily: on the Data Lake instance page, in the SQL Editor or in a notebook.
  From then on it holds a lock on `eth_catalog.duckdb` **until Studio is quit**. Going back to Home, or
  waiting 60 s in Settings, does not release it. The Edit screen only changes name, description and runtime
  options, so it is no way to disconnect.
- While the lock is held, dbt fails: `IO Error: Failed to attach DuckLake MetaData … Could not set lock on
  file … Conflicting lock is held in … Rosetta DBT Studio (PID …)`.
- After a restart of Studio, with the lake not yet opened, `dbt run` passes. Opening the lake afterwards
  shows dbt's objects.
- Consequence: in a lesson, dbt runs first and the lake is opened after; a second dbt run after opening
  the lake needs a restart of Studio.

## Notebooks

- Sidebar **Notebooks**; the connection list offers the lake (**DuckLake Instances ▸ eth_lake**).
- "Create New Notebook" asks for a name and a Python version and builds a dedicated virtual environment
  with ipykernel (about a minute; closing Studio during that step leaves "Environment missing — recreate",
  one click to fix). Cells: Code, SQL, Text. A SQL cell returns "Result as `df`" (a list of dicts unless
  pandas is installed).
- SQL cells use the same statement filter as the SQL Editor: `select` works; `MERGE` → "Query must be a
  SELECT or WITH …"; `begin; …; commit;` → "Multiple SQL statements are not allowed. Query contains
  statement chaining."

## What dbt can do that the SQL Editor cannot

- `incremental_strategy: merge` with `unique_key` compiles to `MERGE INTO "eth_lake"."main"."<model>" …`
  and runs on the lake (two runs, both pass).
- `post_hook: "call eth_lake.set_commit_message('dbt', '<text>')"` sets `author` and `commit_message` on
  the snapshot dbt creates (seen in `snapshots()`).

## Settings and the website

- Settings sidebar: General, AI Settings, Rosetta Cloud, Keystore, Task Manager, Backup & Restore,
  dbt Core, Python, Rosetta CLI, **DuckDB**, Flowfile, Local Runner, Documentation, About.
- Settings ▸ DuckDB: "Persistent Database (DuckDB)", status, file size, active connections (0 / 10), path,
  Diagnostics, Reinitialize Database. This is Studio's own cache database, not the lake (useful for 1.6).
  The status bar shows "DuckDB: 1.5.2-r.1".
- `rosettadb.io` → "Download Now" → `rosettadb.io/download-dbtstudio.html` ("Download Rosetta DBT Studio",
  cards for Windows, Linux, macOS). Links point at GitHub release 1.7.6: Windows `.exe`, Linux `.deb` and
  `.rpm`, Mac ARM64 and Mac Intel `.dmg`. No cookie banner.

## RustFS (S3-compatible storage in Docker), checked 11 Nov 2026

- Image `rustfs/rustfs` (Apache 2.0). Tested tag: `1.0.0-beta.11`. S3 API on 9000, console on 9001, data in
  `/data` (named volume needs no chown; a bind mount needs `chown 10001:10001`). Keys through
  `RUSTFS_ACCESS_KEY` / `RUSTFS_SECRET_KEY`. Path-style addressing, plain http on localhost.
- **Decision (Nuri, 11 Nov): use the existing RustFS container**, `iceberg-v01-rustfs-1`
  (`rustfs/rustfs:1.0.0-beta.11`, 127.0.0.1:9000 S3 API, 9001 console, named volumes
  `iceberg-v01_rustfs-data` → `/data` and `iceberg-v01_rustfs-logs` → `/logs`, restart `unless-stopped`,
  compose file under `conbined-dbt-project_01/…/version-01-iceberg/compose.yml`). It starts with Docker
  Desktop. Its keys come from the container's environment and are never shown on screen or written here.
- **Bucket `eth-lake` created there** for the DuckLake course (next to the existing `iceberg-lakekeeper`,
  untouched). DuckLake write, delete and read against `s3://eth-lake/` on port 9000 verified; the probe
  files were removed, the bucket is empty. The earlier test container on 9100/9101 is removed.
- **DuckDB 1.5.6 + DuckLake on RustFS works** with a full secret: `ENDPOINT 'localhost:9000', USE_SSL false,
  URL_STYLE 'path'`. Table data and delete files land in the bucket as
  `data/<schema>/<table>/ducklake-<uuid>.parquet`. Endpoint only, or an endpoint with `http://`, fails
  (DuckDB then calls `https://<bucket>.localhost:…`).
- **dbt on a RustFS lake works**: `secrets:` (type s3, endpoint, `use_ssl: false`, `url_style: path`, keys
  from `env_var`) plus `attach` with `data_path: "s3://eth-lake/data/"`; `merge` incremental runs twice.
- **Object Explorer (Cloud Explorer) has a `rustfs` source type** (also MinIO, Cloudflare R2, Backblaze B2,
  Garage): name, endpoint `host:port`, "Use SSL/TLS" switch, access key, secret key, region. **Test
  Connection against the RustFS container passes** ("Connection Successful").
- **Save Connection stores the secret in the macOS Keychain.** The recorder runs Studio with the learner
  home, which had no keychain ("Keychain Not Found" dialog; never press Reset To Defaults). Nuri created a
  separate keychain for it: `/Users/Shared/academy/learner/Library/Keychains/login.keychain-db` (set as the
  learner home's default, no timeout). His real login keychain is unchanged. After that the save works with
  no prompt. Keychain access is blocked inside Claude's sandboxed shell, so Studio runs that save a source
  must be started outside the sandbox.
- **Object Explorer on RustFS works (tested, endpoint `localhost:9000`):** the saved source `rustfs_local`
  lists both buckets (`eth-lake`, `iceberg-lakekeeper`) with a **Create bucket** button; opening `eth-lake`
  shows Upload, Create folder, a breadcrumb and a type filter.
- **The DuckLake wizard does not accept the RustFS source (tested).** With `rustfs_local` saved, the `s3`
  storage step still says "No AWS S3 connections found": it lists only sources of type Amazon S3, and that
  type has no endpoint field. So in 1.7.6 a DuckLake registered in Studio (Data Lake screens, lake
  connection in the SQL Editor and notebooks) can use local storage or real AWS S3, not RustFS. In the
  current Studio source the two places are `DataLakeConnectionSelector.tsx` (provider filter `aws` /
  `azure` / `gcs`) and the DuckLake adapter's S3 secret in `duckLake/adapters/base.adapter.ts` (sets
  `ENDPOINT`, not `USE_SSL` or `URL_STYLE`, which RustFS over http needs).
- **Outcome (Nuri, 11 Nov):** the course keeps local file storage. RustFS is not used. The empty bucket
  `eth-lake` is still in the `iceberg-v01` RustFS, and the learner keychain stays (harmless, useful if a
  later course saves Object Explorer sources).

## Recording notes (11 Nov 2026)

- `datalake/instances.json` in Studio's user data folder holds the registered lakes (name, data path,
  catalog path, runtime options, status). Seeding that file plus building the lake at the same paths gives a
  lesson a registered lake without the wizard; Studio 1.5.2 reads a lake built by Python DuckDB 1.5.6.
- A new lake has snapshot 0 (`created_schema:"main"`). The History tab shows Snapshot ID, Time, Schema
  Version, Author, Message, Changes.
- The wizard's catalog field is pre-filled with `/tmp/ducklake/<name>.duckdb`; replace it.
- On an empty dashboard the lake is created with **Create DataLake** (main area) or **New DataLake**
  (sidebar bottom); the next screen offers DuckLake, Apache Iceberg (BETA), Delta Lake, Apache Hudi.

## The result pane runs a statement twice (found 12 Nov 2026)

- In the SQL Editor on a lake, a statement whose result is shown as a table is executed twice: once by the
  editor, and again by the result pane to fetch the page of rows (`queryResult.tsx`, `fetchPage`).
  Statements that only show "Command executed successfully" (CREATE … AS, INSERT, UPDATE, DELETE) run once.
- So a `CALL` that changes the lake and returns rows runs twice. Harmless for set_option, merge, expire,
  cleanup, flush and checkpoint; wrong for `ducklake_add_data_files` (the file was registered twice).
  Workaround in Lesson 4.5: `create temp table added_files as select * from ducklake_add_data_files(…)`.
- Studio's DuckDB 1.5.2 (ducklake 415a9ebd) reports updates in `ducklake_table_changes` as delete + insert;
  1.5.6 reports update_preimage / update_postimage (Lesson 3.4 narration says so).
- Result grid: DATE shows as {"days": n}, TIMESTAMP as {"micros": n}; format with strftime.
- Start-state lakes are built with DuckDB 1.5.2 (`_academy-video-tooling/.cache/seed-env`).
