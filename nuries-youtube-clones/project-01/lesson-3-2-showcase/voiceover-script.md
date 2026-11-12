# Showcase: docs site, README and a public warehouse — voice-over script and beat sheet

dbt + DuckDB in Rosetta DBT Studio · Module 3 · Ship it · next: Project 1 complete

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `lesson-3-1-end`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 1 · Lesson 3.2. Showcase. Badges: GitHub Pages, README, public warehouse.

## s01 · slide — slide `portfolio`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | Last step: make the project easy to show. A README that explains it, live docs, a green build badge, and a warehouse anyone can query. | A portfolio project: a README that explains it, live docs, a green build badge, data anyone can query. | 25 | 9 |

## s02 · browser — Browser

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b02 @0:12 | On GitHub, open the repository's Settings, then Pages. Under Source, choose GitHub Actions, so our workflow can publish the docs. | Browser: open https://github.com/Nuri1977/nyc-taxi-dbt/settings/pages<br>Click **Source**<br>Click **GitHub Actions**<br>Zoom: center-wide | 20 | 9 |

## s03 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b03 @0:21 | In Studio, open the workflow file, and paste three more build steps at the end: generate the docs, copy the site files, and upload them for Pages. | Open project **nyc_taxi** from Recent Projects<br>Open `.github/workflows/dbt_build.yml` in the Explorer<br>paste: {'text': '      - run: dbt docs generate --profiles-dir ci\n      - run: mkdir site && cp target/index.html target/manifest.json target/catalog.json site/\n      - uses: actions/upload-pages-artifact@v5\n        with:\n          path: site\n  docs:\n    needs: build\n    runs-on: ubuntu-latest\n    permissions:\n      pages: write\n      id-token: write\n    environment:\n      name: github-pages\n      url: ${{ steps.deploy.outputs.page_url }}\n    steps:\n      - id: deploy\n        uses: actions/deploy-pages@v5\n', 'end': True}<br>Zoom: code-mid | 27 | 10 |
| b04 @0:31 | And a second job, docs, that runs after build and deploys the site. Save. | Click **Save**<br>(check: `.github/workflows/dbt_build.yml` equals `../snippets/3.2/dbt_build.yml`)<br>Zoom: code-mid | 14 | 6 |
| b05 @0:37 | Now the README. Open it, select all, and paste the new one: a build badge, a docs link, what the project does and where to look, how to query the warehouse, and how to run it yourself. Save. | Close the editor tab for `.github/workflows/dbt_build.yml`<br>Open `README.md` in the Explorer<br>paste: {'replace': True, 'text': "# NYC taxi dbt project\n\n[![dbt build & publish](https://github.com/Nuri1977/nyc-taxi-dbt/actions/workflows/dbt_build.yml/badge.svg)](https://github.com/Nuri1977/nyc-taxi-dbt/actions/workflows/dbt_build.yml)\n[![docs](https://img.shields.io/badge/docs-live-ff7a1a)](https://nuri1977.github.io/nyc-taxi-dbt/)\n\nA dbt + DuckDB project on the NYC TLC green taxi trips of 2025, built in Rosetta DBT Studio.\nGitHub Actions builds and tests it on every push, publishes the warehouse, and deploys the docs.\n\n| What | How | Where to look |\n|---|---|---|\n| Pipeline | raw table → `trips` view → three mart tables | `models/` |\n| Tests | unique, not_null, accepted_values | `models/schema.yml`, `seeds/seeds.yml` |\n| Docs | dbt docs, lineage graph | [docs site](https://nuri1977.github.io/nyc-taxi-dbt/) |\n| CI | `dbt build` on every push and every Monday | `.github/workflows/dbt_build.yml` |\n| Environments | dev in Studio, prod in CI | `profiles.yml`, `ci/profiles.yml` |\n| Warehouse | `prod.duckdb`, a release asset | [Releases](https://github.com/Nuri1977/nyc-taxi-dbt/releases/tag/warehouse) |\n\n## Query the warehouse\n\nIn the DuckDB CLI or any DuckDB client:\n\n```sql\ninstall httpfs; load httpfs;\nattach 'https://github.com/Nuri1977/nyc-taxi-dbt/releases/download/warehouse/prod.duckdb' as taxi (read_only);\nselect * from taxi.main.top_pickup_zones;\n```\n\nThe file holds the raw trips, the `trips` view and the three mart tables.\n\n## Run it yourself\n\nOpen the folder in [Rosetta DBT Studio](https://rosettadb.io/download-dbtstudio.html), or:\n\n```bash\npip install -r requirements.txt\npython scripts/download_data.py\ndbt build\n```\n\n## Data\n\nNYC Taxi & Limousine Commission trip records: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page\n\nCourse: dbt + DuckDB in Rosetta DBT Studio, Project 1. One commit per lesson.\n"}<br>Click **Save**<br>(check: `README.md` equals `../snippets/3.2/README.md`)<br>Zoom: code-mid | 38 | 13 |

## s04 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b06 @0:50 | Git tab: stage all, type a message, publish docs and README, and commit. | Close the editor tab for `README.md`<br>Open the **Git** tab in the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Type the commit message “Publish docs and README”<br>Click **Commit**<br>Zoom: git-panel | 13 | 13 |
| b07 @1:03 | Sync Changes. The push starts the workflow. | git_push: None<br>Zoom: git-panel | 7 | 5 |

## s05 · browser — Browser

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b08 @1:08 | On GitHub, the Actions tab shows the run, now with two jobs: build, then docs. | Browser: open https://github.com/Nuri1977/nyc-taxi-dbt/actions<br>Wait for “Publish docs and README”<br>Click **the run** | 15 | 6 |
| b09 @1:14 | A minute later, both are green. | Wait for “^Success$” | 6 | 3 |
| b10 @1:17 | The docs are live on GitHub Pages, for anyone, with the lineage graph of the whole project. | Browser: open https://nuri1977.github.io/nyc-taxi-dbt/<br>Click **View Lineage Graph** | 17 | 7 |
| b11 @1:23 | And the repository page shows the README, with the green build badge. | Browser: open https://github.com/Nuri1977/nyc-taxi-dbt<br>Scroll to **NYC taxi dbt project** | 12 | 5 |

## s06 · slide — slide `query`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b12 @1:28 | And anyone can query the warehouse. With DuckDB, attach prod dot duckdb straight from the GitHub release, read only, and select from the marts. | README query block: install httpfs; load httpfs; attach the release URL as taxi (read_only); select * from taxi.main.top_pickup_zones. | 24 | 10 |
| b13 @1:38 | East Harlem North leads, with a hundred forty-three thousand trips: built by CI, and read over the internet. | Result: 74 East Harlem North, Manhattan, 143,115 trips; 75 East Harlem South, 82,011; 43 Central Park, 27,348. | 19 | 8 |

## s07 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b15 @1:46 | That's Project 1. Raw files and a seed, models with ref, descriptions, docs and the DAG, tables where they matter, tests, CI on every push, live docs, and a warehouse anyone can query. All built in Rosetta DBT Studio, and all on GitHub. | Project 1 checklist: source + seed, models with ref, properties, docs and DAG, materializations, tests, CI, Pages, public warehouse. | 43 | 17 |

## s08 · closing card (4 s, no voice)

Project 1 complete. Code: github.com/Nuri1977/nyc-taxi-dbt.

**Total: 280 spoken words, 2:07 rendered.**
