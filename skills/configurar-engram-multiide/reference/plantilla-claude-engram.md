## Engram (memoria persistente)

Namespace: `PROJECT_NAME`. Siempre pasar `project: PROJECT_NAME` en tools Engram.

### Reglas de uso proactivo

- Llamar `mem_context` al inicio de cada sesión con `project: PROJECT_NAME`.
- Guardar con `mem_save` inmediatamente tras decisiones, bugs resueltos, patrones o configuraciones relevantes.
- Formato obligatorio en `mem_save`:
  - `**What**: ...`
  - `**Why**: ...`
  - `**Where**: rutas/archivos`
  - `**Learned**: ...` (opcional)
- Buscar con `mem_search` antes de implementar algo que pudo haberse resuelto antes.
- `mem_session_summary` obligatorio al cerrar sesión de trabajo significativa.
- Pasar siempre `project: PROJECT_NAME` en `mem_search`, `mem_context` y `mem_save`.

### Herramientas MCP disponibles

| Tool | Cuándo usarla |
|------|--------------|
| `mem_current_project` | Detectar proyecto activo al inicio |
| `mem_context` | Recuperar contexto reciente |
| `mem_search` | Buscar decisiones, bugs, patrones previos |
| `mem_save` | Guardar decisiones, bugs, configuraciones |
| `mem_session_summary` | Resumen al cerrar sesión |
| `mem_get_observation` | Contenido completo de una obs por ID |

> MCP configurado con: `claude mcp add -s user engram -- /opt/homebrew/bin/engram mcp --tools=agent`
