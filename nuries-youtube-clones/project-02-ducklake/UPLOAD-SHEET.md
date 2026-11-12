# Upload sheet: Data Lakes with DuckLake in Rosetta DBT Studio

Project 2: an Ethereum data lake on your laptop, from the first snapshot to dbt models on top

- **Playlist:** Data Lakes with DuckLake in Rosetta DBT Studio: Project 2
- **Videos:** 31, 1:15:13 in total. Upload in the order below.
- **Visibility:** unlisted (embedded in Rosetta Academy: https://academy.rosettadb.io/)
- **Code repo:** https://github.com/Nuri1977/ethereum-ducklake-dbt (public, `main` at `7e9b9d9`, one commit per hands-on lesson from 2.1; 4.5 has a second commit that fixes a double registration)
- **Made on 12 Nov 2026** with Rosetta DBT Studio 1.7.6, the white slide theme and the Kokoro voice.

## Before you upload

- **Listen once** to each video for pronunciation. Claude cannot hear audio.
- Upload the **4K** file to YouTube with its `.srt`. Share the **1080p** copy in chat or by phone.
- Studio 1.7.6 quirks the videos explain on screen: dates show as a day number in 3.2; the change feed of 3.4 shows updates as delete + insert (DuckDB 1.5.2); 4.4 calls show no result rows; 4.5 wraps `ducklake_add_data_files` in `CREATE TEMP TABLE` because the result pane runs a statement twice.
- In 6.1 the lock error shows a local path; that line is blurred in the video.

## Files

| # | Lesson | Title | Length | 4K file (upload this) | Captions |
|---|---|---|---|---|---|
| 1 | 0 | Welcome: an Ethereum data lake on your laptop | 2:10 | `lesson-0-welcome/lesson-0.mp4` (17 MB) | `lesson-0.srt` |
| 2 | 0.1 | Install Rosetta DBT Studio from rosettadb.io | 2:13 | `lesson-0-1-install/lesson-0-1.mp4` (31 MB) | `lesson-0-1.srt` |
| 3 | 1.1 | Warehouse, data lake, lakehouse | 2:17 | `lesson-1-1-lakehouse/lesson-1-1.mp4` (17 MB) | `lesson-1-1.srt` |
| 4 | 1.2 | Parquet: why lakes use column files | 1:50 | `lesson-1-2-parquet/lesson-1-2.mp4` (14 MB) | `lesson-1-2.srt` |
| 5 | 1.3 | Table formats: Iceberg, Delta Lake, DuckLake | 2:07 | `lesson-1-3-table-formats/lesson-1-3.mp4` (17 MB) | `lesson-1-3.srt` |
| 6 | 1.4 | How DuckLake works | 2:15 | `lesson-1-4-how-ducklake-works/lesson-1-4.mp4` (20 MB) | `lesson-1-4.srt` |
| 7 | 1.5 | The Ethereum data: blocks, transactions, gas | 1:45 | `lesson-1-5-ethereum-data/lesson-1-5.mp4` (18 MB) | `lesson-1-5.srt` |
| 8 | 1.6 | Under the hood: DuckDB and DuckLake in Studio | 2:19 | `lesson-1-6-under-the-hood/lesson-1-6.mp4` (21 MB) | `lesson-1-6.srt` |
| 9 | 2.1 | Create a DuckLake in Studio | 4:21 | `lesson-2-1-create-ducklake/lesson-2-1.mp4` (40 MB) | `lesson-2-1.srt` |
| 10 | 2.2 | Load three months of blocks from S3 | 3:34 | `lesson-2-2-load-blocks/lesson-2-2.mp4` (32 MB) | `lesson-2-2.srt` |
| 11 | 2.3 | Look inside: data files and tables | 2:06 | `lesson-2-3-look-inside/lesson-2-3.mp4` (21 MB) | `lesson-2-3.srt` |
| 12 | 2.4 | Snapshots: every change is a version | 2:10 | `lesson-2-4-snapshots/lesson-2-4.mp4` (21 MB) | `lesson-2-4.srt` |
| 13 | 2.5 | Time travel | 1:57 | `lesson-2-5-time-travel/lesson-2-5.mp4` (17 MB) | `lesson-2-5.srt` |
| 14 | 3.1 | Insert, update, delete, and delete files | 2:21 | `lesson-3-1-insert-update-delete/lesson-3-1.mp4` (23 MB) | `lesson-3-1.srt` |
| 15 | 3.2 | Daily loads without duplicates | 2:08 | `lesson-3-2-daily-loads/lesson-3-2.mp4` (21 MB) | `lesson-3-2.srt` |
| 16 | 3.3 | Schema evolution | 2:11 | `lesson-3-3-schema-evolution/lesson-3-3.mp4` (21 MB) | `lesson-3-3.srt` |
| 17 | 3.4 | The data change feed | 2:09 | `lesson-3-4-change-feed/lesson-3-4.mp4` (18 MB) | `lesson-3-4.srt` |
| 18 | 3.5 | Transactions and conflicts | 2:00 | `lesson-3-5-transactions/lesson-3-5.mp4` (17 MB) | `lesson-3-5.srt` |
| 19 | 4.1 | Partitioning | 7:03 | `lesson-4-1-partitioning/lesson-4-1.mp4` (62 MB) | `lesson-4-1.srt` |
| 20 | 4.2 | Statistics and file pruning | 2:23 | `lesson-4-2-statistics/lesson-4-2.mp4` (22 MB) | `lesson-4-2.srt` |
| 21 | 4.3 | Data inlining for small writes | 1:59 | `lesson-4-3-data-inlining/lesson-4-3.mp4` (17 MB) | `lesson-4-3.srt` |
| 22 | 4.4 | Maintenance | 2:34 | `lesson-4-4-maintenance/lesson-4-4.mp4` (23 MB) | `lesson-4-4.srt` |
| 23 | 4.5 | Adding existing Parquet files | 2:11 | `lesson-4-5-adding-files/lesson-4-5.mp4` (23 MB) | `lesson-4-5.srt` |
| 24 | 5.1 | Inside the catalog: snapshots, tables, columns | 2:16 | `lesson-5-1-catalog-snapshots/lesson-5-1.mp4` (20 MB) | `lesson-5-1.srt` |
| 25 | 5.2 | Inside the catalog: files and statistics | 2:01 | `lesson-5-2-catalog-files/lesson-5-2.mp4` (20 MB) | `lesson-5-2.srt` |
| 26 | 5.3 | Read the lake by hand | 2:13 | `lesson-5-3-read-by-hand/lesson-5-3.mp4` (19 MB) | `lesson-5-3.srt` |
| 27 | 6.1 | Connect a dbt project to the lake | 2:29 | `lesson-6-1-connect-dbt/lesson-6-1.mp4` (24 MB) | `lesson-6-1.srt` |
| 28 | 6.2 | Staging models for blocks and transactions | 2:04 | `lesson-6-2-staging/lesson-6-2.mp4` (23 MB) | `lesson-6-2.srt` |
| 29 | 6.3 | Marts, built incrementally | 2:19 | `lesson-6-3-marts/lesson-6-3.mp4` (29 MB) | `lesson-6-3.srt` |
| 30 | 6.4 | Tests and docs on the lake | 2:02 | `lesson-6-4-tests-docs/lesson-6-4.mp4` (25 MB) | `lesson-6-4.srt` |
| 31 | 7.1 | Going further, and recap | 1:45 | `lesson-7-1-going-further/lesson-7-1.mp4` (15 MB) | `lesson-7-1.srt` |

Captions, thumbnails (`thumbnail.png`) and slides (`.pptx`) sit in the same lesson folder as the video.

## Titles, descriptions and tags

Copy each block as is. Chapters are inside the descriptions.

### 1. Lesson 0 · Welcome: an Ethereum data lake on your laptop

**Title** (96 characters)

```text
Welcome: an Ethereum data lake on your laptop | Data Lakes with DuckLake in Rosetta DBT Studio 0
```

**Description**

```text
Welcome to Project 2. Build a real data lake on your laptop with DuckLake and Rosetta DBT Studio: three months of Ethereum blocks and a week of transactions from a public S3 bucket, with snapshots, time travel and maintenance, and dbt models on top.

Part of the free Data Lakes with DuckLake in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 Welcome
0:23 What you will build
0:53 The data
1:14 The tools
1:31 The course map

Screens from Rosetta DBT Studio 1.7.6.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio

Code for this course (one commit per lesson): https://github.com/Nuri1977/ethereum-ducklake-dbt

Links for this lesson
- DuckLake documentation: https://ducklake.select/docs/stable/
- AWS Public Blockchain Data: https://registry.opendata.aws/aws-public-blockchain/
- Project 1: dbt + DuckDB in Rosetta DBT Studio: https://github.com/Nuri1977/nyc-taxi-dbt

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
```

**Tags**

```text
DuckLake, data lake, lakehouse, DuckDB, dbt, Ethereum, Rosetta DBT Studio, Parquet, SQL
```

### 2. Lesson 0.1 · Install Rosetta DBT Studio from rosettadb.io

**Title** (97 characters)

```text
Install Rosetta DBT Studio from rosettadb.io | Data Lakes with DuckLake in Rosetta DBT Studio 0.1
```

**Description**

```text
Install Rosetta DBT Studio from its website, rosettadb.io: pick the build for your computer on the Download page, copy the app to Applications, and let the first-run setup install Python, dbt Core and the DuckDB adapter for you.

Part of the free Data Lakes with DuckLake in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 The download page
0:30 Copy it to Applications
0:52 First-run setup
1:36 The home screen
1:53 What was installed

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio

Code for this course (one commit per lesson): https://github.com/Nuri1977/ethereum-ducklake-dbt

Links for this lesson
- Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
- Releases on GitHub: https://github.com/rosettadb/dbt-studio/releases
```

**Tags**

```text
Rosetta DBT Studio, install, dbt Core, DuckDB, Mac, Windows, Linux, DuckLake, data lake, lakehouse, dbt, Parquet, Ethereum, SQL
```

### 3. Lesson 1.1 · Warehouse, data lake, lakehouse

**Title** (84 characters)

```text
Warehouse, data lake, lakehouse | Data Lakes with DuckLake in Rosetta DBT Studio 1.1
```

**Description**

```text
Why data lakes exist, what plain files on cheap storage cannot do, and how a lakehouse puts real tables back on top of open files. Ends with four words used through the whole course: lake, table format, catalog and engine.

Part of the free Data Lakes with DuckLake in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 The warehouse
0:25 The data lake
0:42 What plain files lack
1:13 The lakehouse
1:36 Four words
1:59 Recap

Screens from Rosetta DBT Studio 1.7.6.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio

Code for this course (one commit per lesson): https://github.com/Nuri1977/ethereum-ducklake-dbt

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
```

**Tags**

```text
data lake, lakehouse, data warehouse, table format, catalog, DuckLake, DuckDB, dbt, Parquet, Ethereum, Rosetta DBT Studio, SQL
```

### 4. Lesson 1.2 · Parquet: why lakes use column files

**Title** (88 characters)

```text
Parquet: why lakes use column files | Data Lakes with DuckLake in Rosetta DBT Studio 1.2
```

**Description**

```text
What a Parquet file is: columns instead of rows, row groups, compression, and the min and max statistics that let an engine skip data it does not need. With real numbers from one day of Ethereum blocks on S3.

Part of the free Data Lakes with DuckLake in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 Rows or columns
0:27 Inside one file
0:54 Statistics
1:29 Recap

Screens from Rosetta DBT Studio 1.7.6.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio

Code for this course (one commit per lesson): https://github.com/Nuri1977/ethereum-ducklake-dbt

Links for this lesson
- DuckDB: Parquet metadata: https://duckdb.org/docs/stable/data/parquet/metadata

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
```

**Tags**

```text
Parquet, columnar storage, data lake, row groups, statistics, DuckDB, DuckLake, lakehouse, dbt, Ethereum, Rosetta DBT Studio, SQL
```

### 5. Lesson 1.3 · Table formats: Iceberg, Delta Lake, DuckLake

**Title** (97 characters)

```text
Table formats: Iceberg, Delta Lake, DuckLake | Data Lakes with DuckLake in Rosetta DBT Studio 1.3
```

**Description**

```text
What a table format has to track, how Apache Iceberg and Delta Lake keep that metadata as files next to the data, what that costs, and DuckLake's different idea: keep all metadata as plain tables in a SQL database.

Part of the free Data Lakes with DuckLake in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 What a format tracks
0:13 Apache Iceberg
0:33 Delta Lake
0:44 The cost
1:05 DuckLake's idea
1:31 Side by side
1:49 Recap

Screens from Rosetta DBT Studio 1.7.6.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio

Code for this course (one commit per lesson): https://github.com/Nuri1977/ethereum-ducklake-dbt

Links for this lesson
- DuckLake: the manifesto: https://ducklake.select/manifesto/
- Apache Iceberg specification: https://iceberg.apache.org/spec/
- Delta Lake protocol: https://github.com/delta-io/delta/blob/master/PROTOCOL.md

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
```

**Tags**

```text
Apache Iceberg, Delta Lake, DuckLake, table format, catalog, lakehouse, data lake, DuckDB, dbt, Parquet, Ethereum, Rosetta DBT Studio, SQL
```

### 6. Lesson 1.4 · How DuckLake works

**Title** (71 characters)

```text
How DuckLake works | Data Lakes with DuckLake in Rosetta DBT Studio 1.4
```

**Description**

```text
The mental model for the whole course: a DuckLake is a catalog database plus a folder of Parquet files. See what happens on a write and on a read, what that design gives you (transactions, snapshots, time travel), and who can read a DuckLake.

Part of the free Data Lakes with DuckLake in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 Two parts
0:30 A write
0:56 A read
1:17 What you get
1:37 Who can read it
1:56 Recap

Screens from Rosetta DBT Studio 1.7.6.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio

Code for this course (one commit per lesson): https://github.com/Nuri1977/ethereum-ducklake-dbt

Links for this lesson
- DuckLake documentation: https://ducklake.select/docs/stable/
- DuckLake specification: https://ducklake.select/docs/stable/specification/introduction

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
```

**Tags**

```text
DuckLake, lakehouse, data lake, Parquet, catalog, snapshots, time travel, DuckDB, dbt, Ethereum, Rosetta DBT Studio, SQL
```

### 7. Lesson 1.5 · The Ethereum data: blocks, transactions, gas

**Title** (97 characters)

```text
The Ethereum data: blocks, transactions, gas | Data Lakes with DuckLake in Rosetta DBT Studio 1.5
```

**Description**

```text
Just enough Ethereum to read the data: blocks every 12 seconds, transactions inside them, gas and the base fee, wei and ether, hex addresses. Where the data comes from (the AWS public blockchain bucket) and what this course loads.

Part of the free Data Lakes with DuckLake in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 Blocks
0:20 Gas and fees
0:53 Where the data lives
1:05 Two tables
1:23 What we load

Screens from Rosetta DBT Studio 1.7.6.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio

Code for this course (one commit per lesson): https://github.com/Nuri1977/ethereum-ducklake-dbt

Links for this lesson
- AWS Public Blockchain Data: https://registry.opendata.aws/aws-public-blockchain/
- Ethereum: gas and fees: https://ethereum.org/en/developers/docs/gas/

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
```

**Tags**

```text
Ethereum, blockchain data, AWS open data, Parquet, gas, base fee, DuckLake, data lake, lakehouse, DuckDB, dbt, Rosetta DBT Studio, SQL
```

### 8. Lesson 1.6 · Under the hood: DuckDB and DuckLake in Studio

**Title** (98 characters)

```text
Under the hood: DuckDB and DuckLake in Studio | Data Lakes with DuckLake in Rosetta DBT Studio 1.6
```

**Description**

```text
What runs when Rosetta DBT Studio shows a lake: DuckDB inside the app through its official Node.js package, the ducklake extension, and the ATTACH statement Studio runs for you. With short quotes from Studio's own source code, and why dbt is a second DuckDB reading the same lake.

Part of the free Data Lakes with DuckLake in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 Two processes
0:24 DuckDB inside the app
0:48 The DuckLake extension
1:21 See it in Studio
1:37 Two engines, one lake
2:01 Recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio

Code for this course (one commit per lesson): https://github.com/Nuri1977/ethereum-ducklake-dbt

Links for this lesson
- @duckdb/node-api on npm: https://www.npmjs.com/package/@duckdb/node-api
- DuckLake: connecting: https://ducklake.select/docs/stable/duckdb/usage/connecting
- Rosetta DBT Studio source: https://github.com/rosettadb/dbt-studio

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
```

**Tags**

```text
DuckDB, Node.js, DuckLake extension, Electron, Rosetta DBT Studio, DuckLake, data lake, lakehouse, dbt, Parquet, Ethereum, SQL
```

### 9. Lesson 2.1 · Create a DuckLake in Studio

**Title** (80 characters)

```text
Create a DuckLake in Studio | Data Lakes with DuckLake in Rosetta DBT Studio 2.1
```

**Description**

```text
Create the ethereum_lake project and your first DuckLake in Rosetta DBT Studio: a lake called eth_lake with a local data folder and a DuckDB catalog file, made in the Data Lake wizard. Look at the new lake, run the first query on it from the SQL Editor, and push the project to GitHub.

Part of the free Data Lakes with DuckLake in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 What we create
0:22 The project
1:13 The Data Lake wizard
1:58 The new lake
2:27 What the wizard did
2:49 Files that keep git clean
3:13 A repository on GitHub
3:27 First commit and push
3:58 Recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio

Code for this course (one commit per lesson): https://github.com/Nuri1977/ethereum-ducklake-dbt

Links for this lesson
- DuckLake documentation: connecting: https://ducklake.select/docs/stable/duckdb/usage/connecting

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
```

**Tags**

```text
DuckLake, data lake, Rosetta DBT Studio, DuckDB, catalog, Parquet, lakehouse, dbt, Ethereum, SQL
```

### 10. Lesson 2.2 · Load three months of blocks from S3

**Title** (88 characters)

```text
Load three months of blocks from S3 | Data Lakes with DuckLake in Rosetta DBT Studio 2.2
```

**Description**

```text
The first table in the lake: three months of Ethereum blocks read straight from the public S3 bucket into eth_lake.raw.blocks, one month per statement, from Rosetta DBT Studio's SQL Editor. Then the table in the Data Lake screens, and the script committed to the project.

Part of the free Data Lakes with DuckLake in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 The plan
0:35 Load the blocks
2:23 The table in Studio
2:39 Keep the script, commit, push
3:13 Recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio

Code for this course (one commit per lesson): https://github.com/Nuri1977/ethereum-ducklake-dbt

Links for this lesson
- DuckLake: introduction: https://ducklake.select/docs/stable/duckdb/introduction
- DuckDB: reading Parquet from S3: https://duckdb.org/docs/stable/core_extensions/httpfs/s3api

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
```

**Tags**

```text
DuckLake, S3, Parquet, DuckDB, SQL Editor, Ethereum, data lake, lakehouse, dbt, Rosetta DBT Studio, SQL
```

### 11. Lesson 2.3 · Look inside: data files and tables

**Title** (87 characters)

```text
Look inside: data files and tables | Data Lakes with DuckLake in Rosetta DBT Studio 2.3
```

**Description**

```text
Open the blocks table in Studio's Data Lake screens: its schema and its Data Files tab. Then the same from SQL with ducklake_list_files, the Parquet files on disk with glob, and a direct read_parquet on them. The files are ordinary Parquet; the catalog is what makes them a table.

Part of the free Data Lakes with DuckLake in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 The table in Studio
0:29 The same in SQL
0:58 Files and catalog
1:18 Commit and push
1:46 Recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio

Code for this course (one commit per lesson): https://github.com/Nuri1977/ethereum-ducklake-dbt

Links for this lesson
- DuckLake: list files: https://ducklake.select/docs/stable/duckdb/metadata/list_files

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
```

**Tags**

```text
DuckLake, Parquet, ducklake_list_files, catalog, Rosetta DBT Studio, data lake, lakehouse, DuckDB, dbt, Ethereum, SQL
```

### 12. Lesson 2.4 · Snapshots: every change is a version

**Title** (89 characters)

```text
Snapshots: every change is a version | Data Lakes with DuckLake in Rosetta DBT Studio 2.4
```

**Description**

```text
Every change to a DuckLake is a snapshot. See them in Studio's History tabs and with eth_lake.snapshots(), find the current one, load one more day of blocks and watch a new snapshot appear. Plus transactions and commit messages, which group changes into one snapshot.

Part of the free Data Lakes with DuckLake in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 What a snapshot is
0:19 Snapshots in Studio
0:29 Snapshots in SQL
1:00 Transactions and commit messages
1:23 Commit and push
1:51 Recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio

Code for this course (one commit per lesson): https://github.com/Nuri1977/ethereum-ducklake-dbt

Links for this lesson
- DuckLake: snapshots: https://ducklake.select/docs/stable/duckdb/usage/snapshots

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
```

**Tags**

```text
DuckLake, snapshots, versioning, commit message, Rosetta DBT Studio, data lake, lakehouse, DuckDB, dbt, Parquet, Ethereum, SQL
```

### 13. Lesson 2.5 · Time travel

**Title** (64 characters)

```text
Time travel | Data Lakes with DuckLake in Rosetta DBT Studio 2.5
```

**Description**

```text
Query the lake as it was: AT (VERSION => n) on any table, row counts at different snapshots, a month-by-month view of an old version, and a copy of past data made with CREATE TABLE … AS SELECT … AT. Plus time travel by timestamp, attaching an old snapshot, and what keeping the past costs.

Part of the free Data Lakes with DuckLake in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 Query the past
0:32 Bring the past back
0:50 More ways to travel
1:10 Commit and push
1:37 Recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio

Code for this course (one commit per lesson): https://github.com/Nuri1977/ethereum-ducklake-dbt

Links for this lesson
- DuckLake: time travel: https://ducklake.select/docs/stable/duckdb/usage/time_travel

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
```

**Tags**

```text
DuckLake, time travel, snapshots, AT VERSION, DuckDB, data lake, lakehouse, dbt, Parquet, Ethereum, Rosetta DBT Studio, SQL
```

### 14. Lesson 3.1 · Insert, update, delete, and delete files

**Title** (93 characters)

```text
Insert, update, delete, and delete files | Data Lakes with DuckLake in Rosetta DBT Studio 3.1
```

**Description**

```text
Change data in a lake without rewriting Parquet files: a small working copy of one day of blocks, a DELETE and an UPDATE, and what they leave behind: a delete file that lists row positions, and a new data file for the updated rows. Seen in SQL and in Studio's Data Files tab.

Part of the free Data Lakes with DuckLake in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 Files never change
0:11 A small working copy
0:28 Delete and update
0:56 The same in Studio
1:12 How it works
1:35 Commit and push
2:04 Recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio

Code for this course (one commit per lesson): https://github.com/Nuri1977/ethereum-ducklake-dbt

Links for this lesson
- DuckLake: deletion vectors: https://ducklake.select/docs/stable/duckdb/advanced_features/deletion_vectors

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
```

**Tags**

```text
DuckLake, update, delete, delete files, Parquet, Rosetta DBT Studio, data lake, lakehouse, DuckDB, dbt, Ethereum, SQL
```

### 15. Lesson 3.2 · Daily loads without duplicates

**Title** (83 characters)

```text
Daily loads without duplicates | Data Lakes with DuckLake in Rosetta DBT Studio 3.2
```

**Description**

```text
A daily load you can run twice: insert one day of blocks from S3, but only the blocks the table does not have yet. Run it again and nothing changes, not even a new snapshot. Plus MERGE INTO, the general tool for upserts, which we run live from dbt in Lesson 6.3.

Part of the free Data Lakes with DuckLake in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 The problem
0:17 Insert what is new
1:01 MERGE INTO
1:22 Commit and push
1:50 Recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio

Code for this course (one commit per lesson): https://github.com/Nuri1977/ethereum-ducklake-dbt

Links for this lesson
- DuckLake: upserting: https://ducklake.select/docs/stable/duckdb/usage/upserting

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
```

**Tags**

```text
DuckLake, idempotent load, MERGE, upsert, S3, DuckDB, data lake, lakehouse, dbt, Parquet, Ethereum, Rosetta DBT Studio, SQL
```

### 16. Lesson 3.3 · Schema evolution

**Title** (69 characters)

```text
Schema evolution | Data Lakes with DuckLake in Rosetta DBT Studio 3.3
```

**Description**

```text
Change a table's shape without rewriting a single file: add a column and fill it for one day, rename a column, add a NOT NULL constraint. See the new schema in Studio, and the old one through time travel.

Part of the free Data Lakes with DuckLake in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 Add a column
0:25 Rename and constrain
0:48 The schema in Studio
1:04 How it works
1:26 Commit and push
1:54 Recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio

Code for this course (one commit per lesson): https://github.com/Nuri1977/ethereum-ducklake-dbt

Links for this lesson
- DuckLake: schema evolution: https://ducklake.select/docs/stable/duckdb/usage/schema_evolution
- DuckLake: constraints: https://ducklake.select/docs/stable/duckdb/advanced_features/constraints

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
```

**Tags**

```text
DuckLake, schema evolution, ALTER TABLE, time travel, Rosetta DBT Studio, data lake, lakehouse, DuckDB, dbt, Parquet, Ethereum, SQL
```

### 17. Lesson 3.4 · The data change feed

**Title** (73 characters)

```text
The data change feed | Data Lakes with DuckLake in Rosetta DBT Studio 3.4
```

**Description**

```text
Ask the lake what changed between two snapshots: ducklake_table_changes returns every inserted, deleted and updated row, with the value before and after an update. Plus table_insertions and table_deletions, row ids, and what a change feed is for.

Part of the free Data Lakes with DuckLake in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 What changed?
1:03 How and why
1:25 Commit and push
1:52 Recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio

Code for this course (one commit per lesson): https://github.com/Nuri1977/ethereum-ducklake-dbt

Links for this lesson
- DuckLake: data change feed: https://ducklake.select/docs/stable/duckdb/advanced_features/data_change_feed
- DuckLake: row lineage: https://ducklake.select/docs/stable/duckdb/advanced_features/row_lineage

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
```

**Tags**

```text
DuckLake, change data capture, change feed, row lineage, DuckDB, data lake, lakehouse, dbt, Parquet, Ethereum, Rosetta DBT Studio, SQL
```

### 18. Lesson 3.5 · Transactions and conflicts

**Title** (79 characters)

```text
Transactions and conflicts | Data Lakes with DuckLake in Rosetta DBT Studio 3.5
```

**Description**

```text
ACID in a lake: a transaction that changes two tables commits as one snapshot or not at all. How DuckLake handles two writers with optimistic concurrency, which changes conflict and which do not, and why a DuckDB catalog file means one program at a time.

Part of the free Data Lakes with DuckLake in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 One transaction, many changes
0:22 In Studio's SQL Editor
0:43 Two writers
1:12 One writer at a time
1:34 Recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio

Code for this course (one commit per lesson): https://github.com/Nuri1977/ethereum-ducklake-dbt

Links for this lesson
- DuckLake: transactions: https://ducklake.select/docs/stable/duckdb/advanced_features/transactions
- DuckLake: conflict resolution: https://ducklake.select/docs/stable/duckdb/advanced_features/conflict_resolution

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
```

**Tags**

```text
DuckLake, ACID, transactions, concurrency, conflicts, data lake, lakehouse, DuckDB, dbt, Parquet, Ethereum, Rosetta DBT Studio, SQL
```

### 19. Lesson 4.1 · Partitioning

**Title** (65 characters)

```text
Partitioning | Data Lakes with DuckLake in Rosetta DBT Studio 4.1
```

**Description**

```text
Load the big table the right way: a week of Ethereum transactions, 12.7 million rows from S3, into raw.transactions partitioned by day. See one folder per day on disk, the partition in Studio's table page, and why a query for one day reads one file.

Part of the free Data Lakes with DuckLake in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 Why partition
0:19 Create and load
5:27 One folder per day
6:01 Choosing a key
6:18 Commit and push
6:46 Recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio

Code for this course (one commit per lesson): https://github.com/Nuri1977/ethereum-ducklake-dbt

Links for this lesson
- DuckLake: partitioning: https://ducklake.select/docs/stable/duckdb/advanced_features/partitioning

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
```

**Tags**

```text
DuckLake, partitioning, Parquet, S3, Ethereum transactions, data lake, lakehouse, DuckDB, dbt, Ethereum, Rosetta DBT Studio, SQL
```

### 20. Lesson 4.2 · Statistics and file pruning

**Title** (80 characters)

```text
Statistics and file pruning | Data Lakes with DuckLake in Rosetta DBT Studio 4.2
```

**Description**

```text
DuckLake keeps the min and max of every column for every file in its catalog. See them in Studio's Statistics tab, watch EXPLAIN ANALYZE read one file out of seven for a block-number filter, and keep ranges narrow for new data with SORTED BY. Plus the lake's options.

Part of the free Data Lakes with DuckLake in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 Statistics in the catalog
0:26 Pruning in action
0:57 Keep ranges narrow
1:18 Sorted by, and options
1:36 Commit and push
2:05 Recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio

Code for this course (one commit per lesson): https://github.com/Nuri1977/ethereum-ducklake-dbt

Links for this lesson
- DuckLake: sorted tables: https://ducklake.select/docs/stable/duckdb/advanced_features/sorted_tables
- DuckLake: configuration: https://ducklake.select/docs/stable/duckdb/usage/configuration

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
```

**Tags**

```text
DuckLake, statistics, file pruning, sorted tables, EXPLAIN ANALYZE, data lake, lakehouse, DuckDB, dbt, Parquet, Ethereum, Rosetta DBT Studio, SQL
```

### 21. Lesson 4.3 · Data inlining for small writes

**Title** (83 characters)

```text
Data inlining for small writes | Data Lakes with DuckLake in Rosetta DBT Studio 4.3
```

**Description**

```text
The setting we turned off in Lesson 2.2: with data inlining, small inserts are stored as rows inside the catalog instead of as tiny Parquet files. Create a small watchlist table with inlining on, insert two rows, see that no file appears, then flush them into one Parquet file.

Part of the free Data Lakes with DuckLake in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 The small-file problem
0:23 Inlining on one table
0:58 When to use it
1:14 Commit and push
1:41 Recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio

Code for this course (one commit per lesson): https://github.com/Nuri1977/ethereum-ducklake-dbt

Links for this lesson
- DuckLake: data inlining: https://ducklake.select/docs/stable/duckdb/advanced_features/data_inlining

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
```

**Tags**

```text
DuckLake, data inlining, small files, streaming, DuckDB, data lake, lakehouse, dbt, Parquet, Ethereum, Rosetta DBT Studio, SQL
```

### 22. Lesson 4.4 · Maintenance

**Title** (64 characters)

```text
Maintenance | Data Lakes with DuckLake in Rosetta DBT Studio 4.4
```

**Description**

```text
Keep the lake small and fast: merge small files into bigger ones, expire snapshots you no longer need, clean up files that no snapshot uses, and let CHECKPOINT run it all. Count the files on disk before and after each step.

Part of the free Data Lakes with DuckLake in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 Why maintenance
0:22 Merge
0:53 Expire and clean up
1:33 Careful
1:49 Commit and push
2:17 Recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio

Code for this course (one commit per lesson): https://github.com/Nuri1977/ethereum-ducklake-dbt

Links for this lesson
- DuckLake: recommended maintenance: https://ducklake.select/docs/stable/duckdb/maintenance/recommended_maintenance
- DuckLake: expire snapshots: https://ducklake.select/docs/stable/duckdb/maintenance/expire_snapshots

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
```

**Tags**

```text
DuckLake, maintenance, compaction, expire snapshots, cleanup, CHECKPOINT, data lake, lakehouse, DuckDB, dbt, Parquet, Ethereum, Rosetta DBT Studio, SQL
```

### 23. Lesson 4.5 · Adding existing Parquet files

**Title** (82 characters)

```text
Adding existing Parquet files | Data Lakes with DuckLake in Rosetta DBT Studio 4.5
```

**Description**

```text
Register a Parquet file that already exists without copying it: write one day of blocks to a landing folder with COPY, in the table's current shape, then attach it to raw.blocks with ducklake_add_data_files. The file now belongs to the lake.

Part of the free Data Lakes with DuckLake in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 Why add files
0:14 A file in a landing folder
0:39 Register it
1:10 Careful
1:30 Commit and push
1:55 Recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio

Code for this course (one commit per lesson): https://github.com/Nuri1977/ethereum-ducklake-dbt

Links for this lesson
- DuckLake: adding files: https://ducklake.select/docs/stable/duckdb/metadata/adding_files

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
```

**Tags**

```text
DuckLake, ducklake_add_data_files, Parquet, COPY, migration, data lake, lakehouse, DuckDB, dbt, Ethereum, Rosetta DBT Studio, SQL
```

### 24. Lesson 5.1 · Inside the catalog: snapshots, tables, columns

**Title** (99 characters)

```text
Inside the catalog: snapshots, tables, columns | Data Lakes with DuckLake in Rosetta DBT Studio 5.1
```

**Description**

```text
The catalog is an ordinary DuckDB database, attached next to the lake. Open its tables from the SQL Editor: ducklake_snapshot and ducklake_snapshot_changes, ducklake_table, and ducklake_column, where the column renamed in Lesson 3.3 shows up as two rows. Versioning is two columns on every row: begin_snapshot and end_snapshot.

Part of the free Data Lakes with DuckLake in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 The catalog is a database
0:27 Snapshots and changes
0:49 Tables and columns
1:17 The pattern
1:30 Commit and push
1:58 Recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio

Code for this course (one commit per lesson): https://github.com/Nuri1977/ethereum-ducklake-dbt

Links for this lesson
- DuckLake specification: tables: https://ducklake.select/docs/stable/specification/tables/overview

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
```

**Tags**

```text
DuckLake, catalog, metadata, specification, snapshots, data lake, lakehouse, DuckDB, dbt, Parquet, Ethereum, Rosetta DBT Studio, SQL
```

### 25. Lesson 5.2 · Inside the catalog: files and statistics

**Title** (93 characters)

```text
Inside the catalog: files and statistics | Data Lakes with DuckLake in Rosetta DBT Studio 5.2
```

**Description**

```text
The catalog's file tables: ducklake_data_file with the path and row count of every file, ducklake_file_column_stats with the min and max that made pruning work in 4.2, ducklake_file_partition_value from 4.1, table statistics, and the inlined rows table from 4.3.

Part of the free Data Lakes with DuckLake in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 Data files
0:17 Statistics per file
0:34 Partitions, table stats, inlined rows
1:03 The file tables
1:15 Commit and push
1:43 Recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio

Code for this course (one commit per lesson): https://github.com/Nuri1977/ethereum-ducklake-dbt

Links for this lesson
- DuckLake specification: tables: https://ducklake.select/docs/stable/specification/tables/overview

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
```

**Tags**

```text
DuckLake, catalog, file statistics, partitions, specification, data lake, lakehouse, DuckDB, dbt, Parquet, Ethereum, Rosetta DBT Studio, SQL
```

### 26. Lesson 5.3 · Read the lake by hand

**Title** (74 characters)

```text
Read the lake by hand | Data Lakes with DuckLake in Rosetta DBT Studio 5.3
```

**Description**

```text
No magic: answer a query with only the catalog tables and read_parquet. Find the current snapshot, the table, the data path, the files valid at that snapshot, read exactly those files, and get the same count as the lake. This is what any engine must do to read DuckLake.

Part of the free Data Lakes with DuckLake in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 The recipe
0:17 Step by step
0:58 Read the files
1:15 Why it matters
1:29 Commit and push
1:57 Recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio

Code for this course (one commit per lesson): https://github.com/Nuri1977/ethereum-ducklake-dbt

Links for this lesson
- DuckLake specification: queries: https://ducklake.select/docs/stable/specification/queries

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
```

**Tags**

```text
DuckLake, specification, catalog, read_parquet, DuckDB, data lake, lakehouse, dbt, Parquet, Ethereum, Rosetta DBT Studio, SQL
```

### 27. Lesson 6.1 · Connect a dbt project to the lake

**Title** (86 characters)

```text
Connect a dbt project to the lake | Data Lakes with DuckLake in Rosetta DBT Studio 6.1
```

**Description**

```text
Point the ethereum_lake dbt project at the DuckLake: a profiles.yml that attaches the lake and makes it dbt's database, checked with dbt debug. Then the one rule for this module, seen live: while Studio has the lake open, dbt cannot open it.

Part of the free Data Lakes with DuckLake in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 dbt on the lake
0:22 The profile
1:08 Commit and push
1:26 One program at a time
1:50 The rule
2:10 Recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio

Code for this course (one commit per lesson): https://github.com/Nuri1977/ethereum-ducklake-dbt

Links for this lesson
- dbt-duckdb: attaching databases: https://github.com/duckdb/dbt-duckdb#attaching-additional-databases
- DuckLake: connecting: https://ducklake.select/docs/stable/duckdb/usage/connecting

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
```

**Tags**

```text
dbt, DuckLake, dbt-duckdb, profiles.yml, Rosetta DBT Studio, data lake, lakehouse, DuckDB, Parquet, Ethereum, SQL
```

### 28. Lesson 6.2 · Staging models for blocks and transactions

**Title** (95 characters)

```text
Staging models for blocks and transactions | Data Lakes with DuckLake in Rosetta DBT Studio 6.2
```

**Description**

```text
Declare the lake's raw tables as dbt sources, and build two staging views on them: stg_blocks with clear names, gas used in percent and the base fee in gwei, and stg_transactions with values and fees in ether and a success flag. Run them with dbt, look at the rows with dbt show, then see the views in Studio's Data Lake screens.

Part of the free Data Lakes with DuckLake in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 Sources
0:15 stg_blocks
0:31 stg_transactions
0:42 Run and look
1:06 Views in a lake
1:18 The views in Studio
1:28 Commit and push
1:46 Recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio

Code for this course (one commit per lesson): https://github.com/Nuri1977/ethereum-ducklake-dbt

Links for this lesson
- dbt: sources: https://docs.getdbt.com/docs/build/sources
- DuckLake: views: https://ducklake.select/docs/stable/specification/tables/ducklake_view

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
```

**Tags**

```text
dbt, staging models, sources, DuckLake, views, Ethereum, data lake, lakehouse, DuckDB, Parquet, Rosetta DBT Studio, SQL
```

### 29. Lesson 6.3 · Marts, built incrementally

**Title** (79 characters)

```text
Marts, built incrementally | Data Lakes with DuckLake in Rosetta DBT Studio 6.3
```

**Description**

```text
Three marts on the lake: daily_network_activity and top_senders as tables, and daily_gas as an incremental model with the merge strategy, which runs a real MERGE INTO on the lake, plus a post-hook that writes a commit message. Run dbt twice, read the compiled MERGE, and find dbt's snapshots and commit message in Studio's History.

Part of the free Data Lakes with DuckLake in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 Two table marts
0:25 An incremental merge
0:43 Run, twice
1:29 dbt's snapshots
1:42 Commit and push
2:00 Recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio

Code for this course (one commit per lesson): https://github.com/Nuri1977/ethereum-ducklake-dbt

Links for this lesson
- dbt: incremental models: https://docs.getdbt.com/docs/build/incremental-models
- DuckLake: snapshots and commit messages: https://ducklake.select/docs/stable/duckdb/usage/snapshots

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
```

**Tags**

```text
dbt, incremental models, MERGE, DuckLake, commit message, marts, data lake, lakehouse, DuckDB, Parquet, Ethereum, Rosetta DBT Studio, SQL
```

### 30. Lesson 6.4 · Tests and docs on the lake

**Title** (79 characters)

```text
Tests and docs on the lake | Data Lakes with DuckLake in Rosetta DBT Studio 6.4
```

**Description**

```text
DuckLake does not enforce unique keys, so dbt tests check them: a schema.yml with descriptions, unique and not_null on the keys, accepted_values on the success flag, and a relationship from transactions to blocks. dbt build runs 5 models and 9 tests on the lake; then the docs site with the lineage from the raw tables to the marts.

Part of the free Data Lakes with DuckLake in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 Why tests
0:17 schema.yml
0:32 dbt build
0:47 Docs
1:05 The lineage
1:26 Commit and push
1:41 Recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio

Code for this course (one commit per lesson): https://github.com/Nuri1977/ethereum-ducklake-dbt

Links for this lesson
- dbt: data tests: https://docs.getdbt.com/docs/build/data-tests
- DuckLake: unsupported features: https://ducklake.select/docs/stable/duckdb/unsupported_features

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
```

**Tags**

```text
dbt tests, dbt docs, lineage, DuckLake, data quality, data lake, lakehouse, DuckDB, dbt, Parquet, Ethereum, Rosetta DBT Studio, SQL
```

### 31. Lesson 7.1 · Going further, and recap

**Title** (77 characters)

```text
Going further, and recap | Data Lakes with DuckLake in Rosetta DBT Studio 7.1
```

**Description**

```text
Where to go from a laptop lake: a shared lake with a PostgreSQL catalog and object storage, access control, backups, encryption, moving an existing DuckDB database, and what DuckLake does not do yet. Then a recap of the whole course.

Part of the free Data Lakes with DuckLake in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 A shared lake
0:37 Running it for real
1:04 Not yet
1:16 Course recap

Screens from Rosetta DBT Studio 1.7.6.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio

Code for this course (one commit per lesson): https://github.com/Nuri1977/ethereum-ducklake-dbt

Links for this lesson
- DuckLake documentation: https://ducklake.select/docs/stable/
- DuckLake: choosing a catalog database: https://ducklake.select/docs/stable/duckdb/usage/choosing_a_catalog_database
- Course code: https://github.com/Nuri1977/ethereum-ducklake-dbt

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
```

**Tags**

```text
DuckLake, PostgreSQL catalog, S3, data lake, recap, lakehouse, DuckDB, dbt, Parquet, Ethereum, Rosetta DBT Studio, SQL
```
