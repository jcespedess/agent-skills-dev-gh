# Anatomía de una skill

Este documento describe la estructura y el formato de los archivos de skills de agent-skills. Úsalo como guía al contribuir nuevas skills o al entender las existentes.

## Ubicación de archivos

Cada skill vive en su propio directorio bajo `skills/`:

```
skills/
  skill-name/
    SKILL.md           # Requerido: la definición de la skill
    scripts/           # Opcional: helpers ejecutables usados por el flujo de trabajo
    supporting-file.md # Opcional: material de referencia cargado bajo demanda
```

`SKILL.md` es el único archivo requerido. Agrega `scripts/` solo cuando la skill incluya helpers ejecutables, y omite el directorio por completo en las skills solo-Markdown.

## Formato de SKILL.md

### Frontmatter (requerido)

```yaml
---
name: skill-name-with-hyphens
description: Guides agents through [task/workflow]. Use when [specific trigger conditions].
---
```

**Reglas:**
- `name`: En minúsculas, separado por guiones. Debe coincidir con el nombre del directorio.
- `description`: Comienza con lo que hace la skill en tercera persona, luego incluye una o más condiciones de disparo "Use when" claras. Incluye tanto el *qué* como el *cuándo*. Máximo 1024 caracteres.

**Por qué importa:** Los agentes descubren las skills leyendo las descripciones. La descripción se inyecta en el system prompt, por lo que debe indicarle al agente tanto qué proporciona la skill como cuándo activarla. No resumas el flujo de trabajo — si la descripción contiene pasos del proceso, el agente podría seguir el resumen en lugar de leer la skill completa.

### Secciones estándar (patrón recomendado)

El contrato de frontmatter es requerido. La estructura de secciones es un patrón recomendado, no una plantilla rígida: los títulos equivalentes son aceptables cuando sirven al mismo propósito con claridad.

```markdown
# Título de la skill

## Overview
Una o dos oraciones explicando qué hace esta skill y por qué importa.

## When to Use
- Lista de condiciones de activación (síntomas, tipos de tarea)
- Cuándo NO usar (exclusiones)

## [Core Process / The Workflow / Steps]
El flujo de trabajo principal, dividido en pasos numerados o fases.
Incluye ejemplos de código donde ayuden.
Usa diagramas de flujo (ASCII) donde existan puntos de decisión.

## [Specific Techniques / Patterns]
Orientación detallada para escenarios específicos.
Ejemplos de código, plantillas, configuración.

## Common Rationalizations
| Rationalization | Reality |
|---|---|
| Excusa que los agentes usan para saltarse pasos | Por qué la excusa es incorrecta |

## Red Flags
- Patrones de comportamiento que indican que la skill está siendo violada
- Cosas a observar durante la revisión

## Verification
Después de completar el proceso de la skill, confirmar:
- [ ] Lista de criterios de salida
- [ ] Requisitos de evidencia
```

## Propósito de las secciones

### Overview
El "elevator pitch" de la skill. Debe responder: ¿Qué hace esta skill y por qué debería seguirla un agente?

### When to Use
Ayuda a los agentes y a los humanos a decidir si esta skill aplica a la tarea actual. Incluye tanto disparadores positivos ("Usar cuando X") como exclusiones negativas ("NO para Y").

### Core Process
El núcleo de la skill. Este es el flujo de trabajo paso a paso que sigue el agente. Debe ser específico y accionable — no consejos vagos.

**Bueno:** "Ejecutar `npm test` y verificar que todos los tests pasen"
**Malo:** "Asegúrate de que los tests funcionen"

### Common Rationalizations
La característica más distintiva de las skills bien elaboradas. Son las excusas que los agentes usan para saltarse pasos importantes, junto con los rebatimientos. Evitan que el agente se racionalice a sí mismo para no seguir el proceso.

Piensa en cada vez que un agente ha dicho "Agrego los tests después" o "Esto es suficientemente simple para saltarse el spec" — esos casos van aquí con un contraargumento factual.

### Red Flags
Señales observables de que la skill está siendo violada. Útiles durante la revisión de código y el auto-monitoreo.

### Verification
Los criterios de salida. Una lista de verificación que el agente usa para confirmar que el proceso de la skill está completo. Cada casilla debe ser verificable con evidencia (output de tests, resultado del build, screenshot, etc.).

## Archivos de soporte

Crea archivos de soporte solo cuando:
- El material de referencia supera las 100 líneas (mantén el SKILL.md principal enfocado)
- Se necesitan herramientas o scripts de código
- Los checklists son lo suficientemente largos para justificar archivos separados

Mantén los patrones y principios inline cuando sean menos de 50 líneas.

Si una skill no necesita helpers ejecutables, no crees un directorio `scripts/` vacío solo para imitar otras skills. Los directorios vacíos añaden ruido sin cambiar el funcionamiento de la skill.

## Principios de escritura

1. **Proceso sobre conocimiento.** Las skills son flujos de trabajo, no docs de referencia. Pasos, no hechos.
2. **Específico sobre general.** "Ejecutar `npm test`" supera a "verificar los tests".
3. **Evidencia sobre suposición.** Cada casilla de verificación requiere prueba.
4. **Anti-racionalización.** Cada paso que vale la pena saltarse necesita un contraargumento en la tabla de racionalizaciones.
5. **Disclosure progresivo.** El SKILL.md principal es el punto de entrada. Los archivos de soporte se cargan solo cuando se necesitan.
6. **Consciente de tokens.** Cada sección debe justificar su inclusión. Si eliminarla no cambiaría el comportamiento del agente, elimínala.

## Convenciones de nombres

- Directorios de skills: `lowercase-hyphen-separated`
- Archivos de skills: `SKILL.md` (siempre en mayúsculas)
- Archivos de soporte: `lowercase-hyphen-separated.md`
- Referencias: almacenadas en `references/` en la raíz del proyecto, no dentro de los directorios de skills

## Referencias cruzadas entre skills

Referencia otras skills por nombre:

```markdown
Follow the `test-driven-development` skill for writing tests.
If the build breaks, use the `debugging-and-error-recovery` skill.
```

No dupliques contenido entre skills — referencia y enlaza en su lugar.

## Requerido vs. recomendado

Requerido:

- Un archivo `skills/<skill-name>/SKILL.md`
- Frontmatter YAML válido con `name` y `description`
- Una descripción que incluya tanto lo que hace la skill como cuándo usarla

Recomendado:

- El flujo de secciones estándar mostrado arriba
- Títulos equivalentes como `How It Works`, `Core Process` o `Workflow` cuando se lean más naturalmente para la skill
- Archivos de soporte solo cuando mantengan el `SKILL.md` principal enfocado
