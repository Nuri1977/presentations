# S07 · Packages, Jinja, macros & analyses: Google Vids script

**Import:** `s07-packages-jinja-macros.pptx` (speaker notes = the scripts below). **Voiceover:** 489 words, about 3.3 min at 150 wpm. **Demo recording budget:** about 6.2 min (Vids videos max 10 min).

**Scene order in Vids:** scenes 1 to 13 (slides) → your demo recording → scene 14 (recap). Drag the recap scene to the end after you add the recording.

## Voiceover, scene by scene

**Scene 1 · Packages, Jinja, macros & analyses**

Section seven. So far our SQL has been plain. Now we make it smarter: we install a package, use Jinja, write a macro, and meet analyses.

**Scene 2 · Taxi trips have no primary key.**

A real problem: taxi trips have no trip ID. Nothing identifies one trip. We need a primary key to test uniqueness, and later so an incremental model knows which rows to replace. We will build one from several columns.

**Scene 3 · Packages**

The packages page. A package is another dbt project you install into yours, usually for its macros and tests. You list packages in a YAML file and run dbt deps. The most used one is dbt utils, from dbt Labs.

**Scene 4 · Prompt card**

In the demo, the agent adds dbt utils with the latest compatible version and runs dbt deps. Afterwards we check the version on the dbt package hub ourselves. Version numbers are exactly what an AI can get slightly wrong.

**Scene 5 · packages.yml**

Three lines. Notice the version range: at least one point three, below two. We get fixes, but nothing that breaks us.

**Scene 6 · Prompt card**

Before using it, we understand it. In Ask mode: what does the surrogate key macro do, and which columns could identify a trip? It hashes several columns into one ID, and identical rows get the same key, which is how we will find duplicates.

**Scene 7 · Jinja in two minutes**

dbt models are SQL plus Jinja. Double curly braces print something, like ref and source. Curly brace and percent sign is logic: loops, ifs, and macros. Curly brace and hash is a comment. dbt renders the Jinja first, and the database only sees plain SQL.

**Scene 8 · Jinja and macros**

The Jinja and macros page. Jinja adds loops, variables and functions to SQL. A macro is a reusable function in the macros folder. And always check the compiled SQL to see what you produced.

**Scene 9 · By hand: our first macro**

Our own macro, safe divide. Remember the trips with zero distance? Fare per mile would divide by zero. This macro returns empty instead of an error, and every model can use it.

**Scene 10 · Before and after compiling**

On the left, how we call the macro in a model. On the right, what dbt compiles it into: a plain case expression. The database never sees Jinja.

**Scene 11 · Analyses**

Analyses are another block from the projects page. An analysis is a SQL file that dbt compiles but never runs, so no table is built. They are great for queries you want to keep in git, and for experimenting with Jinja.

**Scene 12 · By hand: a Jinja loop**

An analysis with a loop. For each payment type in the list, it writes one count column. Compile it, and the loop is replaced by real columns. But the list is hard-coded, which is not great.

**Scene 13 · Prompt card**

In the demo, the agent makes it data-driven. A dbt utils macro reads the payment types from the seed at compile time. Add a code to the CSV, and the SQL follows automatically.

**Scene 14 · Section 07 done**

That is section seven. A package with a version range, Jinja expressions and loops, our own macro, and an analysis. Next: we put it all together into intermediate and mart models.

## Demo recording: prompting and changing files

**Set up before you hit record**

- Section 06 end state.

**Steps**

1. New chat, **Code** mode. Paste prompt 1. **Allow** `dbt deps`. *File:* `packages.yml`

   > Add dbt-labs/dbt_utils to packages.yml, choosing the latest version compatible with my dbt version, and run dbt deps.

2. Open hub.getdbt.com/dbt-labs/dbt_utils and compare the latest version.
3. New chat, **Ask** mode. Paste prompt 2.

   > Explain what dbt_utils.generate_surrogate_key does, and which columns of stg_tlc__yellow_trips together could identify a trip. Don't write code.

4. Create `macros/safe_divide.sql` by hand. *File:* `macros/safe_divide.sql`
5. Create `analyses/payment_mix.sql` by hand with the `{% for p in [1, 2] %}` loop. Run `dbt compile --select payment_mix`, open the compiled file. *File:* `analyses/payment_mix.sql`
6. New chat, **Code** mode. Paste prompt 3. Compile again and compare. *File:* `analyses/payment_mix.sql`

   > Change analyses/payment_mix.sql so the list of payment types comes from the payment_types seed using dbt_utils.get_column_values instead of a hard-coded list. Compile it.


**Optional lines to say over the recording**

- "The database never sees Jinja, only the compiled SQL."

**All prompts in this section, ready to paste**

1. Add dbt-labs/dbt_utils to packages.yml, choosing the latest version compatible with my dbt version, and run dbt deps.

2. Explain what dbt_utils.generate_surrogate_key does, and which columns of stg_tlc__yellow_trips together could identify a trip. Don't write code.

3. Change analyses/payment_mix.sql so the list of payment types comes from the payment_types seed using dbt_utils.get_column_values instead of a hard-coded list. Compile it.
