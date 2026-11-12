# Statistics and file pruning — voice-over script and beat sheet

Data Lakes with DuckLake in Rosetta DBT Studio · Module 4 · Performance and upkeep · next: Lesson 4.3 · Data inlining for small writes

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `lesson-4-1-end`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 2 · Lesson 4.2. Statistics and file pruning.

## s01 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | In Data Lake, open the transactions table and its Statistics tab. For every column, the catalog keeps the smallest and the largest value. Block numbers go from about twenty-six million ninety-three thousand to twenty-six million one hundred forty-four thousand. | Left bar → **DataLake**<br>Click **eth_lake**<br>Click **transactions**<br>Click **Statistics**<br>Point at **block_number**<br>Zoom: center-wide | 43 | 17 |
| b02 @0:19 | The catalog keeps the same numbers for every single file, so it can rule out files without opening them. | Zoom: center-wide | 19 | 7 |

## s02 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b03 @0:26 | In the SQL Editor, on eth lake: the first and last block number of the week. | Left bar → **SQL Editor**<br>Pick the connection **eth_lake**<br>paste: select min(block_number) as first_block, max(block_number) as last_block from raw.transactions;
explain analyze select count(*) from raw.transactions where block_number between 26100000 and 26100100;
alter table raw.transactions set sorted by (block_number asc);
select option_name, value from eth_lake.options();<br>Click the green run arrow next to line 1<br>Zoom: sql-results | 16 | 12 |
| b04 @0:38 | Now ask for a hundred blocks, with explain analyze in front. It runs the query and returns the plan as text; Studio puts it on one line, so here is the part that matters, from the table scan: total files read, one. Six of the seven files were skipped, using only their statistics. | Click the green run arrow next to line 1<br>Zoom: sql-results<br>Card: *EXPLAIN ANALYZE* — **Total Files Read: 1** — of 7, skipped by min and max | 53 | 19 |

## s03 · slide — slide `sorted`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b05 @0:57 | Pruning works when each file covers a narrow range. Here it does: block numbers grow with time, and each day is its own file. | Narrow ranges per file = good pruning. Here block numbers grow with time, and each day is a file. | 24 | 8 |
| b06 @1:05 | If rows arrive in random order, every file covers almost everything, and nothing can be skipped. | Wide ranges (random order) = every file matches. | 16 | 7 |
| b07 @1:12 | Sorted by tells DuckLake to sort rows when it writes new files, so their ranges stay narrow. | ALTER TABLE … SET SORTED BY (block_number ASC): new files are written sorted. | 17 | 6 |

## s04 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b08 @1:18 | Set it for transactions: sorted by block number. It applies to new writes, and to files that maintenance rewrites later. | Click the green run arrow next to line 1<br>Zoom: explorer | 20 | 8 |
| b09 @1:26 | Other settings live in the lake's options, like the inlining limit we set to zero. Others, like target file size and Parquet compression, are set with set option. | Click the green run arrow next to line 1<br>Zoom: sql-results | 28 | 11 |

## s05 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b10 @1:36 | Save the script as 4 underscore 2 statistics dot sequel, commit, and push. | Left bar → **DBT Studio**<br>Right-click `sql` → **New File** → `4_2_statistics.sql` → **Save**<br>paste: select min(block_number) as first_block, max(block_number) as last_block from raw.transactions;
explain analyze select count(*) from raw.transactions where block_number between 26100000 and 26100100;
alter table raw.transactions set sorted by (block_number asc);
select option_name, value from eth_lake.options();
<br>Click **Save**<br>(check: `sql/4_2_statistics.sql` equals `../snippets/4.2/4_2_statistics.sql`)<br>Close the editor tab for `sql/4_2_statistics.sql`<br>Open the **Git** tab in the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Type the commit message “Statistics and sorted transactions”<br>Click **Commit**<br>git_push: None<br>Zoom: git-panel | 13 | 28 |

## s06 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b11 @2:05 | To recap: the catalog keeps min and max for every column of every file, so queries skip files without opening them. Sorted by keeps ranges narrow. Next: what DuckLake does with very small writes. | Recap: min and max per column per file in the catalog; files skipped without opening them; SORTED BY keeps ranges narrow; options. | 34 | 13 |

## s07 · closing card (4 s, no voice)

Next · Lesson 4.3 · Data inlining.

**Total: 283 spoken words, 2:22 rendered.**
