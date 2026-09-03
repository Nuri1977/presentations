# Lesson 5 - Recording Cue Sheet

Clones the built in example project, so the viewer has something real on screen without any credentials, cloud account or database setup.

Full frame cards are `slides/1.png` (intro) and `slides/6.png` (closing), dropped in during editing, so nothing is performed for them.

App version: **1.6.3**, read off the installed exe and matched against the source. Everything below was checked on `dbt-studio` at `d082d076`, which is the 1.6.3 release merge, so the code and the app you are filming are the same build.

## Before you hit F9

- **No project created yet.** This lesson creates it, so start on the projects screen with an empty list. Verified clean as of 10 Aug 2026: no projects, no connections, and `C:\Users\Edon\rosetta-dbt-studio-projects\` is an empty folder. **Every test clone puts it back**, so run this teardown again after any dry run. Remove the project **in the app** and delete the folder from disk. Both, not one:
    - While a project named `dbtstudio_getting_started` is in the list, the app does not draw the Get Started button at all. It is conditional on that exact name being absent. A leftover project means the button you are about to click is not on screen.
    - If you remove it from the app but leave the folder, the clone fails, because git will not clone into a directory that already has files in it. The app then deletes that folder itself as failure cleanup, so a second click would succeed, but the take is spoiled by an error toast.
- **With an empty list, Get Started is on screen twice.** The header toolbar is always drawn, and the empty state renders underneath it, so you get Search, Get Started, Clone, Import and New across the top, plus a "No Projects found" card holding New Project and Get Started. Both Get Started buttons open the same dialog. Click the one in the card, since it sits next to New Project and makes the comparison slide 2's card is drawing.
- **Delete the leftover connection too.** Deleting the project does not delete the connection it created. A connection named "DBT Connection" survives, pointing at a DuckDB file that no longer exists, and a connections view filmed in that state shows a dead entry no real beginner would have. It is gone now, but it comes back with every clone, so clear it as part of the same teardown.
- The Welcome tour popup dismissed. Lesson 3 ends with it on screen, but by this lesson the viewer has moved on, and it would cover the Get Started button.
- Chrome and any other windows closed. Nothing here needs a browser.
- App maximized, taskbar auto-hidden, OBS windows hidden from capture.
- A working internet connection. This clones from GitHub, so it is the one lesson that fails offline.

## Beats

| Listen for | Do this |
|---|---|
| "On the projects screen, click Get Started" | Click **Get Started** |
| "It tells you what you are about to clone" | Hold on the dialog, let the list be readable |
| "The important part is the DuckDB database" | Point at the DuckDB Database row |
| "This clones the getting started repository from GitHub" | Stay on the dialog, cursor resting on **Create Example Project** |
| "Click Create Example Project" | Click it. The clone is instant, so the workspace arrives immediately |
| "And the project opens" | Already there. This line lands on the open workspace |
| "There is the database, one file in the rosetta folder" | Expand `rosetta/` so `university_sample.duckdb` is on screen. **Do not click it** |
| "What you do not have yet is models" | Expand `models`. The `.gitkeep` inside is expected, and the script is worded to survive it |

## What the dialog actually says

Title: **Get Started with RosettaDB**. Body: "Import our example project to quickly explore RosettaDB's capabilities. This project demonstrates best practices and includes sample data to help you get started."

Under **What's included** it lists four rows: DuckDB Database, Sample DBT Models, Example Analytics, and Best Practices. The action button reads **Create Example Project**, and changes to **Creating...** while it works.

It clones `https://github.com/rosettadb/dbtstudio_getting_started.git`.

Under the list the dialog says "This will open the clone dialog with the getting started repository URL pre-filled". **It does not.** The button clones straight away, so do not wait for a second dialog on the take. Second product accuracy issue for the same report.

After the clone the app deletes the `.git` folder, finds `dbt_project.yml`, reads the connection files in the repo and registers the connection for you. That is why the project is usable the moment it opens. All four steps are confirmed on the clone sitting on this machine: no `.git`, and a `duckdb` connection already written into the app's own store.

## What the clone actually contains

Checked on the real folder, not from the repo listing.

- `rosetta/university_sample.duckdb`, 1.3 MB. This is the database the script calls "just a file, sitting on your machine". It is the only data in the clone.
- `models/` holds one file, `.gitkeep`, and nothing else.
- `seeds/` is empty the same way. **Do not point at `seeds/` while saying "you have raw data"** - the raw data is inside the DuckDB file, not on disk as CSVs.
- `profiles.yml` and `rosetta/main.conf` both carry the full `C:\Users\Edon\...` path to the DuckDB file. Another reason to keep those two off camera.

## The file tree hides nothing

The tree builder applies no filter at all, so everything in the clone is visible.

- **`university_sample.duckdb` is safe to click**, though this lesson does not need to. An earlier version of this sheet said clicking it would dump binary into the editor. That was wrong. `getNonEditableFileMessage` in `src/renderer/helpers/utils.ts` catches `.duckdb` first and shows a short explanation instead. Lesson 6 makes proper use of that; here, expanding `rosetta/` so the file is visible is all slide 5 needs.
- **Do not open `profiles.yml`**, for the path reason above. Visible in the tree is fine.
- **`models/.gitkeep` will show.** Confirmed, not a maybe. The script was reworded for this: slide 5 now says the folder is there "with nothing written to it yet" rather than calling it empty, so expanding `models` and revealing the `.gitkeep` no longer contradicts the narration. Expand it as the beat says.

  Do not explain the `.gitkeep` on camera. It is a git artifact in a project Rosetta has just stripped git out of, and git does not arrive until lesson 22. It belongs in lesson 6.

**The narration deliberately does not repeat the dialog's list.** The dialog claims "Sample DBT Models: ready to run transformations", but `models/` is empty until lesson 7 generates them. Reading that claim aloud would contradict lesson 6, which points out the folder is empty, and lesson 7, which exists to fill it. The script names only the DuckDB database, which is genuinely there.

Worth reporting to the team as a product accuracy issue, separately from the course.

## Timing

**The clone is instant.** Measured on a real take, not estimated. The earlier worry that it might run long and need ramping was backwards, and the fix was the opposite one.

Slide 4 was reordered because of it. The aside about cloning from GitHub yourself now comes first and the click instruction comes last, so the click is the final beat of slide 4 and the workspace appears exactly as slide 5 starts. Previously the click came first and left four seconds of narration playing over an already-open project.

Do not try to stretch the gap in CapCut instead. The app routes through a loading screen that shows a logo, a spinner, and a **Navigate to Select Project** button. Holding or slowing it puts a stray button and a stalled spinner on screen in a beginner lesson.

Everything else is instant and under your control, so hold shots rather than rushing them.

## Known issue to avoid

The clone dialog and the workspace both show the project path under your user folder. Keep `C:\Users\Edon\...` out of frame where you can, and plan to mosaic where you cannot.

## Recording

F9, wait 3 seconds, start the Kokoro MP3 on your phone, perform the beats in sync. Let it run 3 seconds past the last word before F9 again.
