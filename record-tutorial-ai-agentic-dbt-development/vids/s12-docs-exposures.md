# S12 · Docs, lineage & exposures: the capstone: Google Vids script

**Import:** `s12-docs-exposures.pptx` (speaker notes = the scripts below). **Voiceover:** 465 words, about 3.1 min at 150 wpm. **Demo recording budget:** about 6.4 min (Vids videos max 10 min).

**Scene order in Vids:** scenes 1 to 14 (slides) → your demo recording → scene 15 (recap). Drag the recap scene to the end after you add the recording.

**Before converting:** in Google Slides, replace the amber `?` numbers on the real-data slides with your dry-run results. The scripts never read the numbers aloud, so only the slide changes.

## Voiceover, scene by scene

**Scene 1 · Docs, lineage & exposures**

Section twelve, the capstone. We make the project explain itself, ask it questions, answer a real question about congestion pricing, and declare who uses our work.

**Scene 2 · Docs that live next to the code get updated with the code.**

Documentation in a wiki goes stale. In dbt, it lives in the same YAML files as the tests, in the same change as the code, and dbt turns it into a website with a lineage graph.

**Scene 3 · Documentation**

The documentation page, version one. Descriptions go in YAML. Text needed in many places goes in a doc block, written once and used everywhere. dbt docs generate builds the documentation, and dbt docs serve opens it as a website.

**Scene 4 · A doc block, written once, used everywhere**

A doc block in a Markdown file explains payment types once. Every YAML file that has a payment type column points to it. One text, four columns, always consistent.

**Scene 5 · Prompt card**

In the demo, the agent creates doc blocks for payment type, rate code and trip validity, uses them everywhere, and makes sure every model and column has a description. Tedious work across many files, perfect for an agent.

**Scene 6 · Generate and open the docs site**

Then we generate the docs and open the site. Every model, column, test and query is there, with a lineage graph that matches the one in Rosetta.

**Scene 7 · Prompt card**

Now the project explains itself. In Ask mode, we ask the agent to trace the congestion fee from the source to every model that uses it. It reads the files and gives the path.

**Scene 8 · Prompt card**

Another good question before any join: what is the grain of the daily summary, and can we join it to trips without multiplying rows? One row per zone per day, so joining it to trips repeats rows. The agent should warn us.

**Scene 9 · How much CBD congestion fee was collected in January 2025, and where?**

And now the question the whole project was building towards. January twenty twenty-five was the first month of congestion pricing in New York. How much fee was collected, and where?

**Scene 10 · Prompt card**

We ask it in Rosetta's analytics, on top of our marts. Only valid trips count, and we see boroughs instead of IDs. Everything we built is inside this answer.

**Scene 11 · The answer**

Here is the answer on screen: the total fee collected in January, the share of valid trips that paid it, and the borough that collected the most. From raw files to a tested, documented answer.

**Scene 12 · Exposures**

The last block: exposures. An exposure tells dbt that something downstream depends on our models, like this analysis. If someone changes the fact table tomorrow, they see the analysis in the lineage.

**Scene 13 · Declare it**

The agent declares it: a name, a label, the type analysis, an owner, and the two marts it depends on.

**Scene 14 · The complete project**

And here is the complete project, every node built, with our analysis on the far right. From two Parquet files to this.

**Scene 15 · Section 12 done**

That is section twelve. Fully documented, a docs website, a project that explains itself, and a real answer, declared as an exposure. One short section left.

## Demo recording: prompting and changing files

**Set up before you hit record**

- Section 11 end state. Analytics page or Dive available in your release.

**Steps**

1. New chat, **Code** mode. Paste prompt 1. Review a few diffs, **Keep** all. *File:* `models/docs.md, *.yml`

   > Create models/docs.md with doc blocks for payment type, rate code and trip validity, and use them in every YAML that describes those columns. Make sure every model and column has a description.

2. Project menu → **dbt docs generate**, then **dbt docs serve**. Open `fct_trips` and its lineage.
3. New chat, **Ask** mode. Paste prompt 2.

   > Trace cbd_congestion_fee from the source to every model that uses it.

4. Same chat: paste prompt 3.

   > What is the grain of agg_zone_daily, and can I join it to fct_trips without fan-out?

5. Analytics page or Dive: paste prompt 4. Show the chart.

   > How much CBD congestion fee was collected in January 2025 by pickup borough, and what share of trips paid it?

6. Code mode: "Declare this analysis as an exposure in models/marts/_exposures.yml that depends on fct_trips and dim_zones." **Keep**. *File:* `models/marts/_exposures.yml`
7. Regenerate docs; show the exposure in the docs lineage and in Rosetta's lineage view.

**Optional lines to say over the recording**

- "The project explains itself."
- "And here is the answer."

**All prompts in this section, ready to paste**

1. Create models/docs.md with doc blocks for payment type, rate code and trip validity, and use them in every YAML that describes those columns. Make sure every model and column has a description.

2. Trace cbd_congestion_fee from the source to every model that uses it.

3. What is the grain of agg_zone_daily, and can I join it to fct_trips without fan-out?

4. How much CBD congestion fee was collected in January 2025 by pickup borough, and what share of trips paid it?
