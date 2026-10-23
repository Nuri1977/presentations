"""Voiceover scripts for Google Vids, one entry per slide, in slide order.

Rules: written for an AI voice. No square brackets (Vids reads them as voice tags), no code
identifiers read aloud, about 20-25 seconds per scene. Numbers from the dry run are shown
on screen, so the scripts never need them.
"""

TTS = {}

TTS[0] = [
    # 1 title
    "Welcome to AI agentic dbt development. In this crash course we build one real dbt project, from an empty folder to production patterns, using Rosetta dbt Studio and its built-in AI agent. All you need is basic SQL.",
    # 2 statement
    "Agentic means the AI does more than chat. It reads your project, writes files, and runs dbt commands. That is powerful, which is exactly why you stay the engineer. The agent proposes. You review, you decide, and dbt tells you if it is right.",
    # 3 agentic loop
    "Every time we use the agent, we follow one loop. Prompt with good context. Let the agent plan. Let it act. Then review every change. Then run dbt, and verify the actual rows. Review is the step people skip, and the one that matters most.",
    # 4 habits
    "Six habits, used in every section. Give the agent files, not memory. Plan before acting on big tasks. One task per chat. Read every diff before you keep it. Let dbt be the judge. And if you correct the agent twice, write the rule into a skill.",
    # 5 rhythm
    "Each section follows the same rhythm. A few slides with the idea. The official dbt documentation, version one. Then a recorded demo in Rosetta dbt Studio, where we build it, first by hand and then with the agent. We finish with a git checkpoint.",
    # 6 dag
    "This is the project you will build. Sources and seeds on the left. Staging models, one intermediate model with our business rules, and marts on the right. A snapshot keeps history at the bottom, and an exposure marks the real analysis we answer at the end.",
    # 7 data
    "We use real data: New York City yellow taxi trips, published every month by the Taxi and Limousine Commission. Millions of rows per month, small enough for a laptop, and messy enough that our tests will really fail. That is the point.",
    # 8 screen
    "The screen in Rosetta dbt Studio. The project files on the left. The editor in the middle, with run, preview and compiled SQL. The AI chat on the right. Every file the agent writes opens for review, with Keep or Discard. Every command it wants to run waits for Allow or Deny.",
    # 9 modes
    "The chat has two modes. Ask mode is read-only. We use it to explain, profile data, and trace lineage. Code mode is where the agent writes files and runs commands. Ask when you want to understand. Code when you want something built.",
    # 10 docs
    "The dbt documentation now has two versions. This course follows version one, the version Rosetta dbt Studio runs. The core idea: dbt transforms data that is already in your database. You write select statements, and dbt handles the order, the tests and the documentation.",
    # 11 course map
    "Here is the map. Part one covers loading data, project structure, sources, seeds, staging, tests, macros, and the final marts. Part two covers unit tests, incremental models, snapshots, and documentation, ending with a real analysis.",
    # 12 let's start
    "In the demo for this section, we create a new project called N Y C taxi, connect it to a new DuckDB database file, look at the AI, skills and M C P settings, and run dbt debug to check that everything works.",
    # 13 recap
    "That is section zero. We know what we are building, the agentic loop, and the six habits, and we have an empty project that passes dbt debug. Next, we load the real data.",
]

TTS[1] = [
    "Section one. Before writing any dbt model, we need data in the database, and we need to understand it. We load two months of real taxi trips into DuckDB with the agent, and then we find out what is wrong with the data.",
    "Here is something that surprises many beginners. dbt does not load data. It does not download files or call APIs. It transforms data that is already in your database. Loading is done by other tools, before dbt starts.",
    "Extract: the Taxi Commission publishes Parquet files. Load: DuckDB reads them into a schema called raw. Transform: that is dbt, and the rest of this course. We keep the loading SQL in a script, outside dbt, so we can run it again when a new month arrives.",
    "The dbt introduction says the same thing. Data is extracted and loaded by other tools. dbt handles the transformation: modelling, cleaning, testing and documenting. And because dbt only writes select statements, the database does the heavy work.",
    "The dataset. Parquet files, one per month, around three to four million trips each. We start with November and December twenty twenty-four, and add January twenty twenty-five later, on purpose. There is also a zone lookup file and an official data dictionary.",
    "Each row is one taxi trip. When and where: pickup and dropoff times and zones, distance and passengers. Codes, like rate code and payment type, that only make sense with the dictionary. And money columns. The last one, the congestion fee, only exists from January twenty twenty-five.",
    "Our first habit in action. We transcribe the official data dictionary into a Markdown file inside the project. From now on, the agent reads code lists and descriptions from that file, not from memory, because lists like these change over time.",
    "This is the first prompt for the demo. In the SQL editor, the agent creates a raw schema and loads both monthly files into one table, keeping the file name on every row. We ask to see the SQL first, and Rosetta stops at an approval gate before anything runs.",
    "This is roughly the SQL the agent writes, and we save it as the load script. One create table statement that reads both Parquet files. Union by name lets files with different columns combine, which matters later when a new column arrives.",
    "Next, in Ask mode, the agent profiles the table: rows per file, the date range, empty values per column, and three suspicious things. Negative fares, trips with zero distance, and trips that end before they start. We look at the data before we write rules about it.",
    "Here is what real data looks like. Trips picked up outside the month of their file. Negative fares. Trips with zero distance. A block of rows with no passenger count. And trips that end before they start. This is not our bug. This is the source.",
    "Every one of these problems has a home in this course. Guessed tests in the sources section. Changed code lists in seeds. Backwards trips in data tests. Zero distance and invalid trips in the intermediate model. And the new January column in incremental models.",
    "That is section one. dbt is the T in E L T. Two months of real trips are loaded, the data dictionary is in the project, and we know what is wrong with the data. Next: what a dbt project is made of, and how we teach the agent our rules.",
]

TTS[2] = [
    "Section two. We look inside a dbt project: its building blocks, the one configuration file every project has, and the folder structure we follow. Then we teach the agent those rules with a skill.",
    "A dbt project is just a folder. The only required file is dbt project dot yml. Models live in the models folder, with YAML files that describe and test them. Seeds, snapshots, tests, macros and analyses each have their own folder. A connection profile says where to build.",
    "The page About dbt projects, version one, is the map of this course. Its resources table lists every building block a project can have. Its project configuration table lists the settings we put in dbt project dot yml.",
    "Here is every block from that page, with the section that builds it. Models, sources, seeds, tests, macros, analyses, snapshots, docs and exposures. The dashed blocks, like metrics and the semantic layer, are beyond this crash course.",
    "The settings we use. The project name. Our own version number. A required dbt version range, so the project only runs on dbt version one. The connection profile. And the folder paths, which we keep at their defaults. Variables come later, in section ten.",
    "We write this file by hand. The interesting part is at the bottom: settings per folder. Staging and intermediate models become views. Marts become tables. The plus sign means this is a setting, not a folder name. From now on, the folder decides how a model is built.",
    "dbt Labs recommends three layers. Staging is shaped like the source: one model per table, renamed and typed. Intermediate holds business logic. Marts are shaped like the business, and they are what analysts query.",
    "The structure guide puts it simply: move data from source-conformed to business-conformed. And the goal is consistency, so nobody wastes time deciding names and folders. That is exactly what we want the agent to follow.",
    "How does the agent learn these rules? With a skill: a Markdown file of instructions with a short description. What we read in the docs, we write into the skill, and the agent loads it whenever a task matches.",
    "This is our skill, shortened. The dbt version. Naming for each layer. Column conventions, like timestamps ending in at, and booleans starting with is. And the key rule: code values come from the dictionary file, never from memory.",
    "Skills are app-wide, so every project can use them. M C P servers give the agent extra knowledge, like the dbt, DuckDB and Rosetta documentation. You can add your own with one link, for example the dbt documentation site.",
    "In the demo, we test the setup with an Ask mode question: what is the difference between a source and a seed, using the dbt version one docs. The agent should look it up, and tell us which page it used.",
    "That is section two. We know the building blocks, we configured the project file, we know the three layers, and the agent has a skill with our rules. Next: our first block, sources.",
]

TTS[3] = [
    "Section three: sources. This is how we tell dbt about data that already exists in the database, data that dbt did not build.",
    "One rule: never hard-code a table name in a model. It works, but dbt cannot see the dependency. It cannot draw it in the lineage, test it, or document it, and if the schema changes, every model breaks.",
    "On the left, a hard-coded table. On the right, the source function, with the source name and the table name. Both compile to the same SQL, but only the right one appears in the lineage graph, with tests and descriptions attached.",
    "The sources page, version one. Declare sources in YAML, with a name, the schema, and the tables. Select from them with the source function. Add tests and descriptions to source columns. And freshness can warn you when a loader stops delivering data.",
    "On our lineage graph, the first node lights up: the source for yellow taxi trips. Everything else in the project will be built on top of it.",
    "Rosetta can generate the source file for us. The Raw Layer option reads the database and writes a YAML file with every column. No AI involved. It also adds a not null test to every column. That is a guess, and real data will test it.",
    "In the demo, the agent moves that file into our staging folder, names the source T L C, and adds a description to every column from the dictionary file. We tell it not to change the tests yet.",
    "This is what we review before keeping it. The source name and schema. Descriptions that match the dictionary. Notice payment type starts at zero, Flex Fare, from the current dictionary. And the tests are still the generated guesses.",
    "Then we run the source tests. Several not null tests fail: passenger count, rate code, the store and forward flag, and some surcharges. That is real data pushing back on a guess.",
    "Instead of deleting the tests, we ask why. In Ask mode: which rows fail, and what do they have in common?",
    "In our data, the rows with an empty passenger count are the rows with payment type zero, which the dictionary calls Flex Fare. So these are not broken rows. They are a different kind of trip, where some fields are not recorded.",
    "So we decide. We keep not null where a trip cannot exist without a value: the times, the locations and the total. We drop it where the source legitimately leaves values empty. A failing test is a decision, not a bug.",
    "One last thing: freshness. It compares a timestamp with the current time. Our data is historical, so it would always look stale, and we skip it. In a real project with daily data, you turn it on. It tells you when a loader stopped working.",
    "That is section three. Our raw table is now a documented source, and its tests describe reality instead of a guess. First block ticked: sources. Next: seeds.",
]

TTS[4] = [
    "Section four: seeds. Some data is not in any source system. It is a small list we maintain ourselves, like codes and their names. That is what seeds are for.",
    "The seeds page, version one. A seed is a CSV file in the project. dbt seed loads it as a table. Because it is a file in the project, it is version controlled and reviewed. Seeds are best for static data that changes rarely.",
    "Good seeds are small, static lists: code mappings, regions, test accounts to exclude. Bad seeds are raw data exported to CSV, anything large or sensitive, and anything that changes every day.",
    "We need three seeds. The official zone lookup from the Taxi Commission, with two hundred sixty-five zones. And two lists we create from the dictionary: payment types and rate codes. They turn numbers in the trip data into readable names.",
    "On the graph, three new nodes on the left, next to the source. Like sources, seeds are where data enters the project.",
    "The zone lookup is an official file, so nobody should retype it. In the demo, we download it from the Taxi Commission page and drop it into the seeds folder. Notice the column names are not snake case yet. We fix that in staging.",
    "The other two seeds, the agent creates from the dictionary file: every payment type, every rate code, a YAML file with descriptions, and integer types for the IDs. Then it asks to run dbt seed, and waits for our approval.",
    "The review. Payment types must start at zero, Flex Fare, and include six, voided trip. Rate codes must include ninety-nine, unknown. Older versions of the dictionary did not have these, so a list from memory would be wrong. We gave the agent the file, so it got the current list.",
    "Seeds get YAML just like models. Descriptions, and column types, so the IDs are integers instead of guessed types. Even a small lookup gets a primary key test.",
    "We load the seeds with dbt seed and look at the table in the SQL editor. Seven payment types, built from a file in git.",
    "That is section four. Three seeds: one official file, two created from the dictionary, checked and loaded. Next, our first models: staging.",
]

TTS[5] = [
    "Section five: staging models. They take a source and make it clean and consistent. We write the first one by hand, so you see exactly what a model is, and the agent writes the big one.",
    "If you remember one thing: a dbt model is just a select statement in a file. You never write create table. The file name becomes the model name, and dbt adds the right create statement for you.",
    "The SQL models page, version one. A model is one select in a SQL file. The file name is the name of the view or table. To use another model, you use ref, and dbt works out the order. The default is a view.",
    "On the left, what we write: a select, with ref to the zone seed. On the right, what dbt sends to the database: a create view, with ref replaced by the real table name. The Compiled SQL tab in Rosetta shows this for any model.",
    "Every ref is an arrow in the lineage graph. The staging model uses the seed, so the seed is built first. Later, a dimension uses the staging model. dbt reads all these references and builds from left to right.",
    "The structure guide on staging. Name files S T G, then the source, two underscores, then the entity. Do renaming, type casting and simple calculations. Do not join or aggregate. Staging models are views.",
    "Our checklist. Rename to snake case, cast types, turn the yes or no flag into a boolean, and keep every row. No joins, no aggregations, and no filtering. The strange trips stay in staging. We flag them later, where the business rule belongs.",
    "Our first model, written by hand. A source step that selects from the seed with ref. A renamed step that gives every column a clean name. And a final select. The agent will follow the same pattern.",
    "We run it with the model button, open Preview to see the renamed zones, and open Compiled SQL to see ref replaced by the table. We never wrote view in the file. The folder setting from section two decided it.",
    "The trips model is bigger: twenty columns. Timestamps end in at. Distance gets its unit. IDs become snake case. The flag becomes a boolean. Money becomes a decimal. And the file name is kept as source file. Repetitive work, perfect for the agent.",
    "In the demo, the agent creates the staging model for yellow trips, following our skill: snake case, the at suffix, a boolean, decimals, and source file. No filters, no joins. Plus a YAML file with descriptions. Then it builds only this model.",
    "This is the shape we expect, and how we review it. It uses source, not a table name. Every money column is cast. And two things must not be there: a where clause, and a config block. If either appears, we ask the agent to remove it before keeping the file.",
    "Two new nodes in the lineage: our staging models, each fed by exactly one input. One to one, just as the guide says.",
    "That is section five. Models are select statements, ref and source build the graph, and we have two staging models, one by hand and one by the agent. Next: we write down what we expect from the data, with tests.",
]

TTS[6] = [
    "Section six: data tests. A test is how we write down an assumption, so dbt checks it on every run. With real data, some assumptions will be wrong. That is the point.",
    "Every dbt test is a query that looks for bad rows. Zero rows means the test passes. Any rows means it fails, and the failing rows are right there to look at.",
    "dbt ships four generic tests. Unique and not null, usually together on a primary key. Accepted values, for columns with a known list, like payment types. And relationships, which checks that every value exists in another model, like a foreign key.",
    "Two kinds of test. Generic tests are reusable, and you list them under a column in YAML. Singular tests are one SQL file in the tests folder. This one returns trips that end before they start.",
    "The data tests page, version one. Generic tests go under the data tests key in YAML. Singular tests are SQL files. You can set severity to error or warn, test only some rows, and store failing rows in a table.",
    "First, by hand: the zone ID is our primary key, so it gets unique and not null. Two lines, and the official lookup passes.",
    "In the demo, the agent adds the rest: not null on the timestamps, accepted values on payment type from the seed, relationships from both location columns to the zones, and the singular test for backwards trips. Then it runs the tests for this model.",
    "What we review. Accepted values zero to six, taken from the seed. In recent dbt version one, the values sit under a key called arguments. Quote is false, because the codes are numbers. And the relationships test points at the zones model.",
    "The singular test is a plain query for the rows that break our rule: dropoff before pickup. It returns the source file too, so we can see which month the bad rows came from.",
    "And real data says no. The singular test fails: some trips really do end before they start. The accepted values test passes, because we used the current code list. Now we decide what to do.",
    "Rosetta has a shortcut for this moment. In Run History, open the failed test, and the error view offers an AI assistant. We let it propose a fix, and we read it before deciding.",
    "Three options. Deleting the rows in staging hides a real problem, so no. Making the test a warning and storing the failing rows keeps them visible without blocking every build. And in section eight, we flag invalid trips in the intermediate layer. A failing test is a decision.",
    "One line at the top: severity warn, and store failures. The build continues with a warning, and the failing rows are saved in a table we can query.",
    "That is section six. Tests are queries for bad rows. Real data failed one, the AI assistant made a suggestion, and we made the call. Next: reusing code with packages, Jinja and macros.",
]

TTS[7] = [
    "Section seven. So far our SQL has been plain. Now we make it smarter: we install a package, use Jinja, write a macro, and meet analyses.",
    "A real problem: taxi trips have no trip ID. Nothing identifies one trip. We need a primary key to test uniqueness, and later so an incremental model knows which rows to replace. We will build one from several columns.",
    "The packages page. A package is another dbt project you install into yours, usually for its macros and tests. You list packages in a YAML file and run dbt deps. The most used one is dbt utils, from dbt Labs.",
    "In the demo, the agent adds dbt utils with the latest compatible version and runs dbt deps. Afterwards we check the version on the dbt package hub ourselves. Version numbers are exactly what an AI can get slightly wrong.",
    "Three lines. Notice the version range: at least one point three, below two. We get fixes, but nothing that breaks us.",
    "Before using it, we understand it. In Ask mode: what does the surrogate key macro do, and which columns could identify a trip? It hashes several columns into one ID, and identical rows get the same key, which is how we will find duplicates.",
    "dbt models are SQL plus Jinja. Double curly braces print something, like ref and source. Curly brace and percent sign is logic: loops, ifs, and macros. Curly brace and hash is a comment. dbt renders the Jinja first, and the database only sees plain SQL.",
    "The Jinja and macros page. Jinja adds loops, variables and functions to SQL. A macro is a reusable function in the macros folder. And always check the compiled SQL to see what you produced.",
    "Our own macro, safe divide. Remember the trips with zero distance? Fare per mile would divide by zero. This macro returns empty instead of an error, and every model can use it.",
    "On the left, how we call the macro in a model. On the right, what dbt compiles it into: a plain case expression. The database never sees Jinja.",
    "Analyses are another block from the projects page. An analysis is a SQL file that dbt compiles but never runs, so no table is built. They are great for queries you want to keep in git, and for experimenting with Jinja.",
    "An analysis with a loop. For each payment type in the list, it writes one count column. Compile it, and the loop is replaced by real columns. But the list is hard-coded, which is not great.",
    "In the demo, the agent makes it data-driven. A dbt utils macro reads the payment types from the seed at compile time. Add a code to the CSV, and the SQL follows automatically.",
    "That is section seven. A package with a version range, Jinja expressions and loops, our own macro, and an analysis. Next: we put it all together into intermediate and mart models.",
]

TTS[8] = [
    "Section eight, the end of part one. We build the layers that turn clean data into answers: an intermediate model with our business rules, and the marts analysts use. The biggest agent task so far, so we plan before we act.",
    "Staging is done. The intermediate layer adds a trip ID, removes exact duplicates, and adds trip duration, fare per mile, and the valid trip flag we promised. The marts are a fact table of valid trips, a zone dimension, and a daily summary per pickup zone.",
    "The structure guide on intermediate models. Each one has a specific purpose, like isolating complex logic so the marts stay simple. End users never query them. They are views or ephemeral.",
    "The guide on marts. A mart is something the business understands: here, a trip, a zone, and a zone per day. Marts are wide, and they are tables, so queries are fast.",
    "Materialization means how dbt builds a model. A view stores only the query. A table stores the result. Incremental adds only new rows, in section ten. Ephemeral builds nothing and is inlined. A materialized view is kept up to date by the database.",
    "The materializations page. You can set them in the project file, in YAML, or in the model itself, and the most specific setting wins. We set them per folder, and in section ten, one model will override its folder.",
    "This task touches four models and several files. If the agent starts writing and gets the grain wrong, we review a lot of wrong code. So first, we ask for a plan, and we fix the plan.",
    "In the demo, the first prompt asks for the plan only: which intermediate and mart models, the grain of each one, its inputs and its materialization. And it must wait for our OK, without writing any files.",
    "This is the plan we approve. One intermediate model, one row per trip. A fact table, one row per valid trip. A zone dimension. And a daily summary, one row per zone per day. Fixing a plan is much cheaper than fixing code.",
    "Then: go ahead. The agent builds the trip ID, removes duplicates, adds duration and fare per mile with our macro, the validity flag with a reason, and the code names. Then the marts, YAML with tests for every model, and one dbt build.",
    "The heart of the project. The surrogate key from dbt utils. Duration in minutes. Fare per mile with our safe divide. One row per trip ID. And a reason for every invalid trip: ends before it starts, zero distance, negative total, or a pickup outside its file month.",
    "Four new nodes. The intermediate model, fed by staging and two seeds. Then the fact table, the zone dimension, and the daily summary that uses both.",
    "A word on selecting models. A name selects one model. A plus before it adds everything upstream. A plus after it adds everything downstream. You can also select by folder, by source, or by test type.",
    "We run dbt build for everything up to the daily summary: seeds, staging, intermediate, marts, and every test, in the right order. Then we look at the lineage, the timings in Run History, and preview the result.",
    "We ask the data why trips are invalid, by reason, and how many duplicates were removed. Every problem we found in section one now has a rule, a name, and a count. The fact table only contains valid trips.",
    "That is the end of part one. A complete, tested dbt project, from raw files to a fact table and a daily summary, with our business rules in one reviewed place. In part two we make it production-ready.",
]

TTS[9] = [
    "Welcome to part two: production patterns. We start with unit tests. Our tests so far check the data, but our business logic could have a bug that today's data simply does not show. Unit tests catch that.",
    "Two different questions. A data test runs on the real tables and asks: is this data right? A unit test feeds a model a few rows that we invent, and asks: does my SQL do what I meant?",
    "The unit tests page, version one, available since dbt one point eight. A unit test lives in YAML. Given: fake input rows for every model the tested model reads. Expect: the rows that should come out. You only list the columns that matter.",
    "One unit test. The model under test is the intermediate trips model. Given one fake trip with zero distance, and empty inputs for the two seeds, because every input must be mocked. We expect fare per mile to be empty, the trip invalid, and the reason zero distance.",
    "Deciding what to test is the human part. Four cases from the problems we found. Zero distance. A trip that ends before it starts. A normal trip, two and a half miles for fifteen dollars, which must be valid at six dollars a mile. And a negative total.",
    "In the demo, we describe the four cases in plain English, and the agent writes the YAML, mocks every input, and runs only the unit tests. Verbose YAML is perfect agent work. The cases are ours.",
    "We run only the unit tests, and four pass. If one fails, ask the honest question: is the test wrong, or the model?",
    "A test you have never seen fail is a test you cannot trust. So we break the model on purpose.",
    "We change one character: less than or equal to zero becomes less than zero. Now zero-distance trips are valid. The first unit test turns red, and dbt shows what we expected and what we got. We undo the change, and it is green again.",
    "That is section nine. Unit tests lock our business logic. We chose the cases, the agent wrote the YAML, and we watched a test fail on purpose. Next: incremental models.",
]

TTS[10] = [
    "Section ten. Today the fact table is rebuilt from all trips on every run, and that gets slow. We make it incremental, so only new trips are processed. Then a new month arrives, with a surprise.",
    "A table is thrown away and rebuilt on every run. An incremental model keeps the existing table and processes only new rows, inserting them, or replacing rows with the same key.",
    "The incremental models page, version one. The is incremental function is true only on a normal run against an existing table. The word this refers to the existing table. A unique key lets dbt replace rows. And on schema change decides what happens when columns change.",
    "The whole pattern. A config block that says incremental. Then an if block that adds a filter. On the first run, or a full refresh, everything loads. On later runs, only rows newer than what is already in the table.",
    "How are new rows written? The DuckDB configs page lists four strategies. Append, delete and insert, merge, and microbatch. We use delete and insert with our trip ID: simple, and safe when the same trip arrives twice.",
    "Before changing anything, we ask in Ask mode how this would behave. A trip from the last days of the previous month could be missed, so we look back a few days, and the unique key replaces anything we see twice.",
    "How many days back is a setting, not code. So it becomes a project variable, the vars key from section two. We can override it on the command line for a single run.",
    "In the demo, the agent makes the fact table incremental: the trip ID as unique key, delete and insert, and a filter that uses our lookback variable. We leave on schema change at its default, and run it once with a full refresh.",
    "We review it. The folder says table, but the config in the file says incremental, and the file wins because it is more specific. The validity filter, the lookback from the variable, and no on schema change yet.",
    "Now real life happens. January twenty twenty-five is published. We add the file to our load script and run it again. Then dbt build for staging and everything downstream, and Run History shows that only the new rows were processed.",
    "The surprise. January brings a new column: the C B D congestion fee, for the Manhattan Congestion Relief Zone that started on January fifth. It is in the raw table, but not in staging or the fact table. Nothing changes downstream without our decision.",
    "Back to the docs. The default, ignore, does not add new columns. Append new columns adds them. And none of the options fill in old rows. That needs a full refresh.",
    "In the demo, the agent carries the new column through every layer: the dictionary file, the source, staging, intermediate and the fact table, and sets on schema change so the column is added without a full refresh. Updating the dictionary keeps the agent's context current.",
    "The column appears. January rows have values, November and December are empty, exactly as the docs said. Here empty is actually correct, because the fee did not exist before January. Know which option you are choosing.",
    "That is section ten. The fact table is incremental, with a lookback variable, and a real schema change arrived and was carried through on purpose. Next: snapshots.",
]

TTS[11] = [
    "Section eleven: snapshots. Trips never change once they happen. But some data is updated in place, and when that happens, the old value is gone. Snapshots keep it.",
    "Think of an address, a price, or a vendor name. The source system overwrites it, and yesterday's value is lost, unless we keep one row per version, with the dates each version was valid. That is a slowly changing dimension, type two.",
    "This really happened in our data. Older versions of the taxi data dictionary say vendor two is VeriFone. The current one says Curb Mobility. And two new vendors appeared, Myle and Helix.",
    "The snapshots page, version one. Since dbt one point nine, a snapshot is a YAML file pointing at a source or model. It needs a unique key and a strategy. dbt adds valid from and valid to columns, and snapshots ignore full refresh, so history is never wiped.",
    "Two strategies. Timestamp compares an updated at column, when the source has a reliable one. Check compares the actual values of the columns you list. Our vendor list has no timestamp, so we check the vendor name.",
    "First we need a source system that changes. In the demo, the agent creates a small vendor registry table with the old list: Creative Mobile Technologies, and VeriFone.",
    "Then the agent adds the table to our source, creates the snapshot in YAML with the check strategy, and runs dbt snapshot. Many examples online use an older syntax. Our skill says YAML.",
    "Seven lines: a name, the source it reads, a unique key, the check strategy, and the column to check. If the agent writes the old syntax, we discard it, and add the rule to the skill.",
    "After the first snapshot, both vendors are current, and their valid to column is empty.",
    "Then someone updates the vendor system. Vendor two becomes Curb Mobility, and vendors six and seven are added, exactly as in the real dictionary. We run dbt snapshot again.",
    "History, kept. Vendor two now has two rows: VeriFone, valid until the second run, and Curb Mobility, valid from then on. Any report can now ask what a vendor was called at the time of a trip.",
    "On the graph: the new source, the snapshot, and a vendor dimension built from the current rows of the snapshot.",
    "That is section eleven. Snapshots keep history, and we used one on a real change from the taxi data dictionary. Next: documentation, lineage, and a real answer.",
]

TTS[12] = [
    "Section twelve, the capstone. We make the project explain itself, ask it questions, answer a real question about congestion pricing, and declare who uses our work.",
    "Documentation in a wiki goes stale. In dbt, it lives in the same YAML files as the tests, in the same change as the code, and dbt turns it into a website with a lineage graph.",
    "The documentation page, version one. Descriptions go in YAML. Text needed in many places goes in a doc block, written once and used everywhere. dbt docs generate builds the documentation, and dbt docs serve opens it as a website.",
    "A doc block in a Markdown file explains payment types once. Every YAML file that has a payment type column points to it. One text, four columns, always consistent.",
    "In the demo, the agent creates doc blocks for payment type, rate code and trip validity, uses them everywhere, and makes sure every model and column has a description. Tedious work across many files, perfect for an agent.",
    "Then we generate the docs and open the site. Every model, column, test and query is there, with a lineage graph that matches the one in Rosetta.",
    "Now the project explains itself. In Ask mode, we ask the agent to trace the congestion fee from the source to every model that uses it. It reads the files and gives the path.",
    "Another good question before any join: what is the grain of the daily summary, and can we join it to trips without multiplying rows? One row per zone per day, so joining it to trips repeats rows. The agent should warn us.",
    "And now the question the whole project was building towards. January twenty twenty-five was the first month of congestion pricing in New York. How much fee was collected, and where?",
    "We ask it in Rosetta's analytics, on top of our marts. Only valid trips count, and we see boroughs instead of IDs. Everything we built is inside this answer.",
    "Here is the answer on screen: the total fee collected in January, the share of valid trips that paid it, and the borough that collected the most. From raw files to a tested, documented answer.",
    "The last block: exposures. An exposure tells dbt that something downstream depends on our models, like this analysis. If someone changes the fact table tomorrow, they see the analysis in the lineage.",
    "The agent declares it: a name, a label, the type analysis, an owner, and the two marts it depends on.",
    "And here is the complete project, every node built, with our analysis on the far right. From two Parquet files to this.",
    "That is section twelve. Fully documented, a docs website, a project that explains itself, and a real answer, declared as an exposure. One short section left.",
]

TTS[13] = [
    "The final section. Let's look back at what we built, and where you can go next.",
    "This is your project. Sources and seeds, staging, an intermediate model with tested business rules, marts, a snapshot keeping history, and an exposure for a real analysis. Real data, real problems, real decisions.",
    "Remember the map from section two? Every planned block is ticked: models, sources, seeds, tests, macros, analyses, snapshots, docs and exposures. The dashed ones, like metrics and the semantic layer, are your next steps.",
    "If you keep only three habits: give the agent context, not memory. Read every diff before you keep it. And let dbt be the judge. The agent made us faster, but every decision in this project was ours.",
    "The dbt commands we used, all from version one: debug, seed, run and build, test, compile, deps, snapshot, and docs. In Rosetta most of them are buttons, and now you know what each one does.",
    "Where to go next. The semantic layer, to define metrics like revenue once. Contracts and groups, when other teams depend on your models. Python models, which DuckDB supports. And automatic builds on every change, with Rosetta Cloud.",
    "Thank you for building this with us. The project, every checkpoint, and every prompt from this course are in the companion repository. Clone it, try the prompts, and let us know what you build.",
]

# Alternative scripts for scenes that depend on what the dry run shows: (section, scene) -> text
ALT = {
    (3, 11): "In our data, the rows with an empty passenger count are incomplete in several columns at once. The source simply does not record those fields for some trips. So the right question is not how to fix them, but which columns must always have a value.",
    (6, 10): "And real data answers. Look at the singular test result on screen, and the accepted values test, which uses the current code list. Whatever a test reports, the next step is the same: we decide what to do.",
}
