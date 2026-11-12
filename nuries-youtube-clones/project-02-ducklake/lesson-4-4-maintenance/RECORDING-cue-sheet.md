# Maintenance — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.6, dark theme, window 1920x1080.

## Before you start

- Start state `lesson-4-3-end`: 19 Parquet files under lake/data.

## s02 · Merge

| Listen for | Do this |
|---|---|
| "In the SQL Editor, on eth lake: count…" | In the left bar, click **SQL Editor**<br>Open the connection list (top left) and pick **eth_lake**<br>paste: select count(*) as files from glob('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/**/*.parquet');<br>call ducklake_merge_adjacent_files('eth_lake');<br>select count(*) as files from glob('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/**/*.parquet');<br>select snapshot_id, changes from eth_lake.snapshots() where snapshot_id in (6, 7);<br>call ducklake_expire_snapshots('eth_lake', versions => [6, 7]);<br>call ducklake_cleanup_old_files('eth_lake', dry_run => true, cleanup_all => true);<br>call ducklake_cleanup_old_files('eth_lake', cleanup_all => true);<br>select count(*) as files from glob('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/**/*.parquet');<br>checkpoint;<br>Click the green ▶ arrow next to line 1 |
| "Merge adjacent files. Studio shows no result rows…" | Click the green ▶ arrow next to line 1<br>sql_wait: None |
| "Count again: twenty. One more, not fewer: the…" | Click the green ▶ arrow next to line 1 |

## s03 · Expire and clean up

| Listen for | Do this |
|---|---|
| "Snapshots six and seven are the October copy…" | Click the green ▶ arrow next to line 1<br>Click the green ▶ arrow next to line 1 |
| "Now clean up old files. First a dry…" | Click the green ▶ arrow next to line 1 |
| "Run it for real, and count: fourteen files.…" | Click the green ▶ arrow next to line 1<br>Click the green ▶ arrow next to line 1 |
| "In practice, you just run checkpoint, now and…" | Click the green ▶ arrow next to line 1<br>sql_wait: None |

## s05 · Commit and push

| Listen for | Do this |
|---|---|
| "Save the script as 4 underscore 4 maintenance…" | In the left bar, click **DBT Studio**<br>Right-click `sql` → **New File**, type `4_4_maintenance.sql`, click **Save**<br>paste: select count(*) as files from glob('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/**/*.parquet');<br>call ducklake_merge_adjacent_files('eth_lake');<br>select count(*) as files from glob('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/**/*.parquet');<br>select snapshot_id, changes from eth_lake.snapshots() where snapshot_id in (6, 7);<br>call ducklake_expire_snapshots('eth_lake', versions => [6, 7]);<br>call ducklake_cleanup_old_files('eth_lake', dry_run => true, cleanup_all => true);<br>call ducklake_cleanup_old_files('eth_lake', cleanup_all => true);<br>select count(*) as files from glob('/Users/Shared/academy/learner/projects/ethereum_lake/lake/data/**/*.parquet');<br>checkpoint;<br><br>Click **Save** (top right of the editor)<br>(Check that `sql/4_4_maintenance.sql` matches `../snippets/4.4/4_4_maintenance.sql`)<br>Close the editor tab for `sql/4_4_maintenance.sql` (its ×)<br>Click the **Git** tab at the top of the sidebar<br>Hover CHANGES and click **+** (Stage All Changes)<br>Click the message box and type: Maintenance script<br>Click **Commit**<br>git_push: None |
