# The Ethereum data: blocks, transactions, gas — voice-over script and beat sheet

Data Lakes with DuckLake in Rosetta DBT Studio · Module 1 · Data lakes explained · next: Lesson 1.6 · Under the hood: DuckDB and DuckLake in Studio

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `none (slides only)`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 2 · Lesson 1.5. The Ethereum data.

## s01 · slide — slide `blocks`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | Ethereum is a chain of blocks. A new block is added every twelve seconds. On the first of October 2026, that was seven thousand one hundred seventy-six blocks. | A chain of blocks, one every 12 seconds; 7,176 on 1 October 2026. | 29 | 11 |
| b02 @0:14 | Each block holds a list of transactions, two hundred eighty-four on average that day. | A block holds transactions: 284 on average. | 15 | 6 |

## s02 · slide — slide `gas`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b03 @0:20 | Every transaction needs some work, measured in gas. A block has a gas limit, sixty million, and it was about half full on average. | Gas: the work a transaction needs. A block has a gas limit, 60 million. | 24 | 8 |
| b04 @0:28 | For each unit of gas you pay a base fee, set by the network from how busy it is. That day it averaged zero point six four gwei. | Base fee per gas, set by the network: 0.639 gwei on average. | 28 | 9 |
| b05 @0:37 | The units: values are stored in wei. One ether is ten to the eighteen wei, and one gwei is a billion wei. Our staging models convert them. | Units: 1 ether = 10^18 wei; 1 gwei = 10^9 wei. | 27 | 9 |
| b06 @0:46 | Addresses and hashes are long hexadecimal strings, starting with zero x. We never read them out loud. | Addresses and hashes are hex text: 0x… | 17 | 7 |

## s03 · browser — Browser

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b07 @0:53 | The data is free and public. Amazon publishes it in the AWS Public Blockchain dataset, as Parquet files on S3, one folder per day, updated every day. | Browser: open https://registry.opendata.aws/aws-public-blockchain/<br>Zoom: center-wide | 27 | 12 |

## s04 · slide — slide `tables`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b08 @1:05 | We use two tables. Blocks: one row per block, with its number, time, the address that built it, the gas used, and the base fee. | blocks: number, timestamp, miner, gas_used, gas_limit, base_fee_per_gas, transaction_count, date. | 25 | 9 |
| b09 @1:14 | And transactions: one row per transaction, with who sent it, to whom, the value, the gas it used, the price paid, and whether it succeeded. | transactions: hash, block_number, from_address, to_address, value, receipt_gas_used, receipt_effective_gas_price, receipt_status, date. | 25 | 9 |

## s05 · slide — slide `load`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b10 @1:23 | We load three months of blocks: about six hundred sixty thousand rows. | Blocks: three months, 659,896 rows, about 230 MB in the lake. | 12 | 5 |
| b11 @1:28 | And one week of transactions: twelve point seven million rows, about one point seven gigabytes. Not every day of the year: just enough to be real, and still fit on a laptop. | Transactions: one week, 12.7 million rows, about 1.7 GB; without the input column. | 32 | 12 |

## s06 · closing card (4 s, no voice)

Next · Lesson 1.6 · Under the hood.

**Total: 261 spoken words, 1:44 rendered.**
