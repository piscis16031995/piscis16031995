#!/usr/bin/env bash
# Bootstrap idempotente del entorno Cloud Agent.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

python3 --version
test -f index.html
test -f styles.css
test -f main.js
test -f .cursor/environment.json

if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  git remote get-url origin | sed -E 's#https://[^/@]+@#https://#'
  git fetch origin --prune
  git status -sb
fi

python3 "$ROOT/scripts/write-sync-status.py"
echo "install ok"
