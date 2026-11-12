# Install Rosetta DBT Studio from rosettadb.io — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `fresh-install`: empty Studio profile, no Python or dbt runtime.

## s01 · The download page

| Listen for | Do this |
|---|---|
| "Rosetta DBT Studio is free and open source.…" | In the browser, open https://rosettadb.io/<br>Point at **Download Now**<br>Click **Download Now** |
| "The download page has a card for each…" | Scroll to **Download cards** |
| "On Windows, take the E X E installer.…" | Point at **.exe**<br>Point at **.deb**<br>Point at **Mac ARM64**<br>Click the download link **Mac Intel** |

## s03 · First-run setup

| Listen for | Do this |
|---|---|
| "Studio starts with a short setup. First, the…" | Click **dbt 1.x** |
| "Then the exact version. Keep the latest, 1.12.6.…" | Click **1.12.6 latest** |
| "Next, the adapters. For this course we only…" | Uncheck dbt-postgres, dbt-snowflake, dbt-bigquery, dbt-redshift, dbt-databricks, dbt-kinetica<br>Check dbt-duckdb<br>Click **Continue** |
| "Skip the optional tools, and click Install.…" | Click **Continue**<br>Click **Install** |
| "Studio downloads its own Python, then installs dbt…" | Wait until **Finish** is enabled (this takes a while) |
| "Done: Python 3.10.17, and dbt 1.12.6. Click Finish.…" | Click **Finish**<br>Studio opens its main window |

## s04 · The home screen

| Listen for | Do this |
|---|---|
| "This is Studio's home screen. Among the modules…" | Point at **Data Lake** |
| "The status bar shows what was installed: dbt,…" | Point at **dbt: 1.12.6**<br>Point at **DuckDB version** |
