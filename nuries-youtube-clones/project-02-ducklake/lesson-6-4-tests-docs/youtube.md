# YouTube upload: Tests and docs on the lake

- **File:** `lesson-6-4.mp4` (3840x2160, 2:02). Upload the 4K file; YouTube shows HD and 4K only after processing finishes, which can take from minutes to an hour, so the first view may look blurry.
- **Visibility:** unlisted (embedded only in Academy)
- **Captions:** upload `lesson-6-4.srt` (English)
- **Thumbnail:** `thumbnail.png` (1280x720)
- **End screen / cards:** none

## Title

Tests and docs on the lake | Data Lakes with DuckLake in Rosetta DBT Studio 6.4

## Description

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

## Tags

dbt tests, dbt docs, lineage, DuckLake, data quality, data lake, lakehouse, DuckDB, dbt, Parquet, Ethereum, Rosetta DBT Studio, SQL
