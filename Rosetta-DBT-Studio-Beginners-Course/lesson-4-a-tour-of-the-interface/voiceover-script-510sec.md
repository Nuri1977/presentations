# A tour of the interface - Voiceover

Slide 1 - Intro

Rosetta DBT Studio does a lot, and none of it needs another program open.

So before we put anything into it, it is worth knowing what each part actually does.



Slide 2 - The sidebar

On the left is the sidebar. It is how you move between the parts of the app, and it is the one thing on screen that never changes.

Click the logo at the top and it widens into names. DBT Studio, which is your dbt projects. SQL Editor. Notebooks. Object Explorer. DataLake. Flows. And pinned at the bottom, Database Connections and Settings.

Collapse it again, and we work down that list, top to bottom.



Slide 3 - The projects screen

DBT Studio is where you land, and with nothing created yet, it is just this. Manage your projects.

Four ways in. Get Started clones a ready made example project that runs on a local file, so it asks you for no credentials. Clone pulls a dbt project from a Git repository. Import points at one already on your disk. New builds an empty one.

Up in the bar, Select Project switches between them once you have more than one. And Connect to Cloud links the app to a Rosetta Cloud account, which is what lets a project run in the cloud instead of on your own machine.



Slide 4 - The SQL Editor

SQL Editor is a query window on a database, and it needs no dbt project at all.

You pick the database in Select Connection, top left. And the plus, that is what you use to create a new connection.

It opens the full list of what Rosetta can connect to. Choose a type, and you get the form for that one.

Once connected, the three tabs fill up. Data is the schema, your tables and their columns. Queries is the ones that you saved.

Analytics turns results into pages. Two buttons up there: Create Page makes a new one, and Build Static Site exports them all into a website folder that you can host anywhere.

Top right, that icon opens the AI, which will write the query for you once you have given it a provider to talk to.



Slide 5 - Notebooks

Notebooks has the same connection picker and the same empty state, so a notebook needs a database first too.

What differs is the shape. A notebook splits the work into cells, one query each, every cell keeping its own result, with room for notes in between. It saves, so you can come back and run any cell again.



Slide 6 - Object Explorer

Object Explorer. The screen calls itself Cloud Explorer, but it is the same thing.

This one is for data that is not in a database at all, just files in cloud storage. The dashboard counts your connections, your storage types, and what you opened recently, all zero, because we have added nothing.



Slide 7 - Sources and New Source

Sources lists the cloud storage you have connected. None yet, so it offers New Source.

New Source starts with the connection type, which is the list of everything Rosetta can read.

Pick one and the form underneath changes to whatever that provider asks for. Give it a name, fill in what it needs, and then Test Connection checks that it actually works before Save Connection puts it in the list.



Slide 8 - Recent Items

Recent Items is the third tab, a shortcut back to the files that you already opened.



Slide 9 - DataLake

DataLake is the step after that. Once your files are in cloud storage, this turns them into real tables that you can query, without loading them into a database first.

The dashboard follows the same pattern. How many lakes you have, of which kind, and what you have been running.



Slide 10 - DataLakes and Query History

DataLakes, on the left, lists the instances that you have built. None yet.

Query History under it is coming soon.



Slide 11 - Creating a DataLake

New DataLake is where one gets made. Four types offered, three of them still marked Soon, so DuckLake it is.

That opens a five step wizard. Instance details, storage, the catalog, runtime options, and a final review. Name it, describe it, and Next walks you through the rest.

Nothing gets created until you reach the end of the review.



Slide 12 - Flows

The Flows screen is empty because FlowFile does not come installed with Rosetta DBT Studio. It is a sizeable component, and leaving it out saves disk space.

It has to be installed before you can use it, and that happens in Settings, in a single click.

What it does is ETL, visually. Extract data, transform it, load it somewhere, by connecting nodes into a graph rather than writing code.

And ETL stops being something you have to leave the app in order to do.



Slide 13 - Database Connections

Down at the bottom of the sidebar.

Database Connections is the one list that holds both, every database and every cloud source you have registered.

New Connection and Add Cloud Source lead to the two screens we have already seen.



Slide 14 - Settings, General

And Settings.

General holds your projects directory, which is where every project that you make gets written. Under it, the version you are on, a button to check for updates, and the system information, which is the part to copy when you report a bug.



Slide 15 - Settings, the rest

Then four more.

AI Settings is where an AI provider goes. That can be a paid service, or a model running locally on your own machine, which costs nothing.

Rosetta Cloud signs you in, by OAuth or an API key.

Keystore holds credentials, encrypted by the operating system and grouped into environments, so a password never has to sit in your project files.

And Task Manager tracks long jobs that keep running while you work somewhere else.



Slide 16 - Settings, plugins

Below that, Plugins.

dbt Core, Rosetta CLI and DuckDB are in this list because Rosetta installed them for you. Those are the same versions that you can read in the status bar right now.

Flowfile is in the same list, and that is the install button from earlier. About is the version and the licence. And at the very bottom, the theme.



Slide 17 - Closing

That is every part of the app, named.

Next time we stop looking and start building. We create the example project, and by the end of it you will have a real dbt project open on your screen.

