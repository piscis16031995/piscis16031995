# Documentación — piscis16031995

Repositorio de perfil de GitHub y entorno de trabajo de **Diseño Web Profesional** (HTML, CSS y JavaScript desde 0).

## Origen y sincronización

| Recurso | Valor |
| --- | --- |
| GitHub | https://github.com/piscis16031995/piscis16031995 |
| Rama por defecto | `main` |
| Entorno Cursor | [d626cc30-935d-11f1-ba66-0e7d0216e441](https://cursor.com/dashboard/cloud-agents/environments/e/d626cc30-935d-11f1-ba66-0e7d0216e441) |
| Sitio local | http://localhost:8000 |

Comando de sincronización (fetch + estado, sin force-push):

```bash
./scripts/sync-origin.sh
```

Configuración anti-desfase:

- `.gitattributes` fuerza `eol=lf` en texto.
- `.gitignore` evita commitear `.env`, logs y `.local/`.
- `scripts/cloud-agent-install.sh` hace `git fetch origin --prune` en cada bootstrap del contenedor.
- GitHub Actions comprueba que las páginas responden HTTP 200.

## Ramas ampliadas en carpetas

Cada rama remota tiene carpeta propia con `manifiesto.json`, `Documentacion.md` y archivos históricos únicos:

- [`ramas/main/`](ramas/main/Documentacion.md)
- [`ramas/piscis16031995-patch-1/`](ramas/piscis16031995-patch-1/Documentacion.md) — archivo `HTML5` que no estaba en `main`
- [`ramas/cursor-setup-static-web-env-65a1/`](ramas/cursor-setup-static-web-env-65a1/Documentacion.md)

Inventario: [`ramas/inventario.json`](ramas/inventario.json)

## Red pública (sin copiar código ajeno)

No se extrae código fuente de repositorios de terceros ni de seguidores (copyright y licencia). Sí hay metadatos públicos y enlaces:

- [`red/red.json`](red/red.json)
- [`red/Documentacion.md`](red/Documentacion.md)

Seguidores actuales: **jackjosias**, **T-Stephen**, **Aftaritet1990**. Ninguno abrió ni revisó el PR #1 de este repositorio. Los otros repos propios (`02DATATECHIA1995`, `DevSoftGrupoData`) están vacíos.

## Notificación

El pull request de esta rama notifica en GitHub. El envío por Gmail o Zapier requiere conectar esos servidores MCP en Cursor Desktop (Settings → Tools & MCP). En este Cloud Agent esas conexiones no están autenticadas.

## Cómo trabajar sin conflictos

1. Actualiza `origin` con `./scripts/sync-origin.sh`.
2. No edites `main` a la vez en Cursor Desktop y en un agente sin hacer fetch.
3. Fusiona por PR; no reescribas `main`.
4. Si hay conflicto, resuélvelo en la rama de trabajo y vuelve a sincronizar.
