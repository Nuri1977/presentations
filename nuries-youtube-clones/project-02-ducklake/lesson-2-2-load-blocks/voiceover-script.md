# Load three months of blocks from S3 — voice-over script and beat sheet

Data Lakes with DuckLake in Rosetta DBT Studio · Module 2 · Your first lake in Studio · next: Lesson 2.3 · Look inside: data files and tables

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `lesson-2-1-end`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 2 · Lesson 2.2. Load three months of blocks from S3.

## s01 · slide — slide `plan`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | The blocks live in the public bucket, one folder per day. We read them straight from S3, with read parquet and a wildcard: one month at a time. | Source: s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-08-01/ … one folder per day. | 28 | 9 |
| b02 @0:12 | Three statements: create the table with August, then insert September, then October. Each one becomes a snapshot of its own, which we use later for time travel. | Three statements: create table with August, insert September, insert October: three snapshots. | 27 | 10 |
| b03 @0:22 | One setting first. DuckLake can keep small writes inside the catalog, which is called data inlining. We turn it off, so every write becomes Parquet files we can look at. Lesson 4.3 explains it. | First: turn data inlining off, so every write makes Parquet files we can see (explained in 4.3). | 35 | 13 |

## s02 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b04 @0:35 | Open the SQL Editor, and pick the eth lake connection. Here is the script: one statement per line. | Left bar → **SQL Editor**<br>Pick the connection **eth_lake**<br>paste: call eth_lake.set_option('data_inlining_row_limit', 0);
create schema raw;
create table raw.blocks as select * exclude (logs_bloom, last_modified) from read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-08-*/*.parquet');
insert into raw.blocks select * exclude (logs_bloom, last_modified) from read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-09-*/*.parquet');
insert into raw.blocks select * exclude (logs_bloom, last_modified) from read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-10-*/*.parquet');
select strftime(date, '%Y-%m') as month, count(*) as blocks from raw.blocks group by all order by 1;<br>Zoom: explorer | 18 | 9 |
| b05 @0:44 | Run the first two lines: inlining off, and a schema called raw, for the data as it comes in. | Click the green run arrow next to line 1<br>Click the green run arrow next to line 1<br>Zoom: explorer | 19 | 6 |
| b06 @0:51 | Line three creates raw dot blocks from every file of August. Star exclude drops two columns we do not need, like the big logs bloom. Run it: Studio downloads the month from S3 and writes it into the lake. | Click the green run arrow next to line 1<br>sql_wait: None<br>Zoom: explorer<br>Card: *Sped up* — **One month from S3** — 31 files, about 220,000 blocks | 39 | 28 |
| b07 @1:19 | Then September, and October, with insert into. | Click the green run arrow next to line 1<br>sql_wait: None<br>Click the green run arrow next to line 1<br>sql_wait: None<br>Zoom: explorer | 7 | 56 |
| b08 @2:16 | Check the result: blocks per month. About two hundred twenty thousand each, almost six hundred sixty thousand in total. | Click the green run arrow next to line 1<br>Zoom: sql-results<br>Card: *raw.blocks* — **659,896 blocks** — August 222,412 · September 215,033 · October 222,451 | 19 | 8 |

## s03 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b09 @2:23 | Now open Data Lake, and the eth lake instance. Refresh. The new table is listed: blocks, in schema raw, with its rows and size. | Left bar → **DataLake**<br>Click **eth_lake**<br>Click **Refresh**<br>Point at **blocks table**<br>Zoom: center-wide | 24 | 11 |
| b10 @2:34 | And History has four new snapshots: the schema, then one for each month. | Click **History**<br>Zoom: center-wide | 13 | 5 |

## s04 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b11 @2:39 | Keep the script in the project. In DBT Studio, add a folder called sql, and in it a file called 2 underscore 2 load blocks dot sequel, with the same statements. Save. | Left bar → **DBT Studio**<br>new_root_folder: sql<br>Right-click `sql` → **New File** → `2_2_load_blocks.sql` → **Save**<br>paste: call eth_lake.set_option('data_inlining_row_limit', 0);
create schema raw;
create table raw.blocks as select * exclude (logs_bloom, last_modified) from read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-08-*/*.parquet');
insert into raw.blocks select * exclude (logs_bloom, last_modified) from read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-09-*/*.parquet');
insert into raw.blocks select * exclude (logs_bloom, last_modified) from read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-10-*/*.parquet');
select strftime(date, '%Y-%m') as month, count(*) as blocks from raw.blocks group by all order by 1;
<br>Click **Save**<br>(check: `sql/2_2_load_blocks.sql` equals `../snippets/2.2/2_2_load_blocks.sql`)<br>Zoom: explorer | 32 | 16 |
| b12 @2:56 | Git tab: stage all, commit with load three months of blocks, and Sync Changes to push. The lake itself stays out of git; the script is enough to rebuild it. | Close the editor tab for `sql/2_2_load_blocks.sql`<br>Open the **Git** tab in the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Type the commit message “Load three months of blocks”<br>Click **Commit**<br>git_push: None<br>Zoom: git-panel | 30 | 18 |

## s05 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b13 @3:13 | To recap: we turned inlining off, made the raw schema, and loaded three months of blocks from S3, one month per statement. That is six hundred sixty thousand blocks, and four new snapshots. Next, we look inside the lake: the files on disk. | Recap: inlining off; schema raw; raw.blocks from S3, one month per statement; 659,896 blocks; four snapshots; script committed. | 43 | 16 |

## s06 · closing card (4 s, no voice)

Next · Lesson 2.3 · Look inside: data files and tables.

**Total: 334 spoken words, 3:33 rendered.**
