# Notebooks - Voiceover

Slide 1 - Intro

In the SQL Editor, we ran one query at a time. In a notebook, we can build on that work step by step, keeping SQL, Python, and notes together.

Slide 2 - It starts the same way

From the Select Connection dropdown, choose DBT Connection, if it isn’t selected. Notebooks are linked to a connection, so switching to another one won’t lose them.

Slide 3 - Make one

Click the plus. You can create a new notebook, or import one from a JSON file or a Jupyter notebook. We’ll create a new one and call it University. It opens right away while its Python environment gets set up. Rosetta is creating a separate Python environment just for this notebook and installing the kernel into it. That is why it takes a moment, and why anything you in stall here stays out of your other notebooks.

Slide 4 - The cell

The toolbar lets you run all the cells, interrupt or restart the kernel, and install or manage packages for this notebook. Then clear all outputs, which empties every answer but keeps your code, collapse all the cells, the view button for compact or wide, and the three dots for the notebook actions menu. On each cell, drag the handle on the left to move it, use the arrow to hide or show its code, and open its menu to duplicate it, convert it to SQL or Text, or run it and add a new cell below. I’ll switch this cell to SQL and enter a query that counts students by major. The first time we run it, the notebook needs a moment to start its kernel. Once it’s ready, the query runs and the results appear below.

Slide 5 - Your answer is a thing you can use

Let’s install pandas now. pandas is the Python library that turns query results into tables you can filter and calculate on. While it installs, we can view the results as HTML, then click to browse an interactive table. From the output menu, we can copy the output, clear it, or open it full screen. Without pandas, df is a list of dictionaries. A DataFrame is a table, like a spreadsheet. Once pandas finishes installing, Rosetta reruns the query, and df becomes a DataFrame.

Slide 6 - Add another

Now I’ll add a Code cell and use df to add up the student counts. The result is 100, all the students.

Slide 7 — Another query

Next, I’ll count enrollments by semester to see which one is the busiest.

Slide 8 — Not everything is a query

Now I’ll add a Text cell to leave a note about what we found. That way, later, we’ll remember what we were looking at and why.

Slide 9 — It keeps itself

Every change is saved as you go, and if you want to share it, you can use Export as .ipynb, which gives you a standard Jupyter file.

Slide 10 — Closing

That is a notebook: your queries, answers, and notes in one place. Next, see how dbt worked out the build order in the lineage graph.

