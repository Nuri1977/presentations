# YouTube upload: Adding existing Parquet files

- **File:** `lesson-4-5.mp4` (3840x2160, 2:11). Upload the 4K file; YouTube shows HD and 4K only after processing finishes, which can take from minutes to an hour, so the first view may look blurry.
- **Visibility:** unlisted (embedded only in Academy)
- **Captions:** upload `lesson-4-5.srt` (English)
- **Thumbnail:** `thumbnail.png` (1280x720)
- **End screen / cards:** none

## Title

Adding existing Parquet files | Data Lakes with DuckLake in Rosetta DBT Studio 4.5

## Description

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

## Tags

DuckLake, ducklake_add_data_files, Parquet, COPY, migration, data lake, lakehouse, DuckDB, dbt, Ethereum, Rosetta DBT Studio, SQL
