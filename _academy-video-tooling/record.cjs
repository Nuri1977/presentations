// Record the app scenes of a lesson as 4K stills after every visible change, plus an event list.
//   node record.cjs <course_dir> <lesson_dir>
// Output: <lesson_dir>/render/app/{frames/*.jpg, events.json, events.jsonl}
// The renderer (scripts/compose.py) turns events into a timeline paced to the voice.
const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');
const { seedProfile, launchStudio, mainWindow, sizeWindow } = require('./lib/studio.cjs');
const { attachEditor, tameEditor, editorText } = require('./lib/actions.cjs');

const T = path.resolve(__dirname);
const [courseDir, lessonDir] = process.argv.slice(2).map((p) => path.resolve(p));
const course = yaml.load(fs.readFileSync(path.join(courseDir, 'course.yaml'), 'utf8'));
const lesson = yaml.load(fs.readFileSync(path.join(lessonDir, 'lesson.yaml'), 'utf8'));
const OUT = path.join(lessonDir, 'render', 'app');
fs.rmSync(OUT, { recursive: true, force: true });
fs.mkdirSync(path.join(OUT, 'frames'), { recursive: true });
const HOME = '/home/learner';
const T0 = Date.now();
const log = (...a) => console.log(`[${((Date.now() - T0) / 1000).toFixed(1)}s]`, ...a);
const esc = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

let page, app, seeded;
let nFrame = 0;
let cursor = [1180, 640];
let steps = []; // steps of the current beat
let beatId = null;
const beats = {};

async function snap() {
  const name = `${String(nFrame++).padStart(5, '0')}.jpg`;
  await page.screenshot({ path: path.join(OUT, 'frames', name), type: 'jpeg', quality: 92 });
  return name;
}
function ev(e) {
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
  const b = await locator.boundingBox();
  if (!b) throw new Error('no box');
  return b;
}
async function glideTo(x, y, label) {
  ev({ k: 'glide', from: cursor, to: [x, y], label });
  cursor = [x, y];
  await page.mouse.move(x, y);
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
  const { x, y } = await pointAt(locator, label, opt);
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
  return page.getByRole('treeitem', { name: new RegExp(`(^|\\s)${esc(name)}$`), level });
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
  async click_save() {
    await click(page.locator('main').getByRole('button', { name: 'Save', exact: true }).first(), 'Save', { settleMs: [200, 600] });
  },
  async project_menu(item) {
    await click(page.getByRole('button', { name: 'Project', exact: true }).locator('xpath=following-sibling::button[1]'), 'Project menu', { settleMs: [150, 400] });
    await click(page.getByRole('menuitem', { name: item, exact: true }).first(), `Project → ${item}`, { settleMs: [200] });
  },
  async wait_for(what) {
    if (what !== 'manifest') throw new Error('unknown wait_for ' + what);
    const man = path.join(seeded.projectDir, 'target', 'manifest.json');
    const imgs = []; const ts = []; const t0 = Date.now();
    let doneAt = null;
    while (Date.now() - t0 < 90000) {
      imgs.push(await snap()); ts.push((Date.now() - t0) / 1000);
      const toast = await isVisible(page.getByText(/completed successfully/i));
      if (fs.existsSync(man) && !doneAt) doneAt = Date.now();
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
    const depthLabel = page.getByText('Depth', { exact: true }).first();
    const lb = await boxOf(depthLabel);
    const combos = await page.getByRole('combobox').all();
    let target = null;
    for (const c of combos) { const b = await c.boundingBox(); if (b && Math.abs(b.y + b.height / 2 - (lb.y + lb.height / 2)) < 20 && b.x > lb.x) { target = c; break; } }
    if (!target) throw new Error('depth select not found');
    await click(target, 'Depth select', { settleMs: [200, 500] });
    await click(page.getByRole('option', { name: String(n), exact: true }), `Depth ${n}`, { settleMs: [300, 900, 1800, 2800] });
  },
};

(async () => {
  seeded = seedProfile({ stateDir: path.join(courseDir, 'states', lesson.start_state), home: HOME, dbtEnv: path.join(T, '.cache', 'dbt-env'), python: path.join(T, '.cache', 'dbt-env', 'bin', 'python') });
  app = await launchStudio({ appBin: path.join(T, '.cache', 'app', `Rosetta-DBT-Studio-${course.app.version}-x64`, 'rosetta-dbt-studio'), home: HOME, userData: seeded.userData, scale: 2, theme: course.theme });
  app.process().stderr.on('data', (d) => fs.appendFileSync(path.join(OUT, 'electron-stderr.log'), d));
  ({ page } = await mainWindow(app));
  await page.waitForTimeout(3000);
  await sizeWindow(app, page);
  await page.mouse.move(cursor[0], cursor[1]);
  await page.waitForTimeout(2500);
  const initial = await snap();
  let failed = null;
  for (const sc of lesson.scenes) {
    if (sc.kind !== 'app') continue;
    for (const b of sc.beats) {
      beatId = b.id; steps = [];
      if (Object.keys(beats).length === 0) ev({ k: 'still', img: initial, dt: 0 });
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
        await still();
        failed = { beat: b.id, error: e.message.split('\n')[0] };
      }
      beats[b.id] = { steps, cursorEnd: cursor };
      if (failed) break;
    }
    if (failed) break;
  }
  const versions = await page.evaluate(() => document.body.innerText.match(/dbt:\s*[\d.]+|Python:\s*[\d.]+|v\d+\.\d+\.\d+/g));
  fs.writeFileSync(path.join(OUT, 'events.json'), JSON.stringify({ size: [1920, 1080], scale: 2, initialCursor: [1180, 640], beats, failed, versions, frames: nFrame }, null, 1));
  log('frames', nFrame, failed ? 'FAILED ' + JSON.stringify(failed) : 'ok', versions);
  await app.close();
  process.exit(failed ? 2 : 0);
})().catch((e) => { console.error('FATAL', e); process.exit(1); });
