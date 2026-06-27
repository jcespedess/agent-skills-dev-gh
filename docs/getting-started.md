# Primeros pasos con agent-skills

agent-skills funciona con cualquier agente de IA que acepte instrucciones en Markdown. Esta guía cubre el enfoque universal. Para la configuración específica por herramienta, consulta las guías dedicadas.

## Cómo funcionan las skills

Cada skill es un archivo Markdown (`SKILL.md`) que describe un flujo de trabajo de ingeniería específico. Cuando se carga en el contexto del agente, este sigue el flujo de trabajo — incluyendo los pasos de verificación, los anti-patrones a evitar y los criterios de salida.

**Las skills no son documentos de referencia.** Son procesos paso a paso que el agente sigue.

## Inicio rápido (cualquier agente)

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/agent-skills-dev-gh.git
```

### 2. Elegir una skill

Explora el directorio `skills/`. Cada subdirectorio contiene un `SKILL.md` con:
- **When to use** — disparadores que indican cuándo aplica esta skill
- **Process** — flujo de trabajo paso a paso
- **Verification** — cómo confirmar que el trabajo está completo
- **Common rationalizations** — excusas que el agente podría usar para saltarse pasos
- **Red flags** — señales de que la skill está siendo violada

### 3. Cargar la skill en tu agente

Copia el contenido del `SKILL.md` relevante en el system prompt, archivo de reglas o conversación de tu agente. Los enfoques más comunes:

**System prompt:** Pega el contenido de la skill al inicio de la sesión.

**Archivo de reglas:** Agrega el contenido de la skill al archivo de reglas de tu proyecto (CLAUDE.md, .cursorrules, etc.).

**Conversación:** Referencia la skill al dar instrucciones: "Sigue el proceso de test-driven-development para este cambio."

### 4. Usar la meta-skill para descubrimiento

Comienza con la skill `using-agent-skills` cargada. Contiene un diagrama de flujo que mapea los tipos de tareas a la skill apropiada.

## Configuración recomendada

### Mínima (empieza aquí)

Carga tres skills esenciales en tu archivo de reglas:

1. **spec-driven-development** — Para definir qué construir
2. **test-driven-development** — Para demostrar que funciona
3. **code-review-and-quality** — Para verificar la calidad antes del merge

Estas tres cubren las brechas de calidad más críticas en el desarrollo asistido por IA.

### Ciclo de vida completo

Para cobertura integral, carga las skills por fase:

```
Iniciando un proyecto:  spec-driven-development → planning-and-task-breakdown
Durante el desarrollo:  incremental-implementation + test-driven-development
Antes del merge:        code-review-and-quality + security-and-hardening
Antes del deploy:       shipping-and-launch
```

### Carga consciente del contexto

No cargues todas las skills a la vez — desperdicia contexto. Carga las skills relevantes para la tarea actual:

- ¿Trabajando en UI? Carga `frontend-ui-engineering`
- ¿Depurando? Carga `debugging-and-error-recovery`
- ¿Configurando CI? Carga `ci-cd-and-automation`

## Anatomía de una skill

Cada skill sigue la misma estructura:

```
YAML frontmatter (name, description)
├── Overview — Qué hace esta skill
├── When to Use — Disparadores y condiciones
├── Core Process — Flujo de trabajo paso a paso
├── Examples — Ejemplos de código y patrones
├── Common Rationalizations — Excusas y rebatimientos
├── Red Flags — Señales de que la skill está siendo violada
└── Verification — Lista de criterios de salida
```

Consulta [skill-anatomy.es.md](skill-anatomy.es.md) para la especificación completa.

## Uso de agentes

El directorio `agents/` contiene personas de agentes preconfiguradas:

| Agente | Propósito |
|--------|-----------|
| `code-reviewer.md` | Revisión de código en cinco ejes |
| `test-engineer.md` | Estrategia y escritura de tests |
| `security-auditor.md` | Detección de vulnerabilidades |
| `web-performance-auditor.md` | Auditoría de Core Web Vitals y rendimiento (vía `/webperf`) |

Carga una definición de agente cuando necesites una revisión especializada.

## Uso de comandos

El directorio `.claude/commands/` contiene slash commands para Claude Code:

| Comando | Skill invocada |
|---------|----------------|
| `/spec` | spec-driven-development |
| `/plan` | planning-and-task-breakdown |
| `/build` | incremental-implementation + test-driven-development |
| `/build auto` | planning-and-task-breakdown → incremental-implementation + test-driven-development (plan completo, una aprobación) |
| `/test` | test-driven-development |
| `/review` | code-review-and-quality |
| `/ship` | shipping-and-launch |
| `/webperf` | web-performance-auditor (agente especialista, solo apps web) |

## Uso de referencias

El directorio `references/` contiene checklists complementarios:

| Referencia | Usar con |
|-----------|----------|
| `testing-patterns.md` | test-driven-development |
| `performance-checklist.md` | performance-optimization |
| `security-checklist.md` | security-and-hardening |
| `accessibility-checklist.md` | frontend-ui-engineering |

Carga una referencia cuando necesites patrones detallados más allá de lo que cubre la skill.

## Artefactos de spec y tareas

Los comandos `/spec` y `/plan` crean artefactos de trabajo (`SPEC.md`, `tasks/plan.md`, `tasks/todo.md`). Trátalos como **documentos vivos** mientras el trabajo está en curso:

- Mantenlos en control de versiones durante el desarrollo para que el humano y el agente tengan una fuente de verdad compartida.
- Actualízalos cuando cambie el alcance o las decisiones.
- Si tu repositorio no quiere estos archivos a largo plazo, elimínalos antes del merge o agrega la carpeta al `.gitignore` — el flujo de trabajo no requiere que sean permanentes.

## Consejos

1. **Empieza con spec-driven-development** para cualquier trabajo no trivial
2. **Carga siempre test-driven-development** al escribir código
3. **No omitas los pasos de verificación** — ese es el punto central
4. **Carga las skills de forma selectiva** — más contexto no siempre es mejor
5. **Usa los agentes para revisión** — distintas perspectivas detectan distintos problemas
