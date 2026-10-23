# S09 · Unit tests: Google Vids script

**Import:** `s09-unit-tests.pptx` (speaker notes = the scripts below). **Voiceover:** 367 words, about 2.4 min at 150 wpm. **Demo recording budget:** about 7.1 min (Vids videos max 10 min).

**Scene order in Vids:** scenes 1 to 9 (slides) → your demo recording → scene 10 (recap). Drag the recap scene to the end after you add the recording.

## Voiceover, scene by scene

**Scene 1 · Unit tests**

Welcome to part two: production patterns. We start with unit tests. Our tests so far check the data, but our business logic could have a bug that today's data simply does not show. Unit tests catch that.

**Scene 2 · Data tests vs unit tests**

Two different questions. A data test runs on the real tables and asks: is this data right? A unit test feeds a model a few rows that we invent, and asks: does my SQL do what I meant?

**Scene 3 · Unit tests**

The unit tests page, version one, available since dbt one point eight. A unit test lives in YAML. Given: fake input rows for every model the tested model reads. Expect: the rows that should come out. You only list the columns that matter.

**Scene 4 · Anatomy of a unit test**

One unit test. The model under test is the intermediate trips model. Given one fake trip with zero distance, and empty inputs for the two seeds, because every input must be mocked. We expect fare per mile to be empty, the trip invalid, and the reason zero distance.

**Scene 5 · Our four edge cases**

Deciding what to test is the human part. Four cases from the problems we found. Zero distance. A trip that ends before it starts. A normal trip, two and a half miles for fifteen dollars, which must be valid at six dollars a mile. And a negative total.

**Scene 6 · Prompt card**

In the demo, we describe the four cases in plain English, and the agent writes the YAML, mocks every input, and runs only the unit tests. Verbose YAML is perfect agent work. The cases are ours.

**Scene 7 · Run them**

We run only the unit tests, and four pass. If one fails, ask the honest question: is the test wrong, or the model?

**Scene 8 · A test you've never seen fail is a test you can't trust.**

A test you have never seen fail is a test you cannot trust. So we break the model on purpose.

**Scene 9 · Break it on purpose**

We change one character: less than or equal to zero becomes less than zero. Now zero-distance trips are valid. The first unit test turns red, and dbt shows what we expected and what we got. We undo the change, and it is green again.

**Scene 10 · Section 09 done**

That is section nine. Unit tests lock our business logic. We chose the cases, the agent wrote the YAML, and we watched a test fail on purpose. Next: incremental models.

## Demo recording: prompting and changing files

**Set up before you hit record**

- Section 08 end state.

**Steps**

1. New chat, **Code** mode. Paste prompt 1.

   > Write unit tests for int_trips__enriched in models/intermediate/_int__unit_tests.yml: (1) trip_distance 0 gives a null fare_per_mile and is_valid_trip false; (2) dropoff before pickup is invalid; (3) a normal 2.5-mile trip with a $15 fare gives fare_per_mile 6.00 and is valid; (4) a negative total_amount is invalid. Mock every ref the model uses. Then run dbt test --select test_type:unit.

2. Review `_int__unit_tests.yml`: every `ref` mocked, only needed columns. **Keep**. **Allow** the test run: 4 pass. *File:* `models/intermediate/_int__unit_tests.yml`
3. In `int_trips__enriched.sql`, change `trip_distance_miles <= 0` to `< 0` by hand. *File:* `models/intermediate/int_trips__enriched.sql`
4. Run `dbt test --select test_type:unit`: one red test. Show expected vs actual.
5. Undo the change. Run again: green. *File:* `models/intermediate/int_trips__enriched.sql`

**Optional lines to say over the recording**

- "One character, and the test catches it."

**All prompts in this section, ready to paste**

1. Write unit tests for int_trips__enriched in models/intermediate/_int__unit_tests.yml: (1) trip_distance 0 gives a null fare_per_mile and is_valid_trip false; (2) dropoff before pickup is invalid; (3) a normal 2.5-mile trip with a $15 fare gives fare_per_mile 6.00 and is valid; (4) a negative total_amount is invalid. Mock every ref the model uses. Then run dbt test --select test_type:unit.
