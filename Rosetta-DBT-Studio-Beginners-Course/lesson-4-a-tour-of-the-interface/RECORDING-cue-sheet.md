# Lesson 4 - Recording Cue Sheet

A walk through the whole app with nothing in it. No project, no database connection, no AI provider, Flowfile not installed. That is not a compromise, it is the point: this is exactly what a viewer sees the first time they open Rosetta. The narration does not labour it, since the screen says "No Projects found" all by itself.

You work down the sidebar, top to bottom, and every screen gets named as it appears. Nothing is created. The only form you open, you leave.

Full frame cards are `slides/1.png` (intro) and `slides/17.png` (closing), dropped in during editing, so nothing is performed for them.

**The intro card must be clear of the frame before slide 2 starts.** Slide 2 opens on "On the left is the sidebar", which only works once the viewer can see the app. Cut the card out on the last word of slide 1, not into slide 2.

Runtime is about 8 minutes of narration. App version: **1.6.2**.

## Before you hit F9

App state, all of it already true on a fresh install:

- **No projects.** DBT Studio must read "No Projects found".
- **No database connections**, so SQL Editor and Notebooks both sit on their empty state.
- **No AI provider** configured.
- **Flowfile not installed.** Flows must read "Flowfile binary not found". Do not install it.
- **Dark theme.** Settings, bottom of the Settings panel, before you start recording. Lesson 0's footage is dark and the overlay cards are built for dark.
- **The sidebar collapsed**, icons only. Slide 2 is the click that widens it.
- App maximized, taskbar auto-hidden, OBS windows hidden from capture.

Nothing to prepare off camera. That is the whole advantage of this version.

## Beats

Seventeen slides. Slides 1 and 17 are full frame cards, so nothing is performed for them.

Move slowly and hold still between sections. Every click below changes the screen, so the cut points are obvious in the edit.

| Slide | Listen for | Do this |
|---|---|---|
| 1 | Intro card | Nothing. Cards `slides/1.png`. |
| 2 | "On the left is the sidebar" | The card has just cleared. Run the pointer down the collapsed sidebar |
| 2 | "Click the logo at the top and it widens into names" | Click the Rosetta logo. The sidebar expands |
| 2 | "DBT Studio, which is your dbt projects" | Move down the expanded list as each name is said |
| 2 | "Collapse it again" | Collapse the sidebar with the arrow beside the logo |
| 3 | "it is just this. Manage your projects" | Gesture across the empty projects panel |
| 3 | "Get Started clones a ready made example project" | Point at each of the four buttons in turn as named |
| 3 | "Select Project switches between them" | Point at the Select Project dropdown, do not open it |
| 3 | "Connect to Cloud links the app to a Rosetta Cloud account" | Point at Connect to Cloud, top right |
| 4 | "SQL Editor is a query window on a database" | Click **SQL Editor** |
| 4 | "You pick the database in Select Connection, top left" | Point at Select Connection |
| 4 | "And the plus, that is what you use to create a new connection" | Point at the plus, hold, then click it |
| 4 | "It opens the full list of what Rosetta can connect to" | Move across the database tiles, then scroll to show there are more |
| 4 | "Choose a type, and you get the form for that one" | Do not choose one. Press **Back**, top right, to return to the SQL Editor |
| 4 | "Once connected, the three tabs fill up" | Point at Data, then Queries |
| 4 | "Analytics turns results into pages" | Click **Analytics** |
| 4 | "Create Page makes a new one, and Build Static Site exports them all" | Point at the two buttons beside the Pages header, left then right |
| 4 | "Top right, that icon opens the AI" | Point at the AI icon, far top right. Do not click |
| 5 | "Notebooks has the same connection picker" | Click **Notebooks** |
| 5 | "the same connection picker and the same empty state" | Point at Select Connection, then at the empty panel |
| 6 | "Object Explorer" | Click **Object Explorer** |
| 6 | "The screen calls itself Cloud Explorer" | Point at the Cloud Explorer heading |
| 6 | "counts your connections, your storage types, and what you opened recently" | Move across the three tiles, left to right |
| 7 | "Sources lists the cloud storage you have connected" | Click **Sources** in the panel |
| 7 | "New Source starts with the connection type" | Click **New Source** |
| 7 | "the list of everything Rosetta can read" | Move across the eight provider tiles. They are not named aloud, so do not rush |
| 7 | "the form underneath changes to whatever that provider asks for" | Scroll down to show Connection Name, Project ID and the credentials box |
| 7 | "Test Connection checks that it actually works before Save Connection" | Point at Test Connection, then Save Connection. Both are greyed out, which is correct |
| 8 | "Recent Items is the third tab" | Click **Recent Items** |
| 9 | "DataLake is the step after that" | Click **DataLake** |
| 9 | "How many lakes you have, of which kind" | Point at Total DataLakes, then down the four types |
| 10 | "DataLakes, on the left, lists the instances" | Click **DataLakes** |
| 10 | "Query History under it is coming soon" | Click **Query History** |
| 11 | "New DataLake is where one gets made" | Click **New DataLake** |
| 11 | "Four types offered, three of them still marked Soon" | Move across the four tiles, then click **DuckLake** |
| 11 | "Instance details, storage, the catalog" | Move across the five step markers, left to right |
| 11 | "Name it, describe it, and Next walks you through the rest" | Point at Instance Name, Description, Next |
| 11 | (after the words end) | Cancel out. **This is not narrated**, so do it quietly |
| 12 | "The Flows screen is empty because FlowFile does not come installed" | Click **Flows** |
| 12 | "leaving it out saves disk space" | Let the not found message sit on screen. Do not press Start |
| 13 | "Down at the bottom of the sidebar" | Click **Database Connections** |
| 13 | "the one list that holds both" | Gesture across the empty panel and the explanation |
| 13 | "New Connection and Add Cloud Source" | Point at both buttons. Do not click either, both screens are already covered |
| 14 | "And Settings" | Click **Settings** |
| 14 | "General holds your projects directory" | Point at Projects Directory, then Current Installation, then Check for Updates, then System Information |
| 15 | "AI Settings is where an AI provider goes" | Click **AI Settings** |
| 15 | "Rosetta Cloud signs you in" | Click **Rosetta Cloud** |
| 15 | "Keystore holds credentials" | Click **Keystore** |
| 15 | "Task Manager tracks long jobs" | Click **Task Manager** |
| 16 | "Below that, Plugins" | Move down to the Plugins group in the Settings panel |
| 16 | "dbt Core, Rosetta CLI and DuckDB" | Point at each of the three |
| 16 | "Those are the same versions that you can read in the status bar" | Sweep the pointer along the status bar, right side |
| 16 | "Flowfile is in the same list" | Point at Flowfile in the Settings panel |
| 16 | "About is the version and the licence. And at the very bottom, the theme" | Point at About, then at the theme buttons |
| 17 | Closing card | Nothing. Cards `slides/17.png`. |

## Naming accuracy

Sidebar order, from the app source: **DBT Studio**, **SQL Editor**, **Notebooks**, **Object Explorer**, **DataLake**, **Flows**, then **Database Connections** and **Settings** pinned at the bottom.

Object Explorer is the sidebar label. The screen inside it says **Cloud Explorer**. The narration names both so a viewer is not left wondering, and it is worth reporting as a product inconsistency.

The eight storage providers on New Source are Google Cloud Storage, Amazon S3, Azure Blob Storage, MinIO, Cloudflare R2, Backblaze B2, rustfs and Garage. **The narration does not name any of them**, it just says "the list of everything Rosetta can read", so the pointer is what draws attention to them. Overlay card 6 carries the names for the viewer to read.

The DuckLake wizard steps are Instance Details, Storage Configuration, Catalog Configuration, Runtime Options, Review and Create.

## The two buttons on New Source are greyed out

On slide 7 the narration names **Test Connection** and **Save Connection**, and both are disabled until the required fields are filled. That is correct and you should leave them that way, since nothing in this lesson gets created. Point at them, do not click.

## Slide 13 does not open anything

Database Connections is the last screen and the shortest beat, because both of its buttons lead somewhere the viewer has already been. **New Connection** opens the same database grid as the plus in the SQL Editor on slide 4, and **Add Cloud Source** opens the same provider grid as New Source on slide 7. Point at them and move on.

Note the app labels that second button **Add Cloud Source** in the main panel and **New Cloud Source** in the left panel. The narration uses the main panel wording, since that is where the pointer will be.

## Check before you record slide 4

Two things on that slide have not been seen with no connection selected:

- **The Analytics toolbar.** The narration names two buttons beside the Pages header, **Create Page** and **Build Static Site**. If that toolbar is hidden or disabled until a connection exists, the beat has nothing to point at and the wording needs changing. Look at it before you roll.
- **The plus leaves the screen.** It navigates to the same Create New Connection page that slide 13 reaches from Database Connections, so you come back with the **Back** button, top right. Slide 4 is the only place this lesson actually opens that screen. Slide 13 just points at the button and moves on, so the two do not tread on each other.

## What is deliberately unfinished, and said out loud

Three things on screen say "coming soon". The narration names two of them, where the viewer is looking straight at the thing:

- DataLake, **Query History**, which states "Query history functionality coming soon". Named on slide 10.
- Apache Iceberg, Delta Lake and Apache Hudi, all ribboned **Soon** on the New DataLake screen. Named on slide 11.

The third, the **Recent Queries** and **Tables Accessed** tiles on the DataLake dashboard, is deliberately not narrated. Slide 9 stays on what the dashboard is for, and the unfinished bits get named on the screens that actually show them.

## Flowfile stays uninstalled

Flows will read "Flowfile binary not found. Install it from Settings, Flowfile." That is correct and it is what a new user sees on a fresh install, because FlowFile is not included in the initial download. Rosetta installs it into its own Python on request, in one click.

**Do not say it is separate from Rosetta, or an external tool.** An earlier draft of slide 12 did, and the team corrected it: FlowFile is held back from the first install to save disk space, nothing more. The point the slide has to land is that it gives you ETL inside the same app, rather than as a tool of its own.

Do not install it before or during recording. Slide 12 names it, slide 16 points at the install button, and nothing else in the course uses it.

Do not call it "a visual pipeline builder". That phrase belongs to lesson 23, which covers Rosetta's own pipeline editor, a different feature that reads `pipeline-*.yml` into a node graph.

## Known issues to avoid

- **The status bar shows a dash where the dbt version should be** until later in the session, and only fills in once the connections screen has been visited. Do not sweep the status bar before slide 16, or the narration will name a version that is not there.
- Object Explorer, DataLake and Connections all put a panel on the left about 450 pixels wide, which is why most overlay cards sit on the right.
- **Cards 3 and 4 sit bottom left on purpose.** The SQL Editor and Notebooks open the AI panel on the right, so a right hand card gets covered by it.
- **Card 6 sits bottom left and higher than the rest**, so it clears the New Source button in the panel. Drop it at 0,0 like the others, the offset is baked into the PNG.

## Recording

F9, wait 3 seconds, start the Kokoro MP3 on your phone, perform the beats in sync. Let it run 3 seconds past the last word before F9 again.

Nothing here waits on the app, so no speed ramps are needed. Every beat is a click you control.

At just over 8 minutes this is the longest lesson in the series, so pace matters more than usual. If a beat lands early, hold still. If you lose sync, the slide boundaries are the recovery points, since each one is a separate MP3.
