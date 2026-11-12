# Daily loads without duplicates — voice-over script and beat sheet

Data Lakes with DuckLake in Rosetta DBT Studio · Module 3 · Changing data · next: Lesson 3.3 · Schema evolution

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `lesson-3-1-end`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 2 · Lesson 3.2. Daily loads without duplicates.

## s01 · slide — slide `problem`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | Real pipelines run every day, and sometimes twice: a retry after an error, or a click too many. A plain insert would load the same day twice. | A daily load that runs twice (a retry, a mistake) doubles the day. | 27 | 10 |
| b02 @0:12 | We want an idempotent load: one you can run again, and nothing changes. | Idempotent: running it again changes nothing. | 13 | 5 |

## s02 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b03 @0:17 | In the SQL Editor, on eth lake: insert the blocks of the second of November, but only those where no block with the same number exists yet. | Left bar → **SQL Editor**<br>Pick the connection **eth_lake**<br>paste: insert into raw.blocks select s.* exclude (logs_bloom, last_modified) from read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-11-02/*.parquet') as s where not exists (select 1 from raw.blocks as t where t.number = s.number);
select date, count(*) as blocks from raw.blocks where date >= date '2026-11-01' group by all order by 1;
select snapshot_id, changes from eth_lake.snapshots() order by 1 desc limit 3;<br>Click the green run arrow next to line 1<br>sql_wait: None<br>Zoom: explorer | 27 | 13 |
| b04 @0:30 | Count by day. Studio 1.7.6 shows a date column as a day number, so read the rows in order: the first and the second of November, seven thousand one hundred seventy-six blocks each. | Click the green run arrow next to line 1<br>Zoom: sql-results | 36 | 14 |
| b05 @0:43 | Now run the load again, as if a job retried. | Click the green run arrow next to line 1<br>sql_wait: None<br>Zoom: explorer | 10 | 4 |
| b06 @0:47 | Count again: still seven thousand one hundred seventy-six. No duplicates. | Click the green run arrow next to line 1<br>Zoom: sql-results<br>Card: *2 November 2026* — **7,176 blocks** — after two runs | 11 | 6 |
| b07 @0:53 | And the snapshots: one new snapshot for the first run. The second run inserted nothing, so it did not even create a snapshot. | Click the green run arrow next to line 1<br>Zoom: sql-results | 23 | 8 |

## s03 · slide — slide `merge`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b08 @1:01 | The general tool is merge into. It matches new rows to existing ones on a key, updates the rows that match, and inserts the rest. DuckLake supports it. | Code: MERGE INTO raw.blocks AS t USING (…) AS s ON t.number = s.number WHEN MATCHED THEN UPDATE … WHEN NOT MATCHED THEN INSERT. | 28 | 10 |
| b09 @1:11 | Studio's SQL Editor does not accept merge, so here we used insert where not exists. In Lesson 6.3, dbt runs a real merge on this lake for us. | Studio's SQL Editor does not accept MERGE; dbt runs a real MERGE on the lake in Lesson 6.3. | 29 | 11 |

## s04 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b10 @1:22 | Save the load as 3 underscore 2 daily load dot sequel, commit, and push. | Left bar → **DBT Studio**<br>Right-click `sql` → **New File** → `3_2_daily_load.sql` → **Save**<br>paste: insert into raw.blocks select s.* exclude (logs_bloom, last_modified) from read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-11-02/*.parquet') as s where not exists (select 1 from raw.blocks as t where t.number = s.number);
select date, count(*) as blocks from raw.blocks where date >= date '2026-11-01' group by all order by 1;
select snapshot_id, changes from eth_lake.snapshots() order by 1 desc limit 3;
<br>Click **Save**<br>(check: `sql/3_2_daily_load.sql` equals `../snippets/3.2/3_2_daily_load.sql`)<br>Close the editor tab for `sql/3_2_daily_load.sql`<br>Open the **Git** tab in the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Type the commit message “Daily load without duplicates”<br>Click **Commit**<br>git_push: None<br>Zoom: git-panel | 14 | 28 |

## s05 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b11 @1:50 | To recap: insert only rows whose key is new, and the load can run twice safely. A change that changes nothing makes no snapshot. And merge does the same, with updates too. Next: changing a table's columns. | Recap: insert only new keys; run twice, nothing changes; no snapshot for an empty change; MERGE for upserts. | 37 | 14 |

## s06 · closing card (4 s, no voice)

Next · Lesson 3.3 · Schema evolution.

**Total: 255 spoken words, 2:08 rendered.**
