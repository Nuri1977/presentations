# YouTube upload: Dependencies & Jinja

- **File:** `lesson-2-4.mp4` (3840x2160, 3:23). Upload the 4K file; YouTube shows HD and 4K only after processing finishes, which can take from minutes to an hour, so the first view may look blurry.
- **Visibility:** unlisted (embedded only in Academy)
- **Captions:** upload `lesson-2-4.srt` (English)
- **Thumbnail:** `thumbnail.png` (1280x720)
- **End screen / cards:** none

## Title

Dependencies & Jinja | dbt + DuckDB in Rosetta DBT Studio 2.4

## Description

Load the taxi zone lookup seed, then build two models on top of trips with ref(): trips per month and borough, and the ten busiest pickup zones, using a Jinja variable. Compile to see the plain SQL dbt sends to DuckDB, run the project in dependency order, then commit and push. All dbt commands from Rosetta DBT Studio's Project and Model menus.

Part of the free dbt + DuckDB in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 Load the seed
0:19 ref(): models that build on models
0:39 Trips per month
1:02 Top pickup zones, with a Jinja variable
1:30 Jinja in one minute
1:46 Compile: see the plain SQL
2:11 Run in dependency order
2:44 Commit and push
3:02 Recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio
Lesson order inspired by Luke Barousse's dbt course: https://www.youtube.com/watch?v=1Bf049kXV2g

Code for this course (one commit per lesson): https://github.com/Nuri1977/nyc-taxi-dbt

## Tags

dbt ref, Jinja, dbt seed, dbt compile, dependencies, DuckDB, NYC taxi, dbt, dbt core, analytics engineering, Rosetta DBT Studio, SQL
