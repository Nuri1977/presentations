# S03 · Sources: Google Vids script

**Import:** `s03-sources.pptx` (speaker notes = the scripts below). **Voiceover:** 501 words, about 3.3 min at 150 wpm. **Demo recording budget:** about 6.2 min (Vids videos max 10 min).

**Scene order in Vids:** scenes 1 to 13 (slides) → your demo recording → scene 14 (recap). Drag the recap scene to the end after you add the recording.

**Before converting:** in Google Slides, replace the amber `?` numbers on the real-data slides with your dry-run results. The scripts never read the numbers aloud, so only the slide changes.

## Voiceover, scene by scene

**Scene 1 · Sources**

Section three: sources. This is how we tell dbt about data that already exists in the database, data that dbt did not build.

**Scene 2 · Never hard-code a table name.**

One rule: never hard-code a table name in a model. It works, but dbt cannot see the dependency. It cannot draw it in the lineage, test it, or document it, and if the schema changes, every model breaks.

**Scene 3 · Hard-coded vs source()**

On the left, a hard-coded table. On the right, the source function, with the source name and the table name. Both compile to the same SQL, but only the right one appears in the lineage graph, with tests and descriptions attached.

**Scene 4 · Sources**

The sources page, version one. Declare sources in YAML, with a name, the schema, and the tables. Select from them with the source function. Add tests and descriptions to source columns. And freshness can warn you when a loader stops delivering data.

**Scene 5 · Our first block in the DAG**

On our lineage graph, the first node lights up: the source for yellow taxi trips. Everything else in the project will be built on top of it.

**Scene 6 · Rosetta Raw Layer**

Rosetta can generate the source file for us. The Raw Layer option reads the database and writes a YAML file with every column. No AI involved. It also adds a not null test to every column. That is a guess, and real data will test it.

**Scene 7 · Prompt card**

In the demo, the agent moves that file into our staging folder, names the source T L C, and adds a description to every column from the dictionary file. We tell it not to change the tests yet.

**Scene 8 · The source YAML, after the agent**

This is what we review before keeping it. The source name and schema. Descriptions that match the dictionary. Notice payment type starts at zero, Flex Fare, from the current dictionary. And the tests are still the generated guesses.

**Scene 9 · Test the source**

Then we run the source tests. Several not null tests fail: passenger count, rate code, the store and forward flag, and some surcharges. That is real data pushing back on a guess.

**Scene 10 · Prompt card**

Instead of deleting the tests, we ask why. In Ask mode: which rows fail, and what do they have in common?

**Scene 11 · The empty rows have something in common**

In our data, the rows with an empty passenger count are the rows with payment type zero, which the dictionary calls Flex Fare. So these are not broken rows. They are a different kind of trip, where some fields are not recorded.

*If your dry run does not show this:* In our data, the rows with an empty passenger count are incomplete in several columns at once. The source simply does not record those fields for some trips. So the right question is not how to fix them, but which columns must always have a value.

**Scene 12 · The decision**

So we decide. We keep not null where a trip cannot exist without a value: the times, the locations and the total. We drop it where the source legitimately leaves values empty. A failing test is a decision, not a bug.

**Scene 13 · Why we skip freshness**

One last thing: freshness. It compares a timestamp with the current time. Our data is historical, so it would always look stale, and we skip it. In a real project with daily data, you turn it on. It tells you when a loader stopped working.

**Scene 14 · Section 03 done**

That is section three. Our raw table is now a documented source, and its tests describe reality instead of a guess. First block ticked: sources. Next: seeds.

## Demo recording: prompting and changing files

**Set up before you hit record**

- Section 02 end state. Skill and dbt_project.yml in place.

**Steps**

1. Project menu → **Raw Layer**. Output folder: `models/raw`. Open the generated YAML. *File:* `models/raw/*.yml`
2. New chat, **Code** mode. Paste prompt 1.

   > Move the generated source YAML to models/staging/tlc/_tlc__sources.yml. Name the source tlc and keep the table name yellow_trips. Add a description to every column from reference/tlc_yellow_data_dictionary.md, including the full code lists for VendorID, RatecodeID and payment_type. Use the data_tests: key. Don't change which tests exist yet.

3. When `_tlc__sources.yml` opens: scroll it, check two descriptions against the dictionary and payment type 0 = Flex Fare. **Keep**. *File:* `models/staging/tlc/_tlc__sources.yml`
4. Run `dbt test --select source:tlc` (terminal or ask the agent). Show the failing `not_null` tests in Run History.
5. New chat, **Ask** mode. Paste prompt 2. Read the answer on screen.

   > Which rows fail the not_null test on passenger_count? What do they have in common?

6. Edit `_tlc__sources.yml` by hand: remove `not_null` on passenger_count, RatecodeID, store_and_fwd_flag, congestion_surcharge, airport_fee. *File:* `models/staging/tlc/_tlc__sources.yml`
7. Run `dbt test --select source:tlc` again: green.

**Optional lines to say over the recording**

- "The generator guessed not null everywhere. Let's see what real data says."
- "We keep the tests that describe reality."

**All prompts in this section, ready to paste**

1. Move the generated source YAML to models/staging/tlc/_tlc__sources.yml. Name the source tlc and keep the table name yellow_trips. Add a description to every column from reference/tlc_yellow_data_dictionary.md, including the full code lists for VendorID, RatecodeID and payment_type. Use the data_tests: key. Don't change which tests exist yet.

2. Which rows fail the not_null test on passenger_count? What do they have in common?
