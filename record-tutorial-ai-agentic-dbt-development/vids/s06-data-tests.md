# S06 · Data tests: Google Vids script

**Import:** `s06-data-tests.pptx` (speaker notes = the scripts below). **Voiceover:** 503 words, about 3.4 min at 150 wpm. **Demo recording budget:** about 6.1 min (Vids videos max 10 min).

**Scene order in Vids:** scenes 1 to 13 (slides) → your demo recording → scene 14 (recap). Drag the recap scene to the end after you add the recording.

**Before converting:** in Google Slides, replace the amber `?` numbers on the real-data slides with your dry-run results. The scripts never read the numbers aloud, so only the slide changes.

## Voiceover, scene by scene

**Scene 1 · Data tests**

Section six: data tests. A test is how we write down an assumption, so dbt checks it on every run. With real data, some assumptions will be wrong. That is the point.

**Scene 2 · A test is a query that should return zero rows.**

Every dbt test is a query that looks for bad rows. Zero rows means the test passes. Any rows means it fails, and the failing rows are right there to look at.

**Scene 3 · The four built-in generic tests**

dbt ships four generic tests. Unique and not null, usually together on a primary key. Accepted values, for columns with a known list, like payment types. And relationships, which checks that every value exists in another model, like a foreign key.

**Scene 4 · Generic vs singular**

Two kinds of test. Generic tests are reusable, and you list them under a column in YAML. Singular tests are one SQL file in the tests folder. This one returns trips that end before they start.

**Scene 5 · Data tests**

The data tests page, version one. Generic tests go under the data tests key in YAML. Singular tests are SQL files. You can set severity to error or warn, test only some rows, and store failing rows in a table.

**Scene 6 · By hand: test the zones**

First, by hand: the zone ID is our primary key, so it gets unique and not null. Two lines, and the official lookup passes.

**Scene 7 · Prompt card**

In the demo, the agent adds the rest: not null on the timestamps, accepted values on payment type from the seed, relationships from both location columns to the zones, and the singular test for backwards trips. Then it runs the tests for this model.

**Scene 8 · What it should write**

What we review. Accepted values zero to six, taken from the seed. In recent dbt version one, the values sit under a key called arguments. Quote is false, because the codes are numbers. And the relationships test points at the zones model.

**Scene 9 · The singular test**

The singular test is a plain query for the rows that break our rule: dropoff before pickup. It returns the source file too, so we can see which month the bad rows came from.

**Scene 10 · Real data says no**

And real data says no. The singular test fails: some trips really do end before they start. The accepted values test passes, because we used the current code list. Now we decide what to do.

*If your dry run does not show this:* And real data answers. Look at the singular test result on screen, and the accepted values test, which uses the current code list. Whatever a test reports, the next step is the same: we decide what to do.

**Scene 11 · Ask the AI assistant on the error**

Rosetta has a shortcut for this moment. In Run History, open the failed test, and the error view offers an AI assistant. We let it propose a fix, and we read it before deciding.

**Scene 12 · The decision is yours**

Three options. Deleting the rows in staging hides a real problem, so no. Making the test a warning and storing the failing rows keeps them visible without blocking every build. And in section eight, we flag invalid trips in the intermediate layer. A failing test is a decision.

**Scene 13 · Warn, and keep the evidence**

One line at the top: severity warn, and store failures. The build continues with a warning, and the failing rows are saved in a table we can query.

**Scene 14 · Section 06 done**

That is section six. Tests are queries for bad rows. Real data failed one, the AI assistant made a suggestion, and we made the call. Next: reusing code with packages, Jinja and macros.

## Demo recording: prompting and changing files

**Set up before you hit record**

- Section 05 end state. Both staging models built.

**Steps**

1. Create `stg_tlc__taxi_zones.yml` by hand: `unique` + `not_null` on `location_id`. Run `dbt test --select stg_tlc__taxi_zones`. *File:* `models/staging/tlc/stg_tlc__taxi_zones.yml`
2. New chat, **Code** mode. Paste prompt 1.

   > In stg_tlc__yellow_trips.yml add data tests: not_null on pickup_at and dropoff_at; accepted_values on payment_type_id using the codes in seeds/payment_types.csv; relationships from pickup_location_id and dropoff_location_id to stg_tlc__taxi_zones.location_id. Write a singular test, tests/assert_trip_ends_after_it_starts.sql. Run dbt test for this model only.

3. Review the YAML (values 0-6 under `arguments:`) and `tests/assert_trip_ends_after_it_starts.sql`. **Keep**. **Allow** `dbt test`. *File:* `stg_tlc__yellow_trips.yml, tests/assert_trip_ends_after_it_starts.sql`
4. Run History → the failed singular test → error view → **AI assistant**. Read its suggestion.
5. If it proposes filtering in staging: **Discard**.
6. Add `{{ config(severity = 'warn', store_failures = true) }}` to the singular test by hand. Run `dbt test` again: a warning. *File:* `tests/assert_trip_ends_after_it_starts.sql`
7. SQL editor: query the stored-failures table.

**Optional lines to say over the recording**

- "Real data says no."
- "We don't delete facts in staging. We warn, and keep the evidence."

**All prompts in this section, ready to paste**

1. In stg_tlc__yellow_trips.yml add data tests: not_null on pickup_at and dropoff_at; accepted_values on payment_type_id using the codes in seeds/payment_types.csv; relationships from pickup_location_id and dropoff_location_id to stg_tlc__taxi_zones.location_id. Write a singular test, tests/assert_trip_ends_after_it_starts.sql. Run dbt test for this model only.
