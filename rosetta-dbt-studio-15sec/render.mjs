// Renders motion.html to an MP4, frame by frame, with headless Chrome + ffmpeg.
//
//   node render.mjs                     -> rosetta-dbt-studio-<duration>s.mp4 (1920x1080, 60 fps)
//   node render.mjs --fps 30            -> 30 fps instead
//   node render.mjs --stills 1.2 5.8    -> PNG stills at those timestamps (for review)
//   node render.mjs --silent            -> skip the soundtrack
//
// Needs: Google Chrome installed, ffmpeg on PATH, and Playwright (reused from ../../dbt-studio).
// Soundtrack: run `python3 score.py` first to (re)build score.wav.
import { createRequire } from 'module';
import { spawn } from 'child_process';
import { fileURLToPath, pathToFileURL } from 'url';
import path from 'path';
import fs from 'fs';

const here = path.dirname(fileURLToPath(import.meta.url));
const require = createRequire(import.meta.url);
const { chromium } = require(path.join(here, '../../dbt-studio/node_modules/playwright'));

const args = process.argv.slice(2);
const opt = (name, dflt) => { const i = args.indexOf(name); return i >= 0 ? args[i + 1] : dflt; };
const fps = Number(opt('--fps', 60));
const outArg = opt('--out', null);
const stillsAt = args.includes('--stills') ? args.slice(args.indexOf('--stills') + 1).filter((a) => !a.startsWith('--')).map(Number) : null;
const stillsDir = opt('--stills-dir', path.join(here, 'stills'));

const browser = await chromium.launch({
  channel: 'chrome',
  headless: true,
  args: ['--force-color-profile=srgb', '--hide-scrollbars', '--disable-gpu-vsync'],
});
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
await page.goto(pathToFileURL(path.join(here, 'motion.html')).href + '?capture=1', { waitUntil: 'networkidle' });
await page.evaluate(() => window.ready);

const shot = async (t) => {
  await page.evaluate((tt) => window.seek(tt), t);
  return page.screenshot({ type: 'png', clip: { x: 0, y: 0, width: 1920, height: 1080 } });
};

if (stillsAt) {
  fs.mkdirSync(stillsDir, { recursive: true });
  for (const t of stillsAt) {
    const buf = await shot(t);
    const f = path.join(stillsDir, `t${t.toFixed(2).padStart(5, '0')}.png`);
    fs.writeFileSync(f, buf);
    console.log(f);
  }
  await browser.close();
  process.exit(0);
}

const duration = await page.evaluate(() => window.DURATION);
const out = outArg ?? path.join(here, `rosetta-dbt-studio-${duration}s.mp4`);
const frames = Math.round(duration * fps);
// Write to a .part file and rename when ffmpeg finishes, so the .mp4 only appears once it is playable.
const tmp = `${out}.part`;
// score.wav (from `python3 score.py`) is muxed in when present; --silent skips it.
const score = path.join(here, 'score.wav');
const audio = fs.existsSync(score) && !args.includes('--silent')
  ? ['-i', score, '-map', '0:v', '-map', '1:a', '-c:a', 'aac', '-b:a', '256k', '-shortest']
  : [];
const ff = spawn('ffmpeg', [
  '-y', '-loglevel', 'error',
  '-f', 'image2pipe', '-framerate', String(fps), '-c:v', 'png', '-i', '-',
  ...audio,
  '-c:v', 'libx264', '-preset', 'slow', '-crf', '16', '-pix_fmt', 'yuv420p',
  '-profile:v', 'high', '-movflags', '+faststart', '-f', 'mp4', tmp,
], { stdio: ['pipe', 'inherit', 'inherit'] });

const started = Date.now();
for (let i = 0; i < frames; i++) {
  const buf = await shot(i / fps);
  if (!ff.stdin.write(buf)) await new Promise((r) => ff.stdin.once('drain', r));
  if (i % fps === 0) process.stdout.write(`\rframe ${i}/${frames}  ${((Date.now() - started) / 1000).toFixed(0)}s`);
}
ff.stdin.end();
const code = await new Promise((r) => ff.on('close', r));
await browser.close();
if (code !== 0) {
  console.error(`\nffmpeg exited with code ${code}; partial output left at ${tmp}`);
  process.exit(1);
}
fs.renameSync(tmp, out);
console.log(`\nwrote ${out} (${frames} frames @ ${fps} fps) in ${((Date.now() - started) / 1000).toFixed(0)}s`);
