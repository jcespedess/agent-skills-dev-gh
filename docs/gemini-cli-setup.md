# Usar agent-skills con Gemini CLI

## Configuración

### Opción 1: Instalar como skills (Recomendado)

Gemini CLI tiene un sistema nativo de skills que auto-descubre archivos `SKILL.md` en los directorios `.gemini/skills/` o `.agents/skills/`. Cada skill se activa bajo demanda cuando coincide con tu tarea.

**Instalar desde el repositorio:**

```bash
gemini skills install https://github.com/addyosmani/agent-skills.git --path skills
```

**O instalar desde un clon local:**

```bash
git clone https://github.com/addyosmani/agent-skills.git
gemini skills install /path/to/agent-skills/skills/
```

**Instalar solo para un workspace específico:**

```bash
gemini skills install /path/to/agent-skills/skills/ --scope workspace
```

Una vez instalado, verifica con:

```
/skills list
```

Gemini CLI inyecta automáticamente los nombres y descripciones de las skills. Cuando reconoce una tarea coincidente, pide permiso para activar la skill antes de cargar sus instrucciones completas.

### Opción 2: GEMINI.md (Contexto persistente)

Para skills que quieres cargar siempre como contexto persistente del proyecto (en lugar de activación bajo demanda), agrégalas a tu `GEMINI.md`:

```bash
cat /path/to/agent-skills/skills/incremental-implementation/SKILL.md > GEMINI.md
echo -e "\n---\n" >> GEMINI.md
cat /path/to/agent-skills/skills/code-review-and-quality/SKILL.md >> GEMINI.md
```

También puedes modularizar importando desde archivos separados:

```markdown
@skills/test-driven-development/SKILL.md
@skills/incremental-implementation/SKILL.md
```

Usa `/memory show` para verificar el contexto cargado y `/memory reload` para actualizar tras cambios.

> **Skills vs GEMINI.md:** Las skills son experiencia bajo demanda que se activa solo cuando es relevante, manteniendo limpia la ventana de contexto. GEMINI.md provee contexto persistente cargado en cada prompt. Usa skills para flujos de trabajo por fase y GEMINI.md para convenciones del proyecto que deben estar siempre activas.

## Configuración recomendada

### Siempre activo (GEMINI.md)

Agrega estas como contexto persistente para cada sesión:

- `incremental-implementation` — Construir en slices pequeños y verificables
- `code-review-and-quality` — Revisión en cinco ejes

### Bajo demanda (Skills)

Instala estas como skills para que se activen solo cuando sean relevantes:

- `test-driven-development` — Se activa al implementar lógica o corregir bugs
- `spec-driven-development` — Se activa al iniciar un proyecto o feature nuevo
- `frontend-ui-engineering` — Se activa al construir UI
- `security-and-hardening` — Se activa en revisiones de seguridad
- `performance-optimization` — Se activa en trabajo de rendimiento

## Configuración avanzada

### Integración MCP

Varias skills de este pack aprovechan herramientas de [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) para interactuar con el entorno. Por ejemplo:

- `browser-testing-with-devtools` usa la extensión MCP `chrome-devtools`.
- `performance-optimization` puede beneficiarse de herramientas MCP de rendimiento.

Para habilitarlas, asegúrate de tener las extensiones MCP relevantes instaladas en tu configuración de Gemini CLI (`~/.gemini/config.json`).

### Hooks de sesión

Gemini CLI soporta hooks de ciclo de vida de sesión. Puedes usarlos para inyectar contexto automáticamente o ejecutar scripts de validación al inicio de una sesión.

### Carga explícita de contexto

Puedes cargar explícitamente cualquier skill en tu sesión actual referenciándola con el símbolo `@` en tu prompt:

```markdown
Use the @skills/test-driven-development/SKILL.md skill to implement this fix.
```

## Slash commands

El repositorio incluye 7 slash commands en `.gemini/commands/` que mapean al ciclo de vida del desarrollo. Gemini CLI los auto-descubre cuando ejecutas desde la raíz del proyecto.

| Comando | Qué hace |
|---------|----------|
| `/spec` | Escribir un spec estructurado antes de escribir código |
| `/planning` | Descomponer el trabajo en tareas pequeñas y verificables |
| `/build` | Implementar la siguiente tarea de forma incremental |
| `/test` | Flujo TDD — rojo, verde, refactor |
| `/review` | Revisión de código en cinco ejes |
| `/code-simplify` | Reducir complejidad sin cambiar el comportamiento |
| `/ship` | Checklist de pre-lanzamiento con fan-out paralelo de personas |

> **Nota:** Usa `/planning` en lugar de `/plan` — `/plan` entra en conflicto con un comando interno de Gemini CLI.

## Consejos de uso

1. **Prefiere skills sobre GEMINI.md** — Las skills se activan bajo demanda y mantienen tu ventana de contexto enfocada.
2. **Las descripciones de las skills importan** — Cada `SKILL.md` tiene un campo `description` en su frontmatter que indica a los agentes cuándo activarla.
3. **Usa agentes para revisión** — Copia el contenido de `agents/code-reviewer.md` al solicitar revisiones de código estructuradas.
4. **Combina con referencias** — Referencia los checklists de `references/` cuando trabajes en áreas de calidad específicas.
