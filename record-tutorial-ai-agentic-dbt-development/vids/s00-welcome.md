# S00 · Welcome & the agentic loop: Google Vids script

**Import:** `s00-welcome.pptx` (speaker notes = the scripts below). **Voiceover:** 555 words, about 3.7 min at 150 wpm. **Demo recording budget:** about 5.8 min (Vids videos max 10 min).

**Scene order in Vids:** scenes 1 to 12 (slides) → your demo recording → scene 13 (recap). Drag the recap scene to the end after you add the recording.

## Voiceover, scene by scene

**Scene 1 · AI Agentic dbt Development**

Welcome to AI agentic dbt development. In this crash course we build one real dbt project, from an empty folder to production patterns, using Rosetta dbt Studio and its built-in AI agent. All you need is basic SQL.

**Scene 2 · You stay the engineer. The agent does the typing.**

Agentic means the AI does more than chat. It reads your project, writes files, and runs dbt commands. That is powerful, which is exactly why you stay the engineer. The agent proposes. You review, you decide, and dbt tells you if it is right.

**Scene 3 · The agentic loop**

Every time we use the agent, we follow one loop. Prompt with good context. Let the agent plan. Let it act. Then review every change. Then run dbt, and verify the actual rows. Review is the step people skip, and the one that matters most.

**Scene 4 · Six habits for working with an agent**

Six habits, used in every section. Give the agent files, not memory. Plan before acting on big tasks. One task per chat. Read every diff before you keep it. Let dbt be the judge. And if you correct the agent twice, write the rule into a skill.

**Scene 5 · The rhythm of every section**

Each section follows the same rhythm. A few slides with the idea. The official dbt documentation, version one. Then a recorded demo in Rosetta dbt Studio, where we build it, first by hand and then with the agent. We finish with a git checkpoint.

**Scene 6 · What you will build**

This is the project you will build. Sources and seeds on the left. Staging models, one intermediate model with our business rules, and marts on the right. A snapshot keeps history at the bottom, and an exposure marks the real analysis we answer at the end.

**Scene 7 · The data: NYC taxi trips**

We use real data: New York City yellow taxi trips, published every month by the Taxi and Limousine Commission. Millions of rows per month, small enough for a laptop, and messy enough that our tests will really fail. That is the point.

**Scene 8 · The screen in Rosetta dbt Studio**

The screen in Rosetta dbt Studio. The project files on the left. The editor in the middle, with run, preview and compiled SQL. The AI chat on the right. Every file the agent writes opens for review, with Keep or Discard. Every command it wants to run waits for Allow or Deny.

**Scene 9 · Two modes in the AI chat**

The chat has two modes. Ask mode is read-only. We use it to explain, profile data, and trace lineage. Code mode is where the agent writes files and runs commands. Ask when you want to understand. Code when you want something built.

**Scene 10 · Introduction to dbt**

The dbt documentation now has two versions. This course follows version one, the version Rosetta dbt Studio runs. The core idea: dbt transforms data that is already in your database. You write select statements, and dbt handles the order, the tests and the documentation.

**Scene 11 · The course map**

Here is the map. Part one covers loading data, project structure, sources, seeds, staging, tests, macros, and the final marts. Part two covers unit tests, incremental models, snapshots, and documentation, ending with a real analysis.

**Scene 12 · Let's start: create the project**

In the demo for this section, we create a new project called N Y C taxi, connect it to a new DuckDB database file, look at the AI, skills and M C P settings, and run dbt debug to check that everything works.

**Scene 13 · Section 00 done**

That is section zero. We know what we are building, the agentic loop, and the six habits, and we have an empty project that passes dbt debug. Next, we load the real data.

## Demo recording: prompting and changing files

**Set up before you hit record**

- Rosetta dbt Studio open on the projects screen, no `nyc_taxi` project yet.
- AI provider configured; the model you will use for the whole course selected.

**Steps**

1. Projects screen → **New Project**. Name: `nyc_taxi`.
2. Connection: **DuckDB**, new database file `nyc_taxi.duckdb`.
3. Open Settings and point at **AI provider**, **Skills Library**, **MCP servers**. Don't change anything.
4. Back in the project: open the AI chat panel; show the **Ask / Code** switch.
5. Project menu → **dbt debug**. Wait for "All checks passed".
6. Show the versions: app (Help/About), dbt-core and dbt-duckdb (Settings → dbt runtimes), AI model in the chat.

**Optional lines to say over the recording**

- "Let's create the project."
- "A DuckDB file means nothing to install."
- "dbt debug is green: we are ready."
