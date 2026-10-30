#!/usr/bin/env python3
"""Builds assets/ for motion.html from the screenshots in screenshots/ (the screenshots stay untouched).

    python prep.py

- copies every screenshot to assets/
- step palette (edit mode, 2 + 5): keeps dbt / rosetta / shell and hides the rows named after other
  companies' products (shell moves up into the third slot, the rest is painted over)
- run-0..run-5.png: the run, one frame per state, built from 14 (first step running) and 15 (all green):
    run-0  idle: 15 with the step status chips removed (top chip still says FINISHED from the last run)
    run-1  = 14: step 1 running, the rest not started
    run-k  steps < k succeeded, step k running (14's blue frame + Running chip moved onto it), rest not started
    run-5  = 15: every step green
"""
import glob
import os
import shutil

import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'screenshots')
OUT = os.path.join(HERE, 'assets')
os.makedirs(OUT, exist_ok=True)

for f in glob.glob(os.path.join(SRC, '*.png')):
    shutil.copy(f, OUT)


def load(name):
    return np.asarray(Image.open(os.path.join(OUT, name)).convert('RGB')).copy()


def save(a, name):
    Image.fromarray(a).save(os.path.join(OUT, name))


# palette rows (34 px apart): dbt 265, rosetta 299, terraform 333, shell 367, s3 401, kinetica 435
for name in ('2.visual-edit-mode.png', '5.change-reflected-in-graph.png'):
    a = load(name)
    a[333:367, 630:800] = a[367:401, 630:800]
    a[367:470, 630:800] = a[262, 790]
    save(a, name)

running, done = load('14.rerun-running.png'), load('15.all-nodes-success.png')
NODES = [698, 1005, 1312, 1619]   # left edge of each step node; all are 259 px wide
Y0, Y1 = 306, 438


def node(a, k):
    x = NODES[k]
    return a[Y0:Y1, x - 6:x + 265]


# where step 1's "running" look (blue frame + Running chip) differs from its finished look
frame = np.abs(node(running, 0).astype(int) - node(done, 0).astype(int)).sum(2) > 40

idle = done.copy()
for k in range(4):
    n = node(idle, k)
    diff = np.abs(node(done, k).astype(int) - node(running, k).astype(int)).sum(2) > 40
    chip = diff[58:84, 130:258]   # status chip row (364..390), right half only so step 1's blue frame is left out
    xs = np.where(chip.any(0))[0] + 130
    n[58:84, xs.min() - 2:xs.max() + 3] = n[70, xs.min() - 6]
save(idle, 'run-0.png')
save(running, 'run-1.png')
for k in (1, 2, 3):
    a = running.copy()
    for j in range(k):
        node(a, j)[:] = node(done, j)
    n = node(a, k)
    n[:] = node(done, k)
    n[frame] = node(running, 0)[frame]
    save(a, f'run-{k + 1}.png')
save(done, 'run-5.png')

print('assets:', sorted(os.listdir(OUT)))
