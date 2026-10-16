# Lesson 11 - Recording Cue Sheet

The payoff for lesson 8's line about dbt working out the build order. The point it has to land is that the graph is derived from `source()` and `ref()` and nothing else, that it comes from the manifest rather than from your SQL files, and that the shape of the graph is exactly why the run behaved the way it did.

Full frame cards are `slides/1.png` (intro) and `slides/10.png` (closing).

App version: **1.7.3**.

## Before you hit F9

- **Lesson 8 must have run and `target/` must still be there.** Without `target/manifest.json` the panel refuses to draw and shows "dbt Manifest Not Found" instead. That is the opposite of lesson 8, which needs `target/` deleted, so do not record these two back to back without running dbt in between.
- Bottom panel open. Start on the **Terminal** tab so switching to **LINEAGE** happens on camera.
- No file open. `models`, `enhanced`, `staging` and `target` already expanded in the explorer, with `main_students.sql`, `enh_main_grades.sql` and `manifest.json` all visible without scrolling. The **LINEAGE** tab does not exist until a `.sql` model is open, so with nothing open the bottom panel shows only TERMINAL and RUN HISTORY. The tab appearing is part of the take, and slide 2 is about exactly those two preconditions: a model, and a manifest, which dbt writes when you run or compile the project.
- Depth left at its default of **1**. Slide 7 changes it on camera.
- Dark theme, app maximized, taskbar auto-hidden.

## Beats

| Listen for | Do this |
|---|---|
| "Lineage lives in the bottom panel, beside the terminal" | Hold on the start screen. Point at the bottom panel, which shows only TERMINAL and RUN HISTORY |
| "The tab only appears once you have a model open" | Click `main_students.sql` in the explorer. The **LINEAGE** tab appears beside TERMINAL. Do not click it yet |
| "A manifest, which dbt writes when you run or compile the project" | Point at `manifest.json` in the explorer. Only point, do not open it: a non-`.sql` file hides the LINEAGE tab. Keep the cursor there through slide 3 |
| "Click the lineage tab, and you get the shape of the model you just opened straight away" | Click the **LINEAGE** tab, let the graph draw |
| "The source table on one side, your model on the other" | Point at each node, then the arrow |
| "It is there because your model says source, and names the table" | The model file is already open above the graph. Point at the `source('main', 'students')` on line 7, then back at the arrow |
| "Now open the enhanced model instead" | Open `enh_main_grades.sql` from `models/enhanced` |
| "Depth starts at one" | Point at the depth control, still on 1 |
| "Push it up to two, and the source appears behind it" | Change depth to **2**, let it redraw |
| "Four models with nothing between them" | Hold on the graph |
| "It is a small graph today" | Maximize the panel, let the whole thing sit |

## The real graph

Read straight out of `target/manifest.json`, so this is what should draw.

| Model | Reads from | Depth from raw |
|---|---|---|
| `main_courses` | source `courses` | 1 |
| `main_enrollments` | source `enrollments` | 1 |
| `main_grades` | source `grades` | 1 |
| `main_students` | source `students` | 1 |
| `enh_main_grades` | model `main_grades` | 2 |

Four parallel one-hop chains, and exactly one chain that goes two deep. Nothing else connects to anything.

The manifest holds **21 nodes**, being 5 models and 16 tests, plus **4 sources**. Schema version v12. The file is 638 KB.

## Why depth 1 looks wrong on the enhanced model

Select `enh_main_grades` at the default depth and you see `main_grades` and nothing else. The source is one step further back, so it is outside a depth of 1.

That is not a bug and it is worth showing rather than avoiding, because it is the single clearest demonstration of what the depth control is for. Slide 7 exists for this.

The options are 1, 2, 3 and 4. Default orientation is left to right.

## Card placement

**All eight cards sit at the top**, same as lesson 8 and for the same reason: the lineage graph lives in the bottom panel, which fills roughly the lower third. A bottom card would cover the graph the narration is describing.

All eight sit top right, in the blank editor area under the Project and Connect to Cloud buttons, so none of them cover the file tree on the left where `main_students.sql`, `manifest.json` and `enh_main_grades.sql` are clicked or pointed at.

## Timing

Everything is under your control. The graph redraws instantly at this size. The script runs about 157 seconds of speech against a 170 second budget.

The one thing not to rush is slide 7. Let the graph visibly redraw when depth changes from 1 to 2, because that redraw is the whole point of the slide.

## Recording

F9, wait 3 seconds, start the Kokoro MP3 on your phone, perform the beats in sync. Let it run 3 seconds past the last word before F9 again.
