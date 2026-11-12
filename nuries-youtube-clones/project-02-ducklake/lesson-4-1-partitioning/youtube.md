# YouTube upload: Partitioning

- **File:** `lesson-4-1.mp4` (3840x2160, 7:03). Upload the 4K file; YouTube shows HD and 4K only after processing finishes, which can take from minutes to an hour, so the first view may look blurry.
- **Visibility:** unlisted (embedded only in Academy)
- **Captions:** upload `lesson-4-1.srt` (English)
- **Thumbnail:** `thumbnail.png` (1280x720)
- **End screen / cards:** none

## Title

Partitioning | Data Lakes with DuckLake in Rosetta DBT Studio 4.1

## Description

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

## Tags

DuckLake, partitioning, Parquet, S3, Ethereum transactions, data lake, lakehouse, DuckDB, dbt, Ethereum, Rosetta DBT Studio, SQL
