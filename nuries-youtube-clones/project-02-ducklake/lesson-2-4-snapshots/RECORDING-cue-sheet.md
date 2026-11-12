# Snapshots: every change is a version — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `lesson-2-3-end`: raw.blocks with three months, snapshots 0 to 4.

## s02 · Snapshots in Studio

| Listen for | Do this |
|---|---|
| "In Data Lake, open eth lake, and its…" | In the left bar, click **DataLake**<br>Click **eth_lake**<br>Click **History** |

## s03 · Snapshots in SQL

| Listen for | Do this |
|---|---|
| "In the SQL Editor, the same list comes…" | In the left bar, click **SQL Editor**<br>Open the connection list (top left) and pick **eth_lake**<br>paste: select snapshot_id, schema_version, changes from eth_lake.snapshots() order by 1;<br>select * from eth_lake.current_snapshot();<br>insert into raw.blocks select * exclude (logs_bloom, last_modified) from read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-11-01/*.parquet');<br>select snapshot_id, changes from eth_lake.snapshots() order by 1 desc limit 2;<br>Click the green ▶ arrow next to line 1 |
| "Current snapshot tells you where the lake is…" | Click the green ▶ arrow next to line 1 |
| "Now change something. Insert one more day of…" | Click the green ▶ arrow next to line 1<br>sql_wait: None |
| "And list the newest snapshots again. Snapshot five:…" | Click the green ▶ arrow next to line 1 |

## s05 · Commit and push

| Listen for | Do this |
|---|---|
| "Save the queries as 2 underscore 4 snapshots…" | In the left bar, click **DBT Studio**<br>Right-click `sql` → **New File**, type `2_4_snapshots.sql`, click **Save**<br>paste: select snapshot_id, schema_version, changes from eth_lake.snapshots() order by 1;<br>select * from eth_lake.current_snapshot();<br>insert into raw.blocks select * exclude (logs_bloom, last_modified) from read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-11-01/*.parquet');<br>select snapshot_id, changes from eth_lake.snapshots() order by 1 desc limit 2;<br><br>Click **Save** (top right of the editor)<br>(Check that `sql/2_4_snapshots.sql` matches `../snippets/2.4/2_4_snapshots.sql`)<br>Close the editor tab for `sql/2_4_snapshots.sql` (its ×)<br>Click the **Git** tab at the top of the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Click the message box and type: Snapshots and one more day<br>Click **Commit**<br>git_push: None |
