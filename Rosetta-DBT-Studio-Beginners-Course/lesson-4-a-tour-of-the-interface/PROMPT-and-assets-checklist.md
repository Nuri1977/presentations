# Lesson 4 - Prompt and Assets Checklist

Lesson 4, "A tour of the interface", walks the whole app with nothing in it. No project, no connection, no AI provider, Flowfile not installed. It works down the sidebar top to bottom and names every screen as it appears.

The goal is vocabulary, so later lessons can say "the sidebar" or "the SQL Editor" and be understood.

Format: screen recording, with full frame cards for the intro and the close. Concept text is composited on top of the footage in CapCut as transparent content cards. Same approach as lessons 1 to 3.

Runtime is about 8 minutes of narration, 1016 words at 2.11 words per second. App version at time of production: **1.6.2**.

## How this version came about

Two rewrites. It began as a static naming lesson over a single screenshot, which gave the footage nothing to follow. It was then rewritten as a click through of a project that had to be created off camera before lesson 5 created it properly, which was always awkward.

The version here drops the project entirely. Nothing needs preparing, the ordering problem disappears, and the empty state stops being a compromise and becomes the frame: this is what you see the first time you open the app.

What that costs: the workspace parts, the file explorer, the code editor, the AI panel, the terminal, Lineage and Run History, do not exist without a project open, so they are not in this lesson. They get named in the lessons that first need them, in context. The lesson that needs a database connection opens by making one.

## Assets in this folder

| Path | What it is | Status |
|---|---|---|
| `voiceover-script-510sec.md` | Plain script. Subtitle source. | Done |
| `voiceover-kokoro.txt` | Same words with Kokoro markup. | Done |
| `RECORDING-cue-sheet.md` | Beats, prep, and what is deliberately unfinished. | Done |
| `video-presentation.html` | Reference deck, seventeen slides. | Done |
| `slides/1.png` | Intro card, full frame. | Done |
| `slides/17.png` | Closing card, full frame. | Done |
| `overlays/1. card-sidebar.png` | Content card, bottom right. | Done |
| `overlays/2. card-projects.png` | Content card, bottom right. | Done |
| `overlays/3. card-sql-editor.png` | Content card, bottom left. | Done |
| `overlays/4. card-notebooks.png` | Content card, bottom left. | Done |
| `overlays/5. card-object-explorer.png` | Content card, bottom right. | Done |
| `overlays/6. card-sources.png` | Content card, bottom left, raised to clear the New Source button. | Done |
| `overlays/7. card-recent-items.png` | Content card, bottom right. | Done |
| `overlays/8. card-datalake.png` | Content card, bottom right. | Done |
| `overlays/9. card-datalakes-history.png` | Content card, bottom right. | Done |
| `overlays/10. card-new-datalake.png` | Content card, bottom right. | Done |
| `overlays/11. card-flows.png` | Content card, top right. | Done |
| `overlays/12. card-connections.png` | Content card, bottom right. | Done |
| `overlays/13. card-settings-general.png` | Content card, top right. | Done |
| `overlays/14. card-settings-rest.png` | Content card, bottom right. | Done |
| `overlays/15. card-settings-plugins.png` | Content card, bottom right. | Done |
| `sounds/` | Kokoro MP3 per slide, seventeen of them. | To generate |
| Screen recording | The tour of the empty app. | To record |

The three MP3s currently in `sounds/` came from the original eight slide script and match nothing. Regenerate all seventeen.

## Card order

Numbered in the order they go on the timeline. Work down from 1. Fifteen cards over eight minutes, so roughly one every thirty seconds.

## Overlay card placement

Each PNG is a full 1920x1080 frame with the card already positioned. Drop it at 0,0 with scale 100% in CapCut. Do not reposition or rescale.

Most cards sit bottom right, and that is deliberate rather than lazy. Object Explorer, DataLake, Connections and Settings all put a panel down the left side about 450 pixels wide, and that panel is usually the thing being named.

The exceptions, all set from real footage rather than guessed:

- **3 and 4** sit bottom **left**. The SQL Editor and Notebooks both open the AI panel on the right, and a right hand card is covered by it.
- **6** sits bottom left as well, but **raised to 190px** rather than the usual 108px. The New Source form fills the centre and right of the frame, and at the normal height the card lands on the New Source button in the panel. The raised variant clears it.
- **11 and 13** sit top right, because Flows puts its message in the middle of the frame and Settings, General fills the lower half.

Positions were verified by measuring the alpha bounding box of every rendered PNG, not by reading the CSS.

Fade each card in and out with CapCut Animation on the clip itself. Do not use a Transition between clips, since that dips the whole frame including the footage.

## Decisions worth not relitigating

**Dark theme.** Lesson 0's footage is dark and the cards are built for dark. Switch the theme before recording.

**Flowfile stays uninstalled.** It is not bundled. Flows genuinely reads "Flowfile binary not found. Install it from Settings, Flowfile", and that is what a new user meets, so the lesson shows it and explains why. It is an external open source tool, pip installed into Rosetta's own Python on request. Nothing else in the course uses it, and lesson 0 name drops it once without explaining it, so this is its only real coverage.

**Lesson 23 is not Flowfile.** That lesson covers Rosetta's own pipeline editor, `components/pipelineView/`, which reads `pipeline-*.yml` into a node graph and feeds the lesson 25 deploy. Keep the phrase "visual pipeline builder" for lesson 23.

**No forward references in the narration.** The script never says "there is a lesson on this later". A tour names what is on screen and explains what it does. Where a pointer used to be, there is now a short explanation instead, so AI Settings gets "a paid service or a model running locally", Keystore gets "so a password never has to sit in your project files", and so on.

The only forward reference left is the closing hand off, "we create the example project", which every lesson in the series ends with.

**The cards never repeat the narration.** All fifteen were rewritten for this. A card either carries the specifics the voice skips, like the eight storage providers on card 6 and the databases on card 12, or it adds something visible but unspoken, like the file and directory filter on card 7. If a card and the voiceover say the same thing, the card is wasted.

**Settings gets covered in full, but weighted.** General and Plugins get real time, because the projects directory and the bundled dbt, Rosetta CLI and DuckDB are what a beginner actually needs to find later. AI Settings, Rosetta Cloud and Keystore get a sentence each. Task Manager, About and the theme get a clause.

**One video, not two.** Eight minutes is the longest in the series. Splitting Connections and Settings into their own lesson was considered and rejected.

## Open items

- Audio target is minus 14 LUFS. Lesson 1 exported at minus 28 and needed a normalization pass afterwards.
- Kokoro pronunciation of "dbt" is still unverified across the series. Confirmed by ear for this lesson: `[OAuth](/ˌOˈɔθ/)`, `[Flowfile](/flOfˈIl/)`, `[status](/ˈsteɪtəs/)`, plus the existing `[AI](/ˌAˈI/)` and `[query](/kwˈɛɹi/)`.
- Still worth listening for on the full generation: **dbt**, **DuckDB**, **DuckLake**, **API** and **Keystore**.
- The status bar shows a dash where the dbt version should be early in a session, and fills in later. The cue sheet keeps the status bar sweep to slide 16 because of it, but it is worth reporting.
- Object Explorer in the sidebar, Cloud Explorer on the screen. Worth reporting.
