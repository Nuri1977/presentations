# Lesson 0 - What is Rosetta DBT Studio? - screenshots

**5 shots to capture, all fresh from the current app (v1.6.0). Nothing is reused from older decks.**

Slides 1, 3 and 8 need no screenshot (hero logo, component grid, closing logo).

Screenshots live in the **`screenshots/`** subfolder. The deck references them as
`screenshots/<name>.png`, so save them there with these exact filenames:

| # | Filename | Slide | Shows |
|---|----------|-------|-------|
| 1 | `one-window-workspace.png` | 2 | The whole app in one window |
| 2 | `see-your-data.png` | 4 | Previewing a file in cloud storage |
| 3 | `query-and-analyze.png` | 5 | SQL editor with a query and results |
| 4 | `pipelines-visual.png` | 6 | A pipeline as a visual graph |
| 5 | `local-to-cloud.png` | 7 | The project running in Rosetta Cloud |

All five are captured and in place - this lesson's assets are complete.

Folder convention for the rest of the course: keep screenshots in a `screenshots/` subfolder inside
each lesson, with the deck, script and this checklist at the lesson root.

---

## Before you start

**Capture settings (same for every shot):**
- **1920x1080 PNG.** Set the display to 1920x1080 if it isn't already.
- Taskbar on **auto-hide**, app **maximized**.
- Capture with **PrtScn**. Do NOT use `Win+Shift+S` - it adds a drop shadow and you get ~1936x1096.
- **Do not resize the window between shots.** The status bar has to look identical across all five,
  otherwise the video looks like it was filmed across different sessions.

**Make it look like one continuous session:**
- Use the **same project** and the **same connection** for every shot.
- Same theme throughout (pick light or dark and stay there).
- Close any unrelated tabs, modals, toasts or error banners before capturing.

**Keep off screen (this video gets published):**
- Real account emails, org names, and profile avatars.
- Real bucket names, hostnames, database names, and anything resembling a credential or token.
- If your only data is client data, make a throwaway bucket or table with dummy names first.

**Leave room for the text card.** Each slide puts a text panel over part of the image. The position
is listed per shot below - keep that corner free of anything important.

---

## The shots

### 1. `one-window-workspace.png` -> slide 2

The hero shot of the whole product. Open a project so the app is fully populated, then show as much
of the workspace at once as you can: **file tree on the left, a SQL or model file open in the editor,
and the terminal panel visible at the bottom**.

Pick a file with real SQL in it - an empty editor makes the app look unused. If the AI panel is open
that is fine; the narration does not mention it either way.

Card sits **BOTTOM-RIGHT** - keep that corner clear.

---

### 2. `see-your-data.png` -> slide 4

Go to **Cloud Explorer**, open a bucket, and **preview a data file** (Parquet or CSV works best) so
the data grid is on screen.

The point of this slide is "your data, read where it already lives" - so the shot must show actual
rows of data, not just a file listing. Make sure the preview grid is populated, not still loading.

Use dummy or public data. The bucket name is visible in this shot.

Card sits **TOP-RIGHT** - keep the top-right clear and let the data grid sit lower-left.

---

### 3. `query-and-analyze.png` -> slide 5

Open the **SQL Editor**, write a short readable query, run it, and capture with **both the query and
its results** on screen.

Keep the query short enough to read in a couple of seconds - a simple `select ... from ... limit 10`
reads better on video than a 40-line query. Having the schema browser visible on the left is a plus,
it reinforces "query all of it".

Card sits **TOP-RIGHT**.

---

### 4. `pipelines-visual.png` -> slide 6

Open the **Pipeline Builder** and capture the pipeline as a **visual graph of connected nodes**.

Create one from the **"Getting Started" template** so you get several connected steps
(dbt deps, dbt test, teardown) rather than a single lonely node. A graph with one box does not sell
"build pipelines visually".

If you can fit the visual graph and the YAML side by side, even better - that pairing is the
feature's whole pitch.

Card sits **BOTTOM-RIGHT**.

---

### 5. `local-to-cloud.png` -> slide 7

Show the project **set to run in Rosetta Cloud** - the moment where the same project moves off the laptop. The cloud run view or the cloud log output both work.

If a run is in progress or has just succeeded, capture that - a successful cloud run is a stronger image than an idle screen.

Watch for account details in the header on this one.

Card sits **TOP-RIGHT**.

---

## Product name - resolved

The component is **Flowfile**, not "Fileflow". Confirmed from the app's own status bar, which reads
`Flowfile: 0.12.7` in v1.6.0. The deck's component grid (slide 3) has been corrected.

Note that the course doc still says *Fileflow* - that wording came from the original product copy and
should be corrected there too.

---

## Record

Open `video-presentation.html`, press `F`, arrow through 8 slides reading
`voiceover-script-110sec.md`.

Slide 3 (the component grid) is the one to rehearse - eight items in twenty-four seconds. Let the
viewer read while you group them, rather than reading every line aloud.
