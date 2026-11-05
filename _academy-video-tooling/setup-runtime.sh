#!/usr/bin/env bash
# Prepare the pinned recording runtime once per course: Studio's managed CPython + dbt.
# Usage: ./setup-runtime.sh <python_version> <build_tag> <dbt_core_version> <dbt_duckdb_version>
# Example: ./setup-runtime.sh 3.10.17 20250409 1.12.6 1.11.1
set -euo pipefail
cd "$(dirname "$0")"
PYV=${1:-3.10.17}; TAG=${2:-20250409}; DBT=${3:-1.12.6}; DUCK=${4:-1.11.1}
case "$(uname -s)-$(uname -m)" in
  Linux-x86_64) PLAT=x86_64-unknown-linux-gnu ;;
  Darwin-x86_64) PLAT=x86_64-apple-darwin ;;
  Darwin-arm64) PLAT=aarch64-apple-darwin ;;
  *) echo "unsupported platform"; exit 1 ;;
esac
C=.cache; mkdir -p "$C/python"
PYDIR="$C/python/cpython-$PYV-$PLAT"
if [ ! -x "$PYDIR/bin/python3" ]; then
  F="cpython-$PYV+$TAG-$PLAT-install_only.tar.gz"
  curl -sSL -o "$C/python/$F" "https://github.com/astral-sh/python-build-standalone/releases/download/$TAG/$F"
  mkdir -p "$PYDIR" && tar -xzf "$C/python/$F" -C "$PYDIR" --strip-components=1 && rm "$C/python/$F"
fi
rm -rf "$C/dbt-env"
"$PYDIR/bin/python3" -m venv "$C/dbt-env"
"$C/dbt-env/bin/pip" install -q --disable-pip-version-check "dbt-core==$DBT" "dbt-duckdb==$DUCK"
cat > "$C/runtime.json" <<EOF
{"pythonVersion": "$PYV", "pythonBinary": "$(cd "$PYDIR" && pwd)/bin/python3", "dbtVersion": "$DBT", "dbtDuckdbVersion": "$DUCK", "platform": "$PLAT"}
EOF
cat "$C/runtime.json"
"$C/dbt-env/bin/dbt" --version | head -6
