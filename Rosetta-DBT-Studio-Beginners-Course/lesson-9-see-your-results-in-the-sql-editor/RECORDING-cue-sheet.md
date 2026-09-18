# Lesson 9 - Recording Cue Sheet

The first look at the data the models actually contain. One query, run against a staging model rather than the raw table, with the payoff that a view stores nothing and is never stale.

Full frame cards are `slides/1.png` (intro) and `slides/9.png` (closing).

App version: **1.6.6**.

## Before you hit F9

- **Lesson 8 must have run.** The nine objects have to exist, or slide 3 and slide 5 both fall over.
- Open the **SQL Editor** from the sidebar, with **no connection selected yet**. Slide 2 is the selection, so it has to happen on camera.
- If you have been testing, clear Saved Queries (right-click the entry, Delete) and Query History for this connection first, so slides 7 and 8 land on empty lists filling up rather than on someone else's leftovers.
- **Count the tree before you start.** All nine objects have to be under `main`. If only the five tables
  show and the four `main_*` views are missing, **fully quit and reopen the app**. Refresh Schema alone
  does not bring them back, and it happens after an update if the old build is still running. Hit 28 Aug
  2026 on 1.6.6. The views are in the database either way, so slide 4 runs regardless.
- Dark theme, app maximized, taskbar auto-hidden.

## Beats

| Listen for | Do this |
|---|---|
| "It talks to a database" | Sit on the empty SQL Editor, nothing selected |
| "So what it asks for is a connection" | Open Select Connection |
| "and you already have one" | Hold the picker open on `DBT Connection`, then choose it as the line ends |
| "The Data tab is the database, laid out" | Expand the schema so tables and views are both visible |
| "Now ask it a question" | Paste the query, it is already on the clipboard |
| "Notice where it reads from" | Point at `main_students` in the FROM clause |
| "Run it, and the rows come back underneath" | Run, let the grid land |
| "Four majors" | Point down the four rows |
| "Switch it to Chart" | Click **Chart** above the result, let the bars land |
| "other chart types to choose from" | Open **Chart Type**, pick **Pie Chart**, hold on it |
| "That model is a view, and a view stores no rows at all" | Hold on the result, nothing to click |
| "If it is a query that you will want again, save it" | Save Query, name it `Students by major`, not the default "Query #1" |
| "still there the next time you open this database" | Click the **Queries** tab, hold on the saved entry |
| "The editor keeps a history of what you ran" | Open Query History |

## The query

Have this on the clipboard before you hit F9, and paste it. Typing it live took 40 seconds on the
first attempt, against about 11 seconds of narration, so the take drifts badly. Nothing in the script
says you are typing.

```sql
select major, count(*) as students
from main_students
group by major
order by students desc
```

## The answer, verified

Run against the real database, so this is what should come back:

| major | students |
|---|---|
| Physics | 29 |
| Mathematics | 28 |
| Computer Science | 24 |
| Literature | 19 |

Four rows, and they add to 100. If you get anything else, lesson 8 did not run cleanly.

## What should be in the Data tab

Nine objects in schema `main`, all 100 rows.

| Kind | Names |
|---|---|
| Tables | `courses`, `enrollments`, `grades`, `students` |
| Views | `main_courses`, `main_enrollments`, `main_grades`, `main_students` |
| Table, incremental | `enh_main_grades` |

If a model is missing from the tree, use **Refresh Schema** rather than restarting. The schema is cached.

## Card placement, and why it is not a guess

**All seven cards sit bottom left.** This is the one placement in the series that is already settled by real footage: lesson 4 found that the SQL Editor and Notebooks both open the **AI panel on the right**, and a right hand card is covered by it. Lesson 4's cards 3 and 4 were moved left for exactly this reason.

Do not move these right without checking the take first.

## Timing

Everything is under your control. The query returns four rows instantly. Slide 3 of the old script ("Open Select Connection, and pick DBT Connection") was merged into slide 2 on 18 Sep 2026, so the selection now happens during slide 2's narration and the script is a few seconds shorter than the 137 seconds it used to be.

## Recording

F9, wait 3 seconds, start the Kokoro MP3 on your phone, perform the beats in sync. Let it run 3 seconds past the last word before F9 again.
