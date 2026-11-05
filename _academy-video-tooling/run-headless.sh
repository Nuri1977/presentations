#!/usr/bin/env bash
# Run a Node script under a virtual display with a disposable keyring (Linux runner).
# Usage: ./run-headless.sh <script.cjs> [args...]
set -euo pipefail
cd "$(dirname "$0")"
DISPLAY_NUM=${DISPLAY_NUM:-97}
Xvfb ":$DISPLAY_NUM" -screen 0 4000x2300x24 -nolisten tcp >/dev/null 2>&1 &
XVFB_PID=$!
trap 'kill $XVFB_PID 2>/dev/null || true' EXIT
sleep 1.5
export DISPLAY=":$DISPLAY_NUM"
# keytar needs a Secret Service; gnome-keyring gives a throwaway one.
dbus-run-session -- bash -c '
  eval "$(printf "\n" | gnome-keyring-daemon --unlock --components=secrets 2>/dev/null)" || true
  export GNOME_KEYRING_CONTROL GNOME_KEYRING_PID
  node "$@"
' _ "$@"
