# Data inlining for small writes — voice-over script and beat sheet

Data Lakes with DuckLake in Rosetta DBT Studio · Module 4 · Performance and upkeep · next: Lesson 4.4 · Maintenance

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `lesson-4-2-end`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 2 · Lesson 4.3. Data inlining for small writes.

## s01 · slide — slide `problem`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | Lakes have a classic problem: many small inserts, like a stream of events, make many tiny Parquet files. Tiny files are slow to list and slow to read. | Many small inserts = many tiny Parquet files: slow to list and read. | 28 | 10 |
| b02 @0:13 | DuckLake's answer is data inlining. Small inserts are stored as rows inside the catalog database. Later, they are flushed into one proper Parquet file. | Inlining: small inserts are stored as rows in the catalog; flushed to Parquet later in one go. | 24 | 11 |

## s02 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b03 @0:23 | In the SQL Editor, on eth lake: a small table, a watchlist of addresses with a label. Remember, inlining is off for the whole lake. Turn it on for this one table: up to a hundred rows stay in the catalog. | Left bar → **SQL Editor**<br>Pick the connection **eth_lake**<br>paste: create table raw.watchlist (address varchar, label varchar);
call eth_lake.set_option('data_inlining_row_limit', 100, schema => 'raw', table_name => 'watchlist');
insert into raw.watchlist values ('0x00000000219ab540356cbb839cbe05303d7705fa', 'staking deposit'), ('0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2', 'wrapped ether');
select * from raw.watchlist;
select count(*) as files from ducklake_list_files('eth_lake', 'watchlist', schema => 'raw');
call ducklake_flush_inlined_data('eth_lake', schema_name => 'raw', table_name => 'watchlist');
select count(*) as files from ducklake_list_files('eth_lake', 'watchlist', schema => 'raw');<br>Click the green run arrow next to line 1<br>Click the green run arrow next to line 1<br>Zoom: explorer | 41 | 15 |
| b04 @0:38 | Insert two addresses: the staking deposit contract, and wrapped ether. And read them back, like any table. | Click the green run arrow next to line 1<br>Click the green run arrow next to line 1<br>Zoom: sql-results | 17 | 7 |
| b05 @0:46 | But count the table's data files: zero. The two rows live inside the catalog. | Click the green run arrow next to line 1<br>Zoom: sql-results<br>Card: *raw.watchlist* — **2 rows, 0 files** — inlined in the catalog | 14 | 6 |
| b06 @0:51 | Flush the inlined data, and count again: one Parquet file, with both rows. | Click the green run arrow next to line 1<br>Click the green run arrow next to line 1<br>Zoom: sql-results | 13 | 7 |

## s03 · slide — slide `when`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b07 @0:58 | Inlining is on by default for small inserts. We turned it off in Lesson 2.2 only so that every write would show up as files. | Default limit: small inserts are inlined; we set it to 0 in 2.2 to see files. | 26 | 9 |
| b08 @1:07 | Keep it on for frequent small writes, and flush on a schedule, or let maintenance do it, which is the next lesson. | Good for: frequent small writes. Flush on a schedule, or let maintenance do it (4.4). | 22 | 7 |

## s04 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b09 @1:14 | Save the script as 4 underscore 3 inlining dot sequel, commit, and push. | Left bar → **DBT Studio**<br>Right-click `sql` → **New File** → `4_3_inlining.sql` → **Save**<br>paste: create table raw.watchlist (address varchar, label varchar);
call eth_lake.set_option('data_inlining_row_limit', 100, schema => 'raw', table_name => 'watchlist');
insert into raw.watchlist values ('0x00000000219ab540356cbb839cbe05303d7705fa', 'staking deposit'), ('0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2', 'wrapped ether');
select * from raw.watchlist;
select count(*) as files from ducklake_list_files('eth_lake', 'watchlist', schema => 'raw');
call ducklake_flush_inlined_data('eth_lake', schema_name => 'raw', table_name => 'watchlist');
select count(*) as files from ducklake_list_files('eth_lake', 'watchlist', schema => 'raw');
<br>Click **Save**<br>(check: `sql/4_3_inlining.sql` equals `../snippets/4.3/4_3_inlining.sql`)<br>Close the editor tab for `sql/4_3_inlining.sql`<br>Open the **Git** tab in the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Type the commit message “A small inlined table”<br>Click **Commit**<br>git_push: None<br>Zoom: git-panel | 13 | 27 |

## s05 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b10 @1:41 | To recap: with inlining, small inserts become rows in the catalog, not tiny files, and a flush writes them out as one Parquet file. Next: maintenance, to keep the lake small and fast. | Recap: small inserts inlined into the catalog; no tiny files; flush to Parquet later. | 33 | 13 |

## s06 · closing card (4 s, no voice)

Next · Lesson 4.4 · Maintenance.

**Total: 231 spoken words, 1:58 rendered.**
