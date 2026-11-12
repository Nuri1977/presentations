# Create the dbt project — voice-over script and beat sheet

dbt + DuckDB in Rosetta DBT Studio · Module 2 · dbt basics · next: Lesson 2.2 · Get the data

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `after-setup`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 1 · Lesson 2.1. Create the dbt project. Badges: DuckDB connection, dbt debug, first push to GitHub.

## s01 · slide — slide `anatomy`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | A dbt project is a folder. Models, seeds, tests and macros live in their own subfolders, and one file at the top, dbt_project.yml, gives the project its name and settings. | A folder tree: models, seeds, macros, tests, snapshots, analyses, and dbt_project.yml. | 32 | 13 |
| b02 @0:16 | A second file, profiles.yml, says where dbt runs. Our profile has one target, dev, and it points at a DuckDB database file. | profiles.yml: profile nyc_taxi → target dev → type duckdb, path to the database file. | 23 | 10 |

## s01b · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b02a @0:26 | Before we start, a quick look at Settings. Under General: the projects directory, where Studio creates new projects. | Left bar → **Settings**<br>Point at **Projects directory**<br>Zoom: center-wide | 18 | 8 |
| b02b @0:33 | Under dbt Core: the dbt runtime, dbt version one, one point twelve, and the adapters. dbt duckdb is the one for our database. | Click **dbt Core**<br>Point at **dbt-duckdb**<br>Zoom: center-wide | 23 | 11 |
| b02c @0:45 | And Python: Studio runs dbt with its own Python, three point ten, separate from any Python on your computer. | Click **Python**<br>Point at **Python Installation**<br>Zoom: center-wide | 19 | 8 |

## s02 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b03 @0:53 | Now, the database. On the home screen, click New Connection, and choose DuckDB. | Left bar → **Home**<br>Click **New Connection**<br>Click **DuckDB** | 13 | 10 |
| b04 @1:03 | Name it nyc taxi dev. For the file, type a path next to your projects folder: nyc taxi dev dot duckdb. DuckDB creates the file the first time dbt connects. Save. | Click **Connection Name**<br>Press Meta+A<br>Type `nyc_taxi_dev`<br>Click **Database File Path** and type `/Users/Shared/academy/learner/projects/nyc_taxi_dev.duckdb`<br>Click **Save**<br>Zoom: center-wide | 31 | 14 |

## s03 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b05 @1:16 | Now the project. Go back home, open the DBT Project card, and click New Project. | Left bar → **Home**<br>Click **DBT Project**<br>Click **New Project** | 15 | 8 |
| b06 @1:25 | Call it nyc taxi. Keep the template folders switched on, pick the nyc taxi dev connection, and save. | Click **Project Name** and type `nyc_taxi`<br>Point at **template folders**<br>Click **Connection**<br>Click **nyc_taxi_dev**<br>Click **Save**<br>Zoom: center-wide | 18 | 10 |
| b07 @1:34 | Studio creates the folder and opens it. Here are the template folders, and the two files we just talked about. | Point at `models` in the Explorer<br>Point at `dbt_project.yml` in the Explorer<br>Point at `profiles.yml` in the Explorer<br>Zoom: explorer | 20 | 7 |
| b08 @1:41 | Open dbt project dot yml: the project name is nyc taxi, it uses the profile with the same name, and lists where each kind of file lives. | Open `dbt_project.yml` in the Explorer<br>Point at line 5<br>Zoom: code-mid | 27 | 11 |

## s04 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b09 @1:52 | Let's check that dbt can reach the database. In the command box under the terminal, type dbt debug, and press Enter. | In the command box under the terminal, type `dbt debug` and press Enter<br>Zoom: terminal-close | 21 | 9 |
| b10 @2:01 | dbt finds the project and the profile, and connects to DuckDB. All checks passed. | Zoom: terminal-close<br>Card: *dbt debug* — **All checks passed!** — Project, profile and DuckDB connection are OK. | 14 | 7 |

## s05 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b11 @2:08 | Before the first commit, add a dot gitignore file at the top of the project, so build output, logs, data and the database stay out of git. | Right-click the project root → **New File** → `.gitignore` → **Save**<br>Type 61 characters into the editor<br>Click **Save**<br>(check: `.gitignore` equals `../snippets/2.1/gitignore`)<br>Zoom: code-close | 27 | 10 |
| b12 @2:18 | And a short README, so people who open the repository know what it is. | Right-click the project root → **New File** → `README.md` → **Save**<br>Type 114 characters into the editor<br>Click **Save**<br>(check: `README.md` equals `../snippets/2.1/README.md`)<br>Zoom: code-close | 14 | 11 |

## s06 · browser — Browser

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b13 @2:29 | Now a repository on GitHub. Create a new, empty, public repository called nyc taxi dbt, with no README, gitignore or license. Here is ours, still empty. | Browser: open https://github.com/Nuri1977/nyc-taxi-dbt<br>Zoom: center-wide | 26 | 13 |
| b15 @2:42 | GitHub shows its HTTPS address. Copy it. | Point at **HTTPS address**<br>Zoom: center-wide | 7 | 4 |

## s07 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b16 @2:47 | Back in Studio, open the Git tab, and click Initialize Repository. | Open the **Git** tab in the sidebar<br>Click **Initialize Repository**<br>Zoom: git-panel | 11 | 7 |
| b17 @2:53 | Stage all the changes, type a message, create the nyc taxi dbt project, and commit. | Hover CHANGES and click **+** (Stage All Changes)<br>Type the commit message “Create the nyc_taxi dbt project”<br>Click **Commit**<br>Zoom: git-panel | 15 | 9 |
| b18 @3:02 | Click Publish Branch. Studio asks for the remote: paste the repository address, and add it. Studio pushes the main branch to GitHub. | Click **Publish Branch**, paste `https://github.com/Nuri1977/nyc-taxi-dbt.git`, add the remote | 22 | 9 |

## s08 · browser — Browser

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b19 @3:11 | Refresh the repository page. The project is on GitHub: the folders, the two YAML files, the gitignore, and the README. | Browser: open https://github.com/Nuri1977/nyc-taxi-dbt<br>Zoom: center-wide | 20 | 8 |

## s09 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b20 @3:20 | To recap: a DuckDB connection, a dbt project called nyc taxi, a passing dbt debug, and the first commit on GitHub. From now on, every lesson ends with a commit and a push. Next, we get the data. | Recap: DuckDB connection; nyc_taxi project; dbt debug passes; first commit pushed to GitHub. | 38 | 15 |

## s10 · closing card (4 s, no voice)

Next · Lesson 2.2 · Get the data. Code: github.com/Nuri1977/nyc-taxi-dbt.

**Total: 454 spoken words, 3:39 rendered.**
