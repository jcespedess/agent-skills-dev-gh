# Extensión de Stack

Esta es una versión extendida de [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills)
con skills y comandos específicos del stack del proyecto, manteniendo intacta la base original.

## Skills de stack agregadas (`skills/`)

| Skill | Tipo | Estado |
|-------|------|--------|
| `react-frontend` | Frontend | 🟢 Nueva |
| `vue-frontend` | Frontend | 🟢 Nueva |
| `angular-frontend` | Frontend | 🔄 Adaptada de v1.7 interna |
| `nodejs-backend` | Backend | 🔄 Adaptada de v1.7 interna |
| `springboot-backend` | Backend | 🔄 Adaptada de v1.7 interna (Maven · Java 21 · 3.5 · sin Gradle) |
| `python-backend` | Backend | 🔄 Adaptada de v1.7 interna (FastAPI/Django, no-ADK) |
| `go-backend` | Backend | 🟢 Nueva |
| `python-google-adk` | Backend / Agentes | 🟢 Nueva (ADK 2.0) |

Cada skill sigue la anatomía del repo: `frontmatter` → Overview → When to Use → Process → Common Rationalizations → Red Flags → Verification. Todas delegan los specifics de versión a `source-driven-development` (no hardcodean APIs).

## Comandos de stack agregados (`.claude/commands/`)

Cada comando compone su skill de stack con las skills del proceso (incremental + TDD + diseño/seguridad/accesibilidad según corresponda). Aceptan `$ARGUMENTS` para describir qué construir.

| Comando | Compone |
|---------|---------|
| `/scaffold-react` | react-frontend + frontend-ui-engineering + incremental + tdd |
| `/scaffold-vue` | vue-frontend + frontend-ui-engineering + incremental + tdd |
| `/scaffold-angular` | angular-frontend + frontend-ui-engineering + incremental + tdd |
| `/scaffold-node` | nodejs-backend + api-and-interface-design + security + incremental + tdd |
| `/scaffold-springboot` | springboot-backend + api-and-interface-design + security + incremental + tdd |
| `/scaffold-python` | python-backend + api-and-interface-design + security + incremental + tdd |
| `/scaffold-go` | go-backend + api-and-interface-design + security + incremental + tdd |
| `/scaffold-adk` | python-google-adk + python-backend + api-and-interface-design + incremental + tdd |

## Notas
- **Claude Code:** skills y comandos se auto-descubren (skills/ y .claude/commands/). Sin cambios al manifiesto.
- **Gemini / Antigravity:** las skills funcionan tal cual (son harness-agnósticas). Para tener los comandos, replica cada `scaffold-*.md` como `.toml` en `.gemini/commands/` y `commands/` con el mismo cuerpo.
- **Cursor / otros:** copia los `SKILL.md` de stack a `.cursor/rules/` bajo demanda.
