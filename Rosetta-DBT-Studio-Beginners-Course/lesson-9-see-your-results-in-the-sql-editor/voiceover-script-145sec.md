# See your results in the SQL Editor - Voiceover

Slide 1 - Intro

Your models exist now, but so far you have only seen them as lines in the terminal.

The SQL Editor is where you look at what is actually in them.



Slide 2 - It wants a connection

One thing to get straight first.

The SQL Editor does not care about your dbt project. It talks to a database. So what it asks for is a connection, and you already have one, because cloning the example registered it for you.



Slide 3 - The Data tab

The Data tab is the database, laid out.

And there is more in it than there was an hour ago. Your four original tables, and sitting beside them, everything that dbt built.



Slide 4 - Ask it something

Now ask it a question. This one counts students by major.

Notice where it reads from. That is the staging model, not the raw table underneath it.



Slide 5 - The answer

Run it, and the rows come back underneath.

Four majors, and the counts add up to the hundred students that are in the table.

Switch it to Chart, and it already knows which column goes where. There are other chart types to choose from as well.



Slide 6 - What a view really is

Here is the part worth stopping on. That model is a view, and a view stores no rows at all.

When you asked, the database ran the model's SQL and then answered you. That is why building it took about a quarter of a second, and why it can never be out of date.



Slide 7 - Keep it

If it is a query that you will want again, save it.

Saved queries belong to the connection, so they are still there the next time you open this database.



Slide 8 - And if you do not

And if you do not save it, it is not gone either. The editor keeps a history of what you ran.



Slide 9 - Closing

That is one query at a time.

Next, notebooks, which is the same idea broken into pieces.

