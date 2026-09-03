# Lesson 6 - Recording Cue Sheet

A walk through the project that lesson 5 created. No clicking anything that changes state, just the file tree and two files opened read only. The point it has to land is that most of the folders are empty on purpose, and only one of them is yours to fill.

Full frame cards are `slides/1.png` (intro) and `slides/10.png` (closing), dropped in during editing, so nothing is performed for them.

App version: **1.6.3**, read off the installed exe and matched against the source at `d082d076`.

## Before you hit F9

- **The example project has to exist and be open.** Lesson 5 ends here, so continuity is right if you record straight after it. As of 10 Aug 2026 it is **not** on disk, since it was torn down to get lesson 5's beginner state, so re-clone it through Get Started before you record this one.
- **`models/` must still be empty.** If you have already generated models while testing lesson 7, delete them, or delete the project and clone it again from Get Started.
- **Nothing generated on disk.** Five things appear once you run dbt or Rosetta, and all five contradict this lesson if they are on screen. Delete every one of them before recording: `target/`, `logs/`, `.user.yml`, `rosetta/dbtstudio_getting_started/`, and anything under `models/`. The first three are dbt's, the fourth is Rosetta's workspace, all confirmed by running both.
- File tree collapsed to the top level. Nothing pre-expanded, so each expand happens on camera.
- Dark theme. Lesson 0's footage is dark and the cards are built for dark.
- App maximized, taskbar auto-hidden, OBS windows hidden from capture.
- No internet needed. Everything here is on disk.

## What you touch, in order

| # | Slide | Item | Action |
|---|---|---|---|
| 1 | 2 | `dbt_project.yml` | **Open.** Scroll so `name:` and the path settings are both visible |
| 2 | 3 | `profiles.yml` | **Open.** Point at `type: duckdb` |
| 3 | 4 | `models` | Expand, leave the `.gitkeep` showing |
| 4 | 5 | `seeds` | Expand |
| 5 | 6 | `analysis` then `macros` then `snapshots` then `tests` | Select each, one per name |
| 6 | 7 | `rosetta` | Expand |
| 7 | 7 | `university_sample.duckdb` | **Open.** Hold on the warning message |
| 8 | 9 | `models` | Select again, to close on it |

Three files open in the editor. Everything else is selection in the tree.

**The lesson order fights the tree order.** The tree is alphabetical, so this path runs 3rd item, 5th, 1st, 2nd, 6th, 7th, 4th, then back to 3rd. You go down, jump to the top, come back down, then up again. That is deliberate: `models` comes first because it is the one that matters, and `rosetta` comes late because it is not dbt's. The viewer follows the selection highlight, not the geography. Expect the jumping so it does not surprise you mid-take.

## Beats

| Listen for | Do this |
|---|---|
| "Start with the dbt project file" | Click `dbt_project.yml`, let it open in the editor |
| "It names the project, and it tells dbt which folder holds what" | Scroll so `name:` and the path settings are both on screen |
| "Next, the profiles file" | Open `profiles.yml` |
| "It says the type is DuckDB" | Point at the `type: duckdb` line |
| "models is where your SQL lives" | Select `models` and expand it |
| "That single file inside is just a placeholder" | Let the `.gitkeep` sit there. This is the line that explains it, so hold |
| "seeds is for CSV files" | Select `seeds` |
| "analysis, macros, snapshots and tests are all empty" | Move straight down the tree, one folder per name. This is alphabetical order, so you never jump back up |
| "The rosetta folder is not a dbt folder" | Expand `rosetta` |
| "And sitting beside it is the database itself" | Point at `university_sample.duckdb` |
| "Click it, and Rosetta tells you what it is" | Click it. The app refuses to open it as text and explains why. Hold so the message is readable |
| "There is no target folder yet" | Hold on the tree, so the absence reads |
| "The rest is either configuration" | Land back on `models` |

## What is actually in the project

Verified on disk, not from the README.

| Item | Contents |
|---|---|
| `dbt_project.yml` | 21 lines. name, version, config-version, profile, and the six path settings |
| `profiles.yml` | 9 lines. `type: duckdb`, an absolute path to the database, `schema: main`, `threads: 4` |
| `README.md` | The repository readme, 4 KB |
| `models/` | One `.gitkeep`, nothing else |
| `seeds/` | One `.gitkeep`, nothing else |
| `macros/` | One `.gitkeep`, nothing else |
| `tests/` | One `.gitkeep`, nothing else |
| `snapshots/` | One `.gitkeep`, nothing else |
| `analysis/` | One `.gitkeep`, nothing else |
| `rosetta/` | `main.conf` and `university_sample.duckdb` |

Seven folders, three files. Six of the seven hold nothing but a placeholder. `rosetta` is the only one with real content.

## Every "empty" folder shows a file

The file tree filters nothing. `getDirectoryStructure` in `src/main/utils/fileHelper.ts` returns every entry, so the `.gitkeep` in each of those six folders is on screen the moment you expand it.

This is not avoidable and not a bug: **git cannot store an empty directory**, so a folder that ships in the clone has to contain something. Verified on camera in the app: all six of `analysis`, `macros`, `models`, `seeds`, `snapshots` and `tests` show exactly one `.gitkeep` when expanded, and nothing else.

## Clicking the database is safe, and worth doing

`university_sample.duckdb` does **not** open as garbage. `getNonEditableFileMessage` in `src/renderer/helpers/utils.ts` special-cases `.duckdb` before anything tries to read it, and the editor shows a short explanation instead: that it is a DuckDB database file, that it cannot be edited as text, that database files should be reached through queries and tools, and that editing it as text could corrupt it.

That message is a better teaching moment than pointing at the filename, which is why slide 7 now clicks it. Nothing is modified by opening it.

**It prints your full path.** The message is supposed to show just the file name, but it builds it with `filePath.split('/').pop()`, and Windows paths use backslashes, so the split does nothing and the whole `C:\Users\Edon\...` path lands on screen. Mosaic it. It is also a real bug worth sending to the team with the other two.

Slide 4 now handles it out loud, on the first folder you expand, so that every later use of "empty" reads as shorthand the viewer has already been taught. Do not skip that line, and do not expand `models` before it.

The explanation deliberately avoids the words git and repository. Git does not arrive until lesson 22, and slide 8 only has to say the folder is gone, not what it was.

The database is 1,323,008 bytes, so 1.3 MB, and holds four tables in schema `main`: `students`, `courses`, `enrollments` and `grades`. **100 rows each**, columns exactly as the README describes. Confirmed by querying the file directly.

## Two things the narration says are missing

Both are true and both are worth showing rather than telling.

`target/` does not exist yet. dbt creates it on the first run and fills it with compiled SQL, so it belongs to lesson 8, not this one.

`.git` does not exist either. Rosetta deletes it after cloning the example, in `git.service.ts`, because the Get Started flow passes `removeGit: true`. That is deliberate, so the example becomes the viewer's project rather than a checkout of someone else's.

## Product issue to report

`dbt_project.yml` sets `analysis-paths: [analyses]`, but the folder that ships in the repo is called `analysis`. The names do not match. Nothing breaks, because the project has no analyses in it, but a beginner who opens both files sees two different names for the same thing.

Separate from the course, worth sending to the team with the Get Started dialog wording from lesson 5.

## Overlay card placement

All eight cards sit **bottom right**, because every action in this lesson happens in the file tree on the left, and the two files you open are short enough that the lower half of the editor is empty.

Cards 1 and 2 used to sit top right. They were moved down so all eight land in the same place, which means one position to check against your footage instead of two, and no card jumping across the frame between slides 3 and 4.

This placement is a best guess made before any footage exists. Send me a frame from the take and I will measure it properly and re-render anything that lands badly.

**Cards 1 and 2 have to be up while the sentence that needs them is playing.** The narration never speaks a filename anywhere in this lesson, by design, so "the dbt project file" and "the profiles file" are resolved only by the card and by what you click. Fade card 1 in on "Start with the dbt project file", not after it. A card that arrives late leaves the viewer scanning the tree for a folder called dbt, which is the wrong impression to create in the first twenty seconds.

## Timing

Nothing here is timed by the app, so every beat is under your control. Hold shots rather than rushing them. The script runs about 190 seconds of speech, and the slide budget is 200, so there is room.

## Known issue to avoid

`profiles.yml` shows the absolute path, so `C:\Users\Edon\...` will be on screen when you open it. It is the whole point of the slide, so you cannot cut around it. Plan to mosaic the user folder in the edit.

## Recording

F9, wait 3 seconds, start the Kokoro MP3 on your phone, perform the beats in sync. Let it run 3 seconds past the last word before F9 again.
