# Cloud + CI/CD video — generation prompt & asset checklist

This folder is for the next video: **"Deploy and run your dbt project in the cloud — no CI config files."**
Target length: ~90 sec–2 min (same format as `debugging-failed-models` and `dbt-lineage-dag`).

---

## PART A — The prompt (copy-paste this to Claude)

> Build a `video-presentation.html` slide deck for a Rosetta DBT Studio feature video about **Cloud deploy + CI/CD**.
>
> **Match the existing format exactly.** Use `presentations/presentations/debugging-failed-models/video-presentation.html` as the template — same structure, styling, and behavior:
> - Full-screen deck, one `.slide` per section, keyboard navigation (Right arrow / Spacebar advances, Left goes back).
> - Dark theme with the existing CSS variables (`--orange: #ff7a1a`, dark `#05060a` background, Inter font).
> - First and last slides are the logo intro/closing using `logo_hero.svg`.
> - Content slides use a full-bleed screenshot as the background (`.bg`) with a dark `.shade` gradient and a `.content` card holding a short headline + 1–2 supporting lines.
> - Preload the same fonts/animations; no external dependencies beyond what the template already uses.
>
> **Slides (6 total), with the screenshot filename each one uses:**
> 1. **Intro** — `logo_hero.svg` — Headline: "Ship Your dbt Project to the Cloud." Sub: "Deploy and run — no CI config files to write."
> 2. **Cloud mode** — `cloud-toggle-dashboard.png` — Headline: "One toggle to go cloud." Sub: "Flip to Cloud, open the Cloud Dashboard — your project lives in Rosetta Cloud."
> 3. **Push to Cloud** — `push-to-cloud-modal.png` — Headline: "Push your project." Sub: "One click deploys your models, configs, and connections to the cloud."
> 4. **Pipeline runs** — `pipeline-running.png` — Headline: "It runs in the cloud." Sub: "Rosetta kicks off a pipeline run — no GitHub Actions, no YAML CI files."
> 5. **CI/CD tab** — `cicd-tab-logs.png` — Headline: "Watch it in the CI/CD tab." Sub: "Live run status and full logs, right inside the app."
> 6. **Success + closing** — `cicd-run-success.png` then `logo_hero.svg` — Headline: "Green. Repeatable. Done." Sub: "Download Rosetta DBT Studio. Star us on GitHub."
>
> **Also generate** a `voiceover-script-90sec.txt` in the same style as `debugging-failed-models/voiceover-script-2min.txt` — a `[SLIDE X — "title" — filename.png]` cue block per slide with ~130 wpm narration, opening hook, and closing CTA.
>
> Save both files in `presentations/presentations/cloud-cicd-deploy/`. Assume the screenshots listed above will be dropped into the same folder.

---

## PART B — What YOU need to provide (screenshots)

Capture these from the running app and save them into this folder with **these exact filenames** (the HTML references them by name):

| Filename | What to have on screen when you capture it |
|---|---|
| `cloud-toggle-dashboard.png` | Top-right corner in focus — the **Cloud** toggle switched on and the **Cloud Dashboard** button visible. Full window is fine. |
| `push-to-cloud-modal.png` | The **Push to Cloud** modal/dialog open (the deploy step). |
| `pipeline-running.png` | A pipeline **run in progress** — the CI/CD view or dashboard showing an active/running state. |
| `cicd-tab-logs.png` | The bottom panel switched to the **CI/CD tab**, showing a run with its **log output**. |
| `cicd-run-success.png` | A **successful (green) run** in the CI/CD tab. |

Notes for clean shots:
- Use the same window size / zoom across all five so slides feel consistent.
- Full-window screenshots work best — the deck darkens the edges and overlays the text card, so don't crop tight.
- PNG, landscape. The existing decks use ~350–470 KB shots at roughly 1900px wide; anything at your normal screen resolution is fine.

## Assets you already have (reuse, don't recreate)
- `logo_hero.svg` — copy it from any existing folder (e.g. `debugging-failed-models/logo_hero.svg`) into this folder.

---

## PART C — How to run it
1. Drop the 5 screenshots + `logo_hero.svg` into this folder.
2. Paste the Part A prompt to Claude.
3. Open the generated `video-presentation.html`, arrow-key through it, screen-record while reading the voiceover script.

## One decision before you shoot
This is the **short single-flow** version (Cloud is *where* it runs, CI/CD is the *tab that shows the runs*) — ~2 min, matches your channel. If you'd rather do a true **"Rosetta Cloud vs. GitHub Actions for dbt"** comparison, that's a different, longer 4–6 min video with its own script — tell me and I'll write that prompt instead.
