# YouTube upload: Tests: trust your data

- **File:** `lesson-2-8.mp4` (3840x2160, 2:32). Upload the 4K file; YouTube shows HD and 4K only after processing finishes, which can take from minutes to an hour, so the first view may look blurry.
- **Visibility:** unlisted (embedded only in Academy)
- **Captions:** upload `lesson-2-8.srt` (English)
- **Thumbnail:** `thumbnail.png` (1280x720)
- **End screen / cards:** none

## Title

Tests: trust your data | dbt + DuckDB in Rosetta DBT Studio 2.8

## Description

Add data tests to the nyc_taxi project: not_null and unique on each table's grain, and accepted_values on the borough. Run them from Rosetta DBT Studio's Project menu, read a real failure (the N/A borough of zone 265, Outside of NYC), fix it, test one model from the Model menu, then dbt build: run and test in DAG order. Commit and push.

Part of the free dbt + DuckDB in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 What a data test is
0:24 Add tests in YAML
0:58 Run the tests
1:24 Fix and test one model
1:54 Commit and push
2:12 Recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio
Lesson order inspired by Luke Barousse's dbt course: https://www.youtube.com/watch?v=1Bf049kXV2g

Code for this course (one commit per lesson): https://github.com/Nuri1977/nyc-taxi-dbt

## Tags

dbt tests, data tests, unique, not_null, accepted_values, dbt build, NYC taxi, dbt, dbt core, DuckDB, analytics engineering, Rosetta DBT Studio, SQL
