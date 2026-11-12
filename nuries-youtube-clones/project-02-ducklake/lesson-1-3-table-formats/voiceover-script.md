# Table formats: Iceberg, Delta Lake, DuckLake — voice-over script and beat sheet

Data Lakes with DuckLake in Rosetta DBT Studio · Module 1 · Data lakes explained · next: Lesson 1.4 · How DuckLake works

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `none (slides only)`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 2 · Lesson 1.3. Table formats and catalogs.

## s01 · slide — slide `track`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | Every table format answers the same three questions. Which files make up the table right now? What is its schema? And which version is this, so we can go back? | Three questions: which files, which schema, which version. | 30 | 10 |

## s02 · slide — slide `iceberg`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b02 @0:13 | Apache Iceberg keeps its answers as files, in the same bucket as the data. A metadata file in JSON points to a manifest list, which points to manifest files, which finally list the Parquet data files. | Iceberg: metadata JSON file → manifest list → manifests (Avro) → Parquet data files, all in the bucket. | 36 | 14 |
| b03 @0:26 | And you still need a catalog service, which holds one pointer: the current metadata file of each table. | A catalog service holds the pointer to the current metadata file. | 18 | 7 |

## s03 · slide — slide `delta`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b04 @0:33 | Delta Lake also uses files. Each change is a numbered JSON file in a folder called delta log, and every so often a checkpoint file sums up the log. | Delta: a _delta_log folder of numbered JSON commits, plus Parquet checkpoints. | 29 | 11 |

## s04 · slide — slide `cost`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b05 @0:44 | Both designs work, and both are widely used. But they share some costs. Every change writes new small metadata files. | Many small metadata files. | 20 | 8 |
| b06 @0:53 | A query needs several round trips, file after file, before it reads a single row of data. | Several round trips before reading any data. | 17 | 6 |
| b07 @0:59 | And for real use you run a catalog service anyway, often backed by a database. | And a catalog service to run anyway. | 15 | 6 |

## s05 · slide — slide `idea`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b08 @1:05 | DuckLake starts from that last point. If you need a database for the catalog anyway, why not put all the metadata in it? Files, schemas, snapshots, statistics: all plain SQL tables. | If a database is needed anyway, put all the metadata in it: plain SQL tables. | 31 | 12 |
| b09 @1:17 | The data itself stays exactly where it was: Parquet files, on a disk or in a bucket. | Data stays in Parquet files on any storage. | 17 | 6 |
| b10 @1:23 | Now a change is one database transaction, and finding the files for a query is one SQL query. | A change is one database transaction; a read is one query to the catalog. | 18 | 7 |

## s06 · slide — slide `compare`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b11 @1:31 | Side by side. Iceberg and Delta keep metadata as files in the bucket, have many engines, and years of production use. DuckLake keeps metadata in a database, is read by DuckDB today, and is younger. In this course, we use DuckLake: it runs on a laptop with no services at all. | Table: metadata location, catalog, engines, age, for Iceberg, Delta Lake, DuckLake. | 51 | 19 |

## s07 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b12 @1:49 | To recap: a table format tracks files, schema and versions. Iceberg and Delta store that as files next to the data. DuckLake stores it as tables in a database. Next: how DuckLake works, step by step. | Recap: formats track files, schema, versions; Iceberg and Delta use metadata files; DuckLake uses a SQL database. | 36 | 13 |

## s08 · closing card (4 s, no voice)

Next · Lesson 1.4 · How DuckLake works.

**Total: 318 spoken words, 2:07 rendered.**
