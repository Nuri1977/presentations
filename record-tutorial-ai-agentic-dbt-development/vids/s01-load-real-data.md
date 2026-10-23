# S01 · Load the real data: dbt is the "T": Google Vids script

**Import:** `s01-load-real-data.pptx` (speaker notes = the scripts below). **Voiceover:** 575 words, about 3.8 min at 150 wpm. **Demo recording budget:** about 5.7 min (Vids videos max 10 min).

**Scene order in Vids:** scenes 1 to 12 (slides) → your demo recording → scene 13 (recap). Drag the recap scene to the end after you add the recording.

**Before converting:** in Google Slides, replace the amber `?` numbers on the real-data slides with your dry-run results. The scripts never read the numbers aloud, so only the slide changes.

## Voiceover, scene by scene

**Scene 1 · Load the real data**

Section one. Before writing any dbt model, we need data in the database, and we need to understand it. We load two months of real taxi trips into DuckDB with the agent, and then we find out what is wrong with the data.

**Scene 2 · dbt doesn't load data. It transforms data that's already there.**

Here is something that surprises many beginners. dbt does not load data. It does not download files or call APIs. It transforms data that is already in your database. Loading is done by other tools, before dbt starts.

**Scene 3 · ELT, in our project**

Extract: the Taxi Commission publishes Parquet files. Load: DuckDB reads them into a schema called raw. Transform: that is dbt, and the rest of this course. We keep the loading SQL in a script, outside dbt, so we can run it again when a new month arrives.

**Scene 4 · Introduction: ELT**

The dbt introduction says the same thing. Data is extracted and loaded by other tools. dbt handles the transformation: modelling, cleaning, testing and documenting. And because dbt only writes select statements, the database does the heavy work.

**Scene 5 · The dataset**

The dataset. Parquet files, one per month, around three to four million trips each. We start with November and December twenty twenty-four, and add January twenty twenty-five later, on purpose. There is also a zone lookup file and an official data dictionary.

**Scene 6 · What is in a trip record**

Each row is one taxi trip. When and where: pickup and dropoff times and zones, distance and passengers. Codes, like rate code and payment type, that only make sense with the dictionary. And money columns. The last one, the congestion fee, only exists from January twenty twenty-five.

**Scene 7 · The source system's docs are docs too**

Our first habit in action. We transcribe the official data dictionary into a Markdown file inside the project. From now on, the agent reads code lists and descriptions from that file, not from memory, because lists like these change over time.

**Scene 8 · Prompt card**

This is the first prompt for the demo. In the SQL editor, the agent creates a raw schema and loads both monthly files into one table, keeping the file name on every row. We ask to see the SQL first, and Rosetta stops at an approval gate before anything runs.

**Scene 9 · What the load looks like**

This is roughly the SQL the agent writes, and we save it as the load script. One create table statement that reads both Parquet files. Union by name lets files with different columns combine, which matters later when a new column arrives.

**Scene 10 · Prompt card**

Next, in Ask mode, the agent profiles the table: rows per file, the date range, empty values per column, and three suspicious things. Negative fares, trips with zero distance, and trips that end before they start. We look at the data before we write rules about it.

**Scene 11 · What we found**

Here is what real data looks like. Trips picked up outside the month of their file. Negative fares. Trips with zero distance. A block of rows with no passenger count. And trips that end before they start. This is not our bug. This is the source.

**Scene 12 · Where each problem gets handled**

Every one of these problems has a home in this course. Guessed tests in the sources section. Changed code lists in seeds. Backwards trips in data tests. Zero distance and invalid trips in the intermediate model. And the new January column in incremental models.

**Scene 13 · Section 01 done**

That is section one. dbt is the T in E L T. Two months of real trips are loaded, the data dictionary is in the project, and we know what is wrong with the data. Next: what a dbt project is made of, and how we teach the agent our rules.

## Demo recording: prompting and changing files

**Set up before you hit record**

- Project `nyc_taxi` open. `data/` holds `yellow_tripdata_2024-11.parquet` and `yellow_tripdata_2024-12.parquet`.
- `reference/tlc_yellow_data_dictionary.md` written (transcribed from the TLC PDF, every code list included).

**Steps**

1. Open `reference/tlc_yellow_data_dictionary.md`; scroll slowly through the code lists. *File:* `reference/tlc_yellow_data_dictionary.md`
2. SQL Editor → AI panel → **Code** mode. Paste prompt 1.

   > In the DuckDB connection, create a schema called raw. Load data/yellow_tripdata_2024-11.parquet and data/yellow_tripdata_2024-12.parquet into a table raw.yellow_trips using read_parquet with union_by_name and filename = true, so every row keeps the file it came from. Show me the SQL before you run it.

3. At the **approval gate**: pause on the SQL, then **Allow**.
4. Save the SQL as `scripts/load_raw.sql` (use absolute paths). *File:* `scripts/load_raw.sql`
5. Switch the AI panel to **Ask** mode. Paste prompt 2. Let it run all queries.

   > Profile raw.yellow_trips: rows per source file, the pickup date range, null count per column, and how many rows have fare_amount < 0, trip_distance = 0, or dropoff before pickup. One query per question, and show the numbers in a table.

6. Scroll the result tables slowly: rows per file, date range, nulls, negative fares, zero distance, backwards trips.

**Optional lines to say over the recording**

- "The agent shows the SQL first, and waits for my approval."
- "Now we look at the data before we write any rules."
- "These are the numbers on the "What we found" slide."

**All prompts in this section, ready to paste**

1. In the DuckDB connection, create a schema called raw. Load data/yellow_tripdata_2024-11.parquet and data/yellow_tripdata_2024-12.parquet into a table raw.yellow_trips using read_parquet with union_by_name and filename = true, so every row keeps the file it came from. Show me the SQL before you run it.

2. Profile raw.yellow_trips: rows per source file, the pickup date range, null count per column, and how many rows have fare_amount < 0, trip_distance = 0, or dropoff before pickup. One query per question, and show the numbers in a table.
