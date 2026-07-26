# plan-presentation — dbt Query Results & Run History

## Release Context

Release: **1.6.1** (Latest)
Tag: [version/1.6.1](https://github.com/rosettadb/dbt-studio/releases/tag/1.6.1)
Feature focus: **Add dbt Query Results and Run History functionality (#327)**

Other 1.6.1 highlights shipped alongside this feature:
- AI Agent assist action in the Terminal (#348)
- HTML Viewer in the Editor (#352)
- Cloud Explorer downloads inside the app (#318)
- Getting Started Pipeline tab & auto-expanding Cloud Logs (#349)
- Secrets loading and Push to Cloud recovery (#350)
- Saved queries single-click open & SQL editor modified indicator (#351)
- Analytics pie chart label fix (#353)
- Cloud Logs fullscreen landing fix (#357)
- Run History loading-state recovery (#359)

---

## Why This Feature Exists

Before 1.6.1, dbt results in Rosetta DBT Studio were scattered:
- You ran a model preview. The rows opened in a modal.
- You ran `dbt run`. The output lived in the Terminal scrollback.
- You wanted the same query from yesterday. It was gone.
- You wanted to compare raw SQL vs compiled SQL. Two different places.
- A test failed. The error was in a log, not next to the result.

The #327 release fixes that. It mirrors the workflow that `vscode-dbt-power-user` users already know, but built natively into DBT Studio's Electron + React workspace — not layered on top of VS Code's extension APIs.

---

## What We Built — At a Glance

Two new bottom-panel tabs in the selected-project screen, both persisted per project in `localStorage`:

### 1. QUERY RESULTS tab
A tabbed results panel for every SQL / model preview execution.

Inner tabs:
- **Preview** — Result grid with row count, elapsed time, pagination, export.
- **SQL** — Side-by-side `Compiled SQL` and `Raw SQL` with one-click Copy.
- **History** — Flat list of every past query: green `<>` icon, truncated SQL, timestamp; hover shows `Run` + `Bookmark` actions.
- **Bookmarks** — Saved queries per project. Add via dialog (name + tags). Run or delete.

Toolbar:
- `Limit` input (default 500)
- `Run` button ▶
- `Clear results` 🧹
- `Fullscreen` ⛶

Editor integration:
- Monaco `Execute Query` CodeLens at the top of every dbt SQL file.
- Monaco `Execute CTE: <name>` CodeLens above each detected CTE — runs just that CTE plus its dependencies, same behavior Power User users know.
- Auto-switch to `QUERY RESULTS` when a query starts or completes.

### 2. RUN HISTORY tab
A first-class history surface for every dbt command you invoke locally.

Captures:
- `dbt run`, `dbt test`, `dbt build`, `dbt compile`, `dbt seed`, `dbt snapshot`, `dbt deps`, `dbt debug` — everything that goes through `useDbt()`.
- Parses `target/run_results.json` for commands that produce it (run, test, seed, snapshot) for invocation id, per-model/test child rows, statuses, execution times, messages, compiled SQL, relation names, adapter responses.
- Commands without artifacts (deps, compile, debug) still finalize as success rows with elapsed time — no orphaned "running" entries.

Parent row (each dbt invocation):
- Status icon (success / error / warn / cancelled)
- Command string, project name, duration
- Summary counts: total, passed, error, warn, skipped
- Start / completed timestamps, invocation id
- Copy command button (full shell command)
- `Fix with AI` button when failed — opens Project Agent with command, stderr/stdout summary, and log tail.

Expandable child rows (per model / test / seed / snapshot):
- Name, resource type, status, execution time
- Message tooltip / detail
- Unique id
- Compiled SQL / relation name when dbt artifacts included them
- `Explain failure` button on failed or warn children — opens Project Agent with result details.

Toolbar:
- Status filter (All Statuses — includes `Cancelled`)
- Text search over command / result name
- Clear history (with confirmation Dialog)
- Fullscreen ⛶

### Reliability details
- History capped at **50 entries** per project (oldest FIFO out).
- Deduplicated by dbt `metadata.invocation_id` so file-watcher double-fires don't create duplicates.
- Each entry tagged with a renderer `sessionId`. If you close the app mid-run, the interrupted `running` entry is recovered on next open as `cancelled` with a completion timestamp and interruption message.
- Project switch forces a clean remount of the bottom panel so Terminal, Query Results, and Run History all reset to the correct project.
- Storage is entirely renderer-local `localStorage`. No main-process IPC. No SQLite schema. Drops out cleanly if it ever needs to.

---

## Slide-by-Slide Presentation Plan (≈130 seconds)

Matches the reference deck structure from `presentations/what-is-dbt/`:

| Slide | Timing | Screen / Image | Heading / Copy |
|-------|--------|----------------|----------------|
| 1 | 0:00–0:12 | Hero / title card | **"Rosetta DBT Studio 1.6.1 is here."** — "The Workflow Release": 12 shipped improvements across the app, headlined by native Query Results & Run History (#327) plus AI Terminal assist, HTML Viewer, Cloud downloads, Pipelines tab, Secrets & Push recovery, and Saved Queries improvements. |
| 2 | 0:12–0:27 | `001a-query-result-tab-preview.png` + `001c-run-history-tab-error-view1.png` | **"Two new tabs, one place."** — `QUERY RESULTS` and `RUN HISTORY` join Terminal and Lineage in the project bottom panel. |
| 3 | 0:25–0:40 | `001a-query-result-tab-01.png` (Preview with rows) | **"Preview: your rows, right there."** — Run a model, get a grid. Row count, elapsed time, pagination, export. Not a modal. |
| 4 | 0:40–0:55 | `001a-query-result-tab-compiled-sql.png` + `001a-query-result-tab-raw-sql.png` | **"SQL: two views of the same query."** — `Compiled SQL` and `Raw SQL` side-by-side. One-click copy. No more hunting for what actually ran. |
| 5 | 0:55–0:70 | `001a-query-result-tab-history.png` + `001a-query-result-tab-bookmarks.png` | **"History & Bookmarks."** — Every query you ran is still there. Re-run with one click. Save the keepers as bookmarks with tags. |
| 6 | 0:70–0:85 | `001b-run-history-tab-results.png` (Run History — parent rows) + `001b-run-history-tab-detailed-view.png` (expanded child rows) | **"Run History: every dbt command, remembered."** — Parent rows with status and summary. Expand into per-model/test child results. |
| 7 | 0:85–0:95 | `001c-run-history-tab-error-view1.png` + `001c-run-history-tab-error-terminal-dbt.png` | **"When things break."** — A failed run shows exactly which model failed. Don't dig through terminal logs. |
| 8 | 0:95–1:10 | `001c-run-history-tab-error-ai-assistant.png` + `001c-run-history-tab-error-ai-assistant-keep-changes.png` | **"Fix with AI."** — Click 'Explain failure' and the Agent diagnoses the problem and writes the fix for you to approve. |
| 9 | 1:10–1:20 | `004-monaco-editor-autocomplete.png` + `002-dbt-screen-with-git-UI.png` | **"The IDE you expect."** — Monaco editor with Jinja/SQL autocomplete, plus full Git integration built right in. |
| 10 | 1:20–1:30 | `005-run-dbt-comands-from-UI.png` + `006-run-model-dbt0comands-from-UI.png` | **"Run anything. Visually."** — Trigger project-wide or model-specific dbt commands without touching the CLI. |
| 11 | 1:30–1:40 | `008-model-lineage-full-screen.png` + `007-model-lineage.png` | **"Lineage that actually works."** — Interactive, auto-updating DAGs built into the bottom panel or fullscreen. |
| 12 | 1:40–1:50 | Logo / CTA card | **"That's Rosetta DBT Studio."** — Open source. macOS · Windows · Linux. |

---

## Voiceover Script (≈145 seconds, teaching tone — same direction as the what-is-dbt script)

### Overview
- **Total duration**: ~145 seconds
- **Tone**: calm, explanatory, not promo. One person explaining to another.
- **Audience**: existing DBT Studio users and dbt-power-user users who know what the missing pieces were.

### Cue Map

| Slide | Timing | VO |
|-------|--------|----|
| 1 | 0:00–0:12 | "Today we're shipping Rosetta DBT Studio 1.6.1 — The Workflow Release. Twelve improvements across the app. Headlined by Query Results and Run History, and alongside it: AI in the Terminal, HTML Viewer in the editor, Cloud downloads inside the app, the new Pipelines Getting Started tab, Secrets and Push-to-Cloud recovery, Saved Queries one-click open, and a sweep of quality fixes across every surface." |
| 2 | 0:12–0:27 | "At the center of this release are two new tabs in the project bottom panel, right next to Terminal and Lineage — `QUERY RESULTS` and `RUN HISTORY`. The rest of this walkthrough is a quick tour of what they do, and where everything now lives." |
| 3 | 0:27–0:42 | "When you preview a model, the rows land in Preview — row count, elapsed time, pagination, export. No modal to dismiss. No scrolling back through a terminal. Just a grid, where you expect it." |
| 4 | 0:42–0:57 | "And because dbt compiles Jinja, the SQL tab gives you both views — `Compiled SQL` that actually hit the warehouse, and the `Raw SQL` you wrote. Copy either with one click." |
| 5 | 0:57–1:12 | "History keeps every query you ran. Re-run with one click. Bookmark the ones you want to keep, with a name and tags. It persists across sessions, scoped per project." |
| 6 | 1:12–1:27 | "Run History does the same for dbt commands. Parent rows for `dbt run`, `dbt test`, `dbt build`, `dbt compile`, the whole set. Expand one, and you see every model, every test — status, execution time, message." |
| 7 | 1:27–1:37 | "When a run fails, you don't have to scroll through the terminal. The failed model is highlighted right there in the history." |
| 8 | 1:37–1:52 | "And you can fix it immediately. Click 'Explain failure', and the AI Agent reads the error, diagnoses the problem, and proposes a fix. You just review and apply." |
| 9 | 1:52–2:02 | "This completes the workflow we started by bringing the best of VS Code into DBT Studio. The Monaco editor with full Jinja and SQL autocomplete, sitting next to a built-in Git interface." |
| 10 | 2:02–2:12 | "Visual dropdowns that let you trigger any dbt command — for the whole project, or just upstream and downstream from one model." |
| 11 | 2:12–2:22 | "And an interactive lineage graph that updates as you type, right there in the bottom panel." |
| 12 | 2:22–2:32 | "The code, the lineage, the rows, and the runs. All of it, in one window. That's Rosetta DBT Studio 1.6.1. Open source for Mac, Windows, and Linux." |

### Delivery notes
- The spine is slide 1's framing of 1.6.1 as *The Workflow Release* — twelve improvements across the app — with the payoff landing on slide 12's "All of it, in one window." Pause before that final line.
- Slide 4 is deliberately dense with a concrete detail ("the Jinja you wrote") because it's a dbt audience — they already know why compiled-vs-raw matters.
- Slides 9, 10, and 11 act as a rapid-fire reminder that the core IDE features (autocomplete, visual commands, lineage) are already here and robust.

---

## Assets Checklist

Files in `presentations/dbt-sql-results-and-run-history.md/`:

| Filename | Used in slide | Purpose |
|----------|---------------|---------|
| `001-dbt-screen.png` | Slide 2 | Full app overview showing bottom panel tabs (TERMINAL · LINEAGE · **QUERY RESULTS** · **RUN HISTORY**) |
| `001a-query-result-tab-01.png` | Slide 3 | QUERY RESULTS → Preview showing rows (Preview 500 rows in 8.40s) |
| `001a-query-result-tab-preview.png` | Slide 2 | QUERY RESULTS tab view |
| `001a-query-result-tab-compiled-sql.png` | Slide 4 | SQL tab → Compiled SQL view |
| `001a-query-result-tab-raw-sql.png` | Slide 4 | SQL tab → Raw SQL view |
| `001a-query-result-tab-history.png` | Slide 5 | History tab showing prior queries with green `<>` icon |
| `001a-query-result-tab-bookmarks.png` | Slide 5 | Bookmarks tab showing a saved entry |
| `001b-run-history-tab-results.png` | Slide 6 | RUN HISTORY parent rows overview |
| `001b-run-history-tab-detailed-view.png` | Slide 6 | RUN HISTORY expanded child rows |
| `001c-run-history-tab-error-view1.png` | Slide 2 & 7 | RUN HISTORY tab view & failed run showing 'Fix with AI' |
| `001c-run-history-tab-error-terminal-dbt.png` | Slide 7 | Terminal showing the compilation error |
| `001c-run-history-tab-error-ai-assistant.png` | Slide 8 | AI Agent explaining the failure |
| `001c-run-history-tab-error-ai-assistant-keep-changes.png` | Slide 8 | AI Agent proposing and applying the fix |
| `004-monaco-editor-autocomplete.png` | Slide 9 | Monaco Editor showing SQL autocomplete |
| `002-dbt-screen-with-git-UI.png` | Slide 9 | Explorer showing the Git UI integration |
| `005-run-dbt-comands-from-UI.png` | Slide 10 | Project-level dbt commands dropdown |
| `006-run-model-dbt0comands-from-UI.png` | Slide 10 | Model-level dbt commands dropdown |
| `008-model-lineage-full-screen.png` | Slide 11 | Fullscreen lineage view |
| `007-model-lineage.png` | Slide 11 | Lineage inside the bottom panel |

Reference pattern reused from `presentations/what-is-dbt/video-presentation.html`:
- 6–7 slide deck with `.slide` / `.active` / `.prev` classes
- Eyebrow + heading + subtitle cards positioned right or left over a screenshot background
- Keyboard (arrows, space, enter, home, end, f) + click-to-advance controls
- Orange accent `--orange` / `--orange-2` color tokens

---

## Acceptance Criteria — What Makes the Presentation True to the Feature

If someone watches the video and then opens 1.6.1, every claim on screen should be demonstrable in two clicks:

1. Open a project → open a model → `Execute Query` CodeLens is visible at top of Monaco.
2. Click it → bottom panel auto-switches to `QUERY RESULTS` → Preview tab has rows, row count, elapsed time.
3. Switch to SQL tab → both Compiled and Raw sub-tabs render → Copy button works.
4. Switch to History → execution is there → hover shows Run + Bookmark → Run works.
5. Save a bookmark → switch to Bookmarks → entry exists → Run + Delete work.
6. Run `dbt test` with at least one test → switch to `RUN HISTORY` → parent row, summary counts, expand into child rows.
7. If a test fails, the child row exposes `Explain failure` → opens Agent with context.
8. If the whole run fails, parent row exposes `Fix with AI` → opens Agent.
9. Close app mid-run → reopen → the interrupted entry appears as `cancelled`.
10. Switch projects → bottom panel cleanly remounts; Terminal, Query Results, Run History all show the new project.

None of these require a video script voiceover to say. The screenshot on the slide just has to show the thing, and the thing has to work.
