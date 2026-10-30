#!/usr/bin/env python3
"""Builds assets/ for motion.html from the screenshots in screenshots/ (the screenshots stay untouched).

    python prep.py

- copies every screenshot to assets/
- covers the AI model chip (another company's name + logo) in the chat panel's bottom bar
- toast.png: the green "Packages installed" toast from 02c
- df-table.png: a compact copy of the SQL result table from 03b (index, month and revenue columns
  stitched together, so it is readable on a phone instead of spanning the full 1400 px wide cell)
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

for f in glob.glob(os.path.join(SRC, '0*.png')):
    shutil.copy(f, OUT)


def load(name):
    return np.asarray(Image.open(os.path.join(OUT, name)).convert('RGB')).copy()


def save(a, name):
    Image.fromarray(a).save(os.path.join(OUT, name))


# model chip "G gemini-2.5-flash" + its spinner, bottom bar of the chat panel
for name in ('05a-ai-prompt.png', '05b-ai-result.png', '06-import-ipynb.png'):
    a = load(name)
    a[1008:1035, 1632:1790] = a[1022, 1800]
    save(a, name)

c = load('02c-packages-installed.png')
save(c[981:1041, 1490:1890], 'toast.png')

t = load('03b-sql-to-dataframe.png')
cols = [(578, 700), (790, 960), (1690, 1850)]   # index | month | revenue
save(np.concatenate([t[525:858, x0:x1] for x0, x1 in cols], axis=1), 'df-table.png')

print('assets:', sorted(os.listdir(OUT)))
