# Local dbt vs Rosetta DBT Studio - Voiceover

Slide 1 - Hook

Today we're comparing two ways to work on a dbt project, both of them on your own machine. VS Code with the dbt extensions, against Rosetta DBT Studio, and neither one costs anything. Same Postgres database running locally, fourteen tables in it, and the same dbt project already written. So it comes down to one thing: what each one asks of you before you can open that project and start working.

Slide 2 - What each one needs

If you've set dbt up locally before, you know how this goes. Python, then a virtual environment you have to reactivate every session, then dbt and the Postgres adapter installed into it. The project brings its models and its config, but not your credentials, so you write a profiles file by hand into a hidden folder in your home directory. Then dbt debug, which tells you there is no project here if you forgot to change directory first. And you still haven't opened the editor. Seven steps before you see the project. Rosetta DBT Studio is a download. You point it at the project folder, or a zip, and it imports the whole thing. Then you fill in the connection form. There's no virtual environment to make, because it brings its own Python, and installs dbt and its adapters for you.

Slide 3 - From schema to models

That's setup out of the way. Now those fourteen tables need staging models. There are two ways to do that on the dbt side. The codegen package prints the code to your terminal, one table at a time, for you to paste into a file. Power User is nicer about it, and generates a model straight from a source with a click. But both of them handle one table per call, so fourteen tables still means fourteen passes. In Rosetta DBT Studio it's two commands, raw layer then staging layer. Both write the files for you, and both finish in about a second.

Slide 4 - Who runs the AI

Both setups have an AI assistant, and they're not really the same kind of thing. Power User's AI runs on Altimate's service, which means your schema goes off to their cloud to be read. Rosetta DBT Studio lets you pick, and the list reads top down. OpenAI, Claude, Gemini. Then Ollama and LM Studio, which both run on your own hardware. And at the bottom, OpenAI Compatible, which ships a list of eight more with the URLs ready to copy, OpenRouter, Groq and DeepSeek among them.

Slide 5 - What else is in the box

And the editor isn't the whole tool. Power User covers more ground here than you might expect. Query previews, column level lineage, and it even has notebooks, right inside VS Code. Where it stops is storage. There's no object explorer for S3, Google Cloud Storage or Azure, no data lake support, and no pipelines you can actually run. Rosetta DBT Studio has all three, and they turn up in the same download.

Slide 6 - Closing

Rosetta DBT Studio is free, open source, and it runs on your machine, right next to the database it's reading. No virtual environment, nothing to install into it, and no profiles file to write by hand. If any of that sounds useful, a star on GitHub helps other people find it.
