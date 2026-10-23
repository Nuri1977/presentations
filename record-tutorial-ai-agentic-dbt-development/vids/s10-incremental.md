# S10 · Incremental models & a schema change: Google Vids script

**Import:** `s10-incremental.pptx` (speaker notes = the scripts below). **Voiceover:** 568 words, about 3.8 min at 150 wpm. **Demo recording budget:** about 5.7 min (Vids videos max 10 min).

**Scene order in Vids:** scenes 1 to 14 (slides) → your demo recording → scene 15 (recap). Drag the recap scene to the end after you add the recording.

## Voiceover, scene by scene

**Scene 1 · Incremental models & a schema change**

Section ten. Today the fact table is rebuilt from all trips on every run, and that gets slow. We make it incremental, so only new trips are processed. Then a new month arrives, with a surprise.

**Scene 2 · Full rebuild vs incremental**

A table is thrown away and rebuilt on every run. An incremental model keeps the existing table and processes only new rows, inserting them, or replacing rows with the same key.

**Scene 3 · Incremental models**

The incremental models page, version one. The is incremental function is true only on a normal run against an existing table. The word this refers to the existing table. A unique key lets dbt replace rows. And on schema change decides what happens when columns change.

**Scene 4 · The pattern**

The whole pattern. A config block that says incremental. Then an if block that adds a filter. On the first run, or a full refresh, everything loads. On later runs, only rows newer than what is already in the table.

**Scene 5 · Strategies on DuckDB**

How are new rows written? The DuckDB configs page lists four strategies. Append, delete and insert, merge, and microbatch. We use delete and insert with our trip ID: simple, and safe when the same trip arrives twice.

**Scene 6 · Prompt card**

Before changing anything, we ask in Ask mode how this would behave. A trip from the last days of the previous month could be missed, so we look back a few days, and the unique key replaces anything we see twice.

**Scene 7 · A project variable for the lookback**

How many days back is a setting, not code. So it becomes a project variable, the vars key from section two. We can override it on the command line for a single run.

**Scene 8 · Prompt card**

In the demo, the agent makes the fact table incremental: the trip ID as unique key, delete and insert, and a filter that uses our lookback variable. We leave on schema change at its default, and run it once with a full refresh.

**Scene 9 · fct_trips, now incremental**

We review it. The folder says table, but the config in the file says incremental, and the file wins because it is more specific. The validity filter, the lookback from the variable, and no on schema change yet.

**Scene 10 · A new month arrives**

Now real life happens. January twenty twenty-five is published. We add the file to our load script and run it again. Then dbt build for staging and everything downstream, and Run History shows that only the new rows were processed.

**Scene 11 · January brings a new column**

The surprise. January brings a new column: the C B D congestion fee, for the Manhattan Congestion Relief Zone that started on January fifth. It is in the raw table, but not in staging or the fact table. Nothing changes downstream without our decision.

**Scene 12 · What on_schema_change does**

Back to the docs. The default, ignore, does not add new columns. Append new columns adds them. And none of the options fill in old rows. That needs a full refresh.

**Scene 13 · Prompt card**

In the demo, the agent carries the new column through every layer: the dictionary file, the source, staging, intermediate and the fact table, and sets on schema change so the column is added without a full refresh. Updating the dictionary keeps the agent's context current.

**Scene 14 · The result, and the choice**

The column appears. January rows have values, November and December are empty, exactly as the docs said. Here empty is actually correct, because the fee did not exist before January. Know which option you are choosing.

**Scene 15 · Section 10 done**

That is section ten. The fact table is incremental, with a lookback variable, and a real schema change arrived and was carried through on purpose. Next: snapshots.

## Demo recording: prompting and changing files

**Set up before you hit record**

- Section 09 end state. `data/yellow_tripdata_2025-01.parquet` downloaded. Record in two clips if needed.

**Steps**

1. New chat, **Ask** mode. Paste prompt 1.

   > In four bullets, how would fct_trips behave as an incremental model with unique_key trip_id and the delete+insert strategy? What happens to trips from the last few days of the previous month?

2. Add `vars: {lookback_days: 3}` to `dbt_project.yml` by hand. *File:* `dbt_project.yml`
3. New chat, **Code** mode. Paste prompt 2. Review `fct_trips.sql`, **Keep**, **Allow** the `--full-refresh` run. *File:* `models/marts/fct_trips.sql`

   > Make fct_trips incremental: unique_key trip_id, incremental_strategy delete+insert, and on incremental runs only process trips with pickup_at later than the max pickup_at in {{ this }} minus var('lookback_days') days. Leave on_schema_change at its default. Run it once with --full-refresh.

4. Edit `scripts/load_raw.sql`: add the 2025-01 file. Run it in the SQL editor (approval gate). *File:* `scripts/load_raw.sql`
5. Run `dbt build --select stg_tlc__yellow_trips+`. Show in Run History that only new rows were processed.
6. SQL editor: `describe raw.yellow_trips` and `describe fct_trips`. The new column is only in raw.
7. New chat, **Code** mode. Paste prompt 3. Review all five diffs. **Allow** the build. *File:* `dictionary, _tlc__sources.yml, stg, int, fct_trips`

   > The source now has a new column, cbd_congestion_fee (MTA Congestion Relief Zone fee, from 5 January 2025). Add it to reference/tlc_yellow_data_dictionary.md, the source YAML, stg_tlc__yellow_trips, int_trips__enriched and fct_trips. Set on_schema_change on fct_trips so the column is added without a full refresh. Then build.

8. SQL editor: count non-null `cbd_congestion_fee` by month in `fct_trips`.

**Optional lines to say over the recording**

- "A new month, a new column."
- "Empty for November and December, because the fee did not exist yet."

**All prompts in this section, ready to paste**

1. In four bullets, how would fct_trips behave as an incremental model with unique_key trip_id and the delete+insert strategy? What happens to trips from the last few days of the previous month?

2. Make fct_trips incremental: unique_key trip_id, incremental_strategy delete+insert, and on incremental runs only process trips with pickup_at later than the max pickup_at in {{ this }} minus var('lookback_days') days. Leave on_schema_change at its default. Run it once with --full-refresh.

3. The source now has a new column, cbd_congestion_fee (MTA Congestion Relief Zone fee, from 5 January 2025). Add it to reference/tlc_yellow_data_dictionary.md, the source YAML, stg_tlc__yellow_trips, int_trips__enriched and fct_trips. Set on_schema_change on fct_trips so the column is added without a full refresh. Then build.
