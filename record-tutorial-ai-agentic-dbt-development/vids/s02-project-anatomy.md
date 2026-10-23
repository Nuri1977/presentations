# S02 · Project anatomy & teaching the agent: Google Vids script

**Import:** `s02-project-anatomy.pptx` (speaker notes = the scripts below). **Voiceover:** 508 words, about 3.4 min at 150 wpm. **Demo recording budget:** about 6.1 min (Vids videos max 10 min).

**Scene order in Vids:** scenes 1 to 12 (slides) → your demo recording → scene 13 (recap). Drag the recap scene to the end after you add the recording.

## Voiceover, scene by scene

**Scene 1 · Project anatomy & teaching the agent**

Section two. We look inside a dbt project: its building blocks, the one configuration file every project has, and the folder structure we follow. Then we teach the agent those rules with a skill.

**Scene 2 · What is inside a dbt project**

A dbt project is just a folder. The only required file is dbt project dot yml. Models live in the models folder, with YAML files that describe and test them. Seeds, snapshots, tests, macros and analyses each have their own folder. A connection profile says where to build.

**Scene 3 · About dbt projects**

The page About dbt projects, version one, is the map of this course. Its resources table lists every building block a project can have. Its project configuration table lists the settings we put in dbt project dot yml.

**Scene 4 · The blocks, and where we build them**

Here is every block from that page, with the section that builds it. Models, sources, seeds, tests, macros, analyses, snapshots, docs and exposures. The dashed blocks, like metrics and the semantic layer, are beyond this crash course.

**Scene 5 · Project configuration, the keys we set**

The settings we use. The project name. Our own version number. A required dbt version range, so the project only runs on dbt version one. The connection profile. And the folder paths, which we keep at their defaults. Variables come later, in section ten.

**Scene 6 · Our dbt_project.yml**

We write this file by hand. The interesting part is at the bottom: settings per folder. Staging and intermediate models become views. Marts become tables. The plus sign means this is a setting, not a folder name. From now on, the folder decides how a model is built.

**Scene 7 · Three layers**

dbt Labs recommends three layers. Staging is shaped like the source: one model per table, renamed and typed. Intermediate holds business logic. Marts are shaped like the business, and they are what analysts query.

**Scene 8 · How we structure our dbt projects**

The structure guide puts it simply: move data from source-conformed to business-conformed. And the goal is consistency, so nobody wastes time deciding names and folders. That is exactly what we want the agent to follow.

**Scene 9 · Docs → Skill → Agent**

How does the agent learn these rules? With a skill: a Markdown file of instructions with a short description. What we read in the docs, we write into the skill, and the agent loads it whenever a task matches.

**Scene 10 · Our skill**

This is our skill, shortened. The dbt version. Naming for each layer. Column conventions, like timestamps ending in at, and booleans starting with is. And the key rule: code values come from the dictionary file, never from memory.

**Scene 11 · Skills and MCP servers**

Skills are app-wide, so every project can use them. M C P servers give the agent extra knowledge, like the dbt, DuckDB and Rosetta documentation. You can add your own with one link, for example the dbt documentation site.

**Scene 12 · Prompt card**

In the demo, we test the setup with an Ask mode question: what is the difference between a source and a seed, using the dbt version one docs. The agent should look it up, and tell us which page it used.

**Scene 13 · Section 02 done**

That is section two. We know the building blocks, we configured the project file, we know the three layers, and the agent has a skill with our rules. Next: our first block, sources.

## Demo recording: prompting and changing files

**Set up before you hit record**

- Section 01 end state: `raw.yellow_trips` loaded.

**Steps**

1. Open `dbt_project.yml`. Type the `require-dbt-version` line and the `models:` block (staging/intermediate view, marts table). *File:* `dbt_project.yml`
2. Create folders `models/staging/tlc`, `models/intermediate`, `models/marts`. *File:* `models/`
3. Settings → **Skills Library** → New skill `nyc-taxi-dbt-conventions`. Paste the SKILL.md from the course plan (Appendix B). Save. *File:* `SKILL.md (app skills folder)`
4. Settings → **MCP servers**: show the built-in servers. Optional: add `https://gitmcp.io/dbt-labs/docs.getdbt.com`.
5. New chat, **Ask** mode. Paste prompt 1. Point at the MCP tool call and the page it names.

   > Using the dbt v1 docs, what is the difference between a source and a seed? Three bullets, and name the page you used.


**Optional lines to say over the recording**

- "The folder decides how a model is built."
- "This skill is what the agent follows from now on."

**All prompts in this section, ready to paste**

1. Using the dbt v1 docs, what is the difference between a source and a seed? Three bullets, and name the page you used.
