# Schema evolution — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `lesson-3-2-end`: raw.blocks with three months plus 1 and 2 November; snapshots 0 to 11.

## s01 · Add a column

| Listen for | Do this |
|---|---|
| "In the SQL Editor, on eth lake: add…" | In the left bar, click **SQL Editor**<br>Open the connection list (top left) and pick **eth_lake**<br>paste: alter table raw.blocks add column gas_used_pct double;<br>update raw.blocks set gas_used_pct = round(100.0 * gas_used / gas_limit, 2) where date = date '2026-11-02';<br>alter table raw.blocks rename miner to fee_recipient;<br>alter table raw.blocks alter number set not null;<br>select number, fee_recipient, gas_used_pct from raw.blocks where date = date '2026-11-02' limit 3;<br>select number, miner from raw.blocks at (version => 11) limit 3;<br>Click the green ▶ arrow next to line 1 |
| "It is instant: no file is rewritten. Old…" | Click the green ▶ arrow next to line 1<br>sql_wait: None |

## s02 · Rename and constrain

| Listen for | Do this |
|---|---|
| "Miner is an old name; today the field…" | Click the green ▶ arrow next to line 1 |
| "And make number required: not null.…" | Click the green ▶ arrow next to line 1 |
| "Query the new shape: number, fee recipient, and…" | Click the green ▶ arrow next to line 1 |
| "Now time travel to version eleven, before these…" | Click the green ▶ arrow next to line 1 |

## s03 · The schema in Studio

| Listen for | Do this |
|---|---|
| "In Data Lake, open the blocks table and…" | In the left bar, click **DataLake**<br>Click **eth_lake**<br>Click **Refresh**<br>Click **blocks**<br>Click **Schema** |

## s05 · Commit and push

| Listen for | Do this |
|---|---|
| "Save the script as 3 underscore 3 schema…" | In the left bar, click **DBT Studio**<br>Right-click `sql` → **New File**, type `3_3_schema_evolution.sql`, click **Save**<br>paste: alter table raw.blocks add column gas_used_pct double;<br>update raw.blocks set gas_used_pct = round(100.0 * gas_used / gas_limit, 2) where date = date '2026-11-02';<br>alter table raw.blocks rename miner to fee_recipient;<br>alter table raw.blocks alter number set not null;<br>select number, fee_recipient, gas_used_pct from raw.blocks where date = date '2026-11-02' limit 3;<br>select number, miner from raw.blocks at (version => 11) limit 3;<br><br>Click **Save** (top right of the editor)<br>(Check that `sql/3_3_schema_evolution.sql` matches `../snippets/3.3/3_3_schema_evolution.sql`)<br>Close the editor tab for `sql/3_3_schema_evolution.sql` (its ×)<br>Click the **Git** tab at the top of the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Click the message box and type: Evolve the blocks schema<br>Click **Commit**<br>git_push: None |
