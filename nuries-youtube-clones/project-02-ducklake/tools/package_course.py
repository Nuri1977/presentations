"""Package the whole course: UPLOAD-SHEET.md and full-course/ (joined 4K and 1080p videos, captions, YouTube text).
  python3 tools/package_course.py            (all lessons must be packaged)
Lessons are joined without re-encoding (same encoder settings in every lesson)."""
import pathlib, re, subprocess, json, datetime

C = pathlib.Path(__file__).resolve().parents[1]
ORDER = ['lesson-0-welcome', 'lesson-0-1-install', 'lesson-1-1-lakehouse', 'lesson-1-2-parquet', 'lesson-1-3-table-formats',
         'lesson-1-4-how-ducklake-works', 'lesson-1-5-ethereum-data', 'lesson-1-6-under-the-hood', 'lesson-2-1-create-ducklake',
         'lesson-2-2-load-blocks', 'lesson-2-3-look-inside', 'lesson-2-4-snapshots', 'lesson-2-5-time-travel',
         'lesson-3-1-insert-update-delete', 'lesson-3-2-daily-loads', 'lesson-3-3-schema-evolution', 'lesson-3-4-change-feed',
         'lesson-3-5-transactions', 'lesson-4-1-partitioning', 'lesson-4-2-statistics', 'lesson-4-3-data-inlining',
         'lesson-4-4-maintenance', 'lesson-4-5-adding-files', 'lesson-5-1-catalog-snapshots', 'lesson-5-2-catalog-files',
         'lesson-5-3-read-by-hand', 'lesson-6-1-connect-dbt', 'lesson-6-2-staging', 'lesson-6-3-marts', 'lesson-6-4-tests-docs',
         'lesson-7-1-going-further']
REPO = 'https://github.com/Nuri1977/ethereum-ducklake-dbt'


def dur(p):
    return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(p)]).decode().strip())


def mmss(s):
    s = int(round(s)); h, r = divmod(s, 3600); m, s = divmod(r, 60)
    return f'{h}:{m:02d}:{s:02d}' if h else f'{m}:{s:02d}'


def srt_t(t):
    ms = int(round(t * 1000)); h, r = divmod(ms, 3600000); m, r = divmod(r, 60000); s, ms = divmod(r, 1000)
    return f'{h:02d}:{m:02d}:{s:02d},{ms:03d}'


def parse_srt_t(x):
    h, m, rest = x.split(':'); s, ms = rest.split(',')
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000


import yaml
rows = []
for name in ORDER:
    L = C / name
    y = yaml.safe_load((L / 'lesson.yaml').read_text())
    n = str(y['number']); mp4 = L / f"lesson-{n.replace('.', '-')}.mp4"
    if not mp4.exists(): raise SystemExit(f'missing {mp4}')
    yt = (L / 'youtube.md').read_text()
    title = re.search(r'## Title\n\n(.+)\n', yt).group(1).strip()
    desc = re.search(r'## Description\n\n(.*?)\n## Tags', yt, re.S).group(1).strip()
    tags = re.search(r'## Tags\n\n(.+)', yt).group(1).strip()
    rows.append(dict(name=name, n=n, title=y['title'], mp4=mp4, hd=L / f"lesson-{n.replace('.', '-')}-1080p.mp4",
                     srt=L / f"lesson-{n.replace('.', '-')}.srt", d=dur(mp4), size=mp4.stat().st_size, yt_title=title, desc=desc, tags=tags))
total = sum(r['d'] for r in rows)
head = subprocess.run(['git', 'ls-remote', REPO + '.git', 'HEAD'], capture_output=True, text=True).stdout.split()[:1]
today = datetime.date.today().strftime('%-d %b %Y')

# ---- upload sheet
out = [f'# Upload sheet: Data Lakes with DuckLake in Rosetta DBT Studio\n',
       'Project 2: an Ethereum data lake on your laptop, from the first snapshot to dbt models on top\n',
       '- **Playlist:** Data Lakes with DuckLake in Rosetta DBT Studio: Project 2',
       f'- **Videos:** {len(rows)}, {mmss(total)} in total. Upload in the order below.',
       '- **Visibility:** unlisted (embedded in Rosetta Academy: https://academy.rosettadb.io/)',
       f"- **Code repo:** {REPO} (public, `main` at `{head[0][:7] if head else '?'}`, one commit per hands-on lesson from 2.1; 4.5 has a second commit that fixes a double registration)",
       f'- **Made on {today}** with Rosetta DBT Studio 1.7.6, the white slide theme and the Kokoro voice.\n',
       '## Before you upload\n',
       '- **Listen once** to each video for pronunciation. Claude cannot hear audio.',
       '- Upload the **4K** file to YouTube with its `.srt`. Share the **1080p** copy in chat or by phone.',
       '- Studio 1.7.6 quirks the videos explain on screen: dates show as a day number in 3.2; the change feed of 3.4 shows updates as delete + insert (DuckDB 1.5.2); 4.4 calls show no result rows; 4.5 wraps `ducklake_add_data_files` in `CREATE TEMP TABLE` because the result pane runs a statement twice.',
       '- In 6.1 the lock error shows a local path; that line is blurred in the video.\n',
       '## Files\n',
       '| # | Lesson | Title | Length | 4K file (upload this) | Captions |', '|---|---|---|---|---|---|']
for i, r in enumerate(rows, 1):
    out.append(f"| {i} | {r['n']} | {r['title']} | {mmss(r['d'])} | `{r['name']}/{r['mp4'].name}` ({r['size'] / 1e6:.0f} MB) | `{r['srt'].name}` |")
out += ['', 'Captions, thumbnails (`thumbnail.png`) and slides (`.pptx`) sit in the same lesson folder as the video.', '',
        '## Titles, descriptions and tags', '', 'Copy each block as is. Chapters are inside the descriptions.', '']
for i, r in enumerate(rows, 1):
    out += [f"### {i}. Lesson {r['n']} · {r['title']}", '', f"**Title** ({len(r['yt_title'])} characters)", '', '```text', r['yt_title'], '```', '',
            '**Description**', '', '```text', r['desc'], '```', '', '**Tags**', '', '```text', r['tags'], '```', '']
(C / 'UPLOAD-SHEET.md').write_text('\n'.join(out))

# ---- full course
F = C / 'full-course'; F.mkdir(exist_ok=True)
lst = F / 'list.txt'; lst.write_text(''.join(f"file '{r['mp4']}'\n" for r in rows))
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', str(lst), '-c', 'copy', '-movflags', '+faststart', str(F / 'project-2-full-course.mp4')], check=True)
lst.write_text(''.join(f"file '{r['hd']}'\n" for r in rows))
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', str(lst), '-c', 'copy', '-movflags', '+faststart', str(F / 'project-2-full-course-1080p.mp4')], check=True)
lst.unlink()
# captions with offsets
cues, t0 = [], 0.0
for r in rows:
    blocks = [b for b in r['srt'].read_text().strip().split('\n\n') if b.strip()]
    for b in blocks:
        ls = b.split('\n'); a, z = ls[1].split(' --> ')
        cues.append((parse_srt_t(a) + t0, parse_srt_t(z) + t0, '\n'.join(ls[2:])))
    t0 += r['d']
(F / 'project-2-full-course.srt').write_text('\n\n'.join(f'{i}\n{srt_t(a)} --> {srt_t(z)}\n{x}' for i, (a, z, x) in enumerate(cues, 1)) + '\n')
# chapters
ch, t0 = [], 0.0
for r in rows:
    ch.append(f"{mmss(t0) if t0 >= 3600 or True else ''} {r['n']} {r['title']}"); t0 += r['d']
full = F / 'project-2-full-course.mp4'
yt = ['# YouTube upload: full course (Project 2)', '',
      f"- **File:** `project-2-full-course.mp4` (3840x2160, {mmss(dur(full))}, {full.stat().st_size / 1e6:.0f} MB). The {len(rows)} lesson videos joined in order, without re-encoding.",
      f"- **Phone copy:** `project-2-full-course-1080p.mp4` (1920x1080, {(F / 'project-2-full-course-1080p.mp4').stat().st_size / 1e6:.0f} MB)",
      f'- **Captions:** `project-2-full-course.srt` (English, {len(cues)} cues, times shifted per lesson)',
      '- **Thumbnail:** use `../lesson-0-welcome/thumbnail.png`', '- **Visibility:** unlisted', '', '## Title', '',
      'DuckLake Full Course: an Ethereum data lake in Rosetta DBT Studio (Project 2)', '', '## Description', '',
      'The whole of Project 2 in one video: build a real data lake on your laptop with DuckLake and Rosetta DBT Studio. Three months of Ethereum blocks and a week of transactions from a public S3 bucket; snapshots and time travel; updates, deletes and schema changes without rewriting files; partitioning, statistics and maintenance; the catalog read by hand; and dbt models, tests and docs on top of the lake.', '',
      'Part of the free Data Lakes with DuckLake in Rosetta DBT Studio course on Rosetta Academy: https://academy.rosettadb.io/',
      f'Code for this course (one commit per lesson): {REPO}', 'Download Rosetta DBT Studio: https://rosettadb.io/download-dbtstudio.html',
      'DuckLake documentation: https://ducklake.select/docs/stable/', '', 'Chapters'] + [c.strip() for c in ch] + ['', '## Tags', '',
      'DuckLake, data lake, lakehouse, DuckDB, dbt, Parquet, Ethereum, Rosetta DBT Studio, SQL, time travel, snapshots, full course']
(F / 'youtube.md').write_text('\n'.join(yt) + '\n')
print('total', mmss(total), 'lessons', len(rows), 'full', full.stat().st_size / 1e6, 'MB')
