# Narrated slide videos

One video per section, voiced locally with Kokoro (voice `af_heart`, speed 1.0). Rendered at 3840×2160 (4K), H.264 + AAC, loudness normalized to about −16 LUFS. Total: 43 minutes of narrated slides.

## Files per section

| File | What it is |
|---|---|
| `sNN-<name>.mp4` | Slides 1 to N−1 with voiceover |
| `sNN-<name>-recap.mp4` | The recap slide, 11–18 s |
| `.srt` | Subtitles, timed per sentence |

## Putting a section together

1. `sNN-<name>.mp4`
2. Your demo recording in Rosetta dbt Studio (cue sheet: `../vids/sNN-<name>.md`, section "Demo recording")
3. `sNN-<name>-recap.mp4`

The recap narration starts with "That is section N…", so it is written to come after the demo.

## Section lengths

| Section | Slides video | Recap |
|---|---|---|
| S00 Welcome | 3:27 | 0:13 |
| S01 Load the real data | 3:26 | 0:18 |
| S02 Project anatomy | 3:11 | 0:13 |
| S03 Sources | 2:52 | 0:13 |
| S04 Seeds | 2:15 | 0:11 |
| S05 Staging models | 3:10 | 0:15 |
| S06 Data tests | 2:56 | 0:15 |
| S07 Packages, Jinja & macros | 3:01 | 0:13 |
| S08 Intermediate & marts | 3:40 | 0:15 |
| S09 Unit tests | 2:05 | 0:13 |
| S10 Incremental models | 3:26 | 0:13 |
| S11 Snapshots | 2:31 | 0:13 |
| S12 Docs & exposures | 2:52 | 0:13 |
| S13 Wrap-up | 1:21 | 0:13 |

## Before publishing

- **Real-data numbers.** Five slides still show amber `?` placeholders: S01 "What we found", S03 "The empty rows have something in common", S06 "Real data says no", S08 "Why trips are invalid" and S12 "The answer". After your dry run, put the numbers in `numbers.json` (keys are listed in `slides/_source/content_*.py`, field `edit`) and re-render those sections.
- **Narration that depends on the dry run.** S03 scene 11 (the Flex Fare rows) and S06 scene 10 (backwards trips) state a finding. If your dry run disagrees, use the alternative lines in `../vids/s03-sources.md` and `../vids/s06-data-tests.md` and re-render.
- **Listen once** for pronunciation. dbt is read as "D B T", SQL as "sequel", DuckDB as "duck D B", YAML as "yammel", Parquet as "par-kay".
- **YouTube** shows HD/4K only after processing finishes, which can take from minutes to an hour, so the first view may look blurry.

## Re-rendering

`slides/_source/build_videos.py` builds everything from the slides and `tts.py` (needs `kokoro-onnx`, `soundfile`, Playwright, ffmpeg, and the Kokoro model files from github.com/thewh1teagle/kokoro-onnx releases). `refresh_frames.py` re-screenshots single slides and re-encodes, for changing numbers without regenerating the voice.
