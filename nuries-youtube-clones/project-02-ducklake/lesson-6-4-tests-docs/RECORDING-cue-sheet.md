# Tests and docs on the lake — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `lesson-6-3-end`: staging and marts in the project (not built in the lake yet: dbt build builds them); Studio freshly opened.

## s02 · schema.yml

| Listen for | Do this |
|---|---|
| "In models, create schema dot yml. Descriptions for…" | In the left bar, click **DBT Studio**<br>Right-click `models` → **New File**, type `schema.yml`, click **Save**<br>paste: {'text': "models:\n  - name: stg_blocks\n    description: One row per Ethereum block, with clear names and units.\n    columns:\n      - name: block_number\n        description: The block's height in the chain.\n        data_tests:\n          - unique\n          - not_null\n  - name: stg_transactions\n    description: One row per transaction, with values and fees in ether.\n    columns:\n      - name: transaction_hash\n        data_tests:\n          - not_null\n      - name: block_number\n        data_tests:\n          - relationships:\n              arguments:\n                to: ref('stg_blocks')\n                field: block_number\n      - name: succeeded\n        data_tests:\n          - accepted_values:\n              arguments:\n                values: [true, false]\n                quote: false\n  - name: daily_network_activity\n    description: One row per day with blocks, transactions, gas use and the average base fee.\n    columns:\n      - name: block_date\n        data_tests:\n          - unique\n          - not_null\n  - name: daily_gas\n    description: One row per day with transaction fees; built incrementally with a merge.\n    columns:\n      - name: block_date\n        data_tests:\n          - unique\n          - not_null\n"}<br>Click **Save** (top right of the editor)<br>(Check that `models/schema.yml` matches `../snippets/6.4/schema.yml`) |

## s03 · dbt build

| Listen for | Do this |
|---|---|
| "Run dbt build: it builds every model in…" | Close the editor tab for `models/schema.yml` (its ×)<br>Click the command box under the terminal, type `dbt build`, press Enter |

## s04 · Docs

| Listen for | Do this |
|---|---|
| "Now the docs. Project menu, Generate Docs. dbt…" | Open the **Project** menu (arrow next to Project, top right) → **Generate Docs**<br>Wait for “Catalog written” |
| "Then Project, Serve Docs. Studio starts a local…" | Open the **Project** menu (arrow next to Project, top right) → **Serve Docs**<br>Wait for “Serving docs at” |

## s05 · The lineage

| Listen for | Do this |
|---|---|
| "Open it in the browser, on the daily…" | In the browser, open http://127.0.0.1:8080/#!/model/model.ethereum_lake.daily_gas |
| "And the lineage graph for this model: daily…" | Click **View Lineage Graph** |

## s06 · Commit and push

| Listen for | Do this |
|---|---|
| "Commit the tests and descriptions, and push.…" | Click the **Git** tab at the top of the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Click the message box and type: Tests and docs<br>Click **Commit**<br>git_push: None |
