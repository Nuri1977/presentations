# Daily loads without duplicates — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `lesson-3-1-end`: raw.blocks with three months plus 1 November; raw.blocks_day; snapshots 0 to 10.

## s02 · Insert what is new

| Listen for | Do this |
|---|---|
| "In the SQL Editor, on eth lake: insert…" | In the left bar, click **SQL Editor**<br>Open the connection list (top left) and pick **eth_lake**<br>paste: insert into raw.blocks select s.* exclude (logs_bloom, last_modified) from read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-11-02/*.parquet') as s where not exists (select 1 from raw.blocks as t where t.number = s.number);<br>select date, count(*) as blocks from raw.blocks where date >= date '2026-11-01' group by all order by 1;<br>select snapshot_id, changes from eth_lake.snapshots() order by 1 desc limit 3;<br>Click the green ▶ arrow next to line 1<br>sql_wait: None |
| "Count by day. Studio 1.7.6 shows a date…" | Click the green ▶ arrow next to line 1 |
| "Now run the load again, as if a…" | Click the green ▶ arrow next to line 1<br>sql_wait: None |
| "Count again: still seven thousand one hundred seventy-six.…" | Click the green ▶ arrow next to line 1 |
| "And the snapshots: one new snapshot for the…" | Click the green ▶ arrow next to line 1 |

## s04 · Commit and push

| Listen for | Do this |
|---|---|
| "Save the load as 3 underscore 2 daily…" | In the left bar, click **DBT Studio**<br>Right-click `sql` → **New File**, type `3_2_daily_load.sql`, click **Save**<br>paste: insert into raw.blocks select s.* exclude (logs_bloom, last_modified) from read_parquet('s3://aws-public-blockchain/v1.0/eth/blocks/date=2026-11-02/*.parquet') as s where not exists (select 1 from raw.blocks as t where t.number = s.number);<br>select date, count(*) as blocks from raw.blocks where date >= date '2026-11-01' group by all order by 1;<br>select snapshot_id, changes from eth_lake.snapshots() order by 1 desc limit 3;<br><br>Click **Save** (top right of the editor)<br>(Check that `sql/3_2_daily_load.sql` matches `../snippets/3.2/3_2_daily_load.sql`)<br>Close the editor tab for `sql/3_2_daily_load.sql` (its ×)<br>Click the **Git** tab at the top of the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Click the message box and type: Daily load without duplicates<br>Click **Commit**<br>git_push: None |
