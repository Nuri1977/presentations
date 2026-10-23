"""Screen-recording cue sheets: the demo recorded at the end of each section.

Each step is (action, prompt_index or None, file or None). prompt_index refers to the
section's prompt slides, in slide order (1-based); the full prompt text is pulled from the deck.
`say` holds optional lines to speak live (or to add as a Vids voiceover on the recording scene).
"""

REC = {}

REC[0] = dict(
    setup=['Rosetta dbt Studio open on the projects screen, no `nyc_taxi` project yet.', 'AI provider configured; the model you will use for the whole course selected.'],
    steps=[
        ('Projects screen → **New Project**. Name: `nyc_taxi`.', None, None),
        ('Connection: **DuckDB**, new database file `nyc_taxi.duckdb`.', None, None),
        ('Open Settings and point at **AI provider**, **Skills Library**, **MCP servers**. Don\'t change anything.', None, None),
        ('Back in the project: open the AI chat panel; show the **Ask / Code** switch.', None, None),
        ('Project menu → **dbt debug**. Wait for "All checks passed".', None, None),
        ('Show the versions: app (Help/About), dbt-core and dbt-duckdb (Settings → dbt runtimes), AI model in the chat.', None, None),
    ],
    say=['Let\'s create the project.', 'A DuckDB file means nothing to install.', 'dbt debug is green: we are ready.'],
)

REC[1] = dict(
    setup=['Project `nyc_taxi` open. `data/` holds `yellow_tripdata_2024-11.parquet` and `yellow_tripdata_2024-12.parquet`.',
           '`reference/tlc_yellow_data_dictionary.md` written (transcribed from the TLC PDF, every code list included).'],
    steps=[
        ('Open `reference/tlc_yellow_data_dictionary.md`; scroll slowly through the code lists.', None, 'reference/tlc_yellow_data_dictionary.md'),
        ('SQL Editor → AI panel → **Code** mode. Paste prompt 1.', 1, None),
        ('At the **approval gate**: pause on the SQL, then **Allow**.', None, None),
        ('Save the SQL as `scripts/load_raw.sql` (use absolute paths).', None, 'scripts/load_raw.sql'),
        ('Switch the AI panel to **Ask** mode. Paste prompt 2. Let it run all queries.', 2, None),
        ('Scroll the result tables slowly: rows per file, date range, nulls, negative fares, zero distance, backwards trips.', None, None),
    ],
    say=['The agent shows the SQL first, and waits for my approval.', 'Now we look at the data before we write any rules.', 'These are the numbers on the "What we found" slide.'],
)

REC[2] = dict(
    setup=['Section 01 end state: `raw.yellow_trips` loaded.'],
    steps=[
        ('Open `dbt_project.yml`. Type the `require-dbt-version` line and the `models:` block (staging/intermediate view, marts table).', None, 'dbt_project.yml'),
        ('Create folders `models/staging/tlc`, `models/intermediate`, `models/marts`.', None, 'models/'),
        ('Settings → **Skills Library** → New skill `nyc-taxi-dbt-conventions`. Paste the SKILL.md from the course plan (Appendix B). Save.', None, 'SKILL.md (app skills folder)'),
        ('Settings → **MCP servers**: show the built-in servers. Optional: add `https://gitmcp.io/dbt-labs/docs.getdbt.com`.', None, None),
        ('New chat, **Ask** mode. Paste prompt 1. Point at the MCP tool call and the page it names.', 1, None),
    ],
    say=['The folder decides how a model is built.', 'This skill is what the agent follows from now on.'],
)

REC[3] = dict(
    setup=['Section 02 end state. Skill and dbt_project.yml in place.'],
    steps=[
        ('Project menu → **Raw Layer**. Output folder: `models/raw`. Open the generated YAML.', None, 'models/raw/*.yml'),
        ('New chat, **Code** mode. Paste prompt 1.', 1, None),
        ('When `_tlc__sources.yml` opens: scroll it, check two descriptions against the dictionary and payment type 0 = Flex Fare. **Keep**.', None, 'models/staging/tlc/_tlc__sources.yml'),
        ('Run `dbt test --select source:tlc` (terminal or ask the agent). Show the failing `not_null` tests in Run History.', None, None),
        ('New chat, **Ask** mode. Paste prompt 2. Read the answer on screen.', 2, None),
        ('Edit `_tlc__sources.yml` by hand: remove `not_null` on passenger_count, RatecodeID, store_and_fwd_flag, congestion_surcharge, airport_fee.', None, 'models/staging/tlc/_tlc__sources.yml'),
        ('Run `dbt test --select source:tlc` again: green.', None, None),
    ],
    say=['The generator guessed not null everywhere. Let\'s see what real data says.', 'We keep the tests that describe reality.'],
)

REC[4] = dict(
    setup=['Section 03 end state. `taxi_zone_lookup.csv` downloaded from the TLC site.'],
    steps=[
        ('Drop `taxi_zone_lookup.csv` into `seeds/` and open it (265 rows).', None, 'seeds/taxi_zone_lookup.csv'),
        ('New chat, **Code** mode. Paste prompt 1.', 1, None),
        ('Review `payment_types.csv` (row 0 = Flex Fare, row 6 = Voided trip) and `rate_codes.csv` (row 99). **Keep** all three files.', None, 'seeds/payment_types.csv, seeds/rate_codes.csv, seeds/_seeds.yml'),
        ('**Allow** `dbt seed` when asked.', None, None),
        ('SQL editor: `select * from payment_types`. Show the 7 rows.', None, None),
    ],
    say=['Zero, Flex Fare, is there. That came from the file, not from memory.'],
)

REC[5] = dict(
    setup=['Section 04 end state. Seeds loaded.'],
    steps=[
        ('Create `models/staging/tlc/stg_tlc__taxi_zones.sql` and type it by hand (CTEs `source` → `renamed`).', None, 'models/staging/tlc/stg_tlc__taxi_zones.sql'),
        ('Model button **Run**, then **Preview**, then the **Compiled SQL** tab.', None, None),
        ('New chat, **Code** mode. Paste prompt 1.', 1, None),
        ('Review `stg_tlc__yellow_trips.sql`: `source()`, casts, no `where`, no `config()`. Then the `.yml`. **Keep** both.', None, 'models/staging/tlc/stg_tlc__yellow_trips.sql, .yml'),
        ('**Allow** `dbt build --select stg_tlc__yellow_trips`.', None, None),
        ('Preview the model, then open the **lineage** view.', None, None),
    ],
    say=['A model is just a select.', 'No where clause: the strange trips stay, for now.'],
)

REC[6] = dict(
    setup=['Section 05 end state. Both staging models built.'],
    steps=[
        ('Create `stg_tlc__taxi_zones.yml` by hand: `unique` + `not_null` on `location_id`. Run `dbt test --select stg_tlc__taxi_zones`.', None, 'models/staging/tlc/stg_tlc__taxi_zones.yml'),
        ('New chat, **Code** mode. Paste prompt 1.', 1, None),
        ('Review the YAML (values 0-6 under `arguments:`) and `tests/assert_trip_ends_after_it_starts.sql`. **Keep**. **Allow** `dbt test`.', None, 'stg_tlc__yellow_trips.yml, tests/assert_trip_ends_after_it_starts.sql'),
        ('Run History → the failed singular test → error view → **AI assistant**. Read its suggestion.', None, None),
        ('If it proposes filtering in staging: **Discard**.', None, None),
        ('Add `{{ config(severity = \'warn\', store_failures = true) }}` to the singular test by hand. Run `dbt test` again: a warning.', None, 'tests/assert_trip_ends_after_it_starts.sql'),
        ('SQL editor: query the stored-failures table.', None, None),
    ],
    say=['Real data says no.', 'We don\'t delete facts in staging. We warn, and keep the evidence.'],
)

REC[7] = dict(
    setup=['Section 06 end state.'],
    steps=[
        ('New chat, **Code** mode. Paste prompt 1. **Allow** `dbt deps`.', 1, 'packages.yml'),
        ('Open hub.getdbt.com/dbt-labs/dbt_utils and compare the latest version.', None, None),
        ('New chat, **Ask** mode. Paste prompt 2.', 2, None),
        ('Create `macros/safe_divide.sql` by hand.', None, 'macros/safe_divide.sql'),
        ('Create `analyses/payment_mix.sql` by hand with the `{% for p in [1, 2] %}` loop. Run `dbt compile --select payment_mix`, open the compiled file.', None, 'analyses/payment_mix.sql'),
        ('New chat, **Code** mode. Paste prompt 3. Compile again and compare.', 3, 'analyses/payment_mix.sql'),
    ],
    say=['The database never sees Jinja, only the compiled SQL.'],
)

REC[8] = dict(
    setup=['Section 07 end state. If the agent run is long, record it in two clips and trim the waiting.'],
    steps=[
        ('New chat, **Code** mode. Paste prompt 1 (plan only).', 1, None),
        ('Read the plan. Correct it in the chat until it matches the "plan we approve" slide.', None, None),
        ('Same chat: paste prompt 2. Let it work; open each file as it appears.', 2, None),
        ('Review `int_trips__enriched.sql`: surrogate key, `qualify`, `safe_divide`, `invalid_reason`. **Keep** each file after reading it.', None, 'models/intermediate/*, models/marts/*'),
        ('**Allow** `dbt build --select +agg_zone_daily`.', None, None),
        ('Open the full **lineage** view. Then **Run History** timings. Then preview `agg_zone_daily`.', None, None),
        ('New chat, **Ask** mode: "Count invalid trips in int_trips__enriched by invalid_reason, plus the number of duplicates removed."', None, None),
    ],
    say=['First the plan, then the code.', 'Every problem from section one now has a rule and a count.'],
)

REC[9] = dict(
    setup=['Section 08 end state.'],
    steps=[
        ('New chat, **Code** mode. Paste prompt 1.', 1, None),
        ('Review `_int__unit_tests.yml`: every `ref` mocked, only needed columns. **Keep**. **Allow** the test run: 4 pass.', None, 'models/intermediate/_int__unit_tests.yml'),
        ('In `int_trips__enriched.sql`, change `trip_distance_miles <= 0` to `< 0` by hand.', None, 'models/intermediate/int_trips__enriched.sql'),
        ('Run `dbt test --select test_type:unit`: one red test. Show expected vs actual.', None, None),
        ('Undo the change. Run again: green.', None, 'models/intermediate/int_trips__enriched.sql'),
    ],
    say=['One character, and the test catches it.'],
)

REC[10] = dict(
    setup=['Section 09 end state. `data/yellow_tripdata_2025-01.parquet` downloaded. Record in two clips if needed.'],
    steps=[
        ('New chat, **Ask** mode. Paste prompt 1.', 1, None),
        ('Add `vars: {lookback_days: 3}` to `dbt_project.yml` by hand.', None, 'dbt_project.yml'),
        ('New chat, **Code** mode. Paste prompt 2. Review `fct_trips.sql`, **Keep**, **Allow** the `--full-refresh` run.', 2, 'models/marts/fct_trips.sql'),
        ('Edit `scripts/load_raw.sql`: add the 2025-01 file. Run it in the SQL editor (approval gate).', None, 'scripts/load_raw.sql'),
        ('Run `dbt build --select stg_tlc__yellow_trips+`. Show in Run History that only new rows were processed.', None, None),
        ('SQL editor: `describe raw.yellow_trips` and `describe fct_trips`. The new column is only in raw.', None, None),
        ('New chat, **Code** mode. Paste prompt 3. Review all five diffs. **Allow** the build.', 3, 'dictionary, _tlc__sources.yml, stg, int, fct_trips'),
        ('SQL editor: count non-null `cbd_congestion_fee` by month in `fct_trips`.', None, None),
    ],
    say=['A new month, a new column.', 'Empty for November and December, because the fee did not exist yet.'],
)

REC[11] = dict(
    setup=['Section 10 end state.'],
    steps=[
        ('SQL Editor → AI panel → **Code** mode. Paste prompt 1. **Allow** at the approval gate.', 1, None),
        ('New chat, **Code** mode. Paste prompt 2. Check it wrote YAML (not a `{% snapshot %}` block). **Keep**. **Allow** `dbt snapshot`.', 2, 'snapshots/snap_tlc__vendors.yml, _tlc__sources.yml'),
        ('SQL editor: query the snapshot (2 current rows).', None, None),
        ('SQL editor (approval gate): update vendor 2 to "Curb Mobility, LLC"; insert 6 "Myle Technologies Inc" and 7 "Helix".', None, None),
        ('Run `dbt snapshot` again (agent or terminal).', None, None),
        ('Query the snapshot ordered by vendor_id, dbt_valid_from: vendor 2 has two rows.', None, None),
        ('Code mode: "Create dim_vendors from snap_tlc__vendors, current rows only, with YAML and a primary-key test." **Keep**, build.', None, 'models/marts/dim_vendors.sql'),
    ],
    say=['VeriFone, then Curb Mobility: history kept.'],
)

REC[12] = dict(
    setup=['Section 11 end state. Analytics page or Dive available in your release.'],
    steps=[
        ('New chat, **Code** mode. Paste prompt 1. Review a few diffs, **Keep** all.', 1, 'models/docs.md, *.yml'),
        ('Project menu → **dbt docs generate**, then **dbt docs serve**. Open `fct_trips` and its lineage.', None, None),
        ('New chat, **Ask** mode. Paste prompt 2.', 2, None),
        ('Same chat: paste prompt 3.', 3, None),
        ('Analytics page or Dive: paste prompt 4. Show the chart.', 4, None),
        ('Code mode: "Declare this analysis as an exposure in models/marts/_exposures.yml that depends on fct_trips and dim_zones." **Keep**.', None, 'models/marts/_exposures.yml'),
        ('Regenerate docs; show the exposure in the docs lineage and in Rosetta\'s lineage view.', None, None),
    ],
    say=['The project explains itself.', 'And here is the answer.'],
)

REC[13] = dict(
    setup=['Final project open.'],
    steps=[
        ('Optional, 60 seconds: open the full lineage view and slowly pan across the finished project.', None, None),
        ('Optional: show the companion repository and its checkpoint tags.', None, None),
    ],
    say=['From two Parquet files to this.'],
)
