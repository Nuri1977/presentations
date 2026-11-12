# Plan: DuckLake course (Project 2)

**Working title:** Data Lakes with DuckLake in Rosetta DBT Studio: an Ethereum lake on your laptop

**Status:** plan only (11 Nov 2026). Nothing is recorded, no repo exists yet, and no slide is built.
This document is the single source for the course. A later session turns each lesson into a `lesson.yaml`.

---

## 0. Summary

A 31-lesson video course that explains data lakes from zero and then teaches every part of DuckLake 1.0 with a
real example: public Ethereum data, loaded into a DuckLake that lives on the viewer's laptop, managed from
Rosetta DBT Studio. The first half uses Studio's Data Lake screens and SQL Editor. The second half builds a dbt
project whose models are written into the same lake.

| Item | Decision |
|---|---|
| Audience | Beginner data engineers: know SQL and basic dbt (for example, finished Project 1). Lakes, table formats and catalogs are explained from zero |
| Size | 31 lessons in 8 modules, 3 to 5 minutes each, about 2 h 5 min in total, plus one joined full-length video |
| Data | Ethereum only: 90 days of `blocks`, 7 days of trimmed `transactions`, from the public AWS bucket |
| Lake | Local only: DuckDB catalog file + local data folder. PostgreSQL catalog and object storage are slides in the last lesson |
| dbt | Both: Studio UI and SQL first (Modules 2 to 5), then dbt on the lake (Module 6) |
| Comparison | One theory module; Iceberg and Delta are explained, not demonstrated |
| Code repo | New public repo, one commit per hands-on lesson, pushed from Studio's Git tab. No CI lessons |
| Production | Project 1 pipeline: Studio 1.7.6 pinned, automated recording, UI zoom 1.25, Kokoro voice, 4K + 1080p |
| Slides | New white theme with the Rosetta orange accent (section 6) |
| Folder | `presentations/nuries-youtube-clones/project-02-ducklake/` |

## 1. Decisions from the grilling session (Nuri, 11 Nov 2026)

1. **Slides:** no white template exists in `presentations/` (searched). The plan specifies a new white theme.
2. **Audience:** beginner data engineers.
3. **Size:** about 25 lessons, then "add the catalog tables deep dive": 29 lessons.
4. **Dataset:** Nuri proposed Ethereum data; chosen as the only dataset (not NYC taxi).
5. **dbt role:** Studio UI and SQL first, then dbt.
6. **Catalog and storage:** local only.
7. **Comparison:** one theory module.
8. **Data scope:** blocks for 90 days, trimmed transactions for 7 days.
9. **Repo:** new public repo, one commit per lesson.
10. **Production:** same pipeline, Studio 1.7.6.
11. **Theme:** white, orange accent.
12. **Folder:** `project-02-ducklake`.
13. **Two more videos (Nuri, 11 Nov, during Phase 0):** "a video for installing Rosetta DBT Studio from the
    rosettadb.io UI" (Lesson 0.1) and "a video explaining how we use the node package for DuckDB and the
    DuckLake extension inside dbt studio" (Lesson 1.6). The course is now 31 lessons.
14. **Storage stays local (Nuri, 11 Nov, after the RustFS test):** RustFS in Docker was tried as the lake's
    storage. DuckDB and dbt work with it and Object Explorer can browse it, but the DuckLake wizard in
    Studio 1.7.6 has no support for S3-compatible storage. So the lake's files stay in a local folder, as in
    decision 6. A later DuckLake tutorial may use a PostgreSQL catalog with cloud S3. Test details:
    `studio-notes.md`.

## 2. Facts checked on 11 Nov 2026

### 2.1 DuckLake

- Docs: `https://ducklake.select/docs/stable/` is **DuckLake 1.0** (older: 0.1 to 0.4).
- The pinned runtime's DuckDB is **1.5.6**; `INSTALL ducklake; LOAD ducklake;` works there.
- Docs sections the course covers: Introduction, Installation, Connecting, Choosing a Catalog Database,
  Choosing Storage, Snapshots, Schema Evolution, Time Travel, Upserting, Configuration, Paths; Maintenance
  (Recommended Maintenance, Merge Files, Expire Snapshots, Cleanup of Files, Rewrite Files with Deletes,
  Checkpoint); Advanced Features (Constraints, Conflict Resolution, Data Change Feed, Data Inlining, Deletion
  Vectors, Encryption, Partitioning, Row Lineage, Sorted Tables, Transactions, Views, Comments, Macros);
  Metadata (List Files, Adding Files); Migrations; Guides (Access Control, Backups and Recovery, Remote Data
  Path, Public DuckLake on Object Storage, Troubleshooting); Unsupported Features; Specification (Data Types,
  Queries, and the catalog tables).
- Catalog databases in the docs: DuckDB file, SQLite, PostgreSQL, MySQL, and Quack (a DuckDB server).
- **Data inlining is on by default in 1.0:** small inserts stay in the catalog and write no Parquet file. The
  docs' own introduction turns it off (`CALL lake.set_option('data_inlining_row_limit', 0)`) to show files.
  The course does the same in Module 2 and explains inlining in 4.3.
- `MERGE INTO` on DuckLake supports a single UPDATE or DELETE action per statement (docs, Upserting).

### 2.2 Ethereum data

- Bucket: `s3://aws-public-blockchain/v1.0/eth/` (region `us-east-2`), public, no account needed, updated
  daily (newest folder on 11 Nov: `date=2026-11-10`).
- Layout: `<table>/date=YYYY-MM-DD/part-*.snappy.parquet`, one file per day.
- Tables: `blocks`, `transactions`, `logs`, `token_transfers`, `traces`, `contracts`.
- Measured for `date=2026-10-01`:

| Table | Rows | File size | Used in the course |
|---|---|---|---|
| blocks | 7,176 | 5.6 MB | Yes, 90 days |
| transactions | 2,036,041 | 838 MB | Yes, 7 days, without `input` |
| token_transfers | 3,461,091 | 491 MB | No |
| contracts | not measured | 16 MB | No |
| logs | not measured | 1.2 GB | No |
| traces | not measured | 3.0 GB | No |

- `blocks` columns: `number`, `hash`, `parent_hash`, `miner`, `timestamp`, `gas_limit`, `gas_used`,
  `base_fee_per_gas`, `transaction_count`, `size`, `difficulty`, `nonce`, `extra_data`, `logs_bloom`,
  `state_root`, `receipts_root`, `transactions_root`, `sha3_uncles`, `date`, `last_modified`.
- `transactions` columns: `hash`, `block_number`, `block_hash`, `block_timestamp`, `transaction_index`,
  `from_address`, `to_address`, `value` (DOUBLE, in wei), `gas`, `gas_price`, `input`, `nonce`,
  `receipt_gas_used`, `receipt_cumulative_gas_used`, `receipt_effective_gas_price`, `receipt_status`,
  `receipt_contract_address`, `transaction_type`, `max_fee_per_gas`, `max_priority_fee_per_gas`, `date`,
  `last_modified`.
- Measured in Phase 0 (local cache, zstd): blocks 93 days = 667,086 rows, 126 MB; transactions 7 days
  without `input` = 12,695,803 rows, 886 MB. Download: about 3 s per day of blocks, 53 s per day of
  transactions.

### 2.3 Rosetta DBT Studio 1.7.6

Checked in the app on 11 Nov 2026 (Phase 0, first pass):

- Sidebar entry **DataLake** → "DataLake Dashboard"; **New DataLake** → choose DuckLake (Apache Iceberg is
  BETA; Delta Lake and Apache Hudi are "Soon").
- Wizard steps: Instance Details (name, description) → Storage Configuration (local, s3, azure, Google
  Cloud; local needs an **absolute** path) → Catalog Configuration → Runtime Options (max memory 4GB,
  threads 4, query optimizer, temporary directory) → Review & Create → **Create Instance**.
- **Catalog: only DuckDB can be chosen**; SQLite and PostgreSQL are marked "Soon". The catalog file **must
  end in `.db` or `.duckdb`**, so the course uses `lake/eth_catalog.duckdb` (not `ethereum.ducklake`).
- After creation the instance page has tabs **Tables & Views, Overview, History, Activity**, and
  **Import Data**. The catalog file and the empty data folder exist on disk.
- The SQL Editor's connection list has a **DuckLake Instances** group with `eth_lake`.
- Studio's DuckDB is **1.5.2-r.1** (`@duckdb/node-api`); the pinned dbt runtime's DuckDB is 1.5.6.
- **SQL Editor on a lake (tested):** the lake is the current database, so `raw.blocks` works; `select`,
  `create`, `alter`, `call` and S3 reads work. Studio **rejects** statements that start with `FROM`, `SET`
  or `BEGIN` (so: write `select * from …`; no session settings; **no explicit transactions and no commit
  messages**). **`MERGE` is rejected too** (tested), along with `ATTACH`, `USE` and `LOAD`. Notebook SQL
  cells go through the same filter and also refuse several statements in one cell, so there is no place in
  Studio 1.7.6 to run `MERGE` or a transaction by hand. Details: `studio-notes.md`.
- **One writer at a time (tested):** once Studio has opened the lake (Data Lake page, SQL Editor or a
  notebook) it keeps a lock on the catalog file until Studio is quit. dbt then fails with "Could not set
  lock on file … Conflicting lock is held in Rosetta DBT Studio". After a restart of Studio, as long as the
  lake has not been opened, dbt runs; Studio then shows dbt's tables, views and snapshots.
- **dbt covers what the SQL Editor cannot (tested):** `incremental_strategy: merge` runs a real
  `MERGE INTO` on the lake, and a `post_hook` with `call eth_lake.set_commit_message(…)` puts an author and
  a message on the dbt snapshot.
- **dbt on the lake (tested):** dbt's DuckDB 1.5.6 reads and writes a lake created by Studio's 1.5.2 with
  no migration; a view and an incremental model build. The catalog stores the data folder's absolute path.
- **Data (downloaded):** 667,086 blocks over 93 days (126 MB) and 12,695,803 transactions over 7 days
  (886 MB) without the `input` column.

From the source and Project 1:

- Data Lake screens exist: instance list, a create wizard (instance details, catalog configuration, storage
  configuration, runtime options, review), tables, table details with a data-files tab, snapshot history,
  import from storage or URL, row update and delete. Screenshots are in
  `presentations/ducklake-ui-and-sql-editor-presenation/`.
- Catalog types in the code: `duckdb`, `sqlite`, `postgresql`.
- The SQL Editor has DuckLake completions and runs one statement per gutter arrow, each on a fresh connection
  (Project 1 finding). **Phase 0 must check** how the SQL Editor attaches a Studio DuckLake instance, and
  whether session settings (`USE`, `SET`, `BEGIN … COMMIT`) survive between statements.
- Preview and Query Results show TIMESTAMP columns as `[object Object]` in 1.7.6 (Project 1 finding). Demos
  cast timestamps to text (`strftime`) where they must be read on screen.
- dbt-duckdb 1.11.1 has DuckLake support (`is_ducklake`, table workarounds only before DuckDB 1.5.3).

## 3. What the viewer builds

```text
ethereum_lake/                         Studio project = git repo root
├── README.md
├── .gitignore                         lake/ (catalog + data files), target/, logs/
├── sql/                               one script per hands-on lesson (Modules 2 to 5)
│   ├── 2_2_load_blocks.sql
│   ├── 3_2_daily_merge.sql
│   └── …
├── dbt_project.yml  profiles.yml      Module 6
├── models/
│   ├── sources.yml                    lake.raw.blocks, lake.raw.transactions
│   ├── staging/stg_blocks.sql  stg_transactions.sql
│   └── marts/daily_network_activity.sql  daily_gas.sql  top_senders.sql
└── lake/                              gitignored
    ├── eth_catalog.duckdb             the catalog (a DuckDB file)
    └── data/                          Parquet files written by DuckLake
```

- **Lake name:** `eth_lake`. Schemas: `raw` (loaded tables), `main` (dbt models).
- **Raw tables:** `raw.blocks` (90 days) and `raw.transactions` (7 days, partitioned by day in 4.1).
- **dbt marts:** daily blocks, transactions, gas used and average base fee (`daily_network_activity`); daily
  fee statistics (`daily_gas`); the most active sender addresses (`top_senders`).
- **Code repo:** `Nuri1977/ethereum-ducklake-dbt` (public, created empty before 2.1; name to confirm).
  One commit per hands-on lesson, pushed with Studio's Git tab, straight to `main`. Git basics are assumed,
  with the same help links as Project 1.

## 4. Course map (31 lessons)

| # | Lesson | Type | Length | DuckLake docs covered |
|---|---|---|---|---|
| 0 | Welcome: an Ethereum lake on your laptop | slides | 3:00 | |
| 0.1 | Install Rosetta DBT Studio from rosettadb.io | browser + app | 4:00 | |
| 1.1 | Warehouse, data lake, lakehouse | slides | 4:00 | |
| 1.2 | Parquet: why lakes use column files | slides + SQL | 4:00 | |
| 1.3 | Table formats and catalogs: Iceberg, Delta, DuckLake | slides | 4:30 | Overview, FAQ |
| 1.4 | How DuckLake works: a SQL catalog plus Parquet files | slides | 4:00 | Specification intro |
| 1.5 | The Ethereum data: blocks, transactions, gas | slides + browser | 3:30 | |
| 1.6 | Under the hood: DuckDB's Node package and the DuckLake extension in Studio | slides + app | 4:30 | Installation, Connecting |
| 2.1 | Create a DuckLake in Studio | app | 4:00 | Installation, Connecting, Choosing a Catalog Database, Choosing Storage, Paths |
| 2.2 | Load 90 days of blocks from S3 | app | 4:30 | Introduction |
| 2.3 | Look inside: data files and tables | app | 4:00 | List Files |
| 2.4 | Snapshots: every change is a version | app | 3:30 | Snapshots |
| 2.5 | Time travel | app | 3:30 | Time Travel |
| 3.1 | Insert, update, delete, and delete files | app | 4:00 | Deletion Vectors, Rewrite Files with Deletes |
| 3.2 | Daily loads with MERGE | app | 4:30 | Upserting |
| 3.3 | Schema evolution | app | 4:00 | Schema Evolution, Constraints, Comments |
| 3.4 | The data change feed | app | 3:30 | Data Change Feed, Row Lineage |
| 3.5 | Transactions and conflicts | app + slides | 4:00 | Transactions, Conflict Resolution |
| 4.1 | Partitioning | app | 4:30 | Partitioning |
| 4.2 | Sorted tables and file pruning | app | 4:00 | Sorted Tables, Configuration |
| 4.3 | Data inlining for small writes | app | 3:30 | Data Inlining |
| 4.4 | Maintenance | app | 4:30 | Recommended Maintenance, Merge Files, Expire Snapshots, Cleanup of Files, Checkpoint |
| 4.5 | Listing files and adding existing Parquet files | app | 3:30 | List Files, Adding Files |
| 5.1 | Inside the catalog: snapshots, schemas, tables, columns | app | 4:00 | Specification tables |
| 5.2 | Inside the catalog: files, statistics, partitions | app | 4:00 | Specification tables |
| 5.3 | Read the lake by hand | app | 4:00 | Specification queries |
| 6.1 | Connect a dbt project to the lake | app | 4:00 | |
| 6.2 | Staging models for blocks and transactions | app | 4:00 | Views |
| 6.3 | Marts, built incrementally | app | 4:30 | |
| 6.4 | Tests and docs on the lake | app | 4:00 | |
| 7.1 | Going further, and recap | slides | 4:30 | Remote data path, Access Control, Backups and Recovery, Encryption, Migrations, Unsupported Features |

## 5. Lessons in detail

Each lesson lists its goal, the slide content, the demo steps with the real SQL, the Studio feature that
carries it, and the commit. SQL is from the DuckLake 1.0 docs, adapted to `eth_lake`; every statement is run
in the rehearsal before any recording (Phase 2).

### Module 0 · Welcome

**0 Welcome: an Ethereum lake on your laptop**
- *Goal:* show the end result and the route.
- *Slides:* (1) the promise: a real data lake, with versions and time travel, on a laptop; (2) the picture:
  S3 Parquet → DuckLake (catalog + files) → dbt models → answers; (3) the data in numbers; (4) the tools:
  Rosetta DBT Studio, DuckDB, DuckLake, dbt; (5) the course map; (6) what you need: Studio installed
  (link to Project 1, Lesson 1.1), about 3 GB of disk, an internet connection.

**0.1 Install Rosetta DBT Studio from rosettadb.io**
- *Goal:* a viewer who has never seen Studio gets it installed, starting from the website, not from GitHub.
- *Browser:* `rosettadb.io` → the Download page (`rosettadb.io/download-dbtstudio.html`, title "Download
  Rosetta DBT Studio", sections Windows, Linux, macOS) → pick the build for this computer (Intel or Apple
  silicon on a Mac) → the download starts.
- *Slides + app:* open the `.dmg`, drag to Applications, first launch; the setup window: dbt 1.x, the
  version, **dbt-duckdb** as the adapter, Install, Finish. The status bar shows dbt, Python and DuckDB
  versions.
- *Reuse:* the DMG slides and the first-run setup recording from Project 1, Lesson 1.1, re-rendered in the
  white theme; only the website part is new. Windows and Linux get one slide each with the file to pick.
- *Check when recording:* the download page's buttons and file names (they change with each release), and
  that the site does not block the recording browser.

### Module 1 · Data lakes explained (slides)

**1.1 Warehouse, data lake, lakehouse**
- *Goal:* explain why lakes exist and what a lakehouse adds.
- *Slides:* (1) a warehouse: storage and compute in one box, loads through one door; (2) a data lake: files
  on cheap storage, any engine can read them; (3) what plain files lack: no transactions, no schema history,
  slow listing, no safe updates; (4) the lakehouse: a table format puts tables back on top of files;
  (5) one-line definitions of lake, table format, catalog and engine, used through the course.

**1.2 Parquet: why lakes use column files**
- *Goal:* make "a Parquet file" concrete.
- *Slides:* row files vs column files; row groups; min and max statistics per column; compression.
- *Demo (SQL Editor, no lake yet):* read one day of blocks straight from S3 and look at the file's own
  metadata.

```sql
select count(*) from read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-10-01/*.parquet');
select * from parquet_metadata('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-10-01/*.parquet');
```

- *Point to land:* an engine can skip a file or a row group by reading only its statistics. DuckLake keeps
  those statistics in its catalog (seen again in 4.2 and 5.2).

**1.3 Table formats and catalogs: Iceberg, Delta, DuckLake**
- *Goal:* place DuckLake next to the formats the viewer has heard of.
- *Slides:* (1) what a table format must track: which files, which schema, which version; (2) Iceberg:
  metadata files and manifest lists in the bucket, plus a catalog service that points at the current one;
  (3) Delta: a transaction log of JSON and checkpoint files in the bucket; (4) the shared cost: many small
  metadata files, several round trips per query, a catalog to run anyway; (5) DuckLake's idea: since a
  catalog database is needed anyway, put all metadata in it as plain SQL tables; (6) a fair comparison
  table: metadata location, catalog, engines today, maturity. Each row is checked against the three
  projects' docs when the slide is written, with the date on the slide.

**1.4 How DuckLake works**
- *Goal:* give the mental model for the whole course.
- *Slides:* (1) two parts: a catalog database (DuckDB file, SQLite, PostgreSQL or MySQL) and a data path
  with Parquet files; (2) a write, step by step: write Parquet files, then one database transaction that
  records them and creates a snapshot; (3) a read: ask the catalog which files, skip by statistics, read
  Parquet; (4) what follows from it: ACID across tables, cheap snapshots, time travel, small changes
  without small files; (5) who can read it: DuckDB today through the `ducklake` extension, and any SQL
  client can read the catalog tables.

**1.5 The Ethereum data**
- *Goal:* enough domain knowledge to read the tables.
- *Slides:* a block every 12 seconds; a block holds transactions; gas, gas price, base fee; wei and ether
  (1 ether = 10^18 wei); addresses and hashes are hex text.
- *Browser:* the bucket's public listing page for one day; the two tables and their columns (section 2.2).
- *Point to land:* what we load (blocks for 90 days, transactions for 7) and why not everything (sizes).

**1.6 Under the hood: DuckDB's Node package and the DuckLake extension in Studio**
- *Goal:* explain what actually runs when Studio shows a lake, so nothing in Module 2 feels like magic.
- *Slides:*
  1. Studio is an Electron app: a window (the renderer) and a Node.js process (the main process). The
     window never touches the database; it sends a request to the main process.
  2. The main process uses **`@duckdb/node-api`**, DuckDB's official Node.js package (Studio 1.7.6 ships
     `1.5.2-r.1`; the status bar shows it). DuckDB runs **inside** Studio: no server, no install.
  3. The three calls, as real code from Studio's services, shortened:
     `DuckDBInstance.create(':memory:')` → `instance.connect()` → `connection.run(sql)`.
  4. DuckLake is a DuckDB **extension**. Studio runs `INSTALL ducklake; LOAD ducklake;` on the connection
     (and `httpfs` and the catalog's own extension when needed), then
     `ATTACH 'ducklake:<catalog file>' AS "<instance name>" (DATA_PATH '<folder>', AUTOMATIC_MIGRATION …)`.
     When the instance is closed it runs `DETACH`.
  5. One adapter per catalog type (DuckDB, SQLite, PostgreSQL in the code; the 1.7.6 wizard offers DuckDB,
     the others are marked "Soon").
  6. What this means for the viewer: everything the Data Lake screens do is SQL you can also type in the
     SQL Editor; and dbt uses its **own** DuckDB (the Python package inside dbt-duckdb), a second engine
     reading the same lake.
- *App:* Settings ▸ DuckDB (the version screen); the status bar's DuckDB version; then in the SQL Editor
  on a lake connection:

```sql
select version();
select extension_name, loaded, installed, extension_version
from duckdb_extensions() where extension_name in ('ducklake', 'httpfs', 'parquet');
select database_name, type from duckdb_databases();
```

- *Source for the slides (read only):* `dbt-studio/src/main/services/duckdb.service.ts`,
  `duckLake/extensionManager.service.ts`, `duckLake/adapters/base.adapter.ts`. Code on slides is quoted
  from the pinned 1.7.6 release, a few lines at a time.
- *Risk to state on a slide:* Studio's DuckDB (1.5.2) and dbt's DuckDB (1.5.6 in the pinned runtime) are
  different versions. Phase 0 checks that both read and write the same catalog without a format migration.

### Module 2 · Your first lake in Studio

**2.1 Create a DuckLake in Studio**
- *Goal:* a working, empty lake.
- *Demo:* Studio → Data Lake → new DuckLake instance: name `eth_lake`, storage local with the absolute path of `lake/data`, catalog
  type DuckDB with the file `lake/eth_catalog.duckdb`, runtime options left as they are, review, Create
  Instance. Then the SQL the
  wizard stands for:

```sql
INSTALL ducklake;
ATTACH 'ducklake:lake/eth_catalog.duckdb' AS eth_lake (DATA_PATH 'lake/data/');
USE eth_lake;
```

- *Slide:* the other catalog choices (SQLite, PostgreSQL, MySQL) and when a single-file DuckDB catalog is
  enough: one writer process at a time.
- *Also:* create the Studio project `ethereum_lake`, the `.gitignore`, the README, the empty public repo,
  first commit and push.
- *Commit:* "Create the ethereum_lake project".

**2.2 Load 90 days of blocks from S3**
- *Goal:* the first table, loaded from the public bucket.
- *Demo:* turn inlining off so files are visible (explained in 4.3), create the schema, load.

```sql
CALL eth_lake.set_option('data_inlining_row_limit', 0);
CREATE SCHEMA eth_lake.raw;
CREATE TABLE eth_lake.raw.blocks AS
SELECT * EXCLUDE (logs_bloom, last_modified)
SELECT * FROM read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-08-*/*.parquet');
```

  Then the second and third month as two `INSERT INTO … SELECT` statements, so the table has three
  snapshots and three sets of files (used in 2.4, 2.5 and 4.4).
- *Studio:* also show Data Lake → Import data from storage/URL for one day, then the table in the tables
  list with its row count.
- *Check:* `select date, count(*) from eth_lake.raw.blocks group by all order by 1` in the SQL Editor.
- *Commit:* "Load three months of blocks".

**2.3 Look inside: data files and tables**
- *Goal:* show that the lake is ordinary files plus a catalog.
- *Demo:* Studio's table details → data files tab; then the same in SQL.

```sql
SELECT * FROM ducklake_list_files('eth_lake', 'blocks', schema => 'raw');
SELECT * FROM glob('lake/data/**/*');
SELECT * FROM 'lake/data/**/*.parquet' LIMIT 10;
```

- *Point to land:* the Parquet files are readable by any tool, but only the catalog knows which files make
  up the table right now.

**2.4 Snapshots: every change is a version**
- *Goal:* snapshots as the unit of change.
- *Demo:* Studio's snapshot history for `eth_lake`; then SQL.

```sql
SELECT * FROM eth_lake.snapshots();
SELECT * FROM eth_lake.current_snapshot();
BEGIN;
INSERT INTO eth_lake.raw.blocks SELECT * EXCLUDE (logs_bloom, last_modified)
  FROM read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-11-01/*.parquet');
CALL eth_lake.set_commit_message('Nuri', 'Load blocks for 1 Nov');
COMMIT;
```

- *Phase 0 result:* Studio rejects `BEGIN` in the SQL Editor and in notebook cells, so the transaction and
  the commit message cannot run by hand. In this lesson the insert alone runs in the SQL Editor and the
  `BEGIN … COMMIT` block with the commit message is a slide. The commit message is shown **live in 6.3**,
  where a dbt `post_hook` sets it.
- *Commit:* "Add a commit message to a load".

**2.5 Time travel**
- *Goal:* query the past.
- *Demo:* row counts at three versions, then by time, then attach the lake at a version.

```sql
SELECT count(*) FROM eth_lake.raw.blocks AT (VERSION => 2);
SELECT count(*) FROM eth_lake.raw.blocks AT (TIMESTAMP => now() - INTERVAL '10 minutes');
ATTACH 'ducklake:lake/eth_catalog.duckdb' AS eth_then (SNAPSHOT_VERSION 2);
```

- *Slide:* what time travel costs (old files stay until snapshots are expired; see 4.4).

### Module 3 · Changing data

**3.1 Insert, update, delete, and delete files**
- *Goal:* show that changes never rewrite existing Parquet files.
- *Demo:* a small working copy, so the result is easy to read.

```sql
CREATE TABLE eth_lake.raw.blocks_day AS
  SELECT * FROM eth_lake.raw.blocks WHERE date = DATE '2026-10-01';
DELETE FROM eth_lake.raw.blocks_day WHERE transaction_count = 0;
UPDATE eth_lake.raw.blocks_day SET miner = lower(miner);
SELECT * FROM ducklake_list_files('eth_lake', 'blocks_day', schema => 'raw');
SELECT * FROM 'lake/data/**/ducklake-*-delete.parquet';
```

- *Slides:* a delete file lists the row positions to skip; an update is a delete plus an insert; deletion
  vectors as the compact alternative (`ALTER TABLE … SET (write_deletion_vectors = true)`).
- *Studio:* the table's row update and delete screens do the same thing; show the new snapshot they create.
- *Commit:* "Update and delete in the lake".

**3.2 Daily loads with MERGE**
- *Goal:* an idempotent daily load.
- *Demo:* load a day twice without duplicates.

```sql
MERGE INTO eth_lake.raw.blocks AS t
USING (
  SELECT * EXCLUDE (logs_bloom, last_modified)
  FROM read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-11-02/*.parquet')
) AS s
ON (t.number = s.number)
WHEN NOT MATCHED THEN INSERT;
```

  Run it again: zero rows inserted.
- *Phase 0 result:* Studio rejects `MERGE` in the SQL Editor and in notebook cells. So this lesson shows the
  `MERGE` above on a slide and runs the same idempotent load live as an insert that skips existing blocks:

```sql
INSERT INTO raw.blocks
SELECT s.* FROM read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-11-02/*.parquet') AS s
WHERE NOT EXISTS (SELECT 1 FROM raw.blocks AS t WHERE t.number = s.number);
```

  A real `MERGE INTO` runs **live in 6.3** through dbt's `merge` incremental strategy (tested).
- *Slide:* the docs' limit: one UPDATE or DELETE action per MERGE.
- *Commit:* "Daily load with MERGE".

**3.3 Schema evolution**
- *Goal:* change a table's shape without rewriting files.
- *Demo:*

```sql
ALTER TABLE eth_lake.raw.blocks ADD COLUMN gas_used_pct DOUBLE;
UPDATE eth_lake.raw.blocks SET gas_used_pct = round(100.0 * gas_used / gas_limit, 2) WHERE date = DATE '2026-11-02';
ALTER TABLE eth_lake.raw.blocks RENAME miner TO fee_recipient;
ALTER TABLE eth_lake.raw.blocks ALTER size SET TYPE BIGINT;
ALTER TABLE eth_lake.raw.blocks ALTER number SET NOT NULL;
SELECT miner FROM eth_lake.raw.blocks AT (VERSION => 3) LIMIT 5;
```

- *Point to land:* old files are untouched; the catalog maps old column ids to new names, and time travel
  still sees the old schema.
- *Commit:* "Evolve the blocks schema".

**3.4 The data change feed**
- *Goal:* ask "what changed between two versions".
- *Demo:*

```sql
SELECT * FROM eth_lake.table_changes('blocks_day', 2, 4) ORDER BY snapshot_id;
SELECT * FROM eth_lake.table_insertions('blocks_day', 2, 2);
SELECT * FROM eth_lake.table_deletions('blocks_day', 3, 3);
```

  (schema-qualified form to confirm in rehearsal: `ducklake_table_changes('eth_lake', 'raw', 'blocks_day', 2, 4)`).
- *Slides:* change types (insert, delete, update pre-image and post-image); row ids make this possible (row
  lineage); what it is for: incremental downstream loads.

**3.5 Transactions and conflicts**
- *Goal:* ACID across tables, and what happens with two writers.
- *Demo:* one transaction that changes two tables and rolls back; then the same committed, creating one
  snapshot for both.

```sql
BEGIN TRANSACTION;
DELETE FROM eth_lake.raw.blocks_day WHERE number % 2 = 0;
CREATE TABLE eth_lake.raw.scratch AS SELECT 1 AS x;
ROLLBACK;
```

- *Slides:* optimistic concurrency: two writers, the second commit is checked against the first; which
  pairs conflict (same table deletes) and which do not (appends); retries (`ducklake_max_retry_count`).
  A real two-writer demo needs a PostgreSQL catalog, so it stays on slides.
- *Phase 0 result:* Studio rejects `BEGIN`, so the rollback demo is a slide too. The one live moment is the
  single-writer lock: with the lake open in Studio, a dbt run from the terminal fails with "Conflicting
  lock is held"; that error is the lesson's proof that a DuckDB catalog file means one client at a time.

### Module 4 · Performance and upkeep

**4.1 Partitioning**
- *Goal:* load the big table the right way.
- *Demo:* create the table partitioned by day, then load 7 days, one insert per day.

```sql
CREATE TABLE eth_lake.raw.transactions (
  hash VARCHAR, block_number BIGINT, block_timestamp TIMESTAMP, transaction_index BIGINT,
  from_address VARCHAR, to_address VARCHAR, value DOUBLE, gas BIGINT, gas_price BIGINT,
  receipt_gas_used BIGINT, receipt_effective_gas_price BIGINT, receipt_status BIGINT,
  transaction_type BIGINT, max_fee_per_gas BIGINT, max_priority_fee_per_gas BIGINT, date DATE
) PARTITIONED BY (date);
INSERT INTO eth_lake.raw.transactions
SELECT hash, block_number, block_timestamp, transaction_index, from_address, to_address, value, gas,
       gas_price, receipt_gas_used, receipt_effective_gas_price, receipt_status, transaction_type,
       max_fee_per_gas, max_priority_fee_per_gas, date
SELECT * FROM read_parquet('s3://aws-public-blockchain/v1.0/eth/transactions/date=2026-10-01/*.parquet');
```

- *Show:* the folder per partition under `lake/data/`; a query for one day with `EXPLAIN ANALYZE` reading
  one partition; `ALTER TABLE … SET PARTITIONED BY (year(block_timestamp), month(block_timestamp))` as the
  way to change it for new data only.
- *Recording note:* each daily insert reads about 840 MB from S3 minus the `input` column. The wait is a
  speeded-up clip with the real time on a card.
- *Commit:* "Load a week of transactions, partitioned by day".

**4.2 Sorted tables and file pruning**
- *Goal:* make statistics useful.
- *Demo:*

```sql
ALTER TABLE eth_lake.raw.transactions SET SORTED BY (block_number ASC);
CALL ducklake_merge_adjacent_files('eth_lake', 'transactions', schema => 'raw');
EXPLAIN ANALYZE SELECT count(*) FROM eth_lake.raw.transactions WHERE block_number BETWEEN 21000000 AND 21000100;
```

  (block numbers replaced by real ones from the loaded week).
- *Slides:* min and max per file and per column; a sorted table has narrow ranges, so most files are
  skipped; `target_file_size` and `parquet_compression` (`CALL eth_lake.set_option(…)`, `FROM eth_lake.options()`).

**4.3 Data inlining for small writes**
- *Goal:* explain the setting turned off in 2.2.
- *Demo:* turn the default back on for one table, insert 5 rows, show that no file appears, then flush.

```sql
CREATE TABLE eth_lake.raw.watchlist (address VARCHAR, label VARCHAR) WITH (data_inlining_row_limit = 100);
INSERT INTO eth_lake.raw.watchlist VALUES ('0x…', 'exchange'), ('0x…', 'bridge');
SELECT * FROM ducklake_list_files('eth_lake', 'watchlist', schema => 'raw');
CALL ducklake_flush_inlined_data('eth_lake', schema_name => 'raw', table_name => 'watchlist');
```

- *Slide:* why it matters: streaming-style small inserts without thousands of tiny files.
- *Commit:* "A small inlined table".

**4.4 Maintenance**
- *Goal:* keep the lake small and fast.
- *Demo:* count files and bytes before and after each step.

```sql
CALL ducklake_merge_adjacent_files('eth_lake');
CALL ducklake_expire_snapshots('eth_lake', dry_run => true, older_than => now() - INTERVAL '1 hour');
CALL ducklake_expire_snapshots('eth_lake', older_than => now() - INTERVAL '1 hour');
CALL ducklake_cleanup_old_files('eth_lake', dry_run => true, cleanup_all => true);
CALL ducklake_cleanup_old_files('eth_lake', cleanup_all => true);
CALL ducklake_rewrite_data_files('eth_lake', 'blocks_day', schema => 'raw');
CHECKPOINT;
```

- *Slides:* the recommended order (merge, expire, clean up) and that `CHECKPOINT` runs them together;
  expiring snapshots ends time travel to them; `ducklake_delete_orphaned_files` for files no snapshot
  knows.
- *Commit:* "Maintenance script".

**4.5 Listing files and adding existing Parquet files**
- *Goal:* register files without copying them.
- *Demo:* download one day of blocks to `lake/landing/`, then add it.

```sql
COPY (SELECT * EXCLUDE (logs_bloom, last_modified) FROM read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-11-03/*.parquet'))
  TO 'lake/landing/blocks_2026-11-03.parquet';
CALL ducklake_add_data_files('eth_lake', 'blocks', 'lake/landing/blocks_2026-11-03.parquet', schema => 'raw');
```

- *Slide:* the file now belongs to the lake: maintenance may delete it. `allow_missing` and
  `ignore_extra_columns` for files with a different shape (relevant here after 3.3 added a column; the
  rehearsal picks the option that is needed).

### Module 5 · Inside the catalog

The catalog is a DuckDB file, so it can be opened like any database. Each lesson opens
`lake/eth_catalog.duckdb` as a second, read-only DuckDB connection in Studio and reads the `ducklake_*`
tables directly. Phase 0 checks that Studio can open it while the lake is attached; if not, the lessons use
`ATTACH 'lake/eth_catalog.duckdb' AS catalog (READ_ONLY)` in the SQL Editor.

**5.1 Snapshots, schemas, tables, columns**
- *Tables:* `ducklake_metadata`, `ducklake_snapshot`, `ducklake_snapshot_changes`, `ducklake_schema`,
  `ducklake_table`, `ducklake_column`, `ducklake_view`, `ducklake_tag`, `ducklake_column_tag`.
- *Demo:* find the commit message from 2.4 in `ducklake_snapshot_changes`; see the renamed column from 3.3
  as two rows in `ducklake_column` with `begin_snapshot` and `end_snapshot`.
- *Point to land:* versioning is two columns, `begin_snapshot` and `end_snapshot`, on every catalog row.

**5.2 Files, statistics, partitions**
- *Tables:* `ducklake_data_file`, `ducklake_delete_file`, `ducklake_file_column_stats`,
  `ducklake_table_stats`, `ducklake_table_column_stats`, `ducklake_partition_info`,
  `ducklake_partition_column`, `ducklake_file_partition_value`, `ducklake_sort_info`,
  `ducklake_sort_expression`, `ducklake_inlined_data_tables`, `ducklake_files_scheduled_for_deletion`.
- *Demo:* the min and max `block_number` per file for `transactions` (the pruning from 4.2, seen as data);
  the partition value per file; the inlined table from 4.3.

**5.3 Read the lake by hand**
- *Goal:* prove there is no magic: answer a query with only the catalog tables and `read_parquet`.
- *Demo (from the specification's Queries page):* current snapshot → schema → table → columns → data files
  valid at that snapshot → read those files.

```sql
SELECT max(snapshot_id) FROM ducklake_snapshot;
SELECT table_id, table_name FROM ducklake_table
WHERE 12 >= begin_snapshot AND (12 < end_snapshot OR end_snapshot IS NULL);
SELECT path FROM ducklake_data_file
WHERE table_id = 1 AND 12 >= begin_snapshot AND (12 < end_snapshot OR end_snapshot IS NULL);
```

  (ids replaced by the real ones in the rehearsal), then `read_parquet([...])` on the listed paths, and the
  same count from `eth_lake.raw.blocks`.
- *Slide:* this is what any future engine has to implement to read DuckLake.

### Module 6 · dbt on DuckLake

**6.1 Connect a dbt project to the lake**
- *Goal:* dbt builds into `eth_lake`.
- *Demo:* in the `ethereum_lake` Studio project, `profiles.yml` attaches the lake and makes it the target
  database; Project ▸ Debug.

```yaml
ethereum_lake:
  target: dev
  outputs:
    dev:
      type: duckdb
      path: lake/dbt_session.duckdb
      attach:
        - path: "ducklake:lake/eth_catalog.duckdb"
          alias: eth_lake
          options: { data_path: lake/data/ }
      database: eth_lake
      schema: main
      threads: 1
```

- *Phase 0 checks:* the exact attach form dbt-duckdb 1.11.1 accepts for DuckLake (path prefix or an
  `is_ducklake` flag), whether relative paths resolve from the project folder inside Studio, and whether
  Studio's connection form can produce this profile or it must be edited by hand.
- *Slide:* `threads: 1` is the safe choice with a single-file catalog (dbt-duckdb issue #748: intermittent __dbt_tmp errors with more threads). The single-process lock is per process, not per thread.
- *Rule for all of Module 6 (tested):* Studio and dbt cannot hold the lake at the same time. Each lesson
  starts with Studio freshly opened, runs dbt **first**, and opens the Data Lake page or the SQL Editor on
  the lake only afterwards. 6.1 says this out loud and shows "Quit Studio, open it again" once. Raw data a
  lesson needs is loaded at the end of the lesson before, never between two dbt runs.
- *Phase 2 check:* that opening the dbt project in Studio (its own connection, Preview, Query Results)
  does not open the lake before the first dbt run.
- *Commit:* "Point dbt at the lake".

**6.2 Staging models**
- *Demo:* `models/sources.yml` (source `raw`: `blocks`, `transactions`); `stg_blocks.sql` (clear names,
  `gas_used / gas_limit`, base fee in gwei); `stg_transactions.sql` (value in ether, fee paid, a success
  flag from `receipt_status`). Both are views. Model ▸ Run, Model ▸ Preview, Model ▸ Compile.
- *Slide:* a view in DuckLake is catalog metadata only (`ducklake_view`): no files.
- *Commit:* "Staging models".

**6.3 Marts, built incrementally**
- *Demo:* `daily_network_activity` (per day: blocks, transactions, gas used, average base fee) as a table;
  `daily_gas` as an **incremental** model on `date`, so a new day adds rows; `top_senders`. Project ▸ Run;
  then load one more day of raw data and run again.
- *Show:* each dbt run is one or more new snapshots in Studio's snapshot history; time travel on a mart
  (`AT (VERSION => …)`) to compare yesterday's numbers.
- *Tested:* the default strategy with `unique_key` and `incremental_strategy: merge` both work on the lake.
  `daily_gas` uses `merge`, so the compiled SQL (Model ▸ Compile, `target/run`) shows a real `MERGE INTO`:
  this is the live MERGE promised in 3.2.
- *Commit message, live:* `post_hook: "call eth_lake.set_commit_message('dbt', 'daily_gas …')"`; afterwards
  the snapshot history shows the author and message (the live part promised in 2.4).
- *Order:* the extra day of raw data is loaded at the end of 6.2; this lesson runs dbt twice, then opens
  the lake.
- *Commit:* "Marts on the lake".

**6.4 Tests and docs on the lake**
- *Demo:* `schema.yml` with descriptions and tests: `unique` + `not_null` on `block_number` and on the
  marts' `date`; `accepted_values` on `receipt_status`; a `relationships` test from transactions to blocks.
  Project ▸ Build; Project ▸ Generate Docs, Serve Docs; the lineage graph from the two raw tables to the
  marts.
- *Slide:* DuckLake does not enforce primary keys or unique constraints (docs: Unsupported Features), so
  dbt tests are how uniqueness is checked.
- *Commit:* "Tests and docs".

### Module 7 · Wrap-up

**7.1 Going further, and recap**
- *Slides:* (1) a shared lake: PostgreSQL catalog + object storage,
  `ATTACH 'ducklake:postgres:dbname=ducklake_catalog host=…' AS lake (DATA_PATH 's3://bucket/path/')`;
  (2) access control: database permissions on the catalog plus bucket policies on the files;
  (3) backups: back up the catalog database, and version the bucket; (4) encryption of data files with keys
  kept in the catalog; (5) migrating a DuckDB database to DuckLake; (6) what DuckLake does not support
  today, from the docs page, with the date; (7) the recap checklist of the whole course; (8) where to go
  next: the docs, the specification, the repo.
- *Tested fact for slide 1:* DuckLake on S3-compatible storage (RustFS) works from DuckDB and dbt with an
  S3 secret that sets the endpoint, SSL off and path-style addressing; Studio 1.7.6's DuckLake wizard
  cannot use it yet. The slide says a follow-up tutorial covers PostgreSQL + cloud S3.

## 6. Slides: the white theme

A new theme, built on the Project 1 slide engine. **Built (11 Nov):** it lives in `slides-theme/` inside this project (the folder name the tooling expects), with `demo.html` showing one slide of each type. Originally planned as `slides-theme-light/`, (`theme.js` and the same
`data-id` / `data-step` contract), so `render_stills.py` and `compose.py` need no changes.

| Token | Value |
|---|---|
| Background | `#ffffff`; hero slides get a very light warm wash (`#fff7f0` to white) |
| Text | `#14171f`; muted `#5b6472`; dim `#8a93a3` |
| Accent | Rosetta orange `#ff7a1a`, darker `#e8620a` for text on white (contrast) |
| Cards | `#f6f7f9` with a `#e3e6ec` border, 20 px radius, soft shadow |
| Code | white card, `#14171f` text, keywords `#2456d6`, strings `#b4530a`, Jinja `#8a5a00`, comments `#8a93a3` |
| Fonts | Inter for text, JetBrains Mono for code (embedded, as in Project 1) |
| Footer | progress bar in orange, the dark logo variant, "Project 2 · Lesson n" |

- **Slide types:** title, statement, two-card compare, three or four cards in a row, flow (boxes and
  arrows), code focus, before/after code, table, recap, closing.
- **New diagram pieces** the course needs: a "catalog + files" pair, a snapshot timeline, a file strip
  (data files and delete files), a partition folder tree, a two-writer conflict timeline.
- **Checks before use:** orange text on white passes contrast at slide sizes (use the darker orange for
  small text); the light logo assets exist in `brand/` or are added; overlay cards on the dark Studio UI
  keep the dark card style.
- The Studio recordings stay in Studio's dark theme. The plan's default is dark app + white slides; a
  light Studio theme is an option Nuri can choose after seeing the first lesson.

## 7. Production

Same pipeline and rules as Project 1 (`presentations/_academy-video-tooling/`, skill `rosetta-academy-video`).

- **Studio:** 1.7.6, isolated learner profile, `ui_zoom: 1.25`, `browser_zoom: 1.5`, 4K frames.
- **Features first:** Data Lake screens, SQL Editor, Model ▸ Preview/Compile, Run History, Git tab. No
  terminal commands unless Studio has no screen for it.
- **Voice:** Kokoro `af_heart`, voice first. New pronunciations: DuckLake, Parquet, Ethereum, wei, gwei,
  ACID, S3, `.ducklake`, MERGE, hex addresses are never read out.
- **Long waits** (S3 loads) are recorded live and squeezed to the narration.
- **Start states:** each hands-on lesson starts from the previous lesson's lake. The lake is not in git, so
  the state recipe rebuilds it by running the `sql/` scripts of the earlier lessons off camera, from a
  local cache of the downloaded Parquet files (no S3 during state builds).
- **Outputs per lesson:** 4K MP4, 1080p copy, captions, thumbnail, slides, `youtube.md`; then the upload
  sheet and one joined full-length video with chapters.

### Tooling work needed

| Item | Why |
|---|---|
| `slides-theme-light/` | the white theme (section 6) |
| Recorder actions for the Data Lake screens | create-instance wizard, table list, table details tabs, snapshot history, import wizard |
| A `lake:` block in state recipes | rebuild the lake from `sql/` scripts and the local file cache |
| A local cache step | download the 90 + 7 days once into `.cache/data/eth/` |
| SQL Editor multi-statement helper | one `sql_run` per line already exists; add "run all lines in order" |
| Seed a lake instance into the Studio profile | lessons after 2.1 start with `eth_lake` already registered but not yet opened (needed for the dbt-first order in Module 6) |
| `explore.cjs` `KEEP_PROFILE=1` (done) | relaunch Studio on the profile of the last run, to test what a restart does |
| Lake start states (done) | `lake:` block in a state's `recipe.yaml`: builds the lake at the learner path from `states/sql/*.sql` and writes Studio's `datalake/instances.json`, so a lesson starts with `eth_lake` registered and not yet opened. Tested with `states/lake-blocks-one-day` |
| Recorder under UI zoom (fixed) | with `ui_zoom: 1.25` raw mouse clicks missed; the recorder now checks where the pointer really is and corrects it |
| `type_text` `replace: true`, recipe `mkdirs:` (done) | replace a field's default value (catalog path in the wizard); folders the learner made by hand |
| Data Lake wizard | needs no special actions: `nav`, `click_at`, `type_text`, `point_at`, `sql_connection`, `sql_run` cover it (Lesson 2.1 pilot) |

## 8. Phases

| Phase | What | Who |
|---|---|---|
| 0 | Prechecks: download and measure the data; verify every open check in sections 2.3, 5 and 6.1 in Studio 1.7.6; create the empty public repo; add it to the push token | Claude + Nuri (repo, token) |
| 1 | Tooling: the white theme, Data Lake recorder actions, lake state recipes | Claude |
| 2 | Rehearsal: run every lesson's SQL and dbt steps end to end on a scratch lake; record the real numbers; fix this plan where reality differs | Claude |
| 3 | Pilot: Lesson 2.1 (app) and 1.4 (slides) as review cuts; Nuri approves the look and the pace | Claude, Nuri reviews |
| 4 | Production in lesson order (each lesson builds on the last push) | Claude |
| 5 | Package: upload sheet, full-length video, README for the repo | Claude |

## 9. Risks and open checks

| Risk | Plan |
|---|---|
| Studio's SQL Editor rejects `FROM`-first statements, `SET` and `BEGIN` (tested) | `select * from …` everywhere; options through `call <lake>.set_option`; `MERGE`, `BEGIN` and multi-statement cells are rejected in notebooks too (tested), so transactions (2.4, 3.5) are slides, 3.2 runs an insert that skips existing rows, and the live `MERGE` and commit message come from dbt in 6.3 |
| Studio locks the catalog file once it has opened the lake; dbt then cannot attach (tested) | Module 6 lessons run dbt first on a freshly opened Studio and look at the lake afterwards; the restart is shown once in 6.1; start states register the lake without opening it |
| How Studio attaches its DuckLake instance in the SQL Editor is unknown | Phase 0 test; if the instance cannot be queried there, the lessons attach the lake by SQL |
| Timestamps show as `[object Object]` in results | cast to text in queries that show times; note it in each lesson's changes |
| Downloading 7 days of transactions is slow or fails | local cache; the video shows one live load and squeezes it |
| Laptop disk and memory with 14 million rows | measured in Phase 0; drop to 3 days of transactions if needed |
| dbt-duckdb incremental models on DuckLake | Phase 2 picks the strategy that works; otherwise `daily_gas` is a plain table and the lesson says so |
| Data inlining default hides files in Module 2 | turned off in 2.2 on camera, explained in 4.3 |
| Docs change after recording (DuckLake is young) | every slide with a product fact carries the check date; `accuracy_notes` per lesson |
| The S3 bucket changes layout | the repo's README gives the date range used; the local cache keeps the course reproducible |
| Comparison slide accuracy (Iceberg, Delta) | each claim checked against that project's own docs when the slide is written |

## 10. Deliverables and folder layout

```text
presentations/nuries-youtube-clones/project-02-ducklake/
├── plan-ducklake-project02.md        this document
├── course.yaml                       Phase 1
├── slides-theme-light/               Phase 1
├── snippets/<lesson>/                the SQL and dbt files, checked in Phase 2
├── states/                           lake start states
├── lesson-<n>-<slug>/                29 folders: lesson.yaml, slides.html, outputs
├── UPLOAD-SHEET.md                   Phase 5
└── full-course/                      Phase 5
```

## 11. Sources

- DuckLake 1.0 docs, `https://ducklake.select/docs/stable/` (pages listed in section 2.1), read 11 Nov 2026.
- AWS public blockchain bucket, `s3://aws-public-blockchain/v1.0/eth/`, listed and sampled 11 Nov 2026.
- Rosetta DBT Studio 1.7.6 source (read only) and the screenshots in
  `presentations/ducklake-ui-and-sql-editor-presenation/`.
- Project 1 findings: `presentations/nuries-youtube-clones/project-01/studio-notes.md`.
