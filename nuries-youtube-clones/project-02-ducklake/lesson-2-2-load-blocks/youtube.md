# YouTube upload: Load three months of blocks from S3

- **File:** `lesson-2-2.mp4` (3840x2160, 3:33). Upload the 4K file; YouTube shows HD and 4K only after processing finishes, which can take from minutes to an hour, so the first view may look blurry.
- **Visibility:** unlisted (embedded only in Academy)
- **Captions:** upload `lesson-2-2.srt` (English)
- **Thumbnail:** `thumbnail.png` (1280x720)
- **End screen / cards:** none

## Title

Load three months of blocks from S3 | Data Lakes with DuckLake in Rosetta DBT Studio 2.2

## Description

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

## Tags

DuckLake, S3, Parquet, DuckDB, SQL Editor, Ethereum, data lake, lakehouse, dbt, Rosetta DBT Studio, SQL
