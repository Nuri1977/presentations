# Lesson 10 - Recording Cue Sheet

Notebooks, as the counterpart to lesson 9's editor. The points it has to land: a notebook keeps SQL, Python and notes together, each cell keeps its own answer, a SQL result comes back as `df` that a code cell can use, and the notebook saves itself.

Full frame cards are `slides/1.png` (intro) and `slides/10.png` (closing).

App version: **1.7.2**.

## Before you hit F9

* **Lesson 8 must have run**, since the queries read the models.
* **A Python version must already be installed.** Otherwise the Create window downloads one on camera. Make a throwaway notebook first if you are not sure, then delete it.
* **pandas must NOT be installed** in the notebook you record with. The install is part of the demo, on slide 5.
* **Delete every test notebook** for `DBT Connection`, including any old SQL ones, so the list starts empty and no deprecation bar appears.
* Dark theme, app maximized, taskbar auto-hidden.

## Beats

|Slide|Listen for|Do this|
|-|-|-|
|2|"From the Select Connection dropdown"|Open **Select Connection** and pick `DBT Connection`. If it is already selected, just point at it|
|3|"Click the plus to see the options"|**+** beside the notebook search box. Rest on the three items: **Add New Notebook**, **Import Notebooks (JSON)**, **Import Jupyter Notebook (.ipynb)**|
|3|"We'll create a new one and call it University"|**Add New Notebook**, name it `University`, leave the Python version as it is, **Create**. It opens while **Preparing environment…** shows in the kernel bar|
|3|"Rosetta is creating a separate Python environment"|Stay on the **Preparing environment…** bar. Nothing to click|
|4|"The toolbar lets you run all the cells…"|Move left to right along the kernel bar: **Run all cells**, **Interrupt kernel**, **Restart kernel**, **Packages (pip)**|
|4|"Then clear all outputs"|Keep going: **Clear all outputs** (do not press), **Collapse all cells**, **Compact view / Wide view**|
|4|"the three dots for the notebook actions menu"|Open **⋮**: **Rename**, **Duplicate**, **Export as .ipynb**, **Change Python version…**, **Shut down kernel** (greyed out), **Delete notebook**. Close it without choosing|
|4|"drag the handle on the left to move it"|Hover the drag handle at the top left of the cell. Do not drag it|
|4|"use the arrow to hide or show its code"|Click the arrow under the handle: **Hide code**, then **Show code**|
|4|"open its menu to duplicate it, convert it"|Open the cell **⋮**: **Duplicate cell**, **Convert to SQL**, **Convert to Text**, **Run and insert below**. Close it without choosing|
|4|"I'll switch this cell to SQL"|On the starter Code cell use **Convert to SQL** and type the first query. Do not press ▶ until **Preparing environment…** has gone: Run is refused with a warning until then. The first run then waits for the kernel to start|
|5|"Let's install pandas now"|Click **Install pandas** in the notice itself, not Packages (pip). The app reruns this cell by itself when the install finishes|
|5|"we can view the results as HTML"|While it installs, click the table toggle at the top of the result (tooltip **Show as HTML**), then click it again (tooltip **Show as interactive table**)|
|5|"From the output menu"|Open the output **⋮**: **Copy cell output**, **Clear output**, full screen. Close it again|
|5|"Without pandas, df is a list of dictionaries"|Point at the notice text while the install finishes|
|5|"Once pandas finishes installing"|Wait for the rerun. The notice disappears and `df` is a DataFrame|
|6|"Now I'll add a Code cell and use df"|**+ Code** (hover the divider under the cell), type `df\\\\\\\["students"].sum()`, run. It returns **100**|
|7|"I'll count enrollments by semester"|**+ SQL**, type the second query, change **Result as** to `enrollments`, run|
|8|"Now I'll add a Text cell"|**+ Text**, write one sentence about what the numbers showed|
|9|"Every change is saved as you go"|Point at the notebook in the sidebar. There is no save button to press|
|9|"if you want to share it, you can use Export as .ipynb"|**⋮** in the kernel bar, **Export as .ipynb**, then **Cancel** the save window|
|10|"That is a notebook"|Sit on the finished notebook|

## The environment wait

Measured by Edon on 14 Oct 2026: **46 seconds** of **Preparing environment…** after Create.

* **Greyed out while it prepares:** Run all cells, Restart kernel, Packages (pip). Pointing at them during the toolbar tour is fine. Pressing ▶ on a cell only raises "The environment is still being created."
* **Works while it prepares:** converting the cell to SQL and typing the query.
* **So do it in this order:** Create, the toolbar tour, Convert to SQL, type the query, and only then ▶.
* **How much the voice gives you:** from "It opens right away" (about 0:30) to the first Run (about 1:19) is roughly 49 seconds of speech, against a 46 second wait. The wait is covered, with only about 3 seconds to spare, so start typing the query as soon as the toolbar tour ends. The voice explains the environment, then walks the toolbar and the cell controls while you wait.
* **Second wait, not measured:** the first ▶ starts the kernel. The script already says it needs a moment. Time it.

## The cells, in order

**1. SQL cell** (converted from the starter Code cell), Result as `df`:



select major, count(\*) as students
from main\_students
group by major
order by students desc



**2. Code cell:**



df\["students"].sum()



**3. SQL cell**, Result as `enrollments`:



select semester, count(\*) as enrollments
from main\_enrollments
group by semester
order by semester



**4. Text cell**, one sentence, something like:



\*\*Physics and Maths\*\* have the most students, and Spring is the busiest semester.



## Verified numbers

Run against the real database on 14 Oct 2026, after lesson 8's build.

* SQL cell 1: Physics 29, Mathematics 28, Computer Science 24, Literature 19.
* Code cell: those four add up to **100**.
* SQL cell 3: Fall 2023 27, Spring 2024 39, Summer 2024 34.

SQL cell 1 is the same query as lesson 9, on purpose: the notebook starts from an answer the viewer already knows.

## Things not to show

* **Packages (pip) for the pandas install.** That dialog installs but reruns nothing, and the narration says the query reruns itself. Only the **Install pandas** button in the cell output does that.
* **An old SQL notebook.** It carries a deprecation bar across the top.
* **The Python interpreter download.** Have one installed before the take.
* **Two cells both called `df`.** The second SQL cell would overwrite the first one's result. Rename it to `enrollments`.

## Where the add-cell buttons are

Since the 1.7.2 build, the divider between two cells shows a small **+** that opens **+ Code / + SQL / + Text** when you hover it. The always-visible row of three sits at the end of the notebook. Hover deliberately so the buttons are on screen before you click.

## Card placement

**All eight cards sit bottom left.** Lesson 4 established from real footage that this screen opens the AI panel on the right, and a right hand card is covered by it.

## Timing

The script runs about **2:21** at the pace Edon measured on an earlier version (1:58, about 3.2 words a second), so this total is an estimate. Re-time it when the new voiceover is made.

Waits measured by Edon on 14 Oct 2026: **46 seconds** for the environment, **26 seconds** for the pandas install.

Approximate times in the voiceover, assuming an even pace (give or take a few seconds):

* about 0:26 "It opens right away while its Python environment gets set up", then the environment explanation. Voice until the first Run: about 49 seconds, against the 46 second wait
* about 0:40 the toolbar, left to right, then the three dots
* about 0:57 the drag handle, hide code, the cell menu
* about 1:10 "I'll switch this cell to SQL" and typing the query
* about 1:15 "The first time we run it, the notebook needs a moment to start its kernel"
* about 1:23 "Let's install pandas now". Voice until the DataFrame line: about 26 seconds, against the 26 second install
* about 1:49 "Now I'll add a Code cell and use df to add up the student counts"

The kernel start is still unmeasured. `sounds/sound.mp4` in this folder is the old 2:04 voiceover, so it no longer matches: replace it with the new one.

**Length:** the single track is 2,486 characters, 14 under the 2,500 a Vids voiceover allows.

## Recording

F9, wait 3 seconds, start the voiceover audio on your phone, perform the beats in sync. Let it run 3 seconds past the last word before F9 again.

