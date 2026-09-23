# Assets checklist — local dbt vs Rosetta DBT Studio

**This is the LOCAL vs LOCAL video, 7 slides.** v1 (`../dbt-wizard-vs-rosetta/`) is **abandoned,
not superseded** — a desktop app against a paid cloud product was never an adequate comparison, so it
will not be published in any form. Its sibling is `../dbt-cloud-vs-rosetta-cloud/`
(cloud vs cloud). All pricing and platform material moved to that one — this video never mentions price
beyond "both are free".

Deck: `video-presentation.html`, 7 slides, arrow keys, `F` for fullscreen.
Scripts: `voiceover-script.md` (plain, for subtitles) and `voiceover-kokoro.txt` (markup, fed to TTS).
**The two script files must stay identical in wording.** Only markup differs.

Research and verdicts behind every claim: `FEEDBACK-research-findings.md`.

---

## ⚠️ Confirm before recording

1. ~~**Is Rosetta Cloud's $100 flat, or per user?**~~ **RESOLVED 3 Sep 2026 — it is flat.** Evidence,
   from the Stripe checkout for the Business Plan on a real account:
   - Charge is **MKD 5,500.00 per month**, and 5,500 / 55.0001 = **$100.00** exactly
   - Line item reads `Business Plan - MKD 5,500.00 - Billed monthly`, a **single flat charge with no
     quantity and no seat multiplier**. A per-seat Stripe subscription renders a quantity or a seat
     selector; this renders neither
   - The plan feature table has **no seats row at all**, where dbt's card explicitly lists
     "Five (5) developer seats"

   Slide 9's "per developer" vs "per month" contrast therefore stands as written. Residual caveat: this
   proves how *this* checkout bills, not that no seat logic exists anywhere in their Stripe config. If
   seat-based pricing is ever introduced, slide 9 is the line that breaks.
2. **Do not conflate the two data lakes.** Slide 8 claims data lake support in the free download — true
   of the **desktop** DataLake surface. Rosetta Cloud's **Cloud Data Lake** is a paid feature, ✗ on the
   free tier. Keep the claim on the desktop one.

---

## Screenshots

| # | File | State | How to capture |
|---|---|---|---|
| 1 | `broll-rosetta-connection-types.png` | ✅ reused from v1 | Rosetta's New Connection picker, all eight tiles visible |
| 2 | `dbt-empty-project.png` | ❌ **PLACEHOLDER** | `dbt init` project open **in VS Code**, file tree expanded showing the six folders and `my_first_dbt_model.sql`. The v1 capture was the browser IDE and does not fit a local-vs-local video. |
| 3 | `3b-rosetta-staging-generated.png` | ✅ reused from v1 | Generated staging models in Rosetta's file tree |
| 4 | `4-rosetta-ai-providers.png` | ✅ reused from v1 | Provider Type dropdown open, all six options visible |
| 5 | `5-rosetta-nav.png` | ✅ reused from v1 | Sidebar column only, logo row down through Flows |

### Optional, would strengthen slide 2

Slide 2 is currently text-only. Any of these as a background or inset would help, though none is
required — the seven-step list carries the claim on its own:

- A terminal showing `python -m venv` → `activate` → `pip install dbt-postgres`
- `profiles.yml` open in an editor, showing the hand-written host/port/user/password/schema block
- The Power User setup wizard mid-flow, on the interpreter-selection step

### Rosetta Cloud plan page

Captures exist (supplied 3 Sep 2026) but are **not currently referenced by the deck** — slide 9 renders
the numbers as styled text instead, which stays legible on a phone in a way a screenshotted pricing
table does not. Save them into `screenshots/` anyway if you want them as B-roll in the edit.

---

## Accuracy notes — things that are true and must stay

- **Both sides are free locally.** dbt Core, VS Code, and both major extensions cost nothing. Slide 1
  says this out loud. Removing it re-creates the exact flaw the reviewers caught in v1.
- **The `dbt init` template is dbt Core's**, not dbt Labs' platform. Slide 4 says so explicitly. Do not
  let this slide imply the toy models are a dbt Labs failing — they appear identically on both sides.
- **Rosetta Cloud has no scheduler.** Verified by grepping the whole codebase for `cron`/`schedule`:
  only a decorative MUI clock icon. Every cloud run is manually triggered. Slide 6 concedes this.
- **dbt Fusion does not support Postgres**, and dbt Labs' own VS Code extension requires Fusion. That
  is why the comparison uses Power User. Slide 2's versus-line states it plainly.

## Claims that were rejected during research — do not reintroduce

- ❌ **"Athena and Fabric use Postgres as the underlying driver."** False. dbt-athena uses PyAthena,
  dbt-fabric uses pyodbc. Redshift *is* Postgres-derived; those two are not.
- ❌ **"dbt cannot reach a file on your own disk."** True of the browser IDE only. `dbt-duckdb` and
  `dbt-sqlite` both exist and dbt documents them. This killed the v1 connections slide.
- ❌ **"Rosetta has no plan cards / nothing to choose."** False. Rosetta Cloud has three tiers and a
  monthly/yearly toggle.
- ⚠️ **DuckDB-as-proxy** is real in DuckDB, but untested in Rosetta per the reviewer. Do not claim it
  until somebody tests and films it.

## Editorial rules carried over from v1

- Every claim must be verifiable from the other party's own screens or docs.
- **Keep the concessions.** Slide 6 exists so the other nine are believed. Slide 1 conceding that local
  dbt is free is the single most important line in the video — it is what the reviewers said was missing.
- Crop screenshots to the claim. Never shrink a full window into a two-up pane; panes are ~830px.
- No dbt Labs logo anywhere. Their trademark policy requires written permission for logo marks.

## Still open

- **Trademark sign-off** before publishing. Unchanged from v1, still an AdaptiveScale decision.
  https://www.getdbt.com/dbt-assets/dbt-trademark-guidelines
- **Watch the two linked tutorials** (`zZVQluYDwYY`, `B8uwFmVt4sU`) before locking the script. I could
  only retrieve their titles, not their content, so slide 2's step order has not been checked against
  what those videos actually walk through.

---

## Research pass 2 — corrections made 3 Sep 2026

A second research pass against Altimate's own docs found **two claims in this deck were wrong** and have
been fixed. Both would have been caught instantly by anyone who actually uses Power User.

### ❌ FIXED: "VS Code has no notebooks"

**Power User has notebooks built in.** DataPilot Notebooks, created via File → New File inside VS Code,
with jinja-sql, python and markdown cells that execute together. Sharing them across a team goes through
Altimate's SaaS instance, but the notebooks themselves are in the editor.

Slide 7 previously listed "Notebooks, separate extension" in the dbt column. That was false. The slide
now credits Power User's notebooks and narrows the claim to **object storage, data lakes and pipelines**,
which Power User genuinely does not have.

### ❌ FIXED: "codegen prints to your terminal, fourteen times"

True of the codegen package, but **Power User has its own generate-model-from-source feature** — a click
on a source produces a model file, no terminal paste, and no API key needed. Describing only codegen
would have undersold the dbt side.

Per Altimate's docs the feature still works **one source at a time**, so the "fourteen passes" claim
survives. Slide 5 now names both routes and keeps the count comparison.

### Power User's full feature set, for reference

Auto-complete with go-to-definition · query preview with CSV export and charts · **column-level lineage** ·
**generate model from source or from SQL** · doc generation · defer-to-prod · click-to-run · compiled SQL
preview · project health checks · SQL validation · BigQuery cost estimation · log viewer · **notebooks**

**It does not have:** object storage browsing, data lake support, or a pipeline view. Those three are the
honest content of slide 7.

### dbt "successful models built" — for the cloud video

Only models built in a **deployment** environment count — scheduler runs, CI builds, API-triggered runs.
Models built in a development environment (the Studio IDE) **do not count**. Tests, seeds, ephemeral
models and snapshots do not count either. So the 3,000/month free-tier cap applies to orchestration, not
to development. Relevant to the cloud video's slide 5; do not state the cap as if it limits day-to-day work.

### Still unverified

- **What a Rosetta Cloud Compute Unit actually buys.** 100 CU free vs 13,800 on Business is meaningless
  without knowing what one CU is. Not documented publicly. The manage-plans page has ⓘ tooltips next to
  "Monthly Compute Units" — hover one and it may say. Until then, do not imply the free tier is generous
  or stingy; the deck only states the numbers.

---

## Research pass 3 — the tutorial transcript, 3 Sep 2026

Edon supplied the full transcript of *"[Data Build Tool] DBT - The Ultimate Guide | With CI/CD"* —
a ~5-hour dbt Core masterclass. Slide 2's step order has now been checked against what a dbt advocate
actually demonstrates, rather than against my reconstruction of it.

### Confirmed by the tutorial

The overall shape of slide 2 holds. The tutorial's own setup chapter walks through: VS Code, Git,
Python, a package manager, a virtual environment, `dbt-core` plus an adapter, `dbt init`, `dbt debug`,
the VS Code Python extension, then dbt Power User and its setup wizard — including **associating
`*.sql` with `jinja-sql` and `*.yml` with `jinja-yaml`**, exactly as the slide says.

The creator uses **Databricks free edition** as the warehouse rather than Postgres. Worth knowing: the
tutorial audience norm may be Databricks or Snowflake, not Postgres.

### ✅ FIXED: "write profiles.yml by hand" was wrong

`dbt init` **generates** `profiles.yml` by walking you through roughly eight interactive prompts —
project name, adapter, host, connection path, auth method, token, catalog, schema, threads. You do not
type the file from scratch.

The real friction is different, and better: the generated file lands in **`~/.dbt/`, a hidden folder**
that you have to enable hidden files to even see, and the recommended practice is then to copy it into
the project root. Slide 2 step 03 and 04 now say this.

### ✅ ADDED: the `cd` trap

`dbt debug` fails if you are not inside the project directory — it reports no project found. The
tutorial hits this live, more than once, and calls it out as a common mistake. Now slide 2 step 05.

### ✅ ADDED: the Python extension is a separate install

VS Code's Python extension (Microsoft) and dbt Power User are two separate installs. The slide
previously implied one. Now step 06.

### ❌ REJECTED: "you must install an older Python"

The tutorial spends real time installing Python 3.12 because dbt did not support 3.13 at the time, and
shows dbt's own compatibility table with 3.13 marked incompatible.

**This has since closed.** Checked dbt's live compatibility page: dbt Core v1.12 supports **Python 3.10
through 3.14, including 3.13**. Putting this on a slide would repeat the exact Fusion/Postgres error —
a temporary gap presented as permanent. Left out deliberately.

(One softer caveat does remain in dbt's docs: adapter plugins may lag dbt Core on the newest Python.
Too weak and too conditional to script.)

### Useful corroboration for slide 7

The tutorial's creator says that after installing Power User you get almost everything dbt Cloud offers —
lineage, DAGs, query preview — and questions why you would pay for dbt Cloud while learning. That is a
dbt advocate independently confirming Power User is strong, which is why slide 7 credits it rather than
pretending VS Code is bare. Storage remains the honest gap.

### Still not watched

The second link (`zZVQluYDwYY`, "Netflix Data Analysis | DBT Tutorial Course") has not been reviewed.
Same treatment would be worth applying before the script is locked.

---

## Research pass 4 — second tutorial transcript, 3 Sep 2026

Edon supplied the transcript of *"Netflix Data Analysis | DBT Tutorial Course | End-To-End Project"*
(S3 → Snowflake → dbt). Both linked tutorials have now been reviewed.

### Slide 2 is confirmed by two independent tutorials

Different creator, different warehouse (Snowflake here, Databricks in the other), same sequence:
virtualenv → `pip install dbt-<adapter>` → create the `~/.dbt` root folder → `dbt init` (this one prompts
for database, account, username, password, role, warehouse, database, schema and threads — nine) →
`profiles.yml` lands in the hidden folder → install dbt Power User.

Two specific steps are now doubly evidenced:

- **The `cd` trap.** This creator hits "No dbt project found" **twice on camera** and calls it out both
  times as the thing people get wrong. Step 05 is well earned.
- **The hidden `~/.dbt/` folder.** They visibly struggle to locate `profiles.yml`, noting it is hidden
  and that you may need to enable hidden files. Step 04 describes exactly this.

### Both tutorials use dbt Power User — and neither had to

This one runs on **Snowflake**, the other on **Databricks**. Fusion supports both, so dbt Labs' own
extension would have worked for either. They both chose Power User anyway.

That materially strengthens the extension choice: Power User is the community default on its own merits,
not merely the fallback we are forced into by the Fusion/Postgres gap. Slide 2's versus-line can stay as
it is, but the choice no longer rests solely on that technicality.

### ✅ FIXED: "no pipeline view" was too vague

This tutorial spends real time on `dbt docs generate` / `dbt docs serve`, which renders a **model lineage
DAG** the creator calls the feature everyone likes. Slide 7 credited Power User with column-level lineage
and then claimed it had "no pipeline view" — a dbt user would object and point at that graph.

They are different things: dbt's is model lineage, while Rosetta's **Flows** runs deployment pipelines
(its runner installs Git, Terraform and the AWS CLI). But "pipeline view" could not carry that
distinction. Now reads **"runnable pipelines"** on the slide and *"no pipelines you can actually run"*
in the voiceover.

Lineage itself is a wash — Power User has column-level lineage, Rosetta has a lineage panel too. Slide 7
does not claim it either way, which is correct.

### ⚠️ Worth a decision: neither tutorial uses Postgres

The first runs on Databricks, this one on Snowflake. **Neither uses Postgres.** If the audience is dbt
developers and the tutorial norm is cloud warehouses, a Postgres demo may read as unrepresentative.

Against changing it: Rosetta's actual differentiators — local files, DuckDB/SQLite, running where your
data already is — only make sense with local or small data. Moving to Snowflake would trade away the
argument to gain audience familiarity, and would also remove the honest Fusion justification on slide 2.

**Not changing anything.** Flagging it as a real tension for Edon to decide, not a defect.

### Other friction seen but deliberately not scripted

- Everything materialises as a **view by default**; tables require configuring `dbt_project.yml`.
- The schema chosen at `dbt init` becomes the output schema, and correcting it means hand-editing
  `profiles.yml` and dropping the wrongly-created objects.

Both are real, both are project-shaped rather than setup-shaped, and slide 2 is already the longest in
the deck at ~120 words. Left out to avoid bloat.

---

## Restructure — same project, fully local, 3 Sep 2026

Edon's call, and it fixes two fairness problems the deck still had.

### 1. Everything is genuinely local now

The database moves from **Neon Postgres (eu-central-1, Frankfurt)** to **local Postgres in Docker**.

Previously "local vs local" described the *tooling* only, while the data sat on someone else's cloud —
which quietly undercut every "runs on your machine" line in the script. The DB is a prerequisite for
both sides equally, so it inflates neither, and it keeps the Northwind data and the "fourteen tables"
narrative exactly as they were.

**Capture consequence:** every Rosetta screenshot showing a connection now needs to show `localhost`,
not a Neon endpoint. `broll-rosetta-connection-types.png` in particular.

### 2. Both sides start from the same project

Previously slide 4 had *both* sides run `dbt init` and receive dbt Core's toy template. That was never a
fair setup — the audience is dbt developers who **already have projects**, and having one side scaffold
from scratch while the other imports was comparing different activities.

Now there is **one dbt project**, already written, and the video asks what each tool needs to open it:

- **VS Code:** venv → `pip install dbt-postgres` → write `profiles.yml` by hand (the project carries
  models and config but none of your credentials) → find it in the hidden `~/.dbt/` → `cd` in →
  `dbt debug` → Python extension → Power User → its wizard.
- **Rosetta:** download → point it at the project folder or a zip → it finds the dbt root even when
  buried and imports the whole thing → fill in the connection form.

`dbt init` is gone from the script entirely, since neither side scaffolds anything.

### Deck went 8 slides → 7

The **empty project** slide was dropped. Its content (both sides get dbt Core's two toy models, nobody
is to blame) only existed to defuse the greenfield framing, which no longer exists. It was also flagged
in `FEEDBACK-research-findings.md` as the deck's most attackable slide.

**Concessions still standing:** slide 1 says both tools are free and the code is identical; slide 2's
versus-line names the Fusion/Postgres limitation; slide 4 credits both codegen and Power User's
generate-from-source; slide 6 credits Power User's query previews, lineage and notebooks.

### Slide 5 wording tightened

*"your schema and your column names never leave the machine"* → *"nothing about your project goes to a
model vendor at all."* The old phrasing was loose once the DB was remote; it is now both accurate and
unambiguous about what the claim covers.

### New capture list

| File | State | Needs |
|---|---|---|
| `broll-rosetta-connection-types.png` | ⚠️ **restage** | Connection form pointed at **local** Postgres |
| `3b-rosetta-staging-generated.png` | ⚠️ **restage** | Generated from the local DB |
| `4-rosetta-ai-providers.png` | ✅ reuse | Provider dropdown is unaffected |
| `5-rosetta-nav.png` | ✅ reuse | Sidebar is unaffected |
| `dbt-empty-project.png` | ❌ **delete** | Slide removed; no longer referenced |
| *(new)* import dialog | ➕ **capture** | Rosetta importing the existing project folder — this is now slide 3's core claim and nothing shows it |

---

## Slides 2 and 3 merged, 3 Sep 2026 — deck now 6 slides

Edon's call. Two sequential setup slides became **one two-up comparison**: seven numbered steps down the
left for VS Code + dbt, three down the right for Rosetta.

Running them sequentially meant the viewer had to hold seven steps in memory to feel the contrast when
slide 3 arrived. Side by side, the difference is the shape of the two lists and needs no memory at all.

### ✅ Verified: Rosetta ships its own Python and installs dbt for you

This is the strongest fact on the new slide and it was checked in the clone before scripting:

- **`SettingsService.performPythonInstall`** downloads a standalone CPython build from
  `python-build-standalone` (astral-sh) into Rosetta's own app data. It does **not** use the system
  Python — it brings its own.
- **`DbtCoreVersionService.installLatestPackage`** then runs `python -m pip install` into that Python,
  and `getDbtExecutableForPython` resolves the dbt binary beside it.
- `dbtCoreVersion.service.ts` manages install / reinstall / preview-install of dbt Core versions.

So steps 1, 2 and 3 on the left (install Python, make a venv, pip install the adapter) are not merely
"more steps" — **they are steps Rosetta performs for you.** That is what the right pane's foot line says.

### ❌ REMOVED: the Fusion versus-line

Slide 2 previously ended with *"dbt Labs' own extension needs Fusion, which does not support Postgres
yet."* It appeared **only on screen and was never spoken**, so a viewer had no idea why it was there.

It also is not needed. Research pass 4 established that **both linked tutorials chose Power User even
though Fusion supports their warehouses** (Snowflake and Databricks). Power User is the community
default on its own merits, so the comparison needs no Fusion excuse to justify it.

The Fusion/Postgres limitation is still recorded in `FEEDBACK-research-findings.md` Part 8 if it is ever
needed for a description or a comment reply.

### ❌ DECIDED OUT: warehouse / database breadth (4 Sep 2026)

Edon's call, after it was raised and costed: **the video does not compare supported databases at all,
and that is deliberate.** Do not propose adding it again.

The facts, if they are ever needed for a description or comment reply:

- **Rosetta supports 6.** Postgres, Snowflake, BigQuery, Redshift, Databricks, DuckDB. Confirmed twice
  over - `ADAPTER_PACKAGES` in `src/main/services/dbtCoreVersion.service.ts:55`, and the JDBC drivers
  bundled with the CLI at `<install>/drivers/`, which match the list exactly.
- **dbt Core supports roughly 40+**, including 27 community adapters (MySQL, SQL Server / Azure SQL,
  SQLite, Vertica, TimescaleDB, TiDB, SingleStore, CrateDB, MaxCompute and others) plus the trusted set.
  dbt wins this comparison decisively; it would be a genuine concession, not a spin opportunity.
- **dbt v2 / Fusion also supports only 6**: Snowflake, BigQuery, Databricks, Redshift, Spark, DuckDB.
  That is the same list as Rosetta's except Rosetta has Postgres and Fusion has Spark - Fusion does not
  support the database this video runs on. **Keep this out of any script even if the concession is ever
  added back:** conceding and then immediately undercutting the concession reads as spin and costs the
  credibility the concession earns.

Reason it stays out: the video's spine is one local Postgres project opened two ways, and warehouse
breadth does not bear on that scenario. Six slides at 544 words is tight and the arc works.

Side effect: `screenshots/broll-rosetta-connection-types.png` stays **orphaned**. It is kept as B-roll only.

### ✅ FIXED: slide 5 left pane said "VS Code", which made a false claim (4 Sep 2026)

The pane was titled **VS Code** and closed with *"Strong on the editor. Nothing for object storage or
data lakes."* Read as a claim about VS Code, **that is false and an AWS-shop viewer would catch it
immediately.**

- **AWS Toolkit** (official AWS) browses S3 buckets and objects with full CRUD from the AWS Explorer view.
- **Azure Storage** (official Microsoft, `ms-azuretools.vscode-azurestorage`) browses Blob Containers,
  File Shares, Tables and Queues.
- Google ships Cloud Code for GCP, and there are third-party S3 explorers (S3X Explorer, BucketBuddy).

The **voiceover was already safe** - it says *"**Power User** covers more ground... Where **it** stops is
storage"*, and Power User genuinely has no object explorer. Only the HTML was wrong. Fixed by rescoping:

- pane name `VS Code` → **`VS Code + Power User`**, matching slide 4. The deck's convention is
  `VS Code + dbt` where the point is dbt Core itself (slides 2, 3) and `VS Code + Power User` where the
  point is the extension (slides 4, 5). Naming the combination is accurate: that combination has no
  object explorer, and the foot line carries the honesty.
- foot line → *"Strong on the editor. For storage you're installing extensions from **three other vendors.**"*

**The defensible claim is integration, not capability.** Never say VS Code cannot browse object storage.
Say it does not come from your dbt extension and is not in one place. Rosetta's Cloud Explorer ships
**eight** providers in the same download - S3, Google Cloud Storage, Azure Blob, MinIO, Cloudflare R2,
Backblaze B2, rustfs, Garage - confirmed in `src/main/helpers/cloudAuth.helper.ts`. The five
S3-compatible ones are the genuinely differentiated part, since AWS Toolkit will not touch them.

Implementation note: the Cloud Explorer is built on **DuckDB secrets**
(`CREATE OR REPLACE SECRET minio_secret (...)`). That is why `dbt_duckdb` is the one adapter actually
present on disk - DuckDB is load-bearing for this feature, not just an adapter choice.

### New CSS

`.pane-steps` — a compact numbered list for use inside a pane, with leading-zero counters in the accent
colour. Added because the existing `.pane-text ul` bullets could not carry seven ordered items legibly
at pane width.

### Slide map after the merge

| # | Slide | Words |
|---|---|---|
| 1 | Hook | 71 |
| 2 | **What each one needs** (merged) | 141 |
| 3 | From schema to models | 104 |
| 4 | Who runs the AI | 80 |
| 5 | What else is in the box | 72 |
| 6 | Closing | 51 |
| | **Total** | **519** (~2:30) |

Slide 2 is the longest at ~40 seconds on one static frame. It carries the deck's core argument so the
length is earned, but if it drags on playback the fix is in the edit — reveal the seven left-hand steps
progressively — not in the script.

### Capture list changed again by the merge

The merged slide 2 is **pure text on both sides** — no screenshot — so `broll-rosetta-connection-types.png`
is no longer referenced by the deck.

**It is not deleted.** It is a real capture and still useful as B-roll in the edit, but it **no longer
needs restaging** against the local database, which removes one item from the shot list.

Current state:

| File | Status |
|---|---|
| `3b-rosetta-staging-generated.png` | ⚠️ Restage against the **local** Postgres (slide 3) |
| `4-rosetta-ai-providers.png` | ✅ Reuse as-is (slide 4) |
| `5-rosetta-nav.png` | ✅ Reuse as-is (slide 5) |
| `broll-rosetta-connection-types.png` | ➖ Unreferenced. Keep for B-roll, no restage needed |
| *(import dialog)* | ➕ **No longer required** — slide 2 states the import in text, and there is no screenshot slot for it |

That leaves **one** capture outstanding for this video instead of three.

---

## Slide 3 rebuilt as a compare-slide, 3 Sep 2026

The voiceover opened *"the project is open on both sides"* while the frame showed only Rosetta. Fixed by
making slide 3 a two-up, matching slides 2, 4 and 5. It was previously a full-bleed background image.

### ⚠️ BOTH panes need tight crops — a full window will not survive the pane

Measured: `3b-rosetta-staging-generated.png` is **1920x1080**. An ~830px pane scales it to **43%**, so 12px
UI text renders at roughly 5px. It read fine as a full-bleed background at 1920px; it does not read at
pane width. This is the v1 rule ("never shrink a full window into a two-up pane") biting in practice.

| Pane | File | What to capture |
|---|---|---|
| **Left** | `3a-dbt-codegen-terminal.png` ❌ **placeholder** | The **terminal only**, cropped tight, showing codegen's generated SQL for **one** table — the block you would copy into a file. No window chrome, no file tree, no sidebar. |
| **Right** | `3b-rosetta-staging-generated.png` ⚠️ **re-crop + restage** | The **file tree only**, cropped to the `staging` folder with its generated models visible. Not the whole window. And pointed at the **local** Postgres, not Neon. |

Both crops are legible at pane width because each is one dense element — a block of SQL, a list of
filenames — rather than a whole IDE.

### Why one slide rather than two

Two full slides would make the viewer hold the left side in memory while looking at the right. Side by
side the contrast is immediate: *one table's SQL you move by hand* against *a folder that already has
fourteen files*. Same reasoning that made merging slides 2 and 3 work.

### Capture list for this video, current

| File | Status |
|---|---|
| `3a-dbt-codegen-terminal.png` | ❌ New capture — terminal crop, one table |
| `3b-rosetta-staging-generated.png` | ⚠️ Re-crop to the file tree, restage on local Postgres |
| `4-rosetta-ai-providers.png` | ✅ Reuse as-is |
| `5-rosetta-nav.png` | ✅ Reuse as-is |
| `broll-rosetta-connection-types.png` | ➖ Unreferenced. B-roll only |

---

## Slide 4 — named OpenAI-compatible providers, 3 Sep 2026

Was: *"any OpenAI compatible endpoint, which covers most of the rest of them."* Vague, so it read as a
hedge rather than a capability.

Now names them: **Groq, Together, OpenRouter, or a vLLM server you host yourself.**

**Groq is the one Edon has personally tested** through the OpenAI Compatible provider. If the claim is
ever challenged, that is the example to lead with — it is first-hand, not inferred.

Verified in the clone beforehand: `agentAdapter.ts` queries `{baseUrl}/models` to enumerate whatever the
endpoint serves, and the model field is `z.string().optional()` — free text, not a fixed enum. So any
OpenAI-compatible endpoint genuinely works; the named four are examples, not an allow-list.

### Also fixed: an ambiguity the new names would have created

The old line ended *"Two of those run on your own hardware"* — meaning Ollama and LM Studio. With vLLM
now in the sentence (which also self-hosts), "two of those" would have been wrong or at least unclear.
The line now names **Ollama and LM Studio** explicitly instead of counting.

### ⚠️ Check these when generating the audio

Three new proper nouns carry pronunciation markup that has not been heard yet:

| Word | Markup | Expected |
|---|---|---|
| Groq | `[Groq](/ɡɹˈɑk/)` | "grok" |
| OpenRouter | `[OpenRouter](/ˈOpənɹˌUtɚ/)` | "OH-pen-ROW-ter" |
| vLLM | `[vLLM](/vˌiˌɛlˌɛlˈɛm/)` | "vee-L-L-M", spelled out |

vLLM is the most likely to come out wrong. If it does, the fallback is writing it as "a self-hosted
model server" and dropping the name — the sentence works without it.

---

## Slide 4 rewritten again — the app ships its own endpoint list, 3 Sep 2026

Edon supplied screenshots of the **Add AI Provider** dialog with **OpenAI Compatible** selected. The
dialog does more than accept a base URL: expanding **"Popular Compatible API Endpoints"** reveals a
built-in list of **eight named providers**, each with its URL and a copy button.

From the screenshots, verbatim:

| Provider | Base URL |
|---|---|
| OpenRouter | `https://openrouter.ai/api/v1` |
| NVIDIA NIM | `https://integrate.api.nvidia.com/v1` |
| DeepSeek | `https://api.deepseek.com` |
| Groq | `https://api.groq.com/openai/v1` |
| Together AI | `https://api.together.ai/v1` |
| Clarifai | `https://api.clarifai.com/v2/ext/openai/v1` |
| NEAR AI Cloud | `https://cloud-api.near.ai/v1` |
| Heroku (Custom App) | `https://<YOUR_APP_NAME>.herokuapp.com/v1` |

The dialog also states: *"Connect to any server that implements the OpenAI Chat Completions API — local
inference servers, cloud proxies, or custom deployments."* And **API Key is marked optional**, which is
what makes local inference servers work without one.

### ❌ REMOVED: vLLM

The earlier draft named vLLM as a self-hosted example. It is **not in the app's list**, so the claim was
not verifiable from any screen — it came from conversation, not the product. Replaced with providers that
appear in the dialog itself.

Bonus: this also removes the riskiest pronunciation in the deck. Only `Groq` and `OpenRouter` still carry
markup that has not been heard yet.

### Why this framing is stronger

"Any OpenAI-compatible endpoint" sounds like DIY work. **"Ships a list of eight, URLs ready to copy"** is
a feature, and it is provable from one screenshot. It also lands better against the left pane, where
Power User's AI has exactly one destination.

### ➕ New capture — B-roll, NOT a replacement

`rosetta-ai-compatible-endpoints.png` — the **Popular Compatible API Endpoints** section expanded,
cropped to the list.

**Do not swap it in for the dropdown.** The pane must keep `4-rosetta-ai-providers.png`, because that is
the shot proving *"five named providers"* — OpenAI, Anthropic Claude, Google Gemini, Ollama, LM Studio.
Replacing it would leave the mainstream providers unseen, which is the half most viewers care about.

Use it as a **B-roll insert in the edit instead**, cut in over the pane at the moment the voiceover says
*"ships a list of eight more"*, then back to the dropdown. The slide carries claim one, the insert
carries claim two, and neither pane gets crowded.

The pane-foot already states the eight in text, so if the insert never gets shot the slide still stands
on its own.

### Slide 4 reordered to walk the dropdown top down

Edon's call. The line now names the providers in the same order the viewer sees them in the screenshot:

1. **OpenAI, Anthropic Claude, Google Gemini** — the cloud ones people recognise
2. **Ollama and LM Studio** — the two that run locally
3. **OpenAI Compatible** at the bottom, with three of its eight named

Audio and image now move in the same direction, so the viewer can follow the voice down the menu instead
of hunting for whichever item was just mentioned. Naming only three of the eight keeps it a sample rather
than a recital.

The closing line changed from *"choose one of those"* to **"choose one of the local two"** — with six
providers now named in sequence, "those" no longer had a clear referent.

### Pronunciation markup added: LM

`[LM](/ˌɛlˈɛm/)` so it reads "el-em" rather than as a word. It had been bare in every earlier draft of
this script and never generated, so this is the first pass where it would have been at risk.

Untested markup on this slide is now: `Groq`, `OpenRouter`, `LM`.
