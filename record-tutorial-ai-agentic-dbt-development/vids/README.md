# Google Vids package

One video per section. Each section: slides with an AI voiceover first, then your screen recording of the demo in Rosetta dbt Studio, then the recap slide.

| Section | Title | Scenes | Voiceover | Demo budget | Import file |
|---|---|---|---|---|---|
| S00 | Welcome & the agentic loop | 13 | 3.7 min | 5.8 min | `s00-welcome.pptx` |
| S01 | Load the real data: dbt is the "T" | 13 | 3.8 min | 5.7 min | `s01-load-real-data.pptx` |
| S02 | Project anatomy & teaching the agent | 13 | 3.4 min | 6.1 min | `s02-project-anatomy.pptx` |
| S03 | Sources | 14 | 3.3 min | 6.2 min | `s03-sources.pptx` |
| S04 | Seeds | 11 | 2.5 min | 7.0 min | `s04-seeds.pptx` |
| S05 | Staging models | 14 | 3.7 min | 5.8 min | `s05-staging-models.pptx` |
| S06 | Data tests | 14 | 3.4 min | 6.1 min | `s06-data-tests.pptx` |
| S07 | Packages, Jinja, macros & analyses | 14 | 3.3 min | 6.2 min | `s07-packages-jinja-macros.pptx` |
| S08 | Intermediate, marts & materializations | 16 | 4.1 min | 5.4 min | `s08-intermediate-marts.pptx` |
| S09 | Unit tests | 10 | 2.4 min | 7.1 min | `s09-unit-tests.pptx` |
| S10 | Incremental models & a schema change | 15 | 3.8 min | 5.7 min | `s10-incremental.pptx` |
| S11 | Snapshots | 13 | 2.7 min | 6.8 min | `s11-snapshots.pptx` |
| S12 | Docs, lineage & exposures: the capstone | 15 | 3.1 min | 6.4 min | `s12-docs-exposures.pptx` |
| S13 | Wrap-up & what's next | 7 | 1.5 min | 8.0 min | `s13-wrap-up.pptx` |

Voiceover times assume about 150 words per minute; check the first video and adjust.

## Workflow for one section

1. **Numbers (real-data slides only).** Upload the `.pptx` to Google Drive and open it with Google Slides. Replace each amber `?` with your dry-run result.
2. **Convert.** In Google Vids: new video → **Landscape** → **Convert Slides** → pick the presentation → select all slides. Keep **Include AI voiceover, script, background music and animation** on.
3. **Script.** On the script step, click **Replace with speaker notes**. Each scene now has the voiceover from this package. Pick a voice, then import.
4. **Record the demo.** Follow the cue sheet in the section's `.md` file. Record with Vids' own recorder, or upload a screen recording. Trim the waiting while the agent works.
5. **Order.** Drag the recap scene (the last slide) after the recording.
6. **Check the length.** Vids videos are limited to 10 minutes. If the demo runs long, split it into a second video.

## Notes

- Scripts contain no square brackets on purpose: Vids reads `[ ]` as voice tags such as `[excitedly]`. Add tags yourself if you want them.
- Code names (like `stg_tlc__yellow_trips`) are spoken as plain words ("the staging model for yellow trips"), because AI voices read underscores badly. The exact names are on the slides.
- Regenerate this package after editing the slides: `python3 vids_build.py <slides folder> <out folder>` from the slides `_source` folder.
