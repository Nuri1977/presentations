# S05 · Staging models: Google Vids script

**Import:** `s05-staging-models.pptx` (speaker notes = the scripts below). **Voiceover:** 554 words, about 3.7 min at 150 wpm. **Demo recording budget:** about 5.8 min (Vids videos max 10 min).

**Scene order in Vids:** scenes 1 to 13 (slides) → your demo recording → scene 14 (recap). Drag the recap scene to the end after you add the recording.

## Voiceover, scene by scene

**Scene 1 · Staging models**

Section five: staging models. They take a source and make it clean and consistent. We write the first one by hand, so you see exactly what a model is, and the agent writes the big one.

**Scene 2 · A model is just a select statement.**

If you remember one thing: a dbt model is just a select statement in a file. You never write create table. The file name becomes the model name, and dbt adds the right create statement for you.

**Scene 3 · SQL models**

The SQL models page, version one. A model is one select in a SQL file. The file name is the name of the view or table. To use another model, you use ref, and dbt works out the order. The default is a view.

**Scene 4 · What you write vs what dbt runs**

On the left, what we write: a select, with ref to the zone seed. On the right, what dbt sends to the database: a create view, with ref replaced by the real table name. The Compiled SQL tab in Rosetta shows this for any model.

**Scene 5 · ref() builds the DAG**

Every ref is an arrow in the lineage graph. The staging model uses the seed, so the seed is built first. Later, a dimension uses the staging model. dbt reads all these references and builds from left to right.

**Scene 6 · How we structure: Staging**

The structure guide on staging. Name files S T G, then the source, two underscores, then the entity. Do renaming, type casting and simple calculations. Do not join or aggregate. Staging models are views.

**Scene 7 · Staging: do and don't**

Our checklist. Rename to snake case, cast types, turn the yes or no flag into a boolean, and keep every row. No joins, no aggregations, and no filtering. The strange trips stay in staging. We flag them later, where the business rule belongs.

**Scene 8 · By hand: the zones model**

Our first model, written by hand. A source step that selects from the seed with ref. A renamed step that gives every column a clean name. And a final select. The agent will follow the same pattern.

**Scene 9 · Run it, preview it, read the compiled SQL**

We run it with the model button, open Preview to see the renamed zones, and open Compiled SQL to see ref replaced by the table. We never wrote view in the file. The folder setting from section two decided it.

**Scene 10 · The big one: how trip columns get renamed**

The trips model is bigger: twenty columns. Timestamps end in at. Distance gets its unit. IDs become snake case. The flag becomes a boolean. Money becomes a decimal. And the file name is kept as source file. Repetitive work, perfect for the agent.

**Scene 11 · Prompt card**

In the demo, the agent creates the staging model for yellow trips, following our skill: snake case, the at suffix, a boolean, decimals, and source file. No filters, no joins. Plus a YAML file with descriptions. Then it builds only this model.

**Scene 12 · What good looks like**

This is the shape we expect, and how we review it. It uses source, not a table name. Every money column is cast. And two things must not be there: a where clause, and a config block. If either appears, we ask the agent to remove it before keeping the file.

**Scene 13 · Staging in the DAG**

Two new nodes in the lineage: our staging models, each fed by exactly one input. One to one, just as the guide says.

**Scene 14 · Section 05 done**

That is section five. Models are select statements, ref and source build the graph, and we have two staging models, one by hand and one by the agent. Next: we write down what we expect from the data, with tests.

## Demo recording: prompting and changing files

**Set up before you hit record**

- Section 04 end state. Seeds loaded.

**Steps**

1. Create `models/staging/tlc/stg_tlc__taxi_zones.sql` and type it by hand (CTEs `source` → `renamed`). *File:* `models/staging/tlc/stg_tlc__taxi_zones.sql`
2. Model button **Run**, then **Preview**, then the **Compiled SQL** tab.
3. New chat, **Code** mode. Paste prompt 1.

   > Following the nyc-taxi-dbt-conventions skill, create stg_tlc__yellow_trips from source('tlc', 'yellow_trips'). Rename every column to snake_case, timestamps end in _at, store_and_fwd_flag becomes a boolean, money columns are decimal(10,2), and keep the source filename as source_file. No filters, no joins. Add stg_tlc__yellow_trips.yml with descriptions taken from the source YAML. Then build only this model.

4. Review `stg_tlc__yellow_trips.sql`: `source()`, casts, no `where`, no `config()`. Then the `.yml`. **Keep** both. *File:* `models/staging/tlc/stg_tlc__yellow_trips.sql, .yml`
5. **Allow** `dbt build --select stg_tlc__yellow_trips`.
6. Preview the model, then open the **lineage** view.

**Optional lines to say over the recording**

- "A model is just a select."
- "No where clause: the strange trips stay, for now."

**All prompts in this section, ready to paste**

1. Following the nyc-taxi-dbt-conventions skill, create stg_tlc__yellow_trips from source('tlc', 'yellow_trips'). Rename every column to snake_case, timestamps end in _at, store_and_fwd_flag becomes a boolean, money columns are decimal(10,2), and keep the source filename as source_file. No filters, no joins. Add stg_tlc__yellow_trips.yml with descriptions taken from the source YAML. Then build only this model.
