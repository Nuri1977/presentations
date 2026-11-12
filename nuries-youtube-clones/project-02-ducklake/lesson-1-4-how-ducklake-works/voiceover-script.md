# How DuckLake works — voice-over script and beat sheet

Data Lakes with DuckLake in Rosetta DBT Studio · Module 1 · Data lakes explained · next: Lesson 1.5 · The Ethereum data

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `none (slides only)`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 2 · Lesson 1.4. How DuckLake works. Badges: Catalog, Parquet files, Snapshots.

## s01 · slide — slide `parts`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | A DuckLake has two parts, and only two. | Heading: A catalog and a folder of files. | 8 | 3 |
| b02 @0:06 | The first part is the catalog. It is a normal SQL database. It knows the tables, their columns, and exactly which files belong to each table. It can be a DuckDB file, SQLite, PostgreSQL, or MySQL. | Catalog box: a normal SQL database with tables, columns, snapshots and the list of files. Choices: DuckDB file, SQLite, PostgreSQL, MySQL. | 36 | 15 |
| b03 @0:21 | The second part is the data: a folder, or a bucket, of Parquet files. These files are never edited. They are only added, or removed. | Data box: a folder or a bucket of Parquet files, never edited. | 25 | 10 |

## s02 · slide — slide `write`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b04 @0:30 | Here is what happens when you insert rows. First, DuckLake writes the new rows as Parquet files in the data folder. Nobody can see them yet. | Step 1: write new Parquet files into the data folder. | 26 | 10 |
| b05 @0:40 | Then, in one database transaction, the catalog records those files and creates a new snapshot. That commit is the moment the change becomes visible. | Step 2: one transaction in the catalog records the files and creates a snapshot. | 24 | 10 |
| b06 @0:50 | If anything fails on the way, the catalog does not change, and readers never see half a write. | Step 3: if anything fails, the catalog does not change. | 18 | 6 |

## s03 · slide — slide `read`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b07 @0:56 | A read goes the other way. The query first asks the catalog which files make up the table right now. | Ask the catalog which files make up the table now. | 20 | 7 |
| b08 @1:03 | The catalog also keeps statistics for every file, like the smallest and largest value of each column. So files that cannot match the filter are skipped. | Skip files by statistics: min and max per column. | 26 | 10 |
| b09 @1:13 | Only then does it read the Parquet files that are left. | Read only the Parquet files that are left. | 11 | 4 |

## s04 · slide — slide `gets`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b10 @1:17 | This simple design gives you a lot. Changes are real transactions, even across several tables. | Card: ACID transactions, across tables. | 15 | 7 |
| b11 @1:23 | Every change is a snapshot, so you can query a table as it was yesterday, or last week. | Card: snapshots and time travel. | 18 | 6 |
| b12 @1:30 | And a small change stays small. It is a few rows in the catalog, not a pile of new metadata files. | Card: small changes stay small: a few rows in the catalog. | 21 | 7 |

## s05 · slide — slide `readers`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b13 @1:37 | Who can read a DuckLake? Today, DuckDB does, through the ducklake extension. That is what Rosetta DBT Studio uses under the hood. | DuckDB with the ducklake extension reads and writes the lake. | 22 | 9 |
| b14 @1:46 | And because the catalog is plain SQL tables, and the data is plain Parquet, nothing is locked away. Any SQL client can look inside the catalog. | The catalog is plain SQL tables; the data is plain Parquet. | 26 | 10 |

## s06 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b15 @1:56 | To recap: the catalog is a database, and the data is Parquet. Files are never edited, only added or removed. And every change makes a snapshot. Next, we meet the data for this course: Ethereum blocks and transactions. | Recap: catalog is a database, data is Parquet; files are never edited; every change is a snapshot. | 38 | 15 |

## s07 · closing card (4 s, no voice)

Next · Lesson 1.5 · The Ethereum data. Code: github.com/Nuri1977/ethereum-ducklake-dbt.

**Total: 334 spoken words, 2:15 rendered.**
