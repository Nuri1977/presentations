# The data change feed — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `lesson-3-3-end`: raw.blocks_day created at snapshot 8, 7 rows deleted at 9, 72 rows updated at 10.

## s01 · What changed?

| Listen for | Do this |
|---|---|
| "Remember Lesson 3.1? We deleted seven rows of…" | In the left bar, click **SQL Editor**<br>Open the connection list (top left) and pick **eth_lake**<br>paste: select snapshot_id, change_type, count(*) as row_count from ducklake_table_changes('eth_lake', 'raw', 'blocks_day', 9, 10) group by all order by 1, 2;<br>select snapshot_id, change_type, number, extra_data from ducklake_table_changes('eth_lake', 'raw', 'blocks_day', 10, 10) order by number, change_type limit 4;<br>select count(*) as inserted from ducklake_table_insertions('eth_lake', 'raw', 'blocks_day', 8, 8);<br>select count(*) as deleted from ducklake_table_deletions('eth_lake', 'raw', 'blocks_day', 9, 9); |
| "Ducklake table changes, for schema raw, table blocks…" | Click the green ▶ arrow next to line 1 |
| "Look at the rows: each updated block appears…" | Click the green ▶ arrow next to line 1 |
| "And two shortcuts: table insertions, seven thousand one…" | Click the green ▶ arrow next to line 1<br>Click the green ▶ arrow next to line 1 |

## s03 · Commit and push

| Listen for | Do this |
|---|---|
| "Save the queries as 3 underscore 4 change…" | In the left bar, click **DBT Studio**<br>Right-click `sql` → **New File**, type `3_4_change_feed.sql`, click **Save**<br>paste: select snapshot_id, change_type, count(*) as row_count from ducklake_table_changes('eth_lake', 'raw', 'blocks_day', 9, 10) group by all order by 1, 2;<br>select snapshot_id, change_type, number, extra_data from ducklake_table_changes('eth_lake', 'raw', 'blocks_day', 10, 10) order by number, change_type limit 4;<br>select count(*) as inserted from ducklake_table_insertions('eth_lake', 'raw', 'blocks_day', 8, 8);<br>select count(*) as deleted from ducklake_table_deletions('eth_lake', 'raw', 'blocks_day', 9, 9);<br><br>Click **Save** (top right of the editor)<br>(Check that `sql/3_4_change_feed.sql` matches `../snippets/3.4/3_4_change_feed.sql`)<br>Close the editor tab for `sql/3_4_change_feed.sql` (its ×)<br>Click the **Git** tab at the top of the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Click the message box and type: The data change feed<br>Click **Commit**<br>git_push: None |
