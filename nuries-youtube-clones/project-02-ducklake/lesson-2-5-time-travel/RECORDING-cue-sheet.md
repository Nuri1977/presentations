# Time travel — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `lesson-2-4-end`: raw.blocks with three months plus 1 November (667,072 rows), snapshots 0 to 5.

## s01 · Query the past

| Listen for | Do this |
|---|---|
| "In the SQL Editor, on eth lake, start…" | In the left bar, click **SQL Editor**<br>Open the connection list (top left) and pick **eth_lake**<br>paste: select count(*) as blocks from raw.blocks;<br>select count(*) as blocks from raw.blocks at (version => 2);<br>select strftime(date, '%Y-%m') as month, count(*) as blocks from raw.blocks at (version => 3) group by all order by 1;<br>create table raw.blocks_october as select * from raw.blocks at (version => 4) where date >= date '2026-10-01';<br>select count(*) as blocks from raw.blocks_october;<br>drop table raw.blocks_october;<br>Click the green ▶ arrow next to line 1 |
| "Now add at, version equals two. That is…" | Click the green ▶ arrow next to line 1 |
| "Any query works on the past. Blocks per…" | Click the green ▶ arrow next to line 1 |

## s02 · Bring the past back

| Listen for | Do this |
|---|---|
| "Time travel also helps you recover data. Create…" | Click the green ▶ arrow next to line 1<br>sql_wait: None |
| "It holds exactly the October blocks: two hundred…" | Click the green ▶ arrow next to line 1<br>Click the green ▶ arrow next to line 1 |

## s04 · Commit and push

| Listen for | Do this |
|---|---|
| "Save the queries as 2 underscore 5 time…" | In the left bar, click **DBT Studio**<br>Right-click `sql` → **New File**, type `2_5_time_travel.sql`, click **Save**<br>paste: select count(*) as blocks from raw.blocks;<br>select count(*) as blocks from raw.blocks at (version => 2);<br>select strftime(date, '%Y-%m') as month, count(*) as blocks from raw.blocks at (version => 3) group by all order by 1;<br>create table raw.blocks_october as select * from raw.blocks at (version => 4) where date >= date '2026-10-01';<br>select count(*) as blocks from raw.blocks_october;<br>drop table raw.blocks_october;<br><br>Click **Save** (top right of the editor)<br>(Check that `sql/2_5_time_travel.sql` matches `../snippets/2.5/2_5_time_travel.sql`)<br>Close the editor tab for `sql/2_5_time_travel.sql` (its ×)<br>Click the **Git** tab at the top of the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Click the message box and type: Time travel<br>Click **Commit**<br>git_push: None |
