# YouTube upload: Get the data

- **File:** `lesson-2-2.mp4` (3840x2160, 3:17). Upload the 4K file; YouTube shows HD and 4K only after processing finishes, which can take from minutes to an hour, so the first view may look blurry.
- **Visibility:** unlisted (embedded only in Academy)
- **Captions:** upload `lesson-2-2.srt` (English)
- **Thumbnail:** `thumbnail.png` (1280x720)
- **End screen / cards:** none

## Title

Get the data | dbt + DuckDB in Rosetta DBT Studio 2.2

## Description

Bring the NYC TLC green taxi data for 2025 into the nyc_taxi dbt project: twelve parquet files in data/raw (kept out of git), loaded once into a DuckDB table raw.green_trips from Rosetta DBT Studio's SQL Editor; the taxi zone lookup CSV as a seed; and a sources.yml that declares raw.green_trips. Then commit and push from Studio's Git tab.

Part of the free dbt + DuckDB in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 Sources and seeds
0:33 Download the files
0:52 Put the files in the project
1:17 Load the files into DuckDB
2:04 Declare the source
2:27 Commit and push
2:59 Recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio
Lesson order inspired by Luke Barousse's dbt course: https://www.youtube.com/watch?v=1Bf049kXV2g

Code for this course (one commit per lesson): https://github.com/Nuri1977/nyc-taxi-dbt

Links for this lesson
- TLC Trip Record Data (download page): https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
- Green taxi files, 2025 (January; change 01 to 02 … 12): https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-01.parquet
- Taxi zone lookup (CSV): https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv

## Tags

dbt sources, dbt seeds, sources.yml, parquet, DuckDB, SQL Editor, NYC taxi, dbt, dbt core, analytics engineering, Rosetta DBT Studio, SQL
