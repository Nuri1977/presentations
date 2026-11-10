# Welcome: build a dbt + DuckDB project — voice-over script and beat sheet

dbt + DuckDB in Rosetta DBT Studio · Welcome · next: Lesson 1.1 · Install Rosetta DBT Studio

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `none (slides only)`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Lesson 0 · Welcome. Build a dbt + DuckDB project. Project 1 · NYC taxi trips. Badges: Rosetta DBT Studio, dbt Core, DuckDB, GitHub.

## s01 · slide — slide `welcome`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | Welcome to Project 1. In this course, you build a real analytics project with dbt and DuckDB. You start from an empty folder, and finish with a tested, automated pipeline, all inside Rosetta DBT Studio. | Big statement: From raw files to a tested, automated pipeline. Under it: Rosetta DBT Studio · dbt Core · DuckDB · GitHub. | 35 | 15 |

## s02 · slide — slide `build`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b02 @0:18 | We start with a full year of New York City green taxi trips: twelve monthly parquet files, and a small lookup table of taxi zones. | Left column of the DAG: 12 parquet files (2025 green taxi trips) and taxi_zone_lookup.csv. | 25 | 9 |
| b03 @0:27 | dbt turns the raw files into one clean model of trips. | An arrow to the model trips (view): one clean row per trip. | 11 | 5 |
| b04 @0:32 | On top of it, three small tables: trips per month and borough, the busiest pickup zones, and a monthly summary of how riders pay. | Three tables appear: trips_per_month, top_pickup_zones, monthly_summary. | 24 | 9 |
| b05 @0:41 | We add tests that catch bad data, and documentation with a lineage graph. | Badges under the tables: tests, docs and lineage. | 13 | 5 |
| b06 @0:46 | Finally, GitHub Actions rebuilds everything on every change, and publishes the finished DuckDB database, so anyone can query it. | Right column: GitHub Actions builds on every change and publishes prod.duckdb; label: anyone can query it. | 19 | 9 |

## s03 · slide — slide `data`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b07 @0:55 | The data comes from the New York City Taxi and Limousine Commission, the TLC. Every trip has its pickup and drop-off time, the pickup and drop-off zones, the distance, how the rider paid, and what it cost. | Trip card: the columns we use, pickup and drop-off time, zones, distance, payment type, fare, tip, total. Source: NYC TLC Trip Record Data. | 39 | 13 |
| b08 @1:08 | For 2025, that is about five hundred ninety thousand trips, in twelve files of about one megabyte each. Small enough to build on a laptop in seconds. | Big numbers: 12 files · 14.5 MB · 591,375 trips (2025, as of 9 Nov 2026). | 27 | 11 |
| b09 @1:19 | A second file maps every zone number to its name and borough. Zone seventy-four, for example, is East Harlem North, in Manhattan, the busiest pickup zone of the year. | Zone card: taxi_zone_lookup.csv, 265 zones; example row 74 · East Harlem North · Manhattan; joined on the pickup zone. | 30 | 11 |

## s04 · slide — slide `tools`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b10 @1:30 | You need one app: Rosetta DBT Studio. It is open source, it installs Python and dbt Core for you, and it gives you an editor, a terminal, lineage, and git, in one window. | Rosetta DBT Studio card: one app with editor, terminal, lineage and git; installs Python and dbt Core for you; open source. | 33 | 12 |
| b11 @1:42 | DuckDB is the database. It lives in a single file on your computer, so there is no server to set up. And GitHub keeps your code, and later runs the pipeline for you. | DuckDB card: a database in one file, no server. GitHub card: keeps the code, runs the pipeline. | 33 | 11 |

## s05 · slide — slide `repo`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b12 @1:53 | The whole project lives in one public repository on GitHub. We create it in lesson 2.1, and every lesson ends with a commit and a push. | The repository github.com/Nuri1977/nyc-taxi-dbt, public: a commit list, one commit per lesson (Create the nyc_taxi dbt project, Get the data, Models, ...). | 27 | 10 |
| b13 @2:03 | So each lesson's commit is the code for that lesson. The link to the repository is in every video description. | One commit opened: models/trips.sql added, green lines. Label: Code for this lesson. | 20 | 7 |
| b14 @2:11 | Build your own copy as you watch. And if you get stuck, compare it with the course repository. | Two columns: your repo, built as you watch; the course repo, the answer key. | 18 | 6 |

## s06 · slide — slide `map`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b15 @2:17 | The course has three modules. First, set up: install Rosetta DBT Studio. | Module 1 · Set up: 1.1 Install Rosetta DBT Studio. | 12 | 6 |
| b16 @2:23 | Second, dbt basics: create the project and connect it to GitHub, get the data, then models, Jinja, properties, docs, materializations, and tests. | Module 2 · dbt basics: 2.1 Create the project to 2.8 Tests. | 22 | 11 |
| b17 @2:34 | Third, ship it: automate the build with GitHub Actions, and turn the repository into a portfolio project. | Module 3 · Ship it: 3.1 Ship & Automate, 3.2 Showcase. | 17 | 8 |
| b18 @2:42 | You need a computer, a GitHub account and the basics of git, and some basic SQL. No dbt installed yet: we start from zero. New to git? There are links in the description. See you in the first lesson. | What you need: a computer (Mac, Windows or Linux), a GitHub account and the basics of git, basic SQL. No dbt installed: we start from zero. | 39 | 14 |

## s07 · closing card (4 s, no voice)

Next · Lesson 1.1 · Install Rosetta DBT Studio.

**Total: 444 spoken words, 3:00 rendered.**
