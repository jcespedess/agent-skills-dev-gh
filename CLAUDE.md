# agent-skills

This is the agent-skills project — a collection of production-grade engineering skills for AI coding agents.

## Project Structure

```
skills/       → Core skills (SKILL.md per directory)
agents/       → Reusable agent personas (code-reviewer, test-engineer, security-auditor, web-performance-auditor)
hooks/        → Session lifecycle hooks
.claude/commands/ → Slash commands (/spec, /plan, /build, /test, /review, /code-simplify, /ship; plus /webperf specialist audit)
references/   → Supplementary checklists (testing, performance, security, accessibility)
docs/         → Setup guides for different tools
```

## Skills by Phase

**Define:** interview-me, idea-refine, spec-driven-development
**Plan:** planning-and-task-breakdown
**Build:** incremental-implementation, test-driven-development, context-engineering, source-driven-development, doubt-driven-development, frontend-ui-engineering, api-and-interface-design
**Verify:** browser-testing-with-devtools, debugging-and-error-recovery
**Review:** code-review-and-quality, code-simplification, security-and-hardening, performance-optimization
**Ship:** git-workflow-and-versioning, ci-cd-and-automation, deprecation-and-migration, documentation-and-adrs, observability-and-instrumentation, shipping-and-launch

## Conventions

- Every skill lives in `skills/<name>/SKILL.md`
- YAML frontmatter with `name` and `description` fields
- Description starts with what the skill does (third person), followed by trigger conditions ("Use when...")
- Every skill has: Overview, When to Use, Process, Common Rationalizations, Red Flags, Verification
- References are in `references/`, not inside skill directories
- Supporting files only created when content exceeds 100 lines

## Commands

- `npm test` — Not applicable (this is a documentation project)
- Validate: Check that all SKILL.md files have valid YAML frontmatter with name and description

## Engram (memoria persistente)

Namespace: `agent-skills-dev-gh`. Siempre pasar `project: agent-skills-dev-gh` en tools Engram.

Setup: skill **`configurar-engram-multiide`** (`skills/configurar-engram-multiide/`) — Cursor: `/configurar-engram-multiide`; Claude Code: `.claude/commands/skill-configurar-engram-multiide.md`. Rule Cursor: `.cursor/rules/engram.mdc`.

### Reglas de uso proactivo

- Llamar `mem_context` al inicio de cada sesión con `project: agent-skills-dev-gh`.
- Guardar con `mem_save` inmediatamente tras decisiones, bugs resueltos, patrones o configuraciones relevantes.
- Formato obligatorio en `mem_save`:
  - `**What**: ...`
  - `**Why**: ...`
  - `**Where**: rutas/archivos`
  - `**Learned**: ...` (opcional)
- Buscar con `mem_search` antes de implementar algo que pudo haberse resuelto antes.
- `mem_session_summary` obligatorio al cerrar sesión de trabajo significativa.
- Pasar siempre `project: agent-skills-dev-gh` en `mem_search`, `mem_context` y `mem_save`.

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

## Boundaries

- Always: Follow the skill-anatomy.md format for new skills
- Never: Add skills that are vague advice instead of actionable processes
- Never: Duplicate content between skills — reference other skills instead
