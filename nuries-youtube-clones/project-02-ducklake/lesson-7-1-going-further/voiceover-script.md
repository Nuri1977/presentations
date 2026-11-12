# Going further, and recap — voice-over script and beat sheet

Data Lakes with DuckLake in Rosetta DBT Studio · Module 7 · Wrap-up · next: The DuckLake docs and the course repository

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `none (slides only)`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 2 · Lesson 7.1. Going further, and recap.

## s01 · slide — slide `shared`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | Our lake lives on a laptop: a DuckDB file as catalog, and a local folder. For a team, swap both. Use PostgreSQL as the catalog, and object storage like S3 for the data. Same lake format, same SQL. | Code: ATTACH 'ducklake:postgres:dbname=ducklake_catalog host=…' AS lake (DATA_PATH 's3://bucket/path/'); | 38 | 15 |
| b02 @0:18 | Now many people and many machines can attach the same lake, and write at the same time. | Many writers at once; any machine can attach the lake. | 17 | 6 |
| b03 @0:24 | We tested S3 compatible storage too: it works from DuckDB and dbt, but Studio's wizard does not support it yet. A follow-up tutorial covers PostgreSQL with cloud storage. | Tested: S3-compatible storage works from DuckDB and dbt; Studio 1.7.6's wizard does not support it yet. A follow-up tutorial covers PostgreSQL + cloud S3. | 29 | 13 |

## s02 · slide — slide `ops`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b04 @0:37 | Running a lake for real means a few more things. Access control comes from two places: permissions in the catalog database, and policies on the bucket. | Access control: database permissions on the catalog + bucket policies on the files. | 26 | 10 |
| b05 @0:47 | Backups: back up the catalog database, and turn on versioning for the bucket. | Backups: back up the catalog database; version the bucket. | 13 | 5 |
| b06 @0:53 | Encryption: DuckLake can encrypt every data file, and keeps the keys in the catalog. | Encryption: data files encrypted, keys kept in the catalog. | 14 | 6 |
| b07 @0:58 | And an existing DuckDB database can be moved into a DuckLake, table by table. | Migration: move an existing DuckDB database into DuckLake. | 14 | 6 |

## s03 · slide — slide `notyet`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b08 @1:04 | Some things are not supported today, like primary keys, unique and foreign key constraints, and indexes. Check the docs page on unsupported features: it changes with each release. | Not supported today: primary keys, unique and foreign key constraints, indexes, sequences… | 28 | 12 |

## s04 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b09 @1:16 | Let's look back. A DuckLake is a catalog database plus Parquet files. Every change is a snapshot you can travel back to. Updates and deletes never rewrite files. Partitions, statistics and maintenance keep it fast and small. The catalog is plain SQL you can read yourself. And dbt builds tested models right on top. Thanks for watching, and see you in the next course. | Recap of the course: catalog + Parquet; snapshots and time travel; changes without rewrites; partitions, statistics, maintenance; the catalog is plain SQL; dbt on the lake. | 64 | 24 |

## s05 · closing card (4 s, no voice)

Docs: ducklake.select. Code: github.com/Nuri1977/ethereum-ducklake-dbt.

**Total: 243 spoken words, 1:45 rendered.**
