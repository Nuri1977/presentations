# Snapshots: every change is a version — voice-over script and beat sheet

Data Lakes with DuckLake in Rosetta DBT Studio · Module 2 · Your first lake in Studio · next: Lesson 2.5 · Time travel

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `lesson-2-3-end`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 2 · Lesson 2.4. Snapshots: every change is a version.

## s01 · slide — slide `what`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | Every change to a DuckLake creates a snapshot: a numbered version of the whole lake. So far we have five: zero to four. | Snapshot timeline 0 to 4: schema main, schema raw, August, September, October. | 23 | 8 |
| b02 @0:11 | A snapshot is not a copy of the data. It is a few rows in the catalog that say which files were valid from that moment on. | A snapshot is a few rows in the catalog, not a copy of the data. | 27 | 8 |

## s02 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b03 @0:19 | In Data Lake, open eth lake, and its History tab. Each row is a snapshot: its number, time, schema version, and what changed. | Left bar → **DataLake**<br>Click **eth_lake**<br>Click **History**<br>Zoom: center-wide | 23 | 10 |

## s03 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b04 @0:29 | In the SQL Editor, the same list comes from eth lake dot snapshots. Changes says, in words, what each snapshot did. | Left bar → **SQL Editor**<br>Pick the connection **eth_lake**<br>paste: select snapshot_id, schema_version, changes from eth_lake.snapshots() order by 1;
select * from eth_lake.current_snapshot();
insert into raw.blocks select * exclude (logs_bloom, last_modified) from read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-11-01/*.parquet');
select snapshot_id, changes from eth_lake.snapshots() order by 1 desc limit 2;<br>Click the green run arrow next to line 1<br>Zoom: sql-results | 21 | 12 |
| b05 @0:41 | Current snapshot tells you where the lake is now: snapshot four. | Click the green run arrow next to line 1<br>Zoom: sql-results | 11 | 4 |
| b06 @0:45 | Now change something. Insert one more day of blocks, the first of November, straight from S3. | Click the green run arrow next to line 1<br>sql_wait: None<br>Zoom: explorer | 16 | 7 |
| b07 @0:52 | And list the newest snapshots again. Snapshot five: inserted into the blocks table. One statement, one snapshot. | Click the green run arrow next to line 1<br>Zoom: sql-results<br>Card: *eth_lake.snapshots()* — **Snapshot 5** — 7,176 blocks of 1 November | 17 | 8 |

## s04 · slide — slide `tx`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b08 @1:00 | You can also group several statements into one snapshot, with a transaction: begin, your changes, commit. Inside it, set commit message adds an author and a message, like a git commit. | Code: BEGIN; INSERT …; CALL eth_lake.set_commit_message('Nuri', 'Load blocks for 1 Nov'); COMMIT; | 31 | 12 |
| b09 @1:12 | Studio's SQL Editor runs one statement at a time, so we cannot type a transaction there. We set a real commit message later, from dbt, in Lesson 6.3. | Studio's SQL Editor runs one statement at a time; we set a commit message live from dbt in Lesson 6.3. | 29 | 11 |

## s05 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b10 @1:23 | Save the queries as 2 underscore 4 snapshots dot sequel, commit, and push. | Left bar → **DBT Studio**<br>Right-click `sql` → **New File** → `2_4_snapshots.sql` → **Save**<br>paste: select snapshot_id, schema_version, changes from eth_lake.snapshots() order by 1;
select * from eth_lake.current_snapshot();
insert into raw.blocks select * exclude (logs_bloom, last_modified) from read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-11-01/*.parquet');
select snapshot_id, changes from eth_lake.snapshots() order by 1 desc limit 2;
<br>Click **Save**<br>(check: `sql/2_4_snapshots.sql` equals `../snippets/2.4/2_4_snapshots.sql`)<br>Close the editor tab for `sql/2_4_snapshots.sql`<br>Open the **Git** tab in the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Type the commit message “Snapshots and one more day”<br>Click **Commit**<br>git_push: None<br>Zoom: git-panel | 13 | 28 |

## s06 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b11 @1:51 | To recap: every change is a snapshot. Studio shows them in History, SQL shows them with snapshots and current snapshot, and a transaction groups changes into one. Next: we use snapshots to travel back in time. | Recap: every change is a snapshot; History tab; snapshots(); current_snapshot(); transactions group changes. | 36 | 14 |

## s07 · closing card (4 s, no voice)

Next · Lesson 2.5 · Time travel.

**Total: 247 spoken words, 2:09 rendered.**
