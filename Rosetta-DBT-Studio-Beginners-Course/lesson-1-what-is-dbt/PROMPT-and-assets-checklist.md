# Lesson 1 - What is dbt? - screenshots

3 shots, **1920x1080 PNG**. Exact filenames - the HTML references them by name.
The PNGs in this folder were carried over from the original what-is-dbt deck and are already real
captures. Only recapture if the UI has moved.

**Scope note**: this lesson is dbt-only. The old 4th shot (`one-window-workspace.png`) belonged to a
"why you want an app" slide that has been removed - that ground is now covered by Lesson 0
(What is Rosetta DBT Studio?). Do not re-add it here.

## Setup

- Project: **`jaffle_shop_duckdb`**
- Taskbar on auto-hide, **maximize** the window, capture with **PrtScn** (not `Win+Shift+S` - it adds
  the drop shadow and you get ~1936x1096).
- In the app terminal: **`dbt seed`** then **`dbt run`**. Seed first - the models `ref()` the seeds.
- **Restart the app.** The LINEAGE tab stays hidden otherwise (known bug: the "no manifest" result
  gets cached and nothing invalidates it after a run).
- Restarting clears the terminal, so **run `dbt run` again**. Instant the second time.
- Don't resize between shots - the status bar versions must match across all three.

## Shoot in this order

Deck slide order is SQL -> run -> lineage. Capture order below is different on purpose - you must run
dbt before the lineage tab exists.

### 1. `run-output-success.png` -> slide 3

Terminal straight after `dbt run`. Needs `Completed successfully` and `Done. PASS=5` visible.

Card sits **TOP-RIGHT** - keep the output lower/left.

### 2. `dbt-builds-the-order.png` -> slide 4

Select **`customers.sql`**, open the **LINEAGE** tab, collapse the editor so the graph fills the pane.

Use `customers.sql`, not `stg_customers.sql` - it refs all three staging models, so you get a 7-node
fan-in instead of a thin 3-node chain.

Card sits **TOP-RIGHT** on this slide (over the editor), so the whole graph stays clear.

### 3. `model-is-a-select.png` -> slide 2

Open **`models/staging/stg_customers.sql`** (22 lines, fits with no scrolling). **TERMINAL** tab
selected, not LINEAGE - the graph is slide 4's reveal.

Card sits **BOTTOM-RIGHT** - the SQL is short and left-aligned, so the right side is empty.

## Record

Open `video-presentation.html`, press `F`, arrow through 5 slides reading `voiceover-script-80sec.md`.
