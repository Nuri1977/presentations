# YouTube upload: Data inlining for small writes

- **File:** `lesson-4-3.mp4` (3840x2160, 1:58). Upload the 4K file; YouTube shows HD and 4K only after processing finishes, which can take from minutes to an hour, so the first view may look blurry.
- **Visibility:** unlisted (embedded only in Academy)
- **Captions:** upload `lesson-4-3.srt` (English)
- **Thumbnail:** `thumbnail.png` (1280x720)
- **End screen / cards:** none

## Title

Data inlining for small writes | Data Lakes with DuckLake in Rosetta DBT Studio 4.3

## Description

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

## Tags

DuckLake, data inlining, small files, streaming, DuckDB, data lake, lakehouse, dbt, Parquet, Ethereum, Rosetta DBT Studio, SQL
