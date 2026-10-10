# Release roundup — Rosetta DBT Studio 1.7.2

A 60-second narrated promo for [release 1.7.2](https://github.com/rosettadb/dbt-studio/releases/tag/1.7.2) (8 Oct 2026). It leads with the **ChatGPT subscription** provider: frontier models on the plan you already pay for, with no API key and no per-token bill. After that it covers public S3 buckets, notebook tables and the Settings redesign.

- **Video:** both files run 59.9 s and use H.264 with stereo AAC, normalized to −16 LUFS. Captions are in the matching `.srt`.
  - `promo-60s/rosetta-dbt-studio-1.7.2-promo-60s.mp4`: 1920 × 1080. This one plays anywhere (QuickTime, chat previews, Slack).
  - `promo-60s/rosetta-dbt-studio-1.7.2-promo-60s-4k.mp4`: 3840 × 2160. Upload this one to YouTube. Some players and older Intel Macs won't play 4K H.264 smoothly or at all.
- **Deck:** `promo-60s.html`. Each slide is a fixed 1920 × 1080 canvas that scales to the window.
- **Script:** `voice-over-script.txt` has the narration, visuals and timings for each slide. It is 125 words.

Upload the 4K file to YouTube even if most people will watch it at 1080p, because a 4K upload gets a much better encode. HD and 4K playback appear only after YouTube finishes processing, so the first few minutes may look soft.

## Controls (deck)

- **← / →** (or Space): previous / next slide. **Home / End**: first / last slide.
- **T**: transcript panel (This slide / All / Copy).
- **H**: hide the progress bar and controls. **F**: fullscreen.
- The URL hash tracks the slide, so `#3` opens slide 3.

## Slides

| # | Time | Topic | Visual |
|---|------|-------|--------|
| 1 | 0:00 | Hook: frontier models on your ChatGPT plan | ChatGPT model list in Edit AI Provider |
| 2 | 0:10 | Sign in with Plus/Pro, pick a model, no API key | Edit AI Provider (ChatGPT subscription), full-bleed |
| 3 | 0:24 | The AI agent runs on your plan | Agent fixing a notebook cell with `gpt-6-luna` |
| 4 | 0:32 | Public S3 buckets, no credentials | CSV preview + "Public bucket (no credentials)" form |
| 5 | 0:41 | Notebook tables + Settings redesign | Notebook output table, dbt Core settings |
| 6 | 0:49 | Download / GitHub CTA | Centered |

## Files

- `promo-60s/`: the MP4, the `.srt`, `narration.wav`, `timeline.json`, the per-slide audio in `audio/`, and `build_video.py` (Kokoro TTS, a 50/50 blend of the `af_heart` and `af_bella` voices at speed 1.05; pass `--voice af_heart+af_bella`).
- `assets/`: screenshot filenames start with their slide number. Window screenshots are cropped to the app window, without the macOS shadow. `slide-06-rosetta-logo.png` and `linear-white-bg.svg` are copied from `../release-1.7.1/assets/`. These spares are not used in the deck: `slide-02-chatgpt-model-picker.png`, `slide-04-s3-bucket-files.png`, `slide-04-s3-public-bucket.png`, `slide-05-notebook-output-fullscreen.png`, `slide-05-settings-ai-providers.png`, `slide-05-settings-general.png`, `slide-05-settings-rosetta-cloud.png`, `slide-05-settings-dbt-core.png`.

To rebuild, run the command at the end of `voice-over-script.txt`. Add `--measure` to check the length before rendering.

## Accuracy notes (check before publishing)

- **Price claim (#473):** the video says "no API key, and no per-token bill", and the slide 2 card adds "Plan usage limits apply". This follows the app's own text: "Uses your ChatGPT Plus/Pro plan instead of an API key… Plan usage limits apply." It deliberately does not say "cheapest". The provider is labelled **Experimental** in the app, and slide 2 shows that chip.
- **Model names:** "GPT-5.5 to GPT-6" comes from the model dropdown in the screenshot (GPT-5.5, 5.4, 5.4 mini, 5.3 Codex Spark, GPT-6 Sol, GPT-6 Luna). Confirm that this is the list users will see.
- **Your email is visible** (nurilacka@gmail.com) in the Edit AI Provider dialog on slides 1 and 2. Blur it if you don't want it in a public video.
- **Slide 3:** the agent's notebook tools existed before 1.7.2. The slide only shows them running on the ChatGPT plan, with the `gpt-6-luna` chip in the chat input.
- **Notebook tables (#490):** the PR title only says "table and pagination improvements". The Copy / Clear / View output fullscreen menu in the screenshot may come from an earlier release.
- **Date column:** `order_date` shows as `{'days': 17532}` in the notebook screenshots on slides 3 and 5. Viewers may notice, and it looks like a date-serialization bug worth fixing or re-shooting.
- **Public S3 (#494):** the Schema and Statistics preview tabs are shown but not claimed as new.
- **Left out for time (minor items):** text cells that expand to fit their content (#491), easier add-cell buttons (#497), errors for rejected image attachments in AI chat (#493), and new Rosetta pipeline steps defaulting to the rosetta working directory (#492).
- **Resolution:** the source screenshots are about 1920 px wide (not Retina), so full-bleed slides are upscaled 2× in 4K. Retina originals (Cmd+Shift+4 PNGs) of slides 2 and 3 would make them sharper.
- **Voice:** an LLM-grade voice (ElevenLabs, OpenAI gpt-4o-mini-tts, Chatterbox) couldn't be generated in the session that built this, because Hugging Face and the cloud TTS APIs were blocked. If you export the narration from one of those as per-slide audio files, the video can be re-timed to them.
