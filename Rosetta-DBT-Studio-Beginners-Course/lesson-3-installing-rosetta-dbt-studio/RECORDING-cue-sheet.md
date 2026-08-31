# Lesson 3 - Recording Cue Sheet

Two complete walkthroughs, Windows then Mac, each running from the download page to the app open on screen. A viewer watches their own platform start to finish and can stop there.

Full frame cards are `slides/1.png` (intro), `slides/7.png` (Mac divider) and `slides/14.png` (closing). They are dropped in during editing, so nothing is performed for them.

App version: 1.6.1. Download source: rosettadb.io, via Download Now then Choose your build. The page auto detects your platform and badges the matching card with "This is for you", so the Windows card is already highlighted when you land on it.

## What makes this lesson different

Every earlier lesson was filmed on a machine that already had the app. This one needs a machine without it. Read the prep section before touching anything, because the download and install beats can only be filmed once per uninstall.

## Prep, before the Windows pass

- Uninstalled, **and** five leftover locations deleted by hand. The uninstaller removes almost none of them, and reinstalling on top restores old settings and skips the wizard. Delete all of these:
  - `C:\Users\Edon\AppData\Roaming\rosetta-dbt-studio` (the bundled Python, the venv with dbt, and all config)
  - `C:\rosetta` (the Rosetta CLI, reinstalled by the app each time)
  - `C:\Users\Edon\AppData\Local\rosetta-dbt-studio-updater` (cached installer)
  - `C:\Users\Edon\AppData\Local\Programs\rosetta-dbt-studio`
  - `C:\Users\Edon\rosetta-dbt-studio-projects`
- Close the app before deleting. If it is running, the uninstaller cannot remove the locked exe and asar files and leaves them behind.
- Do not touch the system Python at `AppData\Local\Programs\Python`. That is a separate install and Rosetta does not use it.
- Your Groq API key saved somewhere outside the app. It lives encrypted in the keystore and will not survive. You need it again for lessons 16 to 19.
- Chrome open on rosettadb.io, in a clean window, with no personal bookmarks, tabs or profile avatar visible. Start on the home page, not the download page, since the first beat is clicking Download Now.
- Downloads folder cleared of older Rosetta installers, so the file that appears is unambiguous.
- Desktop clear of personal files, taskbar auto-hidden, OBS windows hidden from capture.

## Windows pass

| Listen for | Do this |
|---|---|
| "Head to rosettadb.io, and click Download Now" | Chrome on rosettadb.io, click Download Now |
| "Then Choose your build" | Click Choose your build, land on the three platform cards |
| "Click Download for Windows" | Click the Windows card's button, let the download finish |
| "Open the installer and let it run" | Run it, hold through to completion |
| "It brings its own Python, so nothing else to install" | Hold on the installer, 10x ramp, about 11 sec |
| "Leave every adapter ticked, and click Install" | Wizard at 1x, click Install |
| "It installs dbt and every adapter. This takes a couple of minutes" | 100x ramp, then back to 1x as it completes |
| "Then two confirmations. Python installed, and dbt installed" | Hold on the confirmation alerts at 1x |
| "Click Finish" | Click Finish, let the app open |
| "Give it a moment, and Rosetta DBT Studio opens for the first time" | Loading after Finish, 10x blip at 43-44, about 6 sec |
| "Last thing. It offers you a quick tour of this screen" | Welcome popup appears, let it sit, do not click |
| "showing where your projects live" | Hold on the popup through the rest of the line |

End the Windows pass with the tour popup showing. Do not click **Let's Go**, and do not click **Skip** either. The popup already shows both buttons, so the narration does not tell the viewer to take it or skip it. It only says what the tour contains and lets them decide. Dismissing it on camera would read as if the tour is in the way.

That popup is the shot the divider card cuts away from.

## The quick tour

The app opens with a **Welcome to DBT Studio** popup, seven steps, which the app itself says takes about 30 seconds. Its buttons are **Skip** and **Let's Go**.

Every step targets the project launcher screen, not the workspace: the projects area, the new project button, Get Started, Import, the connections nav, and the search bar. None of it overlaps lesson 4, which walks the file explorer, editor, sidebar, run controls and status bar inside an open project.

The lesson shows the popup and names it, then stops. It is not clicked through. The reason is that the viewer will see this popup on their own screen at exactly this moment, so it has to appear in the video or they will think they did something wrong. Beyond that, its content is covered properly by lessons 5 and 13, and watching someone read seven popups is dead air.

## Mac pass

The Mac pass mirrors the Windows pass beat for beat, so a viewer who skipped the first half gets the whole path. **The setup wizard is identical on both platforms.** Three things differ: two downloads instead of one, dragging instead of running an installer, and the first open confirmation from macOS. That last one is deliberately not narrated and has no card. Mac users have installed downloaded apps before, so it just happens on screen.

The Mac narration never refers back to the Windows pass. The intro tells viewers to skip ahead to their own platform, so this section has to stand on its own for someone who never watched the first half.

Slides 10 to 13 were rewritten after the first Mac attempt. The pass now runs across six beats rather than five, because the browser download, the first open prompt and the splash screen were all missing from the original script.

| Slide | Listen for | Do this |
|---|---|---|
| 8 | "Head to rosettadb.io, and click Download Now" | Chrome on rosettadb.io, click Download Now |
| 8 | "Then Choose your build" | Click Choose your build, land on the three platform cards |
| 8 | "One for Apple Silicon, and one for Intel" | Point at Mac ARM64, then Mac Intel |
| 8 | "it downloads through your browser like any other file" | Click one, let the browser download bar show |
| 9 | "Open it when the download finishes" | Open the downloaded file, the installer window appears |
| 9 | "Drag Rosetta DBT Studio into your Applications folder" | Drag the app across, hold on it landing |
| 10 | "Now open your Applications folder, and start Rosetta DBT Studio from there" | Open Applications, double click the app |
| 10 | (no narration here) | The macOS prompt appears. Let it sit a beat, click **Open**, keep moving. It is not narrated and no card covers it |
| 10 | "First launch takes a moment" | Hold on the splash. Ramp it if it runs long. Overlay card 3 sits here |
| 11 | "Now the setup" | Land on the setup wizard |
| 11 | "Leave them all ticked, and click Install" | Click Install without touching the ticks |
| 11 | "This takes a couple of minutes" | 100x ramp, then back to 1x as it completes |
| 11 | "When it finishes, click Next" | Click Next |
| 12 | "Two confirmations. Python installed, and dbt installed" | Hold on the confirmation alerts at 1x |
| 12 | "Now click Finish, and it restarts itself" | Click Finish. The app quits and relaunches, so the screen goes empty for a moment |
| 13 | "Give it a moment, and Rosetta DBT Studio opens for the first time" | Splash returns, then the main window |
| 13 | "Last thing. It offers you a quick tour of this screen" | Welcome popup appears. Let it sit, do not click |

## Finish quits the app and relaunches it

**Finish and Skip Setup run the same code.** `setup/index.tsx:109-113` sends the Finish button to `handleSkip()`, which sets `isSetup: 'true'` and calls `windows:closeSetup`. That handler, `main.ts:306-309`, is `app.relaunch(); app.quit();`.

So the app does not simply close a window. It exits completely and starts again, coming back through the splash a second time. The second splash is shorter, because `isFirstRun` is now false and it skips the Rosetta download.

This is why the Mac narration says "click Finish, and it restarts itself" rather than "and the app opens". A beginner whose screen goes empty mid install will otherwise assume it crashed. The Windows pass already covers the same gap with "Give it a moment, and Rosetta DBT Studio opens for the first time".

**Watch this on the Mac.** `app.relaunch()` is cross platform, but macOS does not always bring a relaunched app back to the front. If it returns behind other windows or only bounces in the Dock, the beat needs a line about clicking it, and it is worth reporting as a papercut.

## The Mac must be genuinely clean, or the wizard is skipped

This cost a take. On the first attempt the setup wizard never appeared, which looked like a Mac difference and is not one.

`main.ts` runs `if (settings.isSetup !== 'true') showSetupWindow(); else showMainWindow();` with **no platform branch**, and `setup/index.tsx` has no platform conditionals either. The adapter list is hardcoded and the same on both.

Two pieces of leftover state can skip it:

- `isSetup` already `"true"`, so the wizard never opens at all.
- `pythonPath` and `dbtPath` both set, so the wizard opens **past** the adapter list, straight to the finish step.

Settings live at `~/Library/Application Support/rosetta-dbt-studio/database.json`. Check before filming:

```bash
grep -E 'isSetup|pythonPath|dbtPath' ~/Library/Application\ Support/rosetta-dbt-studio/database.json
```

For a true first run, quit the app and delete that folder, `/Applications/Rosetta DBT Studio.app`, and `~/rosetta-dbt-studio-projects`.

## The setup wizard

Window title is **Rosetta dbt™ Studio - Setup**, with the line "Before continuing, you need to set up dbt™ Core and the necessary adapters on your system."

A blue info box confirms Python is already installed and gives its full path. Below that, **Select dbt™ Adapters** lists `dbt-core` greyed and locked on, plus postgres, snowflake, bigquery, redshift, databricks and duckdb, all ticked by default. An **Install** button sits under the list. **Next** stays greyed out until the install finishes. There is also a **Skip Setup** button.

Leave every adapter ticked and do not touch **Skip Setup**. The narration tells the viewer to leave them alone and click Install, so changing the selection on camera contradicts the line.

The click path is Install, wait for it to finish, then Next. The following step shows two confirmation alerts, "Python environment is successfully installed at" and "All set! dbt path:", with a Finish button.

Note that Rosetta downloads and installs its own Python 3.10.17 inside its own folder. It ignores any Python already on the machine, so the wizard behaves the same whether or not the viewer has Python installed.

**This screen shows your username.** The info box reads `C:\Users\Edon\AppData\Roaming\rosetta-dbt-studio\venv\Scripts\python.exe`, and the narration points straight at that box. It cannot be scrolled away or avoided. Plan to mosaic just the path portion in CapCut, leaving "Python environment (version 3.10.17) is already installed at" readable, since that text is the point of the shot.

## Retaking the wizard without reinstalling

Settings, About, Advanced Options has **Reset Factory Settings**. It deletes `database.json`, clears the keystore, and resets `pythonPath`, `dbtPath` and `isSetup` to empty, which brings the setup wizard back. So the first launch beats can be retaken freely.

It also deletes every registered project directory from disk, including `dbtstudio_getting_started` and its generated models. Back that up first or accept regenerating it.

It does not touch the installation, so the download and install beats still need a real uninstall.

## Verify before recording

- **Antivirus false positive is likely, not just possible.** The download page lists 1.6.1 released 24 July 2026, and the fix pinning Electron to 31.7.6 merged on 29 July 2026. So the published installer predates the fix. If Windows Defender or another scanner flags it, stop and ask whether a newer build can be published before filming. Recording a malware warning in a beginner course is worse than delaying the lesson.
- Windows installer is 114.5 MB, macOS 164.7 MB. Neither download is instant, so expect to trim the download bar footage.
- **On Mac, expect the first open prompt.** "Rosetta DBT Studio is an app downloaded from the Internet. Are you sure you want to open it?" is the normal quarantine dialog and a notarized app still shows it. It is now a scripted beat on slide 10, not a problem. What notarization prevents is the different and worse dialog, "cannot be opened because the developer cannot be verified". If you see **that** one, stop and report it. To confirm the build is fine, run `spctl -a -vvv -t install "/Applications/Rosetta DBT Studio.app"` and look for `source=Notarized Developer ID`.
- Check whether `feature/dbt-core-v2-support` has changed the adapter list, since it merged after this sheet was written.

## Recording

F9, wait 3 seconds, start the Kokoro MP3 on your phone, perform the beats in sync. Let it run 3 seconds past the last word before F9 again.

Installs take far longer than the narration allows. Do not try to match real time. Record the full install, then compress it in CapCut so the picture keeps pace with the voice.

## Measured timings, Windows pass

These are from the recorded take, not estimates. The narration is written to fit them.

| Window | What is on screen | Speed | Narration |
|---|---|---|---|
| 11 to 19 | download page, clicking through | 1x | slide 2 |
| 19 to 30 | installer running, Rosetta loading | 10x | slide 3, about 11 sec |
| 31 to 36 | setup wizard, adapter list, click Install | 1x | slide 4 first line |
| 36 to 38 | adapter install | 100x | slide 4 second line |
| 38 to 41 | install completing | 1x | slide 4 second line continues |
| 41 | confirmations shown, Finish clicked | 1x | slide 5 ends here |
| 41 to 47 | loading after Finish, 10x blip at 43 to 44 | mixed | slide 6 first line |
| 47 onward | app opens, tour popup | 1x | slide 6 second line, hold as long as needed |

Do not put the Finish click inside the 100x ramp. It is an action the viewer has to take, and that screen is the only frame that proves the lesson's claim, since it reads "Python environment is successfully installed" and "All set! dbt path".

Coming out of the 100x ramp, step the speed down rather than cutting. Split into 100x, then about a second at 10x, then 1x, with the last split placed where the app changes screens. The app's own screen change then masks the join and no transition is needed. If it still reads as a jump, use a 0.3 second cross dissolve, not a fade to black. Black is reserved for the Mac divider.

## Card timings, Windows pass

Anchored to the recorded take. Bring each card in about a second after its narration starts, and out about a second before the next beat, so it never appears exactly on a cut.

| In | Out | Card | Over what |
|---|---|---|---|
| 12.0 | 18.5 | `overlays/windows/1. card-download-win.png` | the download page, clicking through |
| 20.0 | 29.0 | `overlays/windows/2. card-install-win.png` | the installer running at 10x |
| 32.0 | 40.0 | `overlays/windows/3. card-setup.png` | the wizard, the adapter list, the 100x install |
| 41.5 | 45.5 | `overlays/windows/4. card-finish.png` | the two confirmations and the Finish click |
| 48.0 | end minus 1.5 | `overlays/windows/5. card-tour.png` | the Welcome tour popup |

Leave 45.5 to 48.0 with no card. That is the app loading and opening, and the narration is carrying it. A gap there lets the reveal land.

Cards live in `overlays/windows` and `overlays/mac`, numbered in the order they appear. The setup, finish and tour cards are identical in both folders, since those three screens are the same on either platform.

All five are full 1920x1080 frames. Drop each at position 0,0, scale 100%. Do not move or resize them.

Fade in and out with **Animation** on the card clip itself, about 0.3 seconds each way. Do not use a **Transition**, which dips the whole frame including your footage.

## Card timings, Mac pass

To be filled in once the Mac pass is recorded. Use `overlays/mac`, in the order the numbers give: 1 download, 2 install, 3 first open, 4 setup, 5 finish, 6 tour.

## Editing the adapter install

This is the longest wait in the lesson and the narration gives you about twelve seconds to cover it.

Do not cut the audio and hold on silence. Dead air over a progress bar is what makes a tutorial feel slow. The voice runs continuously and the footage bends around it.

The sequence:

1. Land the click on "and click Install".
2. Hold about a second at normal speed, so the viewer sees it genuinely start. That beat tells them their own machine is doing the same thing.
3. Speed ramp the middle of the install, roughly 10x, across "It downloads dbt and every adapter you ticked, so give it a couple of minutes". The bar should visibly move rather than teleport.
4. Return to normal speed as it completes, landing on "When it finishes, click Next".

Time the real install during your take. The narration says a couple of minutes, so if it comes in much faster or much slower than that, change the line rather than leave a number that does not match what the viewer sees.

A hard cut with a half second cross dissolve is the acceptable alternative if the ramp looks bad. What to avoid is a 40x ramp, which reads as broken rather than compressed.

The two passes are separate recordings. They are joined in editing with the Mac divider card between them.

## Known issue to avoid

Installer dialogs and the browser download bar both expose the user folder. Keep `C:\Users\Edon\...` out of frame where you can, and plan to mosaic it where you cannot.