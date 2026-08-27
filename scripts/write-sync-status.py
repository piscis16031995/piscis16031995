#!/usr/bin/env python3
"""Escribe el estado de sincronización Git/GitHub en .local/sync-status.json."""

from __future__ import annotations

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path


def run(args: list[str]) -> str:
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return (result.stdout or result.stderr or "").strip()


def redact(value: str) -> str:
    if "://" in value and "@" in value:
        scheme, rest = value.split("://", 1)
        host = rest.split("@", 1)[-1]
        return f"{scheme}://{host}"
    return value


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    out_dir = root / ".local"
    out_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "branch": run(["git", "rev-parse", "--abbrev-ref", "HEAD"]),
        "sha": run(["git", "rev-parse", "HEAD"]),
        "upstream": run(
            ["git", "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}"]
        )
        if subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}"],
            capture_output=True,
        ).returncode
        == 0
        else "",
        "status": run(["git", "status", "-sb"]),
        "origin_url": redact(run(["git", "remote", "get-url", "origin"])),
        "ahead_behind": run(
            ["git", "rev-list", "--left-right", "--count", "HEAD...origin/main"]
        ),
        "remote_branches": run(["git", "branch", "-r"]).splitlines(),
        "python": run(["python3", "--version"]),
    }
    path = out_dir / "sync-status.json"
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
