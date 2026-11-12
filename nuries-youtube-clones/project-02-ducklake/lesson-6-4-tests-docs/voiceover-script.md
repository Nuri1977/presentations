# Tests and docs on the lake — voice-over script and beat sheet

Data Lakes with DuckLake in Rosetta DBT Studio · Module 6 · dbt on DuckLake · next: Lesson 7.1 · Going further, and recap

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `lesson-6-3-end`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 2 · Lesson 6.4. Tests and docs on the lake.

## s01 · slide — slide `why`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | A DuckLake supports not null, but no primary keys, no unique constraints, and no foreign keys. Nothing stops a duplicate block from getting in. | DuckLake: NOT NULL yes; primary keys, unique, foreign keys no. | 24 | 10 |
| b02 @0:12 | So we check those rules with dbt tests, every time we build. | dbt tests check them after each build. | 12 | 5 |

## s02 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b03 @0:17 | In models, create schema dot yml. Descriptions for the models, unique and not null on the keys, accepted values on the success flag, and a relationship: every transaction's block number must exist in stg blocks. | Left bar → **DBT Studio**<br>Right-click `models` → **New File** → `schema.yml` → **Save**<br>paste: {'text': "models:\n  - name: stg_blocks\n    description: One row per Ethereum block, with clear names and units.\n    columns:\n      - name: block_number\n        description: The block's height in the chain.\n        data_tests:\n          - unique\n          - not_null\n  - name: stg_transactions\n    description: One row per transaction, with values and fees in ether.\n    columns:\n      - name: transaction_hash\n        data_tests:\n          - not_null\n      - name: block_number\n        data_tests:\n          - relationships:\n              arguments:\n                to: ref('stg_blocks')\n                field: block_number\n      - name: succeeded\n        data_tests:\n          - accepted_values:\n              arguments:\n                values: [true, false]\n                quote: false\n  - name: daily_network_activity\n    description: One row per day with blocks, transactions, gas use and the average base fee.\n    columns:\n      - name: block_date\n        data_tests:\n          - unique\n          - not_null\n  - name: daily_gas\n    description: One row per day with transaction fees; built incrementally with a merge.\n    columns:\n      - name: block_date\n        data_tests:\n          - unique\n          - not_null\n"}<br>Click **Save**<br>(check: `models/schema.yml` equals `../snippets/6.4/schema.yml`)<br>Zoom: code-mid | 35 | 15 |

## s03 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b04 @0:32 | Run dbt build: it builds every model in order, and runs each model's tests right after it. Five models and nine tests: fourteen passes in all. | Close the editor tab for `models/schema.yml`<br>In the command box under the terminal, type `dbt build` and press Enter<br>Zoom: terminal-close<br>Card: *dbt build* — **PASS=14** — 5 models + 9 tests, on the lake | 26 | 14 |

## s04 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b05 @0:47 | Now the docs. Project menu, Generate Docs. dbt reads the project and the lake, and writes a small website into target. | Open the **Project** menu → **Generate Docs**<br>Wait for “Catalog written” | 21 | 11 |
| b06 @0:58 | Then Project, Serve Docs. Studio starts a local web server, on port eighty eighty. | Open the **Project** menu → **Serve Docs**<br>Wait for “Serving docs at” | 14 | 7 |

## s05 · browser — Browser

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b07 @1:05 | Open it in the browser, on the daily gas model: its description, and its columns. | Browser: open http://127.0.0.1:8080/#!/model/model.ethereum_lake.daily_gas<br>Zoom: center-wide | 15 | 6 |
| b08 @1:11 | And the lineage graph for this model: daily gas is built from stg transactions, the staging view on the raw transactions table. The full graph of the project, from both raw tables to all three marts, opens with the button at the top. | Click **View Lineage Graph** | 43 | 15 |

## s06 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b09 @1:26 | Commit the tests and descriptions, and push. | Open the **Git** tab in the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Type the commit message “Tests and docs”<br>Click **Commit**<br>git_push: None<br>Zoom: git-panel | 7 | 15 |

## s07 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b10 @1:41 | To recap: the lake does not enforce unique keys, so dbt tests do, and dbt build runs them with every model. And the docs show each model, its columns and tests, and its lineage. That ends Module 6. One lesson left: where to go from here. | Recap: the lake does not enforce uniqueness; dbt tests do; dbt build = models + tests; docs and lineage. | 46 | 17 |

## s08 · closing card (4 s, no voice)

Next · Lesson 7.1 · Going further.

**Total: 243 spoken words, 2:02 rendered.**
