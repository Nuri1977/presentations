# Data inlining for small writes — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `lesson-4-2-end`: inlining is off for the whole lake (set in 2.2).

## s02 · Inlining on one table

| Listen for | Do this |
|---|---|
| "In the SQL Editor, on eth lake: a…" | In the left bar, click **SQL Editor**<br>Open the connection list (top left) and pick **eth_lake**<br>paste: create table raw.watchlist (address varchar, label varchar);<br>call eth_lake.set_option('data_inlining_row_limit', 100, schema => 'raw', table_name => 'watchlist');<br>insert into raw.watchlist values ('0x00000000219ab540356cbb839cbe05303d7705fa', 'staking deposit'), ('0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2', 'wrapped ether');<br>select * from raw.watchlist;<br>select count(*) as files from ducklake_list_files('eth_lake', 'watchlist', schema => 'raw');<br>call ducklake_flush_inlined_data('eth_lake', schema_name => 'raw', table_name => 'watchlist');<br>select count(*) as files from ducklake_list_files('eth_lake', 'watchlist', schema => 'raw');<br>Click the green ▶ arrow next to line 1<br>Click the green ▶ arrow next to line 1 |
| "Insert two addresses: the staking deposit contract, and…" | Click the green ▶ arrow next to line 1<br>Click the green ▶ arrow next to line 1 |
| "But count the table's data files: zero. The…" | Click the green ▶ arrow next to line 1 |
| "Flush the inlined data, and count again: one…" | Click the green ▶ arrow next to line 1<br>Click the green ▶ arrow next to line 1 |

## s04 · Commit and push

| Listen for | Do this |
|---|---|
| "Save the script as 4 underscore 3 inlining…" | In the left bar, click **DBT Studio**<br>Right-click `sql` → **New File**, type `4_3_inlining.sql`, click **Save**<br>paste: create table raw.watchlist (address varchar, label varchar);<br>call eth_lake.set_option('data_inlining_row_limit', 100, schema => 'raw', table_name => 'watchlist');<br>insert into raw.watchlist values ('0x00000000219ab540356cbb839cbe05303d7705fa', 'staking deposit'), ('0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2', 'wrapped ether');<br>select * from raw.watchlist;<br>select count(*) as files from ducklake_list_files('eth_lake', 'watchlist', schema => 'raw');<br>call ducklake_flush_inlined_data('eth_lake', schema_name => 'raw', table_name => 'watchlist');<br>select count(*) as files from ducklake_list_files('eth_lake', 'watchlist', schema => 'raw');<br><br>Click **Save** (top right of the editor)<br>(Check that `sql/4_3_inlining.sql` matches `../snippets/4.3/4_3_inlining.sql`)<br>Close the editor tab for `sql/4_3_inlining.sql` (its ×)<br>Click the **Git** tab at the top of the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Click the message box and type: A small inlined table<br>Click **Commit**<br>git_push: None |
