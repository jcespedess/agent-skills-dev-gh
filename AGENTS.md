# AGENTS.md

Este archivo proporciona orientación a los agentes de IA (Claude Code, Cursor, Copilot, Antigravity, etc.) cuando trabajan con código en este repositorio.

## Descripción del repositorio

Una colección de skills para Claude.ai y Claude Code orientada a ingenieros de software senior. Las skills son instrucciones y scripts empaquetados que amplían las capacidades de Claude y de los agentes de código.

## Integración con OpenCode

OpenCode utiliza un **modelo de ejecución basado en skills** impulsado por la herramienta `skill` y el directorio `/skills` de este repositorio.

### Reglas principales

- Si una tarea coincide con una skill, DEBES invocarla
- Las skills se encuentran en `skills/<skill-name>/SKILL.md`
- Nunca implementes directamente si existe una skill aplicable
- Sigue siempre las instrucciones de la skill de forma exacta (no las apliques parcialmente)

### Mapeo de intención → skill

El agente debe mapear automáticamente la intención del usuario a las skills:

- Feature / nueva funcionalidad → `spec-driven-development`, luego `incremental-implementation`, `test-driven-development`
- Planificación / desglose → `planning-and-task-breakdown`
- Bug / fallo / comportamiento inesperado → `debugging-and-error-recovery`
- Revisión de código → `code-review-and-quality`
- Refactoring / simplificación → `code-simplification`
- Diseño de API o interfaz → `api-and-interface-design`
- Trabajo de UI → `frontend-ui-engineering`

### Mapeo de ciclo de vida (comandos implícitos)

OpenCode no soporta slash commands como `/spec` o `/plan`.

En su lugar, el agente debe seguir internamente este ciclo de vida:

- DEFINIR → `spec-driven-development`
- PLANIFICAR → `planning-and-task-breakdown`
- CONSTRUIR → `incremental-implementation` + `test-driven-development`
- VERIFICAR → `debugging-and-error-recovery`
- REVISAR → `code-review-and-quality`
- PUBLICAR → `shipping-and-launch`

### Modelo de ejecución

Para cada solicitud:

1. Determinar si aplica alguna skill (incluso con 1% de probabilidad)
2. Invocar la skill apropiada usando la herramienta `skill`
3. Seguir el flujo de trabajo de la skill de forma estricta
4. Proceder a la implementación solo después de completar los pasos requeridos (spec, plan, etc.)

### Anti-racionalización

Los siguientes pensamientos son incorrectos y deben ignorarse:

- "Esto es demasiado pequeño para una skill"
- "Puedo implementar esto rápidamente"
- "Primero voy a recopilar contexto"

Comportamiento correcto:

- Siempre verificar y usar las skills primero

Esto asegura que OpenCode se comporte de forma similar a Claude Code con cumplimiento completo del flujo de trabajo.

## Orquestación: personas, skills y comandos

Este repositorio tiene tres capas componibles. Tienen trabajos distintos y no deben confundirse:

- **Skills** (`skills/<name>/SKILL.md`) — flujos de trabajo con pasos y criterios de salida. El *cómo*. De uso obligatorio cuando una intención coincide.
- **Personas** (`agents/<role>.md`) — roles con una perspectiva y un formato de salida. El *quién*.
- **Slash commands** (`.claude/commands/*.md`) — puntos de entrada para el usuario. El *cuándo*. La capa de orquestación.

Regla de composición: **el usuario (o un slash command) es el orquestador. Las personas no invocan a otras personas.** Una persona puede invocar skills.

El único patrón de orquestación multi-persona que este repositorio respalda es el **fan-out paralelo con un paso de síntesis** — utilizado por `/ship` para ejecutar `code-reviewer`, `security-auditor` y `test-engineer` de forma concurrente y sintetizar sus reportes. No construyas una persona "router" que decida a qué otra persona llamar; ese es el trabajo de los slash commands y el mapeo de intenciones.

Consulta [agents/README.md](agents/README.md) para la matriz de decisiones y [references/orchestration-patterns.md](references/orchestration-patterns.md) para el catálogo completo de patrones.

**Interoperabilidad con Claude Code:** las personas en `agents/` funcionan como subagentes de Claude Code (auto-descubiertos desde el directorio `agents/` de este plugin) y como compañeros de Agent Teams (referenciados por nombre al iniciarlos). Dos restricciones de plataforma se alinean con nuestras reglas: los subagentes no pueden generar otros subagentes, y los teams no pueden anidarse. Los agentes del plugin ignoran silenciosamente los campos de frontmatter `hooks`, `mcpServers` y `permissionMode`.

## Crear una nueva skill

### Estructura de directorios

```
skills/
  {skill-name}/           # nombre de directorio en kebab-case
    SKILL.md              # Requerido: definición de la skill
    scripts/              # Requerido: scripts ejecutables
      {script-name}.sh    # Scripts Bash (preferidos)
  {skill-name}.zip        # Requerido: empaquetado para distribución
```

### Convenciones de nombres

- **Directorio de skill**: `kebab-case` (ej. `web-quality`)
- **SKILL.md**: Siempre en mayúsculas, siempre este nombre exacto
- **Scripts**: `kebab-case.sh` (ej. `deploy.sh`, `fetch-logs.sh`)
- **Archivo zip**: Debe coincidir exactamente con el nombre del directorio: `{skill-name}.zip`

### Formato de SKILL.md

```markdown
---
name: {skill-name}
description: {Una oración describiendo qué hace la skill, seguida de una o más condiciones de disparo "Usar cuando". Incluye frases de disparo como "Deploy my app" o "Check logs" cuando sea útil.}
---

# {Título de la skill}

{Descripción breve de qué hace la skill y por qué importa.}

## How It Works

{Lista numerada explicando el flujo de trabajo de la skill}

## Usage (Opcional)

Incluir esta sección solo si la skill incluye helpers ejecutables en `scripts/`.

```bash
bash /mnt/skills/user/{skill-name}/scripts/{script}.sh [args]
```
```

### Buenas prácticas para eficiencia de contexto

Las skills se cargan bajo demanda — solo el nombre y la descripción se cargan al inicio. El `SKILL.md` completo se carga en contexto solo cuando el agente determina que la skill es relevante. Para minimizar el uso de contexto:

- **Mantén SKILL.md bajo 500 líneas** — coloca material de referencia detallado en archivos separados
- **Escribe descripciones específicas** — ayuda al agente a saber exactamente cuándo activar la skill
- **Usa disclosure progresivo** — referencia archivos de soporte que se lean solo cuando se necesiten
- **Prefiere scripts sobre código inline** — la ejecución de scripts no consume contexto (solo el output sí)
- **Las referencias a archivos funcionan un nivel de profundidad** — enlaza directamente desde SKILL.md a los archivos de soporte

### Requisitos de scripts

- Usar shebang `#!/bin/bash`
- Usar `set -e` para comportamiento fail-fast
- Escribir mensajes de estado en stderr: `echo "Message" >&2`
- Escribir output legible por máquina (JSON) en stdout
- Incluir un trap de limpieza para archivos temporales
- Referenciar la ruta del script como `/mnt/skills/user/{skill-name}/scripts/{script}.sh`

### Crear el paquete zip

Después de crear o actualizar una skill:

```bash
cd skills
zip -r {skill-name}.zip {skill-name}/
```

### Instalación para el usuario final

Documenta estos dos métodos de instalación para los usuarios:

**Claude Code:**
```bash
cp -r skills/{skill-name} ~/.claude/skills/
```

**claude.ai:**
Agrega la skill al conocimiento del proyecto o pega el contenido de SKILL.md en la conversación.

Si la skill requiere acceso a red, indica a los usuarios que agreguen los dominios requeridos en `claude.ai/settings/capabilities`.
