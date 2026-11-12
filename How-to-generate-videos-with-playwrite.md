# How to generate videos with Playwright

This workflow records a reproducible Electron test in an isolated profile. The recording is evidence of the product flow and its visible result; it does not use the user's normal Electron profile, saved connections, keychain entries, or real tables.

## 1. Run an isolated Electron instance

Use the existing Playwright Electron harness rather than opening the renderer in an ordinary browser. A normal browser can load the development page, but it has no Electron preload bridge and will fail on `ipcRenderer` calls.

The harness should:

1. Create a disposable directory under `/private/tmp`, for example `/private/tmp/rosetta-electron-qa-<run-id>`.
2. Create a separate `profile` directory and set Electron's `app.userData` path to it before loading the app's main bundle.
3. Set `E2E_TESTING=true` and use the existing development Electron entrypoint and renderer assets.
4. Seed only the minimum test project, fixtures, and disposable connections needed for the scenario.
5. Launch with Playwright's `_electron.launch`, wait for the real app window, and close the app with `electronApp.close()` after the run.

The profile path must be checked from the Electron main process and must equal the disposable path. Never point the harness at the user's normal profile. Keep test credentials isolated as well; the existing harness prefixes its keychain service names for this purpose.

Example launch shape:

```js
const { _electron } = require('playwright');

const electronApp = await _electron.launch({
  args: [bootstrapPath, `--user-data-dir=${userDataPath}`],
  cwd: appRepository,
  env: {
    ...process.env,
    NODE_ENV: 'test',
    E2E_TESTING: 'true',
    USER_DATA_DIR: userDataPath,
  },
});

const page = electronApp.windows().find((window) => /#\/?app/.test(window.url()));
await page.waitForLoadState('domcontentloaded');
```

If the app needs a REST catalog or object store, start or reuse the disposable local stack described by the test plan, then record the endpoint, namespace, bucket and fixture names in the run manifest. Do not copy production credentials into the recording.

## 2. Record the screen and save the video on the Desktop

Playwright records the Electron app window, including the renderer UI and its visible transitions. It does not record other macOS windows or native dialogs. Set a fixed viewport and device scale so videos from different runs have the same geometry.

Create a dated run directory on the user's Desktop and pass it to `recordVideo.dir` when launching Electron. The video is finalized when the Electron context closes:

```js
const os = require('os');
const fs = require('fs');
const path = require('path');

const runId = new Date().toISOString().replace(/[:.]/g, '-');
const desktop = path.join(os.homedir(), 'Desktop');
const desktopRun = path.join(desktop, `rosetta-playwright-${runId}`);
fs.mkdirSync(desktopRun, { recursive: true });

const electronApp = await _electron.launch({
  args: [bootstrapPath, `--user-data-dir=${userDataPath}`],
  cwd: appRepository,
  viewport: { width: 1365, height: 1050 },
  recordVideo: {
    dir: desktopRun,
    size: { width: 1364, height: 1050 },
  },
  env: {
    ...process.env,
    NODE_ENV: 'test',
    E2E_TESTING: 'true',
    USER_DATA_DIR: userDataPath,
  },
});

const page = await electronApp.firstWindow();
const video = page.video();
const context = electronApp.context();
await context.tracing.start({
  screenshots: true,
  snapshots: true,
  sources: false,
});

// Run the semantic UI actions and assertions here.

await context.tracing.stop({ path: path.join(desktopRun, 'trace.zip') });
await electronApp.close();

// The video is finalized only after the app/context closes.
const videoPath = video ? await video.path() : undefined;
if (!videoPath) throw new Error('Playwright did not produce a video');
fs.copyFileSync(videoPath, path.join(desktopRun, 'electron-test.webm'));
console.log(`Video saved to ${path.join(desktopRun, 'electron-test.webm')}`);
```

The Desktop folder will contain a self-contained run bundle such as:

```text
~/Desktop/rosetta-playwright-2026-09-27T01-30-00-000Z/
  electron-test.webm
  events.jsonl
  trace.zip
  screenshots/
  manifest.json
```

Do not delete the run directory until the video, trace, screenshots, and logs have been reviewed. If the harness cannot use Playwright's Electron `recordVideo` option, keep the same Desktop run directory and use the event screenshots as a fallback; that fallback is an image sequence, not a true screen video.

For every meaningful action, write a structured JSON Lines record containing:

- UTC timestamp and elapsed milliseconds;
- action number and high-level intent;
- page URL and active tab;
- stable locator or accessibility role/name used;
- visible text or value entered, with secrets and tokens redacted;
- result, changed state, and any visible error;
- screenshot path and video time offset when available.

Log semantic actions rather than only coordinates. A useful event is `click button "Test Access"`, `fill textbox "Namespace name" with "qa_video"`, or `select option "Lakekeeper"`; a raw `(x, y)` click is only a fallback. Record the DOM evidence after important transitions with `ariaSnapshot()` or a focused locator assertion. This makes the timeline explainable and lets another service reconstruct the flow.

Example event helper:

```js
async function record(page, run, action, locator, operation) {
  const started = Date.now();
  const target = await locator.evaluate((node) => ({
    role: node.getAttribute('role'),
    name: node.getAttribute('aria-label') || node.textContent?.trim(),
  }));

  await operation();
  const event = {
    at: new Date().toISOString(),
    elapsedMs: Date.now() - run.startedAt,
    action,
    target,
    durationMs: Date.now() - started,
    url: page.url(),
    screenshot: `screenshots/${String(run.index++).padStart(3, '0')}-${action}.png`,
  };
  await page.screenshot({ path: `${run.root}/${event.screenshot}` });
  appendJsonLine(`${run.root}/events.jsonl`, event);
}
```

Wrap the interaction itself, so a failed click or failed assertion is logged as a failed event. Also save Electron stderr/stdout and Playwright `pageerror` events beside `events.jsonl`. Those logs distinguish an application failure from a harness or environment failure.

## 3. Produce a reviewable run bundle

At the end of a run, retain a small manifest with:

- source branch and application revision;
- harness command and disposable profile path;
- viewport, operating-system version, and Playwright version;
- fixture and connection names;
- pass/fail status and known limitations;
- paths to `events.jsonl`, screenshots, trace, video, and Electron logs.

Close tracing and the app only after the final screenshot and result assertion have been written. Verify that the disposable staging directory is removed on quit when the test covers an import. Do not include access tokens, OAuth secrets, cookies, keychain values, or private user data in the manifest, screenshots, video, or generated script.

## 4. Turn the timeline into a VoiceOver script

Generate the narration from the structured events, not from guessed coordinates. Group adjacent low-level events into one user-facing step, retain the exact visible labels and results, and omit implementation details such as IPC channel names. Each narration line should map back to an event number and timestamp.

Example generated script:

```text
[00:00] Open DataLake and select the disposable Lakekeeper connection.
[00:08] Open the Tables and Views tab and choose the qa_video namespace.
[00:15] Import a.csv as qa_video.zips, then review the three detected rows.
[00:27] Set zip to string and import the table.
[00:42] Open the Data tab and verify that 00501, 02134, and 07030 retain their leading zeros.
[00:55] Open SQL Editor and run the fully qualified SELECT statement.
[01:08] The result grid shows the same three rows, so the REST catalog and object-store read path are working.
```

The generator should produce both files:

- `voiceover.md`, written for a human narrator or a text-to-speech service;
- `voiceover.json`, with `{start, end, eventIds, text}` entries for synchronization.

Before sending the script to another VoiceOver service, review it against the video and the final event log. Remove disposable paths, credentials, internal IDs, and unverified claims. If a test fails, narrate the observed error and stop at that point rather than describing the intended next step.

## 5. Acceptance criteria

A video run is complete when the isolated app launched with the expected preload, every recorded action has a semantic locator and result, the screenshots/video/trace share the same run ID, the final state is asserted, and the generated narration can be followed against the video without inventing actions. The run is repeatable from its manifest and leaves the user's normal app profile unchanged.

## 6. Visual rules for lesson videos (from Project 3 on)

These rules come from Nuri's review of the Project 2 (DuckLake) videos on 12 Nov 2026. Project 2 stays as it is; every new course follows them. The full version is in `SKILL.md`, "Visual rules".

### Zoom: let the app do it, and show the full screen first

1. **Pick one app zoom level and keep it.** Make Studio readable with its own zoom (Cmd +/-, which is Electron's zoom factor; `course.yaml` → `ui_zoom`, e.g. 1.25). Choose the level once per course, check that the sidebar, header, editor, terminal and status bar all still fit, and never change it during the course.
2. **No crop zoom by default.** The video shows the whole app window (`zoom: none`).
3. **Full screen first, every time.** Each app scene, and each return from a slide, opens on the full, unzoomed window and holds it for 1.5 to 2 seconds before anything zooms.
4. **Then at most one zoom into one region**, only for a detail that is still too small (a terminal line, a result cell), and back out to the full screen before looking at another region.
5. **Never** start a scene already zoomed, jump from one cropped region to another, stack a crop zoom on another crop zoom, or show a crop where the sidebar, header or terminal are cut in half. A viewer cannot follow it.

### Slides: icons, and no empty space

1. **Icons on every content slide**, for every product, format or service the slide names (DuckLake, DuckDB, dbt, Parquet, Iceberg, Delta Lake, PostgreSQL, S3, GitHub, Studio).
2. **Icon sources, in order:** Studio's own assets, copied read-only from `dbt-studio/assets/icons/` and `dbt-studio/assets/connectionIcons/`; free open-license sets downloaded into the course's `brand/icons/` (Simple Icons CC0, Lucide ISC, Tabler MIT, Material Symbols Apache 2.0, official brand kits); an existing web URL only as a last resort. Note each source and licence in `brand/icons/SOURCES.md`.
3. **Fill the slide.** Cards, diagrams and code cover more than 60% of the content area between the heading and the footer. When there is little text, make cards and fonts bigger, add icons or a Studio screenshot; never leave half the slide empty.
4. **Check before approval:** on the contact sheet of slide stills, every content slide has icons and no slide is more than about 40% empty.
