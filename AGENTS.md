# Cursor Cloud — piscis16031995

Sitio estático (HTML/CSS/JS) servido con Python. El origen Git es `https://github.com/piscis16031995/piscis16031995`.

## Arranque local / Cloud Agent

1. `./scripts/cloud-agent-install.sh` — comprueba Python, hace `git fetch origin --prune` y escribe `.local/sync-status.json`.
2. `./scripts/cloud-agent-start.sh` — verifica que existan las páginas del sitio.
3. Terminal `web`: `python3 -m http.server 8000 --bind 0.0.0.0` → http://localhost:8000

Para alinear el clon con GitHub sin reescribir historial:

```bash
./scripts/sync-origin.sh
```

## Sincronización Cursor ↔ Git ↔ GitHub

- Trabaja en una rama `cursor/piscis16031995/<nombre>-4043` (o el sufijo que asigne el agente).
- Haz `git fetch origin --prune` antes de merge/rebase.
- No uses `git push --force` sobre `main`.
- Los finales de línea están normalizados a LF en `.gitattributes` para evitar diffs falsos entre Cursor (Windows/macOS) y el contenedor Linux.

## Comprobaciones

- GitHub Actions: `.github/workflows/sync-check.yml`
- Manual: abrir Inicio, HTML5, Ramas y Red, y pulsar **Empezar ahora**.
