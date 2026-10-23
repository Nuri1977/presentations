from lib import (title, statement, bullets, flow, columns, code, docs, prompt, table, realdata, dag, blocks, recap,
                 habits, steps)

P1 = 'Part 1 · Core'

# =====================================================================================================================
S05 = dict(num=5, file='s05-staging-models', title='Staging models', short='Staging models', part=P1, minutes=12,
           blurb='A model is a select. One by hand, the big one with the agent, and ref() building the DAG.', slides=[
    title('Staging models', 'Our first models: clean, renamed, typed building blocks, one per source table.',
          chips=['SQL models', 'ref()', 'Preview', 'Compiled SQL', 'stg_ naming'],
          say=['Section five. We finally write models. Staging models are the first layer: they take a source and make it clean and consistent, nothing more.',
               'I write the first one by hand so you see exactly what a model is. Then the agent writes the big one, and we review it.']),

    statement('A model is just<br>a <em>select</em> statement.', kicker='Key idea',
              sub='One `.sql` file, one `select`. The file name is the model name. dbt writes the `create view` or `create table` for you.',
              say=['If you remember one thing from this section: a dbt model is just a select statement in a file.',
                   'You never write `create table` or `insert`. The file name becomes the model name, and dbt wraps your select in the right DDL, depending on the materialization.']),

    docs('SQL models', 'docs/build/sql-models', [
        'A SQL model is a `select` statement in a `.sql` file inside `models/`.',
        'The **file name** becomes the **name** of the view or table dbt builds.',
        'Use `{{ ref(\'model_name\') }}` to select from another model; dbt builds them in the right order.',
        'The default materialization is a **view**; change it with configs.',
    ], say=['The SQL models page, version one. A model is one select statement in a `.sql` file in your models folder. The file name becomes the name of the object in the database.',
            'To use another model, you never type its table name. You use `ref`, and dbt works out the dependency and the build order.',
            'And by default, a model becomes a view. We already changed that per folder in `dbt_project.yml`.'],
        do=['Open docs.getdbt.com/docs/build/sql-models?version=1.']),

    columns('What you write vs what dbt runs', [
        dict(title='You write', color='accent', code="select\n    \"LocationID\" as location_id,\n    \"Borough\"    as borough\nfrom {{ ref('taxi_zone_lookup') }}", lang='sql', size=25),
        dict(title='dbt runs', color='good', code="create view \"nyc_taxi\".\"main\".\"stg_tlc__taxi_zones\" as (\n  select\n    \"LocationID\" as location_id,\n    \"Borough\"    as borough\n  from \"nyc_taxi\".\"main\".\"taxi_zone_lookup\"\n)", lang='sql', size=22),
    ], kicker='Compiled SQL', verdict='The **Compiled SQL** tab in Rosetta shows the right-hand side for any model.',
        say=['On the left, what we write: a select, with `ref` to the seed. On the right, roughly what dbt sends to DuckDB: a `create view`, with `ref` replaced by the real table name.',
             'You never need to guess what dbt does. The Compiled SQL tab in Rosetta shows you the compiled version of any model.'],
        do=['Exact database/schema names depend on your profile; point at the ref being replaced.']),

    flow('ref() builds the DAG', [
        dict(label='taxi_zone_lookup', sub='seed', tag='Input', color='teal'),
        dict(label='stg_tlc__taxi_zones', sub='`ref(\'taxi_zone_lookup\')`', tag='Model', color='blue', hl=True),
        dict(label='dim_zones', sub='`ref(\'stg_tlc__taxi_zones\')`', tag='Model · later', color='blue', dim=True),
    ], kicker='Dependencies', caption='Every `ref()` and `source()` is an arrow in the lineage graph. dbt builds from left to right.',
        say=['Each `ref` is an arrow. Our staging model refs the seed, so the seed must exist first. Later, a dimension will ref the staging model.',
             'dbt reads all these references, draws the graph, and builds things from left to right. That is why you never manage the order yourself.']),

    docs('How we structure: Staging', 'best-practices/how-we-structure/2-staging', [
        'Name files `stg_[source]__[entity]s.sql`: the double underscore separates source and entity.',
        'Do: **renaming**, **type casting**, basic computations, categorizing with `case when`.',
        'Don\'t: **joins** or **aggregations**. Staging stays one-to-one with the source.',
        'Materialize staging models as **views**.',
    ], say=['The staging page of the structure guide. The naming: `stg_`, the source name, two underscores, the entity in plural. So: `stg_tlc__yellow_trips`.',
            'What belongs here: renaming, casting types, small computations, and categorizing with case-when. What does not: joins and aggregations. A staging model has the same rows as its source.',
            'And they are views, which is exactly what we configured for the staging folder.'],
        do=['Open the staging page (v1), scroll to the naming and "do / don\'t" parts.']),

    columns('Staging: do and don\'t', [
        dict(title='Do', color='good', mark='good', items=['Rename to snake_case', 'Cast types (money → decimal)', 'Turn Y/N into a boolean', 'Keep every row, keep lineage columns']),
        dict(title='Don\'t', color='bad', mark='bad', items=['Join to other tables', 'Aggregate or group', 'Filter out "bad" rows', 'Add business rules']),
    ], kicker='Rules we follow', verdict='Dirty rows stay in staging for now. We **flag** them later, in the intermediate layer.',
        say=['Our rules, as a checklist. Rename, cast, turn the Y/N flag into a real boolean, keep every row.',
             'No joins, no aggregations, and, important with our messy data: **no filtering**. We do not delete the strange trips here. We flag them later, where the business rule belongs.']),

    code('By hand: the zones model', 'models/staging/tlc/stg_tlc__taxi_zones.sql', """with source as (

    select * from {{ ref('taxi_zone_lookup') }}

),

renamed as (

    select
        "LocationID"   as location_id,
        "Borough"      as borough,
        "Zone"         as zone_name,
        service_zone
    from source

)

select * from renamed""", 'sql', kicker='Hands on',
         aside=['`ref()` to the seed, never a table name', 'CTEs: `source` → `renamed` → final select', 'Only renaming: one row in, one row out'],
         say=['Here is my first model, typed by hand. Two CTEs. `source` selects everything from the seed, with `ref`. `renamed` gives each column a clean snake-case name.',
              'And a final `select *`. This CTE pattern, import first, then transform, then a final select, is what the skill tells the agent to follow too.'],
         do=['Create models/staging/tlc/stg_tlc__taxi_zones.sql and type it.']),

    steps('Run it, preview it, read the compiled SQL', [
        ('Run the model with the model button', 'dbt run --select stg_tlc__taxi_zones'),
        ('**Preview** tab: the first rows, renamed', None),
        ('**Compiled SQL** tab: `ref` became the real table', None),
        ('No `config()` in the file: it is a **view** because of its folder', None),
    ], kicker='Verify',
        say=['Run it with the model button. Then the Preview tab: there are the zones, with clean names.',
             'Then the Compiled SQL tab: `ref` has become the full table name.',
             'Notice I never wrote "view" in this file. It is a view because it lives in the staging folder. The config we set in section two is doing its job.'],
        do=['Click Run on the model, then Preview, then Compiled SQL.']),

    table('The big one: how trip columns get renamed', ['Raw column', 'Staging column', 'Change'], [
        ['`VendorID`', '`vendor_id`', 'rename'],
        ['`tpep_pickup_datetime` · `tpep_dropoff_datetime`', '`pickup_at` · `dropoff_at`', 'rename, `_at` suffix'],
        ['`trip_distance`', '`trip_distance_miles`', 'rename, unit in the name'],
        ['`RatecodeID` · `payment_type`', '`rate_code_id` · `payment_type_id`', 'rename'],
        ['`PULocationID` · `DOLocationID`', '`pickup_location_id` · `dropoff_location_id`', 'rename'],
        ['`store_and_fwd_flag`', '`is_store_and_forward`', 'Y/N → boolean'],
        ['`fare_amount` … `total_amount`', 'same names', 'cast to `decimal(10,2)`'],
        ['`filename`', '`source_file`', 'keep for lineage'],
    ], kicker='stg_tlc__yellow_trips', size=26,
        say=['The trips staging model is bigger: twenty columns. Here is what should happen to them.',
             'Timestamps get the `_at` suffix. Distance gets its unit in the name. The ID columns become snake case. The Y/N flag becomes a real boolean called `is_store_and_forward`. Money becomes a decimal. And `filename` becomes `source_file`, so we always know which monthly file a row came from.',
             'This is repetitive work. A perfect job for the agent, with the skill telling it our conventions.']),

    prompt('Following the nyc-taxi-dbt-conventions skill, create stg_tlc__yellow_trips from source(\'tlc\', \'yellow_trips\'). Rename every column to snake_case, timestamps end in _at, store_and_fwd_flag becomes a boolean, money columns are decimal(10,2), and keep the source filename as source_file. No filters, no joins. Add stg_tlc__yellow_trips.yml with descriptions taken from the source YAML. Then build only this model.',
           watch=['It loads the **skill** and reads the source YAML', 'Two files open as tabs: SQL and YAML', 'Terminal confirm: `dbt build --select stg_tlc__yellow_trips`'],
           habits=[1, 4, 5],
           say=['The prompt. Code mode, new chat. I name the skill explicitly, then give the rules: snake case, `_at`, boolean, decimals, keep `source_file`. No filters, no joins. A YAML file with descriptions copied from the source. And build only this model.',
                'Watch the tool calls. It should load the skill, read the source YAML, write two files, and then ask to run `dbt build` for just this model.'],
           do=['New chat, Code mode, paste the prompt.', 'Allow the dbt build when asked.']),

    code('What good looks like', 'models/staging/tlc/stg_tlc__yellow_trips.sql', """with source as (
    select * from {{ source('tlc', 'yellow_trips') }}
),
renamed as (
    select
        "VendorID"                          as vendor_id,
        tpep_pickup_datetime                as pickup_at,
        tpep_dropoff_datetime               as dropoff_at,
        passenger_count,
        trip_distance                       as trip_distance_miles,
        "RatecodeID"                        as rate_code_id,
        store_and_fwd_flag = 'Y'            as is_store_and_forward,
        "PULocationID"                      as pickup_location_id,
        "DOLocationID"                      as dropoff_location_id,
        payment_type                        as payment_type_id,
        cast(fare_amount as decimal(10,2))  as fare_amount,
        -- ... other money columns cast the same way ...
        cast(total_amount as decimal(10,2)) as total_amount,
        filename                            as source_file
    from source
)
select * from renamed""", 'sql', kicker='Review before Keep',
         aside=['`source()`, not a table name', 'Casts on every money column', '**No** `where` clause', 'No `config()`: the folder makes it a view'],
         aside_title='Check',
         say=['This is the shape I expect, shortened in the middle. Read it like a reviewer.',
              '`source`, not a hard-coded table. Every money column cast to a decimal. The flag compared to `\'Y\'`, which gives a boolean. `source_file` at the end.',
              'And the two things that must **not** be there: no `where` clause, and no `config` block. If the agent added either, I ask it to remove them before I keep the file.'],
         do=['Scroll through the agent\'s file. Check the four points on the right, then Keep both files.']),

    dag('Staging in the DAG', 5, files=['stg_tlc__yellow_trips.sql', 'stg_tlc__yellow_trips.yml', 'stg_tlc__taxi_zones.sql'],
        say=['Two new nodes: our staging models, each fed by exactly one input. One-to-one, just as the guide says.',
             'Open the lineage view in Rosetta and you will see the same picture.'],
        do=['Open the lineage view for stg_tlc__yellow_trips.']),

    recap('Section 05 done', [
        'A model is a select; the folder decided it is a view',
        '`ref()` and `source()` create the arrows in the DAG',
        'One staging model by hand, one by the agent, both reviewed',
        'Dirty rows kept on purpose: we flag them later',
    ], 's05-end', blocks=['sources', 'seeds', 'models'], next='S06 · Data tests',
        say=['Recap. Models are select statements. `ref` and `source` build the graph. We wrote one staging model ourselves and had the agent write the big one, following our skill, and we reviewed it.',
             'Third block: **models**, at least the first layer. Tag `s05-end`. Next: we write down what we expect from the data, with **tests**.']),
])

# =====================================================================================================================
S06 = dict(num=6, file='s06-data-tests', title='Data tests', short='Data tests', part=P1, minutes=12,
           blurb='Generic and singular tests, real failures, and deciding between error, warn and a flag.', slides=[
    title('Data tests', 'Write down what we expect from the data, watch real data break it, and decide what to do.',
          chips=['data_tests:', 'unique · not_null', 'accepted_values · relationships', 'Singular tests', 'severity'],
          say=['Section six: **data tests**. A test is how we write down an assumption, so dbt can check it every single run.',
               'With real data, some assumptions will be wrong. That is not a problem. That is the point.']),

    statement('A test is a query<br>that should return <em>zero rows</em>.', kicker='Key idea',
              sub='dbt runs it. Zero failing rows: pass. Any rows: fail, and you can look at them.',
              say=['Under the hood, every dbt test is a select query that looks for **bad rows**. If it returns zero rows, the test passes. If it returns any, it fails.',
                   'That makes tests easy to understand and easy to debug: the failing rows are right there to look at.']),

    columns('The four built-in generic tests', [
        dict(title='unique', color='accent', items=['No duplicate values', 'Primary keys']),
        dict(title='not_null', color='accent', items=['No empty values', 'Required columns']),
        dict(title='accepted_values', color='teal', items=['Only values from a list', 'Codes, statuses']),
        dict(title='relationships', color='violet', items=['Every value exists in another model', 'Foreign keys']),
    ], kicker='Generic tests',
        say=['dbt ships with four generic tests. `unique` and `not_null`, usually together on a primary key.',
             '`accepted_values`, for columns that must contain one of a known list, like payment types. And `relationships`, which checks that every value exists in another model, like a foreign key.',
             'You attach them to columns in YAML, with one line each.']),

    columns('Generic vs singular', [
        dict(title='Generic', color='accent', sub='Reusable, configured in YAML', code="columns:\n  - name: location_id\n    data_tests:\n      - unique\n      - not_null", lang='yaml', size=25),
        dict(title='Singular', color='accent2', sub='One SQL file in tests/', code="-- returns the bad rows\nselect *\nfrom {{ ref('stg_tlc__yellow_trips') }}\nwhere dropoff_at < pickup_at", lang='sql', size=25),
    ], kicker='Two kinds',
        say=['Two kinds. **Generic** tests are reusable: you list them under a column in YAML. **Singular** tests are a SQL file in the `tests` folder, written for one specific check.',
             'A singular test is just the query for the bad rows. This one returns trips that end before they start.']),

    docs('Data tests', 'docs/build/data-tests', [
        'Generic tests go under the `data_tests:` key of a model, source or seed column in YAML.',
        'Singular tests are `.sql` files in `tests/` that return the failing rows.',
        'Configure with `severity` (`error` or `warn`), `where`, and `store_failures`.',
        'Run them with `dbt test`, or together with models using `dbt build`.',
    ], say=['The Data tests page, version one. Generic tests go under the `data_tests` key in YAML. Singular tests are SQL files in the tests folder.',
            'And there are configs: `severity`, error or warn; `where`, to test only some rows; and `store_failures`, to keep the failing rows in a table so you can query them.',
            'You run them with `dbt test`, or with `dbt build`, which builds and tests in one go.'],
        do=['Open docs.getdbt.com/docs/build/data-tests?version=1.']),

    code('By hand: test the zones', 'models/staging/tlc/stg_tlc__taxi_zones.yml', """models:
  - name: stg_tlc__taxi_zones
    description: One row per TLC taxi zone.
    columns:
      - name: location_id
        description: TLC taxi zone ID.
        data_tests:
          - unique
          - not_null""", 'yaml', kicker='Hands on', aside=['The primary key gets `unique` + `not_null`', 'The same key, `data_tests:`, works for models, sources and seeds'],
         say=['First, by hand: the zone ID is our primary key, so it gets `unique` and `not_null`. Two lines.',
              'Run `dbt test --select stg_tlc__taxi_zones`. Green. The official lookup is clean.'],
         do=['Write the YAML, run dbt test --select stg_tlc__taxi_zones.']),

    prompt('In stg_tlc__yellow_trips.yml add data tests: not_null on pickup_at and dropoff_at; accepted_values on payment_type_id using the codes in seeds/payment_types.csv; relationships from pickup_location_id and dropoff_location_id to stg_tlc__taxi_zones.location_id. Write a singular test, tests/assert_trip_ends_after_it_starts.sql. Run dbt test for this model only.',
           watch=['Codes come from the seed file, 0 to 6', 'A new file in `tests/`', 'Terminal confirm for `dbt test`'], habits=[1, 4, 5],
           say=['The rest goes to the agent. Not-null on the timestamps, accepted values on payment type, using the seed so the list is correct, relationships from both location columns to the zones, and the singular test for backwards trips.',
                'Then run the tests for this model only.'],
           do=['New chat, Code mode, paste the prompt. Review both files, Keep, Allow dbt test.']),

    code('What it should write', 'stg_tlc__yellow_trips.yml (excerpt)', """      - name: payment_type_id
        data_tests:
          - accepted_values:
              arguments:            # dbt 1.10.5+
                values: [0, 1, 2, 3, 4, 5, 6]
                quote: false
      - name: pickup_location_id
        data_tests:
          - relationships:
              arguments:
                to: ref('stg_tlc__taxi_zones')
                field: location_id""", 'yaml', kicker='Review before Keep',
         aside=['Values **0 to 6**, from the seed', 'In recent dbt v1, test values go under `arguments:`', '`quote: false` because the codes are numbers'],
         aside_title='Check',
         say=['The part to review. Accepted values zero to six, taken from the seed. Recent dbt v1 versions put a test\'s values under `arguments`. Older v1 versions put them directly under the test; both are in the docs.',
              '`quote: false` because these are numbers, not strings. And the relationships test points at the zones model and the `location_id` field.']),

    code('The singular test', 'tests/assert_trip_ends_after_it_starts.sql', """-- A trip cannot end before it starts.
-- Returns the offending rows; zero rows = pass.
select
    source_file,
    pickup_at,
    dropoff_at
from {{ ref('stg_tlc__yellow_trips') }}
where dropoff_at < pickup_at""", 'sql', kicker='tests/',
         aside=['It uses `ref()`, so it shows in the DAG', 'Returns the bad rows, with `source_file`'],
         say=['And the singular test. A plain query for the rows that break our rule: dropoff before pickup. I like that it returns `source_file`, so we can see which month the bad rows came from.']),

    realdata('Real data says no', [
        ('?', 'trips that **end before they start**', 'backwards'),
        ('FAIL', '`assert_trip_ends_after_it_starts`', None),
        ('PASS', '`accepted_values` on `payment_type_id`', None),
    ], foot='The source system really contains these rows. Now we decide what to do about it.',
        say=['And here is the result. [Read the number.] trips end before they start. The singular test fails. The accepted values test passes, because we used the current code list.',
             'These rows are really in the government data. So, what do we do?'],
        do=['Before recording: type the number of backwards trips from your dry run. If accepted_values fails in your run, change PASS and talk about it.']),

    steps('Ask the AI assistant on the error', [
        ('Open **Run History** → the failed test → error view', None),
        ('Click the **AI assistant** and let it propose a fix', None),
        ('Read the proposal. Don\'t keep it yet.', None),
    ], kicker='Run History',
        say=['Rosetta has a shortcut for exactly this moment. In Run History, open the failed test, and in the error view there is an AI assistant. Let it propose a fix.',
             'It will probably suggest filtering those rows out. Let\'s read the suggestion, and then make the decision ourselves.'],
        do=['Run History → failed test → AI assistant. Read its proposal aloud.']),

    columns('The decision is yours', [
        dict(title='Delete the rows in staging', color='bad', mark='bad', items=['Hides a real problem', 'Breaks "staging keeps every row"']),
        dict(title='Warn and keep the failures', color='good', mark='good', items=['`severity: warn`', '`store_failures: true`', 'Visible, queryable, not blocking']),
        dict(title='Flag in intermediate', color='good', mark='good', items=['`is_valid_trip` + reason', 'Marts keep only valid trips', 'Section 08']),
    ], kicker='Error, warn, or flag', verdict='A failing test is a **decision**, not a bug. Here: warn now, flag later.',
        say=['Three options. Delete the rows in staging: easy, but it hides a real problem and breaks our staging rule. No.',
             'Make the test a **warning** and **store the failures**, so we can see and query the bad rows without blocking every build. Yes.',
             'And in section eight, we add an `is_valid_trip` flag in the intermediate layer, and the fact table keeps only valid trips. That is where business rules belong.'],
        do=['If the AI assistant proposed filtering in staging: click Discard and say why.']),

    code('Warn, and keep the evidence', 'tests/assert_trip_ends_after_it_starts.sql', """{{ config(severity = 'warn', store_failures = true) }}

-- A trip cannot end before it starts.
select
    source_file,
    pickup_at,
    dropoff_at
from {{ ref('stg_tlc__yellow_trips') }}
where dropoff_at < pickup_at""", 'sql', kicker='Hands on',
         aside=['Build continues, with a warning', 'Failing rows saved to a table', 'Query them in the SQL editor'],
         say=['One line at the top: severity warn, store failures true. Run the tests again: it is a warning now, not an error, and dbt saved the failing rows into a table.',
              'In the SQL editor I can query that table and see every backwards trip.'],
         do=['Add the config line by hand. Run dbt test again. Query the stored-failures table in the SQL editor.']),

    recap('Section 06 done', [
        'A test is a query for bad rows: zero rows means pass',
        'Generic tests in YAML, a singular test in `tests/`',
        'Real data failed a test, and the AI assistant proposed a fix',
        'We chose: **warn** + **store failures** now, **flag** in S08',
    ], 's06-end', blocks=['sources', 'seeds', 'models', 'data tests'], next='S07 · Packages, Jinja, macros & analyses',
        say=['Recap. Tests are queries for bad rows. We used generic and singular tests. Real data failed one, we listened to the AI assistant, and then we made the call ourselves.',
             'Fourth block: **data tests**. Tag `s06-end`. Next: reusing code, with packages, Jinja and macros.']),
])

# =====================================================================================================================
S07 = dict(num=7, file='s07-packages-jinja-macros', title='Packages, Jinja, macros & analyses', short='Packages, Jinja & macros', part=P1, minutes=12,
           blurb='dbt_utils for a surrogate key, Jinja expressions and loops, a safe_divide macro, and an analysis.', slides=[
    title('Packages, Jinja, macros & analyses', 'Reuse other people\'s code, write our own reusable SQL, and see exactly what Jinja compiles to.',
          chips=['packages.yml', 'dbt deps', 'dbt_utils', '{{ }} · {% %}', 'macros/', 'analyses/'],
          say=['Section seven. So far our SQL has been plain. Now we make it smarter: install a package, use Jinja, write a macro, and meet analyses.']),

    statement('Taxi trips have<br><em>no primary key</em>.', kicker='The problem',
              sub='No trip ID in the data. To test uniqueness, and later to update rows, we need one.',
              say=['Here is a real problem. The taxi data has no trip ID. There is no column that identifies one trip.',
                   'We need a primary key: to test that trips are unique, and in section ten, so an incremental model knows which rows to replace. We will build one from several columns, with a package.']),

    docs('Packages', 'docs/build/packages', [
        'Packages are dbt projects you install into yours: macros, models, tests.',
        'List them in `packages.yml`, then run `dbt deps` to install them into `dbt_packages/`.',
        'Pin a **version range**; find packages on **hub.getdbt.com**.',
    ], say=['The Packages page. A package is simply another dbt project that you install into yours, usually for its macros and tests.',
            'You list packages in `packages.yml` and run `dbt deps`. The most widely used one is `dbt_utils`, from dbt Labs.'],
        do=['Open docs.getdbt.com/docs/build/packages?version=1.']),

    prompt('Add dbt-labs/dbt_utils to packages.yml, choosing the latest version compatible with my dbt version, and run dbt deps.',
           watch=['A new `packages.yml`', 'Terminal confirm for `dbt deps`', 'Then check the version on hub.getdbt.com'], habits=[1, 5],
           say=['Code mode: add `dbt_utils` with the latest version compatible with my dbt version, and run `dbt deps`.',
                'After it runs, I check the version on hub.getdbt.com myself. Version numbers are exactly the kind of thing an AI can get slightly wrong.'],
           do=['New chat, Code mode. Allow dbt deps.', 'Open hub.getdbt.com/dbt-labs/dbt_utils and compare the version.']),

    code('packages.yml', 'packages.yml', """packages:
  - package: dbt-labs/dbt_utils
    version: [">=1.3.0", "<2.0.0"]""", 'yaml', kicker='Result',
         aside=['A version **range**, not "latest"', '`dbt deps` installs into `dbt_packages/`', '`dbt clean` removes it again'],
         say=['Three lines. Note the version **range**: at least one-point-three, below two. That way we get fixes, but nothing that breaks us. Check the current version on the hub when you record.']),

    prompt('Explain what dbt_utils.generate_surrogate_key does, and which columns of stg_tlc__yellow_trips together could identify a trip. Don\'t write code.',
           mode='ask', watch=['A hash of several columns', 'Which columns, and why', 'It should mention duplicates are still possible'], habits=[2],
           say=['Before we use it, we understand it. Ask mode: what does `generate_surrogate_key` do, and which columns could identify a trip? No code.',
                'The answer: it hashes several columns into one ID. For a trip: vendor, pickup and dropoff time, pickup and dropoff zone. And if two rows are completely identical, they get the same key, which is how we will find duplicates.'],
           do=['Ask mode, paste the prompt.']),

    columns('Jinja in two minutes', [
        dict(title='{{ … }}', color='accent', sub='Expressions: print something', items=['`{{ ref(\'x\') }}`', '`{{ source(\'tlc\', \'yellow_trips\') }}`', '`{{ var(\'lookback_days\') }}`']),
        dict(title='{% … %}', color='violet', sub='Statements: logic', items=['`{% for p in list %}` … `{% endfor %}`', '`{% if is_incremental() %}`', '`{% macro name() %}`']),
        dict(title='{# … #}', color='dim', sub='Comments', items=['Removed when compiling', 'Never reach the database']),
    ], kicker='Jinja',
        say=['dbt models are SQL plus **Jinja**, a templating language. Three shapes to remember.',
             'Double curly braces print something: `ref` and `source` are Jinja expressions you already used. Curly-percent is logic: loops, ifs, and defining macros. Curly-hash is a comment.',
             'dbt renders the Jinja first, and the result is plain SQL. That is what the Compiled SQL tab shows.']),

    docs('Jinja and macros', 'docs/build/jinja-macros', [
        'Models can use **Jinja**: expressions `{{ }}`, statements `{% %}`, comments `{# #}`.',
        'Use loops and variables to avoid repeating SQL.',
        '**Macros** are reusable pieces of Jinja, defined in `.sql` files in `macros/`.',
        'Always check the **compiled** SQL to see what your Jinja produced.',
    ], say=['The Jinja and macros page. The idea: SQL is not very good at not repeating yourself. Jinja adds loops, variables and functions.',
            'A **macro** is a reusable function, defined in the macros folder. And the docs say it too: always look at the compiled SQL to see what you produced.'],
        do=['Open docs.getdbt.com/docs/build/jinja-macros?version=1.']),

    code('By hand: our first macro', 'macros/safe_divide.sql', """{% macro safe_divide(numerator, denominator) %}
    case
        when {{ denominator }} = 0 or {{ denominator }} is null then null
        else {{ numerator }} / {{ denominator }}
    end
{% endmacro %}""", 'sql', kicker='Hands on',
         aside=['Why: zero-distance trips', 'Fare per mile would divide by zero', 'Returns `null` instead of an error'],
         say=['Our own macro, written by hand. Remember the zero-distance trips from section one? Fare per mile would divide by zero.',
              '`safe_divide` takes two expressions and returns null when the denominator is zero or empty. Six lines, and every model can use it.'],
         do=['Create macros/safe_divide.sql and type it.']),

    columns('Before and after compiling', [
        dict(title='In a model', color='accent', code="{{ safe_divide('fare_amount',\n               'trip_distance_miles') }}\n    as fare_per_mile", lang='sql', size=25),
        dict(title='Compiled', color='good', code="case\n    when trip_distance_miles = 0\n      or trip_distance_miles is null then null\n    else fare_amount / trip_distance_miles\nend as fare_per_mile", lang='sql', size=24),
    ], kicker='Compiled SQL',
        say=['On the left, how we call it in a model. On the right, what dbt compiles it into: a plain case expression.',
             'The database never sees Jinja. It only sees the SQL on the right.']),

    docs('Analyses', 'docs/build/analyses', [
        '`.sql` files in `analyses/` can use `ref()`, `source()` and Jinja.',
        'dbt **compiles** them but never **runs** them: no table is built.',
        'Useful for one-off queries, audits and reports you want versioned.',
    ], say=['One more block from the projects page: **analyses**. An analysis is a SQL file in the `analyses` folder. It can use `ref` and Jinja like a model.',
            'But dbt only compiles it. It never builds a table. It is great for queries you want to keep in git, like an audit or a report, and to experiment with Jinja.'],
        do=['Open docs.getdbt.com/docs/build/analyses?version=1.']),

    code('By hand: a Jinja loop', 'analyses/payment_mix.sql', """select
    date_trunc('month', pickup_at) as month,
    {% for p in [1, 2] %}
    count(*) filter (where payment_type_id = {{ p }}) as trips_type_{{ p }},
    {% endfor %}
    count(*) as trips
from {{ ref('stg_tlc__yellow_trips') }}
group by 1
order by 1""", 'sql', kicker='Hands on',
         aside=['A loop writes one column per payment type', 'Compile it and read the result', 'The list is hard-coded… for now'],
         say=['An analysis with a loop. For each payment type in the list, write one count column. Two types, two columns.',
              'Compile it and open the compiled SQL: the loop is gone, replaced by two real columns. But the list is hard-coded, which is not great.'],
         do=['Create analyses/payment_mix.sql. Run dbt compile --select payment_mix, open the compiled file.']),

    prompt('Change analyses/payment_mix.sql so the list of payment types comes from the payment_types seed using dbt_utils.get_column_values instead of a hard-coded list. Compile it.',
           watch=['`dbt_utils.get_column_values(ref(\'payment_types\'), \'payment_type_id\')`', 'Compiled SQL now has one column per code', 'Add a code to the seed → a new column appears'], habits=[4, 5],
           say=['Let the agent make it data-driven. `get_column_values` from `dbt_utils` reads the list of payment type IDs from the seed at compile time.',
                'Compile again, and now there is one column for every payment type in the seed. Add a code to the CSV, and the SQL follows automatically.'],
           do=['New chat, Code mode, paste the prompt. Compare the compiled SQL with the hand-written version.']),

    recap('Section 07 done', [
        '`dbt_utils` installed with a version range, via `dbt deps`',
        'Jinja: `{{ }}` prints, `{% %}` decides and loops',
        'Our own `safe_divide` macro for zero-distance trips',
        'An analysis that compiles from a seed-driven loop',
    ], 's07-end', blocks=['sources', 'seeds', 'models', 'data tests', 'macros', 'analysis'], next='S08 · Intermediate, marts & materializations',
        say=['Recap. We installed `dbt_utils`, learned the three Jinja shapes, wrote a macro, and used an analysis to play with a data-driven loop.',
             'Two more blocks: **macros** and **analysis**. Tag `s07-end`. Next: we put it all together into intermediate and mart models.']),
])

# =====================================================================================================================
S08 = dict(num=8, file='s08-intermediate-marts', title='Intermediate, marts & materializations', short='Intermediate & marts', part=P1, minutes=15,
           blurb='Plan-then-act: the agent builds the business logic and the marts from an approved plan.', slides=[
    title('Intermediate, marts & materializations', 'Business logic in the middle, business-ready tables at the end, built by the agent from a plan we approve.',
          chips=['int_', 'fct_ · dim_ · agg_', 'view · table · ephemeral · incremental', 'Plan-then-act', 'dbt build'],
          say=['Section eight, the end of part one. We build the layers that turn clean data into answers: an intermediate model with our business rules, and the marts analysts use.',
               'This is the biggest agent task so far, so we use habit two: plan before act.']),

    columns('From clean data to answers', [
        dict(title='Staging', color='good', sub='done', items=['One-to-one with sources', 'Clean names and types']),
        dict(title='Intermediate', color='blue', sub='now', items=['Surrogate key, dedup', 'Duration, fare per mile', 'Valid-trip flag + reason', 'Join code names']),
        dict(title='Marts', color='accent2', sub='now', items=['`fct_trips`: valid trips', '`dim_zones`: zones', '`agg_zone_daily`: per zone per day']),
    ], kicker='Where we are',
        say=['Staging is done. In the **intermediate** layer we add the logic: a trip ID, removing exact duplicates, trip duration, fare per mile with our macro, and the valid-trip flag we promised in the tests section.',
             'Then the **marts**: a fact table of valid trips, a zone dimension, and a daily aggregate per pickup zone.']),

    docs('How we structure: Intermediate', 'best-practices/how-we-structure/3-intermediate', [
        'Intermediate models have a **specific purpose**: re-graining, isolating complex logic, simplifying joins.',
        'They are **not** exposed to end users.',
        'Usually materialized as **ephemeral** or **views**.',
    ], say=['The intermediate page. Intermediate models exist for a purpose: to isolate complex logic so the marts stay simple.',
            'They are not for end users. And they are usually views or ephemeral. Ours is a view, set by the folder.'],
        do=['Open the intermediate page (v1).']),

    docs('How we structure: Marts', 'best-practices/how-we-structure/4-marts', [
        'Marts are **business-defined entities**: each row is one thing the business cares about.',
        'Wide and denormalized: bring in the attributes people need.',
        'Materialized as **tables** (or incremental) for query speed.',
    ], say=['The marts page. A mart is an entity the business understands: here, a trip, a zone, a zone-day.',
            'They are wide, they bring in the attributes people need, and they are tables, so queries are fast. The guide names marts after entities; we use the classic `fct_` and `dim_` prefixes on top of that.'],
        do=['Open the marts page (v1).']),

    table('Materializations', ['Type', 'What dbt builds', 'Use it for'], [
        ['**view**', 'A view: runs the query every time', 'Staging, intermediate: cheap, always fresh'],
        ['**table**', 'A table: rebuilt on every run', 'Marts that people query a lot'],
        ['**incremental**', 'A table: only new rows added', 'Big facts: section 10'],
        ['**ephemeral**', 'Nothing: inlined as a CTE', 'Small helper logic'],
        ['**materialized view**', 'The database keeps it updated', 'Supported platforms only'],
    ], kicker='How models are built', size=28,
        say=['Materialization means: how does dbt build this model in the database?',
             'A **view** stores only the query. A **table** stores the result and is rebuilt each run. **Incremental** adds only new rows: section ten. **Ephemeral** builds nothing, it is inlined into the models that use it. And **materialized view** is a database feature on supported platforms.']),

    docs('Materializations', 'docs/build/materializations', [
        'Materializations are strategies for persisting models: **view**, **table**, **incremental**, **ephemeral**, **materialized view**.',
        'Set them in `dbt_project.yml`, in a YAML `config:`, or in the model with `{{ config(materialized=...) }}`.',
        'The most specific setting wins: the model file beats YAML, YAML beats `dbt_project.yml`.',
    ], say=['The materializations page. Five built-in types.',
            'You can set the materialization in three places: the project file, a YAML config, or a config block in the model. The most specific one wins. We use the project file per folder, and in section ten one model will override it.'],
        do=['Open docs.getdbt.com/docs/build/materializations?version=1.']),

    statement('Big task?<br><em>Plan</em> before you act.', kicker='Habit 2',
              sub='Ask for the plan, edit it, approve it. Only then let the agent write files.',
              say=['This task touches four models and several YAML files. If the agent starts writing immediately and gets the grain wrong, we review a lot of wrong code.',
                   'So first we ask for a plan: which models, at what grain, from which inputs, with what materialization. We fix the plan. Only then do we let it write.']),

    prompt('Before writing any files, propose the intermediate and mart models needed to answer: (1) trips and revenue per pickup zone per day, (2) a clean trip-level fact table. For each model give its grain, its inputs, and its materialization. Wait for my OK.',
           watch=['A plan, **no** files written', 'Grain stated for every model', 'You edit the plan in the chat'], habits=[2, 3],
           say=['The planning prompt. Two business questions: trips and revenue per zone per day, and a clean trip fact. For each model: grain, inputs, materialization. And: **wait for my OK**.',
                'Watch that it does not write any files yet.'],
           do=['New chat, Code mode, paste the prompt. Read the plan aloud. Correct anything that differs from the next slide.']),

    table('The plan we approve', ['Model', 'Grain', 'Inputs', 'Built as'], [
        ['`int_trips__enriched`', 'one row per trip', '`stg_tlc__yellow_trips`, `payment_types`, `rate_codes`', 'view'],
        ['`fct_trips`', 'one row per **valid** trip', '`int_trips__enriched`', 'table'],
        ['`dim_zones`', 'one row per zone', '`stg_tlc__taxi_zones`', 'table'],
        ['`agg_zone_daily`', 'one row per pickup zone per day', '`fct_trips`, `dim_zones`', 'table'],
    ], kicker='Approved plan', size=27,
        say=['This is the plan I want to approve. One intermediate model, one row per trip. A fact table with one row per **valid** trip. A zone dimension. And the daily aggregate, one row per pickup zone per day.',
             'If the agent proposed something different, I correct it in the chat now. It is much cheaper to fix a plan than to fix code.']),

    prompt('Go ahead. In int_trips__enriched, build trip_id with dbt_utils.generate_surrogate_key, remove exact duplicates, add trip_duration_minutes, fare_per_mile using the safe_divide macro, an is_valid_trip flag and an invalid_reason column, and join the payment type and rate code names. fct_trips keeps only valid trips. agg_zone_daily pivots trip counts by payment type with a Jinja loop over the payment_types seed. Add YAML with descriptions and primary-key tests for every model, then run dbt build --select +agg_zone_daily.',
           watch=['Many tool calls: let it work', 'Each file opens as a tab: read, then Keep', 'Terminal confirm for `dbt build`'], habits=[4, 5],
           say=['Approved, so: go ahead. I repeat the details that matter: the surrogate key, deduplication, duration, fare per mile with **our** macro, the validity flag with a reason, and the code names joined in.',
                'Then the marts, YAML with tests for every model, and one `dbt build` for everything up to the aggregate. This takes a while. Let it work.'],
           do=['Same chat. Paste. While it works, narrate the tool calls.', 'Open each file as it appears; Keep only after reading.']),

    code('Inside int_trips__enriched', 'models/intermediate/int_trips__enriched.sql (excerpt)', """trips as (
    select
        {{ dbt_utils.generate_surrogate_key(['vendor_id', 'pickup_at',
            'dropoff_at', 'pickup_location_id', 'dropoff_location_id',
            'total_amount']) }}                                as trip_id,
        *,
        date_diff('minute', pickup_at, dropoff_at)             as trip_duration_minutes,
        {{ safe_divide('fare_amount', 'trip_distance_miles') }} as fare_per_mile
    from {{ ref('stg_tlc__yellow_trips') }}
    qualify row_number() over (partition by trip_id order by source_file) = 1
),
flagged as (
    select *,
        case
            when dropoff_at < pickup_at   then 'ends_before_start'
            when trip_distance_miles <= 0 then 'zero_distance'
            when total_amount < 0         then 'negative_total'
            when not pickup_in_file_month then 'outside_file_month'
        end as invalid_reason
    from trips
)""", 'sql', kicker='Review before Keep',
         aside=['Package macro + **our** macro', '`qualify` keeps one row per trip ID', 'One reason per invalid trip', '`is_valid_trip = invalid_reason is null`'],
         aside_title='Check',
         say=['The heart of the project, in excerpt. The surrogate key from `dbt_utils`. Duration in minutes. Fare per mile with **our** `safe_divide`. And `qualify` with `row_number` keeps exactly one row per trip ID, which removes exact duplicates.',
              'Then the flag: a `case` that gives the **reason** a trip is invalid. Ends before it starts, zero distance, negative total, or a pickup outside the month of its file. The valid flag is simply "no reason".',
              'Your agent\'s version will differ in details. What matters is that you can read it and say yes, that is our rule.'],
         do=['Point at each check on the right in the agent\'s actual file.', '"pickup_in_file_month" is illustrative: the agent may derive it from source_file differently.']),

    dag('The full core of the project', 8, files=['int_trips__enriched', 'fct_trips', 'dim_zones', 'agg_zone_daily'],
        say=['Four new nodes. The intermediate model in the middle, fed by staging and the two code seeds. Then the fact table, the zone dimension, and the aggregate that uses both.'],
        do=['Open the lineage view in Rosetta, full screen.']),

    table('Selecting what to build', ['Selector', 'Means'], [
        ['`stg_tlc__yellow_trips`', 'just that model'],
        ['`+agg_zone_daily`', 'the model **and everything upstream**'],
        ['`stg_tlc__yellow_trips+`', 'the model **and everything downstream**'],
        ['`path:models/staging`', 'everything in a folder'],
        ['`source:tlc`', 'a source, for tests'],
        ['`test_type:unit`', 'only unit tests: section 09'],
    ], kicker='Node selection', size=29,
        say=['A quick word on selection, because we keep using it. A model name selects that model. A plus **before** the name adds everything upstream. A plus **after** adds everything downstream.',
             'You can select by folder with `path:`, by source, by test type. The node selection syntax page has the full list.'],
        do=['Optional: open reference/node-selection/syntax?version=1.']),

    steps('Verify', [
        ('Build everything up to the aggregate, tests included', 'dbt build --select +agg_zone_daily'),
        ('Open the full **lineage** view', None),
        ('**Run History**: compare view vs table timings', None),
        ('Preview `agg_zone_daily`: zones, days, counts per payment type', None),
    ], kicker='dbt is the judge',
        say=['`dbt build` with a plus: seeds, staging, intermediate, marts, and every test along the way, in the right order.',
             'In Run History you can compare timings: views are instant to build, tables take longer to build but are faster to query.',
             'And preview the aggregate: a row per zone per day, with one column per payment type, from the Jinja loop.'],
        do=['Run the build (or let the agent\'s build finish). Open Run History, then preview agg_zone_daily.']),

    realdata('Why trips are invalid', [
        ('?', '`ends_before_start`', 'inv_backwards'),
        ('?', '`zero_distance`', 'inv_zero'),
        ('?', '`negative_total`', 'inv_neg'),
        ('?', '`outside_file_month`', 'inv_outside'),
        ('?', 'exact duplicates removed', 'dupes'),
        ('?', 'valid trips in `fct_trips`', 'valid'),
    ], foot='Every promise from section 01 now has a rule, a reason and a number.',
        say=['Let\'s ask the data. In Ask mode: count invalid trips by reason. [Read the numbers.]',
             'And this closes the loop from section one: every problem we found now has a rule, a named reason, and a count. The fact table only contains the valid trips.'],
        do=['Ask mode: "Count invalid trips in int_trips__enriched by invalid_reason, plus the number of duplicates removed."', 'Before recording: type your numbers into the amber fields.']),

    recap('Part 1 done', [
        'Intermediate model with key, dedup, metrics and a validity flag',
        'Fact, dimension and aggregate marts, as tables',
        'Five materializations, and where to set them',
        'Plan-then-act on a multi-file task, reviewed file by file',
    ], 's08-end', blocks=['sources', 'seeds', 'models', 'data tests', 'macros', 'analysis'], next='S09 · Unit tests (Part 2)',
        say=['That is the end of part one. We have a complete, tested dbt project: from raw files to a fact table and a daily aggregate, with our business rules in one reviewed place.',
             'Tag `s08-end`. In part two we make it production-ready: unit tests, incremental models, snapshots and documentation.']),
])

DECKS = [S05, S06, S07, S08]
