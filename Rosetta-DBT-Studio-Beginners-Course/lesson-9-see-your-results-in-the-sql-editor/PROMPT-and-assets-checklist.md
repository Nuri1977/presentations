# Lesson 9 - Prompt and Assets Checklist

Lesson 9, "See your results in the SQL Editor", is the first time the viewer sees actual rows out of a model they built. The point it has to land is that the SQL Editor works on a connection rather than a project, and that a view stores nothing, which is why it was cheap to build and cannot go stale.

Format: screen recording, with full frame cards for the intro and the close. Concept text is composited on top of the footage in CapCut as transparent content cards. Same approach as lessons 1 to 8.

App version at time of production: **1.6.6**.

## Assets in this folder

| Path | What it is | Status |
|---|---|---|
| `voiceover-script-145sec.md` | Plain script. Subtitle source. | Done |
| `voiceover-kokoro.txt` | Same words with Kokoro markup. | Done |
| `RECORDING-cue-sheet.md` | Beats, the query, and the verified result. | Done |
| `video-presentation.html` | Reference deck, nine slides. | Done |
| `slides/1.png` | Intro card, full frame. | Done |
| `slides/9.png` | Closing card, full frame. | Done |
| `overlays/1. card-connections-not-projects.png` | Content card, bottom left. | Done |
| `overlays/2. card-data-tab.png` | Content card, bottom left. | Done |
| `overlays/3. card-ask-it.png` | Content card, bottom left. | Done |
| `overlays/4. card-the-answer.png` | Content card, bottom left. | Done |
| `overlays/5. card-what-a-view-is.png` | Content card, bottom left. | Done |
| `overlays/6. card-saved-queries.png` | Content card, bottom left. | Done |
| `overlays/7. card-query-history.png` | Content card, bottom left. | Done |
| `overlays/unused/2. card-select-connection.png` | Dropped 18 Sep 2026 when slide 3 merged into slide 2. Kept, not deleted. | Unused |
| `sounds/` | One voiceover per slide, nine of them. | To generate |
| Screen recording | Connection, one query, save, history. | To record |

## Overlay card placement

All seven bottom left, and this one is settled rather than guessed. Lesson 4 established from real footage that the SQL Editor opens the AI panel on the right, which covers a right hand card. Its own cards 3 and 4 were moved left for the same reason.

Each PNG is a full 1920x1080 frame. Drop it at 0,0 with scale 100%. Fade with CapCut Animation on the clip, never a Transition.

## What is verified, and how

- The query result, Physics 29, Mathematics 28, Computer Science 24, Literature 19, summing to 100: run against the real DuckDB file after lesson 8's build.
- The nine objects and their kinds: queried from `information_schema`.
- The three left hand tabs, Data, Queries and Analytics: `screens/sql/index.tsx:963-995`.
- Select Connection top left, the plus creating a new one, one connection at a time: lesson 4's script, written from real footage.
- The connection is named **DBT Connection**, not the project name. It is the reserved default for the getting started template: `main/services/connectors.service.ts:297,1774`.
- Saved queries filter and `.sql` import: `components/sqlEditor/SavedQueriesList.tsx:267,278`.
- Save Query and Query History as separate surfaces: `components/sqlEditor/index.tsx:460` and `queryHistory/index.tsx:219`.
- The AI panel opening on the right: lesson 4, from footage.
- The chart picks its own axes, a text column along the bottom and the number columns as values, which is why slide 5 can say it "already knows which column goes where": `components/queryResult/queryVisualization/QueryResultVisualization.tsx:94-104`. Chart types are Bar, Line, Scatter and Pie: `ChartConfig.tsx:84-87`.

## Wording note

The script never reads a table name aloud, so Kokoro is never handed `main_students`. The cards carry it instead, which is the same approach as lessons 6 and 7.

Slide 6 says building a view "took about a quarter of a second". The measured figures were 0.21 to 0.25 seconds across the four views, so that is honest at the precision it is spoken.

## No forward references

The closing line into notebooks is the only one, which is the allowed handoff.

## Open items

- Record after lesson 8, with all nine objects present.
- Clear Saved Queries and Query History for this connection first, so slides 7 and 8 are not landing on leftovers.
- The query is pasted, not typed. Typing it live ran 40 seconds against 11 seconds of narration on slide 4.
- Audio target is minus 14 LUFS.
