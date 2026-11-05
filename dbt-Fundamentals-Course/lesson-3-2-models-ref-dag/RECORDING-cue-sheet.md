# Models, ref() and the DAG — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.5, dark theme, window 1920x1080.

## Before you start

- Start state `lesson-3-2-start`: project `dbt_course` with the Lab 1 data in `course.duckdb`, `models/staging` holding `_sources.yml` and the three staging models, and an empty `models/marts`.
- No `target/` or `logs/` folders yet, so the compile in s04 creates them on camera.
- Close every editor tab and start on the home screen (Workspace Overview).
- Bottom panel open on TERMINAL.

## s02 · A model in Rosetta DBT Studio

| Listen for | Do this |
|---|---|
| "Here is one in Rosetta DBT Studio. Open…" | On the home screen, click **dbt_course** under Recent Projects<br>In the Explorer, open `models/staging/stg_orders.sql` (expand each folder on the way) |
| "It is a single select over the raw…" | Hold; nothing moves |
| "The source call on the last line points…" | Point at line 6 |

## s04 · Write fct_orders with ref and compile

| Listen for | Do this |
|---|---|
| "Let's use it. In the marts folder, create…" | Right-click `models/marts` → **New File**, type `fct_orders.sql`, click **Save** |
| "First the orders, straight from the staging orders…" | Type:<br><br>```sql<br>with orders as (<br>    select * from {{ ref('stg_orders') }}<br>),<br>``` |
| "Then the payments, added up per order, from…" | Type:<br><br>```sql<br>payments as (<br>    select order_id, sum(amount) as amount<br>    from {{ ref('stg_payments') }}<br>    group by 1<br>)<br>``` |
| "Finally, one row per order, with its total…" | Type:<br><br>```sql<br>select<br>    o.order_id, o.customer_id, o.order_date, o.status,<br>    coalesce(p.amount, 0) as amount<br>from orders o<br>left join payments p using (order_id)<br>``` |
| "Save it. Then open the Project menu, and…" | Click **Save** (top right of the editor)<br>Open the **Project** menu (arrow next to Project, top right) → **Compile** |
| "Compile turns every model into plain SQL. Nothing…" | Wait for the terminal to finish and the green "dbt compile completed successfully" toast |
| "The result goes into the target folder. Open…" | In the Explorer, open `target/compiled/dbt_course/models/marts/fct_orders.sql` (expand each folder on the way) |
| "The curly braces are gone. In their place…" | Point at line 2 |
| "Point the project at another environment, and the…" | Hold; nothing moves |

## s05 · Lineage in Studio

| Listen for | Do this |
|---|---|
| "Close the compiled copy, which takes you back…" | Close the editor tab for `target/compiled/dbt_course/models/marts/fct_orders.sql` (its ×)<br>Click the **LINEAGE** tab in the bottom panel (it appears after the compile, once the model file is active) |
| "Studio draws this graph from your refs. The…" | Hold; nothing moves |
| "Raise the depth to two, and the raw…" | In the lineage panel, set **Depth** to 2 |
