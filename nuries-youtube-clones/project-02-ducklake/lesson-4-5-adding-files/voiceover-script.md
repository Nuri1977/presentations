# Adding existing Parquet files — voice-over script and beat sheet

Data Lakes with DuckLake in Rosetta DBT Studio · Module 4 · Performance and upkeep · next: Lesson 5.1 · Inside the catalog: snapshots, schemas, tables, columns

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `lesson-4-4-end`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 2 · Lesson 4.5. Adding existing Parquet files.

## s01 · slide — slide `why`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | Sometimes the Parquet files already exist: another tool wrote them, or you are moving an old data lake. Instead of reading and writing them again, you can register them in the catalog. | Files already exist (another tool wrote them, a migration): register instead of copy. | 32 | 12 |

## s02 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b02 @0:14 | In the project, inside the lake folder, make a folder called landing. Git ignores everything under lake. | Left bar → **DBT Studio**<br>Right-click `lake` → **New Folder** → `landing` → **Save**<br>Zoom: explorer | 17 | 11 |
| b03 @0:25 | In the SQL Editor, on eth lake: copy one day of blocks from S3, the third of November, into a Parquet file in landing. We give it the table's current shape: fee recipient instead of miner, and gas used percent. | Left bar → **SQL Editor**<br>Pick the connection **eth_lake**<br>paste: copy (select * exclude (logs_bloom, last_modified, miner), miner as fee_recipient, round(100.0 * gas_used / gas_limit, 2) as gas_used_pct from read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-11-03/*.parquet')) to '/Users/Shared/academy/learner/projects/ethereum_lake/lake/landing/blocks_2026-11-03.parquet';
create temp table added_files as select * from ducklake_add_data_files('eth_lake', 'blocks', '/Users/Shared/academy/learner/projects/ethereum_lake/lake/landing/blocks_2026-11-03.parquet', schema => 'raw');
select strftime(date, '%Y-%m-%d') as day, count(*) as blocks from raw.blocks where date >= date '2026-11-01' group by all order by 1;
select data_file from ducklake_list_files('eth_lake', 'blocks', schema => 'raw');<br>Click the green run arrow next to line 1<br>sql_wait: None<br>Zoom: explorer | 40 | 14 |

## s03 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b04 @0:39 | Now ducklake add data files: the lake, the table, the file, and the schema. Nothing is copied: the catalog just records the file. One Studio detail: the result pane runs a statement again to show its rows, which would register the file twice. So we wrap the call in create temp table, which runs once. | Click the green run arrow next to line 1<br>sql_wait: None<br>Zoom: explorer | 55 | 20 |
| b05 @0:59 | Blocks per day: the third of November is there, seven thousand one hundred eighty-two blocks. | Click the green run arrow next to line 1<br>Zoom: sql-results<br>Card: *raw.blocks* — **3 Nov: 7,182 blocks** — from a file the lake did not write | 16 | 6 |
| b06 @1:05 | And the table's file list now includes the landing file, at its own path. | Click the green run arrow next to line 1<br>Zoom: sql-results | 14 | 5 |

## s04 · slide — slide `careful`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b07 @1:10 | One thing to know: from now on, the file belongs to the lake. Maintenance can merge it, and clean it up. Do not keep using it from outside. | The file now belongs to the lake: maintenance may rewrite or delete it. | 28 | 9 |
| b08 @1:19 | If a file has a different shape, two options help: allow missing for columns the file does not have, and ignore extra columns for columns the table does not have. | Different shape? allow_missing => true (missing columns become NULL), ignore_extra_columns => true. | 30 | 11 |

## s05 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b09 @1:30 | Save the script as 4 underscore 5 add files dot sequel in the sql folder, commit, and push. | Left bar → **DBT Studio**<br>Open `sql/4_5_add_files.sql` in the Explorer<br>paste: {'replace': True, 'text': "copy (select * exclude (logs_bloom, last_modified, miner), miner as fee_recipient, round(100.0 * gas_used / gas_limit, 2) as gas_used_pct from read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-11-03/*.parquet')) to '/Users/Shared/academy/learner/projects/ethereum_lake/lake/landing/blocks_2026-11-03.parquet';\ncreate temp table added_files as select * from ducklake_add_data_files('eth_lake', 'blocks', '/Users/Shared/academy/learner/projects/ethereum_lake/lake/landing/blocks_2026-11-03.parquet', schema => 'raw');\nselect strftime(date, '%Y-%m-%d') as day, count(*) as blocks from raw.blocks where date >= date '2026-11-01' group by all order by 1;\nselect data_file from ducklake_list_files('eth_lake', 'blocks', schema => 'raw');\n"}<br>Click **Save**<br>(check: `sql/4_5_add_files.sql` equals `../snippets/4.5/4_5_add_files.sql`)<br>Close the editor tab for `sql/4_5_add_files.sql`<br>Open the **Git** tab in the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Type the commit message “Register the landing file once”<br>Click **Commit**<br>git_push: None<br>Zoom: git-panel | 18 | 25 |

## s06 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b10 @1:55 | To recap: ducklake add data files registers an existing Parquet file without copying it, and from then on the lake owns it. That ends Module 4. Next, we open the catalog itself. | Recap: COPY to a landing folder; ducklake_add_data_files registers without copying; the file now belongs to the lake. | 32 | 12 |

## s07 · closing card (4 s, no voice)

Next · Lesson 5.1 · Inside the catalog.

**Total: 282 spoken words, 2:11 rendered.**
