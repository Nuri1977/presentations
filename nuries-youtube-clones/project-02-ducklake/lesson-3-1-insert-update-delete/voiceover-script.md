# Insert, update, delete, and delete files — voice-over script and beat sheet

Data Lakes with DuckLake in Rosetta DBT Studio · Module 3 · Changing data · next: Lesson 3.2 · Daily loads without duplicates

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `lesson-2-5-end`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 2 · Lesson 3.1. Insert, update, delete, and delete files.

## s01 · slide — slide `rule`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | Parquet files cannot be edited in place. So how does a lake delete or update a row? Let's watch it happen on a small table. | Rule: Parquet files are never edited. | 25 | 8 |

## s02 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b02 @0:11 | In the SQL Editor, on eth lake, make a working copy: the blocks of the first of October, seven thousand one hundred seventy-six rows. | Left bar → **SQL Editor**<br>Pick the connection **eth_lake**<br>paste: create table raw.blocks_day as select * from raw.blocks where date = date '2026-10-01';
select count(*) as blocks, count(*) filter (where transaction_count < 50) as small_blocks from raw.blocks_day;
delete from raw.blocks_day where transaction_count < 50;
update raw.blocks_day set extra_data = upper(extra_data) where number % 100 = 0;
select regexp_extract(data_file, '[^/]+$') as data_file, regexp_extract(delete_file, '[^/]+$') as delete_file from ducklake_list_files('eth_lake', 'blocks_day', schema => 'raw');
select distinct regexp_extract(file_path, '[^/]+$') as data_file, pos from read_parquet('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/raw/blocks_day/*-delete.parquet') order by pos limit 5;<br>Click the green run arrow next to line 1<br>sql_wait: None<br>Zoom: explorer | 25 | 14 |
| b03 @0:24 | Seven of those blocks hold fewer than fifty transactions. | Click the green run arrow next to line 1<br>Zoom: sql-results | 9 | 4 |

## s03 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b04 @0:28 | Delete those seven. Then update every hundredth block of the day, seventy-two of them. Studio just reports that the command ran. | Click the green run arrow next to line 1<br>Click the green run arrow next to line 1<br>Zoom: sql-results | 22 | 8 |
| b05 @0:37 | Now list the table's files. The original data file is still there, untouched, but it now has a delete file. And there is a second data file: the seventy-two updated rows, written fresh. | Click the green run arrow next to line 1<br>Zoom: sql-results<br>Card: *raw.blocks_day* — **2 data files + 1 delete file** — the original file is never rewritten | 34 | 12 |
| b06 @0:49 | The delete file is Parquet too. It lists row positions in the data file: rows the reader must skip. | Click the green run arrow next to line 1<br>Zoom: sql-results | 19 | 7 |

## s04 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b07 @0:56 | In Data Lake, open eth lake, refresh, and click blocks day. Data Files shows the same two files. | Left bar → **DataLake**<br>Click **eth_lake**<br>Click **Refresh**<br>Click **blocks_day**<br>Click **Data Files**<br>Zoom: center-wide | 18 | 17 |

## s05 · slide — slide `how`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b08 @1:12 | So, a delete writes a small delete file, with the positions to skip. | Delete: write a delete file with the positions to skip. | 13 | 5 |
| b09 @1:17 | An update is a delete of the old rows, plus an insert of the new ones in a new data file. | Update: a delete of the old rows plus an insert of the new rows. | 21 | 6 |
| b10 @1:24 | There is also a more compact format, deletion vectors, that you can switch on per table. And over time, maintenance rewrites files with many deletes, in Lesson 4.4. | Option: ALTER TABLE … SET (write_deletion_vectors = true) for a compact format; maintenance rewrites files later (4.4). | 29 | 11 |

## s06 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b11 @1:35 | Save the script as 3 underscore 1 update delete dot sequel, commit, and push. | Left bar → **DBT Studio**<br>Right-click `sql` → **New File** → `3_1_update_delete.sql` → **Save**<br>paste: create table raw.blocks_day as select * from raw.blocks where date = date '2026-10-01';
select count(*) as blocks, count(*) filter (where transaction_count < 50) as small_blocks from raw.blocks_day;
delete from raw.blocks_day where transaction_count < 50;
update raw.blocks_day set extra_data = upper(extra_data) where number % 100 = 0;
select regexp_extract(data_file, '[^/]+$') as data_file, regexp_extract(delete_file, '[^/]+$') as delete_file from ducklake_list_files('eth_lake', 'blocks_day', schema => 'raw');
select distinct regexp_extract(file_path, '[^/]+$') as data_file, pos from read_parquet('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/raw/blocks_day/*-delete.parquet') order by pos limit 5;
<br>Click **Save**<br>(check: `sql/3_1_update_delete.sql` equals `../snippets/3.1/3_1_update_delete.sql`)<br>Close the editor tab for `sql/3_1_update_delete.sql`<br>Open the **Git** tab in the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Type the commit message “Update and delete in the lake”<br>Click **Commit**<br>git_push: None<br>Zoom: git-panel | 14 | 29 |

## s07 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b12 @2:04 | To recap: the lake never edits a Parquet file. A delete adds a delete file, and an update is a delete plus an insert. Next: a daily load that can run twice without making duplicates. | Recap: files are never edited; a delete adds a delete file; an update is delete plus insert. | 35 | 12 |

## s08 · closing card (4 s, no voice)

Next · Lesson 3.2 · Daily loads without duplicates.

**Total: 264 spoken words, 2:20 rendered.**
