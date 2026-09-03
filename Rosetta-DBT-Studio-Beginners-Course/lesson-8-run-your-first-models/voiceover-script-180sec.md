# Run your first models - Voiceover

Slide 1 - Intro

Your models folder is full, but none of it has run. Those nine files are still just text, and your database has not changed.

dbt run is the step that changes that. It turns them into tables and views that you can query.

Slide 2 - Where Run lives

Open the Project menu and Run is right there, a few entries below the ones that generated your models.

Everything under the three Rosetta entries is standard dbt. Clicking Run is the same as typing dbt run in the terminal.

Slide 3 - What it actually does

dbt reads every model, works out the order, and turns each one into ordinary SQL.

Then it sends that SQL to your database and asks it to build the result.

Slide 4 - The first run is the slow one

Watch the two lines about parsing. dbt has to read the entire project before it can do anything.

That happens once. Every run after this reuses what it learned, which is why the first one always feels slower than it should.

Slide 5 - Reading the terminal

Each model got a start line, a finish line, and how long it took.

The line that matters is the last one. Completed successfully, and five passed out of five. Every model built, nothing skipped.

Slide 6 - Views and tables

Look at the labels. Four are view models. One is incremental.

A view stores no rows. It is a saved query that runs when you ask for it. The incremental one has to be a real table, because it needs to remember what it already has.

Slide 7 - Where it landed

Nothing moved. Your database file is still one file, in the same folder.

It just has more in it than it did a minute ago. The original four tables are untouched, and your models sit beside them.

Slide 8 - The target folder

Refresh the file tree, and the folders logs and target appear.

dbt made both, and neither is yours to maintain. Target is what makes the next run quick, so deleting it just means sitting through that slow first parse again.

Slide 9 - Run History

And the run is remembered. Run History, next to the terminal, gives every dbt command a row, with what passed, what failed, and how long it took.

Open it up and you get every model inside it. That matters far more the day something breaks than it does today.

Slide 10 - Closing

Your models are built.

Next, we go and look at what is actually in them.
