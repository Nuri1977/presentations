# Install Rosetta DBT Studio — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `fresh-install`: Studio 1.7.6 launched with an empty profile (no Python, no dbt, no projects), so its first-run setup appears.
- The browser scene opens the 1.7.6 release page directly.

## s02 · Download the release

| Listen for | Do this |
|---|---|
| "Studio is open source, and every version is…" | In the browser, open https://github.com/rosettadb/dbt-studio/releases/tag/1.7.6 |
| "Scroll down to Assets. There is a build…" | Scroll to **Assets**<br>Point at **.deb**<br>Point at **.exe** |
| "On a Mac, pick the dmg for your…" | Point at **arm64.dmg**<br>Click the download link **x64.dmg** |

## s04 · First-run setup

| Listen for | Do this |
|---|---|
| "Studio starts with a short setup. First, the…" | Click **dbt 1.x** |
| "Then the exact version. Keep the latest, 1.12.6.…" | Click **1.12.6 latest** |
| "Next, the adapters, one for each database dbt…" | Uncheck dbt-postgres, dbt-snowflake, dbt-bigquery, dbt-redshift, dbt-databricks, dbt-kinetica<br>Check dbt-duckdb<br>Click **Continue** |
| "Skip the optional tools, and click Install.…" | Click **Continue**<br>Click **Install** |
| "Studio downloads its own copy of Python, then…" | Wait until **Finish** is enabled (this takes a while) |
| "Python 3.10.17, and dbt 1.12.6 with one adapter.…" | Click **Finish**<br>Studio opens its main window |

## s05 · The home screen

| Listen for | Do this |
|---|---|
| "This is Studio's home screen, the Workspace Overview.…" | Hold; nothing moves |
| "The status bar at the bottom shows what…" | Point at **dbt: 1.12.6** |
| "At the top right are New Connection, Open…" | Point at **New Connection**<br>Point at **Open Project**<br>Point at **Settings** |
