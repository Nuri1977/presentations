# Transactions and conflicts — voice-over script and beat sheet

Data Lakes with DuckLake in Rosetta DBT Studio · Module 3 · Changing data · next: Lesson 4.1 · Partitioning

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `lesson-3-4-end`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 2 · Lesson 3.5. Transactions and conflicts.

## s01 · slide — slide `tx`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | A transaction groups changes. Here, a delete in one table and a new table, between begin and commit. The lake records both in one snapshot, or nothing at all. | Code: BEGIN; DELETE FROM raw.blocks_day …; CREATE TABLE raw.scratch …; COMMIT; → one snapshot for both. | 29 | 11 |
| b02 @0:13 | Change commit to rollback, and it is as if nothing happened: no files are added to the table, and no snapshot is created. | ROLLBACK instead of COMMIT: nothing happened, no snapshot. | 23 | 9 |

## s02 · app — Rosetta DBT Studio

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b03 @0:22 | In Studio's SQL Editor, every statement is its own transaction. Try to start one by hand: begin transaction. | Left bar → **SQL Editor**<br>Pick the connection **eth_lake**<br>Type 18 characters into the editor<br>Zoom: explorer | 18 | 10 |
| b04 @0:32 | Studio refuses it, and lists the statement types it accepts. To group changes, use a SQL client that keeps one session open, or a tool like dbt. | Click the green run arrow next to line 1<br>Zoom: sql-results<br>Card: *Studio 1.7.6* — **One statement, one transaction** — BEGIN is not accepted in the SQL Editor | 27 | 11 |

## s03 · slide — slide `writers`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b05 @0:43 | What about two writers at the same time? DuckLake is optimistic. Both work without locking. When the second one commits, it is checked against what the first one already committed. | Optimistic concurrency: both writers work; at commit, the second is checked against what the first committed. | 30 | 11 |
| b06 @0:54 | Two inserts into the same table do not conflict, and neither do changes to different tables. DuckLake simply retries the commit on top. | No conflict: two appends to the same table; changes to different tables. | 23 | 9 |
| b07 @1:02 | But if both delete rows from the same data file, or both change the same table's schema, the second commit fails, and that writer must try again. | Conflict: both delete from the same data file; both change the same table's schema. The second commit fails. | 27 | 10 |

## s04 · slide — slide `lock`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b08 @1:12 | All of this needs a catalog that many programs can open, like PostgreSQL. Our catalog is a DuckDB file, and a DuckDB file can be opened by one program at a time. | A DuckDB catalog file: one program at a time opens it. PostgreSQL or MySQL catalog: many writers. | 32 | 12 |
| b09 @1:24 | We will see that in Module 6: while Studio has the lake open, dbt cannot open it. Fine on a laptop, but a shared lake needs a shared catalog. | Seen in Module 6: while Studio has the lake open, dbt gets 'Conflicting lock is held'. | 29 | 10 |

## s05 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b10 @1:34 | To recap: a transaction is all or nothing, and one snapshot. In Studio's SQL Editor every statement is its own transaction. Appends do not conflict, deletes in the same file do. And a DuckDB catalog file means one program at a time. That ends Module 3. Next: performance, starting with partitioning. | Recap: transactions are all or nothing; Studio's SQL Editor runs one statement per transaction; appends do not conflict, deletes in the same file do; a DuckDB catalog means one writer. | 51 | 21 |

## s06 · closing card (4 s, no voice)

Next · Lesson 4.1 · Partitioning.

**Total: 289 spoken words, 1:59 rendered.**
