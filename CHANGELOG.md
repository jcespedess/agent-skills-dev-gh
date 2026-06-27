# Changelog

Todos los cambios notables de este proyecto se documentan aquí.
Formato basado en [Keep a Changelog](https://keepachangelog.com/es/1.0.0/), versionado con [SemVer](https://semver.org/lang/es/).

---

## [1.1.0] - 2026-06-27

### Añadido

- Catálogo completo de skills de ingeniería de producción: ciclo de vida (spec, plan, build, test, review, ship) y extensiones de stack (Angular, React, Vue, Node.js, Spring Boot, Python/FastAPI, Go, Google ADK)
- Comandos slash en `.claude/commands/`, `.gemini/commands/` y `commands/` (incluye scaffold por stack)
- Subagentes en `agents/`, hooks de sesión, referencias, ejemplo `examples/login-api`, validador `scripts/validate-skills.js` y workflow CI en `.github/workflows/`
- Configuración Engram (`.engram/`, `.cursor/rules/engram.mdc`) con namespace `agent-skills-dev-gh`
- Guía de análisis en `docs/guias/agent-skills-dev-analysis.md`

### Cambiado

- README y documentación principal orientada a uso genérico (sin referencias organizacionales)
- `STACK-EXTENSIONS.md` como documento de extensiones de stack del proyecto
- Datos de ejemplo y URLs de clone con placeholders genéricos (`TU_USUARIO`, `/ruta/a/…`, usuario `demo` en login-api)

---

## [1.0.1] - 2026-06-16

### Añadido

- Skill `configurar-engram-multiide` movida a `skills/` para alinearse con la convención del repo (multi-IDE: Cursor + Claude Code)
- Documentación principal traducida al español latinoamericano neutro; originales en inglés conservados con sufijo `.en.md` (README, CONTRIBUTING, AGENTS, docs/)
- Sección `## Engram` en `CLAUDE.md` expandida con reglas operacionales completas: `mem_context`, `mem_save`, formato What/Why/Where/Learned, tabla de herramientas MCP
- Chunks Engram sincronizados al repo (`.engram/manifest.json` + `chunks/`)

### Cambiado

- `CLAUDE.md` sección Engram: de puntero de una línea a plantilla operacional completa (fuente: `skills/configurar-engram-multiide/reference/plantilla-claude-engram.md`)
- `.claude/commands/skill-configurar-engram-multiide.md`: ruta actualizada de `.cursor/skills/` a `skills/`

### Corregido

- Argentinismos en `CONTRIBUTING.md` corregidos a español latinoamericano neutro

---

## [1.0.0] - 2026-06-15

### Añadido

- Fork de `addyosmani/agent-skills` v1.0.0 como base del proyecto
- Skills de stack extendido: `angular-frontend`, `nodejs-backend`, `springboot-backend`, `python-backend`, `go-backend`, `react-frontend`, `vue-frontend`, `python-google-adk`
- Comandos scaffold de stack en `.claude/commands/`: `scaffold-angular`, `scaffold-node`, `scaffold-springboot`, `scaffold-python`, `scaffold-go`, `scaffold-react`, `scaffold-vue`, `scaffold-adk`
- Comandos scaffold en `.gemini/commands/` y `commands/` para Gemini CLI y Antigravity
- `STACK-EXTENSIONS.md`: documentación de extensiones específicas del stack extendido
- Configuración Engram MCP por repo: `.engram/config.json`, `.cursor/mcp.json`, `.cursor/rules/engram.mdc`
- Hook `SessionStart` en `.claude/settings.local.json` para inyección automática del meta-skill `using-agent-skills`
- Guía de análisis completo del repo en `docs/guias/agent-skills-dev-analysis.md`
- `scripts/validate-skills.js`: validador de frontmatter, secciones y referencias cruzadas entre skills
- Pipeline CI/CD en `.github/workflows/test-plugin-install.yml`
