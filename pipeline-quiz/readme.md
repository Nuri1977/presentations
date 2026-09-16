# Pipeline Playground

A self-contained, human-readable introduction to pipelines in Rosetta DBT
Studio. It explains the concepts in simple language with illustrations,
story-like chapters, and a process diagram.

The page ends with an interactive ten-question quiz containing true/false and
multiple-choice questions, immediate explanations, progress tracking, a score,
and a restart option.

`pipeline-developers.html` is a second route for engineers working on DBT
Studio. It maps the pipeline file contract, renderer/main-process ownership,
authoring lifecycle, Local Runner and Cloud flows, safety boundaries, known
limitations, and the highest-signal source files.

The developer source map opens seven styled HTML chapters under
`developer-docs/`. Raw Markdown and TypeScript files appear only as secondary
source references inside those readable chapters.

## Open the website

Open `pipeline-quiz.html` for the beginner guide or
`pipeline-developers.html` for the developer architecture guide. The pages
link to one another. No build step, web server, external font, or JavaScript
dependency is required.

The pipeline behavior described by the page is based on the DBT Studio `dev`
branch as audited on 2026-09-03.
