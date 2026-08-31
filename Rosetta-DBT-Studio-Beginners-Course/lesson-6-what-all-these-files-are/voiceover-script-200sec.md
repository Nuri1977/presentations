# What all these files are - Voiceover

Slide 1 - Intro

Your new project is mostly empty folders. That is not a mistake, it is how a dbt project starts.

Here is what each one is for, and which ones you will actually touch.

Slide 2 - The project file

Start with the dbt project file.

This is what turns an ordinary folder into a dbt project. dbt looks for it, and without it nothing runs. It names the project, and it tells dbt which folder holds what.

Slide 3 - The connection

Next, the profiles file. This one is the connection.

It says the type is DuckDB, and it points at a file on your disk. Rosetta wrote it when it created the project, so the path is already correct for this machine.

Slide 4 - Models

models is where your SQL lives, and right now it is empty.

That single file inside is just a placeholder, so the folder can exist before anything is in it. You will see one in most of these folders, and you can ignore all of them.

Every file that you put in here is one model, and a model is one SELECT statement. dbt runs it, and saves the result in your database as a table or a view.

Slide 5 - Seeds

seeds is for CSV files.

Drop one in, and dbt loads it into the database as a table. It is meant for small reference data that does not come from a source system, such as a list of country codes, or a mapping of product categories.

Slide 6 - The optional folders

analysis, macros, snapshots and tests are all empty, and all optional.

analysis holds SQL that you want dbt to compile, but not build into a table. macros holds SQL that you do not want to write twice. snapshots records how a row changed over time. And tests holds your own checks, like this column should never be null.

Slide 7 - The rosetta folder

The rosetta folder is not a dbt folder. None of the paths in the project file point at it. The app made this one, for itself.

It keeps a second copy of the connection, in the format that Rosetta needs. And sitting beside it is the database itself. The whole thing is one file, about a megabyte, with the sample data already inside.

Click it, and Rosetta tells you what it is. A database file, not a text file. You never edit this one by hand. Everything you do to it happens through SQL.

Slide 8 - What is missing

Two things are missing on purpose.

There is no target folder yet. dbt creates that the first time it runs, and fills it with the SQL that it compiled. And there is no git folder, because Rosetta removed it after cloning. This is your project now, not a copy of someone else's.

Slide 9 - Where you will work

Out of all of this, the folder you actually work in is models.

The rest is either configuration that you set once, or folders that you may never open.

Slide 10 - Closing

That is the whole layout.

Next, we fill that empty models folder.
