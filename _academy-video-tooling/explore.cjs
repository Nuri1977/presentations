// Explore the real app before writing a lesson: seed a start state, launch the pinned release,
// run a small steps file, and save screenshots + ARIA snapshots for each step.
//   node explore.cjs <course_dir> <state_name> <steps.cjs> [out_dir]
// steps.cjs: module.exports = async ({ page, app, shot, aria, seeded, log }) => { ... }
const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');
const { seedProfile, launchStudio, mainWindow, sizeWindow } = require('./lib/studio.cjs');

const T = path.resolve(__dirname);
const [courseDir, stateName, stepsFile, outArg] = process.argv.slice(2);
const course = yaml.load(fs.readFileSync(path.join(courseDir, 'course.yaml'), 'utf8'));
const MAC = course.runner === 'mac-desktop';
const HOME = MAC ? course.learner_home : '/home/learner';
const APP_BIN = MAC
  ? path.join(T, '.cache', 'app', `Rosetta-DBT-Studio-${course.app.version}-x64`, 'Rosetta DBT Studio.app', 'Contents', 'MacOS', 'Rosetta DBT Studio')
  : path.join(T, '.cache', 'app', `Rosetta-DBT-Studio-${course.app.version}-x64`, 'rosetta-dbt-studio');
const OUT = path.resolve(outArg || path.join(courseDir, '.cache', 'explore'));
fs.mkdirSync(OUT, { recursive: true });
const T0 = Date.now();
const log = (...a) => console.log(`[${((Date.now() - T0) / 1000).toFixed(1)}s]`, ...a);

(async () => {
  const seeded = seedProfile({ stateDir: path.join(courseDir, 'states', stateName), home: HOME, dbtEnv: path.join(T, '.cache', 'dbt-env'),
    python: path.join(T, '.cache', 'dbt-env', 'bin', 'python'), mac: MAC, projectsDir: course.projects_dir });
  log('seeded', seeded.projectDir);
  const app = await launchStudio({ appBin: APP_BIN, home: HOME, userData: seeded.userData, scale: 2, theme: course.theme, mac: MAC });
  app.process().stderr.on('data', (d) => fs.appendFileSync(path.join(OUT, 'electron.log'), d));
  app.process().stdout.on('data', (d) => fs.appendFileSync(path.join(OUT, 'electron.log'), d));
  const { page, windows } = await mainWindow(app);
  log('windows', JSON.stringify(windows));
  await page.waitForTimeout(3000);
  try { await sizeWindow(app, page); } catch (e) { log('sizeWindow:', e.message); }
  const info = await app.evaluate(({ app: a, BrowserWindow, screen }) => ({
    userData: a.getPath('userData'), home: a.getPath('home'), cwd: process.cwd(),
    bounds: BrowserWindow.getAllWindows().map((b) => ({ b: b.getBounds(), c: b.getContentSize(), visible: b.isVisible() })),
    displays: screen.getAllDisplays().map((d) => ({ id: d.id, bounds: d.bounds, scale: d.scaleFactor })),
  }));
  log('info', JSON.stringify(info));
  const vp = await page.evaluate(() => [innerWidth, innerHeight, devicePixelRatio]);
  log('viewport', vp);
  let n = 0;
  const shot = async (name) => { const f = path.join(OUT, `${String(n++).padStart(2, '0')}-${name}.png`); await page.screenshot({ path: f }); log('shot', path.basename(f)); return f; };
  const aria = async (name, loc) => { const s = await (loc || page.locator('body')).ariaSnapshot(); fs.writeFileSync(path.join(OUT, `${name}.aria.txt`), s); log('aria', name, s.length); return s; };
  try {
    await require(path.resolve(stepsFile))({ page, app, shot, aria, seeded, log });
  } catch (e) {
    log('STEP FAILED', e.message.split('\n')[0]);
    await shot('failed').catch(() => {});
  }
  await app.close();
  log('done');
})().catch((e) => { console.error('FATAL', e); process.exit(1); });
