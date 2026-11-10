# Create the dbt project — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `after-setup`: Studio with Python and dbt installed (as after Lesson 1.1), no project, no connection; learner git config uses the stored token.
- Rehearsal: pushes to the private Nuri1977/nyc-taxi-dbt-rehearsal. The repo-creation scene reuses the Lesson 1.2 recording; the final run creates the public Nuri1977/nyc-taxi-dbt.

## s02 · A DuckDB connection

| Listen for | Do this |
|---|---|
| "First, the database. On the home screen, click…" | Click **New Connection**<br>Click **DuckDB** |
| "Name it nyc taxi dev. For the file,…" | Click **Connection Name**<br>Press Meta+A<br>Type `nyc_taxi_dev`<br>Click **Database File Path** and type `/Users/Shared/academy/learner/projects/nyc_taxi_dev.duckdb`<br>Click **Save** |

## s03 · Create the project

| Listen for | Do this |
|---|---|
| "Now the project. Go back home, open the…" | In the left bar, click **Home**<br>Click **DBT Project**<br>Click **New Project** |
| "Call it nyc taxi. Keep the template folders…" | Click **Project Name** and type `nyc_taxi`<br>Point at **template folders**<br>Click **Connection**<br>Click **nyc_taxi_dev**<br>Click **Save** |
| "Studio creates the folder and opens it. Here…" | Point at `models` in the Explorer<br>Point at `dbt_project.yml` in the Explorer<br>Point at `profiles.yml` in the Explorer |
| "Open dbt project dot yml: the project name…" | In the Explorer, open `dbt_project.yml` (expand each folder on the way)<br>Point at line 5 |

## s04 · Check the setup with dbt debug

| Listen for | Do this |
|---|---|
| "Let's check that dbt can reach the database.…" | Click the command box under the terminal, type `dbt debug`, press Enter |
| "dbt finds the project and the profile, and…" | Hold; nothing moves |

## s05 · Files that keep git clean

| Listen for | Do this |
|---|---|
| "Before the first commit, add a dot gitignore…" | Right-click the project root → **New File** → `.gitignore` → **Save**<br>Type:<br><br>```sql<br>target/<br>dbt_packages/<br>logs/<br>data/<br>*.duckdb<br>*.duckdb.wal<br>.env<br>```<br>Click **Save** (top right of the editor)<br>(Check that `.gitignore` matches `../snippets/2.1/gitignore`) |
| "And a short README, so people who open…" | Right-click the project root → **New File** → `README.md` → **Save**<br>Type:<br><br>```sql<br># NYC taxi dbt project<br><br>Code for the course dbt + DuckDB in Rosetta DBT Studio, Project 1.<br>One commit per lesson.<br>```<br>Click **Save** (top right of the editor)<br>(Check that `README.md` matches `../snippets/2.1/README.md`) |

## s06 · A repository on GitHub

| Listen for | Do this |
|---|---|
| "Now create an empty repository on GitHub: the…" | GitHub (built-in browser): github.com → + → New repository (frames from Lesson 1.2's recording) |
| "Name it nyc taxi dbt, and make it…" | GitHub (built-in browser): Repository name, visibility, Create repository |
| "Copy the HTTPS address of the new, empty…" | GitHub (built-in browser): Quick setup → copy the HTTPS URL |

## s07 · First commit and push

| Listen for | Do this |
|---|---|
| "Back in Studio, open the Git tab, and…" | Click the **Git** tab at the top of the sidebar<br>Click **Initialize Repository** |
| "Stage all the changes, type a message, create…" | Hover CHANGES and click **+** (Stage All Changes)<br>Click the message box and type: Create the nyc_taxi dbt project<br>Click **Commit** |
| "Click Publish Branch. Studio asks for the remote:…" | Click **Publish Branch**, paste `https://github.com/Nuri1977/nyc-taxi-dbt-rehearsal.git`, add the remote |

## s08 · The code is on GitHub

| Listen for | Do this |
|---|---|
| "Refresh the repository page. The project is on…" | In the browser, open https://github.com/Nuri1977/nyc-taxi-dbt-rehearsal |
