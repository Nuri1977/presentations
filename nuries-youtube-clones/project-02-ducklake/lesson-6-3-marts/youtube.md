# YouTube upload: Marts, built incrementally

- **File:** `lesson-6-3.mp4` (3840x2160, 2:19). Upload the 4K file; YouTube shows HD and 4K only after processing finishes, which can take from minutes to an hour, so the first view may look blurry.
- **Visibility:** unlisted (embedded only in Academy)
- **Captions:** upload `lesson-6-3.srt` (English)
- **Thumbnail:** `thumbnail.png` (1280x720)
- **End screen / cards:** none

## Title

Marts, built incrementally | Data Lakes with DuckLake in Rosetta DBT Studio 6.3

## Description

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

## Tags

dbt, incremental models, MERGE, DuckLake, commit message, marts, data lake, lakehouse, DuckDB, Parquet, Ethereum, Rosetta DBT Studio, SQL
