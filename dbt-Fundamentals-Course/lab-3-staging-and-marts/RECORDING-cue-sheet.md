# Staging and marts on DuckDB (walkthrough) — recording cue sheet

For a human retake of the app scenes (the automated recording follows the same steps). App: Rosetta DBT Studio 1.7.5, dark theme, window 1920x1080.

## Before you start

- Start state `lab-1-end`: project `dbt_course` with the Lab 1 data (raw.customers, raw.orders, raw.payments) in `course.duckdb`, `dbt_project.yml` without a models block, and an empty `models` folder.
- No `target/` or `logs/` folders yet.
- Start on the home screen (Workspace Overview), no editor tabs open, bottom panel on TERMINAL.

## s02 · Folders and sources

| Listen for | Do this |
|---|---|
| "Open the dbt course project. The models folder…" | On the home screen, click **dbt_course** under Recent Projects<br>Point at `models` in the Explorer |
| "Right-click models, choose New Folder, and name it…" | Right-click `models` → **New Folder**, type `staging`, click **Save**<br>Right-click `models` → **New Folder**, type `marts`, click **Save** |
| "In staging, create the sources file. Its name…" | Right-click `models/staging` → **New File**, type `_sources.yml`, click **Save** |
| "It declares one source called raw, in the…" | Type:<br><br>```sql<br>version: 2<br><br>sources:<br>  - name: raw<br>    schema: raw<br>    tables:<br>      - name: customers<br>      - name: orders<br>      - name: payments<br>``` |
| "Save the file. From now on, models read…" | Click **Save** (top right of the editor) |

## s03 · Staging models

| Listen for | Do this |
|---|---|
| "Next, one staging model per source table, starting…" | Right-click `models/staging` → **New File**, type `stg_customers.sql`, click **Save** |
| "Light cleanup only. Rename id to customer id,…" | Type:<br><br>```sql<br>select<br>    id as customer_id,<br>    first_name,<br>    last_name,<br>    email,<br>    cast(created_at as date) as created_at<br>from {{ source('raw', 'customers') }}<br>```<br>Click **Save** (top right of the editor) |
| "Staging orders follows the same pattern: rename the…" | Right-click `models/staging` → **New File**, type `stg_orders.sql`, click **Save**<br>Type:<br><br>```sql<br>select<br>    id as order_id,<br>    customer_id,<br>    cast(order_date as date) as order_date,<br>    status<br>from {{ source('raw', 'orders') }}<br>```<br>Click **Save** (top right of the editor) |
| "Staging payments renames the method, and turns cents…" | Right-click `models/staging` → **New File**, type `stg_payments.sql`, click **Save**<br>Type:<br><br>```sql<br>select<br>    id as payment_id,<br>    order_id,<br>    method as payment_method,<br>    amount_cents / 100.0 as amount<br>from {{ source('raw', 'payments') }}<br>```<br>Click **Save** (top right of the editor) |

## s04 · Marts

| Listen for | Do this |
|---|---|
| "Now the marts. In the marts folder, create…" | Right-click `models/marts` → **New File**, type `fct_orders.sql`, click **Save** |
| "It is the model from Lesson 3.2. First…" | Type:<br><br>```sql<br>with orders as (<br>    select * from {{ ref('stg_orders') }}<br>),<br>``` |
| "Then the payments, added up per order.…" | Type:<br><br>```sql<br>payments as (<br>    select order_id, sum(amount) as amount<br>    from {{ ref('stg_payments') }}<br>    group by 1<br>)<br>``` |
| "And one row per order, with its amount.…" | Type:<br><br>```sql<br>select<br>    o.order_id, o.customer_id, o.order_date, o.status,<br>    coalesce(p.amount, 0) as amount<br>from orders o<br>left join payments p using (order_id)<br>```<br>Click **Save** (top right of the editor) |
| "Next, dim customers: one row per customer.…" | Right-click `models/marts` → **New File**, type `dim_customers.sql`, click **Save** |
| "It keeps the customer columns, and adds the…" | Type:<br><br>```sql<br>select<br>    c.customer_id,<br>    c.first_name,<br>    c.last_name,<br>    c.email,<br>    min(o.order_date) as first_order_date,<br>    count(o.order_id) as order_count,<br>    coalesce(sum(o.amount), 0) as lifetime_value<br>``` |
| "Those come from fact orders, joined on customer…" | Type:<br><br>```sql<br>from {{ ref('stg_customers') }} c<br>left join {{ ref('fct_orders') }} o using (customer_id)<br>group by 1, 2, 3, 4<br>```<br>Click **Save** (top right of the editor) |

## s05 · Materializations

| Listen for | Do this |
|---|---|
| "Open dbt project dot yml, and go to…" | In the Explorer, open `dbt_project.yml` (expand each folder on the way) |
| "Add a models block. Everything in staging becomes…" | Click at the end of the file and type:<br><br>```yaml<br><br>models:<br>  dbt_course:<br>    staging:<br>      +materialized: view<br>    marts:<br>      +materialized: table<br>``` |
| "Save it. These are folder defaults, and a…" | Click **Save** (top right of the editor) |

## s06 · Compile and run

| Listen for | Do this |
|---|---|
| "Now open the Project menu, and choose Compile.…" | Open the **Project** menu (arrow next to Project, top right) → **Compile**<br>Wait for the terminal to finish and the green "dbt compile completed successfully" toast |
| "In target, compiled, open fact orders. Every ref…" | In the Explorer, open `target/compiled/dbt_course/models/marts/fct_orders.sql` (expand each folder on the way)<br>Point at line 2 |
| "Then the Project menu again, and Run.…" | Open the **Project** menu (arrow next to Project, top right) → **Run**<br>Wait for the terminal to finish and the green "dbt compile completed successfully" toast |
| "Five models, built in dependency order: three views…" | Hold; nothing moves |

## s07 · Check the result

| Listen for | Do this |
|---|---|
| "Let's check the data. Open the SQL Editor,…" | In the left bar, click **SQL Editor**<br>Open the connection list (top left) and pick **course**<br>Type:<br><br>```sql<br>select customer_id, first_name, order_count, lifetime_value from dim_customers order by lifetime_value desc;<br>``` |
| "Run it with the green arrow next to…" | Click the green ▶ arrow next to line 1 |
| "Ava comes first, with three orders and one…" | Hold; nothing moves |

## s08 · The whole lineage

| Listen for | Do this |
|---|---|
| "Last, the lineage. Back in the project, open…" | In the left bar, click **DBT Studio**<br>In the Explorer, open `models/marts/dim_customers.sql` (expand each folder on the way)<br>Click the **LINEAGE** tab in the bottom panel (it appears after the compile, once the model file is active) |
| "Maximize it, and set the depth to three.…" | Click **Maximize** (top right of the lineage panel)<br>In the lineage panel, set **Depth** to 3<br>Click the fit-view button (bottom left of the graph) |
| "That is the whole lab in one picture:…" | Hold; nothing moves |
