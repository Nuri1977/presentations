# Corrections for the course draft

Found while producing the videos. Apply these to `Academy-course-request-01/dbt_course_draft.docx.md`.
UI labels were already used in the videos; factual flags are waiting for your decision.

## Factual flags (decision needed)

| # | Where in the draft | Draft says | What the app shows | Affects |
|---|---|---|---|---|
| F1 | Open items: "Rosetta DBT Studio runs dbt Core v1"; Lesson 2.2; Lab 2 Part 3 | Studio embeds dbt Core v1 only; v2 is a command-line side lab | The 1.7.5 source has a dbt Core version switch in the dbt settings that installs v2 (`dbt-core@2.0.5`, shipped as `dbt-oss`, needs Python 3.11+). Not yet checked in the UI. The default install is still v1 (1.12.6 here). | Lessons 2.2, 2.3, 2.5; Lab 2 Part 3 could become an in-Studio demo |

## UI labels (already used in the videos)

| # | Where in the draft | Draft says | Real label in 1.7.5 |
|---|---|---|---|
| L1 | Lab 3 step 5.2, Lesson 3.2 | "Run dbt compile" / "Use the Run button or the command runner" | **Project** menu (top right) → **Compile**. The same menu has Run, Test, Build, Generate Docs, Serve Docs, Clean, Deps, Seed. |
| L2 | Lab 3 "Use the file explorer to create folders" | file explorer | **Explorer** tab in the left sidebar; right-click a folder → **New File** / **New Folder**, then type the name and click **Save**. |
| L3 | Lab 3 step 5.4, Lesson 4.3 | "Open the lineage or docs view" | **LINEAGE** tab in the bottom panel. It appears only when a SQL model is open and the project has been compiled (or run) at least once. Default depth is 1; a **Depth** selector raises it. |
| L4 | Lab 2 Part 1 step 1 | "Open the terminal or command runner and run dbt --version" | Bottom panel **TERMINAL** tab, prompt "Type a rosetta or dbt command...". The status bar (bottom right) also shows the dbt and Python versions. |
| L5 | Lab 1 setup steps 2-3 | "create a new project", "create a new connection of type DuckDB" | Home screen buttons are **New Connection**, **Open Project** and **Settings**. The new-project flow has not been checked yet; it will be when Lab 1 is recorded. |
