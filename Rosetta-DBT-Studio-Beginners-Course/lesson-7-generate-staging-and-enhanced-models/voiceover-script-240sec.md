# Generate staging and enhanced models - Voiceover

Slide 1 - Intro

Your models folder is empty. Rosetta fills it in three passes, and each pass reads what the one before it wrote.

Nothing it writes is hidden from you. Every file that it produces is SQL that you could have written by hand.

Slide 2 - The Project menu

It all lives under the Project button.

The top three entries belong to Rosetta. Raw, staging, and enhanced, and they run in that order.

Slide 3 - Raw layer

Raw Layer goes first. It asks for an output folder, and nothing else.

Then it reads your database, and writes down what it finds. That takes a few seconds.

Slide 4 - What raw wrote

One file per table. And these are not models.

They are sources, which is dbt's word for a table that already existed, and that you did not build. Rosetta also puts a not null test on every column. That is a guess, and you are free to change it.

Slide 5 - Staging layer

Staging Layer comes next, and this one asks which tables you want.

It opens on the whole project, so you go into models, and then into raw. And there they are, the four files that raw wrote a moment ago. Tick the folder, and generate.

That list was exactly what the last pass produced, which is why these three run in order. Each one needs what the one before it made.

Slide 6 - What staging wrote

Now you have models. One for each table, and each one selects every column from its source, and nothing else.

It feels unnecessary right now, but this is the layer where renaming and cleaning will go, and having it here from the start gives that work somewhere to live.

Slide 7 - Enhanced layer

Incremental Layer comes last, and it works a bit differently. It writes models that process only new rows instead of rebuilding the whole table.

That needs a column that reliably tells you what is new, and only grades has one, a date on every row. So select only grades, and generate.

That gives you one model instead of four, in a folder called enhanced, and it is the one to look at closely.

Slide 8 - What enhanced wrote

Here is the part to watch.

Rosetta cannot know which column is your key, or which one marks new rows. So it leaves placeholders in capitals where they belong. Left alone, they are not valid SQL, and the model will break the second time that you run it.

Slide 9 - Fill them in

So you fill them in. The first placeholder is the unique key, the column that tells one row apart from another. For grades, that is the grade ID.

The second one is the column that moves forward in time, and it appears twice on the same line. That is the date recorded. It is what dbt looks at to work out which rows arrived since the last run.

Two edits, and the model is real. Save it, and the file is ready to run.

Slide 10 - Closing

Nine files generated, three terminal commands, and just two quick edits.

In just a few minutes, an empty project now has a complete staging and enhanced layer ready to go. The foundation is fully in place, so in the next lesson, we run them.
