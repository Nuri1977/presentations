# Partitioning — voice-over script and beat sheet

Data Lakes with DuckLake in Rosetta DBT Studio · Module 4 · Performance and upkeep · next: Lesson 4.2 · Statistics and file pruning

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `lesson-3-5-end`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 2 · Lesson 4.1. Partitioning.

## s01 · slide — slide `why`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | Transactions are big: almost thirteen million rows for one week. And most questions ask about a day or two. | 12.7 million rows; most questions ask about one day. | 19 | 7 |
| b02 @0:10 | So we partition the table by date. Every day gets its own folder of files, and a query for one day only opens that day's files. | Partition by date: one folder per day; a query for one day only opens that folder. | 26 | 9 |

## s02 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b03 @0:19 | In the SQL Editor, on eth lake: create raw dot transactions, with the columns we need. We leave out input, the largest column. Then set it partitioned by date, before any data goes in. | Left bar → **SQL Editor**<br>Pick the connection **eth_lake**<br>paste: create table raw.transactions (hash varchar, block_number bigint, block_timestamp timestamp, transaction_index bigint, from_address varchar, to_address varchar, value double, gas bigint, gas_price bigint, receipt_gas_used bigint, receipt_effective_gas_price bigint, receipt_status bigint, transaction_type bigint, max_fee_per_gas bigint, max_priority_fee_per_gas bigint, date date);
alter table raw.transactions set partitioned by (date);
insert into raw.transactions select hash, block_number, block_timestamp, transaction_index, from_address, to_address, value, gas, gas_price, receipt_gas_used, receipt_effective_gas_price, receipt_status, transaction_type, max_fee_per_gas, max_priority_fee_per_gas, date from read_parquet('s3://aws-public-blockchain/v1.0/eth/transactions/date=2026-10-0[1-7]/*.parquet');
select strftime(date, '%Y-%m-%d') as day, count(*) as transactions from raw.transactions group by all order by 1;
select regexp_extract(file, 'transactions/(.*)$', 1) as file from glob('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/raw/transactions/**/*.parquet');
select count(*) as transactions from raw.transactions where date = date '2026-10-03';<br>Click the green run arrow next to line 1<br>Click the green run arrow next to line 1<br>Zoom: explorer | 34 | 15 |
| b04 @0:34 | Now load the week, the first to the seventh of October, straight from S3. That is about nine hundred megabytes to download, so it takes a few minutes. The video speeds it up. | Click the green run arrow next to line 1<br>sql_wait: None<br>Zoom: explorer<br>Card: *Sped up* — **One week from S3** — 7 files, 12.7 million rows | 33 | 286 |
| b05 @5:20 | Transactions per day: between one and a half and two million. Twelve point seven million in total. | Click the green run arrow next to line 1<br>Zoom: sql-results | 17 | 6 |

## s03 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b06 @5:27 | On disk, under raw transactions, there is now one folder per date, with one Parquet file in each. | Click the green run arrow next to line 1<br>Zoom: sql-results | 18 | 7 |
| b07 @5:34 | A query for one day, the third of October, only needs the file in that day's folder. The catalog knows which file holds which date, so the rest is never opened. | Click the green run arrow next to line 1<br>Zoom: sql-results | 31 | 10 |
| b08 @5:44 | In Data Lake, open the transactions table. The Partitions tab shows the key: date. | Left bar → **DataLake**<br>Click **eth_lake**<br>Click **Refresh**<br>Click **transactions**<br>Click **Partitions**<br>Zoom: center-wide | 14 | 17 |

## s04 · slide — slide `key`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b09 @6:01 | Choose a key that your queries filter on, with not too many values: a day, or a month. Partition by something like an address, and you get millions of tiny files. | Good keys: low cardinality, used in filters (date, month). Too fine = many small files. | 31 | 10 |
| b10 @6:11 | You can change the key later. The new key applies to new data only; existing files stay as they are. | Change it later: ALTER TABLE … SET PARTITIONED BY (year(block_timestamp), month(block_timestamp)); applies to new data only. | 20 | 7 |

## s05 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b11 @6:18 | Save the script as 4 underscore 1 partitioning dot sequel, commit, and push. | Left bar → **DBT Studio**<br>Right-click `sql` → **New File** → `4_1_partitioning.sql` → **Save**<br>paste: create table raw.transactions (hash varchar, block_number bigint, block_timestamp timestamp, transaction_index bigint, from_address varchar, to_address varchar, value double, gas bigint, gas_price bigint, receipt_gas_used bigint, receipt_effective_gas_price bigint, receipt_status bigint, transaction_type bigint, max_fee_per_gas bigint, max_priority_fee_per_gas bigint, date date);
alter table raw.transactions set partitioned by (date);
insert into raw.transactions select hash, block_number, block_timestamp, transaction_index, from_address, to_address, value, gas, gas_price, receipt_gas_used, receipt_effective_gas_price, receipt_status, transaction_type, max_fee_per_gas, max_priority_fee_per_gas, date from read_parquet('s3://aws-public-blockchain/v1.0/eth/transactions/date=2026-10-0[1-7]/*.parquet');
select strftime(date, '%Y-%m-%d') as day, count(*) as transactions from raw.transactions group by all order by 1;
select regexp_extract(file, 'transactions/(.*)$', 1) as file from glob('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/raw/transactions/**/*.parquet');
select count(*) as transactions from raw.transactions where date = date '2026-10-03';
<br>Click **Save**<br>(check: `sql/4_1_partitioning.sql` equals `../snippets/4.1/4_1_partitioning.sql`)<br>Close the editor tab for `sql/4_1_partitioning.sql`<br>Open the **Git** tab in the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Type the commit message “Load a week of transactions, partitioned by day”<br>Click **Commit**<br>git_push: None<br>Zoom: git-panel | 13 | 28 |

## s06 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b12 @6:46 | To recap: raw transactions is partitioned by date, with one folder per day, so a query for one day opens one file. Next: statistics, and how they skip files even without partitions. | Recap: partitioned by date; one folder per day; a one-day query opens one file; changing the key affects new data. | 32 | 13 |

## s07 · closing card (4 s, no voice)

Next · Lesson 4.2 · Statistics and file pruning.

**Total: 288 spoken words, 7:03 rendered.**
