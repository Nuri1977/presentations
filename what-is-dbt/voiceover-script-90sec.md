# 90-Second Voice-Over Script: What is dbt? | Rosetta DBT Studio

## Overview

**Total Duration**: ~90 seconds
**Target Word Count**: ~210 words (≈135 words/min at a relaxed, explanatory pace)
**Tone**: Calm, plain, explanatory. NOT the promo voice.
**Voice Direction**: This is a teaching video, not an ad. No hype, no "in 60 seconds!", no urgency.
The moment it sounds like marketing, a beginner stops trusting it as an explanation. Slow down.
Leave real pauses. You are explaining something to one person, not announcing it to a room.

**Audience**: People who have never used dbt. Assume they know SQL and nothing else.

**Slide order**: SQL → run → lineage → workspace. Define it, do it, then scale it up. The viewer sees
one model become a table BEFORE the dependency graph is introduced — the concrete thing first, the
clever thing second. The "order in your head" hook is set up at 0:05 and paid off at the very end of
the content on the lineage slide.

---

## Slide Cue Map

| Slide | Timing | Screen | Content |
|-------|--------|--------|---------|
| 1 | 0:00–0:10 | Hero logo | The hook: the order in your head |
| 2 | 0:10–0:30 | `model-is-a-select.png` | A model is just a SELECT |
| 3 | 0:30–0:42 | `run-output-success.png` | Run it, and it builds |
| 4 | 0:42–1:12 | `dbt-builds-the-order.png` | dbt works out the order (payoff) |
| 5 | 1:12–1:30 | `one-window-workspace.png` | Why you want an app for it |
| 6 | 1:30–1:40 | Closing logo | That's dbt |

---

## Full Script

### [0:00–0:10] Hook — Hero logo

"If you work with data, you've got a folder of SQL files somewhere. And in your head, the order you're supposed to run them in.

That list in your head is the problem dbt solves."

---

### [0:10–0:30] The core idea — Model open in the editor

"dbt is built on one small idea. A model is just a SELECT statement.

You write the query. dbt creates the table.

That's it. There's no new language to learn. It's the SQL you already write."

---

### [0:30–0:42] Running it — Terminal output

"Then you run it. Every model you've written becomes a table — in a single command."

---

### [0:42–1:12] Dependencies — Lineage graph

"But real work is queries built on other queries. Your summary reads from a clean table. That clean table reads from raw data.

So when one model points at another, dbt notices. It reads every reference and works out the build order itself.

That list you were keeping in your head? dbt just drew it for you.

And when you change one model, dbt already knows what else has to be rebuilt."

---

### [1:12–1:30] Why an app — Workspace

"You can do all of this from a terminal. Plenty of people do. It means a command line, config files you edit by hand, and a graph you can't actually see.

Rosetta DBT Studio puts it in one window. Your models, the graph, the run, the results. Same dbt underneath. You can just see it."

---

### [1:30–1:40] Closing — Logo

"That's dbt. Rosetta DBT Studio is open source, on Mac, Windows, and Linux."

---

## Delivery Notes

- **The spine is "the order in your head."** Set up at 0:05, paid off at 1:05 on the lineage slide
  ("dbt just drew it for you"). That callback is what makes this an explanation instead of a list of
  facts. It lands last now — pause before "dbt just drew it for you."
- **Slide 3 (run) is deliberately short and says nothing about order.** Order has not been explained
  yet — the run slide only shows "write a query, get a table." Do not add "in the right order" here;
  that idea belongs to the next slide.
- **The "graph you can't actually see" line at 1:20 is load-bearing.** It is the callback that makes
  the lineage slide pay off a second time. Do not cut it for time.
- **The close deliberately does not ask for anything.** The 60-second promo already does the
  "download / star us on GitHub" job. A teaching video that ends in a sales pitch retroactively makes
  the previous 90 seconds feel like setup.
- **Pause** 0.4–0.6s between sections. This video is allowed to breathe; it is not a montage.

### If it runs long

Cut **"And when you change one model, dbt already knows what else has to be rebuilt"** (1:07) first.
It is the only sentence in the script that is not load-bearing.

---

## On-Screen Text Cues (already in the deck)

| Timing | On-Screen Text |
|--------|----------------|
| 0:00–0:10 | "What is dbt?" |
| 0:10–0:30 | "A model is just a SELECT" |
| 0:30–0:42 | "Run it, and it builds" |
| 0:42–1:12 | "dbt works out the order" |
| 1:12–1:30 | "All of it in one window" |
| 1:30–1:40 | "That's dbt." |

---

## Publishing

- **Title**: `What is dbt? | Rosetta DBT Studio`
- **Playlist**: first position in a "Start Here" playlist.
- Deliberately does NOT use the "in X Seconds" title pattern — it would collide with the existing
  "Get Started with Rosetta DBT Studio in 60 Seconds" and leave a newcomer unable to tell which video
  comes first.
