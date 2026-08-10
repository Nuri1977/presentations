# Lesson 2 - Prompt and Assets Checklist

Lesson 2, "What you'll build", is a roadmap video. It shows the finished destination up front so a beginner knows where the path leads before any installation happens.

Format: screen recording of the app, with a full-frame title card at the start and a closing card at the end. Concept text appears as transparent overlay cards composited on top of the footage in CapCut. Same approach as lesson 1.

App version at time of production: 1.6.1.

## Assets in this folder

| Path | What it is | Status |
|---|---|---|
| `voiceover-script-70sec.md` | Plain script. Subtitle source. | Done |
| `voiceover-kokoro.txt` | Same words with Kokoro markup. | Done |
| `RECORDING-cue-sheet.md` | The four beats and prep state. | Done |
| `video-presentation.html` | Reference deck, black backgrounds. | Done |
| `slides/1.png` | Title card, full frame 1920x1080. | Done |
| `slides/5.png` | Closing card, full frame 1920x1080. | Done |
| `overlays/card-project.png` | Overlay card, transparent, bottom right. | Done |
| `overlays/card-lineage.png` | Overlay card, transparent, top right. | Done |
| `overlays/card-ai.png` | Overlay card, transparent, bottom left. | Done |
| `sounds/` | Kokoro MP3 per slide. | To generate |
| Screen recording | The raw OBS capture. | To record |

## Overlay card placement

Each PNG is a full 1920x1080 frame with the card already positioned. In CapCut, drop it at position 0,0 with scale 100% and it lands correctly. Do not reposition or rescale.

Positions were chosen so the card never covers the thing the narration is pointing at:

- `card-project` sits bottom right, because the models tree is in the left explorer.
- `card-lineage` sits top right, because the graph occupies the lower panel.
- `card-ai` sits bottom left, because the AI chat panel renders on the right side of the screen.

Fade each card in and out using CapCut Animation on the clip itself. Do not use a Transition between clips, since that dips the whole frame including the footage.

## Timing

Cards should appear as the matching line is spoken and leave before the next beat starts. Rough targets, to be confirmed against the generated audio:

- `card-project` on "Raw data goes in, and these are your models"
- `card-lineage` on "Rosetta draws the shape of your project for you"
- `card-ai` on "Ask a question in plain English"

## Open items

- Kokoro pronunciation of "dbt" is still unverified. It appears once in this lesson. If it reads as a word rather than dee bee tee, apply `[dbt](/dˌibˌitˈi/)` in `voiceover-kokoro.txt`.
- AI is set up and verified: Groq via the OpenAI Compatible provider type, model `llama-3.3-70b-versatile`, Ask mode, Auto Continue off. The exact prompt is in the cue sheet. Gemini was dropped for production because its free tier allows only 20 requests per day.
- The AI code block header renders as `hljs sql` instead of `sql`. App bug, visible in every lesson where the AI returns code. Worth reporting, not worth blocking on.
- Audio target is -14 LUFS. The lesson 1 export came out at -28 LUFS and needed a normalization pass afterwards. Set the level correctly in CapCut this time.
- Keep the terminal scrolled past any line showing the full user path.
