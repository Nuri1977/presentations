# Lesson 2 - Recording Cue Sheet

This sheet covers the screen recording only. The opening and closing cards are `slides/1.png` and `slides/5.png`, dropped in during editing, so nothing is performed for them.
App version: 1.6.1. Project: `dbtstudio_getting_started` on DuckDB.

## Before you hit F9

- Models already generated (staging + enhanced), so `models/` is full. Lesson 2 shows the destination, not the process.
- `staging` and `enhanced` folders expanded in the explorer.
- No file open in the editor.
- Terminal tab selected in the lower panel, scrolled to the bottom of a previous successful run so `Completed successfully` and `Done. PASS=8` are visible. Scroll far enough that the `cd "C:\Users\...` line at the top of the run is off screen.
- AI panel **closed**. The AI beat opens it on camera, since the line "You will also have AI built into the app" is a reveal. If the panel is already open the moment lands flat.
- AI set to the Groq provider on Ask mode with Auto Continue off, per the setup table below.
- A fresh chat prepared behind the closed panel, so no earlier tool rows or messages appear when it opens.
- App maximized, taskbar auto-hidden, OBS windows hidden from capture.

## Beats

Five moves. Everything else holds still.

| Listen for | Do this |
|---|---|
| "Raw data goes in, and these are your models" | Scroll or gesture across the populated `models/` tree, then open one enhanced model |
| "Rosetta draws the shape of your project for you" | Click the LINEAGE tab, hold on the graph |
| "You will also have AI built into the app" | Open the AI panel |
| "Ask a question in plain English" | Paste the prompt and press enter |
| "and it writes the query for you" | Hold on the generated SQL until the line ends |

Put the prompt on the clipboard before recording and paste it rather than typing. Typing it out takes far longer than the line allows, and pasting is one deterministic action.

## AI setup and prompt

This configuration was tested and produces a clean result. All four parts matter.

| Setting | Value |
|---|---|
| Provider type | OpenAI Compatible |
| Base URL | `https://api.groq.com/openai/v1` |
| Model | `llama-3.3-70b-versatile` |
| Chat mode | **Ask**, not Code |
| Auto Continue | **Off** |

Prompt, exactly as written:

`Write a query that shows which major has the most students in main_students. Only the SQL, in a code block.`

Each clause earns its place. Naming `main_students` stops the model exploring the project for the table. "Only the SQL" removes the explanation and the unhelpful advice about switching to Code mode, which would confuse a beginner in lesson 2. "In a code block" keeps the syntax highlighted block, which reads far better on camera than plain wrapped text.

Why Auto Continue must be off: with it on, the agent runs a tool loop of up to 80 model round trips and the answer took over 20 seconds. With it off the loop is a single step and the reply is quick enough to land inside the narration line.

Gemini is not used for this lesson. Its free tier allows 20 requests per day, which is not enough for repeated takes.

## Known cosmetic issue

The code block header renders as `hljs sql` rather than `sql`. This is an app bug in the message renderer, not something to fix before recording. It will appear in every lesson where the AI returns code.

## Recording

F9, wait 3 seconds, start the Kokoro MP3 on your phone, perform the beats in sync. Let it run 3 seconds past the last word before F9 again. If a beat lands late, keep going and re-take the whole pass. One clean pass edits better than a splice.

## Known issue to avoid

The lesson 1 recording exposed the full run command in the terminal, including the user path. If the terminal is visible in any beat here, either scroll it past that line first or plan to mosaic it in CapCut.
