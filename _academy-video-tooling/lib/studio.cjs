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
    return { userData, projectDir: recipe.project_name ? path.join(projectsDir, recipe.project_name) : null, dbPath: null, recipe };
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
    for (const b of BrowserWindow.getAllWindows()) if (b.isVisible() && !b.isSimpleFullScreen()) b.setSimpleFullScreen(true);
    return 'simple-fullscreen';
  }, { W, H });
  if (fit === 'simple-fullscreen') {
    for (let k = 0; k < 20; k++) {
      const vp = await page.evaluate(() => [window.innerWidth, window.innerHeight]);
      if (vp[0] === W && vp[1] === H) return;
      await new Promise((r) => setTimeout(r, 300));
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
