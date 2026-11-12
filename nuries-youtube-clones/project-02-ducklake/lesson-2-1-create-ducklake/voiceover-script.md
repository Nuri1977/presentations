# Create a DuckLake in Studio — voice-over script and beat sheet

Data Lakes with DuckLake in Rosetta DBT Studio · Module 2 · Your first lake in Studio · next: Lesson 2.2 · Load three months of blocks from S3

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `after-setup`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 2 · Lesson 2.1. Create a DuckLake in Studio. Badges: Data Lake wizard, DuckDB catalog, first push.

## s01 · slide — slide `plan`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | In this lesson we create the project for the whole course, and our first lake. On disk, the lake is two things inside one folder: a catalog file, and a data folder for the Parquet files. | The project folder ethereum_lake, with lake/eth_catalog.duckdb (the catalog) and lake/data/ (the Parquet files). | 36 | 12 |
| b02 @0:15 | We call the lake eth lake. Its storage is a local folder, and its catalog is a single DuckDB file. | Name: eth_lake. Storage: local folder. Catalog: DuckDB file. | 20 | 7 |

## s02 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b03 @0:22 | First, the project. dbt needs a connection, so on the home screen click New Connection, and choose DuckDB. | Left bar → **Home**<br>Click **New Connection**<br>Click **DuckDB** | 18 | 10 |
| b04 @0:32 | Name it ethereum lake dev, with a small DuckDB file next to the projects folder. We point dbt at the lake later, in Module 6. Save. | Click **Connection Name**<br>Press Meta+A<br>Type `ethereum_lake_dev`<br>Click **Database File Path** and type `/Users/Shared/academy/learner/projects/ethereum_lake_dev.duckdb`<br>Click **Save**<br>Zoom: center-wide | 26 | 11 |
| b05 @0:43 | Now open the DBT Project card, click New Project, and call it ethereum lake. Pick the connection, and save. | Left bar → **Home**<br>Click **DBT Project**<br>Click **New Project**<br>Click **Project Name** and type `ethereum_lake`<br>Click **Connection**<br>Click **ethereum_lake_dev**<br>Click **Save**<br>Zoom: center-wide | 19 | 18 |
| b06 @1:00 | In the project, make a folder called lake, and inside it, a folder called data. The lake lives here. | new_root_folder: lake<br>Right-click `lake` → **New Folder** → `data` → **Save**<br>Zoom: explorer | 19 | 13 |

## s03 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b07 @1:13 | Now open Data Lake from the sidebar. There are no lakes yet. Click Create DataLake, and choose DuckLake. | Left bar → **DataLake**<br>Wait 2.5 s<br>Point at **No DataLakes created yet**<br>Click **Create DataLake**<br>Point at **DuckLake**<br>Click **DuckLake**<br>Zoom: center-wide | 18 | 10 |
| b08 @1:23 | Step one, the name: eth underscore lake. Next. | Click **Instance Name** and type `eth_lake`<br>Click **Next**<br>Zoom: center-wide | 8 | 4 |
| b09 @1:27 | Step two, storage. Keep Local, and give the full path of the data folder we just made. This is where the Parquet files will go. | Click **Local Data Path** and type `/Users/Shared/academy/learner/projects/ethereum_lake/lake/data`<br>Click **Next**<br>Zoom: center-wide | 25 | 9 |
| b10 @1:36 | Step three, the catalog. DuckDB is the catalog type. Replace the suggested path with a file in the lake folder: eth catalog dot duckdb. | Click **Catalog Database File** and type `/Users/Shared/academy/learner/projects/ethereum_lake/lake/eth_catalog.duckdb`<br>Zoom: center-wide | 24 | 10 |
| b11 @1:46 | Next. The runtime options, memory and threads, can stay as they are. Next again, and the review shows the name, the data folder, and the DuckDB catalog. Click Create Instance. | Click **Next**<br>Point at **Max Memory**<br>Click **Next**<br>Point at **Local Filesystem**<br>Click **Create Instance**<br>Zoom: center-wide | 30 | 12 |

## s04 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b12 @1:58 | Here is the lake. No tables yet. Open History: there is already one snapshot, number zero. Creating the lake created the schema main. Every change will add a row here. | Point at **Tables & Views**<br>Click **History**<br>Zoom: center-wide<br>Card: *eth_lake · History* — **Snapshot 0** — created the schema main | 30 | 11 |
| b13 @2:09 | Now the SQL Editor. The connection list has a new group, DuckLake Instances. Pick eth lake, and ask for its snapshots. | Left bar → **SQL Editor**<br>Pick the connection **eth_lake**<br>Type 35 characters into the editor<br>Zoom: explorer | 21 | 11 |
| b14 @2:21 | Run it with the green arrow. One row: snapshot zero. The lake answers SQL. | Click the green run arrow next to line 1<br>Zoom: sql-results | 14 | 6 |

## s05 · slide — slide `sql`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b15 @2:27 | In plain DuckDB, the wizard stands for three statements: install the extension, attach the catalog file with its data path, and use it. Studio runs them each time it opens the lake. | Code: INSTALL ducklake; ATTACH 'ducklake:lake/eth_catalog.duckdb' AS eth_lake (DATA_PATH 'lake/data/'); USE eth_lake; | 32 | 13 |
| b16 @2:40 | And remember: with a DuckDB file as the catalog, one program at a time can open the lake. For a laptop, that is enough. | Note: with a DuckDB catalog file, one program at a time can open the lake. | 24 | 9 |

## s06 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b17 @2:49 | Back in the project. Add a dot gitignore file, so build output, logs, the database files, and the whole lake folder stay out of git. The lake is data, not code. | Left bar → **DBT Studio**<br>Right-click the project root → **New File** → `.gitignore` → **Save**<br>Type 61 characters into the editor<br>Click **Save**<br>(check: `.gitignore` equals `../snippets/2.1/gitignore`)<br>Zoom: code-close | 31 | 12 |
| b18 @3:01 | And a short README. | Right-click the project root → **New File** → `README.md` → **Save**<br>Type 137 characters into the editor<br>Click **Save**<br>(check: `README.md` equals `../snippets/2.1/README.md`)<br>Zoom: code-close | 4 | 12 |

## s07 · browser — Browser

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b19 @3:13 | On GitHub, create a new, empty, public repository called ethereum ducklake dbt, with no README, gitignore or license. Here is ours, still empty. Copy its HTTPS address. | Browser: open https://github.com/Nuri1977/ethereum-ducklake-dbt<br>Point at **HTTPS address**<br>Zoom: center-wide | 27 | 14 |

## s08 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b20 @3:27 | Back in Studio, open the Git tab, and click Initialize Repository. | Open the **Git** tab in the sidebar<br>Click **Initialize Repository**<br>Zoom: git-panel | 11 | 7 |
| b21 @3:34 | Stage all the changes, type a message, create the ethereum lake project, and commit. | Hover CHANGES and click **+** (Stage All Changes)<br>Type the commit message “Create the ethereum_lake project”<br>Click **Commit**<br>Zoom: git-panel | 14 | 9 |
| b22 @3:43 | Click Publish Branch, paste the repository address, and add it. Studio pushes the main branch to GitHub. | Click **Publish Branch**, paste `https://github.com/Nuri1977/ethereum-ducklake-dbt.git`, add the remote | 17 | 8 |

## s09 · browser — Browser

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b23 @3:51 | Refresh the repository page. The project is on GitHub. The lake folder is not: git ignores it. | Browser: open https://github.com/Nuri1977/ethereum-ducklake-dbt<br>Zoom: center-wide | 17 | 7 |

## s10 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b24 @3:58 | To recap: we created the ethereum lake project, and the eth lake DuckLake inside it, with the Data Lake wizard. It is a catalog file and a data folder, it starts with snapshot zero, and the SQL Editor can query it. The project is on GitHub. Next, we load three months of blocks into the lake. | Recap: project ethereum_lake; eth_lake created in the Data Lake wizard; catalog file plus data folder; snapshot 0; first push. | 56 | 19 |

## s11 · closing card (4 s, no voice)

Next · Lesson 2.2 · Load three months of blocks from S3.

**Total: 541 spoken words, 4:21 rendered.**
