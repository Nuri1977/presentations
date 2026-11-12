// Record the app scenes of a lesson as 4K stills after every visible change, plus an event list.
//   node record.cjs <course_dir> <lesson_dir>
// Output: <lesson_dir>/render/app/{frames/*.jpg, events.json, events.jsonl}
// The renderer (scripts/compose.py) turns events into a timeline paced to the voice.
const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');
const { execFileSync } = require('child_process');
const { seedProfile, launchStudio, mainWindow, sizeWindow } = require('./lib/studio.cjs');
const { attachEditor, tameEditor, editorText } = require('./lib/actions.cjs');

const T = path.resolve(__dirname);
const [courseDir, lessonDir] = process.argv.slice(2).map((p) => path.resolve(p));
const course = yaml.load(fs.readFileSync(path.join(courseDir, 'course.yaml'), 'utf8'));
const lesson = yaml.load(fs.readFileSync(path.join(lessonDir, 'lesson.yaml'), 'utf8'));
const OUT = path.join(lessonDir, 'render', 'app');
fs.rmSync(OUT, { recursive: true, force: true });
fs.mkdirSync(path.join(OUT, 'frames'), { recursive: true });
const MAC = course.runner === 'mac-desktop';
const HOME = MAC ? course.learner_home || '/Users/Shared/academy/learner' : '/home/learner';
const APP_BIN = MAC
  ? path.join(T, '.cache', 'app', `Rosetta-DBT-Studio-${course.app.version}-x64`, 'Rosetta DBT Studio.app', 'Contents', 'MacOS', 'Rosetta DBT Studio')
  : path.join(T, '.cache', 'app', `Rosetta-DBT-Studio-${course.app.version}-x64`, 'rosetta-dbt-studio');
const T0 = Date.now();
const log = (...a) => console.log(`[${((Date.now() - T0) / 1000).toFixed(1)}s]`, ...a);
const esc = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

let page, app, seeded, LAUNCH;
// UI zoom (like Cmd + in the app): Studio re-lays-out larger, so 4K frames stay sharp instead of being cropped
// and upscaled later. Mouse coordinates are CSS px; events are written in 1920x1080 DIP, so they are scaled by Z.
const UIZ = course.ui_zoom || 1;            // Studio (Electron zoom factor)
const BZ = course.browser_zoom || UIZ;      // browser pages (smaller viewport at a higher device scale)
let Z = 1;                                  // zoom of the current surface
const dip = (p) => [Math.round(p[0] * Z), Math.round(p[1] * Z)];
async function applyUiZoom(z) {
  if (!app) return;
  await app.evaluate(({ BrowserWindow }, f) => { for (const b of BrowserWindow.getAllWindows()) b.webContents.setZoomFactor(f); }, z);
  if (surface === 'app') Z = z;
  await page.waitForTimeout(700);
}
let nFrame = 0;
let cursor = [1180, 640];
// Two surfaces: the Studio window ('app' scenes) and a headless Chromium page ('browser' scenes),
// both 1920x1080 at scale 2. Each keeps its own cursor position.
let studioPage = null, browser = null, browserPage = null, surface = 'app';
const cursors = { app: [1180, 640], browser: [960, 300] };
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36';
async function getBrowserPage() {
  if (browserPage) return browserPage;
  const { chromium } = require('playwright');
  const opts = { headless: true, viewport: { width: Math.round(1920 / BZ), height: Math.round(1080 / BZ) }, deviceScaleFactor: 2 * BZ, colorScheme: 'dark', userAgent: UA, acceptDownloads: true };
  if (course.browser_profile) {
    // saved recording profile (signed in to GitHub once by Nuri with browser-login.cjs); never Nuri's own Chrome
    browser = await chromium.launchPersistentContext(course.browser_profile, opts);
    browserPage = browser.pages()[0] || (await browser.newPage());
  } else {
    browser = await chromium.launch({ headless: true });
    browserPage = await (await browser.newContext(opts)).newPage();
  }
  return browserPage;
}
// Locator from a lesson.yaml spec: "Exact text" | {role, name, regex?, exact?} | {text, regex?} | {selector}
function loc(spec) {
  if (typeof spec === 'string') return page.getByText(spec, { exact: true }).first();
  if (spec.selector) return page.locator(spec.selector).first();
  if (spec.role) return page.getByRole(spec.role, spec.name === undefined ? {} : { name: spec.regex ? new RegExp(spec.name) : spec.name, exact: spec.regex ? undefined : spec.exact ?? true }).first();
  if (spec.text) return page.getByText(spec.regex ? new RegExp(spec.text) : spec.text, { exact: !spec.regex }).first();
  throw new Error('bad locator ' + JSON.stringify(spec));
}
const specLabel = (s) => (typeof s === 'string' ? s : s.label || s.name || s.text || s.selector);
let steps = []; // steps of the current beat
let beatId = null;
const beats = {};

async function snap() {
  const name = `${String(nFrame++).padStart(5, '0')}.jpg`;
  // a page that is navigating cannot be captured for a moment: retry until the new page has painted
  for (let k = 0; ; k++) {
    try {
      if (surface === 'app' && app && UIZ !== 1) {
        // Studio with a UI zoom: Playwright would capture CSS px x 2 (smaller than 4K); take the window's own pixels
        const sz = await app.evaluate(async ({ BrowserWindow }, out) => {
          const w = BrowserWindow.getAllWindows().find((b) => b.isVisible() && !b.isDestroyed());
          const img = await w.webContents.capturePage();
          process.mainModule.require('fs').writeFileSync(out, img.toJPEG(92));
          return img.getSize();
        }, path.join(OUT, 'frames', name));
        if (sz.width < 3000) throw new Error('capturePage gave ' + sz.width + 'x' + sz.height);
      } else {
        await page.screenshot({ path: path.join(OUT, 'frames', name), type: 'jpeg', quality: 92 });
      }
      return name;
    } catch (e) {
      if (k >= 30 || !/captureScreenshot|navigat|Execution context/i.test(e.message)) throw e;
      await new Promise((r) => setTimeout(r, 300));
    }
  }
}
function ev(e) {
  if (e.at) e.at = dip(e.at);
  if (e.from) e.from = dip(e.from);
  if (e.to) e.to = dip(e.to);
  steps.push(e);
  fs.appendFileSync(path.join(OUT, 'events.jsonl'), JSON.stringify({ beat: beatId, t: Date.now() - T0, ...e }) + '\n');
}
async function still(dt = 0) { ev({ k: 'still', img: await snap(), dt }); }
// frames over real time, e.g. a menu opening or the terminal streaming
async function settle(timesMs) {
  let prev = 0;
  for (const t of timesMs) { await page.waitForTimeout(t - prev); prev = t; await still(t / 1000); }
}
async function boxOf(locator, timeout = 15000) {
  await locator.waitFor({ state: 'visible', timeout });
  await locator.scrollIntoViewIfNeeded().catch(() => {});
  const b = await locator.boundingBox();
  if (!b) throw new Error('no box');
  return b;
}
async function glideTo(x, y, label) {
  ev({ k: 'glide', from: cursor, to: [x, y], label });
  cursor = [x, y];
  await page.mouse.move(x, y);
  // With Electron's zoom factor the mouse sometimes works in window points and sometimes in CSS px
  // (seen in Studio 1.7.6 at zoom 1.25). Ask the page where the pointer really is and correct once.
  if (surface === 'app' && Z !== 1) {
    const got = await page.evaluate(() => {
      if (!window.__recMM) { window.__recMM = [null, null]; addEventListener('mousemove', (e) => { window.__recMM = [e.clientX, e.clientY]; }, true); return null; }
      return window.__recMM;
    }).catch(() => null);
    let at = got;
    if (!at) { await page.mouse.move(x + 1, y); await page.mouse.move(x, y); at = await page.evaluate(() => window.__recMM).catch(() => null); }
    if (at && at[0] !== null && (Math.abs(at[0] - x) > 2 || Math.abs(at[1] - y) > 2)) {
      const f = Math.max(x, y) === x ? x / Math.max(1, at[0]) : y / Math.max(1, at[1]);
      await page.mouse.move(x * f, y * f);
    }
  }
  await page.waitForTimeout(140);
  await still(); // hover state at arrival
}
async function pointAt(locator, label, { dx = 0.5, dy = 0.5, maxDx = 9999 } = {}) {
  const b = await boxOf(locator);
  const x = b.x + Math.min(b.width * dx, maxDx);
  const y = b.y + b.height * dy;
  await glideTo(Math.round(x), Math.round(y), label);
  return { x, y, b };
}
async function click(locator, label, { button = 'left', settleMs = [150, 450], ...opt } = {}) {
  let { x, y, b } = await pointAt(locator, label, opt);
  // the page can still be settling (a banner, a list loading): if the target moved during the glide, follow it
  for (let i = 0; i < 3; i++) {
    const nb = await locator.boundingBox().catch(() => null);
    if (!nb || (Math.abs(nb.y - b.y) < 4 && Math.abs(nb.x - b.x) < 4)) break;
    await page.waitForTimeout(400);
    ({ x, y, b } = await pointAt(locator, label, opt));
  }
  await page.mouse.down({ button });
  await page.waitForTimeout(60);
  await page.mouse.up({ button });
  ev({ k: 'press', at: [x, y], button, label });
  await settle(settleMs);
}
async function typeKeys(text, label, perChar = true) {
  const imgs = [];
  for (const ch of text) {
    if (ch === '\n') await page.keyboard.press('Enter'); else await page.keyboard.insertText(ch);
    if (perChar) imgs.push(await snap());
  }
  ev({ k: 'type', imgs, chars: text.length, label });
}

// ---- tree helpers (Studio's explorer exposes treeitem roles with levels) ----
function treeItem(name, level) {
  // file rows start with an icon glyph, so match the name at the end after whitespace
  // git status badges (e.g. "+ U", "M") can follow the name
  return page.getByRole('treeitem', { name: new RegExp(`(^|\\s)${esc(name)}(\\s+\\+?\\s*[A-Z]{1,2})?$`), level });
}
async function isVisible(loc) { return (await loc.count()) > 0 && (await loc.first().isVisible()); }
async function openPath(rel, { open = true } = {}) {
  const parts = rel.split('/');
  for (let i = 0; i < parts.length; i++) {
    const item = treeItem(parts[i], i + 2).first();
    const last = i === parts.length - 1;
    if (!last) {
      const child = treeItem(parts[i + 1], i + 3);
      if (await isVisible(child)) continue; // already expanded
      await click(item, `expand ${parts[i]}`, { dx: 0.3, maxDx: 140 });
    } else if (open) {
      await click(item, `open ${rel}`, { dx: 0.3, maxDx: 160, settleMs: [200, 700] });
    }
  }
}

// ---- actions from lesson.yaml ----
const ACTIONS = {
  async open_project(name) {
    await click(page.getByRole('button', { name: new RegExp(esc(name)) }).first(), `open project ${name}`, { dx: 0.15, settleMs: [300, 900, 1800, 3000] });
    await sizeWindow(app, page);
    await applyUiZoom(UIZ);
  },
  async open_file(rel) { await openPath(rel); },
  async new_file({ folder, name }) {
    await openPath(folder, { open: false }); // make sure the folder row is visible
    const parts = folder.split('/');
    await click(treeItem(parts[parts.length - 1], parts.length + 1).first(), `right-click ${folder}`, { button: 'right', dx: 0.3, maxDx: 140, settleMs: [150, 400] });
    await click(page.getByRole('menuitem', { name: 'New File' }), 'New File', { settleMs: [200, 500] });
    await click(page.getByRole('textbox', { name: /file name/i }).first(), 'file name field', { dx: 0.25, settleMs: [150] });
    await typeKeys(name, 'file name');
    await click(page.getByRole('button', { name: 'Save', exact: true }).last(), 'Save new file', { settleMs: [250, 700, 1300] });
    const openTab = page.locator('main').getByText(name, { exact: true }).first();
    if (!(await isVisible(openTab)) || (await page.locator('.monaco-editor:visible').count()) === 0) {
      await openPath(`${folder}/${name}`);
    }
    await attachEditor(page);
    await tameEditor(page);
  },
  async type(text) {
    await attachEditor(page);
    await tameEditor(page);
    await typeKeys(text.replace(/\n$/, '\n'), 'type in editor');
    const now = await editorText(page);
    log('editor length', now.length);
  },
  // Paste a long block into the editor in one go (plan D8: long YAML is pasted, short files are typed).
  async paste(arg) {
    const { text, end, replace } = typeof arg === 'string' ? { text: arg, end: false } : arg;
    await attachEditor(page);
    await tameEditor(page);
    if (end) await page.evaluate(() => { const ed = window.__recEditor; const m = ed.getModel(); const n = m.getLineCount(); ed.setPosition({ lineNumber: n, column: m.getLineMaxColumn(n) }); ed.revealLine(n); ed.focus(); });
    // inserted through the editor API, never the system clipboard
    await page.evaluate(({ t, replace }) => { const ed = window.__recEditor; const sel = replace ? ed.getModel().getFullModelRange() : ed.getSelection(); if (replace) ed.setSelection(sel); ed.executeEdits('paste', [{ range: sel, text: t, forceMoveMarkers: true }]); ed.pushUndoStop(); }, { t: text, replace });
    await page.waitForTimeout(300);
    await still();
  },
  async click_save() {
    await click(page.locator('main').getByRole('button', { name: 'Save', exact: true }).first(), 'Save', { settleMs: [200, 600] });
  },
  async project_menu(item) {
    await click(page.getByRole('button', { name: 'Project', exact: true }).locator('xpath=following-sibling::button[1]'), 'Project menu', { settleMs: [150, 400] });
    await click(page.getByRole('menuitem', { name: item, exact: true }).first(), `Project → ${item}`, { settleMs: [200] });
  },
  // The Model split button above an open model: arrow ▸ item (Run, Build Model, Test, Compile, Preview, ...).
  async model_menu(item) {
    await click(page.getByRole('button', { name: 'Model', exact: true }).locator('xpath=following-sibling::button[1]'), 'Model menu', { settleMs: [150, 400] });
    await click(page.getByRole('menuitem', { name: item, exact: true }).first(), `Model → ${item}`, { settleMs: [200] });
  },
  async wait_for(what) {
    if (what !== 'manifest' && what !== 'run') throw new Error('unknown wait_for ' + what);
    const man = path.join(seeded.projectDir, 'target', 'manifest.json');
    const imgs = []; const ts = []; const t0 = Date.now();
    let doneAt = null;
    while (Date.now() - t0 < 90000) {
      imgs.push(await snap()); ts.push((Date.now() - t0) / 1000);
      const toast = await isVisible(page.getByText(what === 'run' ? /dbt run completed successfully/i : /completed successfully/i));
      if ((what === 'run' ? toast : fs.existsSync(man)) && !doneAt) doneAt = Date.now();
      if (doneAt && (toast || Date.now() - doneAt > 4000)) break;
      await page.waitForTimeout(350);
    }
    for (let k = 0; k < 3; k++) { await page.waitForTimeout(400); imgs.push(await snap()); ts.push((Date.now() - t0) / 1000); }
    ev({ k: 'live', imgs, ts, label: 'compile output' });
  },
  async point({ editor_line }) {
    const line = page.locator('.monaco-editor:visible .view-lines .view-line').nth(editor_line - 1);
    // view-line elements are absolutely positioned; pick by their top order
    const tops = await page.locator('.monaco-editor:visible .view-lines .view-line').evaluateAll((els) => els.map((e) => [parseFloat(e.style.top), e.getBoundingClientRect().x, e.getBoundingClientRect().y, e.getBoundingClientRect().height, e.innerText.length]));
    tops.sort((a, b) => a[0] - b[0]);
    const [, x, y, h, len] = tops[editor_line - 1];
    const textW = Math.min(len * 9.6, 520);
    await glideTo(Math.round(x + textW * 0.55), Math.round(y + h * 0.75), `point line ${editor_line}`);
  },
  async close_tab(rel) {
    // each editor tab is labelled with the file's full path and holds a close button
    const tab = page.locator(`main [aria-label="${path.join(seeded.projectDir, rel)}"]`).first();
    await click(tab.locator('button').first(), `close tab ${rel}`, { settleMs: [200, 700, 1500] });
  },
  async bottom_tab(label) {
    const tab = page.getByText(label, { exact: true }).first();
    const t0 = Date.now();
    while (!(await isVisible(tab)) && Date.now() - t0 < 12000) await page.waitForTimeout(400);
    if (!(await isVisible(tab))) throw new Error(`${label} tab did not appear`);
    await click(tab, `${label} tab`, { settleMs: [300, 900, 1800, 2800] });
  },
  async lineage_depth(n) {
    // the panel and the Maximize dialog each have their own Depth select; use the dialog when it is open
    const root = (await page.getByRole('dialog').count()) ? page.getByRole('dialog').last() : page;
    const lb = await boxOf(root.getByText('Depth', { exact: true }).first());
    let target = null;
    for (const c of await root.getByRole('combobox').all()) { const b = await c.boundingBox(); if (b && Math.abs(b.y + b.height / 2 - (lb.y + lb.height / 2)) < 20 && b.x > lb.x) { target = c; break; } }
    if (!target) throw new Error('depth select not found');
    await click(target, 'Depth select', { settleMs: [200, 500] });
    await click(page.getByRole('option', { name: String(n), exact: true }), `Depth ${n}`, { settleMs: [300, 900, 1800, 2800] });
  },
  async lineage_maximize() {
    await click(page.getByRole('button', { name: 'Maximize' }).first(), 'Maximize lineage', { settleMs: [300, 900, 1800] });
  },
  async lineage_fit() {
    const root = (await page.getByRole('dialog').count()) ? page.getByRole('dialog').last() : page;
    const fit = root.locator('.react-flow__controls-fitview').first();
    if (await fit.count()) await click(fit, 'fit view', { settleMs: [300, 900, 1600] });
  },
  async new_folder({ parent, name }) {
    await openPath(parent, { open: false });
    const parts = parent.split('/');
    await click(treeItem(parts[parts.length - 1], parts.length + 1).first(), `right-click ${parent}`, { button: 'right', dx: 0.3, maxDx: 140, settleMs: [150, 400] });
    await click(page.getByRole('menuitem', { name: 'New Folder' }), 'New Folder', { settleMs: [200, 500] });
    await click(page.getByRole('dialog').getByRole('textbox').first(), 'folder name field', { dx: 0.25, settleMs: [150] });
    await typeKeys(name, 'folder name');
    await click(page.getByRole('dialog').getByRole('button', { name: 'Save', exact: true }).first(), 'Save new folder', { settleMs: [250, 700, 1300] });
    if (!fs.existsSync(path.join(seeded.projectDir, parent, name))) throw new Error('folder not created: ' + name);
    if (!(await isVisible(treeItem(name, parent.split('/').length + 2).first()))) { await page.waitForTimeout(1500); await ACTIONS.expand(parent).catch(() => {}); }
    await ACTIONS.ensure_tree({ name, level: parent.split('/').length + 2 });
  },
  // Type at a line: at its end, or `back` characters before the end (e.g. 1 = before a closing bracket).
  async insert_at({ line, text, back = 0 }) {
    await attachEditor(page);
    await tameEditor(page);
    await page.evaluate(({ line, back }) => { const ed = window.__recEditor; const m = ed.getModel(); ed.setPosition({ lineNumber: line, column: m.getLineMaxColumn(line) - back }); ed.revealLineInCenter(line); ed.focus(); }, { line, back });
    await page.waitForTimeout(200);
    await still();
    await typeKeys(text, `type at line ${line}`);
  },
  async type_start(text) {
    await attachEditor(page);
    await tameEditor(page);
    await page.evaluate(() => { const ed = window.__recEditor; ed.setPosition({ lineNumber: 1, column: 1 }); ed.revealLine(1); ed.focus(); });
    await page.waitForTimeout(200);
    await still();
    await typeKeys(text, 'type at start of file');
  },
  async type_end(text) {
    await attachEditor(page);
    await tameEditor(page);
    await page.evaluate(() => { const ed = window.__recEditor; const m = ed.getModel(); const n = m.getLineCount(); ed.setPosition({ lineNumber: n, column: m.getLineMaxColumn(n) }); ed.revealLine(n); ed.focus(); });
    await page.waitForTimeout(200);
    await still();
    await typeKeys(text, 'type at end of file');
  },
  async nav(label) {
    await click(page.getByRole('link', { name: label, exact: true }).first(), `nav ${label}`, { settleMs: [300, 900, 1800, 2600] });
  },
  async sql_connection(name) {
    await click(page.getByRole('combobox').first(), 'connection select', { settleMs: [200, 500] });
    await click(page.getByRole('option', { name, exact: true }).first(), `connection ${name}`, { settleMs: [400, 1200, 2400, 3400] });
  },
  async sql_run(arg) {
    // the green run arrow sits in the gutter, 74 px left of a statement's line (scroll a long line back first)
    const line = (arg && arg.line) || 1;
    await page.evaluate(() => { const ed = window.__recEditor; if (ed) { ed.setScrollLeft(0); ed.setPosition({ lineNumber: 1, column: 1 }); } });
    await page.waitForTimeout(300);
    const rows = await page.locator('.monaco-editor:visible .view-lines .view-line').evaluateAll((els) => els.map((e) => { const r = e.getBoundingClientRect(); return [parseFloat(e.style.top), r.x, r.y, r.height]; }));
    rows.sort((a, b) => a[0] - b[0]);
    const [, bx, by, bh] = rows[line - 1];
    const x = Math.round(bx - 74), y = Math.round(by + bh / 2);
    await glideTo(x, y, 'run arrow');
    await page.mouse.down(); await page.waitForTimeout(60); await page.mouse.up();
    ev({ k: 'press', at: [x, y], button: 'left', label: `run query line ${line}` });
    await settle((arg && arg.settleMs) || [300, 900, 1800, 3000]);
  },
  async point_tree(rel) {
    const parts = rel.split('/');
    await pointAt(treeItem(parts[parts.length - 1], parts.length + 1).first(), `point ${rel}`, { dx: 0.3, maxDx: 140 });
  },
  // Off-camera check: the saved file equals the lesson's snippet (path relative to the lesson folder).
  async expect_file({ path: rel, snippet }) {
    const got = fs.readFileSync(path.join(seeded.projectDir, rel), 'utf8');
    const want = fs.readFileSync(path.resolve(lessonDir, snippet), 'utf8');
    if (got !== want) throw new Error(`${rel} differs from ${snippet} (${got.length} vs ${want.length} chars)`);
    log('  file matches snippet', rel);
  },
  // Type a command into the box under the terminal, press Enter, and capture the output live.
  async terminal({ cmd, until, timeoutMs = 90000 }) {
    const box = page.getByRole('textbox', { name: 'Type a rosetta or dbt command...' });
    await click(box, 'terminal command box', { dx: 0.2, settleMs: [150] });
    await typeKeys(cmd, 'terminal command');
    await page.keyboard.press('Enter');
    const imgs = []; const ts = []; const t0 = Date.now();
    let seenAt = null;
    while (Date.now() - t0 < timeoutMs) {
      imgs.push(await snap()); ts.push((Date.now() - t0) / 1000);
      if (!seenAt && (await page.getByText(until).count())) seenAt = Date.now();
      if (seenAt && Date.now() - seenAt > 1800) break;
      await page.waitForTimeout(350);
    }
    if (!seenAt) throw new Error(`terminal output "${until}" did not appear`);
    ev({ k: 'live', imgs, ts, label: `terminal: ${cmd}` });
  },
  async git_tab() {
    await click(page.getByRole('tab', { name: /\bGit$/ }).first(), 'Git tab', { settleMs: [200, 700, 1400] });
  },
  async explorer_tab() {
    await click(page.getByRole('tab', { name: 'Explorer' }).first(), 'Explorer tab', { settleMs: [200, 700] });
  },
  // Hover the changed file, then click its "Stage Changes" (+) button, which only shows on hover.
  async git_stage(name) {
    // the file name also shows in the editor tab and breadcrumb: use the match inside the sidebar (x < 380)
    let rb = null;
    for (const m of await page.getByText(name, { exact: true }).all()) {
      const b = await m.boundingBox();
      if (b && b.x < 380 && b.width > 0) { rb = b; break; }
    }
    if (!rb) throw new Error(`${name} not found in the Git panel`);
    await glideTo(Math.round(rb.x + rb.width / 2), Math.round(rb.y + rb.height / 2), `hover ${name}`);
    await page.waitForTimeout(250);
    await still();
    let target = null;
    for (const ic of await page.locator('svg[data-testid="AddIcon"]').all()) {
      const b = await ic.boundingBox();
      if (b && Math.abs(b.y + b.height / 2 - (rb.y + rb.height / 2)) < 14 && b.x > rb.x) { target = ic.locator('xpath=ancestor::button[1]'); break; }
    }
    if (!target) throw new Error('stage button not found for ' + name);
    await click(target, `Stage ${name}`, { settleMs: [250, 700, 1300] });
  },
  async git_message(text) {
    await click(page.locator('[contenteditable="true"][data-placeholder^="Message"]').first(), 'commit message box', { dx: 0.3, settleMs: [150] });
    await typeKeys(text, 'commit message');
  },
  // ---- generic actions (both surfaces) ----
  // Wait for a long query in the SQL Editor: Studio shows a Stop Query button while it runs.
  async sql_wait(arg) {
    const { timeoutMs = 1200000, everyMs = 3000 } = arg || {};
    await page.waitForTimeout(700);
    const t0 = Date.now(); let n = 0;
    while (await page.getByRole('button', { name: 'Stop Query' }).count()) {
      if (Date.now() - t0 > timeoutMs) throw new Error('query still running after ' + timeoutMs + ' ms');
      await page.waitForTimeout(everyMs);
      if (n++ % 4 === 0) await still((Date.now() - t0) / 1000);
    }
    log('  query finished after', ((Date.now() - t0) / 1000).toFixed(1), 's');
    await page.waitForTimeout(900);
    await still();
  },
  async click_at(spec) {
    // closes: true = the click closes this window (e.g. setup Finish), so take no frames after it
    await click(loc(spec), `click ${specLabel(spec)}`, { dx: spec.dx ?? 0.5, settleMs: spec.closes ? [] : spec.settleMs || [200, 600] });
  },
  async point_at(spec) {
    await pointAt(loc(spec), `point ${specLabel(spec)}`, { dx: spec.dx ?? 0.5 });
    await page.waitForTimeout(spec.hold || 250);
    await still();
  },
  async check(names) {
    for (const n of [].concat(names)) {
      const c = page.getByRole('checkbox', { name: n, exact: true });
      if (!(await c.isChecked())) await click(c, `check ${n}`, { settleMs: [150] });
    }
  },
  async uncheck(names) {
    for (const n of [].concat(names)) {
      const c = page.getByRole('checkbox', { name: n, exact: true });
      if (await c.isChecked()) await click(c, `uncheck ${n}`, { settleMs: [150] });
    }
  },
  // Live frames until a control becomes enabled (e.g. the setup's Finish button); compose speeds it up.
  async wait_enabled({ role = 'button', name, timeoutMs = 600000, everyMs = 1500 }) {
    const target = page.getByRole(role, { name, exact: true });
    const imgs = []; const ts = []; const t0 = Date.now();
    while (Date.now() - t0 < timeoutMs) {
      imgs.push(await snap()); ts.push((Date.now() - t0) / 1000);
      if (await target.isEnabled().catch(() => false)) break;
      await page.waitForTimeout(everyMs);
    }
    if (!(await target.isEnabled().catch(() => false))) throw new Error(`${name} never became enabled`);
    log(`  ${name} enabled after ${((Date.now() - t0) / 1000).toFixed(1)}s`);
    await page.waitForTimeout(500); imgs.push(await snap()); ts.push((Date.now() - t0) / 1000);
    ev({ k: 'live', imgs, ts, label: `wait for ${name}`, wait: true, real_s: (Date.now() - t0) / 1000 });
  },
  // The setup window closes on Finish. Studio 1.7.6 then restarts itself (app.relaunch), which detaches it
  // from Playwright, so stop the detached copy and start Studio again on the same, now set-up, profile.
  async follow_window() {
    const old = page; const t0 = Date.now();
    let next = null;
    while (!next && Date.now() - t0 < 8000) {
      for (const w of app.windows()) if (w !== old && !w.isClosed() && /#\/?app/.test(w.url())) next = w;
      if (!next) await new Promise((r) => setTimeout(r, 300));
    }
    if (!next) {
      await new Promise((r) => setTimeout(r, 3000));
      const ps = execFileSync('ps', ['-axo', 'pid=,command=']).toString().split('\n');
      for (const line of ps) {
        if (line.includes('/Contents/MacOS/Rosetta DBT Studio ') && line.includes(`--user-data-dir=${seeded.userData}`)) {
          const pid = Number(line.trim().split(/\s+/)[0]);
          try { process.kill(pid); log('  stopped the self-relaunched Studio', pid); } catch (e) {}
        }
      }
      await new Promise((r) => setTimeout(r, 1500));
      app = await launchStudio(LAUNCH);
      app.process().stderr.on('data', (d) => fs.appendFileSync(path.join(OUT, 'electron-stderr.log'), d));
      ({ page: next } = await mainWindow(app, 150000));
      log('  relaunched Studio');
    }
    page = studioPage = next;
    await page.waitForTimeout(2500);
    await sizeWindow(app, page);
    await applyUiZoom(UIZ);
    await page.waitForTimeout(1500);
    await still();
  },
  // Click a field and type into it, one frame per character.
  async type_text(spec) {
    await click(loc(spec), `field ${specLabel(spec)}`, { dx: spec.dx ?? 0.2, settleMs: [150] });
    if (spec.replace) { await page.keyboard.press('Meta+A'); await page.keyboard.press('Backspace'); await page.waitForTimeout(120); } // field has a default value
    await typeKeys(spec.text, `type ${specLabel(spec)}`);
  },
  // Wait (e.g. a page load or a server check), then take one frame.
  async pause(ms) {
    await page.waitForTimeout(ms);
    await still();
  },
  // New file in the project root (right-click the root row, level 1).
  async new_root_file(name) {
    const root = page.getByRole('treeitem', { level: 1 }).first();
    await click(root, 'right-click project root', { button: 'right', dx: 0.15, maxDx: 120, settleMs: [150, 400] });
    await click(page.getByRole('menuitem', { name: 'New File' }), 'New File', { settleMs: [200, 500] });
    await click(page.getByRole('textbox', { name: /file name/i }).first(), 'file name field', { dx: 0.25, settleMs: [150] });
    await typeKeys(name, 'file name');
    await click(page.getByRole('button', { name: 'Save', exact: true }).last(), 'Save new file', { settleMs: [250, 700, 1300] });
    if ((await page.locator('.monaco-editor:visible').count()) === 0) await openPath(name);
    await attachEditor(page);
    await tameEditor(page);
  },
  // Live frames until a text appears (terminal output, toasts); 'gone' waits for it to disappear instead.
  async wait_text({ text, regex, timeoutMs = 120000, everyMs = 700, label }) {
    const t = page.getByText(regex ? new RegExp(text) : text).first();
    const imgs = []; const ts = []; const t0 = Date.now();
    while (Date.now() - t0 < timeoutMs) {
      imgs.push(await snap()); ts.push((Date.now() - t0) / 1000);
      if ((await t.count()) && (await t.isVisible().catch(() => false))) break;
      await page.waitForTimeout(everyMs);
    }
    if (!(await t.count())) throw new Error(`text "${text}" did not appear`);
    for (let k = 0; k < 2; k++) { await page.waitForTimeout(500); imgs.push(await snap()); ts.push((Date.now() - t0) / 1000); }
    ev({ k: 'live', imgs, ts, label: label || `wait for ${text}` });
  },
  async git_init() {
    await click(page.getByRole('button', { name: 'Initialize Repository' }), 'Initialize Repository', { settleMs: [300, 1000, 2000, 3000] });
  },
  async git_stage_all() {
    // the "Stage All Changes" (+) button sits in the CHANGES header and shows on hover
    const hdr = page.getByText('Changes', { exact: true }).last();
    const hb = await boxOf(hdr);
    await glideTo(Math.round(hb.x + hb.width / 2), Math.round(hb.y + hb.height / 2), 'hover Changes');
    await page.waitForTimeout(250);
    let target = null;
    for (const ic of await page.locator('svg[data-testid="AddIcon"]').all()) {
      const b = await ic.boundingBox();
      if (b && Math.abs(b.y + b.height / 2 - (hb.y + hb.height / 2)) < 14) { target = ic.locator('xpath=ancestor::button[1]'); break; }
    }
    if (!target) throw new Error('Stage All Changes button not found');
    await click(target, 'Stage All Changes', { settleMs: [250, 800, 1500] });
  },
  // Publish Branch: with no remote, Studio asks for one ("Add git remote"); paste the URL, add it, and the push runs.
  async publish_branch({ url }) {
    await click(page.getByRole('button', { name: /Publish Branch/ }).first(), 'Publish Branch', { settleMs: [300, 900] });
    const dlg = page.getByRole('dialog').last();
    if (await dlg.count()) {
      await click(dlg.getByRole('textbox').first(), 'remote URL field', { dx: 0.3, settleMs: [150] });
      await typeKeys(url, 'remote URL');
      const add = dlg.getByRole('button', { name: /Add|Save|Connect/ }).last();
      await click(add, 'Add remote', { settleMs: [400, 1200, 2500] });
      if (await page.getByRole('button', { name: /Publish Branch/ }).count()) {
        await click(page.getByRole('button', { name: /Publish Branch/ }).first(), 'Publish Branch', { settleMs: [400, 1200, 2500, 4000] });
      }
    }
  },
  // Off camera: copy files into the project (e.g. the downloaded data); from is relative to the lesson folder.
  async copy_in({ from, to, settleMs = 2500 }) {
    const src = path.resolve(lessonDir, from);
    const dst = path.join(seeded.projectDir, to);
    if (fs.statSync(src).isDirectory()) {
      fs.mkdirSync(dst, { recursive: true });
      for (const f of fs.readdirSync(src)) fs.copyFileSync(path.join(src, f), path.join(dst, f));
    } else { fs.mkdirSync(path.dirname(dst), { recursive: true }); fs.copyFileSync(src, dst); }
    log('  copied in', from, '→', to);
    await page.waitForTimeout(settleMs);
  },
  // Expand every folder on a path (clicks only the collapsed ones).
  async expand(rel) {
    const parts = rel.split('/');
    for (let i = 0; i < parts.length; i++) {
      const item = treeItem(parts[i], i + 2).first();
      if ((await item.getAttribute('aria-expanded')) !== 'true') await click(item, `expand ${parts[i]}`, { dx: 0.3, maxDx: 140, settleMs: [200, 600] });
    }
  },
  // After creating a folder: wait for its row; if the tree did not redraw, use the Explorer's refresh button.
  async ensure_tree({ name, level }) {
    for (let k = 0; k < 2; k++) {
      const t0 = Date.now();
      while (Date.now() - t0 < 5000) { if (await isVisible(treeItem(name, level).first())) return; await page.waitForTimeout(300); }
      await ACTIONS.refresh_explorer();
    }
    if (!(await isVisible(treeItem(name, level).first()))) throw new Error('tree row not shown: ' + name);
  },
  // The Explorer's refresh button (right of the file search box): shows files added outside Studio.
  async refresh_explorer() {
    // the icon has no accessible name; it sits about 20 px right of the search box, centred on it
    const b = await boxOf(page.getByRole('textbox', { name: 'Search files or folders...' }));
    const x = Math.round(b.x + b.width + 20), y = Math.round(b.y + b.height / 2);
    await glideTo(x, y, 'refresh Explorer');
    await page.mouse.down(); await page.waitForTimeout(60); await page.mouse.up();
    ev({ k: 'press', at: [x, y], button: 'left', label: 'refresh Explorer' });
    await settle([300, 900, 1600]);
  },
  // New folder in the project root (right-click the root row, level 1).
  async new_root_folder(name) {
    const root = page.getByRole('treeitem', { level: 1 }).first();
    await click(root, 'right-click project root', { button: 'right', dx: 0.15, maxDx: 120, settleMs: [150, 400] });
    await click(page.getByRole('menuitem', { name: 'New Folder' }), 'New Folder', { settleMs: [200, 500] });
    await click(page.getByRole('dialog').getByRole('textbox').first(), 'folder name field', { dx: 0.25, settleMs: [150] });
    await typeKeys(name, 'folder name');
    await click(page.getByRole('dialog').getByRole('button', { name: 'Save', exact: true }).first(), 'Save new folder', { settleMs: [250, 700, 1300] });
    if (!fs.existsSync(path.join(seeded.projectDir, name))) throw new Error('folder not created: ' + name);
    await ACTIONS.ensure_tree({ name, level: 2 });
  },
  // Push the new commit to the tracked branch; checks that origin/main moved.
  async git_push({ name = '^(Push|Sync Changes)' } = {}) {
    const head = () => execFileSync('git', ['rev-parse', 'HEAD'], { cwd: seeded.projectDir }).toString().trim();
    const remote = () => execFileSync('git', ['ls-remote', 'origin', 'refs/heads/main'], { cwd: seeded.projectDir, env: { ...process.env, HOME, GIT_CONFIG_NOSYSTEM: '1' }, stdio: 'pipe' }).toString().split(/\s/)[0];
    await click(page.getByRole('button', { name: new RegExp(name) }).first(), 'Push', { settleMs: [400, 1200, 2500, 4000] });
    let ok = false;
    for (let k = 0; k < 20 && !ok; k++) { ok = remote() === head(); if (!ok) await page.waitForTimeout(1000); }
    if (!ok) throw new Error('push did not reach origin/main');
    await still();
    log('  pushed', head().slice(0, 7));
  },
  // Scroll the widest scrollable area of the open dialog to its right edge (e.g. a preview table), as a short clip.
  async dialog_scroll_right({ frames = 14 } = {}) {
    const max = await page.evaluate(() => {
      const d = [...document.querySelectorAll('[role=dialog]')].pop();
      const els = [...d.querySelectorAll('*')].filter((e) => e.scrollWidth > e.clientWidth + 20 && getComputedStyle(e).overflowX !== 'visible');
      els.sort((x, y) => (y.scrollWidth - y.clientWidth) - (x.scrollWidth - x.clientWidth));
      window.__recScroller = els[0];
      return els[0] ? els[0].scrollWidth - els[0].clientWidth : 0;
    });
    if (!max) throw new Error('nothing to scroll in the dialog');
    await still();
    const imgs = []; const ts = [];
    for (let i = 1; i <= frames; i++) {
      const u = i / frames; const e = u < 0.5 ? 4 * u * u * u : 1 - Math.pow(-2 * u + 2, 3) / 2;
      await page.evaluate((x) => { window.__recScroller.scrollLeft = x; }, max * e);
      await page.waitForTimeout(50);
      imgs.push(await snap()); ts.push(i * 0.09);
    }
    ev({ k: 'live', imgs, ts, label: 'scroll dialog right' });
  },
  // Change Studio's zoom for the following beats (e.g. 1.75 for a dense dialog), like pressing Cmd +.
  async ui_zoom(z) { await applyUiZoom(z === 'default' ? UIZ : Number(z)); await still(); },
  async press_keys(keys) {
    await page.keyboard.press(keys);
    await page.waitForTimeout(150);
    await still();
  },
  // Type at the current focus (no click first).
  async type_keys(text) {
    await typeKeys(text, 'type');
  },
  // ---- browser actions ----
  async goto(url) {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await page.waitForTimeout(3500);
    await still();
  },
  // Smooth scroll so the target sits at `at` (fraction of the viewport height); frames become a short live clip.
  async scroll_to(spec) {
    const b = await boxOf(loc(spec));
    const y0 = await page.evaluate(() => window.scrollY);
    const y1 = Math.max(0, y0 + b.y - 1080 * (spec.at ?? 0.3));
    const n = spec.frames || 14; const imgs = []; const ts = [];
    for (let i = 1; i <= n; i++) {
      const u = i / n; const e = u < 0.5 ? 4 * u * u * u : 1 - Math.pow(-2 * u + 2, 3) / 2;
      await page.evaluate((y) => window.scrollTo(0, y), y0 + (y1 - y0) * e);
      await page.waitForTimeout(40);
      imgs.push(await snap()); ts.push(i * 0.07);
    }
    ev({ k: 'live', imgs, ts, label: `scroll to ${specLabel(spec)}` });
  },
  // Click a download link; the download starts for real, then is cancelled unless keep: true.
  async click_download(spec) {
    const dl = page.waitForEvent('download', { timeout: 30000 });
    await click(loc(spec), `download ${specLabel(spec)}`, { settleMs: [200, 700] });
    const d = await dl;
    log('  download started', d.suggestedFilename());
    if (!spec.keep) await d.cancel();
  },
  async git_commit() {
    const count = () => { try { return execFileSync('git', ['rev-list', '--count', 'HEAD'], { cwd: seeded.projectDir, stdio: 'pipe' }).toString().trim(); } catch (e) { return '0'; } };
    const before = count();
    // the label shows the staged count once something is staged, e.g. "Commit (1)"
    await click(page.getByRole('button', { name: /^Commit( \(\d+\))?$/ }).first(), 'Commit', { settleMs: [300, 900, 1800, 2800] });
    const after = count();
    if (after === before) throw new Error('commit did not land');
    log('  commit', execFileSync('git', ['log', '--oneline', '-1'], { cwd: seeded.projectDir }).toString().trim());
  },
};

(async () => {
  // Studio is launched only when the lesson has app scenes (a browser-only lesson needs no start state)
  const needsApp = lesson.scenes.some((sc) => sc.kind === 'app');
  let initial = null;
  if (needsApp) {
    seeded = seedProfile({ stateDir: path.join(courseDir, 'states', lesson.start_state), home: HOME, dbtEnv: path.join(T, '.cache', 'dbt-env'), python: path.join(T, '.cache', 'dbt-env', 'bin', 'python'), mac: MAC, projectsDir: course.projects_dir });
    LAUNCH = { appBin: APP_BIN, home: HOME, userData: seeded.userData, scale: 2, theme: course.theme, mac: MAC };
    app = await launchStudio(LAUNCH);
    app.process().stderr.on('data', (d) => fs.appendFileSync(path.join(OUT, 'electron-stderr.log'), d));
    app.process().stdout.on('data', (d) => fs.appendFileSync(path.join(OUT, 'electron-stderr.log'), d));
    app.process().on('exit', (code, sig) => log('electron exited', code, sig));
    ({ page } = await mainWindow(app, 150000));
    studioPage = page;
    await page.waitForTimeout(3000);
    await sizeWindow(app, page);
    await applyUiZoom(UIZ);
    cursor = cursors.app = [Math.round(1180 / UIZ), Math.round(640 / UIZ)];
    await page.mouse.move(cursor[0], cursor[1]);
    await page.waitForTimeout(2500);
    initial = await snap();
  }
  let failed = null;
  let firstRecorded = true;
  for (const sc of lesson.scenes) {
    if (sc.kind !== 'app' && sc.kind !== 'browser') continue;
    // switch surface, keeping each surface's cursor where it was
    cursors[surface] = cursor;
    surface = sc.kind;
    page = surface === 'browser' ? await getBrowserPage() : studioPage;
    Z = surface === 'browser' ? BZ : UIZ;
    if (surface === 'browser' && !cursors.browserScaled) { cursors.browser = [Math.round(960 / BZ), Math.round(300 / BZ)]; cursors.browserScaled = true; }
    cursor = cursors[surface];
    if (surface === 'browser') await page.mouse.move(cursor[0], cursor[1]);
    for (const b of sc.beats) {
      beatId = b.id; steps = [];
      if (firstRecorded && surface === 'app') ev({ k: 'still', img: initial, dt: 0 });
      firstRecorded = false;
      log('beat', b.id);
      try {
        for (const a of b.actions || []) {
          const [k, v] = typeof a === 'string' ? [a, undefined] : Object.entries(a)[0];
          if (!ACTIONS[k]) throw new Error('unknown action ' + k);
          log('  action', k);
          await ACTIONS[k](v);
        }
        if (!(b.actions || []).length) await still(); // a beat without actions holds the current screen
      } catch (e) {
        log('FAILED in', b.id, e.message.split('\n')[0]);
        await still().catch(() => {});
        failed = { beat: b.id, error: e.message.split('\n')[0] };
      }
      beats[b.id] = { steps, cursorEnd: dip(cursor) };
      if (failed) break;
    }
    if (failed) break;
  }
  const versions = studioPage && await studioPage.evaluate(() => document.body.innerText.match(/dbt:\s*[\d.]+|Python:\s*[\d.]+|v\d+\.\d+\.\d+/g)).catch(() => null);
  fs.writeFileSync(path.join(OUT, 'events.json'), JSON.stringify({ size: [1920, 1080], scale: 2, uiZoom: UIZ, browserZoom: BZ, initialCursor: [1180, 640], beats, failed, versions, frames: nFrame }, null, 1));
  log('frames', nFrame, failed ? 'FAILED ' + JSON.stringify(failed) : 'ok', versions);
  if (browser) await browser.close().catch(() => {});
  if (app) await app.close().catch(() => {});
  // Serve Docs leaves a dbt docs server running after Studio closes: stop the learner's copies
  for (const line of execFileSync('ps', ['-axo', 'pid=,command=']).toString().split('\n')) {
    if (line.includes('rosetta-dbt-studio/venv/bin/dbt') && line.includes('docs serve') && line.includes(HOME)) {
      try { process.kill(Number(line.trim().split(/\s+/)[0])); log('stopped dbt docs serve'); } catch (e) {}
    }
  }
  process.exit(failed ? 2 : 0);
})().catch((e) => { console.error('FATAL', e); process.exit(1); });
