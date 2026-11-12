# Partitioning — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `lesson-3-5-end`: raw.blocks and raw.blocks_day; no transactions yet.

## s02 · Create and load

| Listen for | Do this |
|---|---|
| "In the SQL Editor, on eth lake: create…" | In the left bar, click **SQL Editor**<br>Open the connection list (top left) and pick **eth_lake**<br>paste: create table raw.transactions (hash varchar, block_number bigint, block_timestamp timestamp, transaction_index bigint, from_address varchar, to_address varchar, value double, gas bigint, gas_price bigint, receipt_gas_used bigint, receipt_effective_gas_price bigint, receipt_status bigint, transaction_type bigint, max_fee_per_gas bigint, max_priority_fee_per_gas bigint, date date);<br>alter table raw.transactions set partitioned by (date);<br>insert into raw.transactions select hash, block_number, block_timestamp, transaction_index, from_address, to_address, value, gas, gas_price, receipt_gas_used, receipt_effective_gas_price, receipt_status, transaction_type, max_fee_per_gas, max_priority_fee_per_gas, date from read_parquet('s3://aws-public-blockchain/v1.0/eth/transactions/date=2026-10-0[1-7]/*.parquet');<br>select strftime(date, '%Y-%m-%d') as day, count(*) as transactions from raw.transactions group by all order by 1;<br>select regexp_extract(file, 'transactions/(.*)$', 1) as file from glob('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/raw/transactions/**/*.parquet');<br>select count(*) as transactions from raw.transactions where date = date '2026-10-03';<br>Click the green ▶ arrow next to line 1<br>Click the green ▶ arrow next to line 1 |
| "Now load the week, the first to the…" | Click the green ▶ arrow next to line 1<br>sql_wait: None |
| "Transactions per day: between one and a half…" | Click the green ▶ arrow next to line 1 |

## s03 · One folder per day

| Listen for | Do this |
|---|---|
| "On disk, under raw transactions, there is now…" | Click the green ▶ arrow next to line 1 |
| "A query for one day, the third of…" | Click the green ▶ arrow next to line 1 |
| "In Data Lake, open the transactions table. The…" | In the left bar, click **DataLake**<br>Click **eth_lake**<br>Click **Refresh**<br>Click **transactions**<br>Click **Partitions** |

## s05 · Commit and push

| Listen for | Do this |
|---|---|
| "Save the script as 4 underscore 1 partitioning…" | In the left bar, click **DBT Studio**<br>Right-click `sql` → **New File**, type `4_1_partitioning.sql`, click **Save**<br>paste: create table raw.transactions (hash varchar, block_number bigint, block_timestamp timestamp, transaction_index bigint, from_address varchar, to_address varchar, value double, gas bigint, gas_price bigint, receipt_gas_used bigint, receipt_effective_gas_price bigint, receipt_status bigint, transaction_type bigint, max_fee_per_gas bigint, max_priority_fee_per_gas bigint, date date);<br>alter table raw.transactions set partitioned by (date);<br>insert into raw.transactions select hash, block_number, block_timestamp, transaction_index, from_address, to_address, value, gas, gas_price, receipt_gas_used, receipt_effective_gas_price, receipt_status, transaction_type, max_fee_per_gas, max_priority_fee_per_gas, date from read_parquet('s3://aws-public-blockchain/v1.0/eth/transactions/date=2026-10-0[1-7]/*.parquet');<br>select strftime(date, '%Y-%m-%d') as day, count(*) as transactions from raw.transactions group by all order by 1;<br>select regexp_extract(file, 'transactions/(.*)$', 1) as file from glob('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/raw/transactions/**/*.parquet');<br>select count(*) as transactions from raw.transactions where date = date '2026-10-03';<br><br>Click **Save** (top right of the editor)<br>(Check that `sql/4_1_partitioning.sql` matches `../snippets/4.1/4_1_partitioning.sql`)<br>Close the editor tab for `sql/4_1_partitioning.sql` (its ×)<br>Click the **Git** tab at the top of the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Click the message box and type: Load a week of transactions, partitioned by day<br>Click **Commit**<br>git_push: None |
