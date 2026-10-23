# S08 · Intermediate, marts & materializations: Google Vids script

**Import:** `s08-intermediate-marts.pptx` (speaker notes = the scripts below). **Voiceover:** 616 words, about 4.1 min at 150 wpm. **Demo recording budget:** about 5.4 min (Vids videos max 10 min).

**Scene order in Vids:** scenes 1 to 15 (slides) → your demo recording → scene 16 (recap). Drag the recap scene to the end after you add the recording.

**Before converting:** in Google Slides, replace the amber `?` numbers on the real-data slides with your dry-run results. The scripts never read the numbers aloud, so only the slide changes.

## Voiceover, scene by scene

**Scene 1 · Intermediate, marts & materializations**

Section eight, the end of part one. We build the layers that turn clean data into answers: an intermediate model with our business rules, and the marts analysts use. The biggest agent task so far, so we plan before we act.

**Scene 2 · From clean data to answers**

Staging is done. The intermediate layer adds a trip ID, removes exact duplicates, and adds trip duration, fare per mile, and the valid trip flag we promised. The marts are a fact table of valid trips, a zone dimension, and a daily summary per pickup zone.

**Scene 3 · How we structure: Intermediate**

The structure guide on intermediate models. Each one has a specific purpose, like isolating complex logic so the marts stay simple. End users never query them. They are views or ephemeral.

**Scene 4 · How we structure: Marts**

The guide on marts. A mart is something the business understands: here, a trip, a zone, and a zone per day. Marts are wide, and they are tables, so queries are fast.

**Scene 5 · Materializations**

Materialization means how dbt builds a model. A view stores only the query. A table stores the result. Incremental adds only new rows, in section ten. Ephemeral builds nothing and is inlined. A materialized view is kept up to date by the database.

**Scene 6 · Materializations**

The materializations page. You can set them in the project file, in YAML, or in the model itself, and the most specific setting wins. We set them per folder, and in section ten, one model will override its folder.

**Scene 7 · Big task? Plan before you act.**

This task touches four models and several files. If the agent starts writing and gets the grain wrong, we review a lot of wrong code. So first, we ask for a plan, and we fix the plan.

**Scene 8 · Prompt card**

In the demo, the first prompt asks for the plan only: which intermediate and mart models, the grain of each one, its inputs and its materialization. And it must wait for our OK, without writing any files.

**Scene 9 · The plan we approve**

This is the plan we approve. One intermediate model, one row per trip. A fact table, one row per valid trip. A zone dimension. And a daily summary, one row per zone per day. Fixing a plan is much cheaper than fixing code.

**Scene 10 · Prompt card**

Then: go ahead. The agent builds the trip ID, removes duplicates, adds duration and fare per mile with our macro, the validity flag with a reason, and the code names. Then the marts, YAML with tests for every model, and one dbt build.

**Scene 11 · Inside int_trips__enriched**

The heart of the project. The surrogate key from dbt utils. Duration in minutes. Fare per mile with our safe divide. One row per trip ID. And a reason for every invalid trip: ends before it starts, zero distance, negative total, or a pickup outside its file month.

**Scene 12 · The full core of the project**

Four new nodes. The intermediate model, fed by staging and two seeds. Then the fact table, the zone dimension, and the daily summary that uses both.

**Scene 13 · Selecting what to build**

A word on selecting models. A name selects one model. A plus before it adds everything upstream. A plus after it adds everything downstream. You can also select by folder, by source, or by test type.

**Scene 14 · Verify**

We run dbt build for everything up to the daily summary: seeds, staging, intermediate, marts, and every test, in the right order. Then we look at the lineage, the timings in Run History, and preview the result.

**Scene 15 · Why trips are invalid**

We ask the data why trips are invalid, by reason, and how many duplicates were removed. Every problem we found in section one now has a rule, a name, and a count. The fact table only contains valid trips.

**Scene 16 · Part 1 done**

That is the end of part one. A complete, tested dbt project, from raw files to a fact table and a daily summary, with our business rules in one reviewed place. In part two we make it production-ready.

## Demo recording: prompting and changing files

**Set up before you hit record**

- Section 07 end state. If the agent run is long, record it in two clips and trim the waiting.

**Steps**

1. New chat, **Code** mode. Paste prompt 1 (plan only).

   > Before writing any files, propose the intermediate and mart models needed to answer: (1) trips and revenue per pickup zone per day, (2) a clean trip-level fact table. For each model give its grain, its inputs, and its materialization. Wait for my OK.

2. Read the plan. Correct it in the chat until it matches the "plan we approve" slide.
3. Same chat: paste prompt 2. Let it work; open each file as it appears.

   > Go ahead. In int_trips__enriched, build trip_id with dbt_utils.generate_surrogate_key, remove exact duplicates, add trip_duration_minutes, fare_per_mile using the safe_divide macro, an is_valid_trip flag and an invalid_reason column, and join the payment type and rate code names. fct_trips keeps only valid trips. agg_zone_daily pivots trip counts by payment type with a Jinja loop over the payment_types seed. Add YAML with descriptions and primary-key tests for every model, then run dbt build --select +agg_zone_daily.

4. Review `int_trips__enriched.sql`: surrogate key, `qualify`, `safe_divide`, `invalid_reason`. **Keep** each file after reading it. *File:* `models/intermediate/*, models/marts/*`
5. **Allow** `dbt build --select +agg_zone_daily`.
6. Open the full **lineage** view. Then **Run History** timings. Then preview `agg_zone_daily`.
7. New chat, **Ask** mode: "Count invalid trips in int_trips__enriched by invalid_reason, plus the number of duplicates removed."

**Optional lines to say over the recording**

- "First the plan, then the code."
- "Every problem from section one now has a rule and a count."

**All prompts in this section, ready to paste**

1. Before writing any files, propose the intermediate and mart models needed to answer: (1) trips and revenue per pickup zone per day, (2) a clean trip-level fact table. For each model give its grain, its inputs, and its materialization. Wait for my OK.

2. Go ahead. In int_trips__enriched, build trip_id with dbt_utils.generate_surrogate_key, remove exact duplicates, add trip_duration_minutes, fare_per_mile using the safe_divide macro, an is_valid_trip flag and an invalid_reason column, and join the payment type and rate code names. fct_trips keeps only valid trips. agg_zone_daily pivots trip counts by payment type with a Jinja loop over the payment_types seed. Add YAML with descriptions and primary-key tests for every model, then run dbt build --select +agg_zone_daily.
