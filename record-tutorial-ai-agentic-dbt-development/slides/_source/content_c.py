from lib import (title, statement, bullets, flow, columns, code, docs, prompt, table, realdata, dag, blocks, recap,
                 habits, steps)

P2 = 'Part 2 · Production patterns'

# =====================================================================================================================
S09 = dict(num=9, file='s09-unit-tests', title='Unit tests', short='Unit tests', part=P2, minutes=10,
           blurb='Lock the business logic with fixed inputs and expected outputs, written by the agent from plain English.', slides=[
    title('Unit tests', 'Data tests check the data. Unit tests check the logic, with inputs we choose.',
          chips=['unit_tests:', 'given / expect', 'dict format', 'test_type:unit', 'dbt 1.8+'],
          kicker='Part 2 · Section 09',
          say=['Welcome to part two: production patterns. We start with **unit tests**.',
               'In part one, our tests checked the **data**. But our business logic, the valid-trip rules and fare per mile, could have a bug that the current data happens not to show. Unit tests catch that.']),

    columns('Data tests vs unit tests', [
        dict(title='Data tests', color='accent', sub='Is the data OK?', items=['Run against the real tables', 'Find bad rows in the data', 'Every run, in every environment']),
        dict(title='Unit tests', color='violet', sub='Is the logic OK?', items=['Run against small inputs **you** write', 'Compare output to an expected result', 'In development and CI']),
    ], kicker='Two questions', verdict='A data test asks *"is this data right?"*. A unit test asks *"does my SQL do what I meant?"*',
        say=['Two different questions. A data test runs on the real tables and asks: is this data right?',
             'A unit test feeds a model a few rows that **we** invent, and compares the output to what we expect. It asks: does my SQL do what I meant? Even for cases that are not in today\'s data.']),

    docs('Unit tests', 'docs/build/unit-tests', [
        'Available from **dbt 1.8**. Defined in YAML under `models/`, with `unit_tests:`.',
        '`given`: mock rows for every `ref` or `source` the model uses. `expect`: the rows you expect back.',
        'Formats: `dict`, `csv` or `sql`. You only list the columns that matter.',
        'Only SQL models; upstream models must exist (`dbt run --empty` builds them cheaply).',
    ], say=['The unit tests page, version one, available since dbt 1.8. A unit test lives in YAML under `models`.',
            'It has `given`: fake input rows, for every model or source the model reads. And `expect`: the rows that should come out. You only list the columns that matter.',
            'Two rules to remember: every input must be mocked, and the upstream models must exist in the database. We already built them.'],
        do=['Open docs.getdbt.com/docs/build/unit-tests?version=1.']),

    code('Anatomy of a unit test', 'models/intermediate/_int__unit_tests.yml', """unit_tests:
  - name: zero_distance_is_invalid
    model: int_trips__enriched
    given:
      - input: ref('stg_tlc__yellow_trips')
        rows:
          - {vendor_id: 1, trip_distance_miles: 0, fare_amount: 12.50,
             total_amount: 15.00, pickup_at: '2024-11-03 10:00:00',
             dropoff_at: '2024-11-03 10:12:00', source_file: '...2024-11.parquet'}
      - input: ref('payment_types')
        rows: []
      - input: ref('rate_codes')
        rows: []
    expect:
      rows:
        - {fare_per_mile: null, is_valid_trip: false,
           invalid_reason: 'zero_distance'}""", 'yaml', kicker='unit_tests:',
         aside=['`model`: what we test', '`given`: **every** ref is mocked', '`expect`: only the columns we check'],
         say=['Here is one unit test. The model under test is `int_trips__enriched`. In `given`, one fake trip with zero distance, and empty inputs for the two seeds, because every ref must be mocked.',
              'In `expect`, the three columns we care about: fare per mile is null, the trip is invalid, and the reason is zero distance.']),

    table('Our four edge cases', ['#', 'Input', 'Expected'], [
        ['1', '`trip_distance_miles = 0`', '`fare_per_mile` null, invalid, `zero_distance`'],
        ['2', 'dropoff **before** pickup', 'invalid, `ends_before_start`'],
        ['3', '2.5 miles, $15 fare, normal times', '`fare_per_mile = 6.00`, **valid**'],
        ['4', '`total_amount < 0`', 'invalid, `negative_total`'],
    ], kicker='We decide the cases', size=30,
        say=['The human part: deciding **what** to test. Four cases, straight from the problems we found in section one.',
             'Zero distance. Backwards trip. A normal trip, two and a half miles for fifteen dollars, which must be valid with six dollars a mile. And a negative total.',
             'Notice case three: always include a **happy path**, or a model that marks everything invalid would pass.']),

    prompt('Write unit tests for int_trips__enriched in models/intermediate/_int__unit_tests.yml: (1) trip_distance 0 gives a null fare_per_mile and is_valid_trip false; (2) dropoff before pickup is invalid; (3) a normal 2.5-mile trip with a $15 fare gives fare_per_mile 6.00 and is valid; (4) a negative total_amount is invalid. Mock every ref the model uses. Then run dbt test --select test_type:unit.',
           watch=['Every `ref` mocked, including the seeds', 'Only the needed columns in each row', 'Terminal confirm for the unit tests'], habits=[4, 5],
           say=['Plain English in, YAML out. I describe the four cases and ask it to mock every ref, then run only the unit tests.',
                'This is a great job for an agent: unit-test YAML is verbose and fiddly, but the cases are ours.'],
           do=['New chat, Code mode, paste the prompt. Review the YAML. Allow the test run.']),

    steps('Run them', [
        ('Only the unit tests', 'dbt test --select test_type:unit'),
        ('Four passing tests, each with a clear name', None),
        ('If one fails: is the **test** wrong, or the **model**?', None),
    ], kicker='Verify',
        say=['`dbt test --select test_type:unit`. Four green tests.',
             'If one fails, ask yourself the honest question: is the test wrong, or is the model wrong? Sometimes the agent writes an expectation that does not match our rule. That is a review moment too.']),

    statement('A test you\'ve never seen fail<br>is a test you can\'t <em>trust</em>.', kicker='Prove it',
              sub='Break the model on purpose, watch the test turn red, then undo.',
              say=['Now let\'s prove these tests actually protect us. A test you have never seen fail might not be testing anything.']),

    steps('Break it on purpose', [
        ('In `int_trips__enriched`: change `trip_distance_miles <= 0` to `< 0`', None),
        ('Run the unit tests again: test 1 turns **red**', 'dbt test --select test_type:unit'),
        ('Read the diff dbt prints: expected vs actual', None),
        ('Undo the change: green again', None),
    ], kicker='Hands on',
        say=['By hand, I change one character: "less than or equal to zero" becomes "less than zero". So zero-distance trips are now valid. A realistic, one-character bug.',
             'Run the unit tests. Test one is red, and dbt shows the difference: we expected invalid, we got valid.',
             'Undo, run again, green. Now I trust these tests.'],
        do=['Edit the condition by hand, run, show the failure output, revert, run again.']),

    recap('Section 09 done', [
        'Unit tests check **logic** with inputs we choose',
        'Four edge cases from real problems, plus a happy path',
        'The agent wrote the YAML; we chose the cases',
        'We saw a test fail on purpose, so we trust it',
    ], 's09-end', blocks=['sources', 'seeds', 'models', 'data tests', 'macros', 'analysis'], next='S10 · Incremental models & a schema change',
        say=['Recap. Unit tests lock our business logic. We chose four cases, the agent wrote the YAML, and we broke the model on purpose to prove the tests work.',
             'Tag `s09-end`. Next: our fact table is rebuilt from scratch every run. Let\'s fix that with **incremental** models.']),
])

# =====================================================================================================================
S10 = dict(num=10, file='s10-incremental', title='Incremental models & a schema change', short='Incremental models', part=P2, minutes=15,
           blurb='Process only new data, a project variable for the lookback, and a real new column arriving in January 2025.', slides=[
    title('Incremental models & a schema change', 'Process only the new data, and handle a source that changes shape.',
          chips=['is_incremental()', '{{ this }}', 'unique_key', 'delete+insert', 'vars', 'on_schema_change'],
          say=['Section ten. Today `fct_trips` is rebuilt from all the trips on every run. With months of data, that gets slow and expensive.',
               'We make it **incremental**: only new trips are processed. And then a new month arrives, with a surprise.']),

    columns('Full rebuild vs incremental', [
        dict(title='table', color='dim', sub='every run', items=['Drop the table', 'Re-process **all** months', 'Simple, but slow as data grows']),
        dict(title='incremental', color='accent', sub='every run after the first', items=['Keep the table', 'Process only **new** rows', 'Insert, or replace by key']),
    ], kicker='The idea',
        say=['A table materialization throws everything away and rebuilds it. Simple, and fine for small data.',
             'An incremental model keeps the existing table, and on each run processes only the new rows, then inserts them, or replaces rows with the same key.']),

    docs('Incremental models', 'docs/build/incremental-models', [
        '`is_incremental()` is true only when the table **exists**, the model is **incremental**, and it is **not** a `--full-refresh`.',
        '`{{ this }}` is the existing table: use it to find what is already loaded.',
        '`unique_key` lets dbt **replace** rows instead of only appending.',
        '`on_schema_change`: `ignore` (default), `fail`, `append_new_columns`, `sync_all_columns`.',
    ], say=['The incremental models page. Three tools. `is_incremental()` is a Jinja function that is true only on a normal run against an existing incremental table.',
            '`this` refers to the existing table, so we can ask it: what is the latest trip you already have? And `unique_key` lets dbt replace rows that come in again.',
            'And at the bottom, `on_schema_change`: what to do when the columns change. Remember that one.'],
        do=['Open docs.getdbt.com/docs/build/incremental-models?version=1.']),

    code('The pattern', 'any incremental model', """{{ config(materialized = 'incremental', unique_key = 'id') }}

select *
from {{ ref('upstream_model') }}

{% if is_incremental() %}
  -- only on incremental runs:
  where event_time >= (select max(event_time) from {{ this }})
{% endif %}""", 'sql', kicker='is_incremental()',
         aside=['First run: no `where`, everything is loaded', 'Later runs: only rows newer than the table', 'The SQL must work both ways'],
         say=['The whole pattern in a few lines. A config block that says incremental, with a unique key.',
              'Then an `if is_incremental()` block that adds a `where` clause. On the very first run, or a full refresh, the block is skipped and everything loads. On later runs, only rows newer than what is in the table.']),

    table('Strategies on DuckDB', ['Strategy', 'What it does', 'Needs'], [
        ['`append`', 'Insert new rows only', '-'],
        ['`delete+insert`', 'Delete rows with matching keys, then insert', '`unique_key`'],
        ['`merge`', 'Update matching rows, insert the rest', '`unique_key`, DuckDB 1.4+'],
        ['`microbatch`', 'Process time batches independently', '`event_time`, `begin`, `batch_size`, dbt 1.9+'],
    ], kicker='dbt-duckdb configs', size=28, hl_rows=[1],
        foot='Source: **Resource configs → DuckDB configs** (v1). We use `delete+insert`.',
        say=['How exactly are new rows written? That depends on the adapter. The DuckDB configs page lists four strategies.',
             '`append` just inserts. `delete+insert` deletes rows whose key comes in again, then inserts. `merge` needs a recent DuckDB. `microbatch` needs dbt 1.9.',
             'We use **delete+insert** with our trip ID. Simple, and safe when the same trip arrives twice.'],
        do=['Optional: open reference/resource-configs/duckdb-configs?version=1.']),

    prompt('In four bullets, how would fct_trips behave as an incremental model with unique_key trip_id and the delete+insert strategy? What happens to trips from the last few days of the previous month?',
           mode='ask', watch=['First run vs later runs', 'Why a **lookback** window helps', 'Duplicates replaced by key'], habits=[2],
           say=['Before changing anything, Ask mode: how would this behave, and what about trips at the end of the previous month?',
                'The key point it should mention: if we only take trips newer than the maximum, a late-arriving trip from a few days earlier would be missed. So we look back a few days, and the unique key replaces anything we see twice.']),

    code('A project variable for the lookback', 'dbt_project.yml', """vars:
  lookback_days: 3""", 'yaml', kicker='vars', aside=['From the **project configuration** table in S02', 'Used in SQL as `{{ var(\'lookback_days\') }}`', 'Override at run time: `--vars \'{lookback_days: 7}\'`'],
         say=['How many days back? That is a setting, not code. So it becomes a project variable, the `vars` key from the configuration table we saw in section two.',
              'In SQL we read it with `var`. And we can override it on the command line for one run, without touching the code.'],
         do=['Add the vars block to dbt_project.yml by hand.', 'Optional: open docs/build/project-variables?version=1.']),

    prompt('Make fct_trips incremental: unique_key trip_id, incremental_strategy delete+insert, and on incremental runs only process trips with pickup_at later than the max pickup_at in {{ this }} minus var(\'lookback_days\') days. Leave on_schema_change at its default. Run it once with --full-refresh.',
           watch=['A `config()` block **in the model** beats the folder\'s `table`', '`{% if is_incremental() %}` around the filter', 'Terminal confirm: `--full-refresh`'], habits=[4, 5],
           say=['Code mode. Incremental, unique key, delete+insert, the filter with our variable. I explicitly say: leave `on_schema_change` at its default. You will see why in a minute.',
                'And run it once with full refresh, to build the table from scratch.'],
           do=['New chat, Code mode, paste. Review, Keep, Allow the full-refresh run.']),

    code('fct_trips, now incremental', 'models/marts/fct_trips.sql (top)', """{{ config(
    materialized = 'incremental',
    unique_key = 'trip_id',
    incremental_strategy = 'delete+insert'
) }}

select *
from {{ ref('int_trips__enriched') }}
where is_valid_trip

{% if is_incremental() %}
  and pickup_at > (
      select max(pickup_at) - interval {{ var('lookback_days') }} day
      from {{ this }}
  )
{% endif %}""", 'sql', kicker='Review before Keep',
         aside=['The folder says `table`, the file says `incremental`: **the file wins**', 'Lookback from the variable', 'No `on_schema_change` yet'],
         aside_title='Check',
         say=['Review. The config block at the top: incremental. Our folder config says marts are tables, but the setting in the model file is more specific, so it wins.',
              'The validity filter, and inside the `is_incremental` block, the lookback using our variable. And no `on_schema_change`. Keep.']),

    flow('A new month arrives', [
        dict(label='Add Jan 2025', sub='one more file in `scripts/load_raw.sql`', tag='Load'),
        dict(label='Re-run the load', sub='`raw.yellow_trips` now has 3 months', tag='Load'),
        dict(label='dbt build', sub='staging and everything downstream', tag='dbt', hl=True),
        dict(label='Only January', sub='Run History shows the rows processed', tag='Verify'),
    ], kicker='Real life',
        say=['Now real life happens: the Taxi Commission publishes January 2025. I add the file to our load script and run it again. The raw table now has three months.',
             'Then `dbt build`, selecting staging and everything downstream. In Run History, look at the fact table: only the new rows were processed, not all three months.'],
        do=['Edit scripts/load_raw.sql: add the 2025-01 file. Run it in the SQL editor.', 'Run dbt build --select stg_tlc__yellow_trips+.', 'Show rows processed for fct_trips in Run History.']),

    realdata('January brings a new column', [
        ('`cbd_congestion_fee`', 'in `raw.yellow_trips`: **yes**', None),
        ('missing', 'in `stg_tlc__yellow_trips` and `fct_trips`', None),
        ('5 Jan 2025', 'MTA Congestion Relief Zone fee starts', None),
    ], foot='Staging lists its columns explicitly, so a new source column stops there. On purpose.',
        say=['And here is the surprise I promised in section one. January 2025 has a new column: `cbd_congestion_fee`, the fee for the Manhattan Congestion Relief Zone that started on the fifth of January.',
             'It is in the raw table, thanks to `union_by_name`. But it is **not** in staging or the fact table, because staging lists its columns one by one.',
             'That is a good thing. Nothing changes downstream without us deciding it.'],
        do=['SQL editor: describe raw.yellow_trips, then describe fct_trips. Show the column in one, not the other.']),

    table('What on_schema_change does', ['Value', 'New columns', 'Removed columns'], [
        ['`ignore` (default)', 'not added', 'run fails'],
        ['`fail`', 'run fails', 'run fails'],
        ['`append_new_columns`', '**added**', 'kept'],
        ['`sync_all_columns`', 'added', 'dropped, types synced'],
    ], kicker='Incremental models, v1 docs', size=30, hl_rows=[2],
        foot='None of these **backfill** old rows. New columns are empty for rows loaded before.',
        say=['Back to the docs. When the columns of an incremental model change, `on_schema_change` decides what happens. The default, `ignore`, does not add new columns.',
             '`append_new_columns` adds them. And the docs say something important: none of these options fill in old rows. That needs a full refresh.'],
        do=['Scroll the incremental page to the on_schema_change section.']),

    prompt('The source now has a new column, cbd_congestion_fee (MTA Congestion Relief Zone fee, from 5 January 2025). Add it to reference/tlc_yellow_data_dictionary.md, the source YAML, stg_tlc__yellow_trips, int_trips__enriched and fct_trips. Set on_schema_change on fct_trips so the column is added without a full refresh. Then build.',
           watch=['Five files touched, in lineage order', 'The dictionary file is updated **first**', '`on_schema_change: append_new_columns`'], habits=[1, 4, 5],
           say=['Code mode. The column must flow through every layer: dictionary, source YAML, staging, intermediate, fact. And set `on_schema_change` so the fact table gets the column without a full refresh.',
                'Notice I ask it to update the dictionary file too. That file is the agent\'s memory for this project. If we don\'t update it, the next prompt works with old knowledge.'],
           do=['New chat, Code mode, paste. Review all five diffs. Allow the build.']),

    columns('The result, and the choice', [
        dict(title='append_new_columns', color='accent', items=['Column added to `fct_trips`', 'January rows: filled', 'Nov + Dec rows: **NULL**, as the docs said', 'Fast: no rebuild']),
        dict(title='--full-refresh', color='accent2', items=['Table rebuilt from scratch', 'Every row re-processed', 'Nov + Dec: NULL anyway, the fee didn\'t exist', 'Slow on big tables']),
    ], kicker='Verify', verdict='Here NULL is the **truth**: before 5 January 2025 there was no fee. Know which one you are choosing.',
        say=['The column is there. January rows have values, November and December are NULL, exactly as the docs said: no backfill.',
             'And in this case, NULL is actually correct, because the fee did not exist before January. A full refresh would give the same answer, much slower. In other projects, a full refresh is how you backfill. Know which one you are choosing.'],
        do=['Query fct_trips: count non-null cbd_congestion_fee by month.']),

    recap('Section 10 done', [
        '`fct_trips` processes only new trips, with a lookback from `vars`',
        'The model\'s `config()` overrides the folder\'s `table`',
        'A real new column arrived and stopped at staging, by design',
        '`append_new_columns` carried it through, no backfill',
    ], 's10-end', blocks=['sources', 'seeds', 'models', 'data tests', 'macros', 'analysis'], next='S11 · Snapshots',
        say=['Recap. The fact table is incremental, with a lookback window from a project variable. A real schema change arrived, stopped safely at staging, and we carried it through deliberately.',
             'Tag `s10-end`. Next: data that changes in place, and **snapshots**.']),
])

# =====================================================================================================================
S11 = dict(num=11, file='s11-snapshots', title='Snapshots', short='Snapshots', part=P2, minutes=10,
           blurb='Keep history for data that is changed in place: the TLC vendor list really changed.', slides=[
    title('Snapshots', 'Some tables are updated in place and forget their past. Snapshots remember it.',
          chips=['snapshots/*.yml', 'dbt snapshot', 'check strategy', 'dbt_valid_from / to', 'SCD Type 2'],
          say=['Section eleven: **snapshots**. Trips never change once they happen. But some data is updated in place, and when that happens, the old value is gone. Snapshots keep it.']),

    statement('When a row is updated,<br>the old value is <em>gone</em>.', kicker='The problem',
              sub='Unless you keep it. That is a slowly changing dimension, type 2.',
              say=['Think of a customer\'s address, a product\'s price, a vendor\'s name. The source system just overwrites it. Yesterday\'s value is gone forever.',
                   'Unless we keep history ourselves: one row per version, with the dates each version was valid. That is called a slowly changing dimension, type 2. dbt does it with snapshots.']),

    flow('This really happened to the taxi data', [
        dict(label='Older dictionary', sub='VendorID 2 = **VeriFone Inc.**', tag='Before'),
        dict(label='March 2025 dictionary', sub='VendorID 2 = **Curb Mobility, LLC**', tag='After', hl=True),
        dict(label='New vendors', sub='6 = **Myle Technologies**, 7 = **Helix**', tag='Added'),
    ], kicker='A real change', caption='If we only kept the current list, every old report would show the new name.',
        say=['And this really happened in our data. Older versions of the TLC data dictionary say vendor 2 is VeriFone. The current one says Curb Mobility. And two new vendors appeared, Myle and Helix.',
             'If we only keep the current list, history gets rewritten. Let\'s keep it with a snapshot.']),

    docs('Snapshots', 'docs/build/snapshots', [
        'Configure snapshots in YAML in `snapshots/` (dbt 1.9+), with `relation:` pointing at a source or model.',
        'Required: `unique_key` and a `strategy`: `timestamp` (needs `updated_at`) or `check` (needs `check_cols`).',
        'dbt adds `dbt_valid_from`, `dbt_valid_to`, `dbt_scd_id`, `dbt_updated_at`; current rows have `dbt_valid_to` null.',
        'Run with `dbt snapshot`. Snapshots ignore `--full-refresh`, so history is never wiped.',
    ], say=['The Snapshots page, version one. Since dbt 1.9, a snapshot is configured in a YAML file in the snapshots folder, pointing at a source or model.',
            'It needs a unique key and a strategy. And dbt adds columns that say when each version was valid. The current version has an empty `valid_to`.',
            'And an important safety feature: snapshots ignore full refresh. You cannot accidentally delete history.'],
        do=['Open docs.getdbt.com/docs/build/snapshots?version=1.']),

    columns('Two strategies', [
        dict(title='timestamp', color='accent', sub='The source has an `updated_at`', items=['Compares the timestamp', 'Fast and reliable', 'Needs a trustworthy column']),
        dict(title='check', color='violet', sub='No timestamp available', items=['Compares the values of `check_cols`', 'Works on any table', 'Our vendor list: check `vendor_name`']),
    ], kicker='Strategy',
        say=['Two strategies. **Timestamp**: if the source has a reliable `updated_at` column, dbt compares it. **Check**: if not, dbt compares the actual values of the columns you list.',
             'Our vendor list has no timestamp, so we use `check` on the vendor name.']),

    prompt('Create raw.vendor_registry (vendor_id, vendor_name) with two rows: 1 = Creative Mobile Technologies, LLC and 2 = VeriFone Inc.',
           where='SQL Editor · AI panel', mode='sql', watch=['Approval gate for DDL', 'This plays the "source system"'], habits=[4],
           say=['First we need a source system that changes. In the SQL editor, the agent creates a small vendor registry table with the **old** list: Creative Mobile and VeriFone.',
                'This plays the role of a vendor system that someone updates in place.'],
           do=['SQL Editor AI panel, Code mode. Read and Allow at the approval gate.']),

    prompt('Add vendor_registry to the tlc source. Create snapshots/snap_tlc__vendors.yml on source(\'tlc\', \'vendor_registry\') with the check strategy on vendor_name and unique_key vendor_id, using the YAML snapshot syntax for my dbt version. Run dbt snapshot.',
           watch=['A **YAML** file, not a `{% snapshot %}` block', '`relation: source(...)`', 'Terminal confirm: `dbt snapshot`'], habits=[1, 4, 6],
           say=['Code mode. Add the table to our source, create the snapshot in YAML with the check strategy, and run `dbt snapshot`.',
                'Watch the syntax. Many examples on the internet use an older `{% snapshot %}` block. Our skill says YAML, and the docs page is still open to compare.'],
           do=['New chat, Code mode, paste. Compare with the docs before Keep. Allow dbt snapshot.']),

    code('The snapshot', 'snapshots/snap_tlc__vendors.yml', """snapshots:
  - name: snap_tlc__vendors
    relation: source('tlc', 'vendor_registry')
    config:
      unique_key: vendor_id
      strategy: check
      check_cols: [vendor_name]""", 'yaml', kicker='Review before Keep',
         aside=['YAML, dbt 1.9+', '`check` on `vendor_name`', 'If you see `{% snapshot %}`: Discard, and add it to the skill (habit 6)'],
         aside_title='Check',
         say=['Seven lines. Name, the relation, and the config: unique key, check strategy, check the vendor name.',
              'If the agent wrote the old block syntax instead, discard it. And if it happens twice, that line goes into the skill. Habit six.']),

    table('After the first snapshot', ['vendor_id', 'vendor_name', 'dbt_valid_from', 'dbt_valid_to'], [
        ['1', 'Creative Mobile Technologies, LLC', 'run 1', 'null'],
        ['2', 'VeriFone Inc.', 'run 1', 'null'],
    ], kicker='snap_tlc__vendors', size=30,
        say=['After the first run, the snapshot is a copy of the registry plus validity columns. Both rows are current: `valid_to` is empty.']),

    steps('The registry changes', [
        ('In the SQL editor: vendor 2 becomes **Curb Mobility, LLC**', "update raw.vendor_registry ..."),
        ('Insert vendors 6 (**Myle Technologies Inc**) and 7 (**Helix**)', "insert into raw.vendor_registry ..."),
        ('Take a new snapshot', 'dbt snapshot'),
    ], kicker='Something changes',
        say=['Now someone updates the vendor system. With the SQL editor, behind the approval gate: vendor 2 becomes Curb Mobility, and vendors 6 and 7 are added. Exactly what happened in the real dictionary.',
             'Then `dbt snapshot` again.'],
        do=['SQL editor (approval gate): update vendor 2, insert 6 and 7.', 'Run dbt snapshot (agent or terminal; there is no Project-menu button).']),

    table('History, kept', ['vendor_id', 'vendor_name', 'dbt_valid_from', 'dbt_valid_to'], [
        ['1', 'Creative Mobile Technologies, LLC', 'run 1', 'null'],
        ['2', 'VeriFone Inc.', 'run 1', '**run 2**'],
        ['2', 'Curb Mobility, LLC', '**run 2**', 'null'],
        ['6', 'Myle Technologies Inc', 'run 2', 'null'],
        ['7', 'Helix', 'run 2', 'null'],
    ], kicker='snap_tlc__vendors', size=29, hl_rows=[1, 2],
        say=['And here it is. Vendor 2 now has **two** rows. VeriFone, valid until the second run. Curb Mobility, valid from the second run, and current.',
             'The new vendors were simply added. Nothing was lost. Any report can now ask: what was this vendor called at the time of the trip?'],
        do=['Query the snapshot ordered by vendor_id, dbt_valid_from.']),

    dag('Snapshot and current dimension', 11, files=['snapshots/snap_tlc__vendors.yml', 'models/marts/dim_vendors.sql'],
        say=['On the graph: the new source, the snapshot, and a `dim_vendors` model. I ask the agent to build that dimension from the current rows of the snapshot, the ones where `valid_to` is empty.'],
        do=['Ask (Code mode): "Create dim_vendors from snap_tlc__vendors, current rows only, with YAML and a primary-key test." Review, Keep, build.']),

    recap('Section 11 done', [
        'Snapshots keep history of data that is updated in place',
        'YAML config, `check` strategy on `vendor_name`',
        'A real dictionary change, kept as two versions',
        '`dim_vendors` built from the current snapshot rows',
    ], 's11-end', blocks=['sources', 'seeds', 'models', 'data tests', 'macros', 'analysis', 'snapshots'], next='S12 · Docs, lineage & exposures: the capstone',
        say=['Recap. Snapshots keep history. We used the check strategy on a real change from the TLC dictionary, and built a current dimension on top.',
             'Block ticked: **snapshots**. Tag `s11-end`. Last build section: documentation, lineage, and a real answer.']),
])

# =====================================================================================================================
S12 = dict(num=12, file='s12-docs-exposures', title='Docs, lineage & exposures: the capstone', short='Docs & exposures', part=P2, minutes=12,
           blurb='Doc blocks, the docs site, asking the project questions, answering the capstone, and declaring an exposure.', slides=[
    title('Docs, lineage & exposures', 'The project explains itself, and answers a real question.',
          chips=['description', 'doc blocks', 'dbt docs generate', 'Lineage', 'exposures', 'Capstone'],
          say=['Section twelve, the capstone. We make the project explain itself with documentation, we ask it questions, we answer a real question about congestion pricing, and we declare who uses our work.']),

    statement('Docs that live next to the code<br>get <em>updated</em> with the code.', kicker='Key idea',
              sub='Descriptions in YAML, shared text in doc blocks, and a generated website with lineage.',
              say=['Documentation in a wiki goes stale, because nobody updates it when the code changes. In dbt, the documentation lives in the same YAML files as the tests, in the same pull request as the code.',
                   'And dbt turns it into a website, with a lineage graph, for free.']),

    docs('Documentation', 'docs/build/documentation', [
        'Add a `description` to models, sources, seeds, snapshots and columns in YAML.',
        '**Doc blocks**: `{% docs name %}…{% enddocs %}` in `.md` files, used with `{{ doc(\'name\') }}`.',
        '`dbt docs generate` builds the docs; `dbt docs serve` opens the site locally.',
    ], say=['The Documentation page, version one. Descriptions go in YAML. When the same text is needed in many places, like what a payment type is, you write a **doc block** once and reference it everywhere.',
            '`dbt docs generate` builds the documentation, and `dbt docs serve` opens it as a website.'],
        do=['Open docs.getdbt.com/docs/build/documentation?version=1.']),

    columns('A doc block, written once, used everywhere', [
        dict(title='models/docs.md', color='violet', code="{% docs payment_type %}\nHow the passenger paid, from the TLC\ndata dictionary: 0 = Flex Fare,\n1 = Credit card, 2 = Cash, 3 = No charge,\n4 = Dispute, 5 = Unknown, 6 = Voided trip.\n{% enddocs %}", lang='md', size=23),
        dict(title='any YAML', color='accent', code="- name: payment_type_id\n  description: '{{ doc(\"payment_type\") }}'", lang='yaml', size=24,
             foot='Source, staging, intermediate and fct: one text, four columns.'),
    ], kicker='Doc blocks',
        say=['On the left, a doc block in a Markdown file: the payment type explanation, written once.',
             'On the right, how any YAML uses it: `doc`, with the block\'s name. The payment type column appears in four models. One text, always consistent.']),

    prompt('Create models/docs.md with doc blocks for payment type, rate code and trip validity, and use them in every YAML that describes those columns. Make sure every model and column has a description.',
           watch=['Text comes from the dictionary file', 'Every YAML that has those columns updated', 'Nothing left without a description'], habits=[1, 4],
           say=['This is tedious work across many files: a perfect agent task. Doc blocks for payment type, rate code and validity, used everywhere, and every model and column described.'],
           do=['New chat, Code mode, paste. Review a few diffs, Keep all.']),

    steps('Generate and open the docs site', [
        ('Build the documentation', 'dbt docs generate'),
        ('Serve it locally', 'dbt docs serve'),
        ('Open `fct_trips`: descriptions, columns, tests, SQL', None),
        ('Compare the docs lineage with Rosetta\'s lineage view', None),
    ], kicker='Verify',
        say=['From the Project menu: docs generate, then docs serve. A website opens. Click `fct_trips`: description, every column, the tests, the SQL, compiled and raw.',
             'And the lineage graph at the bottom. Compare it with Rosetta\'s own lineage view: same project, same graph.'],
        do=['Project menu → docs generate, then docs serve. Navigate to fct_trips and its lineage.']),

    prompt('Trace cbd_congestion_fee from the source to every model that uses it.',
           mode='ask', watch=['Source → staging → intermediate → fct', 'It reads the files, not memory'], habits=[5],
           say=['Now the project explains itself. Ask mode. "Trace the congestion fee from the source to every model that uses it."',
                'The agent reads the files and gives the path: the source, staging, intermediate, the fact table. That used to take a person half an hour.'],
           do=['New chat, Ask mode.']),

    prompt('What is the grain of agg_zone_daily, and can I join it to fct_trips without fan-out?',
           mode='ask', watch=['Grain: pickup zone × day', 'Joining to trips multiplies rows', 'A good question before any join'], habits=[5],
           say=['One more. "What is the grain of `agg_zone_daily`, and can I join it to `fct_trips` without fan-out?"',
                'Grain is one row per zone per day. Joining it to trips repeats each daily row for every trip. That is a fan-out, and the agent should warn us. Exactly the question to ask before writing a join.']),

    statement('How much CBD congestion fee was collected in January 2025, and <em>where</em>?', kicker='The capstone question',
              sub='Everything we built, used to answer one real question.',
              say=['And now the question the whole project was building towards. January 2025 was the first month of New York\'s congestion pricing for taxis. How much fee was collected, and where?']),

    prompt('How much CBD congestion fee was collected in January 2025 by pickup borough, and what share of trips paid it?',
           where='Analytics page or Dive', mode='ask', watch=['Built on `fct_trips` + `dim_zones`', 'Only valid trips are counted', 'A chart, not just a table'], habits=[5],
           say=['I ask it in Rosetta\'s analytics, on top of our marts. Because it uses `fct_trips`, only valid trips count, and because of `dim_zones`, we get boroughs instead of IDs.',
                'Everything we built is in this answer: the source, the staging, the validity rules, the incremental load, the new column.'],
           do=['Use the Analytics page or a Dive, whichever ships in the release you record with. Show the chart.']),

    realdata('The answer', [
        ('?', 'total CBD fee collected, January 2025', 'cbd_total'),
        ('?', 'share of valid trips that paid it', 'cbd_share'),
        ('?', 'borough with the most fee collected', 'cbd_top'),
    ], kicker='Capstone',
        foot='From raw Parquet to a tested, documented answer, in one project.',
        say=['And the answer. [Read the numbers.] From raw Parquet files to a tested, documented, explainable answer.'],
        do=['Before recording: type the three numbers from your dry run into the amber fields.']),

    docs('Exposures', 'docs/build/exposures', [
        'An exposure describes a **downstream use** of your project: a dashboard, notebook, analysis, ML model or application.',
        'It has a `type`, an `owner`, and `depends_on`: the models it uses.',
        'Exposures appear in the **lineage** and in the docs site.',
    ], say=['Last block: **exposures**. Our analysis is now something people rely on. An exposure tells dbt that, so the lineage shows who uses which models.',
            'It has a type, an owner, and the models it depends on. If someone changes `fct_trips` tomorrow, they see this analysis downstream.'],
        do=['Open docs.getdbt.com/docs/build/exposures?version=1.']),

    code('Declare it', 'models/marts/_exposures.yml', """exposures:
  - name: cbd_fee_analysis
    label: CBD congestion fee, January 2025
    type: analysis
    maturity: medium
    owner:
      name: Data team
      email: data@example.com
    depends_on:
      - ref('fct_trips')
      - ref('dim_zones')
    description: Fee collected and share of trips paying it, by pickup borough.""", 'yaml', kicker='Agent result',
         aside=['Type, owner, maturity', '`depends_on` draws the arrows', 'Use a real team address in your project'],
         say=['I ask the agent to declare it. This is the result: name, a readable label, type analysis, an owner, and `depends_on` with our two marts.'],
         do=['Code mode prompt: "Declare this analysis as an exposure in models/marts/_exposures.yml that depends on fct_trips and dim_zones." Keep.']),

    dag('The complete project', 12, all_built=True, new=['exp'], files=['models/docs.md', 'models/marts/_exposures.yml'],
        say=['And here is the complete project. Every node built. On the far right, our exposure: the analysis, connected to the marts it uses.',
             'From two Parquet files to this, in twelve sections.'],
        do=['Regenerate docs; show the exposure in the docs lineage and in Rosetta.']),

    recap('Section 12 done', [
        'Every model and column described; shared text in doc blocks',
        'The docs site and lineage, generated from the project',
        'The project answered questions about itself',
        'The capstone answered, and declared as an exposure',
    ], 's12-end', blocks=['sources', 'seeds', 'models', 'data tests', 'macros', 'analysis', 'snapshots', 'docs', 'exposures'], next='S13 · Wrap-up & what\'s next',
        say=['Recap. Fully documented, a docs website, a project that explains itself, a real answer, and an exposure.',
             'The last two blocks: **docs** and **exposures**. Tag `s12-end`. One short section left: the wrap-up.']),
])

# =====================================================================================================================
S13 = dict(num=13, file='s13-wrap-up', title='Wrap-up & what\'s next', short='Wrap-up', part=P2, minutes=5,
           blurb='What we built, the blocks map fully ticked, the six habits, and where to go next.', slides=[
    title('Wrap-up & what\'s next', 'What we built, what we learned, and where to go from here.',
          chips=['14 sections', '9 dbt blocks', '1 real project'],
          say=['The final section. Let\'s look back at what we built, and where you can go next.']),

    dag('What we built', 13, all_built=True, new=[],
        say=['This is your project. Sources and seeds on the left. Staging, an intermediate model with tested business logic, and marts. A snapshot keeping history. And an exposure, a real analysis, on the right.',
             'Real data, real problems, real decisions.']),

    blocks('The blocks map, ticked', upto=13, kicker='About dbt projects (v1)',
           foot='Next up from the same page: metrics, semantic models, saved queries, groups, user-defined functions.',
           say=['Remember the map from section two? Every block we planned is ticked: models, sources, seeds, data tests, macros, analysis, snapshots, docs and exposures.',
                'The dashed ones are your next steps: the semantic layer with metrics, semantic models and saved queries, groups for larger teams, and user-defined functions.']),

    habits('The six habits', hl=[1, 4, 5],
           say=['And the six habits. If you take only three with you: give the agent **context** instead of trusting its memory. **Read every diff** before you keep it. And let **dbt be the judge**: run, test, look at the rows.',
                'The agent made us faster in every section. But every decision in this project, every test we kept or dropped, every rule, was ours.']),

    table('Commands we used', ['Command', 'What it did for us'], [
        ['`dbt debug`', 'checked the setup'],
        ['`dbt seed`', 'loaded the CSV lookups'],
        ['`dbt run` · `dbt build`', 'built models (and tested them)'],
        ['`dbt test`', 'data tests and unit tests'],
        ['`dbt compile`', 'showed what Jinja became'],
        ['`dbt deps`', 'installed `dbt_utils`'],
        ['`dbt snapshot`', 'kept vendor history'],
        ['`dbt docs generate` · `serve`', 'built and opened the docs site'],
    ], kicker='dbt v1 commands', size=27,
        say=['The dbt commands we used, all version one. Debug, seed, run and build, test, compile, deps, snapshot, and docs.',
             'In Rosetta most of them are buttons. Now you know what each button does.']),

    bullets('Where to go next', [
        ('The Semantic Layer', 'Metrics, semantic models and saved queries: define "revenue" once.'),
        ('Model contracts and groups', 'Guarantee column names and types for the people who depend on you.'),
        ('Python models', 'dbt-duckdb can run Python models next to your SQL.'),
        ('CI and deployment', 'Run `dbt build` on every pull request, and on a schedule, with Rosetta Cloud.'),
        ('Ingestion', 'Replace our load script with a real loader.'),
    ], kicker='Next steps',
        say=['Where to go next. The semantic layer, to define metrics like revenue once. Contracts and groups, when other teams depend on your models. Python models, which dbt-duckdb supports.',
             'And CI and deployment: running `dbt build` automatically on every change. There is a separate video about deploying with Rosetta Cloud.']),

    statement('Thanks for building<br>with <em>us</em>.', kicker='The end',
              sub='Rosetta dbt Studio · the course project and prompts are in the companion repository.',
              say=['Thank you for building this with me. The project, every checkpoint tag, and every prompt from these slides are in the companion repository.',
                   'Clone it, check out any tag, and try the prompts yourself. And let us know what you build.']),
])

DECKS = [S09, S10, S11, S12, S13]
