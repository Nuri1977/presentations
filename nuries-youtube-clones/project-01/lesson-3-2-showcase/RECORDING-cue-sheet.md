# Showcase: docs site, README and a public warehouse — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `lesson-3-1-end`: a clone of what Lesson 3.1 pushed (CI workflow), the parquet files in data/raw, the nyc_taxi_dev connection, and the database after dbt build (off camera).
- Rehearsal repo made public by Nuri on 10 Nov 2026 for this lesson; Final run on the public Nuri1977/nyc-taxi-dbt; Pages Source is switched to GitHub Actions on camera.

## s02 · Turn on GitHub Pages

| Listen for | Do this |
|---|---|
| "On GitHub, open the repository's Settings, then Pages.…" | In the browser, open https://github.com/Nuri1977/nyc-taxi-dbt/settings/pages<br>Click **Source**<br>Click **GitHub Actions** |

## s03 · Docs in the workflow, and a README

| Listen for | Do this |
|---|---|
| "In Studio, open the workflow file, and paste…" | On the home screen, click **nyc_taxi** under Recent Projects<br>In the Explorer, open `.github/workflows/dbt_build.yml` (expand each folder on the way)<br>paste: {'text': '      - run: dbt docs generate --profiles-dir ci\n      - run: mkdir site && cp target/index.html target/manifest.json target/catalog.json site/\n      - uses: actions/upload-pages-artifact@v5\n        with:\n          path: site\n  docs:\n    needs: build\n    runs-on: ubuntu-latest\n    permissions:\n      pages: write\n      id-token: write\n    environment:\n      name: github-pages\n      url: ${{ steps.deploy.outputs.page_url }}\n    steps:\n      - id: deploy\n        uses: actions/deploy-pages@v5\n', 'end': True} |
| "And a second job, docs, that runs after…" | Click **Save** (top right of the editor)<br>(Check that `.github/workflows/dbt_build.yml` matches `../snippets/3.2/dbt_build.yml`) |
| "Now the README. Open it, select all, and…" | Close the editor tab for `.github/workflows/dbt_build.yml` (its ×)<br>In the Explorer, open `README.md` (expand each folder on the way)<br>paste: {'replace': True, 'text': "# NYC taxi dbt project\n\n[![dbt build & publish](https://github.com/Nuri1977/nyc-taxi-dbt/actions/workflows/dbt_build.yml/badge.svg)](https://github.com/Nuri1977/nyc-taxi-dbt/actions/workflows/dbt_build.yml)\n[![docs](https://img.shields.io/badge/docs-live-ff7a1a)](https://nuri1977.github.io/nyc-taxi-dbt/)\n\nA dbt + DuckDB project on the NYC TLC green taxi trips of 2025, built in Rosetta DBT Studio.\nGitHub Actions builds and tests it on every push, publishes the warehouse, and deploys the docs.\n\n| What | How | Where to look |\n|---|---|---|\n| Pipeline | raw table → `trips` view → three mart tables | `models/` |\n| Tests | unique, not_null, accepted_values | `models/schema.yml`, `seeds/seeds.yml` |\n| Docs | dbt docs, lineage graph | [docs site](https://nuri1977.github.io/nyc-taxi-dbt/) |\n| CI | `dbt build` on every push and every Monday | `.github/workflows/dbt_build.yml` |\n| Environments | dev in Studio, prod in CI | `profiles.yml`, `ci/profiles.yml` |\n| Warehouse | `prod.duckdb`, a release asset | [Releases](https://github.com/Nuri1977/nyc-taxi-dbt/releases/tag/warehouse) |\n\n## Query the warehouse\n\nIn the DuckDB CLI or any DuckDB client:\n\n```sql\ninstall httpfs; load httpfs;\nattach 'https://github.com/Nuri1977/nyc-taxi-dbt/releases/download/warehouse/prod.duckdb' as taxi (read_only);\nselect * from taxi.main.top_pickup_zones;\n```\n\nThe file holds the raw trips, the `trips` view and the three mart tables.\n\n## Run it yourself\n\nOpen the folder in [Rosetta DBT Studio](https://rosettadb.io/download-dbtstudio.html), or:\n\n```bash\npip install -r requirements.txt\npython scripts/download_data.py\ndbt build\n```\n\n## Data\n\nNYC Taxi & Limousine Commission trip records: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page\n\nCourse: dbt + DuckDB in Rosetta DBT Studio, Project 1. One commit per lesson.\n"}<br>Click **Save** (top right of the editor)<br>(Check that `README.md` matches `../snippets/3.2/README.md`) |

## s04 · Commit and push

| Listen for | Do this |
|---|---|
| "Git tab: stage all, type a message, publish…" | Close the editor tab for `README.md` (its ×)<br>Click the **Git** tab at the top of the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Click the message box and type: Publish docs and README<br>Click **Commit** |
| "Sync Changes. The push starts the workflow.…" | git_push: None |

## s05 · Live on GitHub

| Listen for | Do this |
|---|---|
| "On GitHub, the Actions tab shows the run,…" | In the browser, open https://github.com/Nuri1977/nyc-taxi-dbt/actions<br>Wait for “Publish docs and README”<br>Click **the run** |
| "A minute later, both are green.…" | Wait for “^Success$” |
| "The docs are live on GitHub Pages, for…" | In the browser, open https://nuri1977.github.io/nyc-taxi-dbt/<br>Click **View Lineage Graph** |
| "And the repository page shows the README, with…" | In the browser, open https://github.com/Nuri1977/nyc-taxi-dbt<br>Scroll to **NYC taxi dbt project** |
