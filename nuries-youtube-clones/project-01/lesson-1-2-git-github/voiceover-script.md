# Git and GitHub — voice-over script and beat sheet

dbt + DuckDB in Rosetta DBT Studio · Module 1 · Set up · next: Lesson 2.1 · Create the dbt project

App: Rosetta DBT Studio 1.7.6 (dbt-core 1.12.6, dbt-duckdb 1.11.1, Python 3.10.17), dark theme. Voice: Kokoro `af_heart` at 1.0. Start state: `none (slides only)`.

Spoken lines are plain words. Code names are said as words and shown exactly on screen. Start times (@m:ss) and lengths are measured from the rendered video.

## s00 · title card (3 s, no voice)

Project 1 · Lesson 1.2. Git and GitHub. Badges: version control, GitHub, one PR per lesson.

## s01 · slide — slide `why`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b01 @0:03 | A dbt project is code: SQL and YAML files. Git keeps the history of that code, so you can see what changed, undo a mistake, and work with others. | Statement: A dbt project is code. Git keeps its history. Three cards: see what changed, undo mistakes, work together. | 29 | 11 |
| b02 @0:13 | GitHub keeps a copy online. Others can see your work there, and later it runs your pipeline for you. | GitHub card: a copy online that others can see, and that can run your pipeline. | 19 | 7 |

## s02 · slide — slide `flow`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b03 @0:20 | Here is the loop. You change files in your project folder. | Your project folder: changed files. | 11 | 4 |
| b04 @0:24 | You commit them: a snapshot with a short message, made in Studio's Git tab. | Commit: a snapshot with a message, made in Studio's Git tab. | 14 | 5 |
| b05 @0:29 | You push the commits to GitHub. In Studio, that is Publish Branch the first time, then Push. | Push: commits go to GitHub; in Studio, Publish Branch the first time, then Push. | 17 | 6 |
| b06 @0:36 | And from lesson 2.2 on, each lesson's work goes on its own branch, and becomes a pull request on GitHub, which we merge into main. | Pull request: from Lesson 2.2 each lesson is a branch and a pull request, merged into main. | 26 | 9 |

## s03 · browser — Browser

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b07 @0:45 | Let's create the repository. On GitHub, signed in, click the plus button at the top, and choose New repository. | Browser: open https://github.com/rosettadb/dbt-studio<br>Click **+ Create new**<br>Click **New repository** | 19 | 8 |
| b08 @0:53 | Give it a name. This is a rehearsal copy, nyc taxi dbt rehearsal, and it is private. In your own project, call it nyc taxi dbt, and make it public. | Click **Repository name** and type `nyc-taxi-dbt-rehearsal`<br>Wait 1.5 s<br>Click **Choose visibility**<br>Click **Private**<br>Zoom: gh-form | 30 | 12 |
| b09 @1:05 | Leave everything else empty: no README, no gitignore, no license. Our first commit, in lesson 2.1, brings those files. Click Create repository. | Point at **Add README**<br>Point at **No .gitignore**<br>Point at **No license**<br>Click **Create repository**<br>Zoom: gh-form | 23 | 11 |
| b10 @1:16 | The repository is ready, and empty. GitHub shows its address. Copy the HTTPS address: Studio needs it in lesson 2.1. | Point at **Clone URL**<br>Click **Copy URL**<br>Zoom: center-wide<br>Card: *Repository address* — **Copy the HTTPS URL** — Studio adds it as the remote in Lesson 2.1. | 21 | 10 |

## s04 · slide — slide `token`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b11 @1:26 | One more thing. GitHub does not accept your account password for pushing code. Pushes use a personal access token: a key you create on GitHub. | Password crossed out → personal access token. | 25 | 10 |
| b12 @1:35 | Make it work for this repository only, with contents and workflows set to read and write. We set it up right before the first push, in lesson 2.1. | Token settings: only this repository; Contents and Workflows, read and write; an expiry date. | 29 | 10 |

## s05 · slide — slide `recap`

| Beat | Spoken | On screen | Words | ~s |
|---|---|---|---|---|
| b13 @1:45 | To recap. Git keeps the history, GitHub keeps a copy online, and one pull request per lesson keeps every change easy to follow. Next, we create the dbt project. | Recap: git keeps the history; GitHub keeps a copy online; one pull request per lesson. | 29 | 12 |

## s06 · closing card (4 s, no voice)

Next · Lesson 2.1 · Create the dbt project.

**Total: 292 spoken words, 2:01 rendered.**
