#!/usr/bin/env bash
# Build one lesson end to end: record (if it has app/browser scenes), voice, stills, compose, package.
#   tools/make_lesson.sh <lesson-folder> [--no-record] [--from tts|stills|compose|package]
set -euo pipefail
C="$(cd "$(dirname "$0")/.." && pwd)"
L="$C/$1"; shift
T="$C/../../_academy-video-tooling"
PY="$T/.cache/venv/bin/python"
REC=1; FROM=record
while [ $# -gt 0 ]; do case "$1" in --no-record) REC=0;; --from) FROM="$2"; shift;; esac; shift; done
cd "$T"
step() { case "$FROM" in record) return 0;; tts) [ "$1" != record ];; stills) [ "$1" != record ] && [ "$1" != tts ];; compose) [ "$1" = compose ] || [ "$1" = package ];; package) [ "$1" = package ];; esac; }
if step record && [ $REC = 1 ] && grep -qE "kind: (app|browser)" "$L/lesson.yaml"; then node record.cjs "$C" "$L"; fi
if step tts; then "$PY" scripts/tts.py "$C" "$L" | tail -1; fi
if step stills; then "$PY" scripts/render_stills.py "$C" "$L" | tail -1; fi
if step compose; then nice -n 10 "$PY" scripts/compose.py "$C" "$L" | tail -1; fi
if step package; then nice -n 10 "$PY" scripts/package.py "$C" "$L" | tail -1; fi
