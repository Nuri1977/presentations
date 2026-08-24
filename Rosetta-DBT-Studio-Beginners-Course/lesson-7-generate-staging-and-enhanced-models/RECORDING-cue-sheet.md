# Lesson 7 - Recording Cue Sheet

Rosetta fills the empty models folder in three passes: raw, staging, enhanced. The point it has to land is that the generated files are ordinary SQL, that the order is forced because each pass reads the last one's output, and that the enhanced layer comes out unfinished and has to be completed by hand.

Full frame cards are `slides/1.png` (intro) and `slides/10.png` (closing).

App version: **1.6.3**, read off the installed exe. Rosetta CLI 2.10.0.

## The Windows launcher was broken. It is fixed on this machine.

**The three Rosetta layer buttons did not work on this Windows install.** The launcher script they call was corrupted. It has been repaired, verified, and this lesson is recordable now. Read the rest of this section anyway, because the fix is local and the team still needs to ship it.

**Re-verified 12 Aug 2026**, after the app was updated to 1.6.3. The repair survived, because the CLI at `C:\rosetta\` is a separate install from the app in `AppData\Local\Programs`, so updating the app does not touch it. Confirmed by running the extensionless path the app actually spawns, which returned `2.10.0` and exit 0. Re-check this before the shoot if the **CLI** is ever reinstalled; an app update alone is not a threat to it.

`C:\rosetta\rosetta-2.10.0-win_x64\rosetta-2.10.0-win_x64\bin\rosetta.bat` is truncated at line 18, where it reads `set DEFAULT_JVM_OPTS=drivers"`. Everything that should follow, the `APP_HOME` resolution, `JAVA_EXE`, `CLASSPATH` and `CMD_LINE_ARGS`, is missing. Running it produces:

```
'drivers"    -Djdk.tls.client.protocols=TLSv1.2  -classpath  com.adaptivescale.rosetta.cli.Main ' is not recognized as an internal or external command
```

The app cannot avoid it. `utils.ts:377` builds `cd "<project>\rosetta" && "<rosettaPath>" dbt-next extract ...`, `settings.service.ts:276` sets `rosettaPath` to `bin\rosetta` with **no extension**, and `cli.adapter.ts:36` spawns with `shell: true`, which on Windows is `cmd.exe`. cmd resolves the extensionless path through PATHEXT and lands on the broken `.bat`.

So Raw Layer, Staging Layer and Incremental/Enhanced Layer all failed on Windows.

**What was done.** The original file is kept beside it as `rosetta.bat.broken-backup`. The replacement restores what the truncation removed: `APP_HOME`, `JAVA_EXE` pointing at the bundled JRE in the same `bin` folder, `CLASSPATH` set to `lib\*` plus `drivers\*` and `drivers\libs\*`, and `%*` for the arguments. Verified by running `rosetta --version` and a real `dbt-next extract` through the **extensionless** path, which is the exact form the app uses:

```
cmd /c ""C:\rosetta\...\bin\rosetta" dbt-next extract -o <dir> -s dbtstudio_getting_started"
```

Both returned exit 0, and the extract wrote all four YAML files.

**This is a local repair, not a product fix.** The Rosetta CLI zip still ships the corrupted file, so every other Windows user is still broken. The team needs to fix it upstream. Two things follow for the shoot: the footage will show a patched install rather than exactly what a viewer downloads, and if Rosetta is ever reinstalled or updated, the repair is wiped and has to be redone. If that trade is not acceptable, the alternative is to record this lesson on the Mac, where the Unix `rosetta` script in the same folder was always intact.

## Before you hit F9

- **Start from lesson 6's end state.** `models/` empty apart from `.gitkeep`, no `target/`, no `logs/`, no `.user.yml`, and no `rosetta/dbtstudio_getting_started/` folder. dbt and Rosetta each leave one of those behind, so delete all five if you have been testing. **Checked 12 Aug 2026: the project is in exactly this state**, so if you have run nothing since lesson 6, there is nothing to clean up.
- Dark theme, app maximized, taskbar auto-hidden.
- No internet needed.

## Where the Project button is

Top right of the window, between the project name and **Connect to Cloud**: `▶ Project ⌄`.

**Only the caret does anything.** The "Project" half of the split button is bound to an empty handler and rendered with `cursor: default`, so clicking it produces no response at all. The `⌄` is what opens the menu. Aim for the caret, or the take shows the app apparently ignoring a click.

Confirmed against the real menu, which lists thirteen entries in this order:

**Raw Layer, Staging Layer, Incremental/Enhanced Layer** (the three with the Rosetta icon), then Run, Test, Build, Compile, Debug, Generate Docs, Serve Docs, Clean, Deps, Seed (the dbt ones).

The three you want are the top three, which is convenient: the cursor never has to travel past them.

Names only appear, with **no subtitles under them**. The code carries a `subTitle` for every entry but the component never renders it, so nothing explains the entries on screen. That is the gap card 1 is filling.

Each of the three opens a dialog rather than running anything, so the menu click is safe. If `rosettaPath` were unset they would only show a toast, but it is set here, so all three open their dialog.

The open menu covers roughly the upper right quadrant, down to about half screen height. Bottom right stays clear, which is where card 1 sits.

## The two picker dialogs, confirmed against real footage

Staging and Incremental use the same picker, titled **Rosetta DBT Staging** and **Rosetta DBT Incremental**. Both open with **nothing selected** and their Generate button **disabled** until you tick something.

**The picker shows the whole project, not raw's output.** You see `analysis`, `macros`, `models`, `seeds`, `snapshots`, plus `dbt_project.yml`, `profiles.yml` and `README.md`. The four files raw wrote only appear once you expand `models` and then `raw`, where the folder is labelled `raw (contains 4 SQL/YAML files)`.

**Expand rather than using Select All, in both dialogs, for different reasons.**

In staging, slide 5 says "that list is exactly what raw just wrote". That is only true on screen after you expand down to `raw`. Doing the expansion makes the sentence honest and shows the dependency the slide exists to teach. Select All is one click but hides it.

Expand `raw` so the four names are visible, then tick the **folder** checkbox rather than the four files. One click, and the viewer still sees which four tables it covers. The slide says "which tables you want", and the tables are what those filenames are: `main_courses`, `main_enrollments`, `main_grades`, `main_students`.

The staging picker filters to YAML, so on a clean take the tree is short: `.gitkeep`, `raw`, `profiles.yml`, `README.md`. `staging` and `enhanced` do not exist yet. The incremental picker accepts SQL as well, so by the time you reach it `staging` is there with a checkbox of its own. Leave it alone.

In incremental it is not a style choice. **Select All generates enhanced models for everything**, which is the exact failure this lesson is built to avoid. A test run with Select All logged "Processing 4 YAML files" and "Processing 4 SQL files" and wrote four `enh_*.sql` files, every one carrying `UNIQUE_KEY_COLUMNS`. That project passes its first `dbt run` and fails its second. Tick only `main_grades.yaml` under `raw`.

## Why the Rosetta workspace folder must be deleted

`rosetta/dbtstudio_getting_started/` is in the prep list for a reason that is easy to miss. If it survives from an earlier run, Raw Layer prints:

```
model.yaml already exists at .\dbtstudio_getting_started\model.yaml. Skipping extraction.
```

Slide 3 says "what it does is read your database and write down what it found", while the terminal says it skipped doing exactly that. Delete the folder so a real extraction runs and the log matches the narration.

## Beats

| Listen for | Do this |
|---|---|
| "It all lives under the Project button" | Click the **caret** on `▶ Project ⌄`, top right next to Connect to Cloud |
| "The top three entries belong to Rosetta" | Hold so all three read |
| "Raw Layer goes first" | Click **Raw Layer** |
| "It asks for an output folder, and nothing else" | Hold on the dialog. Do not touch the path |
| "Then it reads your database" | Click **Generate Raw Layer** |
| "That takes a few seconds" | The extract runs, about 4.4s. This line exists to cover it |
| "One file per table" | Expand `models/raw` in the tree |
| "They are sources, which is dbt's word" | Open any one of the four YAML files |
| "Staging Layer comes next" | Project caret, **Staging Layer** |
| "so you go into models, and then into raw" | Expand `models`, then expand `raw` so the four names are visible |
| "Tick the folder, and generate" | Tick the **`raw` folder** checkbox, then **Generate Staging Models** |
| "That list was exactly what the last pass produced" | The run finishes under this line |
| "Now you have models" | Expand `models/staging` and open one |
| "Incremental Layer comes last" | Project caret, **Incremental/Enhanced Layer** |
| "So select only grades, and generate" | Expand `models` then `raw`, tick **only** `main_grades.yaml`, then **Generate Incremental Models**. **Never Select All here** |
| "in a folder called enhanced" | The `enhanced` folder appears in the tree |
| "Here is the part to watch" | Open `enh_main_grades.sql`, scroll so both placeholders are visible |
| "The first placeholder is the unique key" | Put the cursor on the `UNIQUE_KEY_COLUMNS` line |
| "For grades, that is the grade ID" | Make the first edit |
| "it appears twice on the same line" | Move to the `where` line, so both instances read |
| "That is the date recorded" | Make the second edit, both instances |
| "Save it" | Click **Save**. An unsaved file leaves lesson 8 with nothing to run |

## The two edits, exactly

In `models/enhanced/enh_main_grades.sql`:

| Replace | With |
|---|---|
| `unique_key = ['UNIQUE_KEY_COLUMNS'],` | `unique_key = ['grade_id'],` |
| `where INCREMENTAL_COLUMN > (select max(INCREMENTAL_COLUMN) from {{ this }})` | `where date_recorded > (select max(date_recorded) from {{ this }})` |

## What each pass actually produces

Verified by running all three.

| Pass | Command | Output | Time |
|---|---|---|---|
| Raw Layer | `dbt-next extract -o models/raw -s <connection>` | 4 YAML source files, one per table, `not_null` on every column | 4.4s |
| Staging Layer | `dbt-next staging -o models/staging -i <yaml>...` | 4 SQL models, plain passthrough selects | 1.5s |
| Enhanced Layer | `dbt-next incremental -o models/enhanced -i <yaml>` | 1 SQL model, incremental, with placeholders | 1.4s |

None of them needs a speed ramp.

A staging model looks like this, and that is the whole file:

```sql
with grades as (
	select grade_id, enrollment_id, grade, date_recorded
	from {{ source('main', 'grades') }}
)
select * from grades
```

## Why only grades gets an enhanced model

An incremental model needs a column that reliably marks new rows.

- `grades` has `date_recorded`, a real DATE. It qualifies.
- `courses` and `enrollments` have no such column at all.
- `students` has `enrollment_year`, which looks like one but is a year. Two students enrolling in the same year, and a strict `>` comparison misses the later one.

Selecting one file out of four is also the clearest demonstration of why the picker exists.

## Product issues to report

Three more for the list, on top of the corrupted `rosetta.bat`.

**The enhanced layer ships unfinished.** Generated incremental models contain the literal tokens `UNIQUE_KEY_COLUMNS` and `INCREMENTAL_COLUMN`, which are not columns in any database. A first `dbt run` passes anyway, because `is_incremental()` is false on a first build and the broken line never executes. The **second** run fails:

```
Binder Error: Referenced column "INCREMENTAL_COLUMN" not found in FROM clause!
```

With all four tables selected, that is 4 failed models out of 8. A beginner who generates everything and runs twice hits it with no warning.

**The Staging menu subtitle is wrong, but nobody can see it.** The code sets "Generate dbt Staging Layer (runs extract first)" and it does not run extract: it only consumes the YAML that Raw Layer already wrote, and if `models/` is empty the dialog has nothing to select and Generate stays disabled.

Downgraded after checking the real menu: `SplitButton` declares `subTitle` in its props type and never renders it, so none of the thirteen entries shows a subtitle at all. The wrong string is dead code, not something a beginner reads. Still worth sending, since anyone who later makes the component render subtitles would ship the error to users, but it is not confusing anyone today. Do not describe it to the team as a user-facing bug.

**`dbt-next business` is not exposed.** The CLI has a fourth subcommand, "Generate business dbt models from connection config", and the repo README advertises a business layer. The menu offers only three.

## Timing

Every beat is under your control, and the three commands are all under 5 seconds. The script runs **497 words, about 236 seconds** of speech, up from 165. Slides 3, 5, 7, 9 and 10 were all lengthened to match what they actually ask you to do on screen.

Per slide, at the series' rate of roughly 2.1 words per second:

| Slide | Words | ~sec | Load |
|---|---|---|---|
| 1 Intro | 42 | 20 | full frame card |
| 2 Project menu | 24 | 11 | one click, then hold |
| 3 Raw | 29 | 14 | two clicks plus the 4.4s run |
| 4 What raw wrote | 49 | 23 | expand and open |
| 5 Staging | 71 | 34 | six actions plus a 1.5s run |
| 6 What staging wrote | 49 | 23 | expand and open |
| 7 Enhanced | 66 | 31 | six actions plus a 1.4s run |
| 8 What enhanced wrote | 48 | 23 | open and scroll |
| 9 Fill them in | 75 | 36 | three token replacements |
| 10 Closing | 44 | 21 | full frame card |

## The generate click never lands on the last words

Each of the three passes runs a command you do not control, and the next slide opens by claiming the files already exist. So in all three slides the generate instruction sits **before** the end, with narration after it to cover the run:

| Slide | Click falls at | Narration after it | Run it has to cover |
|---|---|---|---|
| 3 Raw | 45% | 7.6s | 4.4s |
| 5 Staging | 61% | 13.3s | 1.5s |
| 7 Enhanced | 71% | 9.0s | 1.4s |

This is why slide 5 says "tick the folder, and generate" in the middle and then explains why the three passes run in order, rather than ending on the instruction. Keep that shape if you reword any of them, or the generation will still be running when the next slide asserts it is done.

Do not touch the output path in any of the three dialogs. All three are prefilled correctly, with `models/raw`, `models/staging` and `models/enhanced`.

## Recording

F9, wait 3 seconds, start the Kokoro MP3 on your phone, perform the beats in sync. Let it run 3 seconds past the last word before F9 again.
