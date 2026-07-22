# What is dbt? — screenshots

4 shots, **1920x1080 PNG**. Exact filenames — the HTML references them by name.
The PNGs currently in this folder are placeholders; overwrite them in place.

## Setup

- Project: **`jaffle_shop_duckdb`**
- Taskbar on auto-hide, **maximize** the window, capture with **PrtScn** (not `Win+Shift+S` — it adds
  the drop shadow and you get ~1936x1096).
- In the app terminal: **`dbt seed`** then **`dbt run`**. Seed first — the models `ref()` the seeds.
- **Restart the app.** The LINEAGE tab stays hidden otherwise (known bug: the "no manifest" result
  gets cached and nothing invalidates it after a run).
- Restarting clears the terminal, so **run `dbt run` again**. Instant the second time.
- Don't resize between shots — the status bar versions must match across all four.

## Shoot in this order

Deck slide order is SQL → run → lineage → workspace. Capture order below is different on purpose —
you must run dbt before the lineage tab exists.

### 1. `run-output-success.png` → slide 3

Terminal straight after `dbt run`. Needs `Completed successfully` and `Done. PASS=5` visible.

Card sits **TOP-RIGHT** — keep the output lower/left.

### 2. `dbt-builds-the-order.png` → slide 4

Select **`customers.sql`**, open the **LINEAGE** tab, collapse the editor so the graph fills the pane.

Use `customers.sql`, not `stg_customers.sql` — it refs all three staging models, so you get a 7-node
fan-in instead of a thin 3-node chain.

Card sits **TOP-RIGHT** on this slide (over the editor), so the whole graph stays clear. Bottom-right
put the card straight on top of the `customers` node — the convergence point of the fan-in.

### 3. `model-is-a-select.png` → slide 2

Open **`models/staging/stg_customers.sql`** (22 lines, fits with no scrolling). **TERMINAL** tab
selected, not LINEAGE — the graph is slide 4's reveal.

Card sits **BOTTOM-RIGHT** — the SQL is short and left-aligned, so the right side is empty.

### 4. `one-window-workspace.png` → slide 5

The whole app: tree, editor, terminal. Your call on the AI panel — the narration never mentions AI,
and the card only covers its lower half.

Card sits **BOTTOM-RIGHT**.

## Record

Open `video-presentation.html`, press `F`, arrow through 6 slides reading `voiceover-script-90sec.md`.
