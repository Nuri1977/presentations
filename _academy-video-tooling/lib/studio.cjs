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
// opts: { stateDir, home, dbtEnv, python }
function seedProfile(opts) {
  const recipe = require('js-yaml').load(fs.readFileSync(path.join(opts.stateDir, 'recipe.yaml'), 'utf8'));
  const home = opts.home;
  const userData = path.join(home, '.config', 'rosetta-dbt-studio');
  const projectsDir = path.join(home, 'rosetta-dbt-studio-projects');
  const projectDir = path.join(projectsDir, recipe.project_name);
  fs.rmSync(userData, { recursive: true, force: true });
  fs.rmSync(projectDir, { recursive: true, force: true });
  fs.mkdirSync(userData, { recursive: true });
  copyDir(path.join(opts.stateDir, recipe.project_dir), projectDir);

  // DuckDB file next to the project, loaded with the recipe's SQL.
  const dbPath = path.join(projectDir, recipe.database_file);
  const sqlFiles = (recipe.sql || []).map((f) => path.resolve(opts.stateDir, f));
  const py = `import duckdb,sys\ncon=duckdb.connect(sys.argv[1])\nfor f in sys.argv[2:]:\n    con.execute(open(f).read())\ncon.close()`;
  execFileSync(opts.python, ['-c', py, dbPath, ...sqlFiles], { stdio: 'inherit' });

  // dbt profile (Studio keeps it beside the project).
  fs.writeFileSync(
    path.join(projectDir, 'profiles.yml'),
    `${recipe.project_name}:\n  target: dev\n  outputs:\n    dev:\n      type: duckdb\n      path: ${dbPath}\n      threads: 4\n`,
  );

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
          name: 'course',
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
    args: [`--user-data-dir=${opts.userData}`, '--no-sandbox', `--force-device-scale-factor=${scale}`, '--disable-gpu'],
    env: { ...process.env, HOME: opts.home, ELECTRON_NO_UPDATER: '1', DISABLE_ANALYTICS: '1' },
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
async function sizeWindow(electronApp, page) {
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
