// Open the course's saved recording browser profile, visibly, on GitHub's sign-in page, so Nuri can sign in once.
//   node browser-login.cjs <course_dir>
// Claude never types in this window. It closes by itself once github.com shows a signed-in user (or after 15 minutes).
const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');
const { chromium } = require('playwright');
const course = yaml.load(fs.readFileSync(path.join(process.argv[2], 'course.yaml'), 'utf8'));
(async () => {
  if (!course.browser_profile) throw new Error('course.yaml has no browser_profile');
  fs.mkdirSync(course.browser_profile, { recursive: true });
  const ctx = await chromium.launchPersistentContext(course.browser_profile, { headless: false, viewport: { width: 1280, height: 860 }, colorScheme: 'dark' });
  let page = ctx.pages()[0] || (await ctx.newPage());
  await page.goto('https://github.com/login');
  await page.bringToFront();
  const t0 = Date.now();
  let user = '';
  while (Date.now() - t0 < 20 * 60 * 1000) {
    await new Promise((r) => setTimeout(r, 2000));
    // if the tab was closed by mistake, open the sign-in page again (the window stays until signed in)
    const open = ctx.pages().filter((p) => !p.isClosed());
    if (!open.length) { page = await ctx.newPage(); await page.goto('https://github.com/login'); continue; }
    for (const p of open) {
      user = await p.evaluate(() => document.querySelector('meta[name="user-login"]')?.content || '').catch(() => '');
      if (user) break;
    }
    if (user) break;
  }
  console.log(user ? `signed in as ${user}` : 'not signed in');
  await new Promise((r) => setTimeout(r, 1500));
  await ctx.close().catch(() => {});
})().catch((e) => { console.error('ERR', e.message); process.exit(1); });
