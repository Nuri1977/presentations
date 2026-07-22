# Pipeline Visualization video — asset checklist

Video: **"See your pipeline.yml as a live, interactive graph."**
Target length: ~90 sec–2 min. Same format as `cloud-cicd-deploy` and `debugging-failed-models`.

The deck (`video-presentation.html`) and voiceover (`voiceover-script-90sec.txt`) are already generated.
You just need to drop in the screenshots below with these **exact filenames** — the HTML references them by name.

---

## The feature (so the shots match the copy)

The CI/CD tab renders `pipeline.yml` as a **React Flow + Dagre** graph:
- Each step is a **node** (colored header = plugin: dbt / command / etc.), laid out **left → right** in run order.
- Bottom-left **Controls** bar: **zoom in**, **zoom out**, **fit view**, and **toggle interactivity** (the lock).
- Two extra control buttons appear in read mode:
  - **magic-wand** (AutoFixHigh) → **Visual edit** — opens the node palette, drag-drop steps, wire + double-click to configure.
  - **pencil** (Edit) → **Edit pipeline.yml** — opens the raw YAML in the Monaco editor.
- When a cloud run is recorded, nodes show **live status** (Running / Success / Failed) + per-step duration, and a "Last run" chip sits on top.

---

## Screenshots to capture

| Filename | What to have on screen |
|---|---|
| `pipeline-graph.png` | The CI/CD tab showing the pipeline as a graph — several step nodes connected left→right. Nodes centered; leave the left gutter with the controls visible. (The card sits center-right.) |
| `graph-navigate.png` | Same graph, **zoomed in a bit** so the +/−/fit-view controls (bottom-left) are the visual focus. Consider hovering the fit-view button. Card center-right. |
| `toggle-interactivity.png` | Graph with the **interactivity lock** button highlighted/hovered in the controls bar. Card center-right. |
| `visual-edit-palette.png` | **Visual edit mode** on (magic-wand clicked): the **node palette** panel visible on the left, edit toolbar up top (Pipeline Name field, Save/Cancel), ideally mid-drag of a new step. Card sits bottom-LEFT, so keep the palette + a node or two toward center/right. |
| `edit-pipeline-yaml.png` | The **raw pipeline.yml open in the editor** (pencil clicked) — Monaco showing the `jobs:` / `steps:` YAML. Card bottom-LEFT, so keep the YAML text toward center/right. |
| `pipeline-live-status.png` | A pipeline **mid-run or just-finished**: nodes showing Running/Success/Failed chips + durations, and the "Last run … RUNNING/FINISHED" chip on top. Card center-right. |

Notes for clean shots:
- Same window size / zoom across all six so the slides feel consistent (the `cloud-cicd-deploy` SESSION-NOTES used 1798×1088).
- Full-window screenshots work best — the deck darkens the edges and overlays the text card, so don't crop tight.
- PNG, landscape.
- `logo_hero.svg` is already in this folder (copied from `cloud-cicd-deploy`).

## How to run it
1. Drop the 6 screenshots into this folder with the exact names above.
2. Open `video-presentation.html`, arrow-key through it, screen-record while reading the voiceover script.
