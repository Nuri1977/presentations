#!/usr/bin/env bash
# Build lessons listed (space separated) in a queue file, one at a time, until the file is empty.
#   tools/build_queue.sh <queue-file>
Q="$1"; cd "$(dirname "$0")/.."
while pgrep -f "make_lesson.sh" >/dev/null; do sleep 20; done
while true; do
  l=$(awk '{print $1}' "$Q"); [ -z "$l" ] && break
  echo "== $l $(date +%H:%M)"; tools/make_lesson.sh "$l" --no-record 2>&1 | tail -2
  awk '{$1=""; sub(/^ /,""); print}' "$Q" > "$Q.tmp" && mv "$Q.tmp" "$Q"
done
echo "queue empty $(date +%H:%M)"
