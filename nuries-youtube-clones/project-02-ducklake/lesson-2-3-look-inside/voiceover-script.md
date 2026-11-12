# Look inside: data files and tables — voice-over script and beat sheet

Data Lakes with DuckLake in Rosetta DBT Studio · Module 2 · Your first lake in Studio · next: Lesson 2.4 · Snapshots: every change is a version

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `lesson-2-2-end`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 2 · Lesson 2.3. Look inside: data files and tables.

## s01 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | Open Data Lake, then eth lake, and click the blocks table. Studio opens the table's own page. | Left bar → **DataLake**<br>Click **eth_lake**<br>Click **blocks**<br>Zoom: center-wide | 17 | 10 |
| b02 @0:13 | The Schema tab lists the columns and their types, as the catalog stores them. | Click **Schema**<br>Zoom: center-wide | 14 | 5 |
| b03 @0:18 | And Data Files: three Parquet files, one per load. August, September, and October, each about seventy megabytes, with its row count and the snapshot that added it. | Click **Data Files**<br>Zoom: center-wide<br>Card: *raw.blocks* — **3 data files** — one per month, one per snapshot | 27 | 11 |

## s02 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b04 @0:29 | The same list is one function in SQL. In the SQL Editor, on eth lake, ducklake list files gives each data file of the table, and its size. | Left bar → **SQL Editor**<br>Pick the connection **eth_lake**<br>paste: select data_file, data_file_size_bytes from ducklake_list_files('eth_lake', 'blocks', schema => 'raw');
select file from glob('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/**/*.parquet');
select count(*) as blocks from read_parquet('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/raw/blocks/*.parquet');<br>Click the green run arrow next to line 1<br>Zoom: explorer | 28 | 12 |
| b05 @0:41 | The files are on your disk. Glob lists every Parquet file under the lake's data folder: the same three, in a folder per schema and table. | Click the green run arrow next to line 1<br>Zoom: sql-results | 26 | 9 |
| b06 @0:50 | And they are plain Parquet. Read them directly, without the lake, and you get the same six hundred sixty thousand rows. | Click the green run arrow next to line 1<br>Zoom: sql-results<br>Card: *read_parquet on the files* — **659,896 rows** — the same as raw.blocks | 21 | 8 |

## s03 · slide — slide `point`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b07 @0:58 | So any tool that reads Parquet can read these files. | Any tool can read the files. | 10 | 4 |
| b08 @1:02 | But only the catalog knows which files make up the table right now. After a delete or an update, the folder also holds files that are no longer current, and delete files. Reading the folder directly would give the wrong answer. That is what the catalog is for. | Only the catalog knows which files are the table now: after a delete or an update, reading all files gives the wrong answer. | 48 | 16 |

## s04 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b09 @1:18 | Save the queries as sql, 2 underscore 3 look inside dot sequel, then commit, and push. | Left bar → **DBT Studio**<br>Right-click `sql` → **New File** → `2_3_look_inside.sql` → **Save**<br>paste: select data_file, data_file_size_bytes from ducklake_list_files('eth_lake', 'blocks', schema => 'raw');
select file from glob('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/**/*.parquet');
select count(*) as blocks from read_parquet('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/raw/blocks/*.parquet');
<br>Click **Save**<br>(check: `sql/2_3_look_inside.sql` equals `../snippets/2.3/2_3_look_inside.sql`)<br>Close the editor tab for `sql/2_3_look_inside.sql`<br>Open the **Git** tab in the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Type the commit message “Look inside the lake”<br>Click **Commit**<br>git_push: None<br>Zoom: git-panel | 16 | 28 |

## s05 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b10 @1:46 | To recap: Studio's table page shows the schema and the data files. In SQL, ducklake list files gives the same list, and the files are plain Parquet on disk. But the catalog decides which files are the table. Next: snapshots. | Recap: the table page (Schema, Data Files); ducklake_list_files; glob; read_parquet; the catalog decides. | 40 | 15 |

## s06 · closing card (4 s, no voice)

Next · Lesson 2.4 · Snapshots.

**Total: 247 spoken words, 2:05 rendered.**
