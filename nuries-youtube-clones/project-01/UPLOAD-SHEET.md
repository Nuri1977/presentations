# Upload sheet: dbt + DuckDB in Rosetta DBT Studio

Project 1: NYC taxi trips, from raw files to a tested, automated pipeline

- **Playlist:** dbt + DuckDB in Rosetta DBT Studio: Project 1
- **Videos:** 12, 35:12 in total. Upload in the order below.
- **Visibility:** unlisted (embedded in Rosetta Academy: https://academy.rosettadb.io/)
- **Code repo:** https://github.com/Nuri1977/nyc-taxi-dbt (public, `main` at `5d54490`, one commit per lesson from 2.1)
- **Docs site:** https://nuri1977.github.io/nyc-taxi-dbt/
- **Checked on 11 Nov 2026:** every 4K file is 3840x2160 H.264 level 5.1 and every 1080p copy is 1920x1080 level 4.0; durations match the timelines; each lesson folder has captions (`.srt`, `.vtt`), `thumbnail.png`, slides (`.pptx`) and `youtube.md`.

## Before you upload

- **Listen once** to each video for pronunciation. Claude cannot hear audio.
- Upload the **4K** file to YouTube with its `.srt`. Share the **1080p** copy in chat or by phone.
- YouTube shows HD and 4K only after processing, so the first view may look blurry.
- Lessons 2.1–3.2 were recorded before the UI-zoom change; GitHub pages in 3.1 and 3.2 have small text.
- Studio 1.7.6 shows timestamp columns as `[object Object]` in Preview; the videos scroll past them (2.3).

## Files

| # | Lesson | Title | Length | 4K file (upload this) | Captions | Thumbnail |
|---|---|---|---|---|---|---|
| 1 | 0 | Welcome: build a dbt + DuckDB project | 3:00 | `lesson-0-welcome/lesson-0.mp4` (44 MB) | `lesson-0.srt` | `thumbnail.png` |
| 2 | 1.1 | Install Rosetta DBT Studio | 2:51 | `lesson-1-1-install/lesson-1-1.mp4` (47 MB) | `lesson-1-1.srt` | `thumbnail.png` |
| 3 | 2.1 | Create the dbt project | 3:39 | `lesson-2-1-create-project/lesson-2-1.mp4` (43 MB) | `lesson-2-1.srt` | `thumbnail.png` |
| 4 | 2.2 | Get the data | 3:17 | `lesson-2-2-get-data/lesson-2-2.mp4` (37 MB) | `lesson-2-2.srt` | `thumbnail.png` |
| 5 | 2.3 | Models: your first dbt model | 3:42 | `lesson-2-3-models/lesson-2-3.mp4` (51 MB) | `lesson-2-3.srt` | `thumbnail.png` |
| 6 | 2.4 | Dependencies & Jinja | 3:23 | `lesson-2-4-jinja/lesson-2-4.mp4` (43 MB) | `lesson-2-4.srt` | `thumbnail.png` |
| 7 | 2.5 | Properties: describe your models | 2:46 | `lesson-2-5-properties/lesson-2-5.mp4` (43 MB) | `lesson-2-5.srt` | `thumbnail.png` |
| 8 | 2.6 | Docs & the DAG | 2:32 | `lesson-2-6-docs-dag/lesson-2-6.mp4` (38 MB) | `lesson-2-6.srt` | `thumbnail.png` |
| 9 | 2.7 | Materializations: views and tables | 2:03 | `lesson-2-7-materializations/lesson-2-7.mp4` (34 MB) | `lesson-2-7.srt` | `thumbnail.png` |
| 10 | 2.8 | Tests: trust your data | 2:32 | `lesson-2-8-tests/lesson-2-8.mp4` (44 MB) | `lesson-2-8.srt` | `thumbnail.png` |
| 11 | 3.1 | Ship & Automate: CI with GitHub Actions | 3:13 | `lesson-3-1-ship-automate/lesson-3-1.mp4` (43 MB) | `lesson-3-1.srt` | `thumbnail.png` |
| 12 | 3.2 | Showcase: docs site, README and a public warehouse | 2:07 | `lesson-3-2-showcase/lesson-3-2.mp4` (38 MB) | `lesson-3-2.srt` | `thumbnail.png` |

Captions and thumbnails sit in the same lesson folder as the video.

## Titles, descriptions and tags

Copy each block as is. Chapters are inside the descriptions.

### 1. Lesson 0 · Welcome: build a dbt + DuckDB project

**Title** (76 characters)

```text
Welcome: build a dbt + DuckDB project | dbt + DuckDB in Rosetta DBT Studio 0
```

**Description**

```text
Welcome to Project 1. Build a real analytics project with dbt and DuckDB in Rosetta DBT Studio: a year of NYC green taxi trips, from raw parquet files to clean models, tests, docs, and a GitHub Actions pipeline that publishes a warehouse anyone can query. This lesson shows what you will build, the data, the tools, and how to use the course repository: one commit per lesson.

Part of the free dbt + DuckDB in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 Welcome
0:18 What you will build
0:55 The data
1:30 The tools
1:53 The course repository
2:17 The course map

Screens from Rosetta DBT Studio 1.7.6.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio
Lesson order inspired by Luke Barousse's dbt course: https://www.youtube.com/watch?v=1Bf049kXV2g

Code for this course (one commit per lesson): https://github.com/Nuri1977/nyc-taxi-dbt

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
- Git and GitHub Explained in 7 Minutes: https://www.youtube.com/watch?v=y-an0v208A0
- Learn GitHub without needing the terminal: https://www.youtube.com/watch?v=2SgI1kAczfk
```

**Tags**

```text
dbt course, dbt tutorial, DuckDB, NYC taxi, analytics engineering, GitHub, dbt, dbt core, Rosetta DBT Studio, SQL
```

### 2. Lesson 1.1 · Install Rosetta DBT Studio

**Title** (67 characters)

```text
Install Rosetta DBT Studio | dbt + DuckDB in Rosetta DBT Studio 1.1
```

**Description**

```text
Install Rosetta DBT Studio 1.7.6, the one app used for the whole course. Download it from the GitHub release page, copy it to Applications, and let its first-run setup install Python and dbt Core with the DuckDB adapter. No Python or dbt to install yourself.

Part of the free dbt + DuckDB in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 One app for the whole course
0:16 Download the release
0:52 Copy it to Applications
1:15 First-run setup
2:04 The home screen
2:28 What was installed

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio
Lesson order inspired by Luke Barousse's dbt course: https://www.youtube.com/watch?v=1Bf049kXV2g

Code for this course (one commit per lesson): https://github.com/Nuri1977/nyc-taxi-dbt
```

**Tags**

```text
install dbt, Rosetta DBT Studio, dbt Core, DuckDB, Mac, dbt, dbt core, analytics engineering, NYC taxi, SQL
```

### 3. Lesson 2.1 · Create the dbt project

**Title** (63 characters)

```text
Create the dbt project | dbt + DuckDB in Rosetta DBT Studio 2.1
```

**Description**

```text
Create the nyc_taxi dbt project in Rosetta DBT Studio: a DuckDB connection, Studio's project template, dbt_project.yml and profiles.yml, and dbt debug. Then create a public GitHub repository and push the first commit from Studio's Git tab. Git and GitHub basics are assumed; links for beginners are below.

Part of the free dbt + DuckDB in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 What a dbt project is
0:26 Where Studio keeps Python and dbt
0:53 A DuckDB connection
1:16 Create the project
1:52 Check the setup with dbt debug
2:08 Files that keep git clean
2:29 A repository on GitHub
2:47 First commit and push
3:20 Recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio
Lesson order inspired by Luke Barousse's dbt course: https://www.youtube.com/watch?v=1Bf049kXV2g

Code for this course (one commit per lesson): https://github.com/Nuri1977/nyc-taxi-dbt

New to git and GitHub? Start here (free videos):
- Git and GitHub for Beginners - Crash Course (freeCodeCamp): https://www.youtube.com/watch?v=RGOj5yH7evk
- Git Tutorial for Beginners: Learn Git in 1 Hour (Programming with Mosh): https://www.youtube.com/watch?v=8JJ101D3knE
- Git and GitHub Explained in 7 Minutes: https://www.youtube.com/watch?v=y-an0v208A0
- Learn GitHub without needing the terminal: https://www.youtube.com/watch?v=2SgI1kAczfk
```

**Tags**

```text
dbt project, dbt_project.yml, profiles.yml, dbt debug, DuckDB, GitHub, dbt, dbt core, analytics engineering, Rosetta DBT Studio, NYC taxi, SQL
```

### 4. Lesson 2.2 · Get the data

**Title** (53 characters)

```text
Get the data | dbt + DuckDB in Rosetta DBT Studio 2.2
```

**Description**

```text
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
```

**Tags**

```text
dbt sources, dbt seeds, sources.yml, parquet, DuckDB, SQL Editor, NYC taxi, dbt, dbt core, analytics engineering, Rosetta DBT Studio, SQL
```

### 5. Lesson 2.3 · Models: your first dbt model

**Title** (69 characters)

```text
Models: your first dbt model | dbt + DuckDB in Rosetta DBT Studio 2.3
```

**Description**

```text
Build the first dbt model of the NYC taxi project: trips.sql, one select over the raw 2025 green taxi parquet files. Run it from the Model menu in Rosetta DBT Studio, preview the rows, read the compiled SQL, check the run history, then commit and push the model from Studio's Git tab.

Part of the free dbt + DuckDB in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 What a model is
0:25 Write trips.sql in Rosetta DBT Studio
1:19 How dbt runs a model
1:42 Run the model
1:56 Preview the rows
2:25 The SQL dbt wrote, and the run history
2:51 Commit the model
3:22 Recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio
Lesson order inspired by Luke Barousse's dbt course: https://www.youtube.com/watch?v=1Bf049kXV2g

Code for this course (one commit per lesson): https://github.com/Nuri1977/nyc-taxi-dbt
```

**Tags**

```text
dbt models, dbt run, preview, compiled SQL, DuckDB, NYC taxi, dbt, dbt core, analytics engineering, Rosetta DBT Studio, SQL
```

### 6. Lesson 2.4 · Dependencies & Jinja

**Title** (61 characters)

```text
Dependencies & Jinja | dbt + DuckDB in Rosetta DBT Studio 2.4
```

**Description**

```text
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
```

**Tags**

```text
dbt ref, Jinja, dbt seed, dbt compile, dependencies, DuckDB, NYC taxi, dbt, dbt core, analytics engineering, Rosetta DBT Studio, SQL
```

### 7. Lesson 2.5 · Properties: describe your models

**Title** (73 characters)

```text
Properties: describe your models | dbt + DuckDB in Rosetta DBT Studio 2.5
```

**Description**

```text
Describe the nyc_taxi models and the zone seed with properties: models/schema.yml and seeds/seeds.yml. Turn on persist_docs in dbt_project.yml, run the project from Rosetta DBT Studio's Project menu, and see the descriptions as comments inside DuckDB in Studio's SQL Editor. Then commit and push.

Part of the free dbt + DuckDB in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 What properties are
0:22 schema.yml and seeds.yml
1:08 Keep the descriptions in the database
1:33 Descriptions inside DuckDB
2:06 Commit and push
2:28 Recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio
Lesson order inspired by Luke Barousse's dbt course: https://www.youtube.com/watch?v=1Bf049kXV2g

Code for this course (one commit per lesson): https://github.com/Nuri1977/nyc-taxi-dbt
```

**Tags**

```text
dbt properties, schema.yml, persist_docs, documentation, DuckDB, NYC taxi, dbt, dbt core, analytics engineering, Rosetta DBT Studio, SQL
```

### 8. Lesson 2.6 · Docs & the DAG

**Title** (55 characters)

```text
Docs & the DAG | dbt + DuckDB in Rosetta DBT Studio 2.6
```

**Description**

```text
Add monthly_summary, a model with two refs, and describe it. Learn what the DAG is, run the model with everything upstream from Rosetta DBT Studio's Model menu, then generate and serve the dbt docs site: model pages, column descriptions and the lineage graph. Commit and push.

Part of the free dbt + DuckDB in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 A model with two refs
0:40 The DAG
0:57 Run a model and everything upstream
1:11 Generate and serve the docs
1:31 The docs site
1:52 Commit and push
2:11 Recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio
Lesson order inspired by Luke Barousse's dbt course: https://www.youtube.com/watch?v=1Bf049kXV2g

Code for this course (one commit per lesson): https://github.com/Nuri1977/nyc-taxi-dbt
```

**Tags**

```text
dbt docs, DAG, lineage, ref, documentation, DuckDB, NYC taxi, dbt, dbt core, analytics engineering, Rosetta DBT Studio, SQL
```

### 9. Lesson 2.7 · Materializations: views and tables

**Title** (75 characters)

```text
Materializations: views and tables | dbt + DuckDB in Rosetta DBT Studio 2.7
```

**Description**

```text
Views or tables? Make the three marts of the nyc_taxi project tables with one line in dbt_project.yml, keep trips a view with a config block, run the project from Rosetta DBT Studio's Project menu, and check the result in information_schema in Studio's SQL Editor. Commit and push.

Part of the free dbt + DuckDB in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 View or table?
0:29 One line for the whole project
0:43 Keep trips a view
0:55 Run and check
1:26 Commit and push
1:46 Recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio
Lesson order inspired by Luke Barousse's dbt course: https://www.youtube.com/watch?v=1Bf049kXV2g

Code for this course (one commit per lesson): https://github.com/Nuri1977/nyc-taxi-dbt
```

**Tags**

```text
dbt materializations, view, table, dbt_project.yml, config, DuckDB, NYC taxi, dbt, dbt core, analytics engineering, Rosetta DBT Studio, SQL
```

### 10. Lesson 2.8 · Tests: trust your data

**Title** (63 characters)

```text
Tests: trust your data | dbt + DuckDB in Rosetta DBT Studio 2.8
```

**Description**

```text
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
```

**Tags**

```text
dbt tests, data tests, unique, not_null, accepted_values, dbt build, NYC taxi, dbt, dbt core, DuckDB, analytics engineering, Rosetta DBT Studio, SQL
```

### 11. Lesson 3.1 · Ship & Automate: CI with GitHub Actions

**Title** (80 characters)

```text
Ship & Automate: CI with GitHub Actions | dbt + DuckDB in Rosetta DBT Studio 3.1
```

**Description**

```text
Add continuous integration to the nyc_taxi dbt project: a prod profile, pinned requirements, a script that downloads the TLC files, and a GitHub Actions workflow that runs dbt build on every push and publishes the DuckDB warehouse as a release asset. Created in Rosetta DBT Studio, pushed from its Git tab, and checked on GitHub.

Part of the free dbt + DuckDB in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 Dev, prod and CI
0:23 Four files
1:49 The workflow, step by step
2:09 Commit and push
2:28 The run on GitHub
2:56 Recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio
Lesson order inspired by Luke Barousse's dbt course: https://www.youtube.com/watch?v=1Bf049kXV2g

Code for this course (one commit per lesson): https://github.com/Nuri1977/nyc-taxi-dbt
```

**Tags**

```text
GitHub Actions, CI, dbt build, prod target, DuckDB, NYC taxi, dbt, dbt core, analytics engineering, Rosetta DBT Studio, SQL
```

### 12. Lesson 3.2 · Showcase: docs site, README and a public warehouse

**Title** (91 characters)

```text
Showcase: docs site, README and a public warehouse | dbt + DuckDB in Rosetta DBT Studio 3.2
```

**Description**

```text
Turn the nyc_taxi dbt project into a portfolio piece: deploy the dbt docs to GitHub Pages from the CI workflow, write a README with a build badge, and see how anyone can query the published DuckDB warehouse straight from the GitHub release.

Part of the free dbt + DuckDB in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/

Chapters
0:00 A portfolio project
0:21 Docs in the workflow, and a README
0:50 Commit and push
1:08 Live on GitHub
1:28 Query the warehouse from anywhere
1:46 Project 1 recap

Recorded in Rosetta DBT Studio 1.7.6 with dbt Core 1.12.6 and dbt-duckdb 1.11.1.
Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html
Source code: https://github.com/rosettadb/dbt-studio
Lesson order inspired by Luke Barousse's dbt course: https://www.youtube.com/watch?v=1Bf049kXV2g

Code for this course (one commit per lesson): https://github.com/Nuri1977/nyc-taxi-dbt
```

**Tags**

```text
GitHub Pages, dbt docs, README, DuckDB, httpfs, portfolio, NYC taxi, dbt, dbt core, analytics engineering, Rosetta DBT Studio, SQL
```
