# Project 2 production tracker

Lessons are produced in course order. App lessons start from the previous lesson's push to
`github.com/Nuri1977/ethereum-ducklake-dbt`, so they must be recorded one after another.

Pipeline per lesson (from `_academy-video-tooling/`):
`record.cjs` (app/browser scenes) → `tts.py` → `render_stills.py` → `compose.py` → `package.py`.
Helper: `tools/make_lesson.sh <lesson-folder> [--no-record]`.

Lesson SQL is rehearsed first with `tools/rehearse.py` (scratch lake, local cache instead of S3).
Each hands-on lesson keeps its script in `snippets/<n>/`; the next lessons' start states rebuild the lake
from those scripts (`lake:` in `states/<name>/recipe.yaml`).

| # | Folder | Status |
|---|---|---|
| 0 | lesson-0-welcome | done |
| 0.1 | lesson-0-1-install | done |
| 1.1 | lesson-1-1-lakehouse | done |
| 1.2 | lesson-1-2-parquet | done |
| 1.3 | lesson-1-3-table-formats | done |
| 1.4 | lesson-1-4-how-ducklake-works | done |
| 1.5 | lesson-1-5-ethereum-data | done |
| 1.6 | lesson-1-6-under-the-hood | done |
| 2.1 | lesson-2-1-create-ducklake | done |
| 2.2 | lesson-2-2-load-blocks | done |
| 2.3 | lesson-2-3-look-inside | done |
| 2.4 | lesson-2-4-snapshots | done |
| 2.5 | lesson-2-5-time-travel | done |
| 3.1 | lesson-3-1-insert-update-delete | done |
| 3.2 | lesson-3-2-daily-loads | done |
| 3.3 | lesson-3-3-schema-evolution | done |
| 3.4 | lesson-3-4-change-feed | done |
| 3.5 | lesson-3-5-transactions | done |
| 4.1 | lesson-4-1-partitioning | done |
| 4.2 | lesson-4-2-sorted-tables | done |
| 4.3 | lesson-4-3-data-inlining | done |
| 4.4 | lesson-4-4-maintenance | done |
| 4.5 | lesson-4-5-adding-files | done |
| 5.1 | lesson-5-1-catalog-snapshots | done |
| 5.2 | lesson-5-2-catalog-files | done |
| 5.3 | lesson-5-3-read-by-hand | done |
| 6.1 | lesson-6-1-connect-dbt | done |
| 6.2 | lesson-6-2-staging | done |
| 6.3 | lesson-6-3-marts | done |
| 6.4 | lesson-6-4-tests-docs | done |
| 7.1 | lesson-7-1-going-further | done |
| pkg | UPLOAD-SHEET.md, full-course/ | done (31 videos, 1:15:13; full course 707 MB 4K, 187 MB 1080p) |

Notes:
- Start-state lakes are built with DuckDB 1.5.2 (`_academy-video-tooling/.cache/seed-env`), the version inside Studio, from 3.4 on. Lessons 2.2 to 3.4 were recorded on lakes built by 1.5.6; nothing visible differs except the change feed (3.4, narration explains).
- Build queue: `tools/build_queue.sh <queue-file>` renders recorded lessons one after another.
- All 31 lessons recorded on 12 Nov 2026; repo main ends at "Tests and docs" (6.4). Render status: a lesson is done when its folder has `lesson-<n>.mp4`, `-1080p.mp4`, `.srt` and `youtube.md`.
- 12 Nov 2026: all 31 lessons rendered and packaged. Narration corrected after the dbt DuckLake review (3.5, 6.1, 6.3, 6.4).
