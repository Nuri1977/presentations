// Human-looking actions on a Playwright page: drawn cursor, eased mouse glides, clean editor typing.
const CURSOR_INIT = () => {
  const install = () => {
    if (document.getElementById('__rec_cursor')) return;
    const c = document.createElement('div');
    c.id = '__rec_cursor';
    c.innerHTML =
      '<svg width="28" height="28" viewBox="0 0 28 28"><path d="M4 2 L4 22 L9.5 16.8 L13.2 25 L16.4 23.6 L12.8 15.6 L20 15.6 Z" fill="#fff" stroke="#111" stroke-width="1.6" stroke-linejoin="round"/></svg>';
    Object.assign(c.style, { position: 'fixed', left: '-100px', top: '-100px', width: '28px', height: '28px', zIndex: 2147483647, pointerEvents: 'none', filter: 'drop-shadow(0 2px 3px rgba(0,0,0,.45))' });
    document.documentElement.appendChild(c);
    const r = document.createElement('div');
    r.id = '__rec_ripple';
    Object.assign(r.style, { position: 'fixed', width: '36px', height: '36px', marginLeft: '-18px', marginTop: '-18px', borderRadius: '50%', border: '3px solid rgba(249,115,22,.95)', background: 'rgba(249,115,22,.18)', zIndex: 2147483646, pointerEvents: 'none', opacity: 0, transform: 'scale(.3)' });
    document.documentElement.appendChild(r);
    window.addEventListener('mousemove', (e) => { c.style.left = e.clientX - 3 + 'px'; c.style.top = e.clientY - 2 + 'px'; }, true);
    window.addEventListener('mousedown', (e) => {
      r.style.left = e.clientX + 'px'; r.style.top = e.clientY + 'px';
      r.animate([{ opacity: 1, transform: 'scale(.3)' }, { opacity: 0, transform: 'scale(1.6)' }], { duration: 450, easing: 'ease-out' });
    }, true);
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', install); else install();
};

const state = new WeakMap();
const ease = (t) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);

async function glideTo(page, x, y, ms = 650) {
  const s = state.get(page) || { x: 960, y: 540 };
  const steps = Math.max(8, Math.round(ms / 16));
  // slight arc so it does not look robotic
  const mx = (s.x + x) / 2 + (y - s.y) * 0.08;
  const my = (s.y + y) / 2 - (x - s.x) * 0.08;
  for (let i = 1; i <= steps; i++) {
    const t = ease(i / steps);
    const px = (1 - t) * (1 - t) * s.x + 2 * (1 - t) * t * mx + t * t * x;
    const py = (1 - t) * (1 - t) * s.y + 2 * (1 - t) * t * my + t * t * y;
    await page.mouse.move(px, py);
    await page.waitForTimeout(ms / steps);
  }
  state.set(page, { x, y });
}

async function centerOf(locator) {
  await locator.scrollIntoViewIfNeeded().catch(() => {});
  const b = await locator.boundingBox();
  if (!b) throw new Error('no bounding box for locator');
  return { x: b.x + b.width / 2, y: b.y + b.height / 2, box: b };
}

async function clickLocator(page, locator, { button = 'left', glideMs = 650, hold = 120 } = {}) {
  const { x, y } = await centerOf(locator);
  await glideTo(page, x, y, glideMs);
  await page.waitForTimeout(hold);
  await page.mouse.down({ button });
  await page.waitForTimeout(70);
  await page.mouse.up({ button });
}

// Find the visible Monaco editor instance through React's fiber tree (Studio does not expose window.monaco).
async function attachEditor(page) {
  const res = await page.evaluate(() => {
    const hosts = [...document.querySelectorAll('.monaco-editor')].filter((h) => h.offsetParent !== null);
    for (const host of hosts) {
      let el = host;
      while (el) {
        const fk = Object.keys(el).find((k) => k.startsWith('__reactFiber$'));
        if (fk) {
          let f = el[fk];
          for (let d = 0; f && d < 60; d++, f = f.return) {
            for (let h = f.memoizedState, g = 0; h && g < 80; h = h.next, g++) {
              const v = h.memoizedState && h.memoizedState.current;
              if (v && typeof v.getModel === 'function' && typeof v.executeEdits === 'function' && v.getDomNode && v.getDomNode() === host) {
                window.__recEditor = v;
                return 'ok';
              }
            }
          }
        }
        el = el.parentElement;
      }
    }
    return 'not-found:' + hosts.length;
  });
  if (res !== 'ok') throw new Error('editor not found: ' + res);
}

// Editor helpers that would change typed text. Studio's React wrapper re-applies its own options on
// re-render, so wrap updateOptions to keep these overrides in force for the whole recording.
const EDITOR_OVERRIDES = {
  autoClosingBrackets: 'never', autoClosingQuotes: 'never', autoClosingOvertype: 'never', autoSurround: 'never',
  autoIndent: 'none', formatOnType: false, quickSuggestions: false, suggestOnTriggerCharacters: false,
  acceptSuggestionOnEnter: 'off', tabCompletion: 'off', wordBasedSuggestions: 'off', parameterHints: { enabled: false },
  cursorBlinking: 'solid', inlineSuggest: { enabled: false },
};
async function tameEditor(page) {
  await page.evaluate((ov) => {
    const ed = window.__recEditor;
    if (!ed.__recTamed) {
      const orig = ed.updateOptions.bind(ed);
      ed.updateOptions = (o) => orig({ ...(o || {}), ...ov });
      ed.__recTamed = true;
    }
    ed.updateOptions({});
    ed.focus();
  }, EDITOR_OVERRIDES);
}

// Type text exactly as given with real keystrokes (helpers off). onChar(i) lets the recorder grab a frame.
async function typeInEditor(page, text, { onChar } = {}) {
  await tameEditor(page);
  let i = 0;
  for (const ch of text) {
    if (ch === '\n') await page.keyboard.press('Enter');
    else await page.keyboard.insertText(ch);
    if (onChar) await onChar(i, ch);
    i++;
  }
}

async function editorText(page) {
  return page.evaluate(() => window.__recEditor.getModel().getValue());
}

module.exports = { CURSOR_INIT, glideTo, clickLocator, centerOf, attachEditor, tameEditor, typeInEditor, editorText, EDITOR_OVERRIDES };
