# YouTube upload: Daily loads without duplicates

- **File:** `lesson-3-2.mp4` (3840x2160, 2:08). Upload the 4K file; YouTube shows HD and 4K only after processing finishes, which can take from minutes to an hour, so the first view may look blurry.
- **Visibility:** unlisted (embedded only in Academy)
- **Captions:** upload `lesson-3-2.srt` (English)
- **Thumbnail:** `thumbnail.png` (1280x720)
- **End screen / cards:** none

## Title

Daily loads without duplicates | Data Lakes with DuckLake in Rosetta DBT Studio 3.2

## Description

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

## Tags

DuckLake, idempotent load, MERGE, upsert, S3, DuckDB, data lake, lakehouse, dbt, Parquet, Ethereum, Rosetta DBT Studio, SQL
