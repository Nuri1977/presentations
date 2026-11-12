# Warehouse, data lake, lakehouse — voice-over script and beat sheet

Data Lakes with DuckLake in Rosetta DBT Studio · Module 1 · Data lakes explained · next: Lesson 1.2 · Parquet: why lakes use column files

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `none (slides only)`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 2 · Lesson 1.1. Warehouse, data lake, lakehouse.

## s01 · slide — slide `warehouse`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | Let's start with the classic data warehouse. One system owns everything: the storage, and the engine that runs your queries. Data goes in through the warehouse's own door. | Warehouse box: storage and compute in one system; data goes in through its own loader. | 28 | 11 |
| b02 @0:13 | That makes it fast and safe, with real transactions. But the data lives in the warehouse's own format, only its engine can read it, and you pay for storage and compute together. | Pros: fast, safe, transactions. Cons: the data lives in its format; one engine; you pay for storage and compute together. | 32 | 11 |

## s02 · slide — slide `lake`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b03 @0:25 | A data lake turns this around. The data is just files, on cheap storage: a folder, or a bucket on S3. In open formats, like Parquet. | Lake: files on cheap storage (a folder, S3); open formats like Parquet. | 26 | 10 |
| b04 @0:34 | Any engine can read those files: DuckDB, Spark, Trino, or a Python script. Storage and compute are separate. | Engines around it: DuckDB, Spark, Trino, Python, all read the same files. | 18 | 8 |

## s03 · slide — slide `lacks`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b05 @0:42 | But plain files have problems. There are no transactions: a reader can see a write that is only half done. | No transactions: a reader can see half a write. | 20 | 7 |
| b06 @0:49 | There are no safe updates or deletes. To change one row, you rewrite a whole file, and hope nobody reads it at that moment. | No safe updates or deletes: you rewrite whole files. | 24 | 8 |
| b07 @0:57 | And there is no schema and no history. Which columns does the table have, and what did it look like yesterday? The files do not say. | No schema and no history: which columns, which version? | 26 | 9 |
| b08 @1:06 | Even finding the files is slow: listing thousands of objects in a bucket, just to plan one query. | Slow listing: listing thousands of files in a bucket. | 18 | 7 |

## s04 · slide — slide `lakehouse`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b09 @1:13 | The lakehouse fixes this, without giving up open files. It adds a table format on top: a small layer of metadata that says which files make up each table, right now. | Lakehouse: open files plus a table format on top. | 31 | 11 |
| b10 @1:24 | With that layer you get the warehouse features back: transactions, safe updates and deletes, schema changes, and a history you can travel back in. The data stays in open files. | You get back: transactions, updates and deletes, schema changes, history and time travel. | 30 | 12 |

## s05 · slide — slide `words`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b11 @1:36 | Four words we use through the whole course. The lake: the data files, on some storage. | Lake: the files, on some storage. | 16 | 6 |
| b12 @1:42 | The table format: the rules for keeping track of which files make up a table, and how it changes. | Table format: the rules for tracking which files are a table. | 19 | 7 |
| b13 @1:48 | The catalog: where that tracking information is stored. | Catalog: where that tracking information lives. | 8 | 4 |
| b14 @1:52 | And the engine: the program that reads it all and runs your queries. In this course, that is DuckDB. | Engine: the program that runs your queries, here DuckDB. | 19 | 7 |

## s06 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b15 @1:59 | To recap: a warehouse is one system for everything. A lake is open files. A lakehouse is open files, plus a table format that makes them behave like tables. Next: why lakes store data in Parquet. | Recap: warehouse = one system; lake = open files; lakehouse = open files + a table format. | 36 | 14 |

## s07 · closing card (4 s, no voice)

Next · Lesson 1.2 · Parquet.

**Total: 351 spoken words, 2:17 rendered.**
