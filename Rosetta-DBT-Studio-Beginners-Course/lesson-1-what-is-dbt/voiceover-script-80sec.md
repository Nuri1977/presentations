# What is dbt? - Voiceover

Slide 1 - Hook

If you work with data, you've got a folder of SQL files somewhere. And in your head, the order you're supposed to run them in.

That list in your head is the problem dbt solves.

Slide 2 - The core idea

dbt is built on one small idea. A model is just a SELECT statement.

You write the query. dbt creates the table.

That's it. There's no new language to learn. It's the SQL you already write.

Slide 3 - Running it

Then you run it. Every model you've written becomes a table, in a single command.

Slide 4 - Dependencies

But real work is queries built on other queries. Your summary reads from a clean table. That clean table reads from raw data.

So when one model points at another, dbt notices. It reads every reference and works out the build order itself.

That list you were keeping in your head? dbt just drew it for you.

And when you change one model, dbt already knows what else has to be rebuilt.

Slide 5 - Closing

That's dbt. A model is a SELECT, and dbt works out the order.

In the next video, we'll look at what you'll build across this course.
