# Academy video tooling

Code for the `rosetta-academy-video` skill. See `DESIGN.md` for the decisions behind it.

## One-time setup (per runner)

```sh
npm install --omit=dev            # js-yaml; Playwright comes from the runner (Linux) or devDependencies (Mac: npm install)
./setup-runtime.sh 3.10.17 20250409 1.12.6 1.11.1   # Studio's CPython + pinned dbt, into .cache/
# download the course's pinned release into .cache/app (Linux: the x64 tar.gz from the GitHub release)
```

Linux runner only: `apt-get install -y libxss1 gnome-keyring dbus-x11 fonts-inter fonts-jetbrains-mono`.

## Files

| Path | What it does |
|---|---|
| `lib/studio.cjs` | Seed a throwaway profile from a start state, launch the release, size the window |
| `lib/actions.cjs` | Drawn cursor, eased glides, clicks, editor typing with helpers off |
| `run-headless.sh` | Run a script under Xvfb with a disposable keyring (Linux) |
| `setup-runtime.sh` | Build the pinned Python + dbt runtime |
| `record.cjs` | Play the app scenes of `lesson.yaml` against the release; 4K still after every change + `events.json` |
| `scripts/tts.py` | Kokoro voice per beat + sentence cues (`--human` measures your own `voice-human/<beat>.wav`) |
| `scripts/render_stills.py` | Slide build states, overlay cards and the thumbnail as 4K stills |
| `scripts/compose.py` | Voice-paced timeline, cursor, ripples, zooms, cards, crossfades → MP4, SRT, VTT, timeline |
| `scripts/package.py` | `youtube.md`, `.pptx`, `RECORDING-cue-sheet.md`, `readme.md`, timed beat sheet |
| `scripts/script_from_lesson.py` | `lesson.yaml` → `voiceover-script.md` (beat sheet) |

## Order for one lesson

`script_from_lesson.py` (beat sheet, get approval) → `record.cjs` → `tts.py` → `render_stills.py` → `compose.py` (try `--preview 45` first) → `package.py`.

`.cache/` and `node_modules/` are not committed.

## Things that bite

- **One recording at a time.** `run-headless.sh` always uses Xvfb display `:97`. A second run started while another is still going shares that display, and when the first one exits it takes the display down and the app quits mid-beat (`Target page, context or browser has been closed`).
- **Save every typed file.** The `type` action only types. Add `click_save` after it (and say "save it" in the narration), or the file stays empty on disk and `dbt compile` / `dbt run` will not see it.
- **dbt usage tracking** is blocked in the cloud sandbox and can stall dbt; `lib/studio.cjs` sets `DBT_SEND_ANONYMOUS_USAGE_STATS=false` and `DO_NOT_TRACK=1`.
- **SQL Editor dates.** Studio 1.7.5's result grid shows DATE columns as `{"days": N}`. Select only the columns you need in on-screen queries.
