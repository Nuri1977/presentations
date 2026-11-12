// Launch the official Rosetta DBT Studio release with a throwaway, seeded profile.
// Never touches the user's real profile or the dbt-studio source repo.
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');
const { _electron } = require('playwright');

const W = 1920;
const H = 1080;

function copyDir(src, dst) {
  fs.mkdirSync(dst, { recursive: true });
  for (const e of fs.readdirSync(src, { withFileTypes: true })) {
    const s = path.join(src, e.name);
    const d = path.join(dst, e.name);
    if (e.isDirectory()) copyDir(s, d);
    else if (e.name !== '.gitkeep') fs.copyFileSync(s, d); // .gitkeep only keeps empty folders in git
  }
}

// Build the start state: project files, DuckDB data, dbt profile, Studio database.json.
// opts: { stateDir, home, dbtEnv, python, mac, projectsDir }
//   mac: userData under ~/Library/Application Support like a real Mac install (default: ~/.config, Linux)
//   projectsDir: folder name under home for projects (default: rosetta-dbt-studio-projects)
// Recipe extras (optional): copy: [{from, to}] copies files/folders into the project (e.g. data not in git);
//   git: {user, email, commits: [{message, paths}]} builds a local history (never pushed).
// lake: a DuckLake at the learner path, as the earlier lessons left it, registered in Studio but not yet opened.
//   lake: { name: eth_lake, dir: lake, catalog: eth_catalog.duckdb, sql: [../sql/a.sql, ...], vars: {key: path} }
// The catalog stores the data folder's absolute path, so the lake is always built in place (never copied).
// SQL files run in order with the lake attached and selected; {{project}}, {{cache}} and vars are replaced.
function seedLake({ recipe, opts, userData, projectDir }) {
  const lk = recipe.lake;
  const dir = path.join(projectDir, lk.dir || 'lake');
  const catalog = path.join(dir, lk.catalog || `${lk.name}_catalog.duckdb`);
  const data = path.join(dir, 'data');
  fs.rmSync(dir, { recursive: true, force: true });
  fs.mkdirSync(data, { recursive: true });
  for (const d of lk.dirs || []) fs.mkdirSync(path.join(dir, d), { recursive: true }); // e.g. landing (4.5)
  const vars = { project: projectDir, cache: path.resolve(opts.stateDir, '..', '..', '.cache'), ...(lk.vars || {}) };
  // S3 reads in the lesson scripts are rewritten to the local cache (same files, no network, seconds not minutes)
  const cacheEth = path.join(vars.cache, 'data', 'eth');
  const tmp = fs.mkdtempSync(path.join(require('os').tmpdir(), 'lake-seed-'));
  const sqlFiles = (lk.sql || []).map((f, i) => {
    let t = fs.readFileSync(path.resolve(opts.stateDir, f), 'utf8');
    t = t.replace(/read_parquet\('s3:\/\/aws-public-blockchain\/v1\.0\/eth\/(blocks|transactions)\/date=([^/']+)\/\*\.parquet'\)/g,
      (m, tb, d) => `read_parquet('${cacheEth}/${tb}/${tb}_${d}.parquet')`);
    t = t.replace(/\*\s+exclude\s*\(logs_bloom,\s*last_modified(,\s*)?/gi, (m, more) => (more ? '* exclude (' : '* exclude ('));
    t = t.replace(/\*\s+exclude\s*\(\s*\)/gi, '*');
    const out = path.join(tmp, `${String(i).padStart(2, '0')}.sql`);
    fs.writeFileSync(out, t);
    return out;
  });
  const py = [
    'import duckdb,sys,json,re',
    'cat,data,name,vars=sys.argv[1],sys.argv[2],sys.argv[3],json.loads(sys.argv[4])',
    'con=duckdb.connect()',
    'con.execute(f"attach \'ducklake:{cat}\' as {name} (data_path \'{data}/\')")',
    'con.execute(f"use {name}")',
    'for f in sys.argv[5:]:',
    '    t=open(f).read()',
    '    for k,v in vars.items(): t=t.replace("{{"+k+"}}",str(v))',
    '    t=chr(10).join(l for l in t.splitlines() if not l.strip().startswith("--"))',
    '    for st in [x.strip() for x in t.split(";") if x.strip()]: con.execute(st)',
    'con.execute("use memory"); con.execute(f"detach {name}"); con.close()',
  ].join('\n');
  // build the lake with the same DuckDB + DuckLake version that Studio runs (1.5.2 / 415a9ebd), so Studio
  // reads exactly what it would have written itself (the dbt runtime's 1.5.6 writes delete files differently)
  const seedPy = path.join(path.dirname(opts.dbtEnv), 'seed-env', 'bin', 'python');
  execFileSync(fs.existsSync(seedPy) ? seedPy : opts.python, ['-c', py, catalog, data, lk.name, JSON.stringify(vars), ...sqlFiles], { stdio: 'inherit' });
  const now = '2026-11-01T09:00:00.000Z';
  fs.mkdirSync(path.join(userData, 'datalake'), { recursive: true });
  fs.writeFileSync(path.join(userData, 'datalake', 'instances.json'), JSON.stringify({
    version: '1.0.0',
    instances: [{
      id: `ducklake_1794435029641_${lk.name.replace(/[^a-z0-9]/gi, '').slice(0, 9).padEnd(9, '0')}`, name: lk.name, description: lk.description || '',
      dataPath: data, storage: { type: 'local', local: { path: data } }, catalog: { type: 'duckdb', duckdb: { metadataPath: catalog } },
      createdAt: now, updatedAt: now, status: 'inactive',
      runtimeOptions: { maxMemory: '4GB', threads: 4, enableOptimizer: true, tempDirectory: '/tmp/ducklake' },
    }],
    lastModified: now,
  }, null, 2));
}

function seedProfile(opts) {
  const recipe = require('js-yaml').load(fs.readFileSync(path.join(opts.stateDir, 'recipe.yaml'), 'utf8'));
  const home = opts.home;
  const userData = opts.mac ? path.join(home, 'Library', 'Application Support', 'rosetta-dbt-studio') : path.join(home, '.config', 'rosetta-dbt-studio');
  const projectsDir = path.join(home, opts.projectsDir || 'rosetta-dbt-studio-projects');
  // fresh: true = a brand-new install (empty profile, no runtime, no project), e.g. the install lesson
  if (recipe.fresh) {
    fs.rmSync(userData, { recursive: true, force: true });
    fs.mkdirSync(userData, { recursive: true });
    for (const d of recipe.clean || []) fs.rmSync(path.join(home, d), { recursive: true, force: true });
    return { userData, projectDir: null, dbPath: null, recipe };
  }
  // setup_only: true = Studio already set up (Python + dbt, as after Lesson 1.1) but no project or connection yet
  if (recipe.setup_only) {
    fs.rmSync(userData, { recursive: true, force: true });
    fs.mkdirSync(userData, { recursive: true });
    for (const d of recipe.clean || []) fs.rmSync(path.join(home, d), { recursive: true, force: true });
    fs.mkdirSync(projectsDir, { recursive: true });
    for (const d of recipe.mkdirs || []) fs.mkdirSync(path.join(home, d), { recursive: true }); // folders the learner made by hand
    if (recipe.git) {
      const g = recipe.git;
      fs.writeFileSync(path.join(home, '.gitconfig'), `[user]\n\tname = ${g.user}\n\temail = ${g.email}\n[init]\n\tdefaultBranch = main\n[credential]\n\thelper =\n\thelper = store\n`);
    }
    const rt = JSON.parse(fs.readFileSync(path.join(path.dirname(opts.dbtEnv), 'runtime.json'), 'utf8'));
    const venv0 = path.join(userData, 'venv');
    fs.symlinkSync(opts.dbtEnv, venv0);
    const py0 = path.join(userData, 'python', `cpython-${rt.pythonVersion}-${rt.platform}`);
    fs.mkdirSync(path.dirname(py0), { recursive: true });
    fs.symlinkSync(path.dirname(path.dirname(rt.pythonBinary)), py0);
    fs.writeFileSync(path.join(userData, 'database.json'), JSON.stringify({
      schemaVersion: 1,
      settings: {
        isSetup: 'true', pythonPath: path.join(venv0, 'bin', 'python3'), pythonBinary: path.join(py0, 'bin', 'python3'),
        pythonVersion: rt.pythonVersion, dbtPath: path.join(venv0, 'bin', 'dbt'), dbtVersion: rt.dbtVersion,
        projectsDirectory: projectsDir, dbtSampleDirectory: path.join(userData, 'dbt_sample'), sampleRosettaMainConf: path.join(userData, 'main.conf'),
      },
      projects: [], connections: [],
    }, null, 2));
    const pd = recipe.project_name ? path.join(projectsDir, recipe.project_name) : null;
    if (recipe.lake) seedLake({ recipe, opts, userData, projectDir: pd });
    return { userData, projectDir: pd, dbPath: null, recipe };
  }
  const projectDir = path.join(projectsDir, recipe.project_name);
  fs.rmSync(userData, { recursive: true, force: true });
  fs.rmSync(projectDir, { recursive: true, force: true });
  fs.mkdirSync(userData, { recursive: true });
  const gitEnv = { ...process.env, HOME: home, GIT_CONFIG_NOSYSTEM: '1' };
  if (recipe.git) {
    const g = recipe.git;
    // keep pushes on the learner's own token file (~/.git-credentials, written by Nuri), never the Mac keychain
    fs.writeFileSync(path.join(home, '.gitconfig'), `[user]\n\tname = ${g.user}\n\temail = ${g.email}\n[init]\n\tdefaultBranch = main\n[credential]\n\thelper =\n\thelper = store\n`);
  }
  if (recipe.clone) {
    // clone: the end of the previous lesson as pushed to GitHub (read-only clone), plus the empty
    // template folders git does not keep
    fs.mkdirSync(projectsDir, { recursive: true });
    execFileSync('git', ['clone', '-q', recipe.clone, projectDir], { env: gitEnv, stdio: 'pipe' });
    for (const d of recipe.dirs || []) fs.mkdirSync(path.join(projectDir, d), { recursive: true });
  } else {
    copyDir(path.join(opts.stateDir, recipe.project_dir), projectDir);
  }
  for (const c of recipe.copy || []) {
    const src = path.resolve(opts.stateDir, c.from);
    const dst = path.join(projectDir, c.to);
    if (fs.statSync(src).isDirectory()) copyDir(src, dst);
    else { fs.mkdirSync(path.dirname(dst), { recursive: true }); fs.copyFileSync(src, dst); }
  }

  for (const d of recipe.mkdirs || []) fs.mkdirSync(path.join(projectDir, d), { recursive: true });

  // DuckDB file next to the project, loaded with the recipe's SQL.
  const dbPath = path.join(projectDir, recipe.database_file);
  fs.mkdirSync(path.dirname(dbPath), { recursive: true });
  const sqlFiles = (recipe.sql || []).map((f) => path.resolve(opts.stateDir, f));
  const py = `import duckdb,sys\ncon=duckdb.connect(sys.argv[1])\nfor f in sys.argv[2:]:\n    con.execute(open(f).read())\ncon.close()`;
  execFileSync(opts.python, ['-c', py, dbPath, ...sqlFiles], { stdio: 'inherit' });

  // dbt profile (Studio keeps it beside the project). A cloned project keeps the committed one.
  if (!recipe.clone) fs.writeFileSync(
    path.join(projectDir, 'profiles.yml'),
    `${recipe.project_name}:\n  target: dev\n  outputs:\n    dev:\n      type: duckdb\n      path: ${dbPath}\n      threads: 4\n`,
  );

  // Local git history for the start state (as if the earlier lessons had committed on camera). Never pushed.
  if (recipe.git && !recipe.clone) {
    const g = recipe.git;
    const git = (...a) => execFileSync('git', a, { cwd: projectDir, env: gitEnv, stdio: 'pipe' });
    git('init', '-q', '-b', 'main');
    for (const c of g.commits || []) {
      git('add', '--', ...c.paths);
      git('commit', '-q', '-m', c.message);
    }
  }

  // dbt: commands the earlier lessons ran on camera (e.g. seed, run), so the database matches the story.
  // They run off camera with the pinned runtime; the .user.yml dbt writes beside profiles.yml is removed.
  for (const cmd of recipe.dbt || []) {
    execFileSync(path.join(opts.dbtEnv, 'bin', 'dbt'), [...cmd.split(' '), '--profiles-dir', projectDir], { cwd: projectDir, env: { ...gitEnv, DBT_SEND_ANONYMOUS_USAGE_STATS: 'false' }, stdio: 'pipe' });
  }
  fs.rmSync(path.join(projectDir, '.user.yml'), { force: true });

  // Managed venv location as Studio expects it, pointing at the pinned recording env.
  const runtime = JSON.parse(fs.readFileSync(path.join(path.dirname(opts.dbtEnv), 'runtime.json'), 'utf8'));
  const venv = path.join(userData, 'venv');
  fs.symlinkSync(opts.dbtEnv, venv);
  const pyHome = path.join(userData, 'python', `cpython-${runtime.pythonVersion}-${runtime.platform}`);
  fs.mkdirSync(path.dirname(pyHome), { recursive: true });
  fs.symlinkSync(path.dirname(path.dirname(runtime.pythonBinary)), pyHome);

  const project = {
    id: `${recipe.project_name}-id`,
    name: recipe.project_name,
    path: projectDir,
    connectionId: 'course-duckdb-id',
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
  };
  const db = {
    schemaVersion: 1,
    settings: {
      isSetup: 'true',
      pythonPath: path.join(venv, 'bin', 'python3'),
      pythonBinary: path.join(pyHome, 'bin', 'python3'),
      pythonVersion: runtime.pythonVersion,
      dbtPath: path.join(venv, 'bin', 'dbt'),
      dbtVersion: runtime.dbtVersion,
      projectsDirectory: projectsDir,
      dbtSampleDirectory: path.join(userData, 'dbt_sample'),
      sampleRosettaMainConf: path.join(userData, 'main.conf'),
    },
    projects: [project],
    connections: [
      {
        id: 'course-duckdb-id',
        connection: {
          type: 'duckdb',
          name: recipe.connection_name || 'course',
          database_path: dbPath,
          short_database_path: recipe.database_file,
        },
      },
    ],
    selectedProject: project,
  };
  fs.writeFileSync(path.join(userData, 'database.json'), JSON.stringify(db, null, 2));
  if (recipe.lake) seedLake({ recipe, opts, userData, projectDir });
  return { userData, projectDir, dbPath, recipe };
}

// opts: { appBin, home, userData, scale, theme, recordVideoDir }
async function launchStudio(opts) {
  const scale = opts.scale || 2;
  const electronApp = await _electron.launch({
    executablePath: opts.appBin,
    args: [`--user-data-dir=${opts.userData}`, '--no-sandbox', `--force-device-scale-factor=${scale}`, ...(opts.mac ? [] : ['--disable-gpu'])],
    // Mac: start from / like an app opened from Finder, so relative paths behave as they do for a learner
    ...(opts.mac ? { cwd: '/' } : {}),
    // dbt usage tracking is blocked in the sandbox and can stall dbt; it never shows on screen
    env: { ...process.env, HOME: opts.home, ELECTRON_NO_UPDATER: '1', DISABLE_ANALYTICS: '1', DBT_SEND_ANONYMOUS_USAGE_STATS: 'false', DO_NOT_TRACK: '1', BROWSER: '/usr/bin/true' }, // dbt docs serve must not open the Mac's real browser
    ...(opts.recordVideoDir ? { recordVideo: { dir: opts.recordVideoDir, size: { width: W, height: H } } } : {}),
    timeout: 120000,
  });
  const theme = opts.theme || 'dark';
  await electronApp.context().addInitScript((t) => {
    try {
      // Studio stores the MUI color scheme JSON-encoded.
      localStorage.setItem('dbt-studio-theme-mode', JSON.stringify(t));
      localStorage.setItem('dbt-studio-quickstart-tour-seen', 'true');
    } catch (e) {}
  }, theme);
  return electronApp;
}

// Wait for the main app window (not the splash), then size its content to 1920x1080.
async function mainWindow(electronApp, timeoutMs = 90000) {
  const t0 = Date.now();
  while (Date.now() - t0 < timeoutMs) {
    for (const w of electronApp.windows()) {
      const url = w.url();
      if (/#\/?app|index\.html/.test(url) && !/splash|loader/i.test(url)) {
        const size = await electronApp.evaluate(({ BrowserWindow }) =>
          BrowserWindow.getAllWindows().map((b) => ({ title: b.getTitle(), size: b.getContentSize(), visible: b.isVisible() })),
        );
        return { page: w, windows: size };
      }
    }
    await new Promise((r) => setTimeout(r, 500));
  }
  throw new Error('Main window did not appear: ' + electronApp.windows().map((w) => w.url()).join(', '));
}

// Studio sizes its window itself after load, so keep applying 1920x1080 until it holds.
// On a Mac with a 1920x1080 display the menu bar would clip a titled window to 1027 px, so the
// window goes into simple full screen there (covers the menu bar, no new Space, no animation).
async function sizeWindow(electronApp, page) {
  const fit = await electronApp.evaluate(({ BrowserWindow, screen }, s) => {
    if (process.platform !== 'darwin') return 'skip';
    const d = screen.getPrimaryDisplay().bounds;
    if (d.width !== s.W || d.height !== s.H) return `display ${d.width}x${d.height}`;
    // the window can open on another display (e.g. the laptop screen): put it on the primary one first
    for (const b of BrowserWindow.getAllWindows()) {
      if (!b.isVisible()) continue;
      const wb = b.getBounds();
      if (wb.x < d.x || wb.y < d.y || wb.x >= d.x + d.width || wb.y >= d.y + d.height) {
        if (b.isSimpleFullScreen()) b.setSimpleFullScreen(false);
        b.setBounds({ x: d.x + 40, y: d.y + 60, width: 1200, height: 800 });
      }
      if (!b.isSimpleFullScreen()) b.setSimpleFullScreen(true);
    }
    return 'simple-fullscreen';
  }, { W, H });
  if (fit === 'simple-fullscreen') {
    for (let attempt = 0; attempt < 4; attempt++) {
      for (let k = 0; k < 20; k++) {
        // with a UI zoom the CSS viewport is smaller; the window itself must still be 1920x1080 DIP
        const vp = await page.evaluate(() => [Math.round(window.innerWidth * window.devicePixelRatio / 2), Math.round(window.innerHeight * window.devicePixelRatio / 2)]);
        if (Math.abs(vp[0] - W) <= 2 && Math.abs(vp[1] - H) <= 2) return;
        await new Promise((r) => setTimeout(r, 300));
      }
      // sometimes the first switch does not take: leave simple full screen and enter it again
      await electronApp.evaluate(({ BrowserWindow }) => { for (const b of BrowserWindow.getAllWindows()) { if (b.isVisible()) b.setSimpleFullScreen(false); } });
      await new Promise((r) => setTimeout(r, 1200));
      await electronApp.evaluate(({ BrowserWindow }) => { for (const b of BrowserWindow.getAllWindows()) { if (b.isVisible()) b.setSimpleFullScreen(true); } });
      await new Promise((r) => setTimeout(r, 1500));
    }
    throw new Error('simple full screen did not give 1920x1080');
  }
  let ok = 0;
  for (let k = 0; k < 40 && ok < 3; k++) {
    const sz = await electronApp.evaluate(({ BrowserWindow }, s) => {
      const out = [];
      for (const b of BrowserWindow.getAllWindows()) {
        if (!b.isVisible()) continue;
        if (b.isMaximized()) b.unmaximize();
        const [w, h] = b.getContentSize();
        if (w !== s.W || h !== s.H) { b.setContentSize(s.W, s.H); b.setPosition(0, 0); }
        out.push(b.getContentSize());
      }
      return out;
    }, { W, H });
    const vp = page ? await page.evaluate(() => [window.innerWidth, window.innerHeight]) : [W, H];
    ok = sz.length && sz.every(([w, h]) => w === W && h === H) && vp[0] === W && vp[1] === H ? ok + 1 : 0;
    await new Promise((r) => setTimeout(r, 500));
  }
  if (ok < 3) throw new Error('window did not settle at 1920x1080');
}

module.exports = { seedProfile, launchStudio, mainWindow, sizeWindow, W, H };
