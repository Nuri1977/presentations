# Schema evolution — voice-over script and beat sheet

Data Lakes with DuckLake in Rosetta DBT Studio · Module 3 · Changing data · next: Lesson 3.4 · The data change feed

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `lesson-3-2-end`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 2 · Lesson 3.3. Schema evolution.

## s01 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | In the SQL Editor, on eth lake: add a column to blocks, gas used percent, a double. | Left bar → **SQL Editor**<br>Pick the connection **eth_lake**<br>paste: alter table raw.blocks add column gas_used_pct double;
update raw.blocks set gas_used_pct = round(100.0 * gas_used / gas_limit, 2) where date = date '2026-11-02';
alter table raw.blocks rename miner to fee_recipient;
alter table raw.blocks alter number set not null;
select number, fee_recipient, gas_used_pct from raw.blocks where date = date '2026-11-02' limit 3;
select number, miner from raw.blocks at (version => 11) limit 3;<br>Click the green run arrow next to line 1<br>Zoom: explorer | 17 | 12 |
| b02 @0:15 | It is instant: no file is rewritten. Old rows simply have no value. Fill it for one day, the second of November: gas used divided by the gas limit. | Click the green run arrow next to line 1<br>sql_wait: None<br>Zoom: explorer | 29 | 11 |

## s02 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b03 @0:25 | Miner is an old name; today the field means the fee recipient. Rename it. | Click the green run arrow next to line 1<br>Zoom: explorer | 14 | 6 |
| b04 @0:31 | And make number required: not null. | Click the green run arrow next to line 1<br>Zoom: explorer | 6 | 4 |
| b05 @0:35 | Query the new shape: number, fee recipient, and gas used percent. | Click the green run arrow next to line 1<br>Zoom: sql-results | 11 | 5 |
| b06 @0:39 | Now time travel to version eleven, before these changes. The column is still called miner there. Each snapshot keeps its own schema. | Click the green run arrow next to line 1<br>Zoom: sql-results<br>Card: *AT (VERSION => 11)* — **miner** — the old name, at the old version | 22 | 9 |

## s03 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b07 @0:48 | In Data Lake, open the blocks table and its Schema tab: fee recipient in place of miner, and the new column at the end. | Left bar → **DataLake**<br>Click **eth_lake**<br>Click **Refresh**<br>Click **blocks**<br>Click **Schema**<br>Zoom: center-wide | 24 | 16 |

## s04 · slide — slide `how`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b08 @1:04 | How does this work without touching files? Every column has an id in the catalog. A rename changes the name, not the id, so old files still map to the right column. | Old files are untouched; the catalog maps each column id to its name at each snapshot. | 32 | 11 |
| b09 @1:16 | You can add, drop and rename columns, promote types the safe way, like integer to big integer, and add not null. And every version keeps its own schema. | Allowed: add, drop, rename, safe type promotion (int to bigint), not null. | 28 | 10 |

## s05 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b10 @1:26 | Save the script as 3 underscore 3 schema evolution dot sequel, commit, and push. | Left bar → **DBT Studio**<br>Right-click `sql` → **New File** → `3_3_schema_evolution.sql` → **Save**<br>paste: alter table raw.blocks add column gas_used_pct double;
update raw.blocks set gas_used_pct = round(100.0 * gas_used / gas_limit, 2) where date = date '2026-11-02';
alter table raw.blocks rename miner to fee_recipient;
alter table raw.blocks alter number set not null;
select number, fee_recipient, gas_used_pct from raw.blocks where date = date '2026-11-02' limit 3;
select number, miner from raw.blocks at (version => 11) limit 3;
<br>Click **Save**<br>(check: `sql/3_3_schema_evolution.sql` equals `../snippets/3.3/3_3_schema_evolution.sql`)<br>Close the editor tab for `sql/3_3_schema_evolution.sql`<br>Open the **Git** tab in the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Type the commit message “Evolve the blocks schema”<br>Click **Commit**<br>git_push: None<br>Zoom: git-panel | 14 | 28 |

## s06 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b11 @1:54 | To recap: we added a column, renamed one, and added a constraint, without rewriting a single file. And time travel still sees the old schema. Next: asking the lake what changed between two versions. | Recap: add, rename, not null without rewriting files; each snapshot keeps its schema. | 34 | 13 |

## s07 · closing card (4 s, no voice)

Next · Lesson 3.4 · The data change feed.

**Total: 231 spoken words, 2:11 rendered.**
