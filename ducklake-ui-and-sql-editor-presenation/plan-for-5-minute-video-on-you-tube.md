# 5-Minute YouTube Video Plan: Rosetta DBT studio DuckLake UI + SQL Editor

## Goal

Create a polished 5-minute YouTube product video that promotes Rosetta DBT studio as a modern desktop workspace for data teams, with a focused spotlight on the DuckLake UI, SQL Editor, and SQL Notebooks.

The video should feel like a high-quality SaaS product demo: clear, practical, energetic, and visually grounded in real screenshots. Use the provided screenshots and logo assets from:

`presentations/ducklake-ui-and-sql-editor-presenation/`

## Core Message

Rosetta DBT studio brings data lake management, SQL exploration, notebooks, cloud storage, database connections, and AI-assisted analytics into one desktop workspace. With DuckLake support, teams can create new lakehouse instances, import existing DuckLakes, inspect metadata, query data, export results, and work interactively through SQL notebooks.

Under the hood, Rosetta DBT studio uses `@duckdb/node-api`, the DuckDB Node.js API, to connect to DuckDB and power DuckLake workflows through DuckDB's DuckLake extension.

## Audience

Data engineers, analytics engineers, lakehouse users, dbt users, BI/analytics teams, and technical founders who want a local-first desktop workflow for DuckLake, DuckDB, cloud object storage, and SQL analytics.

## Tone And Style

- Professional, modern, confident, and practical.
- Fast enough to feel engaging, but not rushed.
- Use real UI screenshots as the primary visual evidence.
- Add subtle zooms, pans, cursor highlights, and callout labels.
- Use clean typography and short on-screen text.
- Avoid generic stock imagery except for abstract background moments between sections.
- Music: modern technology beat, warm, minimal, not overpowering.
- Voice: clear, calm, optimistic, technical but accessible.

## Visual Brand Direction

- Primary brand asset: `logo_new_05.png`
- Use dark UI-friendly backgrounds, soft shadows, and orange accent highlights inspired by the logo.
- Keep screenshots crisp and readable.
- Use full-screen product shots whenever possible.
- Use animated overlays for key words such as "DuckLake", "SQL Editor", "Notebooks", "Cloud Storage", "Metadata", "Export", and "Snapshots".

## Required Assets

Use these assets as the main visual sequence:

- `logo_new_05.png`
- `database-connection-suported.png`
- `database-and-sorage-object-connections.png`
- `database-connection-create-example.png`
- `create-cloud-object-storage-types.png`
- `create-ducklake-instance-details.png`
- `create-ducklake-catalog-configuration.png`
- `create-ducklake-storage-configuration.png`
- `create-ducklake-runtime-options.png`
- `create-ducklake-review.png`
- `ducklake_overview.png`
- `tables_and_views.png`
- `table_overview.png`
- `table_schema.png`
- `table-data.png`
- `table-statistics.png`
- `table-parque-files.png`
- `table-partitions.png`
- `table-snapshot-history.png`
- `table-schema-add-column.png`
- `table-schema-rename-column.png`
- `table-schema-alter-column-type.png`
- `table-schem-delete-column.png`
- `table-data-update-rows.png`
- `table-data-delete-rows.png`
- `import-data-from-storage.png`
- `import-data-from-url.png`
- `sql-editor-schema-view.png`
- `sql-editor-autocomplete.png`
- `sql-editor-autocomplete-01.png`
- `sql-editor-query-data.png`
- `sql-editor-preview-and export-data.png`
- `sql-notebooks_01.png`
- `sql-notebooks-02.png`
- `sql-notebooks-03.png`

## Video Structure

### 0:00-0:20 - Hook: One Workspace For DuckLake

**Visuals**

- Start with `logo_new_05.png` centered on a dark background.
- Quick cuts of `ducklake_overview.png`, `sql-editor-query-data.png`, and `sql-notebooks_01.png`.
- Add kinetic text overlays:
  - "Rosetta DBT studio"
  - "DuckLake UI"
  - "SQL Editor"
  - "SQL Notebooks"

**Voiceover**

"Meet Rosetta DBT studio: a desktop workspace for modern data teams. Manage DuckLake lakehouses, connect to cloud storage, explore metadata, query data, and build notebook workflows without jumping between tools."

"Under the hood, Rosetta DBT studio uses the DuckDB Node.js API to connect to DuckDB and power DuckLake workflows through DuckDB's DuckLake extension."

**On-Screen Text**

"Rosetta DBT studio: DuckLake, SQL, Notebooks, and Cloud Data in one workspace"

### 0:20-0:55 - The Problem: Data Work Is Fragmented

**Visuals**

- Show a soft abstract transition from multiple scattered panels into a single Rosetta DBT studio workspace.
- Use `database-connection-suported.png` and `database-and-sorage-object-connections.png`.
- Highlight icons for PostgreSQL, Snowflake, BigQuery, DuckDB, S3, Azure Blob, GCS, and DuckLake from the visible UI.

**Voiceover**

"Data work often gets split across database clients, cloud consoles, SQL tools, notebooks, and file explorers. Rosetta DBT studio brings those workflows together, so teams can move from connection setup to analysis and lakehouse operations in one focused interface."

**On-Screen Text**

"Less context switching. More productive data work."

### 0:55-1:35 - Connections: Databases And Cloud Storage

**Visuals**

- Show `database-connection-create-example.png`.
- Show `create-cloud-object-storage-types.png`.
- Show `database-and-sorage-object-connections.png`.
- Animate a simple path: "Connect -> Browse -> Reuse in DuckLake".

**Voiceover**

"Start by connecting the systems your team already uses. Rosetta DBT studio supports database connections and cloud object storage, including S3-compatible storage, Azure Blob, and Google Cloud Storage. Those saved cloud connections can be reused when creating new DuckLake instances or importing existing DuckLakes, keeping setup clean and secure."

**On-Screen Text**

"Database connections + cloud object storage"

### 1:35-2:15 - Create Or Import A DuckLake Instance

**Visuals**

- Walk through the wizard using:
  - `create-ducklake-instance-details.png`
  - `create-ducklake-catalog-configuration.png`
  - `create-ducklake-storage-configuration.png`
  - `create-ducklake-runtime-options.png`
  - `create-ducklake-review.png`
- Add subtle numbered step labels:
  - "1. Instance"
  - "2. Catalog"
  - "3. Storage"
  - "4. Runtime"
  - "5. Review"

**Voiceover**

"The DuckLake setup flow guides you through the essentials: instance details, catalog configuration, storage location, runtime options, and final review. You can create a new DuckLake or import an existing one by connecting the metadata catalog and data storage, matching the way DuckLake is designed to work."

**On-Screen Text**

"Create or import DuckLake instances with guided setup"

### 2:15-2:55 - DuckLake UI: Manage Tables, Metadata, And History

**Visuals**

- Show `ducklake_overview.png`.
- Show `tables_and_views.png`.
- Show `table_overview.png`.
- Show `table_schema.png`.
- Show `table-statistics.png`.
- Show `table-parque-files.png`.
- Show `table-partitions.png`.
- Show `table-snapshot-history.png`.
- Use zoom-ins on table names, schema columns, statistics, files, partitions, and snapshots.

**Voiceover**

"Once the instance is running, Rosetta DBT studio becomes a visual control center for DuckLake. Browse tables and views, inspect schemas, review statistics, see Parquet data files, examine partitions, and follow snapshot history. It gives teams a practical way to understand what is inside the lakehouse, not just query it."

**On-Screen Text**

"Tables, schemas, files, partitions, statistics, snapshots"

### 2:55-3:25 - Table Operations And Data Import

**Visuals**

- Show:
  - `table-schema-add-column.png`
  - `table-schema-rename-column.png`
  - `table-schema-alter-column-type.png`
  - `table-schem-delete-column.png`
  - `table-data-update-rows.png`
  - `table-data-delete-rows.png`
  - `import-data-from-storage.png`
  - `import-data-from-url.png`
- Use split-screen layout: schema changes on left, data import/update actions on right.

**Voiceover**

"The DuckLake UI is built for real operations: schema evolution, row updates, deletes, and importing data from cloud storage or URLs. It helps turn lakehouse management into a guided workflow instead of a set of disconnected commands."

**On-Screen Text**

"Schema evolution. Data changes. Imports."

### 3:25-4:05 - SQL Editor For DuckLake

**Visuals**

- Show `sql-editor-schema-view.png` as the sidebar schema browser.
- Show `sql-editor-autocomplete.png` and `sql-editor-autocomplete-01.png`.
- Show `sql-editor-query-data.png`.
- Show `sql-editor-preview-and export-data.png`.
- Add callouts:
  - "DuckLake instances in connection dropdown"
  - "Schema browser"
  - "Autocomplete"
  - "Server-side pagination"
  - "Export CSV, JSON, Parquet"

**Voiceover**

"DuckLake also works directly inside the SQL Editor. Select a DuckLake instance, browse schemas, get Monaco-powered autocomplete for tables and columns, run queries, page through large results, and export full datasets to CSV, JSON, or Parquet."

**On-Screen Text**

"Query DuckLake directly in the SQL Editor"

### 4:05-4:40 - SQL Notebooks For Repeatable Analysis

**Visuals**

- Show:
  - `sql-notebooks_01.png`
  - `sql-notebooks-02.png`
  - `sql-notebooks-03.png`
- Animate multiple notebook cells running one after another.
- Highlight SQL cells, markdown cells, output table, and notebook tabs.

**Voiceover**

"For deeper analysis, SQL Notebooks provide a cell-based workflow with SQL and Markdown. Create reusable notebooks, run cells against DuckLake or database connections, keep results paginated for large tables, and document the analysis as you go."

**On-Screen Text**

"SQL + Markdown notebooks for repeatable analytics"

### 4:40-5:00 - Closing: Build With Rosetta DBT studio

**Visuals**

- Fast montage of the strongest screenshots:
  - `ducklake_overview.png`
  - `tables_and_views.png`
  - `sql-editor-query-data.png`
  - `sql-notebooks_01.png`
- End with the CTA screen: `logo_new_05.png`, "Ready to build your lakehouse?", and download buttons for macOS, Windows, and Linux.
- Show a final prompt: "Star us on GitHub" with the repository link.

**Voiceover**

"Rosetta DBT studio brings DuckLake management, SQL exploration, notebooks, cloud storage, and AI-ready analytics into one desktop experience. Download the Rosetta DBT studio desktop app today for macOS, Windows, or Linux, and join our community on GitHub. Let’s build the modern lakehouse together."

**On-Screen Text**

"Ready to build your lakehouse? Download Rosetta DBT studio for macOS, Windows, and Linux. Star us on GitHub."

## Full Voiceover Script

Meet Rosetta DBT studio: a desktop workspace for modern data teams. Manage DuckLake lakehouses, connect to cloud storage, explore metadata, query data, and build notebook workflows without jumping between tools.

Under the hood, Rosetta DBT studio uses the DuckDB Node.js API to connect to DuckDB and power DuckLake workflows through DuckDB's DuckLake extension.

Data work often gets split across database clients, cloud consoles, SQL tools, notebooks, and file explorers. Rosetta DBT studio brings those workflows together, so teams can move from connection setup to analysis and lakehouse operations in one focused interface.

Start by connecting the systems your team already uses. Rosetta DBT studio supports database connections and cloud object storage, including S3-compatible storage, Azure Blob, and Google Cloud Storage. Those saved cloud connections can be reused when creating new DuckLake instances or importing existing DuckLakes, keeping setup clean and secure.

The DuckLake setup flow guides you through the essentials: instance details, catalog configuration, storage location, runtime options, and final review. You can create a new DuckLake or import an existing one by connecting the metadata catalog and data storage, matching the way DuckLake is designed to work.

Once the instance is running, Rosetta DBT studio becomes a visual control center for DuckLake. Browse tables and views, inspect schemas, review statistics, see Parquet data files, examine partitions, and follow snapshot history. It gives teams a practical way to understand what is inside the lakehouse, not just query it.

The DuckLake UI is built for real operations: schema evolution, row updates, deletes, and importing data from cloud storage or URLs. It helps turn lakehouse management into a guided workflow instead of a set of disconnected commands.

DuckLake also works directly inside the SQL Editor. Select a DuckLake instance, browse schemas, get Monaco-powered autocomplete for tables and columns, run queries, page through large results, and export full datasets to CSV, JSON, or Parquet.

For deeper analysis, SQL Notebooks provide a cell-based workflow with SQL and Markdown. Create reusable notebooks, run cells against DuckLake or database connections, keep results paginated for large tables, and document the analysis as you go.

Rosetta DBT studio brings DuckLake management, SQL exploration, notebooks, cloud storage, and AI-ready analytics into one desktop experience. Download the Rosetta DBT studio desktop app today for macOS, Windows, or Linux, and join our community on GitHub. Let’s build the modern lakehouse together.

## AI Video Generator Prompt

Create a 5-minute YouTube product video promoting Rosetta DBT studio, focusing on its DuckLake UI, SQL Editor, and SQL Notebooks. Use the provided image assets as the primary visuals. The video must include professional narration, modern technology background music, subtle UI zooms, cursor highlights, clean callout labels, and short on-screen text.

Style: polished SaaS product demo, dark modern interface, orange accent highlights matching the Rosetta DBT studio logo, crisp readable screenshots, smooth transitions, confident but practical tone. Avoid generic stock footage unless used only as subtle abstract transitions. Do not invent UI screens; use the supplied screenshots.

Use this structure:

1. 0:00-0:20: Open with `logo_new_05.png`, then quick montage of `ducklake_overview.png`, `sql-editor-query-data.png`, and `sql-notebooks_01.png`. On-screen text: "Rosetta DBT studio: DuckLake, SQL, Notebooks, and Cloud Data in one workspace."
2. 0:20-0:55: Show the problem of fragmented data workflows using `database-connection-suported.png` and `database-and-sorage-object-connections.png`. On-screen text: "Less context switching. More productive data work."
3. 0:55-1:35: Show connection setup using `database-connection-create-example.png`, `create-cloud-object-storage-types.png`, and `database-and-sorage-object-connections.png`. Emphasize database and cloud object storage connections.
4. 1:35-2:15: Show the DuckLake setup wizard with `create-ducklake-instance-details.png`, `create-ducklake-catalog-configuration.png`, `create-ducklake-storage-configuration.png`, `create-ducklake-runtime-options.png`, and `create-ducklake-review.png`. Emphasize that users can create new DuckLakes or import existing ones.
5. 2:15-2:55: Show DuckLake management using `ducklake_overview.png`, `tables_and_views.png`, `table_overview.png`, `table_schema.png`, `table-statistics.png`, `table-parque-files.png`, `table-partitions.png`, and `table-snapshot-history.png`.
6. 2:55-3:25: Show table operations and imports using `table-schema-add-column.png`, `table-schema-rename-column.png`, `table-schema-alter-column-type.png`, `table-schem-delete-column.png`, `table-data-update-rows.png`, `table-data-delete-rows.png`, `import-data-from-storage.png`, and `import-data-from-url.png`.
7. 3:25-4:05: Show DuckLake in the SQL Editor using `sql-editor-schema-view.png`, `sql-editor-autocomplete.png`, `sql-editor-autocomplete-01.png`, `sql-editor-query-data.png`, and `sql-editor-preview-and export-data.png`. Add callouts for schema browser, autocomplete, pagination, and export.
8. 4:05-4:40: Show SQL Notebooks using `sql-notebooks_01.png`, `sql-notebooks-02.png`, and `sql-notebooks-03.png`. Highlight SQL cells, Markdown cells, output tables, notebook tabs, and repeatable analysis.
9. 4:40-5:00: Closing montage with `ducklake_overview.png`, `tables_and_views.png`, `sql-editor-query-data.png`, `sql-notebooks_01.png`. End on the CTA screen: `logo_new_05.png`, "Ready to build your lakehouse?", download buttons for macOS, Windows, Linux, and "Star us on GitHub". On-screen text: "Ready to build your lakehouse? Download Rosetta DBT studio for macOS, Windows, and Linux. Star us on GitHub."

Use the full voiceover script from this plan. Time the visuals to match the narration. Make sure all screenshot text remains readable. Use subtle camera movements: slow zoom in, pan, crop to important UI areas, and highlight boxes around relevant controls. Keep text overlays short and readable.

## Thumbnail Concept

Use `logo_new_05.png` on the left and a collage of `ducklake_overview.png`, `sql-editor-query-data.png`, and `sql-notebooks_01.png` on the right.

Thumbnail text:

"DuckLake in Rosetta DBT studio"

Small supporting text:

"UI + SQL Editor + Notebooks"

## YouTube Metadata Draft

**Title**

Rosetta DBT studio DuckLake UI: SQL Editor, Notebooks, Cloud Storage, and Lakehouse Management

**Description**

Explore Rosetta DBT studio's DuckLake workflow: create new DuckLake instances, import existing DuckLakes, connect cloud storage, browse tables and metadata, inspect snapshots, run SQL, export data, and build repeatable SQL notebooks.

This 5-minute demo shows how Rosetta DBT studio brings DuckLake management, SQL exploration, notebooks, database connections, and cloud object storage into one desktop workspace. Download the app for macOS, Windows, or Linux and start building.

GitHub: https://github.com/rosettadb/dbt-studio

**Tags**

Rosetta DBT studio, DuckLake, DuckDB, SQL Editor, SQL Notebooks, lakehouse, data engineering, analytics engineering, cloud storage, S3, Azure Blob, Google Cloud Storage, Parquet, dbt, data platform
