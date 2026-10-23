from lib import (title, statement, bullets, flow, columns, code, docs, prompt, table, realdata, dag, blocks, recap,
                 habits, steps)

P1 = 'Part 1 · Core'

# =====================================================================================================================
S00 = dict(num=0, file='s00-welcome', title='Welcome & the agentic loop', short='Welcome', part=P1, minutes=6,
           blurb='What we build, how the screen works, and the six habits of working with an AI agent.', slides=[
    title('AI Agentic dbt Development',
          'Build one real dbt project with an AI agent, and stay the engineer in charge.',
          chips=['14 sections', '≈ 2.5 hours', 'dbt v1', 'Rosetta dbt Studio', 'Real NYC taxi data'],
          kicker='Crash course · Section 00',
          say=['Welcome to this crash course on AI agentic dbt development. My name is ___, and for the next couple of hours we are going to build **one real dbt project**, from an empty folder all the way to production patterns.',
               'We use Rosetta dbt Studio, a desktop dbt IDE with an AI agent built in, and real public data: New York City taxi trips. Millions of rows, and they are messy, which is exactly what we want.',
               'You don\'t need to know dbt already. You need basic SQL, and Rosetta dbt Studio installed. If you haven\'t installed it, the Beginners Course, lessons 3 and 4, covers that.'],
          do=['Slides window full screen, presenter window on your second screen.']),

    statement('You stay the engineer.<br>The agent does the *typing*.',
              sub='Agentic means the AI reads your project, writes files and runs commands. You decide, review and verify.',
              kicker='The idea',
              say=['Let me be clear about what "agentic" means in this course. The agent in Rosetta dbt Studio is not just a chatbot. It can read your project files, write new models, and run dbt commands.',
                   'That is powerful, and it is also why **you** stay in charge. The agent proposes. You read what it wrote, you decide, and dbt tells us whether it is actually right.',
                   'So this is a dbt course first. The agent makes us faster, but we will understand every line it writes.']),

    flow('The agentic loop', [
        dict(label='Prompt', sub='Say what you want, with context', tag='You'),
        dict(label='Plan', sub='Agent proposes the steps', tag='Agent'),
        dict(label='Act', sub='Writes files, asks to run commands', tag='Agent'),
        dict(label='Review', sub='You read every diff', tag='You', hl=True, color='accent2'),
        dict(label='Run', sub='dbt build / test', tag='dbt'),
        dict(label='Verify', sub='Look at the rows', tag='You'),
    ], kicker='How we work', caption='Every practical part of this course follows this loop. The highlighted step is the one people skip, and the one that matters most.',
        say=['Every time we use the agent, we go around this loop. We **prompt**, with enough context. For bigger tasks the agent **plans** first. Then it **acts**: it writes files and asks permission to run commands.',
             'Then comes the step that matters most: **review**. Rosetta opens every file the agent writes, and we click Keep or Discard. We read before we keep.',
             'Finally we **run** dbt and **verify** the actual rows. The agent saying "done" is not the finish line. dbt passing, and the data looking right, is.']),

    habits('Six habits for working with an agent', kicker='Rules of the road',
           say=['These are six habits we will repeat in every section. You will see them at the bottom of every prompt slide.',
                'One: **context over memory**. We give the agent files, like the official data dictionary, instead of trusting what it remembers. Two: **plan before act** for anything that touches several files. Three: **one task per chat**. A fresh chat per section keeps the context clean.',
                'Four: **read every diff** before you keep it. Five: **dbt is the judge**. We run and test. Six: if you correct the agent on the same thing twice, write it into the **skill**, so you never correct it a third time. We will build that skill in section 2.']),

    flow('The rhythm of every section', [
        dict(label='Slide', sub='The idea in one picture', tag='1-2 min'),
        dict(label='Docs', sub='The dbt v1 page, on screen', tag='2-4 min'),
        dict(label='Build', sub='First by hand, then with the agent', tag='5-10 min', hl=True),
        dict(label='Verify', sub='Run, test, look at rows', tag='1-2 min'),
        dict(label='Checkpoint', sub='A git tag you can return to', tag='end'),
    ], kicker='Course format',
        say=['Every section has the same rhythm. A few slides with the idea. Then we open the **official dbt documentation**, version 1, and read the important parts together.',
             'Then we build it in Rosetta dbt Studio. The **first time** we meet a concept, I write it **by hand**, so you see the real dbt code. The repetitive bulk goes to the agent.',
             'We verify, and we end with a **git tag**. If you get lost, you can check out that tag and continue from exactly where I am.']),

    dag('What you will build', 0, all_built=True, new=[], kicker='The finished project',
        say=['This is the finished project, as a lineage graph. On the left, **sources** and **seeds**: the raw taxi trips, the official zone lookup and two code lists.',
             'In the middle, **staging** models that clean things up, an **intermediate** model with our business logic, and on the right the **marts**: a fact table of trips, dimensions, and a daily aggregate.',
             'At the bottom, a **snapshot** that keeps history of a vendor list. And on the far right, an **exposure**: the real analysis we answer at the end of the course.'],
        do=['Point at each column of the graph as you name it.']),

    columns('The data: NYC taxi trips', [
        dict(title='Real & public', color='good', items=['Published monthly by the NYC Taxi & Limousine Commission', 'No sign-up, free to download', 'Parquet files, one per month']),
        dict(title='Big enough', color='accent', items=['About 3-4 million trips per month', 'We start with Nov + Dec 2024', 'DuckDB on a laptop handles it in seconds']),
        dict(title='Messy enough', color='accent2', items=['Nulls, negative fares, zero-mile trips', 'An official data dictionary', 'A new column appears in January 2025']),
    ], kicker='Why this dataset',
        say=['Why taxi data? Because it is **real**. The NYC Taxi and Limousine Commission publishes every yellow cab trip, month by month, as Parquet files.',
             'It is big enough to feel real, millions of rows per month, but DuckDB on a laptop handles it easily.',
             'And it is **messy**. That is the point. When we write tests, they will actually fail. And in January 2025 the data gets a brand-new column, so we will see a real schema change.']),

    bullets('The screen in Rosetta dbt Studio', [
        ('File tree, left', 'Your dbt project: models, seeds, tests, YAML.'),
        ('Editor, centre', 'SQL and YAML, with run buttons, Preview and Compiled SQL tabs.'),
        ('AI chat, right', 'The agent. It reads, writes and runs inside your real project.'),
        ('Keep / Discard', 'Every file the agent writes opens as a tab. You decide.'),
        ('Allow / Deny', 'Every terminal command the agent wants to run waits for you.'),
    ], kicker='Orientation',
        say=['Here is the layout we will use all course. On the left the file tree, your dbt project. In the middle the editor, with buttons to run a model, preview its rows and see its compiled SQL.',
             'On the right, the **AI chat**. The important part is that the agent works inside your real project. When it writes a file, the file opens as a tab and you get **Keep** or **Discard**.',
             'When it wants to run a terminal command, like `dbt build`, it stops and asks. You click **Allow** or **Deny**. Nothing runs behind your back.'],
        do=['Switch to Rosetta dbt Studio and point at each area.']),

    columns('Two modes in the AI chat', [
        dict(title='Ask mode', color='teal', sub='Read-only conversation', items=['Explain a model or a concept', 'Profile data, answer questions', 'Trace lineage, check grain', 'Safe: it does not change files']),
        dict(title='Code mode', color='violet', sub='The agent acts', items=['Writes and edits files', 'Asks to run dbt commands', 'Multi-step tasks with tool calls', 'You review with Keep / Discard']),
    ], kicker='AI chat', verdict='Rule of thumb: **ask** when you want to understand, **code** when you want something built.',
        say=['The chat has two modes. **Ask** mode is a read-only conversation. We use it to explain things, profile data and trace lineage. It does not change your files.',
             '**Code** mode is where the agent acts: it writes files and asks to run commands. Each prompt slide in this course tells you which mode I am using.']),

    docs('Introduction to dbt', 'docs/introduction', [
        'dbt transforms data that is **already loaded** in your warehouse: it is the "T" in ELT.',
        'You write **select statements**; dbt turns them into tables and views.',
        'dbt works out the **order** to build things from `ref()`, and adds **tests** and **documentation**.',
        'Throughout this course we read the **v1** docs, the version Rosetta dbt Studio runs.',
    ], say=['This is the official dbt documentation. Notice the version picker: the site now has v1 and v2. **Everything in this course is dbt v1**, the version Rosetta dbt Studio runs. Every link I open ends in `?version=1`.',
            'The core idea on this page: dbt does the **T** in ELT. It does not load data. It transforms data that is already in your database, using plain **select** statements.',
            'dbt figures out the build order from references between models, and it brings software practices to SQL: tests, documentation, version control.'],
        do=['Open docs.getdbt.com/docs/introduction?version=1.', 'Click the version picker and show v1 selected.']),

    table('The course map', ['#', 'Section', 'dbt block'], [
        ['00-02', 'Welcome · Load the data · Project anatomy', 'project, dbt_project.yml'],
        ['03', 'Sources', 'sources'],
        ['04', 'Seeds', 'seeds'],
        ['05', 'Staging models', 'models'],
        ['06', 'Data tests', 'data tests'],
        ['07', 'Packages, Jinja, macros & analyses', 'macros, analysis'],
        ['08', 'Intermediate, marts & materializations', 'models'],
        ['09-10', 'Unit tests · Incremental models', 'data tests, models, vars'],
        ['11-12', 'Snapshots · Docs, lineage & exposures', 'snapshots, docs, exposures'],
    ], kicker='Where we are going', size=27,
        say=['Here is the whole course. Part one, sections zero to eight, is the core: sources, seeds, staging models, tests, macros, and the final marts.',
             'Part two, sections nine to thirteen, is production patterns: unit tests, incremental models, snapshots, and documentation, ending with a real analysis.',
             'The right column shows the dbt **building block** each section covers. Those blocks come straight from the "About dbt projects" page in the docs, and we will tick them off as we go.']),

    steps('Let\'s start: create the project', [
        ('Projects screen → **New Project**, name it `nyc_taxi`', None),
        ('Connection: **DuckDB**, a new file `nyc_taxi.duckdb`', None),
        ('Show where AI provider, Skills and MCP settings live', None),
        ('Check the setup', 'dbt debug'),
    ], kicker='Hands on',
        say=['Let\'s create the project. On the projects screen, New Project, and I call it `nyc_taxi`. For the connection I choose **DuckDB**, with a new database file, `nyc_taxi.duckdb`. DuckDB is a database that lives in a single file on your machine, so there is nothing to install.',
             'Quickly, so you know where they are: this is where you pick the AI provider, this is the Skills library and this is the MCP servers panel. We use all of them later.',
             'Finally `dbt debug` from the Project menu. Green means dbt can see the project and connect to the database.'],
        do=['New Project → nyc_taxi → DuckDB → nyc_taxi.duckdb.', 'Point at Settings → AI provider, Skills, MCP.', 'Project menu → dbt debug. Wait for green.',
            'Say the versions on screen: app, dbt-core 1.x, dbt-duckdb, AI model.']),

    recap('Section 00 done', [
        'We know what we are building and why taxi data',
        'The agentic loop, with **Review** as the key step',
        'Six habits we will repeat in every section',
        'An empty `nyc_taxi` project that passes `dbt debug`',
    ], 's00-end', next='S01 · Load the real data: dbt is the "T"',
        say=['That\'s the setup. We know the plan, the loop and the habits, and we have an empty project that passes dbt debug.',
             'I tag this point as `s00-end`. Next, we load the real data, and you will see why dbt is only the T in ELT.'],
        do=['Commit and tag s00-end (optional on camera).']),
])

# =====================================================================================================================
S01 = dict(num=1, file='s01-load-real-data', title='Load the real data: dbt is the "T"', short='Load the real data', part=P1, minutes=10,
           blurb='ELT, load two months of taxi trips into DuckDB with the agent, and profile what is wrong with them.', slides=[
    title('Load the real data', 'dbt is the "T" in ELT. Before any model, we load the raw data and find out what is wrong with it.',
          chips=['ELT', 'DuckDB', 'SQL Editor AI', 'Approval gate', 'Profiling'],
          say=['Section one. Before we write a single dbt model, we need data in the database. And we need to understand it.',
               'We will load two months of real taxi trips into DuckDB, using the agent in the SQL editor, and then profile the data to find out what is wrong with it.']),

    statement('dbt doesn\'t load data.<br>It transforms data that\'s <em>already there</em>.', kicker='Key idea',
              sub='Extract and Load happen before dbt. Here, a small SQL script plays the role of the EL tool.',
              say=['This surprises many beginners: **dbt does not load data**. It does not download files or call APIs.',
                   'In a real company, a tool like Airbyte or Fivetran extracts and loads data into the warehouse. dbt starts after that.',
                   'In this course, a tiny SQL script plays the role of that loading tool. Keep this in mind: everything before the `raw` schema is not dbt.']),

    flow('ELT, in our project', [
        dict(label='Extract', sub='TLC publishes monthly Parquet files', tag='Outside dbt', color='dim'),
        dict(label='Load', sub='`read_parquet` into the `raw` schema in DuckDB', tag='Outside dbt', color='dim'),
        dict(label='Transform', sub='dbt models: staging → intermediate → marts', tag='dbt', hl=True),
    ], kicker='The pipeline', caption='`scripts/load_raw.sql` does E and L. Everything after the `raw` schema is dbt.',
        say=['Here is the pipeline. **Extract**: the Taxi Commission publishes Parquet files. **Load**: DuckDB reads those files into a schema we call `raw`.',
             'Then **Transform**: that is dbt, and that is the rest of this course.',
             'We keep the loading SQL in a file, `scripts/load_raw.sql`, outside of dbt, because when a new month arrives in section ten, we run it again.']),

    docs('Introduction: ELT', 'docs/introduction', [
        'Data is first **extracted** and **loaded** into the warehouse by other tools.',
        'dbt handles the **transformation**: modelling, cleaning, testing, documenting.',
        'Because dbt only writes `select` statements, it runs **inside** your data platform.',
    ], say=['Back to the docs introduction for one paragraph: dbt sits on top of data that is already loaded. It turns select statements into tables and views inside your database.',
            'So the database does the heavy work. For us, that database is DuckDB, running on my laptop.'],
        do=['Scroll the introduction page to the ELT / "what is dbt" paragraph.']),

    table('The dataset', ['', ''], [
        ['Publisher', 'NYC Taxi & Limousine Commission (TLC)'],
        ['Format', 'Parquet, one file per month'],
        ['We load', '**Nov 2024** + **Dec 2024** now, **Jan 2025** in section 10'],
        ['Size', 'About 3-4 million trips per month'],
        ['Lookup', '`taxi_zone_lookup.csv`, 265 taxi zones'],
        ['Documentation', 'Data dictionary for yellow taxi trips (March 2025)'],
        ['Attribution', 'Data: NYC Taxi & Limousine Commission, TLC Trip Record Data'],
    ], kicker='Dataset card', size=30,
        say=['The dataset card. The publisher is the NYC Taxi and Limousine Commission. Files are Parquet, one per month, and each month is around three to four million trips.',
             'We start with November and December 2024. January 2025 comes later, on purpose.',
             'Two more things from the same site: a zone lookup CSV with 265 taxi zones, and a **data dictionary** that explains every column. That dictionary becomes very important.']),

    columns('What is in a trip record', [
        dict(title='When & where', color='accent', items=['`VendorID`', '`tpep_pickup_datetime`', '`tpep_dropoff_datetime`', '`PULocationID` · `DOLocationID`', '`trip_distance` · `passenger_count`']),
        dict(title='Codes', color='teal', items=['`RatecodeID` (1-6, 99)', '`payment_type` (0-6)', '`store_and_fwd_flag` (Y/N)']),
        dict(title='Money', color='accent2', items=['`fare_amount` · `extra` · `mta_tax`', '`tip_amount` · `tolls_amount`', '`improvement_surcharge` · `total_amount`', '`congestion_surcharge` · `airport_fee`', '`cbd_congestion_fee` (from 2025)']),
    ], kicker='Columns, from the data dictionary',
        say=['Each row is one taxi trip. We have **when and where**: pickup and dropoff time, pickup and dropoff zone, distance and passengers.',
             'Then **codes**: rate code, payment type, and a store-and-forward flag. Those codes only make sense with the dictionary. Payment type 1 is credit card, 2 is cash, and so on.',
             'And **money**: the fare, extras, taxes, tips, tolls, surcharges, and the total. Notice the last one: `cbd_congestion_fee`. It only exists from January 2025. Remember that.']),

    bullets('The source system\'s docs are docs too', [
        ('We transcribe the PDF dictionary to Markdown', '`reference/tlc_yellow_data_dictionary.md`, with every code list.'),
        ('The agent reads this file all course long', 'Descriptions, accepted values, seeds: all from the file, not from memory.'),
        ('Why it matters', 'Code lists change. An AI that "remembers" an old list will be confidently wrong.'),
    ], kicker='Habit 1 · Context over memory',
        say=['Here is our first habit in action. I took the official PDF data dictionary and wrote it as a Markdown file in the project: `reference/tlc_yellow_data_dictionary.md`.',
             'From now on, whenever the agent needs a description or a list of codes, it reads this file. Not its memory.',
             'Why? Because code lists change over time. You will see it in section 4: the payment types list today is not the one an AI model may remember.'],
        do=['Open reference/tlc_yellow_data_dictionary.md in the editor and scroll through it.']),

    prompt('In the DuckDB connection, create a schema called raw. Load data/yellow_tripdata_2024-11.parquet and data/yellow_tripdata_2024-12.parquet into a table raw.yellow_trips using read_parquet with union_by_name and filename = true, so every row keeps the file it came from. Show me the SQL before you run it.',
           where='SQL Editor · AI panel', mode='sql',
           watch=['It shows the SQL first', 'The **approval gate** for DDL: read it aloud, then Allow', '`union_by_name` matters later, when a new column arrives'],
           habits=[1, 4],
           say=['Now the agent. I am in the SQL editor, with the AI panel in Code mode. I ask it to create a `raw` schema and load the two Parquet files into one table, `raw.yellow_trips`.',
                'Two details in the prompt. `filename = true` keeps the name of the source file on every row, which helps us later. `union_by_name` lets files with different columns be combined. We need that when January arrives.',
                'And I ask it to **show me the SQL first**. Watch: because this creates tables, Rosetta stops at an approval gate. I read the SQL, and only then I allow it.'],
           do=['Paste the prompt into the SQL Editor AI panel (Code mode).', 'When the approval gate appears: read the SQL out loud, then click Allow.', 'Save the SQL as scripts/load_raw.sql.']),

    code('What the load looks like', 'scripts/load_raw.sql', """-- EL step. Not part of dbt. Re-run when a new month arrives.
create schema if not exists raw;

create or replace table raw.yellow_trips as
select *
from read_parquet(
    [
        '/ABSOLUTE/PATH/nyc_taxi/data/yellow_tripdata_2024-11.parquet',
        '/ABSOLUTE/PATH/nyc_taxi/data/yellow_tripdata_2024-12.parquet'
    ],
    union_by_name = true,   -- files can have different columns
    filename = true         -- adds a "filename" column
);""", 'sql', kicker='scripts/load_raw.sql', aside=['Absolute paths: relative ones resolve against the app, not the project', 'Viewers can use the TLC URLs directly instead of local files', 'We run this again in section 10'],
         aside_title='Notes',
         say=['This is roughly what the agent writes, and what I save as `scripts/load_raw.sql`. One `create table as select` from `read_parquet`, with a list of files.',
              'Use absolute paths here. And if you are following along, you can put the TLC download URLs straight into that list. DuckDB reads Parquet over HTTPS.',
              'This file is our "loader". When a new month arrives, we add a line and run it again.']),

    prompt('Profile raw.yellow_trips: rows per source file, the pickup date range, null count per column, and how many rows have fare_amount < 0, trip_distance = 0, or dropoff before pickup. One query per question, and show the numbers in a table.',
           where='SQL Editor · AI panel', mode='ask',
           watch=['It writes and runs read-only queries', 'Numbers come back as a table', 'Write the surprises down: next slide'],
           habits=[5],
           say=['Before modelling anything, we look at the data. I switch to **Ask** mode, so the agent only reads, and ask it to profile the table.',
                'Rows per file, the date range, nulls per column, and three suspicious things: negative fares, zero-distance trips, and trips that end before they start.',
                'This is habit five: dbt, and the data, are the judge. We find out what is true before we write rules about it.'],
           do=['Switch the AI panel to Ask mode and paste the prompt.', 'Let it run; read the result table aloud.']),

    realdata('What we found', [
        ('?', 'trips with a pickup **outside** the file\'s month', 'outside_month'),
        ('?', 'trips with a **negative** fare', 'neg_fare'),
        ('?', 'trips with **zero** distance', 'zero_dist'),
        ('?', 'rows with **null** passenger count', 'null_pax'),
        ('?', 'trips that **end before they start**', 'backwards'),
        ('≈ 7M', 'rows loaded from two monthly files', 'rows'),
    ], foot='**We will come back to every one of these.**',
        say=['And here is what real data looks like. Let me read the numbers. [Read each card.]',
             'Trips with a pickup date outside the month of the file. Negative fares. Trips with zero miles. A whole block of rows where passenger count is empty. And trips that end before they start.',
             'None of this is a bug in our code. This is the source system. **We will come back to every one of these** in the course: with tests, with flags, with unit tests.'],
        do=['Before recording: click each amber "?" and type the numbers from your dry-run profile, then press Esc.']),

    table('Where each problem gets handled', ['Problem', 'Handled in'], [
        ['Guessed `not_null` tests on columns that are often empty', 'S03 · Sources'],
        ['Code values that changed (payment type 0, rate code 99)', 'S04 · Seeds'],
        ['Trips that end before they start', 'S06 · Data tests'],
        ['Zero-distance trips (division by zero), invalid trips', 'S07 macro · S08 `is_valid_trip`'],
        ['Edge cases locked down', 'S09 · Unit tests'],
        ['A new column in January 2025', 'S10 · Incremental models'],
    ], kicker='The plan for the mess', size=28,
        say=['Here is the promise, written down. Each of those problems has a home in the course.',
             'Guessed tests that fail, in section 3. Code lists that changed, in section 4. Backwards trips, in the tests section. Zero-mile trips get a safe division macro and an `is_valid_trip` flag. And the new January column is the star of section 10.']),

    recap('Section 01 done', [
        'dbt is the **T**: loading happens before dbt',
        '`raw.yellow_trips` loaded with two months of real trips',
        'The data dictionary is in the project, for the agent to read',
        'We profiled the data and wrote down what is wrong with it',
    ], 's01-end', next='S02 · Project anatomy & teaching the agent',
        say=['Recap. dbt is the T. We loaded two months of real trips into a `raw` schema with the agent, behind an approval gate. We put the data dictionary in the project. And we know what is wrong with the data.',
             'Tag `s01-end`. Next: what a dbt project is made of, and how we teach the agent our rules.']),
])

# =====================================================================================================================
S02 = dict(num=2, file='s02-project-anatomy', title='Project anatomy & teaching the agent', short='Project anatomy', part=P1, minutes=10,
           blurb='The building blocks of a dbt project, dbt_project.yml, the three layers, and a skill that teaches the agent our rules.', slides=[
    title('Project anatomy & teaching the agent', 'What a dbt project is made of, how it is configured, and how we teach the agent our conventions.',
          chips=['About dbt projects', 'dbt_project.yml', 'Staging · Intermediate · Marts', 'Skills', 'MCP'],
          say=['Section two. We look inside a dbt project: the building blocks, the one configuration file every project has, and the folder structure we will follow.',
               'Then we teach the agent those rules with a skill, so every model it writes from now on follows them.']),

    bullets('What is inside a dbt project', [
        ('`dbt_project.yml`', 'The one required file. Name, profile, paths, configs.'),
        ('`models/`', 'SQL select statements, plus YAML that describes them.'),
        ('`seeds/` · `snapshots/` · `tests/`', 'CSV lookups, history tables, singular tests.'),
        ('`macros/` · `analyses/`', 'Reusable Jinja, and SQL that compiles but never builds.'),
        ('A connection profile', 'Where to build: here, our DuckDB file.'),
    ], kicker='Anatomy', cols=1,
        say=['A dbt project is just a folder. The only file it **must** have is `dbt_project.yml`.',
             'Models live in `models/`: SQL files with one select each, plus YAML files that describe and test them. Seeds, snapshots and singular tests have their own folders, and so do macros and analyses.',
             'And a connection profile tells dbt **where** to build. Rosetta set that up for us when we picked DuckDB.'],
        do=['Expand the project folders in the file tree as you name them.']),

    docs('About dbt projects', 'docs/build/projects', [
        'A project is a directory with a `dbt_project.yml` file.',
        'The **resources table** lists every building block: models, sources, seeds, data tests, macros, docs, snapshots, exposures, analysis...',
        'The **project configuration table** lists the keys in `dbt_project.yml`: `name`, `version`, `require-dbt-version`, `profile`, the `*-paths`, `vars`.',
    ], quote='This page is the table of contents for the whole course.',
        say=['This page is the map of the course. "About dbt projects", version one.',
             'It has two tables. The **resources** table lists every building block a project can have. And the **project configuration** table lists the keys we set in `dbt_project.yml`.',
             'Every section in this course builds one or more of these blocks. Let me show you how they map.'],
        do=['Open docs.getdbt.com/docs/build/projects?version=1 and scroll to both tables.']),

    blocks('The blocks, and where we build them', upto=-1, kicker='Blocks map',
           foot='Dashed blocks (Semantic Layer, groups, UDFs) are beyond this crash course: candidates for a Part 3.',
           say=['Here is every block from that page, with the section that builds it. Models get three sections, because staging, marts and incremental are different jobs.',
                'Sources, seeds, tests, macros and analyses, snapshots, docs and exposures each get their own section.',
                'The dashed ones, metrics, semantic models, saved queries, groups and user-defined functions, are beyond a crash course. You will see this map again at the end, fully ticked.']),

    table('Project configuration, the keys we set', ['Key', 'What it does', 'Our value'], [
        ['`name`', 'Project name, snake case', '`nyc_taxi`'],
        ['`version`', 'Version of *your* project', '`1.0.0`'],
        ['`require-dbt-version`', 'Restrict to a range of dbt v1 versions', '`[">=1.10.0", "<2.0.0"]`'],
        ['`profile`', 'Which connection to use', 'the DuckDB profile'],
        ['`*-paths`', 'Where each block lives', 'defaults: `models`, `seeds`, `tests`...'],
        ['`vars`', 'Project variables', 'added in S10'],
    ], kicker='dbt_project.yml', size=28,
        say=['The configuration table, applied to our project. `name` is `nyc_taxi`. `version` is our project\'s own version.',
             '`require-dbt-version` is useful: we restrict the project to dbt version one, so it refuses to run on a version it was not written for.',
             '`profile` points to the connection. The paths say where each block lives, and we keep the defaults. `vars` we add later, in section ten.']),

    code('Our dbt_project.yml', 'dbt_project.yml', """name: nyc_taxi
version: '1.0.0'
profile: nyc_taxi
require-dbt-version: [">=1.10.0", "<2.0.0"]

model-paths: ["models"]
seed-paths: ["seeds"]
test-paths: ["tests"]
analysis-paths: ["analyses"]
macro-paths: ["macros"]
snapshot-paths: ["snapshots"]

models:
  nyc_taxi:
    staging:
      +materialized: view
    intermediate:
      +materialized: view
    marts:
      +materialized: table""", 'yaml', kicker='By hand', aside=['The `+` marks a **config**, not a folder name', '`models → nyc_taxi → staging` scopes it to one folder', 'No model file needs to say "view": the folder decides'],
         aside_title='Read it',
         say=['I write this one by hand. The top is the configuration table we just read.',
              'The bottom is the interesting part: **folder-level configs**. Under `models`, then our project name, then a folder, I set how models in that folder are built. Staging and intermediate become views, marts become tables.',
              'The plus sign tells dbt "this is a setting, not a sub-folder". From now on, no staging model needs to say it is a view. The folder decides.'],
         do=['Edit dbt_project.yml on camera.', 'Create the folders models/staging, models/intermediate, models/marts.']),

    columns('Three layers', [
        dict(title='Staging', color='good', sub='Source-conformed', items=['One model per source table', 'Rename, cast, light cleanup', '`stg_tlc__yellow_trips`', 'View']),
        dict(title='Intermediate', color='blue', sub='Purpose-built', items=['Joins and business logic', 'Not for end users', '`int_trips__enriched`', 'View']),
        dict(title='Marts', color='accent2', sub='Business-conformed', items=['Facts, dimensions, aggregates', 'What analysts query', '`fct_trips` · `dim_zones` · `agg_zone_daily`', 'Table']),
    ], kicker='How we structure the project',
        say=['dbt Labs recommends three layers. **Staging** is shaped like the source: one model per source table, renamed and typed, nothing else.',
             '**Intermediate** is where business logic lives: joins, calculations, flags. End users never query it directly.',
             '**Marts** are shaped like the business: a fact table of trips, dimensions like zones, and aggregates. That is what analysts use.']),

    docs('How we structure our dbt projects', 'best-practices/how-we-structure/1-guide-overview', [
        'Move data from **source-conformed** to **business-conformed**.',
        'Three layers: **staging**, **intermediate**, **marts**, each building on the one before.',
        'The goal is **consistency**: less time deciding where files go and what to call them.',
    ], say=['This is the guide those layers come from. The key phrase: we move data from **source-conformed**, shaped by the systems that produced it, to **business-conformed**, shaped by how the business thinks.',
            'And the goal is consistency. If every model follows the same rules, nobody wastes time deciding names and folders. That is exactly what we want the agent to follow too.'],
        do=['Open the How we structure overview (v1) and scroll the folder tree.']),

    flow('Docs → Skill → Agent', [
        dict(label='Docs', sub='We read the rules together', tag='1'),
        dict(label='Skill', sub='We write them into a SKILL.md', tag='2', hl=True),
        dict(label='Agent', sub='Loads the skill and follows it', tag='3'),
    ], kicker='Teaching the agent', caption='A skill is a Markdown file of instructions. Rosetta\'s agent loads it when a task matches its description.',
        say=['How does the agent learn these rules? With a **skill**. A skill is a Markdown file with instructions, plus a short description of when to use it.',
             'What we read in the docs, we write into the skill. The agent loads the skill whenever the task matches, so it follows our conventions without us repeating them in every prompt.',
             'And remember habit six: when you correct the agent twice on the same thing, it goes into this file.']),

    code('Our skill', 'nyc-taxi-dbt-conventions/SKILL.md', """---
name: nyc-taxi-dbt-conventions
description: Conventions for the NYC taxi dbt project (dbt v1). Use whenever you create or edit models, YAML, seeds, tests or snapshots.
---
# NYC taxi dbt conventions

## dbt version
- dbt v1 (dbt-core 1.x). Follow the v1 docs; ignore "v2 only".
- Tests use the data_tests: key. Snapshots are YAML files.

## Layers
- staging: stg_<source>__<entity>s. Rename, cast. No joins, no filters.
- intermediate: int_<entity>__<verb>. Business logic lives here.
- marts: fct_, dim_, agg_. Materialization comes from dbt_project.yml.

## Columns
- snake_case. Timestamps end in _at, booleans start with is_.
- Money is decimal(10,2). Keep source_file through to fct_trips.

## YAML
- Every model and column has a description. Primary keys: unique + not_null.
- Code values come from reference/tlc_yellow_data_dictionary.md, never from memory.""", 'md', kicker='Skills Library',
         say=['Here is the skill, shortened. At the top, the name and the description: that description is how the agent knows when to load it.',
              'Then our rules: dbt version one. The naming for each layer. Column conventions: timestamps end in `_at`, booleans start with `is_`, money is a decimal.',
              'And the most important line: code values come from the dictionary file, **never from memory**.'],
         do=['Settings → Skills Library → New skill. Paste the full SKILL.md from the course plan (Appendix B).', 'Optional: ask the agent in Ask mode to draft it, then edit by hand.']),

    bullets('Skills and MCP servers', [
        ('Skills are app-wide', 'They live in the app\'s skills folder, so they are available in every project.'),
        ('MCP servers give the agent outside knowledge', 'Built in: Rosetta CLI, dbt Core, DuckDB and DuckLake documentation.'),
        ('Add your own with a URL', 'Optional: `gitmcp.io/dbt-labs/docs.getdbt.com`, so the agent reads the same docs we read.'),
    ], kicker='Agent setup',
        say=['Two things to know. Skills are **app-wide**: once saved, every project can use them. That is why the description says "NYC taxi project".',
             'MCP servers give the agent extra knowledge sources. Rosetta ships with servers for the Rosetta CLI, dbt Core, DuckDB and DuckLake.',
             'You can add your own with one URL. I add one for the dbt documentation site, so the agent can read the same pages we read.'],
        do=['Open the MCP servers panel. Show the built-in servers.', 'Optional: add https://gitmcp.io/dbt-labs/docs.getdbt.com.']),

    prompt('Using the dbt v1 docs, what is the difference between a source and a seed? Three bullets, and name the page you used.',
           mode='ask', watch=['It calls an MCP tool to read the docs', 'It names the page', 'Short answer: three bullets'], habits=[1],
           say=['Let\'s test the setup in Ask mode. "Using the dbt v1 docs, what is the difference between a source and a seed?"',
                'Watch the tool calls: it should look the answer up, not answer from memory, and tell us which page it used. Good preview of the next two sections, too.'],
           do=['New chat, Ask mode, paste the prompt.', 'Point at the MCP tool call in the chat.']),

    recap('Section 02 done', [
        'The building blocks of a dbt project, from the v1 docs',
        '`dbt_project.yml` with a v1 version range and folder materializations',
        'Three layers: staging, intermediate, marts',
        'A skill that teaches the agent our conventions, and MCP docs access',
    ], 's02-end', next='S03 · Sources',
        say=['Recap. We know the building blocks, we configured `dbt_project.yml`, we know the three layers, and the agent has a skill with our rules.',
             'Tag `s02-end`. Next: our first block, **sources**.']),
])

# =====================================================================================================================
S03 = dict(num=3, file='s03-sources', title='Sources', short='Sources', part=P1, minutes=10,
           blurb='Declare the raw table as a source, document it from the dictionary, and watch guessed tests fail on real data.', slides=[
    title('Sources', 'Give the raw data a name, a description and tests, so dbt knows where everything starts.',
          chips=['sources:', 'source()', 'Rosetta Raw Layer', 'data_tests', 'freshness'],
          say=['Section three: **sources**. This is how we tell dbt about data that already exists in the database, data that dbt did not build.']),

    statement('Never hard-code<br>a table name.', kicker='Key idea',
              sub='`from raw.yellow_trips` works, but dbt can\'t see it: no lineage, no tests, no docs.',
              say=['One rule: never hard-code a table name in a model. Writing `from raw.yellow_trips` works, but dbt cannot see that dependency.',
                   'It cannot draw it in the lineage, it cannot test it, and if the schema name changes, every model breaks. Sources fix all of that.']),

    columns('Hard-coded vs source()', [
        dict(title='Hard-coded', color='bad', code="select *\nfrom raw.yellow_trips", lang='sql', size=30, foot='dbt sees plain text. No lineage, no tests.'),
        dict(title='With source()', color='good', code="select *\nfrom {{ source('tlc', 'yellow_trips') }}", lang='sql', size=30,
             foot='Compiles to the real table, **and** appears in the DAG.'),
    ], kicker='The difference',
        say=['Side by side. On the left, a hard-coded table. On the right, the `source` function with two arguments: the source name, `tlc`, and the table name, `yellow_trips`.',
             'When dbt compiles the right one, it becomes the same full table name. But now dbt knows the model depends on that source. It shows up in the lineage graph, and we can attach tests and descriptions to it.']),

    docs('Sources', 'docs/build/sources', [
        'Declare sources in a `.yml` file under a `sources:` key, with a `name`, optional `schema`, and `tables`.',
        'Select from them with `{{ source(\'source_name\', \'table_name\') }}`: dbt compiles it and adds the dependency to the DAG.',
        'Add descriptions and `data_tests` to source columns; run them with `dbt test --select "source:*"`.',
        'Freshness: configured under `config:`, checked with `dbt source freshness`.',
    ], say=['The Sources page, version one. A source is declared in YAML, under a `sources` key: a name, the schema if it is different from the name, and the list of tables.',
            'In a model we select from it with the `source` function. And just like models, sources can have descriptions and tests.',
            'There is also **freshness**: dbt can warn you when a source has not received new data for too long. In v1 that is `dbt source freshness`. We will not run it, and I will tell you why at the end.'],
        do=['Open docs.getdbt.com/docs/build/sources?version=1.', 'Show the YAML example and the "testing sources" part.']),

    dag('Our first block in the DAG', 3, files=['models/staging/tlc/_tlc__sources.yml'],
        say=['On our lineage graph, the very first node lights up: the source `tlc.yellow_trips`. Everything else in the project will be built on top of it.']),

    bullets('Rosetta Raw Layer', [
        ('Project → Raw Layer', 'Reads the DuckDB database and writes a source YAML. No AI involved.'),
        ('One YAML file per table, every column listed', 'A fast, deterministic start. We have one table, so one file.'),
        ('A `not_null` test on every column', 'That is a **guess**. Real data will tell us if it is right.'),
    ], kicker='Generate, then improve',
        say=['We don\'t have to type the source YAML by hand. Rosetta has a generator: Project menu, **Raw Layer**. It reads the database and writes a YAML file with every table and every column. No AI here, it is deterministic.',
             'It also adds a `not_null` test to every column. That is a guess, and with real data, guesses get tested. Keep that in mind.'],
        do=['Project menu → Raw Layer. Choose an output folder. Open the generated YAML.']),

    prompt('Move the generated source YAML to models/staging/tlc/_tlc__sources.yml. Name the source tlc and keep the table name yellow_trips. Add a description to every column from reference/tlc_yellow_data_dictionary.md, including the full code lists for VendorID, RatecodeID and payment_type. Use the data_tests: key. Don\'t change which tests exist yet.',
           watch=['It reads the dictionary file, not memory', 'The file opens as a tab: read it, then Keep', '`data_tests:` key (v1)'], habits=[1, 4],
           say=['Now the agent improves that file. Code mode. I ask it to move the YAML into our staging folder, name the source `tlc`, and add a description to every column, **from the dictionary file**.',
                'I also say: don\'t change the tests yet. We want to see what happens with the generated guesses first.',
                'Watch the tool calls: it reads the dictionary, it writes the file, and the file opens as a tab for review.'],
           do=['New chat, Code mode, paste the prompt.', 'When the file opens: spot-check two descriptions against the PDF, then Keep.']),

    code('The source YAML, after the agent', 'models/staging/tlc/_tlc__sources.yml', """sources:
  - name: tlc
    schema: raw
    description: NYC TLC yellow taxi trip records, loaded by scripts/load_raw.sql.
    tables:
      - name: yellow_trips
        columns:
          - name: tpep_pickup_datetime
            description: Date and time when the meter was engaged.
            data_tests:
              - not_null
          - name: passenger_count
            description: Number of passengers in the vehicle.
            data_tests:
              - not_null      # guessed by the generator
          - name: payment_type
            description: >
              How the passenger paid. 0 = Flex Fare, 1 = Credit card,
              2 = Cash, 3 = No charge, 4 = Dispute, 5 = Unknown, 6 = Voided trip.""", 'yaml', kicker='Review',
         aside=['Source `tlc`, schema `raw`', 'Descriptions match the dictionary', 'Payment type list includes **0 = Flex Fare**', 'Tests still the generated guesses'],
         aside_title='Check before Keep',
         say=['This is the part to review. The source is called `tlc`, but the schema is `raw`, because the names differ.',
              'Descriptions come from the dictionary. Look at payment type: the list starts at **zero, Flex Fare**. That is from the current dictionary.',
              'And the tests are still the generated `not_null` guesses. Let\'s run them.']),

    steps('Test the source', [
        ('Run every test on the `tlc` source', 'dbt test --select source:tlc'),
        ('Several `not_null` tests **fail**', None),
        ('Ask: which rows fail, and what do they have in common?', None),
    ], kicker='Verify',
        say=['`dbt test --select source:tlc`. This runs every test attached to our source.',
             'And several fail. `passenger_count`, `RatecodeID`, the store-and-forward flag, some surcharges. That is real data pushing back on a guess.'],
        do=['Run dbt test --select source:tlc in the terminal or ask the agent to run it.', 'Show the failing tests in Run History.']),

    prompt('Which rows fail the not_null test on passenger_count? What do they have in common?',
           mode='ask', watch=['It queries the failing rows', 'It looks for a pattern across columns'], habits=[5],
           say=['Instead of just deleting the tests, we ask why. Ask mode: which rows fail, and what do they have in common?'],
           do=['Ask mode, paste the prompt. Read the answer aloud.']),

    realdata('The empty rows have something in common', [
        ('?', 'rows with null `passenger_count`', 'null_pax'),
        ('?', 'of those rows have `payment_type = 0`', 'flex_share'),
        ('0', '= **Flex Fare** in the current data dictionary', None),
    ], foot='Not broken data: **a different kind of trip**, where some fields are not recorded.',
        say=['Here is the answer from my dry run. [Read the numbers.] The rows with empty passenger count are the rows with payment type zero, which the dictionary calls **Flex Fare**.',
             'So these are not broken rows. They are a different kind of trip, where some fields are simply not recorded. That changes what the right test is.'],
        do=['Before recording: type your dry-run numbers into the amber fields. If the pattern does not hold, say "these rows are incomplete" and skip the Flex Fare point.']),

    columns('The decision', [
        dict(title='Keep not_null on', color='good', mark='good', items=['pickup and dropoff time', 'pickup and dropoff location', 'total_amount']),
        dict(title='Drop not_null on', color='bad', mark='bad', items=['`passenger_count`', '`RatecodeID`', '`store_and_fwd_flag`', '`congestion_surcharge` · `airport_fee`']),
    ], kicker='You decide', verdict='A failing test is a **decision**, not a bug. We keep tests that describe reality.',
        say=['So we decide. We keep `not_null` where a trip really can\'t exist without the value: times, locations, the total.',
             'We drop it on the columns the source legitimately leaves empty. A test should describe reality, not our hopes. This is a human decision; the agent can make the edit.'],
        do=['Edit the YAML by hand, or ask the agent to remove those five not_null tests. Re-run dbt test --select source:tlc until green.']),

    bullets('Why we skip freshness', [
        ('Freshness compares a timestamp to **now**', '`loaded_at_field` + `warn_after` / `error_after`, under `config:`.'),
        ('Our data is historical', 'Months old by design, so it would always be "stale".'),
        ('In production, turn it on', '`dbt source freshness` tells you when a loader stopped working.'),
    ], kicker='Freshness',
        say=['One last thing: freshness. dbt compares a timestamp column with the current time and warns you if the data is too old.',
             'Our data is historical, months old on purpose, so it would always fail. In a real project, with data arriving daily, you turn it on. It is how you find out a loader stopped working.']),

    recap('Section 03 done', [
        '`raw.yellow_trips` is now `source(\'tlc\', \'yellow_trips\')`',
        'Every column documented from the data dictionary',
        'Generated `not_null` guesses tested against real data',
        'We kept the tests that describe reality',
    ], 's03-end', blocks=['sources'], next='S04 · Seeds',
        say=['Recap. Our raw table is a source, documented from the dictionary, and its tests now describe reality instead of a guess.',
             'First block ticked: **sources**. Tag `s03-end`. Next, **seeds**.']),
])

# =====================================================================================================================
S04 = dict(num=4, file='s04-seeds', title='Seeds', short='Seeds', part=P1, minutes=8,
           blurb='Small, static lookup data as version-controlled CSVs, and why the agent must read codes from the dictionary.', slides=[
    title('Seeds', 'Small, static lookup data, kept as CSV files in the project and loaded by dbt.',
          chips=['seeds/', 'dbt seed', 'column_types', 'Context over memory'],
          say=['Section four: **seeds**. Some data is not in any source system. It is a small list we maintain ourselves: codes and their names. That is what seeds are for.']),

    docs('Seeds', 'docs/build/seeds', [
        'Seeds are **CSV files** in your project that dbt loads into the database with `dbt seed`.',
        'Because they live in the project, they are **version controlled** and code reviewed.',
        'Best for **static data that changes infrequently**: code mappings, small lists.',
        'Set types with `column_types` in a properties YAML file.',
    ], say=['The Seeds page. A seed is a CSV file in the project. `dbt seed` loads it into the database as a table.',
            'Because it is a file in the project, it is in git, it gets reviewed, it has history. The docs say seeds are best for static data that changes infrequently, like mappings of codes to names.'],
        do=['Open docs.getdbt.com/docs/build/seeds?version=1.']),

    columns('Good seeds, bad seeds', [
        dict(title='Good', color='good', mark='good', items=['Code → name mappings', 'A list of zones or regions', 'Test emails to exclude', 'Small, static, reviewed']),
        dict(title='Bad', color='bad', mark='bad', items=['Raw data exported to CSV', 'Anything large', 'Sensitive production data', 'Data that changes every day']),
    ], kicker='When to use a seed',
        say=['Good seeds: code-to-name mappings, small reference lists, lists of test accounts to exclude.',
             'Bad seeds: raw data dumped to CSV, anything big, anything sensitive, anything that changes daily. That belongs in a source, loaded by a proper tool.']),

    columns('Our three seeds', [
        dict(title='taxi_zone_lookup', color='teal', sub='Official CSV from TLC', items=['265 zones', '`LocationID`, `Borough`, `Zone`, `service_zone`', 'Downloaded, not typed']),
        dict(title='payment_types', color='teal', sub='From the data dictionary', items=['`payment_type_id`, `payment_type_name`', 'Codes 0 to 6']),
        dict(title='rate_codes', color='teal', sub='From the data dictionary', items=['`rate_code_id`, `rate_code_name`', 'Codes 1 to 6, and 99']),
    ], kicker='What we add',
        say=['We need three seeds. The **taxi zone lookup** is an official CSV from the Taxi Commission: 265 zones, with borough and zone name. We download it as is.',
             'The other two we create from the data dictionary: **payment types** and **rate codes**. These turn the numbers in the trip data into readable names.']),

    dag('Seeds in the DAG', 4, files=['seeds/taxi_zone_lookup.csv', 'seeds/payment_types.csv', 'seeds/rate_codes.csv', 'seeds/_seeds.yml'],
        say=['On the graph, three new nodes on the left: our seeds. They sit next to the source, because, just like sources, they are where data enters the project.']),

    steps('By hand: the official lookup', [
        ('Download `taxi_zone_lookup.csv` from the TLC trip record page', None),
        ('Save it into `seeds/`', None),
        ('Open it: 265 rows, four columns', None),
    ], kicker='Hands on',
        say=['The zone lookup I add by hand. It is an official file, so nobody should retype it. I download it from the TLC page and drop it into `seeds/`.',
             'Open it: 265 rows. Location ID, borough, zone name, and service zone. Notice the names are not snake case. We fix that in staging.'],
        do=['Download https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv into seeds/.', 'Open it in the editor.']),

    prompt('Create two seeds from reference/tlc_yellow_data_dictionary.md: seeds/payment_types.csv (payment_type_id, payment_type_name) and seeds/rate_codes.csv (rate_code_id, rate_code_name). Include every code in the dictionary. Add seeds/_seeds.yml with descriptions, and column_types so the ids are integers. Then run dbt seed.',
           watch=['It reads the dictionary file', 'Terminal confirm for `dbt seed`: Allow', 'Check the codes on the next slide'], habits=[1, 4],
           say=['The other two seeds, the agent creates. Code mode. Two CSV files from the dictionary, every code included, plus a YAML file with descriptions and integer types for the IDs. Then run `dbt seed`.',
                'Watch for the terminal confirmation. The agent wants to run `dbt seed`, and it waits for me to allow it.'],
           do=['New chat, Code mode, paste the prompt.', 'Allow dbt seed when asked.']),

    columns('Check the codes', [
        dict(title='payment_types.csv', color='teal', code="payment_type_id,payment_type_name\n0,Flex Fare\n1,Credit card\n2,Cash\n3,No charge\n4,Dispute\n5,Unknown\n6,Voided trip", lang='csv', size=26),
        dict(title='rate_codes.csv', color='teal', code="rate_code_id,rate_code_name\n1,Standard rate\n2,JFK\n3,Newark\n4,Nassau or Westchester\n5,Negotiated fare\n6,Group ride\n99,Null/unknown", lang='csv', size=26),
    ], kicker='Review before Keep', verdict='**0 = Flex Fare** and **99 = unknown** are in the current dictionary. A list from memory often stops at 1-6.',
        say=['Now the review. Payment types must start at **zero, Flex Fare**, and end at six, voided trip. Rate codes must include **99**, null or unknown.',
             'Why do I check exactly these? Because older versions of this dictionary did not have them. An AI that answered from memory could easily give you one to six and miss these.',
             'This is habit one paying off: we gave it the file, so it got the current list.'],
        do=['Open both CSVs. Point at row 0 and row 99.']),

    code('Types and descriptions', 'seeds/_seeds.yml', """seeds:
  - name: payment_types
    description: Payment type codes from the TLC data dictionary.
    config:
      column_types:
        payment_type_id: integer
    columns:
      - name: payment_type_id
        data_tests: [unique, not_null]

  - name: rate_codes
    description: Rate codes from the TLC data dictionary.
    config:
      column_types:
        rate_code_id: integer""", 'yaml', kicker='seeds/_seeds.yml',
         aside=['Seeds get YAML just like models', '`column_types` stops dbt guessing types', 'Even a lookup gets a primary-key test'],
         say=['Seeds get a YAML file just like models. Descriptions, and `column_types`, so the IDs are integers instead of whatever type dbt guesses from the CSV.',
              'And even a tiny lookup gets a primary-key test: unique and not null.']),

    steps('Verify', [
        ('Load the seeds', 'dbt seed'),
        ('Look at the table in the SQL editor', 'select * from payment_types'),
        ('Three tables, built from three files in git', None),
    ], kicker='Verify',
        say=['`dbt seed` loaded three tables. In the SQL editor, `select * from payment_types`, and there it is, seven rows, from a file in git.'],
        do=['SQL editor: select * from payment_types; show the 7 rows.']),

    recap('Section 04 done', [
        'Seeds are small, static CSVs in the project',
        'The official zone lookup, downloaded as is',
        'Two code lists created from the dictionary, not from memory',
        'Types and tests in `_seeds.yml`; loaded with `dbt seed`',
    ], 's04-end', blocks=['sources', 'seeds'], next='S05 · Staging models',
        say=['Recap. Three seeds: one official file, two created from the dictionary. We checked the codes, we typed the IDs, we loaded them.',
             'Second block: **seeds**. Tag `s04-end`. Next, we write our first models: **staging**.']),
])

DECKS = [S00, S01, S02, S03, S04]
