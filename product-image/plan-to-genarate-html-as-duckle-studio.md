# Plan: DBT Studio Product Image HTML

## Goal

Create a single HTML page that renders a 16:9 product announcement image for DBT Studio, inspired by the Duckle v0.5.3 reference image and the local presentation style in `presentations/jaffle-shop-ai-workflow/video-presentation.html`.

The page should be designed so it can be opened in a browser and captured as a high-resolution product image.

## Target Output

- File to create later: `presentations/product-image/dbt-studio-product-image.html`
- Canvas size: `1536px x 1024px` for direct screenshot parity with the Duckle reference, with all key content inside a safe area.
- Visual style: dark product launch poster, orange highlights, crisp UI mockup, feature cards, connector/tool badges, and open-source/GitHub footer.
- Purpose: promotional product image for DBT Studio.

## Source References

- Duckle-style reference image: `/Users/nuri/Downloads/vxl6zatlxfah1.png`
- Local HTML style reference: `presentations/jaffle-shop-ai-workflow/video-presentation.html`
- DBT Studio assets: `dbt-studio/assets`
- Useful app assets:
  - `dbt-studio/assets/logo_sora.png`
  - `dbt-studio/assets/logo_new_01.png`
  - `dbt-studio/assets/icon.png`
  - `dbt-studio/assets/icons/dbt-bit_tm.png`
  - `dbt-studio/assets/icons/duckdb.svg`
  - `dbt-studio/assets/icons/duck-lake.svg`
  - `dbt-studio/assets/icons/git.svg`
  - `dbt-studio/assets/icons/bot.svg`
  - `dbt-studio/assets/connectionIcons/duckdb.png`
  - `dbt-studio/assets/connectionIcons/postgresql.png`
  - `dbt-studio/assets/connectionIcons/snowflake.png`
  - `dbt-studio/assets/connectionIcons/bigquery.png`
  - `dbt-studio/assets/connectionIcons/databricks.png`
  - `dbt-studio/assets/connectionIcons/s3.png`
  - `dbt-studio/assets/connectionIcons/azure_blob.png`
  - `dbt-studio/assets/connectionIcons/cloudflare_r2.png`
  - `dbt-studio/assets/connectionIcons/minio.png`

Optional supporting screenshots from existing presentations:

- `presentations/jaffle-shop-ai-workflow/full-project-editor.png`
- `presentations/ai-agent-sql-editor/sql-editor-ai-panel.png`
- `presentations/ducklake-ui-and-sql-editor-presenation/sql-editor-schema-view.png`
- `presentations/ducklake-ui-and-sql-editor-presenation/sql-editor-query-data.png`
- `presentations/dbt-lineage-dag/dbt-docs-lineage.png`

## Main Message

Hero headline:

```text
DBT Studio is live.
```

Alternative if version is known:

```text
DBT Studio v0.x is live.
```

Short description:

```text
DBT Studio is the local-first, open-source workspace for building, running, and understanding dbt projects with AI, SQL, lineage, Git, and lakehouse tooling in one desktop app.
```

Top-right badge:

```text
WHAT'S NEW
AI + dbt workflow
```

## Layout

Use a single full-screen poster layout, not a slideshow.

### 1. Background

- Dark near-black background: `#05070b`.
- Subtle grid texture similar to the Duckle image.
- Orange glow in the upper-left and lower-right corners.
- Muted blue/cyan glow behind the product UI mockup, but keep orange as the dominant accent.
- No decorative blobs that look disconnected from the product; glows should support depth only.

### 2. Header / Brand

Top-left:

- Use DBT Studio logo asset, preferably `logo_sora.png` or `logo_new_01.png`.
- If the logo image is too wide, render app icon plus text:

```text
DBT Studio
```

Top-right:

- Orange bordered announcement badge:

```text
WHAT'S NEW
AI + dbt workflow
```

### 3. Hero Copy

Left column, similar to Duckle:

```text
DBT Studio is live.
```

Use white text for `DBT Studio` and orange gradient for `is live.` or the version phrase.

Subtitle:

```text
The local-first, open-source workspace for dbt projects: model editing, SQL exploration, AI agent workflows, lineage, Git, and warehouse connections in one desktop app.
```

### 4. Product UI Mockup

Right side:

Build a polished fake-but-believable DBT Studio app window using HTML/CSS, optionally overlaid with real screenshots.

Mockup should include:

- App title bar with DBT Studio mark.
- Left sidebar with navigation:
  - Projects
  - SQL
  - AI Agent
  - Lineage
  - Cloud Explorer
  - Settings
- Main editor area:
  - File tree for `models/staging`, `models/marts`, `schema.yml`
  - Monaco-like SQL editor panel with dbt model SQL.
  - Right AI Agent panel showing a compact workflow:

```text
Analyze project
Generate staging models
Run dbt compile
Explain lineage impact
```

- Bottom result table or terminal strip:

```text
dbt compile completed
12 models, 18 tests, 0 errors
```

Use orange active states, dark panels, and green success dots.

### 5. Feature Cards

Create an 8-card grid below the hero, matching Duckle's bordered cards.

Each card has an icon, orange title, and short body copy.

Cards:

1. **AI Agent for dbt**
   ```text
   Ask the agent to create models, explain SQL, update YAML, run dbt commands, and reason over your project context.
   ```

2. **Project-aware SQL editor**
   ```text
   Write SQL with schema browsing, autocomplete, saved queries, query results, and export workflows.
   ```

3. **Visual dbt lineage**
   ```text
   Trace models, sources, exposures, and downstream impact before you change production logic.
   ```

4. **Local-first desktop workflow**
   ```text
   Work with projects, profiles, credentials, DuckDB, and local files without moving your development loop to the browser.
   ```

5. **Git built in**
   ```text
   Review local changes, manage branches, commit work, and keep dbt project changes close to the editor.
   ```

6. **Cloud Explorer**
   ```text
   Browse S3, Azure Blob, GCS, R2, MinIO, and compatible storage with DuckDB-powered previews.
   ```

7. **DuckDB + DuckLake ready**
   ```text
   Explore local analytics, lakehouse tables, schemas, snapshots, and data previews from one workspace.
   ```

8. **Multi-provider AI**
   ```text
   Use OpenAI, Anthropic, Gemini, Ollama, LM Studio, and OpenAI-compatible providers with project context.
   ```

### 6. Capability Bar

Below the feature cards, add a horizontal capability bar with icon+text items:

```text
dbt Models | SQL Editor | AI Agent | Data Lineage | Cloud Explorer | Git | DuckDB | Notebooks | Saved Queries
```

### 7. Integrations / Footer

Bottom row should feel like Duckle's logo strip.

Left box:

```text
100% open source
local-first dbt development
```

Middle integrations:

```text
dbt | DuckDB | PostgreSQL | Snowflake | BigQuery | Databricks | S3 | Azure Blob | R2 | MinIO
```

Right GitHub box:

```text
github.com/Adaptivescale/dbt-studio
```

If the exact public repo URL differs, keep the text generic:

```text
Available on GitHub
```

Bottom hashtags:

```text
#dbt #DataEngineering #AnalyticsEngineering #AI #SQL #DuckDB #DataLineage #OpenSource #LocalFirst
```

## Visual Rules

- Keep the design dense but readable, like a product launch graphic.
- Use orange borders and highlights, but avoid making the whole image a single orange theme; add neutral dark panels, white text, muted gray copy, small green success indicators, and a few blue/cyan storage/warehouse accents.
- Cards should use `border-radius: 8px` or less.
- Use stable dimensions so the image captures cleanly at 1536x1024.
- Avoid large instructional text. The image should feel like a finished product poster, not a how-to page.
- Use actual image assets from `dbt-studio/assets` for brand and connector logos.
- Use inline CSS in the HTML file, like the jaffle workflow presentation.
- Prefer CSS-drawn UI panels and icons for the mock app window where real screenshots do not fit cleanly.

## Suggested HTML Structure

```html
<main class="poster">
  <section class="hero">
    <header class="brand-row">...</header>
    <div class="hero-copy">...</div>
    <div class="product-window">...</div>
  </section>

  <section class="feature-grid">...</section>

  <section class="capability-bar">...</section>

  <footer class="footer-strip">...</footer>
</main>
```

## Screenshot / Export Notes

Open the HTML in a browser at `1536x1024`, then capture the viewport.

If using Playwright later:

```bash
npx playwright screenshot --viewport-size=1536,1024 presentations/product-image/dbt-studio-product-image.html presentations/product-image/dbt-studio-product-image.png
```

If local file screenshots have path issues, run a small static server from the repo root and capture:

```bash
python3 -m http.server 4173
```

Then open:

```text
http://localhost:4173/presentations/product-image/dbt-studio-product-image.html
```

## Acceptance Criteria

- The HTML renders as a single complete product image with no scrolling required at `1536x1024`.
- Brand, headline, product mockup, eight feature cards, capability bar, and footer are visible.
- DBT Studio assets load from `dbt-studio/assets`.
- Text does not overlap at the target viewport size.
- The result is visually similar in density and hierarchy to the Duckle reference, while clearly branded as DBT Studio.
