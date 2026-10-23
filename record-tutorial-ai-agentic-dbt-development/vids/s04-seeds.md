# S04 · Seeds: Google Vids script

**Import:** `s04-seeds.pptx` (speaker notes = the scripts below). **Voiceover:** 376 words, about 2.5 min at 150 wpm. **Demo recording budget:** about 7.0 min (Vids videos max 10 min).

**Scene order in Vids:** scenes 1 to 10 (slides) → your demo recording → scene 11 (recap). Drag the recap scene to the end after you add the recording.

## Voiceover, scene by scene

**Scene 1 · Seeds**

Section four: seeds. Some data is not in any source system. It is a small list we maintain ourselves, like codes and their names. That is what seeds are for.

**Scene 2 · Seeds**

The seeds page, version one. A seed is a CSV file in the project. dbt seed loads it as a table. Because it is a file in the project, it is version controlled and reviewed. Seeds are best for static data that changes rarely.

**Scene 3 · Good seeds, bad seeds**

Good seeds are small, static lists: code mappings, regions, test accounts to exclude. Bad seeds are raw data exported to CSV, anything large or sensitive, and anything that changes every day.

**Scene 4 · Our three seeds**

We need three seeds. The official zone lookup from the Taxi Commission, with two hundred sixty-five zones. And two lists we create from the dictionary: payment types and rate codes. They turn numbers in the trip data into readable names.

**Scene 5 · Seeds in the DAG**

On the graph, three new nodes on the left, next to the source. Like sources, seeds are where data enters the project.

**Scene 6 · By hand: the official lookup**

The zone lookup is an official file, so nobody should retype it. In the demo, we download it from the Taxi Commission page and drop it into the seeds folder. Notice the column names are not snake case yet. We fix that in staging.

**Scene 7 · Prompt card**

The other two seeds, the agent creates from the dictionary file: every payment type, every rate code, a YAML file with descriptions, and integer types for the IDs. Then it asks to run dbt seed, and waits for our approval.

**Scene 8 · Check the codes**

The review. Payment types must start at zero, Flex Fare, and include six, voided trip. Rate codes must include ninety-nine, unknown. Older versions of the dictionary did not have these, so a list from memory would be wrong. We gave the agent the file, so it got the current list.

**Scene 9 · Types and descriptions**

Seeds get YAML just like models. Descriptions, and column types, so the IDs are integers instead of guessed types. Even a small lookup gets a primary key test.

**Scene 10 · Verify**

We load the seeds with dbt seed and look at the table in the SQL editor. Seven payment types, built from a file in git.

**Scene 11 · Section 04 done**

That is section four. Three seeds: one official file, two created from the dictionary, checked and loaded. Next, our first models: staging.

## Demo recording: prompting and changing files

**Set up before you hit record**

- Section 03 end state. `taxi_zone_lookup.csv` downloaded from the TLC site.

**Steps**

1. Drop `taxi_zone_lookup.csv` into `seeds/` and open it (265 rows). *File:* `seeds/taxi_zone_lookup.csv`
2. New chat, **Code** mode. Paste prompt 1.

   > Create two seeds from reference/tlc_yellow_data_dictionary.md: seeds/payment_types.csv (payment_type_id, payment_type_name) and seeds/rate_codes.csv (rate_code_id, rate_code_name). Include every code in the dictionary. Add seeds/_seeds.yml with descriptions, and column_types so the ids are integers. Then run dbt seed.

3. Review `payment_types.csv` (row 0 = Flex Fare, row 6 = Voided trip) and `rate_codes.csv` (row 99). **Keep** all three files. *File:* `seeds/payment_types.csv, seeds/rate_codes.csv, seeds/_seeds.yml`
4. **Allow** `dbt seed` when asked.
5. SQL editor: `select * from payment_types`. Show the 7 rows.

**Optional lines to say over the recording**

- "Zero, Flex Fare, is there. That came from the file, not from memory."

**All prompts in this section, ready to paste**

1. Create two seeds from reference/tlc_yellow_data_dictionary.md: seeds/payment_types.csv (payment_type_id, payment_type_name) and seeds/rate_codes.csv (rate_code_id, rate_code_name). Include every code in the dictionary. Add seeds/_seeds.yml with descriptions, and column_types so the ids are integers. Then run dbt seed.
