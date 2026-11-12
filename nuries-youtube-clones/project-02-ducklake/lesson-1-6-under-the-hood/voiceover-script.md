# Under the hood: DuckDB and DuckLake in Studio — voice-over script and beat sheet

Data Lakes with DuckLake in Rosetta DBT Studio · Module 1 · Data lakes explained · next: Lesson 2.1 · Create a DuckLake in Studio

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `after-setup`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 2 · Lesson 1.6. Under the hood. Badges: Electron, @duckdb/node-api, ducklake extension.

## s01 · slide — slide `electron`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | Before we build a lake, let's look under the hood. Rosetta DBT Studio is an Electron app. That means two parts: the window you see, and a Node.js process behind it. | Studio is an Electron app: a window (renderer) and a Node.js process (main). | 32 | 12 |
| b02 @0:14 | The window never touches a database. When you run a query, it sends a request to the main process, which runs the SQL and sends back the rows. | The window sends a request; the main process runs the SQL and sends back rows. | 28 | 10 |

## s02 · slide — slide `node`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b03 @0:24 | The main process uses DuckDB's official Node package, duck D B slash node A P I. Studio 1.7.6 ships version 1.5.2. DuckDB runs inside Studio itself: no server, nothing else to install. | @duckdb/node-api 1.5.2: DuckDB's official Node.js package, in Studio's package.json. | 36 | 16 |
| b04 @0:40 | In Studio's code, it is three calls. Create a DuckDB instance. Connect to it. And run SQL on the connection. | Code: DuckDBInstance.create(path) → instance.connect() → connection.run(sql). | 20 | 8 |

## s03 · slide — slide `extension`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b05 @0:48 | DuckLake is not built into DuckDB. It is an extension. So on that connection, Studio first runs install ducklake, and load ducklake. | INSTALL ducklake; LOAD ducklake; | 22 | 10 |
| b06 @0:58 | Then it attaches the lake: the catalog file, a name, and the data path. And it makes the lake the current database. That is exactly what you could type yourself. | ATTACH 'ducklake:<catalog file>' AS "eth_lake" (DATA_PATH '<folder>', AUTOMATIC_MIGRATION TRUE); USE "eth_lake"; | 30 | 10 |
| b07 @1:08 | There is one adapter per catalog type. In 1.7.6 the wizard offers DuckDB; SQLite and PostgreSQL are marked as coming soon. When a lake is closed, Studio detaches it. | One adapter per catalog type: DuckDB (offered), SQLite and PostgreSQL (Soon). DETACH when the lake is closed. | 31 | 13 |

## s04 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b08 @1:21 | You can see the engine in Studio. Open Settings, then DuckDB. This is Studio's own DuckDB database, for caching and previews. | Left bar → **Settings**<br>Click **DuckDB**<br>Zoom: center-wide | 21 | 9 |
| b09 @1:30 | And the status bar always shows the DuckDB version inside the app: 1.5.2. | Point at **DuckDB version**<br>Zoom: statusbar | 15 | 7 |

## s05 · slide — slide `twoengines`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b10 @1:37 | One more thing for later. When dbt runs, it uses its own DuckDB, the Python package inside dbt duckdb, version 1.5.6. So two engines read and write the same lake. We checked that they agree. | Studio: DuckDB 1.5.2 (Node). dbt: DuckDB 1.5.6 (Python, inside dbt-duckdb). Both read and write the same lake. | 37 | 16 |
| b11 @1:53 | But with a DuckDB file as the catalog, only one of them can open it at a time. Keep that in mind for Module 6. | With a DuckDB catalog file, only one of them can open the lake at a time. | 25 | 8 |

## s06 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b12 @2:01 | To recap: DuckDB runs inside Studio, through its Node package. DuckLake is an extension that Studio loads. And everything the Data Lake screens do is plain SQL. Now, let's create our lake. | Recap: DuckDB runs inside Studio; ducklake is an extension; the Data Lake screens run plain SQL. | 32 | 13 |

## s07 · closing card (4 s, no voice)

Next · Lesson 2.1 · Create a DuckLake in Studio.

**Total: 329 spoken words, 2:18 rendered.**
