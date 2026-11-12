# Maintenance — voice-over script and beat sheet

Data Lakes with DuckLake in Rosetta DBT Studio · Module 4 · Performance and upkeep · next: Lesson 4.5 · Adding existing Parquet files

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `lesson-4-3-end`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 2 · Lesson 4.4. Maintenance.

## s01 · slide — slide `why`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | A lake grows untidy. Every load adds files, old files stay around for time travel, and delete files pile up. | Every load adds files; old files stay for time travel; delete files pile up. | 20 | 8 |
| b02 @0:11 | DuckLake's recommended routine has three steps: merge small files, expire old snapshots, and clean up files nobody needs. Checkpoint runs them all together. | The recommended order: merge, expire, clean up. CHECKPOINT runs them together. | 23 | 11 |

## s02 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b03 @0:22 | In the SQL Editor, on eth lake: count the Parquet files on disk. Nineteen. | Left bar → **SQL Editor**<br>Pick the connection **eth_lake**<br>paste: select count(*) as files from glob('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/**/*.parquet');
call ducklake_merge_adjacent_files('eth_lake');
select count(*) as files from glob('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/**/*.parquet');
select snapshot_id, changes from eth_lake.snapshots() where snapshot_id in (6, 7);
call ducklake_expire_snapshots('eth_lake', versions => [6, 7]);
call ducklake_cleanup_old_files('eth_lake', dry_run => true, cleanup_all => true);
call ducklake_cleanup_old_files('eth_lake', cleanup_all => true);
select count(*) as files from glob('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/**/*.parquet');
checkpoint;<br>Click the green run arrow next to line 1<br>Zoom: sql-results | 14 | 12 |
| b04 @0:34 | Merge adjacent files. Studio shows no result rows for this call, but behind it, the four files of the blocks table, the three months and the November days, became one. | Click the green run arrow next to line 1<br>sql_wait: None<br>Zoom: sql-results | 30 | 11 |
| b05 @0:45 | Count again: twenty. One more, not fewer: the new file is written, and the four old ones are still on disk. | Click the green run arrow next to line 1<br>Zoom: sql-results | 21 | 7 |

## s03 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b06 @0:53 | Snapshots six and seven are the October copy we made and dropped in Lesson 2.5. We will never travel back to them. Expire them. Again Studio shows no rows, but they are gone. | Click the green run arrow next to line 1<br>Click the green run arrow next to line 1<br>Zoom: sql-results | 34 | 13 |
| b07 @1:05 | Now clean up old files. First a dry run, which only lists what it would delete: the files of that October copy, and the files the merge replaced. | Click the green run arrow next to line 1<br>Zoom: sql-results | 28 | 10 |
| b08 @1:15 | Run it for real, and count: fourteen files. And time travel still works: the merged file keeps every row's history. | Click the green run arrow next to line 1<br>Click the green run arrow next to line 1<br>Zoom: sql-results<br>Card: *Parquet files on disk* — **19 → 20 → 14** — merge, then expire and clean up | 20 | 8 |
| b09 @1:24 | In practice, you just run checkpoint, now and then. It flushes inlined data, merges, expires and cleans up, following the lake's options. | Click the green run arrow next to line 1<br>sql_wait: None<br>Zoom: sql-results | 22 | 10 |

## s04 · slide — slide `careful`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b10 @1:33 | Be careful with two things. Expiring a snapshot ends time travel to it, for good. And cleanup really deletes files. | Expiring a snapshot ends time travel to it. Cleanup deletes files for good. | 20 | 8 |
| b11 @1:41 | Files that no snapshot ever knew about, for example after a crash in the middle of a write, are removed with delete orphaned files. | Files no snapshot knows (a crash mid-write): ducklake_delete_orphaned_files. | 24 | 9 |

## s05 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b12 @1:49 | Save the script as 4 underscore 4 maintenance dot sequel, commit, and push. | Left bar → **DBT Studio**<br>Right-click `sql` → **New File** → `4_4_maintenance.sql` → **Save**<br>paste: select count(*) as files from glob('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/**/*.parquet');
call ducklake_merge_adjacent_files('eth_lake');
select count(*) as files from glob('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/**/*.parquet');
select snapshot_id, changes from eth_lake.snapshots() where snapshot_id in (6, 7);
call ducklake_expire_snapshots('eth_lake', versions => [6, 7]);
call ducklake_cleanup_old_files('eth_lake', dry_run => true, cleanup_all => true);
call ducklake_cleanup_old_files('eth_lake', cleanup_all => true);
select count(*) as files from glob('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/**/*.parquet');
checkpoint;
<br>Click **Save**<br>(check: `sql/4_4_maintenance.sql` equals `../snippets/4.4/4_4_maintenance.sql`)<br>Close the editor tab for `sql/4_4_maintenance.sql`<br>Open the **Git** tab in the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Type the commit message “Maintenance script”<br>Click **Commit**<br>git_push: None<br>Zoom: git-panel | 13 | 27 |

## s06 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b13 @2:17 | To recap: merge small files, expire snapshots you do not need, clean up, or simply run checkpoint. Next: registering Parquet files that already exist, without copying them. | Recap: merge, expire, clean up; CHECKPOINT does it all; expiring ends time travel. | 27 | 12 |

## s07 · closing card (4 s, no voice)

Next · Lesson 4.5 · Adding existing Parquet files.

**Total: 296 spoken words, 2:33 rendered.**
