#!/usr/bin/env python3
"""Builds assets/ for motion.html from the screenshots in screenshots/ (the screenshots stay untouched).

    python prep.py

- scales every screenshot to 2000 px wide (2032 -> 2000), so motion.html works in one set of coordinates
- browser screenshots (01, 06): keeps only the page; the browser bar (bookmarks, other sites' icons, the file
  path with a username) is cropped off
- covers the AI model chip (another company's name + logo) in the chat panel's bottom bar
- Build Analytics Site dialog (03): swaps the username in the output folder ("/Users/nuri/") for "/Users/user/".
  The field uses a proportional font, so the line is split into letters at the gaps between them and "user"
  is put together from letters of the same line ("u" from nuri, "s", "e", "r" from Users); the rest of the
  path moves left by the difference in width
"""
import os

import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'screenshots')
OUT = os.path.join(HERE, 'assets')
os.makedirs(OUT, exist_ok=True)


def load(name):
    im = Image.open(os.path.join(SRC, name)).convert('RGB')
    return np.asarray(im.resize((2000, round(im.height * 2000 / im.width)), Image.LANCZOS)).copy()


def save(a, name):
    Image.fromarray(a).save(os.path.join(OUT, name))


def cover(a, x0, y0, x1, y1):
    """Paint a box with the background, blended row by row from the columns just left and right of it."""
    u = np.linspace(0, 1, x1 - x0)[None, :, None]
    a[y0:y1, x0:x1] = (a[y0:y1, x0 - 1:x0] * (1 - u) + a[y0:y1, x1:x1 + 1] * u).astype(np.uint8)


def letters(band, bg):
    """Column spans of the letters in a line of text, split at the columns between them (faint edge pixels ignored)."""
    ink = (np.abs(band.astype(int) - bg).sum(2) > 300).any(0)
    spans, start = [], None
    for x, on in enumerate(ink):
        if on and start is None:
            start = x
        elif not on and start is not None:
            spans.append((start, x))
            start = None
    if start is not None:
        spans.append((start, len(ink)))
    return spans


def swap_user(a, y0, y1, x0, x1):
    """'/Users/nuri/...' -> '/Users/user/...' in one line of proportional text inside x0..x1."""
    band = a[y0:y1, x0:x1]
    bg = band[:, -3:].reshape(-1, 3).mean(0)
    sp = letters(band, bg)
    # / U s e r s / n u r i /  -> each letter's cell runs from the middle of the gap before it to the middle of the gap after it
    assert len(sp) >= 12, f'expected the letters of /Users/nuri/, got {len(sp)} spans'
    cut = [0] + [(sp[i][1] + sp[i + 1][0]) // 2 for i in range(len(sp) - 1)] + [band.shape[1]]
    cell = lambda k: band[:, cut[k]:cut[k + 1]].copy()
    parts = [band[:, :cut[7]].copy()] + [cell(k) for k in (8, 2, 3, 4)] + [band[:, cut[11]:].copy()]
    line = np.concatenate(parts, axis=1)[:, :band.shape[1]]
    band[:] = bg.astype(np.uint8)
    band[:, :line.shape[1]] = line
    print(f'  swapped the username at y {y0}-{y1} ({len(sp)} letters found)')


for name in sorted(os.listdir(SRC)):
    a = load(name)
    if 'browser' in name:
        a = a[150:1075, 56:1944].copy()            # page only: no browser bar
    if name.startswith(('slide-02', 'slide-03', 'slide-07')):
        cover(a, 1642, 1006, 1818, 1044)
    if name.startswith('slide-03'):
        swap_user(a, 600, 624, 712, 1250)
    save(a, name)

print('assets:', sorted(os.listdir(OUT)))
