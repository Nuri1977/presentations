# Plan dbt Project 01

**A Project #1 course for Rosetta DBT Studio: dbt + DuckDB on NYC taxi data, built and recorded by Claude Code using computer use**

| | |
|---|---|
| Status | Draft plan, written 9 Nov 2026. **Amended the same day by the "Course repo and PR design" below, which overrides any section it contradicts** (numbering, tags, D2, D7, D11, the recorder) |
| Executes it | Claude Code in the Claude desktop app, as a **local session on Nuri's Mac** (runner `mac-desktop`), with computer use turned on |
| Skill | `rosetta-academy-video` (this plan extends it; it does not replace it) |
| Tooling | `presentations/_academy-video-tooling/` (extended, see section 10) |
| Course folder | `presentations/nuries-youtube-clones/project-01/` (this file lives here) |
| Model course | Luke Barousse, *dbt for Data Analytics & Engineering*, Project #1: video `youtube.com/watch?v=1Bf049kXV2g`, code `github.com/lukebarousse/dbt_Analytics_Engineering_Course/tree/main/project_1` |

---

## Change of 10 Nov 2026: git kept light in the dbt course (overrides the PR design below)

Nuri: "this is a dbt tutorial and we just show that there is a public repo they can get the code."

- **dbt course:** no branches, no pull requests, no repo-creation lesson. Lesson 2.1 creates the project, then commits and pushes it to GitHub from Studio's Git tab (Initialize Repository, commit, add remote, Publish Branch). Every later lesson ends with a short commit + push in the Git tab, straight to `main`. Each video points to `github.com/Nuri1977/nyc-taxi-dbt` for the code.
- **Lesson 1.2 (Git and GitHub) leaves the dbt course.** The empty repo is created off camera before 2.1 (rehearsal: `nyc-taxi-dbt-rehearsal`, already created). The 1.2 review cut becomes the first video of a **separate GitHub series** (write a file, commit, push, open a PR, merge, from Studio's UI), planned later on the same project.
- **3.1 Ship & Automate and 3.2 Showcase stay** in the dbt course (CI on push to `main`, published warehouse, Pages, README).
- Course map: 0 Welcome · 1.1 Install · 2.1–2.8 dbt basics · 3.1–3.2 ship it (12 videos). Lesson 0's repo slide (PR list) and course map need a re-render for this.
- Still needed before 2.1: Nuri stores the push token in `/Users/Shared/academy/learner/.git-credentials`.
- **Git and GitHub basics are assumed** (Nuri, 10 Nov). Lesson 2.1 creates the public repo on github.com and connects it from Studio, without teaching git. For beginners, Lesson 0 and 2.1 link to free videos (in their YouTube descriptions, `course.yaml` → `help_links`): freeCodeCamp "Git and GitHub for Beginners – Crash Course", Programming with Mosh "Learn Git in 1 Hour", "Git and GitHub Explained in 7 Minutes", "Learn GitHub without needing the terminal". Lesson 0's course map says "New to git? Links in the description".
- Renumbered review cuts: Models is now **2.3** (was 3.3); 1.1 now leads to 2.1.
- **dbt commands come from Studio's dropdowns, not the terminal** (Nuri, 10 Nov). Whole project: the **Project** split button ▸ Run, Test, Build, Compile, Debug, Generate Docs, Serve Docs, Clean, Deps, Seed. One model: the **Model** split button on the open file ▸ Run, Build Model, Test, Compile, Preview (and the +model / model+ variants). This applies to the lessons after 2.2 (2.3 onward) and to any new lessons; 2.1 and 2.2 keep their terminal commands (Nuri, 10 Nov):
  - 2.3 Models: Model ▸ Run for `trips` (or Project ▸ Run); rows: Model ▸ Preview. Preview fails on a view over relative parquet paths in 1.7.6 (`studio-notes.md`), so where it fails the lesson keeps the terminal `dbt show` and says why, until the plan's view-rows decision changes.
  - 2.4 Jinja: Project ▸ Seed, Model ▸ Compile on `top_pickup_zones`, Project ▸ Run.
  - 2.5 Properties: Project ▸ Run after `persist_docs`.
  - 2.6 Docs & DAG: Model ▸ Run +model (Upstream) on `monthly_summary`; Project ▸ Generate Docs, Serve Docs.
  - 2.7 Materializations: Project ▸ Run.
  - 2.8 Tests: Project ▸ Test, Model ▸ Test on one model, Project ▸ Build.
  - 3.1/3.2: Project ▸ Build before the push; CI runs `dbt build` itself.

- **Rehearsal status (10 Nov 2026, night run):** review cuts recorded for 2.2 Get the data, 2.3 Models (updated), 2.4 Dependencies & Jinja, 2.5 Properties, 2.6 Docs & the DAG, 2.7 Materializations, 2.8 Tests and 3.1 Ship & Automate. Each starts from a clone of the previous lesson's push (`states/lesson-2-N-end`, `clone:` + `dbt:` in the recipe) and ends with a real push to `nyc-taxi-dbt-rehearsal` via Sync Changes. 3.1's workflow ran green on GitHub (40 s) and published `prod.duckdb`. Findings in `studio-notes.md`.
- **3.2 Showcase is waiting on Nuri:** GitHub Pages needs a repo setting (Pages source: GitHub Actions), and Pages plus the public `attach` query need a public repo (the rehearsal repo is private). Options: make the rehearsal repo public for 3.2, or record 3.2 only in the final run on the public `nyc-taxi-dbt`.

## Course repo and PR design (agreed with Nuri, 9 Nov 2026; superseded in part by the change above)

**Goal:** one public git project, shared with learners, built continuously from Lesson 0 to the last lesson. Every lesson starts exactly where the previous one ended, and every lesson that changes files does it in **one pull request**.

### Repo and permissions

| | |
|---|---|
| Public repo | `github.com/Nuri1977/nyc-taxi-dbt` (replaces D2's dedicated account) |
| Public repo status | Nuri created it on 9 Nov 2026 (public, empty). It stays as a placeholder: **right before the final run Nuri deletes it** (Settings → Delete; it is empty), and the final 1.2 take creates it again on camera, exactly as a learner would. The push token is made after that take |
| Rehearsal repo | `github.com/Nuri1977/nyc-taxi-dbt-rehearsal`, private. Does not exist yet; the rehearsal run's 1.2 creates it on camera |
| Git writes | **Only through the UI, on camera:** Rosetta DBT Studio's Git panel (Create New Branch, commit, Publish Branch, Push, Switch Branch, Pull) and the GitHub website in the recording browser (new repo, Compare & pull request, Squash and merge, Delete branch, Settings). Bash only reads repo state (`git log/status/diff`, `gh pr view`). No `gh pr create/merge`, no force-push. The no-git-writes rule still holds for every other repo |
| Credentials | Nuri signs in to GitHub once in the recording browser profile. After Lesson 1.2 creates the repo (rehearsal run and final run each), Claude Code pauses; Nuri creates a fine-grained token for that repo only (Contents + Workflows read/write) and stores it in the learner home's credential store. Claude Code never types or sees it |
| Learners | Build their own repo by following the videos. Our merged PRs are the answer key: "Code for this lesson" in every description links to the lesson's merged PR |
| Tags | None. The merged PR (its Files tab and merge commit) marks each lesson's end state |

### Lessons (13, renumbered; branch names `lesson-<module>-<n>`)

| # | Lesson | Old # | Repo action |
|---|---|---|---|
| 0 | Welcome: what you build, the NYC taxi data, how to use the repo | 1.1 (merged in) | none (slides; nothing is built yet, so the DAG is drawn on a slide) |
| 1.1 | Install Rosetta DBT Studio 1.7.6 | 2.1 | none. Real download; the app is dragged into a stage "Applications" folder under the learner home, never `/Applications` |
| 1.2 | Git and GitHub | 2.2 | create the **empty** repo on github.com. Then the token pause |
| 2.1 | Create the dbt project | 3.1 | Initialize Repository, first commit (project, `.gitignore`, short README with the lesson table), Publish Branch `main`. **The only direct push to main** |
| 2.2 | Get the data | 3.2 | PR #1 |
| 2.3 | Models | 3.3 | PR |
| 2.4 | Dependencies & Jinja | 3.4 | PR |
| 2.5 | Properties | 3.5 | PR |
| 2.6 | Docs & the DAG | 3.6 | PR |
| 2.7 | Materializations | 3.7 | PR |
| 2.8 | Tests | 3.8 | PR |
| 3.1 | Ship & Automate | 4.1 | PR; the workflow also runs on `pull_request`, so this PR shows the dbt build check. Publishing the warehouse runs only on `main` |
| 3.2 | Showcase | 4.2 | PR; README rewritten as the portfolio README (badge, docs link, query block); GitHub Pages |

### The PR flow inside every lesson from 2.2

1. Start on `main`, up to date (end of the previous lesson).
2. Studio Git tab → **Create New Branch** `lesson-2-3` (example).
3. The lesson's work; one or more commits in the Git tab (stage with +, message, Commit).
4. **Publish Branch**.
5. GitHub website: **Compare & pull request** → title `Lesson 2.3: Models` → body: what this lesson adds, files changed, how to check (`dbt build` passes), link to the README → Create pull request. From 3.1 on, wait for the green check.
6. **Squash and merge** → Confirm → **Delete branch**.
7. Studio: Switch Branch → `main` → **Pull**. The next lesson starts here.

### Other decisions

- **View rows:** use `dbt show --select <model> --limit 10` in the command box under Studio's terminal. The SQL Editor is used only for tables (marts after 2.7) and metadata queries, because Studio 1.7.6 runs SQL Editor queries from `/` and the parquet path is relative (see `studio-notes.md`).
- **Studio 1.7.6 is pinned** for the whole course. If rehearsal shows the "no branch after Initialize" display in 2.1, the narration covers the refresh.
- **Recorder:** the stills recorder (Playwright, true 4K frames, drawn cursor) for every lesson, including the GitHub website scenes. No computer-use live capture.
- **Look:** the Lesson 3.3 review cut (now 2.3) is the template: slides v2, zooms, cards, Kokoro `af_heart`.
- **Review flow:** rehearse **all** lessons against the rehearsal repo and send one review cut per lesson. After Nuri approves them (or sends notes), record all final takes into the public repo in one run, in order.
- **Native apps:** the Finder steps in 1.1 are outside Playwright. They need a screen capture of the Finder window (`screencapture -l`) or computer use. Decide during the 1.1 rehearsal.

---

## 0. Summary

Luke's video is 8.5 hours long and covers two projects. We take only his **Project #1 path**: the dbt basics plus the dbt + DuckDB pipeline he ships with GitHub Actions. We skip his "What is dbt?" intro and all of Project #2 (Databricks). We rebuild that path as **13 short lessons (4 to 7 minutes each, about 75 minutes in total)**, done entirely in **Rosetta DBT Studio**, on a different public dataset (**NYC TLC Green Taxi trips, 2025**), with our own slides, narration and code. All code is pushed to **one public GitHub repo**, with one commit and one tag per lesson. The AI Assistant is never used.

**How it gets made:** Claude Code does the project itself, on Nuri's Mac, while the screen is recorded:

- **Computer use** drives the native apps: Rosetta DBT Studio and Finder (clicks, menus, dialogs, Source Control, file names, commit messages).
- **Playwright** handles the three things computer use cannot do or cannot do well:
  - the **browser**, because computer use only reads browser windows and never clicks in them;
  - **exact code typing** in Studio's editor, through a small "typist" attached over Chrome DevTools Protocol (CDP) with the editor helpers switched off, as in the pilot;
  - **slide rendering**, frame by frame at 4K.
- **ffmpeg** records the "stage" display live at 4K/30 fps.
- **Voice first:** narration is generated and measured before recording. Computer use is slow, so each raw take has idle gaps. A cutter removes them and fits every beat to its voice line.

Every lesson ships with the skill's normal outputs: a 4K MP4 for YouTube, a 1080p MP4 for phones, captions, beat sheet, YouTube package, PPTX, and a cue sheet for a human retake.

---

## 1. Scope: what we take from Luke's Project #1

### 1.1 Chapter map

| Luke's chapter (video time) | Our lesson | Notes |
|---|---|---|
| Course intro and "What is dbt?" (before Data & Project Intro) | — | **Skipped** (per Nuri) |
| Data & Project Intro (ends at 0:22:12) | **1.1 The project and the data** | New dataset; previews the finished result; recorded last |
| Tool Setup (0:22:12) | **2.1 Install Rosetta DBT Studio** and **2.2 Git and GitHub** | Studio replaces VS Code + uv + terminal |
| dbt Setup (0:40:41) | **3.1 Create the dbt project** | Studio's New Project + DuckDB connection, `dbt debug`, first commit and publish |
| (his `download_data.py`, Get the Data card) | **3.2 Get the data** | Browser download recorded, Finder move, seed CSV, declared source |
| Models (1:21:42) | **3.3 Models** | Pilot lesson |
| Dependencies & Jinja (1:38:31) | **3.4 Dependencies & Jinja** | `dbt seed`, `ref()`, `{% set %}`, compiled SQL, lineage |
| Properties (1:59:45) | **3.5 Properties** | `schema.yml`, descriptions, `persist_docs` |
| Docs & the DAG (2:13:53) | **3.6 Docs & the DAG** | Second-level model with two refs, Generate/Serve Docs, LINEAGE |
| Materializations (2:34:06) | **3.7 Materializations** | Project default `table`, staging `view` |
| Tests Pt.1 (2:46:21) | **3.8 Tests** | Grain tests, one deliberate failure, Build |
| Ship & Automate (2:59:44) | **4.1 Ship & Automate** | CI profile, GitHub Actions, warehouse published as a release asset |
| Showcase (3:16:33) | **4.2 Showcase** | README + badge, docs on GitHub Pages, query the published warehouse from Studio |
| Project #2 (Databricks) and everything after 3:30 | — | Out of scope |

### 1.2 What his project_1 contains, and our equivalent

| Luke's project_1 | Ours |
|---|---|
| About 692k job postings, 12 monthly parquet files (about 85 MB), GitHub release `dataset-v1` | NYC TLC **Green** taxi trips 2025, 12 monthly parquet files from the TLC site (sizes and row counts measured in Phase 0) |
| Seed: skills CSV shown in the intro | Seed: `taxi_zone_lookup.csv` (TLC zone lookup, about 265 rows: LocationID, Borough, Zone, service_zone) |
| `sources.yml` with `external_location: read_parquet(...)` | Same pattern over `data/raw/green_tripdata_2025-*.parquet` |
| `job_postings` (view, cleaned) | `trips` (view, cleaned) |
| `jobs_per_month`, `top_locations` | `trips_per_month` (by pickup borough, joins the seed), `top_pickup_zones` (joins the seed, Jinja `top_n`) |
| `monthly_summary` (two refs) | `monthly_summary` (two refs: total trips and share paid by card) |
| `unique` / `not_null` on mart grains, `persist_docs` | Same, plus `accepted_values` and seed key tests |
| `ci/profiles.yml` (prod), GitHub Actions on push, weekly and manual; publishes `prod.duckdb` as release asset; docs on GitHub Pages | Same design. `pip` + `requirements.txt` instead of uv, docs deployed by the workflow |
| dbt v2 with uv, VS Code | Studio's managed Python + dbt Core (see D3), Studio editor, Project menu, Source Control |

**Originality rule:** Luke's course provides the topic order only. Narration, slide designs, dataset, model names, SQL and README are ours. We do not reuse his frames, diagrams, wording or code verbatim. Each YouTube description credits him with a link (D9).

---

## 2. Decisions for Nuri (defaults in bold; Claude Code proceeds with the defaults unless told otherwise)

| # | Decision | Default | Alternatives |
|---|---|---|---|
| D1 | Dataset | **NYC TLC Green Taxi 2025, all 12 months + taxi zone lookup CSV as a seed.** Small files, so CI and recordings stay fast; the size is close to Luke's | Yellow Taxi 2025 Q1 (3 months, about 10M rows: better known but slow in CI); Citi Bike |
| D2 | GitHub owner and repo for the course project | **A dedicated GitHub account or org for recording (no personal account on camera), repo `nyc-taxi-dbt`, public.** A private rehearsal repo `nyc-taxi-dbt-rehearsal` for dry runs | Nuri's own account; under `rosettadb` |
| D3 | dbt version | **What Studio 1.7.6 installs by default (dbt Core v1.x; 1.7.5 installed 1.12.6 + dbt-duckdb 1.11.1).** YAML is written so it also parses on v2 (`data_tests:`, `config:` blocks) | Studio's dbt Core v2 switch, to match Luke (needs a check of the v2 install path in the UI) |
| D4 | Voice | **Run a 30-second voice comparison first: Kokoro `af_heart` vs Chatterbox (MIT licence, runs on Apple Silicon/MPS, adds an inaudible "Perth" watermark).** Nuri picks by ear | Kokoro only (skill default); Nuri's own voice via `voice-human/` |
| D5 | YouTube visibility | **Unlisted** (skill default), one playlist "Project 1" | Public playlist |
| D6 | Capture display | **External 4K monitor set to "looks like 1920 x 1080" (HiDPI), used only as the stage** | Built-in display, 1600 x 900 pt window, upscaled to 4K (slightly softer) |
| D7 | Install scene (2.1) | **Real download of the 1.7.6 Mac release in the browser and the real copy to `/Applications`, as a learner does it. Before the take, Claude Code checks `/Applications` for an existing Rosetta DBT Studio; if one is there, it asks Nuri before replacing it** (that cannot be undone) | Show the download and the opened DMG/zip, then copy the app to a separate stage folder |
| D8 | Code entry | **Typed live by the CDP typist for files of 25 lines or fewer; pasted (clipboard) for longer files, with the narration saying "paste it from the link in the description"** | Paste everything; type everything |
| D9 | Credit line | **"Lesson order inspired by Luke Barousse's dbt course (link)" in every description** | None |
| D10 | On-screen paths | **Isolated home `/Users/Shared/academy/learner`; project at `/Users/Shared/academy/learner/projects/nyc_taxi`** | A dedicated macOS user `learner` (cleanest, more setup) |
| D11 | Studio version | **Pin 1.7.6 (tag dated 4 Nov 2026).** Its Source Control has Initialize Repository, Publish Branch, Push, Pull, Sync Changes and an Add Git Remote dialog. Four git changes were made after 1.7.6 and are not in any release yet: branch shown after init, cached HEAD refresh, cancelling stale git queries, and the Commit / Commit & Push split button | Wait for the next release if rehearsal shows the "no branch after init" bug on camera |

---

## 3. Ground rules (hard rules for Claude Code)

1. **Never change `dbt-studio/`.** Read-only reference only. Copying image files out of `dbt-studio/assets` or `.../conbined-dbt-project_01/dbt-studio-old-01/assets` (same files) into the course `brand/` folder is fine.
2. **`presentations/` is Nuri's git repo:** write files only, never stage, commit, branch or push. Offer a commit message when asked.
3. **Course repo (`nyc-taxi-dbt`):** commits and pushes happen **only through Studio's Source Control, on camera**, as the lesson says. Rehearsals push to the rehearsal repo only. Off camera, Claude Code may only check out tags, clean the working folder and create **local** tags for start states. Pushing tags needs Nuri's OK. **Never force-push the public repo** without Nuri's explicit OK in that session.
4. **No AI Assistant:** never open Studio's AI chat or agent panels. The isolated profile has no AI provider configured. Slides and narration do not mention AI.
5. **Isolation:** Studio runs with its own `HOME` and `--user-data-dir`. The browser is a dedicated Chrome profile. Nuri's normal Studio profile, Chrome profile, keychain items and git config are never used. Check before every recording session that the paths match (section 6.4).
6. **No secrets or personal data on screen:** no tokens, emails, notifications, or Nuri's paths and bookmarks. GitHub sign-in in the recording browser profile is done **by Nuri**; the personal access token is stored **by Nuri** in the isolated credential store. Every take is checked frame by frame around auth steps (section 12).
7. **Full-screen control:** computer use takes the screen only during takes. Nuri grants it in the kickoff prompt ("you may take full-screen control for recording takes") and leaves the Mac alone while a take runs.
8. **Computer use never clicks in browsers** (browsers are read-only for it). All browser steps go through Playwright. `cliclick` is used **only to move the visible cursor** (cosmetic glide), never to click or type.
9. **One approval gate per lesson** (skill rule): beat sheet + slide contact sheet, sent in module batches (section 11). After approval, record, render and deliver without more questions.
10. **Voice first:** beats are voiced and measured before any take. Takes are cut to fit the voice, not the other way round.
11. **Real labels:** use the label Studio actually shows. Log any difference from this plan in `studio-notes.md`. Facts (versions, row counts, licences) come from the rehearsal or a checked web source with the date in `accuracy_notes`.
12. **If `_academy-video-tooling/` is missing or broken, stop and ask** (skill rule). Extending it with new files as in section 10 is expected.
13. Claude cannot hear audio: Nuri listens once per lesson for pronunciation.

---

## 4. The data

| Item | Value (checked 9 Nov 2026 on the TLC page) |
|---|---|
| Source page | `https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page` (monthly, about 2 months behind; newest listed: Sep 2026) |
| Trip files | `https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-01.parquet` … `-12.parquet` (same URL pattern as the Yellow files listed on the page) |
| Seed | `https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv` |
| Data dictionary | Yellow: `https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf`. **Green dictionary URL: verify on the page in Phase 0** |
| Page notes | Parquet schema "may change slightly" across years (hence `union_by_name = true`); 2025+ files add `cbd_congestion_fee`; TLC makes no accuracy guarantees; the page states no terms of use. **Phase 0 records the NYC Open Data terms link in `accuracy_notes`** |
| Columns we use (Green) | `VendorID`, `lpep_pickup_datetime`, `lpep_dropoff_datetime`, `PULocationID`, `DOLocationID`, `passenger_count`, `trip_distance`, `payment_type`, `fare_amount`, `tip_amount`, `total_amount`. **Confirm against the files and the Green dictionary in Phase 0** (payment_type 1 = credit card) |
| Zone lookup | `LocationID, Borough, Zone, service_zone`. Some zone names repeat across IDs, so marts use `zone_id` as the grain, never the name |

**Phase 0 measures and records** in `accuracy_notes`: file sizes, row counts per month, rows after the `trips` filter, distinct boroughs (including `Unknown`/`N/A` values), top 10 pickup zones, and the monthly share paid by card. Slides only show numbers from this measurement, each labelled "2025 data as of <date>".

---

## 5. The course project (the public repo)

### 5.1 Layout at the end of Lesson 4.2

The repo root is the Studio project folder (Studio initialises git there).

```text
nyc_taxi/                         ← Studio project = git repo root (D10 path)
├── .github/workflows/dbt_build.yml   4.1 (Pages job added in 4.2)
├── .gitignore                        3.1
├── README.md                         4.2
├── requirements.txt                  4.1 (pins = Studio's runtime)
├── ci/profiles.yml                   4.1 (prod target, path from env var)
├── scripts/download_data.py          4.1 (CI downloads the 12 files)
├── data/                             gitignored: raw/*.parquet, dev.duckdb (local), prod.duckdb (CI)
├── dbt_project.yml                   Studio template; edited 3.5 and 3.7
├── models/
│   ├── sources.yml                   3.2
│   ├── trips.sql                     3.3 (config view added 3.7)
│   ├── trips_per_month.sql           3.4
│   ├── top_pickup_zones.sql          3.4
│   ├── monthly_summary.sql           3.6
│   └── schema.yml                    3.5, 3.6, 3.8
├── seeds/
│   ├── taxi_zone_lookup.csv          3.2 (downloaded on camera)
│   └── seeds.yml                     3.5, 3.8
└── analyses/ macros/ snapshots/ tests/   template folders (empty)
```

**Final DAG:** `raw.green_trips` (source) → `trips` (view) → `trips_per_month`, `top_pickup_zones`, `monthly_summary` (tables); `taxi_zone_lookup` (seed) → `trips_per_month`, `top_pickup_zones`; `trips_per_month` → `monthly_summary`.

### 5.2 Commits and tags

Each lesson from 3.1 on ends with one commit made on camera and a tag `lesson-<n>-end` (for example `lesson-3-3-end`). `rec.cjs tag` creates the tag **locally** after the take, off camera. **Pushing tags needs Nuri's OK**, asked once in Phase 2; without it, Nuri runs `git push --tags` himself. Tags are:

- the **start state** of the next lesson (section 6.5);
- the **"code for this lesson"** link in each YouTube description;
- the learner's way to compare (like Luke's reference folder).

The full file contents per lesson are in **Appendix A**. Phase 2 (rehearsal) runs every snippet against the real data before any final take.

---

## 6. How the recording works

### 6.1 Surfaces and drivers

| Surface | Driver | Why |
|---|---|---|
| Rosetta DBT Studio (native app) | **Computer use** (full-screen tools during takes) | As asked. Real app, real clicks, real dialogs |
| Code typed in Studio's editor | **CDP typist** (`rec.cjs type`) — Playwright `connectOverCDP` to Studio started with `--remote-debugging-port`; `tameEditor` (pilot code) switches off auto-close, auto-indent and suggestions; types real keystrokes, timed to the beat | Typing through computer use is fast but Monaco's helpers can add brackets and indentation; the pilot proved the tamed path. Fallback: clipboard paste (D8) |
| Finder (move downloads, open DMG) | **Computer use** | Native app |
| Browser (TLC page, GitHub, docs site) | **Playwright** with `channel: 'chrome'` and a dedicated persistent profile, full screen on the stage display | Computer use cannot click in browsers; Playwright gives semantic locators and handles downloads |
| Slides | **Playwright render** (offline, 4K, frame-stepped animations) | Deterministic and sharp; no screen capture needed |

If Phase 0 shows that computer use grants Studio only the **"click" tier** (typing blocked), the typist also handles input fields (file names, commit messages), and computer use keeps clicks and menus.

### 6.2 Machine setup (runner `mac-desktop`)

- Claude desktop app with **Computer use on** (Settings → This computer → Computer use). Claude Code runs as a **local** session in `presentations/`. A cloud session cannot capture the screen: its shell is a Linux VM.
- **Two displays (D6):** the external 4K display is the **stage** (only Studio, Chrome or Finder ever appear there). Claude Desktop and everything else stays on the built-in display.
- **Focus mode on**, notifications off, menu bar auto-hide on the stage, Dock hidden, desktop wallpaper plain dark. Pointer size slightly larger (Accessibility → Display → Pointer size, one notch) so the cursor reads at 1080p.
- **Permissions (Nuri grants once):** Screen & System Audio Recording for the process that runs ffmpeg (Claude); Accessibility for `cliclick`; computer use access for "Rosetta DBT Studio" and "Finder".
- **Homebrew:** `ffmpeg` (avfoundation + videotoolbox), `cliclick`, `node@22`, `python@3.12`, `git`. Tooling: `npm install` (includes Playwright 1.57 dev dependency). Python: `pip install kokoro-onnx soundfile python-pptx pyyaml` (+ `chatterbox-tts` if D4).

### 6.3 Capture

- `rec.cjs take start` runs ffmpeg on the stage display:
  `ffmpeg -f avfoundation -capture_cursor 1 -capture_mouse_clicks 1 -framerate 30 -i "<stage>:none" -vf "crop=3840:2160:<x>:<y>" -c:v h264_videotoolbox -b:v 60M -pix_fmt yuv420p raw.mov`
  - The real cursor is visible and clicks flash.
  - The crop is the app window's bounds, which equal the full stage display in D6 mode.
  - In D6 fallback mode the window is 1600 x 900 pt (3200 x 1800 px) and `compose.py` upscales it with lanczos.
- **Cursor glides:** before every click the cursor glides there smoothly.
  - Computer-use clicks: the agent first calls `rec.cjs glide x y`, which converts screenshot coordinates to screen points with the scale measured in Phase 0 and runs `cliclick -e 400 m:x,y`.
  - Browser clicks: the Playwright driver does the same from the element's box.
  - Either way the cursor never teleports.
- **Every take is a run bundle** (as in `How-to-generate-videos-with-playwrite.md`): `render/takes/<scene>-<n>/{raw.mov, marks.jsonl, events.jsonl, manifest.json, screenshots/}`.
  - `marks.jsonl`: beat start/end/void with wall-clock time.
  - `events.jsonl`: one semantic event per action, e.g. `click menuitem "Seed"`, `type models/trips.sql (612 chars)`, `download green_tripdata_2025-01.parquet`.
  - `manifest.json`: app version, display mode, fps measured, tag, profile path, pass/fail.
- **fps gate:** a take is valid only if the measured fps is 29.5 or higher (frame count over duration). Otherwise fall back to the D6 fallback size. As a last resort, use the pilot's stills recorder (`record.cjs`) for that scene.

### 6.4 Isolation and start states

- `rec.cjs studio launch --state <tag>`:
  1. copies a **profile snapshot** into a fresh `--user-data-dir`;
  2. sets `HOME=/Users/Shared/academy/learner`, which holds its own `.gitconfig` (`user.name "Rosetta Academy"`, a noreply email, `init.defaultBranch main`, `credential.helper store`) and `.git-credentials` written by Nuri;
  3. checks out the project at `<tag>` (`git checkout -f <tag> && git clean -fdx -e data/`) and restores the matching `dev.duckdb` snapshot;
  4. launches `"<release>/Rosetta DBT Studio.app/Contents/MacOS/Rosetta DBT Studio" --user-data-dir=… --remote-debugging-port=9333`;
  5. puts the window full screen on the stage;
  6. **asserts the isolation:** reads `app.getPath('userData')` and `os.homedir()` over CDP, checks that Nuri's own Studio profile folder in `~/Library/Application Support/` has an unchanged mtime, and refuses to continue on any mismatch.
- Profile snapshots (made in Phase 2):
  - `after-setup`: Python and dbt installed by Studio itself in Lesson 2.1;
  - `after-project`: `nyc_taxi` and its DuckDB connection registered.
- localStorage: `dbt-studio-theme-mode` = `"dark"` (JSON) and `dbt-studio-quickstart-tour-seen` = `true` (pilot finding).
- Browser: `profiles/chrome-academy/`, a persistent Playwright profile signed in to the D2 GitHub account by Nuri. Bookmarks bar off, no extensions, downloads go to `learner/Downloads`.

### 6.5 Voice-first fit (how slow computer use becomes a tight video)

1. `tts.py` voices every beat and writes `beats.json` (durations).
2. During a take, computer use works at its own pace. `marks.jsonl` brackets each beat.
3. `cut_take.py` processes each beat window:
   - **Remove idle:** ffmpeg `freezedetect` (`n=0.003:d=0.5`) finds still stretches; keep 0.25 s on each side of every change.
   - **Fit to the voice:** the target is the voice length + 0.35 s lead + 0.6 s tail.
     - Active footage shorter than the target: play at 1x, then hold the last frame.
     - Longer: speed up to 1.5x.
     - Still longer: add a silent pause after the beat's audio and log it. Over 2 s, the beat is flagged and split in `lesson.yaml`.
   - **`wait: true` beats** (installs, CI runs, long `dbt build`): speed up to 12x with a small "sped up" card.
   - **Typist beats:** the typist already sizes its speed to the voice (9 to 30 characters per second, ±20 % jitter), so they are kept at 1x.
4. Voided beats are dropped; the latest valid take of each beat is used.

### 6.6 Compose (v2)

`compose.py` v2 builds the timeline from **clips** (slide build clips + cut app/browser clips) instead of stills:

- Zoom rects per beat (existing `ZOOMS` names + `source-control`, `sql-results`, `finder`, `browser-content`) with 0.7 s ease, done as ffmpeg crop/scale expressions.
- Overlay cards rendered by Playwright as transparent PNGs, faded in 0.3 s.
- Crossfades: scene 0.5 s, slide step 0.4 s.
- Narration mixed and normalised to -16 LUFS, peak -1.5 dBFS.
- Outputs: 4K master (H.264 High 5.1, CRF 16, AAC, faststart) and the 1080p copy (High 4.0, CRF 20, stereo AAC 160k 48 kHz), exactly as the skill specifies.

---

## 7. Slides v2: bigger, full-bleed, professional

Nuri asked for slides that look more professional, cover the whole page, and have bigger, more visible content. v2 keeps the house identity (dark theme, Inter + JetBrains Mono, orange `#ff7a1a` / `#ff9a3d`) but uses the whole canvas.

**Canvas and type (1920 x 1080 CSS, rendered @2x = 4K):**

| Element | v1 (pilot) | v2 |
|---|---|---|
| Title card display | 104 px | 136 to 156 px |
| Slide heading | 64 px | 80 to 88 px |
| Body / bullets | 24 to 32 px | 40 to 44 px (minimum 30 px anywhere) |
| Code | 31 px | 38 to 44 px, at most 14 lines per slide |
| Side margin | 120 px | 72 px safe area; backgrounds and diagrams run full-bleed |

At most 5 bullets and 12 words per bullet. Every slide fills at least 80 % of the canvas: no empty halves.

**Templates** (in `project-01/slides-theme/theme.css` + `theme.js`, shared by all lessons; each lesson's `slides.html` only holds sections):

1. **Section title card:** full-bleed dark gradient with an orange glow, a large module eyebrow (e.g. "dbt BASICS"), a huge title, and the Rosetta DBT Studio lockup bottom-left. Luke uses a similar card; ours keeps our own colours and type.
2. **Statement:** one big sentence (88 px) + one large icon.
3. **Flow diagram:** full-width animated SVG (nodes 220 px+, labels 34 px+), dash-flow arrows, built per sentence.
4. **Code focus:** full-height editor-style panel with a file tab, line highlights stepping per beat, and a short callout column.
5. **Split with real app:** left 40 % text, right 60 % a real 4K Studio frame from the rehearsal, with numbered callouts.
6. **Compare:** two tall columns (view vs table, dev vs prod).
7. **Schema cards:** source and seed column cards joined by the key line (`PULocationID = LocationID`), with real counts.
8. **Recap checklist:** large ticks.
9. **Next lesson / code link:** next title + `github.com/<owner>/nyc-taxi-dbt/tree/lesson-x-y-end`.

**Persistent footer** on content slides (48 px): the white `logo_new.svg` lockup left, "Project 1 · Lesson 3.3" right, thin progress bar.

**Animations "recorded with Playwright":** `render_slides.py` pauses all CSS and SVG animations and steps `document.getAnimations()` `currentTime` at 1/30 s. It screenshots each frame at 4K: perfect, repeatable motion with no live capture.

**Brand kit (`project-01/brand/`)**, copied from `dbt-studio/assets` (identical to `conbined-dbt-project_01/dbt-studio-old-01/assets`):

| File | Use |
|---|---|
| `icon.svg` / `icon.png` (orange stacked database) | App icon on title cards, install lesson |
| `logo_new.svg` / `logo_new.png` (white "DBT Studio" text) | Lockup on dark backgrounds (footer, title cards) |
| `logo_new_04/05/06` (grey text) | Only on light panels |
| `logo_new_01.png`, `logo_sora.png` ("rosetta" wordmark + DBT Studio) | Closing card (on a light card or recoloured) |
| `icons/rosetta.png`, `icons/rosetta-labs.png` | Small marks |
| `icons/dbt-bit_tm.svg` | dbt mark (nominative use, unmodified) |
| `icons/duckdb.svg`, `connectionIcons/duckdb.png` (2000 px) | DuckDB |
| `icons/git.svg`, `icons/git-branch.svg`, `icons/folder.svg`, `icons/flow.svg`, `icons/analytics.png` | Git, files, pipeline, marts |
| `dmg-background.png` | Install visual in 2.1 (only if the 1.7.6 Mac asset is a DMG) |

From the web: **Simple Icons** (CC0-1.0; read their DISCLAIMER: trademarks still belong to their owners) for GitHub, GitHub Actions, Python and Apache Parquet. Icons are unmodified, used only to name the tool, and never imply endorsement. **No NYC or TLC logos:** draw our own taxi and map SVG. No photos of people.

**Slide QA:** contact sheet of every build state per lesson. Check: nothing under 30 px, nothing clipped, nothing within 72 px of an edge, no empty half, numbers sourced.

---

## 8. Voice

- Engine is a course setting: `voice.engine: kokoro | chatterbox | human`. `tts.py` gets an engine adapter.
- **D4 voice comparison (Phase 1, 15 minutes):** voice beats b01 to b04 of Lesson 3.3 with Kokoro `af_heart` 1.0 and Chatterbox (default voice, MPS). Mux each over the same slide clip and send both 1080p clips. Nuri picks; the choice goes into `course.yaml`.
- Pronunciation list: the dbt-Fundamentals list plus `NYC → "N Y C"`, `TLC → "T L C"`, `EWR → "Newark airport"`, `parquet → "par-kay"`, `CSV → "C S V"`, `GitHub → "git hub"`, `CI → "C I"`, `PAT → "personal access token"`. Code names are said as words ("trips per month", "top pickup zones").
- Kokoro speaks about 185 words per minute, so a 6-minute lesson is about 1,000 words. Chatterbox: measure in the comparison.

---

## 9. Lessons

Common to every lesson:

- Title card (3 s) and next-lesson card (4 s).
- Start from the previous tag; end with one commit on camera and the next tag. 2.x and 1.1 have no tag.
- `expect:` checks after each app beat.
- Chapters of 10 s or more.
- Target length in brackets. "CU" = computer use, "PW" = Playwright browser, "TY" = CDP typist.

### 1.1 The project and the data (4:30) — recorded last

Start: `lesson-4-2-end`.

| Scene | Surface | Content |
|---|---|---|
| s01 | Slide (flow) | What you will build: parquet files → `trips` → three marts → tests → docs → GitHub Actions → a warehouse anyone can query |
| s02 | App (CU) | The finished project: open `top_pickup_zones.sql`, LINEAGE depth 2 (zoom `lineage-wide`), Project → Build (`wait: true`), all green |
| s03 | Browser (PW) | The repo README with the green badge, then the docs site lineage graph |
| s04 | Slide (schema cards) | The data: 12 monthly Green taxi files (real total), the zone lookup (real count), joined on pickup zone |
| s05 | Browser (PW) | TLC Trip Record Data page → 2025 → Green Taxi Trip Records links; the Green data dictionary at `payment_type` |
| s06 | Slide | Course map: 4 modules, 13 lessons, "no dbt installed yet: we start from zero" |

### 2.1 Install Rosetta DBT Studio (5:00)

Start: no app in the stage folder, empty profile.

| Scene | Surface | Content |
|---|---|---|
| s01 | Slide | The toolkit: Studio (editor, Project menu, lineage, Source Control, SQL Editor), dbt Core, DuckDB, GitHub |
| s02 | Browser (PW) | `github.com/rosettadb/dbt-studio/releases/tag/1.7.6` → Assets → the Mac asset for this CPU (arm64 or x64), downloaded |
| s03 | App (CU, Finder) | Open the download, drag the app to Applications (D7: ask Nuri first if a copy already exists), open it; handle the Gatekeeper prompt if one appears (verify in Phase 0; narrate it if it appears) |
| s04 | App (CU) | First-run setup: Studio installs Python and dbt (`wait: true`, timelapse). Status bar shows the dbt and Python versions (zoom) |
| s05 | Slide | What was installed and where (versions from the rehearsal) |
| s06 | App (CU) | Home screen tour: New Project, New Connection, Open Project, Settings (verify the 1.7.6 labels) |

After the take: snapshot the profile as `after-setup`.

### 2.2 Git and GitHub (4:00)

| Scene | Surface | Content |
|---|---|---|
| s01 | Slide (statement) | Why analytics code needs version control: history, review, automation |
| s02 | Slide (flow, own design) | Working folder → staged changes → commits → GitHub; push and pull arrows; the Studio control for each step (commit box, Publish Branch, Push, Pull/Sync Changes) |
| s03 | Browser (PW) | GitHub → New repository → `nyc-taxi-dbt`, Public, no README, .gitignore or licence → Create → the HTTPS URL is shown and copied |
| s04 | Slide | Credentials: username + fine-grained personal access token for this repo (Contents: read/write, **Workflows: read/write**, needed in 4.1). Token page shown only as a redacted mock |
| s05 | Slide | Git on a Mac: installed with the Command Line Tools (verify what Studio shows if git is missing) |

### 3.1 Create the dbt project (7:00)

Start: `after-setup` profile.

| Scene | Surface | Content |
|---|---|---|
| s01 | Slide | Anatomy of a dbt project (folders, `dbt_project.yml`), profile → target → `dev` = a DuckDB file |
| s02 | App (CU) | New Project → **Setup New Project**: Project Name `nyc_taxi`, Project Path (D10), Connection → New Connection → Connection Type DuckDB, file `data/dev.duckdb` (verify the field and whether `data/` is created), **Create template dbt directories** on → create |
| s03 | App (CU) | Explorer tour; open `dbt_project.yml` (zoom `editor-code`): name, profile, paths |
| s04 | App (CU) | TERMINAL → `dbt debug` → all checks pass (zoom `terminal`) |
| s05 | App (CU + TY) | New File `.gitignore` at the root → typed (A1) → Save |
| s06 | App (CU) | Source Control → Initialize Repository → changes listed → message "Create the nyc_taxi dbt project" → Commit → Add remote `origin` (Add Git Remote dialog; find its entry point in Phase 2) → Publish Branch |
| s07 | Browser (PW) | Refresh the repo page: the files are on GitHub |

End: `lesson-3-1-end`; snapshot `after-project`.

### 3.2 Get the data (5:30)

| Scene | Surface | Content |
|---|---|---|
| s01 | Slide (flow) | Raw files stay out of git; DuckDB reads parquet in place; a **source** names them; a **seed** is a small CSV that lives in the repo |
| s02 | Browser (PW) | TLC page → 2025 → January → Green Taxi Trip Records → download. February to December follow as a fast montage (auto-cut). Then Taxi Zone Lookup Table (CSV) |
| s03 | App (CU, Finder) | Downloads → the 12 parquet files → new folder `data/raw/` in the project; the CSV → `seeds/` |
| s04 | App (CU) | Studio Explorer shows both. Source Control lists only the CSV: `data/` is ignored (a teaching moment) |
| s05 | App (CU + TY) | New File `models/sources.yml` → typed (A2) → Save |
| s06 | App (CU) | SQL Editor: `select count(*) from read_parquet('data/raw/*.parquet')` — **only if the relative path resolves from Studio** (Phase 2 check); otherwise the count goes on the s01 slide |
| s07 | App (CU) | Commit "Declare the raw trips source and add the zone lookup" → Push / Sync Changes |

### 3.3 Models (6:00) — pilot lesson

| Scene | Surface | Content |
|---|---|---|
| s01 | Slide (statement) | A model is one `select` in one `.sql` file; dbt builds an object named after the file |
| s02 | App (CU + TY) | New File `models/trips.sql` → typed (A3) → Save |
| s03 | Slide (flow, own design) | How a model runs: compile → wrap in `create view … as` → execute in DuckDB |
| s04 | App (CU) | Project → Run → terminal "OK created sql view model main.trips" (zoom `terminal`) |
| s05 | App (CU) | SQL Editor: `select pickup_at, pickup_zone_id, trip_distance, total_amount from trips limit 10` (timestamp and number columns only; the 1.7.5 grid showed DATE columns as `{"days": N}`) |
| s06 | App (CU) | `target/run/.../trips.sql`: the `create view` dbt wrote |
| s07 | Slide + app | Recap; commit "Add the trips staging model" → Push |

### 3.4 Dependencies & Jinja (6:30)

| Scene | Surface | Content |
|---|---|---|
| s01 | App (CU) | Project → Seed → `taxi_zone_lookup` loaded (zoom `terminal`) |
| s02 | Slide | `ref()`: name the model or seed, not the table; it records a dependency |
| s03 | App (CU + TY) | New `models/trips_per_month.sql` (A4) → Save |
| s04 | App (CU + TY) | New `models/top_pickup_zones.sql` with `{% set top_n = 10 %}` (A5) → Save |
| s05 | Slide (code focus) | Jinja in one minute: `{{ }}`, `{% %}`, `{# #}`; compile turns it into plain SQL |
| s06 | App (CU) | Project → Compile → open `target/compiled/nyc_taxi/models/top_pickup_zones.sql`: `limit 10` and the full table names (zoom) |
| s07 | App (CU) | Project → Run → order shown in the terminal. Open `trips_per_month.sql` → LINEAGE (switch files once after compiling; the pilot found the lookup is cached) → depth 2 shows the source and the seed |
| s08 | App (CU) | Commit + push |

### 3.5 Properties (5:30)

| Scene | Surface | Content |
|---|---|---|
| s01 | Slide | Properties = YAML beside your models: descriptions, columns, tests, config. Sources go in `sources.yml`, models in `schema.yml`, seeds in `seeds/seeds.yml` |
| s02 | App (CU + paste) | New `models/schema.yml` (A6, pasted per D8) → Save; new `seeds/seeds.yml` (typed) → Save |
| s03 | App (CU + TY) | `dbt_project.yml`: add `+persist_docs` (A6) → Save → Project → Run |
| s04 | App (CU) | SQL Editor: `select table_name, column_name, comment from duckdb_columns() where table_name = 'trips_per_month'` → descriptions inside the database. **Only if dbt-duckdb persists comments in the rehearsal**; otherwise cut the scene |
| s05 | Slide | Where descriptions show up: docs site, database comments, every reviewer |
| s06 | App (CU) | Commit + push |

### 3.6 Docs & the DAG (6:00)

| Scene | Surface | Content |
|---|---|---|
| s01 | App (CU + TY) | New `models/monthly_summary.sql` (A7, two refs) → Save; append its `schema.yml` entry (paste) → Save |
| s02 | Slide (flow) | DAG: directed, acyclic; order, parallel runs, impact analysis |
| s03 | App (CU) | Project → Run → `monthly_summary.sql` → LINEAGE depth 2 (zoom `lineage-wide`) |
| s04 | App (CU) + Browser (PW) | Project → Generate Docs → Serve Docs. **If Studio opens the system browser** (Nuri's real Chrome), cover that window. Before the take, set the isolated profile so the docs URL opens in the recording Chrome profile instead (Phase 2 decides how; never show Nuri's browser). Docs: model page, column descriptions, lineage graph |
| s05 | App (CU) | Commit + push |

### 3.7 Materializations (5:00)

| Scene | Surface | Content |
|---|---|---|
| s01 | Slide (compare) | View vs table: storage, freshness, speed; incremental and ephemeral named as "later" |
| s02 | App (CU) | SQL Editor: `select table_name, table_type from information_schema.tables where table_schema = 'main' order by 1` → everything is a VIEW |
| s03 | App (CU + TY) | `dbt_project.yml`: `+materialized: table` (A8); `trips.sql`: first line `{{ config(materialized='view') }}` → Save both |
| s04 | App (CU) | Project → Run → "table model" and "view model" in the log; re-run the query → marts are BASE TABLE, `trips` is VIEW |
| s05 | Slide | Why `trips` stays a view here, and the marts become tables |
| s06 | App (CU) | Commit + push |

### 3.8 Tests (6:00)

| Scene | Surface | Content |
|---|---|---|
| s01 | Slide | A data test is a query that returns bad rows; `unique`, `not_null`, `accepted_values`, `relationships`; grain |
| s02 | App (CU + paste) | Add tests (A9) to `schema.yml` and `seeds.yml` → Save |
| s03 | App (CU) | Project → Test → one deliberate FAIL (zoom `terminal`). **Phase 2 picks the failure that the real data gives:** an `accepted_values` list for `borough` that misses a value present in 2025, or else `unique` on the wrong grain |
| s04 | App (CU) | Open the failing test's compiled SQL in `target/compiled/…`, run it in the SQL Editor → the bad rows |
| s05 | App (CU + TY) | Fix the YAML → Project → Test → all PASS |
| s06 | Slide | `build` = run + test in DAG order; a failing test stops what depends on it |
| s07 | App (CU) | Project → Build → green → commit + push. Tag `lesson-3-8-end` = end of dbt Basics |

### 4.1 Ship & Automate (7:00)

| Scene | Surface | Content |
|---|---|---|
| s01 | Slide (compare) | dev vs prod targets; CI = a clean machine that builds and tests every push |
| s02 | App (CU + TY/paste) | New files (A10): `requirements.txt` (typed), `ci/profiles.yml` (typed), `scripts/download_data.py` (pasted), `.github/workflows/dbt_build.yml` (pasted) → Save each |
| s03 | Slide (code focus) | The workflow, step by step: triggers (push, Monday, manual), install, download, `dbt build --profiles-dir ci`, publish `prod.duckdb` |
| s04 | App (CU) | Source Control → commit "Add CI: build, test and publish the warehouse" → Push |
| s05 | Browser (PW) | Repo → Actions → the run (`wait: true` timelapse) → green → Releases → `warehouse` → `prod.duckdb` |
| s06 | Slide | What just happened; the badge comes next lesson |

### 4.2 Showcase (6:00)

| Scene | Surface | Content |
|---|---|---|
| s01 | Slide | A portfolio project: README, live docs, green badge, data anyone can query |
| s02 | Browser (PW) | Repo Settings → Pages → Source: GitHub Actions (one-time; must come before the push) |
| s03 | App (CU + paste) | Add the Pages job to the workflow (A11) and `README.md` (A11, then type the owner/repo names) → commit "Publish docs and README" → Push |
| s04 | Browser (PW) | Actions run green → Pages URL → docs lineage on the public site → README with badge and query block |
| s05 | App (CU) | Studio SQL Editor (DuckDB): `install httpfs; load httpfs; attach '<release URL>' as taxi (read_only); select * from taxi.main.top_pickup_zones;` → results. **Verify in Phase 2 that the DuckDB SQL Editor accepts ATTACH**; the README shows the same SQL for the `duckdb` CLI |
| s06 | Slide | Project 1 recap checklist |

---

## 10. Tooling work (in `_academy-video-tooling/`, one change set, about 2,000 to 2,600 lines)

| File | New/changed | What it does | Acceptance test |
|---|---|---|---|
| `rec.cjs` | New | CLI for computer-use takes: `env check`, `studio launch/quit --state`, `take start/stop`, `mark`, `glide`, `type`, `browser`, `check`, `tag` | `env check` prints display, fps, permissions and versions; a 10 s test take passes the fps gate |
| `lib/mac.cjs` | New | Stage display detection (`system_profiler SPDisplaysDataType -json`), window bounds, ffmpeg avfoundation start/stop, `cliclick` glide, screenshot-to-points scale | Crop matches the window ±2 px; glide lands within 3 px |
| `lib/typist.cjs` | New | `connectOverCDP`, reuse `tameEditor` from `lib/actions.cjs`, type a snippet at a speed sized to the beat's voice; clipboard-paste fallback; returns a diff of editor text vs snippet | Typing A5 gives a byte-identical file on disk |
| `lib/browser.cjs` | New | Persistent Chrome profile, full screen on the stage, semantic steps (`goto`, `click {role,name}`, `scroll_to`, `hover`, `download {save_to}`, `wait_for`), cursor glides, `events.jsonl` | The TLC download step saves the file and logs one event |
| `lib/studio.cjs` | Changed | Mac launch path (`.app/Contents/MacOS/...`), `HOME` + `--user-data-dir` + `--remote-debugging-port`, profile snapshots, isolation assertions | Launch refuses if `userData` is not the throwaway path |
| `scripts/cut_take.py` | New | `freezedetect` idle removal, fit-to-voice (1x / hold / 1.5x / wait 12x), per-beat clips, cut report | Report lists every beat with ratio and flags |
| `scripts/render_slides.py` | New (keeps `render_stills.py` for the pilot course) | Theme v2, frame-stepped animations, per-step clips, cards as PNG, thumbnail | Contact sheet of all states; one 2 s animation clip at 30 fps |
| `scripts/compose.py` | Changed | v2 timeline of clips, eased zoom via ffmpeg, cards, crossfades, wait badge, upscaling for D6 fallback | `--preview 45` renders; ffprobe checks pass |
| `scripts/tts.py` | Changed | Engine adapter (`kokoro`, `chatterbox`, `human`) | Same beat in both engines |
| `scripts/script_from_lesson.py`, `scripts/package.py` | Changed | Describe the new actions (`do`, `type`, `browser`, `wait`); write the repo tag link into `youtube.md` | Beat sheet shows the steps in plain words |
| `README.md`, `DESIGN.md` | Changed | Document the `mac-desktop` + computer-use runner and the pilot findings | — |

**`lesson.yaml` additions** (everything else stays as in the skill):

```yaml
start_state: lesson-3-2-end          # git tag of the course repo (+ dev.duckdb snapshot)
scenes:
  - id: s02
    kind: app                        # live capture on the stage display
    driver: computer-use             # or: playwright-electron (pilot fallback)
    beats:
      - id: b05
        say: "In the models folder, create a new file called trips dot sequel."
        do:                          # plain-language steps for computer use, using real labels
          - "Explorer: right-click models → New File"
          - "Type the name trips.sql, click Save"
        expect: { file_exists: models/trips.sql }
      - id: b06
        say: "Start with the columns we need from the raw trips source..."
        type: { snippet: snippets/3.3/trips.sql, part: 1 }   # CDP typist; paste: true for long files
        expect: { file_equals_snippet: true }
        zoom: editor-code
        card: { eyebrow: "A model", title: "One select, one file", pos: top-right }
      - id: b08
        say: "Save it, then open the Project menu and choose Run."
        do: ["Click Save", "Project split-button arrow → Run"]
        wait: true                   # allows timelapse speed-up
        expect: { run_results: success }
  - id: s03
    kind: browser
    beats:
      - id: b12
        say: "..."
        browser:
          - goto: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
          - click: { role: button, name: "2025" }          # verify labels in Phase 2
          - download: { link: "Green Taxi Trip Records", near: "January", save_to: "~/Downloads" }
```

---

## 11. Execution phases

### Phase 0: Prechecks (Nuri present, about 1 hour)

1. Nuri opens Claude desktop → Code → **local** session in `presentations/`. Pastes the **Phase 0 kickoff** (below).
2. Claude Code checks and writes `project-01/precheck.md`:
   - the computer-use tools are present in this local session (if not: stop and tell Nuri to turn on Computer use in Settings → This computer);
   - macOS version, CPU (pick the arm64/x64 release asset), displays (D6 mode), Homebrew tools.
   - Studio 1.7.6 release assets (zip or DMG).
   - Studio's default Python, dbt and dbt-duckdb versions (from a throwaway first run) → `course.yaml.runtime` + `requirements.txt` pins.
   - Computer use access + tier for "Rosetta DBT Studio" and "Finder".
   - Screen-recording permission, a 10 s test take (fps, crop, no control overlay from Claude inside the crop, cursor and click flash visible).
   - CDP attach + typist test into a scratch file.
   - Isolation assertions.
   - Green 2025 files: sizes, row counts, columns.
   - Zone CSV, Green data dictionary URL, NYC Open Data terms link.
3. Nuri, by hand:
   - creates the D2 GitHub account or org (if new) and **signs in to it in the recording Chrome profile** (`rec.cjs browser login` opens it);
   - creates the fine-grained token (Contents RW + Workflows RW on `nyc-taxi-dbt` and `nyc-taxi-dbt-rehearsal`) and writes it into `/Users/Shared/academy/learner/.git-credentials` himself;
   - creates the private rehearsal repo.

```text
Phase 0 kickoff (paste into Claude Code):
Use the rosetta-academy-video skill and presentations/nuries-youtube-clones/project-01/plan-dbt-project01.md.
Runner: mac-desktop with computer use. Do Phase 0 only and write project-01/precheck.md.
You may take full-screen control only for the 10-second test take. Do not change dbt-studio/.
Do not run git write commands in presentations/.
```

### Phase 1: Tooling (Claude Code, about 1 working day)

- Build section 10 with each acceptance test.
- Create `project-01/course.yaml` (Appendix B), `slides-theme/`, `brand/`, `snippets/` (Appendix A, one folder per lesson), `studio-notes.md`, `.gitignore` (same as the dbt-Fundamentals course + `render/`, `profiles/`, `takes/`).
- Run the **D4 voice comparison** and send both clips.
- Output: a short report to Nuri with a suggested commit message for `presentations/`.

### Phase 2: Rehearsal, "do the project" (Claude Code with computer use, about half a day)

- With full-screen control, Claude Code performs **all 13 lessons' steps end to end** in the isolated Studio, pushing to the **rehearsal** repo. Low-quality test captures are allowed.
- It records real labels and every surprise in `studio-notes.md`: Add Remote entry point, auth prompts, Serve Docs behaviour, SQL Editor relative paths and ATTACH, `persist_docs`, the deliberate test failure, the 1.7.6 branch-after-init display.
- It validates every snippet (`dbt build` green, CI green on the rehearsal repo, Pages live) and measures the numbers for slides.
- It saves: profile snapshots, a `dev.duckdb` per tag, reference 4K screenshots for slides (`brand/app-frames/`).
- Then it writes **`lesson.yaml` + `slides.html` for every lesson** and generates beat sheets and slide contact sheets.
- If a factual claim differs from this plan (versions, behaviour), flag it in `studio-notes.md` and hold that lesson (skill rule).

### Phase 3: Pilot, Lesson 3.3 Models (about 2 hours)

- Approval gate: send the 3.3 beat sheet + slide contact sheet; wait for "approved".
- Then voice, a final take from `lesson-3-2-end` **against the rehearsal repo**, cut, compose, package, verify.
- Send the 1080p clip (plays on phones) and the 4K master. Nuri judges: look of the slides, cursor and typing feel, pace, voice, zooms.
- Tune the tooling. Do not start Phase 4 until Nuri approves the pilot look.

### Phase 4: Production (in lesson order, because final takes push to the public repo)

| Batch | Lessons | Approval |
|---|---|---|
| A | 2.1, 2.2, 3.1, 3.2 | One message with 4 beat sheets + contact sheets |
| B | 3.3 (re-take against the public repo, reusing the approved script), 3.4 to 3.8 | One message |
| C | 4.1, 4.2, then 1.1 (needs the finished repo) | One message |

For each lesson after approval:

1. `tts.py`
2. `studio launch --state <prev tag>`
3. take each scene (all `expect:` checks pass; a failed check means re-taking that scene from its state)
4. `rec.cjs tag`
5. `cut_take.py`
6. `render_slides.py`
7. `compose.py --preview 45`, look at frames, then the full render
8. `package.py`
9. verify (section 12)
10. deliver

A push is always the **last beat** of a take, so a failed take never leaves the public repo ahead of the video. If a lesson must be re-taken after its push, ask Nuri before any force-push.

```text
Phase 4 kickoff (per batch):
Use the rosetta-academy-video skill and project-01/plan-dbt-project01.md. Runner mac-desktop.
Batch B is approved: produce lessons 3.3 to 3.8 in order. You may take full-screen control for recording takes.
Push only through Studio's Source Control on camera, to the public repo. No force-push.
Do not change dbt-studio/ and do not run git write commands in presentations/.
```

### Phase 5: Course package

- Playlist order, consistent thumbnails.
- Every `youtube.md` gets: summary, chapters, "Code for this lesson: <tag link>", Studio download link, credit line (D9), tags.
- A course `README` section in the public repo listing lessons, for Nuri to add video links after upload.

### Phase 6: Follow-up (optional)

Propose an update to the `rosetta-academy-video` skill (via a skill card) that adds the `mac-desktop` + computer-use runner, the drivers table, the cut rules and the slide v2 theme.

---

## 12. QA and acceptance

**Per take (automatic):** fps ≥ 29.5; crop equals window bounds; every beat has start/end marks; every `expect:` passes; `events.jsonl` has a semantic locator or `do:` step for every action; the isolation assertions passed at launch.

**Per lesson (Claude Code looks):**

- 4K file: 3840x2160 H.264 + AAC, duration = timeline total.
- 1080p file: 1920x1080, High, level 40, stereo AAC, about 3 MB/min.
- Loudness about -16 LUFS, peak about -1.5 dBFS.
- A contact sheet of about 16 frames across all scenes (typing, menus, terminal, zooms, cards, lineage, browser, every slide build).
- Check for: no notification or foreign window, no personal path/email/token/bookmark, no AI panel, cursor visible and gliding, text readable at 1080p, `cut_take` report with no beat stretched past 1.5x (except `wait` beats).

**Lesson accepted when:**

- the narration matches what is on screen (no invented steps);
- the repo tag exists and its files equal the lesson's snippets;
- for 4.x, the Actions run is green and the release asset or Pages site loads;
- Nuri has listened once for pronunciation.

---

## 13. Deliverables and folder layout

```text
presentations/nuries-youtube-clones/project-01/
  plan-dbt-project01.md      this plan
  precheck.md                Phase 0 results
  course.yaml                Appendix B
  studio-notes.md            real labels + surprises (replaces draft-corrections.md for this course)
  brand/                     asset kit + app-frames/ from the rehearsal
  slides-theme/              theme.css, theme.js (v2)
  snippets/<lesson>/         exact files typed or pasted on camera (Appendix A)
  lesson-1-1-project-and-data/ … lesson-4-2-showcase/
      lesson.yaml  slides.html  voiceover-script.md  voiceover-<engine>.txt  timeline.json
      <id>.mp4 (4K)  <id>-1080p.mp4  <id>.srt  <id>.vtt  <id>-slides.pptx
      youtube.md  thumbnail.png  RECORDING-cue-sheet.md  readme.md
      render/                (gitignored: takes, clips, frames, audio)
```

**Delivery** (mac-desktop): files are written in place; Claude Code reports paths. It sends the **1080p copy first** for viewing, telling Nuri: "1080p plays on phones; the 4K file is for YouTube". Upload the 4K MP4 unlisted with the `.srt`. YouTube shows HD/4K only after processing.

---

## 14. Risks and fallbacks

| Risk | Fallback |
|---|---|
| Computer use is slow (seconds per action) | Expected: idle is cut out (6.5); takes are bracketed per beat |
| Studio granted only "click" tier | Typist handles all typing; computer use clicks |
| CDP port blocked in the packaged app | Clipboard paste for code (D8) and computer-use typing for short fields |
| Live capture below 29.5 fps | D6 fallback size; last resort the pilot's stills recorder (`record.cjs`) for that scene |
| Claude's control overlay or a notification inside the crop | Two-display setup, Focus mode; re-take the scene |
| 1.7.6 does not show the branch after Initialize Repository (fixed after 1.7.6, not released yet) | Narrate the refresh workaround, or wait for the next release (D11) |
| Serve Docs opens Nuri's real browser | Open the docs URL in the recording profile instead (3.6) |
| GitHub asks for credentials on camera | Pre-stored in the isolated credential store; auth explained on a slide (2.2) |
| Push of workflow file rejected | Token needs **Workflows: read/write** (2.2, Phase 0) |
| TLC page layout changes / CloudFront refuses scripts | Download step uses the pinned URLs; `download_data.py` sends a User-Agent header; CI failure is caught in rehearsal |
| TLC republishes 2025 files and numbers drift | Slides say "as of <date>"; `accuracy_notes` keep the measured counts |
| Kokoro sounds robotic | D4 comparison; human voice path stays available |
| Retake needed after a public push | Ask Nuri; never force-push on our own |

---

## Appendix A: Project files by lesson (validate all in Phase 2)

**A1 `.gitignore` (3.1)**

```text
target/
dbt_packages/
logs/
data/
*.duckdb
*.duckdb.wal
.env
```

**A2 `models/sources.yml` (3.2)**

If dbt warns that `external_location` is an unknown config key, move it under `config: meta:` and record the working form in `studio-notes.md`.

```yaml
sources:
  - name: raw
    description: NYC TLC green taxi trip records for 2025, read in place from data/raw.
    tables:
      - name: green_trips
        description: One row per green taxi trip, as reported to the TLC.
        config:
          external_location: "read_parquet('data/raw/green_tripdata_2025-*.parquet', union_by_name = true)"
```

**A3 `models/trips.sql` (3.3; line 1 added in 3.7)**

```sql
{{ config(materialized='view') }}   -- added in 3.7

-- one row per 2025 green taxi trip, obviously broken rows removed
select
    VendorID              as vendor_id,
    lpep_pickup_datetime  as pickup_at,
    lpep_dropoff_datetime as dropoff_at,
    PULocationID          as pickup_zone_id,
    DOLocationID          as dropoff_zone_id,
    passenger_count,
    trip_distance,
    payment_type,
    fare_amount,
    tip_amount,
    total_amount
from {{ source('raw', 'green_trips') }}
where lpep_pickup_datetime >= '2025-01-01'
  and lpep_pickup_datetime <  '2026-01-01'
  and trip_distance > 0
  and total_amount > 0
```

**A4 `models/trips_per_month.sql` (3.4)**

```sql
-- trips per month and pickup borough
select
    date_trunc('month', t.pickup_at) as month,
    z.Borough                        as borough,
    count(*)                         as trips,
    round(avg(t.fare_amount), 2)     as avg_fare
from {{ ref('trips') }} as t
left join {{ ref('taxi_zone_lookup') }} as z
    on t.pickup_zone_id = z.LocationID
group by all
order by month, borough
```

**A5 `models/top_pickup_zones.sql` (3.4)**

```sql
-- the busiest pickup zones of 2025
{% set top_n = 10 %}

select
    t.pickup_zone_id as zone_id,
    z.Zone           as zone,
    z.Borough        as borough,
    count(*)         as trips
from {{ ref('trips') }} as t
join {{ ref('taxi_zone_lookup') }} as z
    on t.pickup_zone_id = z.LocationID
group by all
order by trips desc
limit {{ top_n }}
```

**A6 Properties (3.5)**

`dbt_project.yml`: add under the project's `models:` key (the project name comes from Studio's template):

```yaml
models:
  nyc_taxi:
    +persist_docs:
      relation: true
      columns: true
```

`models/schema.yml`:

```yaml
models:
  - name: trips
    description: Cleaned 2025 green taxi trips; one row per trip. Rows with no distance or no charge are removed.
    columns:
      - name: pickup_at
        description: When the meter started.
      - name: pickup_zone_id
        description: TLC taxi zone where the trip started (joins taxi_zone_lookup.LocationID).
      - name: payment_type
        description: TLC payment code; 1 is credit card (see the data dictionary).
      - name: total_amount
        description: Total charged to the rider, in US dollars.
  - name: trips_per_month
    description: Trips and average fare per month and pickup borough.
    columns:
      - name: month
        description: Month of pickup.
      - name: borough
        description: Pickup borough from the zone lookup.
      - name: trips
        description: Trips that month from that borough.
  - name: top_pickup_zones
    description: The ten busiest pickup zones of 2025.
    columns:
      - name: zone_id
        description: TLC zone id; the grain of this table.
      - name: trips
        description: Trips that started in the zone.
```

`seeds/seeds.yml`:

```yaml
seeds:
  - name: taxi_zone_lookup
    description: TLC taxi zones, from the Taxi Zone Lookup Table on the TLC site.
    columns:
      - name: LocationID
        description: Zone id used by PULocationID and DOLocationID.
```

**A7 `models/monthly_summary.sql` (3.6)** + schema entry

```sql
-- one row per month: total trips and the share paid by card
with totals as (
    select month, sum(trips) as total_trips
    from {{ ref('trips_per_month') }}
    group by month
),
card as (
    select date_trunc('month', pickup_at) as month, count(*) as card_trips
    from {{ ref('trips') }}
    where payment_type = 1   -- credit card
    group by month
)
select
    month,
    total_trips,
    card_trips,
    round(100.0 * card_trips / total_trips, 1) as pct_card
from totals
join card using (month)
order by month
```

```yaml
  - name: monthly_summary
    description: One row per month of 2025 with total trips and the share paid by card.
    columns:
      - name: month
        description: Month of pickup; the grain.
      - name: pct_card
        description: Percent of the month's trips paid by credit card.
```

**A8 `dbt_project.yml` (3.7)**

```yaml
models:
  nyc_taxi:
    +materialized: table
    +persist_docs:
      relation: true
      columns: true
```

**A9 Tests (3.8)**

Add `data_tests:` under the existing columns; final values are chosen after the rehearsal. The `accepted_values` list starts **missing one borough present in the data**, to fail on purpose.

```yaml
      - name: month            # monthly_summary
        data_tests: [not_null, unique]
      - name: zone_id          # top_pickup_zones
        data_tests: [not_null, unique]
      - name: borough          # trips_per_month
        data_tests:
          - accepted_values:
              arguments:
                values: ['Bronx', 'Brooklyn', 'EWR', 'Manhattan', 'Queens', 'Staten Island', 'Unknown']
      - name: LocationID       # seeds.yml
        data_tests: [not_null, unique]
```

On dbt Core 1.12, check whether `accepted_values` takes `values:` directly or under `arguments:` and keep the form that parses without warnings. Record it in `studio-notes.md`.

**A10 CI files (4.1)**

`requirements.txt` (pins = Studio's runtime from Phase 0):

```text
dbt-core==<from Phase 0>
dbt-duckdb==<from Phase 0>
```

`ci/profiles.yml` (the profile name must match `dbt_project.yml`):

```yaml
nyc_taxi:
  target: prod
  outputs:
    prod:
      type: duckdb
      path: "{{ env_var('DUCKDB_PATH') }}"
      threads: 4
```

`scripts/download_data.py`:

```python
"""Download the 2025 NYC TLC green taxi trip files into data/raw/. Run from the repo root."""
import urllib.request
from pathlib import Path

BASE = "https://d37ci6vzurychx.cloudfront.net/trip-data"
RAW = Path("data/raw")

RAW.mkdir(parents=True, exist_ok=True)
for month in range(1, 13):
    name = f"green_tripdata_2025-{month:02d}.parquet"
    target = RAW / name
    if target.exists():
        print("have", name)
        continue
    print("downloading", name)
    request = urllib.request.Request(f"{BASE}/{name}", headers={"User-Agent": "nyc-taxi-dbt-course"})
    with urllib.request.urlopen(request) as response:
        target.write_bytes(response.read())
print("done")
```

`.github/workflows/dbt_build.yml`. Before 4.1, check each action's current major version on its GitHub page and update the pins:

```yaml
name: dbt build & publish
on:
  push:
    branches: [main]
  schedule:
    - cron: '23 5 * * 1'     # every Monday
  workflow_dispatch:
permissions:
  contents: write
jobs:
  build:
    runs-on: ubuntu-latest
    env:
      DUCKDB_PATH: ${{ github.workspace }}/data/prod.duckdb
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
          cache: pip
      - run: pip install -r requirements.txt
      - run: python scripts/download_data.py
      - run: dbt seed --profiles-dir ci
      - run: dbt build --profiles-dir ci
      - name: Publish the warehouse
        run: |
          gh release create warehouse --title "Warehouse" --notes "Built by dbt on every push" || true
          gh release upload warehouse data/prod.duckdb --clobber
        env:
          GH_TOKEN: ${{ github.token }}
```

(`dbt build` already runs seeds; the separate `dbt seed` line is optional. Keep it only if it makes the narration clearer.)

**A11 Showcase (4.2)**

Workflow additions:

```yaml
      # in job "build", after "Publish the warehouse":
      - run: dbt docs generate --profiles-dir ci
      - run: mkdir site && cp target/index.html target/manifest.json target/catalog.json site/
      - uses: actions/upload-pages-artifact@v3
        with:
          path: site
  docs:
    needs: build
    runs-on: ubuntu-latest
    permissions:
      pages: write
      id-token: write
    environment:
      name: github-pages
      url: ${{ steps.deploy.outputs.page_url }}
    steps:
      - id: deploy
        uses: actions/deploy-pages@v4
```

`README.md` (outline, our wording):

- title + badge (`actions/workflows/dbt_build.yml/badge.svg`) + "docs live" badge;
- one-paragraph summary;
- a "What I built / How / Where to look" table (pipeline, tests, docs, CI, environments, published warehouse);
- DAG image (Studio LINEAGE frame);
- "Query the warehouse": `install httpfs; load httpfs; attach 'https://github.com/<owner>/nyc-taxi-dbt/releases/download/warehouse/prod.duckdb' as taxi (read_only); select * from taxi.main.top_pickup_zones;` Note: only the marts are tables; `trips` is a view over local files;
- "Run it yourself" (Rosetta DBT Studio link, or pip + `dbt build`);
- "Data": NYC TLC, link to the page and the terms;
- credit line (D9).

---

## Appendix B: `course.yaml` (draft)

```yaml
title: "dbt + DuckDB in Rosetta DBT Studio"
subtitle: "Project 1: NYC taxi trips, from raw files to a tested, automated pipeline"
series: nuries-youtube-clones/project-01
inspired_by: "Luke Barousse, dbt for Data Analytics & Engineering (Project #1)"

app:
  name: Rosetta DBT Studio
  version: 1.7.6
  release_url: https://github.com/rosettadb/dbt-studio/releases/tag/1.7.6
  assets: { mac_arm64: "<from Phase 0>", mac_x64: "<from Phase 0>" }

runner: mac-desktop
capture: { mode: live, display: stage, window_pt: [1920, 1080], fps: 30, cursor: real, click_flash: true }
drivers: { app: computer-use, code: cdp-typist, browser: playwright-chrome, slides: playwright-render }
theme: dark-v2

runtime: { python: "<Phase 0>", dbt_core: "<Phase 0>", dbt_duckdb: "<Phase 0>" }

dataset:
  name: NYC TLC Green Taxi Trip Records 2025
  base_url: https://d37ci6vzurychx.cloudfront.net/trip-data/
  files: green_tripdata_2025-01.parquet … green_tripdata_2025-12.parquet
  seed_url: https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv
  page: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

course_repo:
  public: https://github.com/<owner>/nyc-taxi-dbt
  rehearsal: https://github.com/<owner>/nyc-taxi-dbt-rehearsal
  tag: "lesson-{number}-end"
  learner_home: /Users/Shared/academy/learner
  project_path: /Users/Shared/academy/learner/projects/nyc_taxi

voice: { engine: kokoro, voice: af_heart, speed: 1.0 }   # D4 may switch to chatterbox
video: { width: 3840, height: 2160, fps: 30, crf: 16, title_card_s: 3, closing_card_s: 4 }
youtube: { visibility: unlisted, playlist: "dbt + DuckDB in Rosetta DBT Studio: Project 1",
           tags: [dbt, dbt core, DuckDB, analytics engineering, Rosetta DBT Studio, NYC taxi, GitHub Actions, SQL] }

pronunciation:   # dbt-Fundamentals list, plus:
  - [ '\bNYC\b', 'N Y C' ]
  - [ '\bTLC\b', 'T L C' ]
  - [ '\bEWR\b', 'Newark airport' ]
  - [ '\bparquet\b', 'par-kay' ]
  - [ '\bCSV\b', 'C S V' ]
  - [ '\bGitHub\b', 'git hub' ]
```

---

## Appendix C: Sources checked for this plan (9 Nov 2026)

- Luke Barousse course repo, `project_1/` (README, models, `schema.yml`, `ci/profiles.yml`, workflow, snippets): `github.com/lukebarousse/dbt_Analytics_Engineering_Course`
- NYC TLC Trip Record Data page (file URLs, zone lookup, data dictionary, notes): `nyc.gov/site/tlc/about/tlc-trip-record-data.page`
- dbt-duckdb README (`external_location` in source `meta` or table `config`; `path` resolution): `github.com/duckdb/dbt-duckdb`
- dbt Core v2 announcement (first alpha 1 Jun 2026; v1 not forced to upgrade): `docs.getdbt.com/blog/dbt-core-v2-is-here`
- Chatterbox (MIT licence, MPS support, Perth watermark): `github.com/resemble-ai/chatterbox`
- Simple Icons (CC0-1.0 + trademark disclaimer): `github.com/simple-icons/simple-icons`
- Rosetta DBT Studio source at tag 1.7.6 (read-only): Source Control labels, Add Git Remote dialog, Setup New Project fields, Project menu items, default Python 3.10.17 / build 20250409
- Existing tooling: `_academy-video-tooling/DESIGN.md`, `README.md`, pilot `lesson-3-2` files, `How-to-generate-videos-with-playwrite.md`
