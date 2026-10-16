# Lineage and the build order - Voiceover

Slide 1 - Intro

dbt built your models in a particular order, and nobody told it what that order was.

The lineage graph is where you can watch it work that out.



Slide 2 - Where it lives

Lineage lives in the bottom panel, beside the terminal.

But it is not there yet. The tab only appears once you have a model open.

And it needs one more thing before it will draw anything. A manifest, which dbt writes when you run or compile the project.



Slide 3 - Why it needs a manifest

That last one catches people out.

The graph is not drawn from your SQL files. It is drawn from the manifest, which is the file that dbt writes while it compiles. No manifest, no graph.



Slide 4 - Reading it

Click the lineage tab, and you get the shape of the model you just opened straight away.

The source table on one side, your model on the other, and an arrow running between them.



Slide 5 - Where the arrow came from

That arrow is not configuration. You never declared it anywhere.

It is there because your model says source, and names the table. dbt read that one line and drew the conclusion.



Slide 6 - The deeper one

Now open the enhanced model instead.

It reads from a staging model, and that staging model reads from the source. So it sits two steps away from the raw data, rather than one.



Slide 7 - The depth control

Except at first you will only see one of those steps.

Depth starts at one, which means immediate neighbours and nothing else. Push it up to two, and the source appears behind it.



Slide 8 - Why the order was the order

And this is the whole explanation for the run that you watched earlier.

Four models with nothing between them, so they all went at once. One model waiting on another, so it went last, on its own.

Slide 9 - Why you will care later

It is a small graph today, and you could hold it in your head.

But this is the thing that tells you what you are about to break when you change a model. It is also the reason that you never write the build order down yourself.

Slide 10 - Closing

That is how dbt knows the order.

Next, what happens when you outgrow a database that lives in a single file.

