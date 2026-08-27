# Ramas del repositorio

Esta carpeta **amplía cada rama remota** en un directorio con JSON, documentación y archivos que esa rama aportó.

No sustituye a Git: las ramas reales siguen en `origin`. Aquí hay un inventario legible para Cursor, revisores y el sitio estático.

| Carpeta | Rama Git | Notas |
| --- | --- | --- |
| `main/` | `main` | Rama publicada. Sitio estático + entorno Cloud Agent. |
| `piscis16031995-patch-1/` | `piscis16031995-patch-1` | 1 commit por delante de `main` (`Create HTML5`). 2 commits por detrás. |
| `cursor-setup-static-web-env-65a1/` | `cursor/piscis16031995/setup-static-web-env-65a1` | Rama del PR #1, ya fusionada; 1 merge commit por detrás de `main`. |

Archivo maestro: [`inventario.json`](inventario.json)
