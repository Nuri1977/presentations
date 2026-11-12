# YouTube upload: full course (Project 1)

- **File:** `project-1-full-course.mp4` (3840x2160, 35:12, 506 MB). The 12 lesson videos joined in order, without re-encoding.
- **Phone copy:** `project-1-full-course-1080p.mp4` (1920x1080, 119 MB)
- **Captions:** `project-1-full-course.srt` (English, 430 lines, times shifted per lesson)
- **Thumbnail:** use `../lesson-0-welcome/thumbnail.png`
- **Visibility:** unlisted

## Title

dbt + DuckDB Full Course: NYC taxi project in Rosetta DBT Studio (Project 1)

## Description

The whole of Project 1 in one video: build a dbt + DuckDB project on the 2025 NYC green taxi trips in Rosetta DBT Studio, from installing the app to a tested pipeline with CI, live docs and a published warehouse.

Part of the free dbt + DuckDB in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/
Code for this course (one commit per lesson): https://github.com/Nuri1977/nyc-taxi-dbt
Docs site built in the course: https://nuri1977.github.io/nyc-taxi-dbt/

Chapters
0:00 0 Welcome: build a dbt + DuckDB project
3:00 1.1 Install Rosetta DBT Studio
5:52 2.1 Create the dbt project
9:32 2.2 Get the data
12:50 2.3 Models: your first dbt model
16:32 2.4 Dependencies & Jinja
19:55 2.5 Properties: describe your models
22:42 2.6 Docs & the DAG
25:15 2.7 Materializations: views and tables
27:18 2.8 Tests: trust your data
29:51 3.1 Ship & Automate: CI with GitHub Actions
33:05 3.2 Showcase: docs site, README and a public warehouse

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio
Lesson order inspired by Luke Barousse's dbt course: https://www.youtube.com/watch?v=1Bf049kXV2g

Data
- TLC Trip Record Data: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
- Taxi zone lookup (CSV): https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
- Git and GitHub Explained in 7 Minutes: https://www.youtube.com/watch?v=y-an0v208A0
- Learn GitHub without needing the terminal: https://www.youtube.com/watch?v=2SgI1kAczfk

## Tags

dbt full course, dbt tutorial, dbt, dbt core, DuckDB, analytics engineering, Rosetta DBT Studio, NYC taxi, SQL, GitHub Actions, dbt docs, dbt tests

## Detailed chapters (optional: replace the chapter list above)

Each lesson's own chapters, with times in the full video.

0 Welcome: build a dbt + DuckDB project
  0:00 Welcome
  0:18 What you will build
  0:55 The data
  1:30 The tools
  1:53 The course repository
  2:17 The course map

1.1 Install Rosetta DBT Studio
  3:00 One app for the whole course
  3:16 Download the release
  3:52 Copy it to Applications
  4:15 First-run setup
  5:04 The home screen
  5:28 What was installed

2.1 Create the dbt project
  5:52 What a dbt project is
  6:18 Where Studio keeps Python and dbt
  6:45 A DuckDB connection
  7:08 Create the project
  7:44 Check the setup with dbt debug
  8:00 Files that keep git clean
  8:21 A repository on GitHub
  8:39 First commit and push
  9:12 Recap

2.2 Get the data
  9:32 Sources and seeds
  10:05 Download the files
  10:24 Put the files in the project
  10:49 Load the files into DuckDB
  11:36 Declare the source
  11:59 Commit and push
  12:31 Recap

2.3 Models: your first dbt model
  12:50 What a model is
  13:15 Write trips.sql in Rosetta DBT Studio
  14:09 How dbt runs a model
  14:32 Run the model
  14:46 Preview the rows
  15:15 The SQL dbt wrote, and the run history
  15:41 Commit the model
  16:12 Recap

2.4 Dependencies & Jinja
  16:32 Load the seed
  16:51 ref(): models that build on models
  17:11 Trips per month
  17:34 Top pickup zones, with a Jinja variable
  18:02 Jinja in one minute
  18:18 Compile: see the plain SQL
  18:43 Run in dependency order
  19:16 Commit and push
  19:34 Recap

2.5 Properties: describe your models
  19:55 What properties are
  20:17 schema.yml and seeds.yml
  21:03 Keep the descriptions in the database
  21:28 Descriptions inside DuckDB
  22:01 Commit and push
  22:23 Recap

2.6 Docs & the DAG
  22:42 A model with two refs
  23:22 The DAG
  23:39 Run a model and everything upstream
  23:53 Generate and serve the docs
  24:13 The docs site
  24:34 Commit and push
  24:53 Recap

2.7 Materializations: views and tables
  25:15 View or table?
  25:44 One line for the whole project
  25:58 Keep trips a view
  26:10 Run and check
  26:41 Commit and push
  27:01 Recap

2.8 Tests: trust your data
  27:18 What a data test is
  27:42 Add tests in YAML
  28:16 Run the tests
  28:42 Fix and test one model
  29:12 Commit and push
  29:30 Recap

3.1 Ship & Automate: CI with GitHub Actions
  29:51 Dev, prod and CI
  30:14 Four files
  31:40 The workflow, step by step
  32:00 Commit and push
  32:19 The run on GitHub
  32:47 Recap

3.2 Showcase: docs site, README and a public warehouse
  33:05 A portfolio project
  33:26 Docs in the workflow, and a README
  33:55 Commit and push
  34:13 Live on GitHub
  34:33 Query the warehouse from anywhere
  34:51 Project 1 recap
