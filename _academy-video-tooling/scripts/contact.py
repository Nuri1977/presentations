"""Contact sheet: grab frames at given times from a video and tile them (3 per row), with the time in a corner.

    python3 scripts/contact.py <video> <out.png> t1 t2 ...   (seconds)
"""
import pathlib, subprocess, sys, tempfile
from PIL import Image, ImageDraw

video, out, *ts = sys.argv[1:]
tmp = pathlib.Path(tempfile.mkdtemp())
ims = []
for i, t in enumerate(ts):
    f = tmp / f"{i:02d}.png"
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-ss', t, '-i', video, '-frames:v', '1', '-vf', 'scale=960:540', str(f)], check=True)
    im = Image.open(f).convert('RGB')
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, 70, 22), fill=(0, 0, 0))
    d.text((6, 5), f"{float(t):.0f}s", fill=(255, 200, 0))
    ims.append(im)
cols = 3
rows = (len(ims) + cols - 1) // cols
sheet = Image.new('RGB', (cols * 970 + 10, rows * 550 + 10), (40, 40, 40))
for i, im in enumerate(ims):
    sheet.paste(im, (10 + (i % cols) * 970, 10 + (i // cols) * 550))
sheet.save(out)
print(out)
