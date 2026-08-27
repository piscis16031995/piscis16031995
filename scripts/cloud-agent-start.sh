#!/usr/bin/env bash
# Comprobación por arranque: el servidor web vive en terminals, no aquí.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

python3 - <<'PY'
from pathlib import Path

required = ["index.html", "styles.css", "main.js", "html5.html", "ramas.html", "red.html"]
missing = [name for name in required if not Path(name).is_file()]
if missing:
    raise SystemExit(f"Faltan archivos del sitio: {', '.join(missing)}")
print("start ok")
PY
