# Install Rosetta DBT Studio — voice-over script and beat sheet

dbt + DuckDB in Rosetta DBT Studio · Module 1 · Set up · next: Lesson 2.1 · Create the dbt project

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `fresh-install`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 1 · Lesson 1.1. Install Rosetta DBT Studio. Badges: version 1.7.6, Mac · Windows · Linux, about 5 minutes.

## s01 · slide — slide `toolkit`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | In this lesson, you install Rosetta DBT Studio, the one app we use for the whole course. You download it, copy it to your computer, and its first-run setup installs Python and dbt Core for you. | Statement: One app. It installs Python and dbt Core for you. Three steps: download, copy, first-run setup. | 37 | 13 |

## s02 · browser — Browser

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b02 @0:16 | Studio is open source, and every version is published on GitHub. Open the releases page of rosettadb, dbt-studio. The latest release is 1.7.6. | Browser: open https://github.com/rosettadb/dbt-studio/releases/tag/1.7.6<br>Zoom: center-wide<br>Card: *Download page* — **github.com/rosettadb/dbt-studio/releases** — Latest: 1.7.6 | 26 | 12 |
| b03 @0:28 | Scroll down to Assets. There is a build for every system: a dmg for Mac, an exe for Windows, and deb, rpm and flatpak packages for Linux. | Scroll to **Assets**<br>Point at **.deb**<br>Point at **.exe**<br>Zoom: center-wide | 27 | 11 |
| b04 @0:39 | On a Mac, pick the dmg for your processor: arm64 for Apple silicon, x64 for Intel. This Mac has an Intel chip, so click the x64 dmg. | Point at **arm64.dmg**<br>Click the download link **x64.dmg**<br>Zoom: center-wide<br>Card: *This Mac: Intel* — **The x64 .dmg, 196 MB** — Apple silicon Macs: the arm64 .dmg (187 MB). | 27 | 12 |

## s03 · slide — slide `dmg`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b05 @0:52 | When the download finishes, open the file. A window shows the app on the left, and your Applications folder on the right. | The Rosetta Studio disk window (the release's own background): the app icon on the left, Applications on the right. | 22 | 8 |
| b06 @0:59 | Drag Rosetta DBT Studio onto Applications, and wait for the copy to finish. | A cursor drags the app icon along the INSTALL arrow onto Applications. | 13 | 6 |
| b07 @1:05 | Then open it from Applications. The first time, macOS asks whether you want to open an app downloaded from the internet. Click Open. | Prompt card: Rosetta DBT Studio is an app downloaded from the internet. Are you sure you want to open it? Open is highlighted. | 23 | 9 |

## s04 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b08 @1:15 | Studio starts with a short setup. First, the dbt version. Choose dbt 1.x, the recommended one. | Click **dbt 1.x**<br>Zoom: setup | 17 | 8 |
| b09 @1:23 | Then the exact version. Keep the latest, 1.12.6. | Click **1.12.6 latest**<br>Zoom: setup | 10 | 5 |
| b10 @1:28 | Next, the adapters, one for each database dbt can talk to. This course only needs DuckDB, so uncheck the others, keep dbt-duckdb, and click Continue. | Uncheck dbt-postgres, dbt-snowflake, dbt-bigquery, dbt-redshift, dbt-databricks, dbt-kinetica<br>Check dbt-duckdb<br>Click **Continue**<br>Zoom: setup<br>Card: *Adapters* — **Only dbt-duckdb** — You can add others later in Settings. | 26 | 12 |
| b11 @1:39 | Skip the optional tools, and click Install. | Click **Continue**<br>Click **Install** | 7 | 3 |
| b12 @1:43 | Studio downloads its own copy of Python, then installs dbt Core and the DuckDB adapter, all inside its own folder. Here it took about a minute and a half; the video speeds it up. | Wait until **Finish** is enabled (sped up)<br>Zoom: setup<br>Card: *Sped up* — **About 90 seconds** — Python 3.10.17, then dbt Core 1.12.6 + dbt-duckdb | 34 | 13 |
| b13 @1:55 | Python 3.10.17, and dbt 1.12.6 with one adapter. Click Finish. | Click **Finish**<br>Studio opens its main window | 14 | 9 |

## s05 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b14 @2:04 | This is Studio's home screen, the Workspace Overview. No projects yet: we create the first one in Module 2. | — | 19 | 7 |
| b15 @2:11 | The status bar at the bottom shows what was installed: dbt 1.12.6, Python 3.10.17, and DuckDB. | Point at **dbt: 1.12.6**<br>Zoom: statusbar | 20 | 11 |
| b16 @2:22 | At the top right are New Connection, Open Project, and Settings. That is all we need for now. | Point at **New Connection**<br>Point at **Open Project**<br>Point at **Settings**<br>Zoom: home-header | 18 | 6 |

## s06 · slide — slide `installed`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b17 @2:28 | To recap: you installed one app. Studio set up its own Python and dbt Core, with the DuckDB adapter, inside its own folder. You did not install Python or dbt yourself. | Rosetta DBT Studio 1.7.6 in Applications; in Studio's own folder: Python 3.10.17 and dbt Core 1.12.6 with dbt-duckdb. | 31 | 13 |
| b18 @2:41 | Next, we create the dbt project, and connect it to a repository on GitHub. | Next: create the dbt project and connect it to GitHub. | 14 | 6 |

## s07 · closing card (4 s, no voice)

Next · Lesson 2.1 · Create the dbt project.

**Total: 385 spoken words, 2:51 rendered.**
