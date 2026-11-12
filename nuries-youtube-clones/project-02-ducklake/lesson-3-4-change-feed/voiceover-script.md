# The data change feed — voice-over script and beat sheet

Data Lakes with DuckLake in Rosetta DBT Studio · Module 3 · Changing data · next: Lesson 3.5 · Transactions and conflicts

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `lesson-3-3-end`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 2 · Lesson 3.4. The data change feed.

## s01 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | Remember Lesson 3.1? We deleted seven rows of blocks day at snapshot nine, and updated seventy-two at snapshot ten. Ask the lake what changed between those two snapshots. | Left bar → **SQL Editor**<br>Pick the connection **eth_lake**<br>paste: select snapshot_id, change_type, count(*) as row_count from ducklake_table_changes('eth_lake', 'raw', 'blocks_day', 9, 10) group by all order by 1, 2;
select snapshot_id, change_type, number, extra_data from ducklake_table_changes('eth_lake', 'raw', 'blocks_day', 10, 10) order by number, change_type limit 4;
select count(*) as inserted from ducklake_table_insertions('eth_lake', 'raw', 'blocks_day', 8, 8);
select count(*) as deleted from ducklake_table_deletions('eth_lake', 'raw', 'blocks_day', 9, 9);<br>Zoom: explorer | 30 | 12 |
| b02 @0:14 | Ducklake table changes, for schema raw, table blocks day, from nine to ten. Grouped by type, Studio's DuckDB, version 1.5.2, shows the update as a delete plus an insert: seventy-nine deletes, and seventy-two inserts at ten. | Click the green run arrow next to line 1<br>Zoom: sql-results<br>Card: *DuckDB 1.5.2 in Studio* — **79 deletes · 72 inserts** — DuckDB 1.5.6: 7 deletes, 72 update pre- and post-images | 40 | 17 |
| b03 @0:31 | Look at the rows: each updated block appears twice, the old value in lower case, deleted, and the new value in upper case, inserted. Newer DuckDB, like the 1.5.6 inside dbt, labels these as update pre-image and post-image, and puts both at snapshot ten. Change feeds are young: check them on your version. | Click the green run arrow next to line 1<br>Zoom: sql-results | 57 | 22 |
| b04 @0:53 | And two shortcuts: table insertions, seven thousand one hundred seventy-six rows at snapshot eight, and table deletions, seven at snapshot nine. | Click the green run arrow next to line 1<br>Click the green run arrow next to line 1<br>Zoom: sql-results | 22 | 11 |

## s02 · slide — slide `why`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b05 @1:03 | Four change types: insert, delete, and for updates, the pre-image and the post-image. | Change types: insert, delete, update_preimage, update_postimage. | 15 | 6 |
| b06 @1:09 | This works because every row in a DuckLake has a stable row id, kept across updates. That is called row lineage. | Row lineage: every row has a stable row id, so the lake can follow it across snapshots. | 21 | 8 |
| b07 @1:17 | What is it for? Downstream jobs that only process what changed since their last run, instead of everything. | Use: incremental loads downstream: process only what changed since last time. | 18 | 7 |

## s03 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b08 @1:25 | Save the queries as 3 underscore 4 change feed dot sequel, commit, and push. | Left bar → **DBT Studio**<br>Right-click `sql` → **New File** → `3_4_change_feed.sql` → **Save**<br>paste: select snapshot_id, change_type, count(*) as row_count from ducklake_table_changes('eth_lake', 'raw', 'blocks_day', 9, 10) group by all order by 1, 2;
select snapshot_id, change_type, number, extra_data from ducklake_table_changes('eth_lake', 'raw', 'blocks_day', 10, 10) order by number, change_type limit 4;
select count(*) as inserted from ducklake_table_insertions('eth_lake', 'raw', 'blocks_day', 8, 8);
select count(*) as deleted from ducklake_table_deletions('eth_lake', 'raw', 'blocks_day', 9, 9);
<br>Click **Save**<br>(check: `sql/3_4_change_feed.sql` equals `../snippets/3.4/3_4_change_feed.sql`)<br>Close the editor tab for `sql/3_4_change_feed.sql`<br>Open the **Git** tab in the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Type the commit message “The data change feed”<br>Click **Commit**<br>git_push: None<br>Zoom: git-panel | 14 | 28 |

## s04 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b09 @1:52 | To recap: ducklake table changes tells you every row that changed between two snapshots, with before and after values. Next: transactions, and what happens with two writers. | Recap: ducklake_table_changes between two snapshots; insertions and deletions; row ids; incremental work. | 27 | 12 |

## s05 · closing card (4 s, no voice)

Next · Lesson 3.5 · Transactions and conflicts.

**Total: 244 spoken words, 2:09 rendered.**
