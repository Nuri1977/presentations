# Connect a dbt project to the lake — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `lesson-5-3-end`: Studio freshly opened; the lake is registered but not opened yet.

## s02 · The profile

| Listen for | Do this |
|---|---|
| "In DBT Studio, open profiles dot yml. Today…" | In the left bar, click **DBT Studio**<br>In the Explorer, open `profiles.yml` (expand each folder on the way) |
| "Replace the output. Path is a small local…" | paste: {'replace': True, 'text': 'ethereum_lake:\n  target: dev\n  outputs:\n    dev:\n      type: duckdb\n      path: lake/dbt_session.duckdb\n      attach:\n        - path: "ducklake:lake/eth_catalog.duckdb"\n          alias: eth_lake\n      database: eth_lake\n      schema: main\n      threads: 1\n'}<br>Click **Save** (top right of the editor)<br>(Check that `profiles.yml` matches `../snippets/6.1/profiles.yml`) |
| "Check it: in the command box under the…" | Click the command box under the terminal, type `dbt debug`, press Enter |

## s03 · Commit and push

| Listen for | Do this |
|---|---|
| "Commit the profile: point dbt at the lake.…" | Close the editor tab for `profiles.yml` (its ×)<br>Click the **Git** tab at the top of the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Click the message box and type: Point dbt at the lake<br>Click **Commit**<br>git_push: None |

## s04 · One program at a time

| Listen for | Do this |
|---|---|
| "Now the rule for this module. Open Data…" | In the left bar, click **DataLake**<br>Click **eth_lake** |
| "Back in DBT Studio, run dbt debug again.…" | In the left bar, click **DBT Studio**<br>Click the command box under the terminal, type `dbt debug`, press Enter |
