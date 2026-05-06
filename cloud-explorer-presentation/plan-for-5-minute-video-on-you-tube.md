# 5-Minute YouTube Video Plan: Rosetta DBT studio — Cloud Explorer

## Goal

Create a polished 5-minute YouTube product video that promotes Rosetta DBT studio's **Cloud Explorer** — a unified desktop interface for browsing, managing, and previewing data from seven cloud storage providers using DuckDB.

The video should feel like a high-quality SaaS product demo: clear, practical, energetic, and visually grounded in real screenshots. Use the provided screenshots from:

`presentations/cloud-explorer-presentation/`

Reuse the logo and provider icons from:

`presentations/ducklake-ui-and-sql-editor-presenation/`

## Core Message

Rosetta DBT studio's Cloud Explorer connects to AWS S3, Azure Blob Storage, Google Cloud Storage, MinIO, Cloudflare R2, Backblaze B2, and rustfs from one desktop workspace. Teams can browse buckets and files, upload and manage objects, and preview CSV, Parquet, JSON, AVRO, and Excel files with DuckDB-powered queries — including server-side pagination, filter builder, schema inspection, and column statistics — without leaving the app.

## Audience

Data engineers, analytics engineers, cloud data teams, and technical founders who work with cloud object storage and need a fast, local-first desktop tool to explore and validate cloud data files.

## Tone And Style

- Professional, modern, confident, and practical.
- Fast enough to feel engaging, but not rushed.
- Use real UI screenshots as the primary visual evidence.
- Add subtle zooms, pans, cursor highlights, and callout labels.
- Use clean typography and short on-screen text.
- Avoid generic stock imagery except for abstract background moments between sections.
- Music: modern technology beat, warm, minimal, not overpowering.
- Voice: clear, calm, optimistic, technical but accessible.

## Visual Brand Direction

- Primary brand asset: `logo_new_05.png` (from ducklake-ui-and-sql-editor-presenation)
- Use dark UI-friendly backgrounds, soft shadows, and orange accent highlights inspired by the logo.
- Keep screenshots crisp and readable.
- Use full-screen product shots whenever possible.
- Use animated overlays for key words such as "Cloud Explorer", "DuckDB Preview", "Server-Side Pagination", "Filter Builder", "Schema Inspection", and "Statistics".

## Required Assets

Provider icons (from `connectionIcons/`):

- `s3.png`, `azure.png`, `googlecloud.png`, `minio.png`, `cloudflare_r2.png`, `blackbaze.png`, `rustfs.png`

Screenshots (from `cloud-explorer-presentation/`):

- `dashboard.png`
- `cloud-source-connetions.png`
- `new-connection-form.png`
- `cloud-buckets-list.png`
- `cloud-buckets-list-create-new-bucket.png`
- `cloud-files-list-inside-a-bucket.png`
- `upload-files-to-bukcet.png`
- `create-rename-delete-folders-and-files.png`
- `recent-items-visited.png`
- `duckdb-preview-SCV-Paruet-AVRO-JSON-EXCEL.png`
- `ducdb-preview-data-table.png`
- `duckdb-preview-full-screen.png`
- `duckdb-preview-schema.png`
- `duckdb-preview-statitics.png`
- `duckdb-preview-filters-form.png`
- `duckdb-preview-filtered-data-2.png`

---

## Video Structure

### 0:00–0:20 — Hook: One Workspace for All Cloud Storage

**Visuals**

- Open with `logo_new_05.png` centered on a dark background.
- Quick cuts of `dashboard.png`, `duckdb-preview-SCV-Paruet-AVRO-JSON-EXCEL.png`, and `duckdb-preview-full-screen.png`.
- Kinetic text overlays: "AWS S3", "Azure Blob", "GCS", "MinIO", "Cloudflare R2", "Backblaze B2", "rustfs".

**Voiceover**

"Meet the Cloud Explorer in Rosetta DBT studio: one desktop workspace to connect, browse, manage, and preview data from every major cloud storage provider. No extra tools. No context switching."

**On-Screen Text**

"Rosetta DBT studio: Cloud Explorer — 7 providers, DuckDB previews, one workspace"

---

### 0:20–0:50 — The Problem: Cloud Data Is Fragmented

**Visuals**

- Show `cloud-source-connetions.png`.
- Animate provider icons across the screen converging into the Rosetta DBT studio logo.

**Voiceover**

"Data teams juggle multiple cloud storage providers, each with its own console, its own access patterns, and its own way of browsing files. Rosetta DBT studio's Cloud Explorer solves this by connecting all seven providers — S3, Azure Blob, GCS, MinIO, Cloudflare R2, Backblaze B2, and rustfs — into one unified interface."

**On-Screen Text**

"Less cloud console switching. More productive data work."

---

### 0:50–1:25 — Connections: Seven Providers, One Form

**Visuals**

- Show `new-connection-form.png`.
- Highlight the provider dropdown, credential fields, and "Test Connection" button.
- Animate callout: "Credentials stored securely in system keychain".

**Voiceover**

"Adding a cloud connection is straightforward. Select the provider, fill in the credentials, and test the connection before saving. All sensitive credentials are stored securely in the system keychain — never in plain text. Connections are reusable across the entire workspace."

**On-Screen Text**

"Secure. Reusable. One-time setup."

---

### 1:25–2:00 — Browsing: Buckets, Folders, and Files

**Visuals**

- Show `cloud-buckets-list.png` — card view.
- Show `cloud-files-list-inside-a-bucket.png` — breadcrumb navigation.
- Animate: file-type icons, pagination controls, search box.

**Voiceover**

"Once connected, Cloud Explorer lets you navigate buckets and files just like a desktop file browser. Toggle between card and list view, use breadcrumbs to go deeper into folder hierarchies, and search within large directories. File types are automatically detected and shown with distinct icons."

**On-Screen Text**

"Browse buckets and files like a native desktop app."

---

### 2:00–2:25 — File Management: Upload, Create, Rename, Delete

**Visuals**

- Show `cloud-buckets-list-create-new-bucket.png`.
- Show `upload-files-to-bukcet.png`.
- Show `create-rename-delete-folders-and-files.png`.

**Voiceover**

"Cloud Explorer is not read-only. Create new buckets, upload files, create folders, rename objects, and delete files — all from the same interface, across any connected provider."

**On-Screen Text**

"Full file management. No cloud console required."

---

### 2:25–2:50 — Recent Items and Quick Navigation

**Visuals**

- Show `recent-items-visited.png`.
- Highlight file vs. directory filtering and quick access links.

**Voiceover**

"The Recent Items view tracks the last fifty locations you accessed. Filter between files and directories for quick lookup, and jump back to any recent location with a single click."

**On-Screen Text**

"Your recently visited cloud locations, always one click away."

---

### 2:50–3:30 — DuckDB Preview: Any Format, No Download

**Visuals**

- Show `duckdb-preview-SCV-Paruet-AVRO-JSON-EXCEL.png` — format badge callouts.
- Show `ducdb-preview-data-table.png` — paginated table view with rows-per-page selector.
- Add callouts: "CSV", "Parquet", "JSON", "AVRO", "Excel", "Server-side LIMIT/OFFSET", "200M+ rows".

**Voiceover**

"The real power of Cloud Explorer is DuckDB-powered data preview. Click any supported file and Rosetta DBT studio queries it directly in the cloud using DuckDB. CSV, Parquet, JSON, JSONL, AVRO, and Excel files are all supported. True server-side pagination means only the current page of rows is loaded — so you can preview files with hundreds of millions of rows without exhausting memory."

**On-Screen Text**

"DuckDB previews — no download. Parquet, CSV, JSON, AVRO, Excel."

---

### 3:30–4:00 — Schema, Statistics, and Filter Builder

**Visuals**

- Show `duckdb-preview-schema.png` — column names, types, nullability.
- Show `duckdb-preview-statitics.png` — null count, distinct, min, max, mean.
- Show `duckdb-preview-filters-form.png` — condition builder rows.
- Show `duckdb-preview-filtered-data-2.png` — filtered results with "Filtered" chip.

**Voiceover**

"The full-screen modal adds a Schema tab to inspect column names, types, and nullability — straight from file metadata for Parquet. The Statistics tab computes null count, distinct values, min, max, and mean per column using a ten-thousand-row DuckDB sample. And the Filter Builder lets you construct WHERE clause conditions without writing SQL: pick a column, choose an operator, type a value, and apply."

**On-Screen Text**

"Schema · Statistics · Visual filter builder — all DuckDB-powered."

---

### 4:00–4:40 — Closing: Cloud Explorer at Full Speed

**Visuals**

- Fast montage of the strongest screenshots:
  - `cloud-buckets-list.png`
  - `duckdb-preview-SCV-Paruet-AVRO-JSON-EXCEL.png`
  - `duckdb-preview-statitics.png`
  - `duckdb-preview-filters-form.png`
- End on the CTA screen: `logo_new_05.png`, "Ready to explore your cloud data?", download buttons.

**Voiceover**

"Rosetta DBT studio's Cloud Explorer brings seven cloud providers, DuckDB-powered file previews, server-side pagination, visual filter builder, schema inspection, and column statistics into one cohesive desktop workspace. Download Rosetta DBT studio for macOS, Windows, or Linux today, and star us on GitHub. Let's build better data workflows together."

**On-Screen Text**

"Ready to explore your cloud data? Download Rosetta DBT studio for macOS, Windows, and Linux. Star us on GitHub."

---

## Full Voiceover Script

Meet the Cloud Explorer in Rosetta DBT studio: one desktop workspace to connect, browse, manage, and preview data from every major cloud storage provider. No extra tools. No context switching.

Data teams juggle multiple cloud storage providers, each with its own console, its own access patterns, and its own way of browsing files. Rosetta DBT studio's Cloud Explorer solves this by connecting all seven providers — S3, Azure Blob, GCS, MinIO, Cloudflare R2, Backblaze B2, and rustfs — into one unified interface.

Adding a cloud connection is straightforward. Select the provider, fill in the credentials, and test the connection before saving. All sensitive credentials are stored securely in the system keychain — never in plain text. Connections are reusable across the entire workspace.

Once connected, Cloud Explorer lets you navigate buckets and files just like a desktop file browser. Toggle between card and list view, use breadcrumbs to go deeper into folder hierarchies, and search within large directories. File types are automatically detected and shown with distinct icons.

Cloud Explorer is not read-only. Create new buckets, upload files, create folders, rename objects, and delete files — all from the same interface, across any connected provider.

The Recent Items view tracks the last fifty locations you accessed. Filter between files and directories for quick lookup, and jump back to any recent location with a single click.

The real power of Cloud Explorer is DuckDB-powered data preview. Click any supported file and Rosetta DBT studio queries it directly in the cloud using DuckDB. CSV, Parquet, JSON, JSONL, AVRO, and Excel files are all supported. True server-side pagination means only the current page of rows is loaded — so you can preview files with hundreds of millions of rows without exhausting memory.

The full-screen modal adds a Schema tab to inspect column names, types, and nullability — straight from file metadata for Parquet. The Statistics tab computes null count, distinct values, min, max, and mean per column using a ten-thousand-row DuckDB sample. And the Filter Builder lets you construct WHERE clause conditions without writing SQL: pick a column, choose an operator, type a value, and apply.

Rosetta DBT studio's Cloud Explorer brings seven cloud providers, DuckDB-powered file previews, server-side pagination, visual filter builder, schema inspection, and column statistics into one cohesive desktop workspace. Download Rosetta DBT studio for macOS, Windows, or Linux today, and star us on GitHub. Let's build better data workflows together.

---

## AI Video Generator Prompt

Create a 5-minute YouTube product video promoting Rosetta DBT studio's Cloud Explorer. Use the provided image assets as the primary visuals. The video must include professional narration, modern technology background music, subtle UI zooms, cursor highlights, clean callout labels, and short on-screen text.

Style: polished SaaS product demo, dark modern interface, orange accent highlights matching the Rosetta DBT studio logo, crisp readable screenshots, smooth transitions, confident but practical tone. Avoid generic stock footage unless used only as subtle abstract transitions. Do not invent UI screens; use the supplied screenshots.

Use this structure:

1. 0:00–0:20: Open with `logo_new_05.png`, then quick montage of `dashboard.png`, `duckdb-preview-SCV-Paruet-AVRO-JSON-EXCEL.png`, and `duckdb-preview-full-screen.png`. Kinetic text: "7 providers, DuckDB previews, one workspace."
2. 0:20–0:50: Show the problem of fragmented cloud storage using `cloud-source-connetions.png`. Animate provider icons converging. On-screen text: "Less cloud console switching."
3. 0:50–1:25: Show `new-connection-form.png`. Highlight credential fields, test button, and keychain security note. On-screen text: "Secure. Reusable. One-time setup."
4. 1:25–2:00: Show `cloud-buckets-list.png` and `cloud-files-list-inside-a-bucket.png`. Highlight card/list toggle, breadcrumbs, search, and file-type icons.
5. 2:00–2:25: Show `cloud-buckets-list-create-new-bucket.png`, `upload-files-to-bukcet.png`, and `create-rename-delete-folders-and-files.png`. On-screen text: "Full file management. No cloud console required."
6. 2:25–2:50: Show `recent-items-visited.png`. Highlight filter and quick navigation. On-screen text: "Recently visited, one click away."
7. 2:50–3:30: Show `duckdb-preview-SCV-Paruet-AVRO-JSON-EXCEL.png` and `ducdb-preview-data-table.png`. Add callouts for format badges, rows-per-page, and server-side pagination.
8. 3:30–4:00: Show `duckdb-preview-schema.png`, `duckdb-preview-statitics.png`, `duckdb-preview-filters-form.png`, and `duckdb-preview-filtered-data-2.png`. Callouts: Schema tab, Statistics tab, Filter Builder, Filtered chip.
9. 4:00–4:40: Fast montage of `cloud-buckets-list.png`, `duckdb-preview-SCV-Paruet-AVRO-JSON-EXCEL.png`, `duckdb-preview-statitics.png`, `duckdb-preview-filters-form.png`. End on CTA screen: `logo_new_05.png`, "Ready to explore your cloud data?", download buttons, "Star us on GitHub."

Use the full voiceover script from this plan. Time the visuals to match the narration. Ensure all screenshot text remains readable. Use subtle camera movements: slow zoom in, pan, crop to important UI areas.

---

## Thumbnail Concept

Use `logo_new_05.png` on the left and a collage of `duckdb-preview-SCV-Paruet-AVRO-JSON-EXCEL.png`, `duckdb-preview-filters-form.png`, and `cloud-buckets-list.png` on the right.

**Thumbnail text:** "Cloud Explorer in Rosetta DBT studio"

**Supporting text:** "7 Providers · DuckDB Preview · Filter Builder"

---

## YouTube Metadata Draft

**Title**

Rosetta DBT studio Cloud Explorer: Browse, Preview, and Query Cloud Files with DuckDB

**Description**

See how Rosetta DBT studio's Cloud Explorer connects to AWS S3, Azure Blob Storage, Google Cloud Storage, MinIO, Cloudflare R2, Backblaze B2, and rustfs from one desktop app. Browse buckets and files, upload and manage objects, and preview CSV, Parquet, JSON, AVRO, and Excel files with DuckDB — including server-side pagination, visual filter builder, schema inspection, and column statistics.

Download Rosetta DBT studio for macOS, Windows, or Linux and start exploring your cloud data today.

GitHub: https://github.com/rosettadb/dbt-studio

**Tags**

Rosetta DBT studio, Cloud Explorer, DuckDB, AWS S3, Azure Blob Storage, Google Cloud Storage, MinIO, Cloudflare R2, Backblaze B2, rustfs, cloud storage, data preview, Parquet, CSV, JSON, AVRO, data engineering, analytics engineering, desktop app
