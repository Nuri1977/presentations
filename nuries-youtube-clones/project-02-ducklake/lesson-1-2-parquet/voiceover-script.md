# Parquet: why lakes use column files — voice-over script and beat sheet

Data Lakes with DuckLake in Rosetta DBT Studio · Module 1 · Data lakes explained · next: Lesson 1.3 · Table formats and catalogs

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `none (slides only)`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 2 · Lesson 1.2. Parquet: why lakes use column files.

## s01 · slide — slide `rows`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | A CSV file stores data row by row. Each line is a whole record: every column of one Ethereum block. | A row file: each line holds a whole block, all columns. | 20 | 8 |
| b02 @0:10 | Parquet stores it column by column. All the block numbers together, then all the miners, then all the transaction counts. | A column file: all numbers together, then all miners, then all counts. | 20 | 8 |
| b03 @0:18 | Why does that matter? Analytics queries use a few columns out of many. With columns stored apart, the engine reads only the ones it needs. | A query for two columns reads two columns, not the whole file. | 25 | 9 |

## s02 · slide — slide `inside`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b04 @0:27 | Here is a real file: one day of Ethereum blocks from the public bucket. Seven thousand one hundred seventy-six rows, in one row group, compressed with Snappy. | One real file: one day of blocks, 7,176 rows, 1 row group, Snappy compression. | 28 | 10 |
| b05 @0:38 | A big file is split into row groups, chunks of rows. Inside each chunk, every column is stored on its own. | Row groups: chunks of rows; each column stored in each chunk. | 21 | 7 |
| b06 @0:45 | The file is five point six megabytes. More than half of it is one column, logs bloom, that we do not need. Later we simply leave it out. | Biggest column: logs_bloom, 3.0 MB of 5.6 MB. We drop it when we load. | 28 | 9 |

## s03 · slide — slide `stats`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b07 @0:54 | The most useful part: for every column in every row group, the file stores the smallest and the largest value. Block numbers in this file go from twenty-six million ninety-three thousand to twenty-six million one hundred thousand. | Per column, per row group: min and max. number: 26,093,738 to 26,100,913. | 40 | 15 |
| b08 @1:09 | So if you ask for block twenty-six million two hundred thousand, the engine looks at those two numbers and skips the whole file, without reading a single row. | Query for block 26,200,000: skip this file without reading it. | 29 | 10 |
| b09 @1:19 | DuckLake goes one step further: it copies these statistics into its catalog, so it can skip files before even opening them. We see that in Modules 4 and 5. | DuckLake keeps these statistics in its catalog (Modules 4 and 5). | 29 | 11 |

## s04 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b10 @1:29 | To recap: Parquet stores columns, not rows. It splits rows into row groups, compresses each column, and keeps the min and max of every column, so engines can skip what they do not need. Next: how table formats turn these files into tables. | Recap: columns, row groups, compression, min and max per column. | 43 | 16 |

## s05 · closing card (4 s, no voice)

Next · Lesson 1.3 · Table formats and catalogs.

**Total: 283 spoken words, 1:50 rendered.**
