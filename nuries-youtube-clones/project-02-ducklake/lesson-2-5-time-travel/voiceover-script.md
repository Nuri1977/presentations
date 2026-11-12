# Time travel — voice-over script and beat sheet

Data Lakes with DuckLake in Rosetta DBT Studio · Module 2 · Your first lake in Studio · next: Lesson 3.1 · Insert, update, delete, and delete files

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `lesson-2-4-end`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 2 · Lesson 2.5. Time travel.

## s01 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | In the SQL Editor, on eth lake, start with the table as it is now: six hundred sixty-seven thousand blocks, three months and one day. | Left bar → **SQL Editor**<br>Pick the connection **eth_lake**<br>paste: select count(*) as blocks from raw.blocks;
select count(*) as blocks from raw.blocks at (version => 2);
select strftime(date, '%Y-%m') as month, count(*) as blocks from raw.blocks at (version => 3) group by all order by 1;
create table raw.blocks_october as select * from raw.blocks at (version => 4) where date >= date '2026-10-01';
select count(*) as blocks from raw.blocks_october;
drop table raw.blocks_october;<br>Click the green run arrow next to line 1<br>Zoom: sql-results | 26 | 12 |
| b02 @0:15 | Now add at, version equals two. That is the table as it was at snapshot two, right after we loaded August: two hundred twenty-two thousand blocks. | Click the green run arrow next to line 1<br>Zoom: sql-results<br>Card: *AT (VERSION => 2)* — **222,412 blocks** — August only | 27 | 10 |
| b03 @0:24 | Any query works on the past. Blocks per month at version three: August and September, no October yet. | Click the green run arrow next to line 1<br>Zoom: sql-results | 18 | 7 |

## s02 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b04 @0:32 | Time travel also helps you recover data. Create a table from the past: October, as it was at version four, before the November day came in. | Click the green run arrow next to line 1<br>sql_wait: None<br>Zoom: explorer | 26 | 10 |
| b05 @0:41 | It holds exactly the October blocks: two hundred twenty-two thousand four hundred fifty-one. We only needed it for the demo, so drop it again. | Click the green run arrow next to line 1<br>Click the green run arrow next to line 1<br>Zoom: sql-results | 26 | 9 |

## s03 · slide — slide `more`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b06 @0:50 | You can also travel by time: at timestamp, for example now minus one day. | By time: AT (TIMESTAMP => now() - INTERVAL '1 day'). | 14 | 6 |
| b07 @0:56 | Or attach the whole lake, read only, as it was at one snapshot. | A whole lake at a version: ATTACH 'ducklake:…' AS eth_then (SNAPSHOT_VERSION 2). | 13 | 5 |
| b08 @1:01 | The cost: as long as an old snapshot exists, its files stay on disk. In Lesson 4.4 we expire old snapshots, and clean up. | The cost: old files stay on disk until old snapshots are expired (Lesson 4.4). | 25 | 9 |

## s04 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b09 @1:10 | Save the queries as 2 underscore 5 time travel dot sequel, commit, and push. | Left bar → **DBT Studio**<br>Right-click `sql` → **New File** → `2_5_time_travel.sql` → **Save**<br>paste: select count(*) as blocks from raw.blocks;
select count(*) as blocks from raw.blocks at (version => 2);
select strftime(date, '%Y-%m') as month, count(*) as blocks from raw.blocks at (version => 3) group by all order by 1;
create table raw.blocks_october as select * from raw.blocks at (version => 4) where date >= date '2026-10-01';
select count(*) as blocks from raw.blocks_october;
drop table raw.blocks_october;
<br>Click **Save**<br>(check: `sql/2_5_time_travel.sql` equals `../snippets/2.5/2_5_time_travel.sql`)<br>Close the editor tab for `sql/2_5_time_travel.sql`<br>Open the **Git** tab in the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Type the commit message “Time travel”<br>Click **Commit**<br>git_push: None<br>Zoom: git-panel | 14 | 27 |

## s05 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b10 @1:37 | To recap: add at version to any table to read the past, in any query. Copy past data back with create table as. That is the end of Module 2. Next, in Module 3, we change data: updates, deletes, and what they do to the files. | Recap: AT (VERSION => n); any query on the past; copy past data with CREATE TABLE AS; by timestamp; costs disk until expired. | 46 | 15 |

## s06 · closing card (4 s, no voice)

Next · Lesson 3.1 · Insert, update, delete.

**Total: 235 spoken words, 1:56 rendered.**
