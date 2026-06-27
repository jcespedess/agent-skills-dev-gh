# Usar agent-skills con GitHub Copilot

## Configuración

### Instrucciones de Copilot

Copilot soporta la creación de agent skills usando un directorio `.github/skills`, `.claude/skills` o `.agents/skills` en tu repositorio.

```bash
mkdir -p .github

# Crear archivos para las skills esenciales
cat /path/to/agent-skills/skills/test-driven-development/SKILL.md > .github/skills/test-driven-development/SKILL.md
cat /path/to/agent-skills/skills/code-review-and-quality/SKILL.md > .github/skills/code-review-and-quality/SKILL.md
```

Para más detalles, consulta [Creating agent skills for GitHub Copilot](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-skills).

### Personas de agentes (*.agent.md)

Copilot soporta personas de agentes especializados. Usa los agentes de agent-skills:

> **Importante:** GitHub Copilot requiere que los archivos de agentes personalizados se llamen `*.agent.md`.
> Los archivos llamados `*.md` son ignorados silenciosamente por Copilot.
> Consulta la [documentación de agentes personalizados de VS Code](https://code.visualstudio.com/docs/copilot/customization/custom-agents#_custom-agent-file-structure) para más detalles.

```bash
# Crear el directorio de agentes y copiar las definiciones
mkdir -p .github/agents
cp /path/to/agent-skills/agents/code-reviewer.md .github/agents/code-reviewer.agent.md
cp /path/to/agent-skills/agents/test-engineer.md .github/agents/test-engineer.agent.md
cp /path/to/agent-skills/agents/security-auditor.md .github/agents/security-auditor.agent.md
```

Invoca los agentes en Copilot Chat:
- `@code-reviewer Review this PR`
- `@test-engineer Analyze test coverage for this module`
- `@security-auditor Check this endpoint for vulnerabilities`

### Instrucciones personalizadas (nivel usuario)

Para skills que quieres en todos los repositorios:

1. Abre VS Code → Settings → GitHub Copilot → Custom Instructions
2. Agrega resúmenes de tus skills más usadas

## Configuración recomendada

### .github/copilot-instructions.md

GitHub Copilot soporta instrucciones a nivel de proyecto vía `.github/copilot-instructions.md`.

```markdown
# Estándares de código del proyecto

## Testing
- Escribe tests antes del código (TDD)
- Para bugs: escribe primero un test fallido (patrón Prove-It)
- Jerarquía de tests: unitario > integración > e2e (usa el nivel más bajo que capture el comportamiento)
- Ejecuta `npm test` después de cada cambio

## Calidad del código
- Revisa en cinco ejes: correctitud, legibilidad, arquitectura, seguridad, rendimiento
- Todo PR debe pasar: lint, verificación de tipos, tests, build
- Sin secretos en el código ni en el control de versiones

## Implementación
- Construye en incrementos pequeños y verificables
- Cada incremento: implementar → testear → verificar → commitear
- Nunca mezcles cambios de formato con cambios de comportamiento

## Límites
- Siempre: ejecutar tests antes de commits, validar input del usuario
- Preguntar primero: cambios en schema de base de datos, nuevas dependencias
- Nunca: commitear secretos, eliminar tests fallidos, saltarse la verificación
```

### Agentes especializados

Usa los agentes para flujos de trabajo de revisión focalizados en Copilot Chat.

## Consejos de uso

1. **Mantén las instrucciones concisas** — Las instrucciones de Copilot funcionan mejor cuando están enfocadas. Resume las reglas clave en lugar de incluir archivos de skills completos.
2. **Usa agentes para revisión** — Los agentes code-reviewer, test-engineer y security-auditor están diseñados para el modelo de agentes de Copilot.
3. **Referencia en el chat** — Cuando trabajes en una fase específica, pega el contenido de la skill relevante en Copilot Chat para contexto.
4. **Combina con revisiones de PR** — Configura Copilot para revisar PRs usando la persona del agente code-reviewer.
