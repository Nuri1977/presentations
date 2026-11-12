# Welcome: an Ethereum data lake on your laptop — voice-over script and beat sheet

Data Lakes with DuckLake in Rosetta DBT Studio · Welcome · next: Lesson 0.1 · Install Rosetta DBT Studio

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `none (slides only)`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 2 · Lesson 0 · Welcome. Data lakes and DuckLake. Badges: Rosetta DBT Studio, DuckLake, DuckDB, dbt.

## s01 · slide — slide `promise`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | Welcome to Project 2. In this course, you build a real data lake, on your own laptop. Not a toy: a lake with versions, time travel, maintenance, and dbt models on top. | Statement: a real data lake on your laptop, with versions, time travel and dbt on top. | 32 | 12 |
| b02 @0:14 | You need no cloud account and no server. Everything runs inside Rosetta DBT Studio, with open source tools. | Pills: no cloud account, no server, open source. | 18 | 8 |

## s02 · slide — slide `build`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b03 @0:23 | We start from a public bucket on Amazon S3, with the Ethereum blockchain as Parquet files, one folder a day. | Source node: Ethereum data on S3, public Parquet files, one folder a day. | 20 | 8 |
| b04 @0:31 | We load it into a DuckLake: a catalog database, and a folder of Parquet files that the catalog manages. | Lake node: DuckLake, a catalog file and a folder of Parquet files. | 19 | 7 |
| b05 @0:38 | Then dbt builds clean models on top: staging views, and marts that grow day by day. | dbt node: staging views and marts, built incrementally. | 16 | 7 |
| b06 @0:45 | And at the end, answers: how busy the network was each day, what gas cost, and who sent the most transactions. | Answers node: daily activity, gas fees, the busiest senders. | 21 | 8 |

## s03 · slide — slide `data`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b07 @0:53 | The data is real. Three months of Ethereum blocks: August to October 2026, almost six hundred sixty thousand blocks. | Blocks: August to October 2026, 92 days, 659,896 blocks. | 19 | 10 |
| b08 @1:03 | And one week of transactions: twelve point seven million rows. | Transactions: 1 to 7 October 2026, 12.7 million rows. | 10 | 5 |
| b09 @1:07 | Big enough to feel real, small enough for a laptop. About three gigabytes of free disk is plenty. | Disk: about 3 GB free is enough. | 18 | 7 |

## s04 · slide — slide `tools`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b10 @1:14 | One app does it all: Rosetta DBT Studio. It has screens for data lakes, a SQL editor, dbt, and git, in one window. | Rosetta DBT Studio: one app, Data Lake screens, SQL Editor, dbt, git. | 23 | 9 |
| b11 @1:23 | Underneath, DuckDB is the engine, and DuckLake is the lake format. And dbt builds the models. | DuckDB and DuckLake: the engine, and the lake format. | 16 | 7 |

## s05 · slide — slide `map`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b12 @1:31 | Here is the route. First, we install Studio, and explain data lakes: warehouses, lakehouses, Parquet, table formats, and how DuckLake works. | Modules 0 and 1: install, and data lakes explained. | 21 | 10 |
| b13 @1:41 | Then hands on. We create the lake and load it, change data safely, make it fast and keep it tidy, and look inside the catalog. | Modules 2 to 5: first lake, changing data, performance and upkeep, inside the catalog. | 25 | 9 |
| b14 @1:50 | Finally, dbt on the lake, and where to go next. | Modules 6 and 7: dbt on DuckLake, and going further. | 10 | 4 |
| b15 @1:54 | You need a computer, some basic SQL, and a GitHub account. Every hands-on lesson ends with a commit to the course repository, linked in the description. See you in the next lesson. | What you need: a computer, basic SQL, a GitHub account; the code repo github.com/Nuri1977/ethereum-ducklake-dbt. | 33 | 12 |

## s06 · closing card (4 s, no voice)

Next · Lesson 0.1 · Install Rosetta DBT Studio.

**Total: 301 spoken words, 2:10 rendered.**
