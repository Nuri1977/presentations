# Statistics and file pruning — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `lesson-4-1-end`: raw.transactions loaded and partitioned by date (seven files).

## s01 · Statistics in the catalog

| Listen for | Do this |
|---|---|
| "In Data Lake, open the transactions table and…" | In the left bar, click **DataLake**<br>Click **eth_lake**<br>Click **transactions**<br>Click **Statistics**<br>Point at **block_number** |
| "The catalog keeps the same numbers for every…" | Hold; nothing moves |

## s02 · Pruning in action

| Listen for | Do this |
|---|---|
| "In the SQL Editor, on eth lake: the…" | In the left bar, click **SQL Editor**<br>Open the connection list (top left) and pick **eth_lake**<br>paste: select min(block_number) as first_block, max(block_number) as last_block from raw.transactions;<br>explain analyze select count(*) from raw.transactions where block_number between 26100000 and 26100100;<br>alter table raw.transactions set sorted by (block_number asc);<br>select option_name, value from eth_lake.options();<br>Click the green ▶ arrow next to line 1 |
| "Now ask for a hundred blocks, with explain…" | Click the green ▶ arrow next to line 1 |

## s04 · Sorted by, and options

| Listen for | Do this |
|---|---|
| "Set it for transactions: sorted by block number.…" | Click the green ▶ arrow next to line 1 |
| "Other settings live in the lake's options, like…" | Click the green ▶ arrow next to line 1 |

## s05 · Commit and push

| Listen for | Do this |
|---|---|
| "Save the script as 4 underscore 2 statistics…" | In the left bar, click **DBT Studio**<br>Right-click `sql` → **New File**, type `4_2_statistics.sql`, click **Save**<br>paste: select min(block_number) as first_block, max(block_number) as last_block from raw.transactions;<br>explain analyze select count(*) from raw.transactions where block_number between 26100000 and 26100100;<br>alter table raw.transactions set sorted by (block_number asc);<br>select option_name, value from eth_lake.options();<br><br>Click **Save** (top right of the editor)<br>(Check that `sql/4_2_statistics.sql` matches `../snippets/4.2/4_2_statistics.sql`)<br>Close the editor tab for `sql/4_2_statistics.sql` (its ×)<br>Click the **Git** tab at the top of the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Click the message box and type: Statistics and sorted transactions<br>Click **Commit**<br>git_push: None |
