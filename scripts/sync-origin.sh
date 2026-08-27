#!/usr/bin/env bash
# Sincroniza el clon local con origin sin reescribir historial.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

git remote -v | sed -E 's#https://[^/@]+@#https://#'
git fetch origin --prune
git status -sb

if git show-ref --verify --quiet refs/remotes/origin/main; then
  echo "Comparación con origin/main:"
  git rev-list --left-right --count HEAD...origin/main || true
  git log --oneline --decorate --graph --max-count=12 --all
fi

python3 "$ROOT/scripts/write-sync-status.py"
echo "sync ok"
