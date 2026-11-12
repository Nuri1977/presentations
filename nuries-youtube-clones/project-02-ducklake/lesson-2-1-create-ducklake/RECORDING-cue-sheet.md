# Create a DuckLake in Studio — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `after-setup`: Studio set up (Python 3.10.17, dbt 1.12.6), no project, no connection, no lake.
- Pushes to the public Nuri1977/ethereum-ducklake-dbt, created empty before the lesson.

## s02 · The project

| Listen for | Do this |
|---|---|
| "First, the project. dbt needs a connection, so…" | In the left bar, click **Home**<br>Click **New Connection**<br>Click **DuckDB** |
| "Name it ethereum lake dev, with a small…" | Click **Connection Name**<br>Press Meta+A<br>Type `ethereum_lake_dev`<br>Click **Database File Path** and type `/Users/Shared/academy/learner/projects/ethereum_lake_dev.duckdb`<br>Click **Save** |
| "Now open the DBT Project card, click New…" | In the left bar, click **Home**<br>Click **DBT Project**<br>Click **New Project**<br>Click **Project Name** and type `ethereum_lake`<br>Click **Connection**<br>Click **ethereum_lake_dev**<br>Click **Save** |
| "In the project, make a folder called lake,…" | new_root_folder: lake<br>Right-click `lake` → **New Folder**, type `data`, click **Save** |

## s03 · The Data Lake wizard

| Listen for | Do this |
|---|---|
| "Now open Data Lake from the sidebar. There…" | In the left bar, click **DataLake**<br>Wait 2.5 s<br>Point at **No DataLakes created yet**<br>Click **Create DataLake**<br>Point at **DuckLake**<br>Click **DuckLake** |
| "Step one, the name: eth underscore lake. Next.…" | Click **Instance Name** and type `eth_lake`<br>Click **Next** |
| "Step two, storage. Keep Local, and give the…" | Click **Local Data Path** and type `/Users/Shared/academy/learner/projects/ethereum_lake/lake/data`<br>Click **Next** |
| "Step three, the catalog. DuckDB is the catalog…" | Click **Catalog Database File** and type `/Users/Shared/academy/learner/projects/ethereum_lake/lake/eth_catalog.duckdb` |
| "Next. The runtime options, memory and threads, can…" | Click **Next**<br>Point at **Max Memory**<br>Click **Next**<br>Point at **Local Filesystem**<br>Click **Create Instance** |

## s04 · The new lake

| Listen for | Do this |
|---|---|
| "Here is the lake. No tables yet. Open…" | Point at **Tables & Views**<br>Click **History** |
| "Now the SQL Editor. The connection list has…" | In the left bar, click **SQL Editor**<br>Open the connection list (top left) and pick **eth_lake**<br>Type:<br><br>```sql<br>select * from eth_lake.snapshots();<br>``` |
| "Run it with the green arrow. One row:…" | Click the green ▶ arrow next to line 1 |

## s06 · Files that keep git clean

| Listen for | Do this |
|---|---|
| "Back in the project. Add a dot gitignore…" | In the left bar, click **DBT Studio**<br>Right-click the project root → **New File** → `.gitignore` → **Save**<br>Type:<br><br>```sql<br>target/<br>dbt_packages/<br>logs/<br>lake/<br>*.duckdb<br>*.duckdb.wal<br>.env<br>```<br>Click **Save** (top right of the editor)<br>(Check that `.gitignore` matches `../snippets/2.1/gitignore`) |
| "And a short README.…" | Right-click the project root → **New File** → `README.md` → **Save**<br>Type:<br><br>```sql<br># Ethereum data lake with DuckLake<br><br>Code for the course Data lakes and DuckLake in Rosetta DBT Studio, Project 2.<br>One commit per lesson.<br>```<br>Click **Save** (top right of the editor)<br>(Check that `README.md` matches `../snippets/2.1/README.md`) |

## s07 · A repository on GitHub

| Listen for | Do this |
|---|---|
| "On GitHub, create a new, empty, public repository…" | In the browser, open https://github.com/Nuri1977/ethereum-ducklake-dbt<br>Point at **HTTPS address** |

## s08 · First commit and push

| Listen for | Do this |
|---|---|
| "Back in Studio, open the Git tab, and…" | Click the **Git** tab at the top of the sidebar<br>Click **Initialize Repository** |
| "Stage all the changes, type a message, create…" | Hover CHANGES and click **+** (Stage All Changes)<br>Click the message box and type: Create the ethereum_lake project<br>Click **Commit** |
| "Click Publish Branch, paste the repository address, and…" | Click **Publish Branch**, paste `https://github.com/Nuri1977/ethereum-ducklake-dbt.git`, add the remote |

## s09 · The code is on GitHub

| Listen for | Do this |
|---|---|
| "Refresh the repository page. The project is on…" | In the browser, open https://github.com/Nuri1977/ethereum-ducklake-dbt |
