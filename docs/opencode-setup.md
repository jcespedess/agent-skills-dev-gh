# Configuración de OpenCode

Esta guía explica cómo usar Agent Skills con OpenCode de una manera que se acerque a la experiencia de Claude Code (selección automática de skills, flujos de trabajo guiados por ciclo de vida y aplicación estricta del proceso).

## Descripción general

OpenCode soporta `/commands` personalizados, pero no tiene un sistema de plugins nativo ni enrutamiento automático de skills como Claude Code.

En cambio, la paridad se logra mediante:

- Un system prompt sólido (`AGENTS.md`)
- La herramienta integrada `skill`
- Descubrimiento consistente de skills desde el directorio `/skills`

Esto crea un **flujo de trabajo guiado por el agente** donde las skills se seleccionan y ejecutan automáticamente.

Si bien es posible recrear `/spec`, `/plan` y otros comandos en OpenCode, esta integración usa intencionalmente un enfoque guiado por el agente:

- Las skills se seleccionan automáticamente según la intención
- Los flujos de trabajo se aplican vía `AGENTS.md`
- No se requiere invocación manual de comandos

Esto se acerca más a cómo se comporta Claude Code en la práctica, donde las skills se activan automáticamente en lugar de manualmente.

---

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/addyosmani/agent-skills.git
```

2. Abre el proyecto en OpenCode.

3. Asegúrate de que los siguientes archivos estén presentes en tu workspace:

- `AGENTS.md` (raíz)
- Directorio `skills/`

No se requiere instalación adicional.

---

## Cómo funciona

### 1. Descubrimiento de skills

Todas las skills viven en:

```
skills/<skill-name>/SKILL.md
```

Los agentes de OpenCode están instruidos (vía `AGENTS.md`) para:

- Detectar cuándo aplica una skill
- Invocar la herramienta `skill`
- Seguir la skill exactamente

### 2. Invocación automática de skills

El agente evalúa cada solicitud y la mapea a la skill apropiada.

Ejemplos:

- "construir una funcionalidad" → `incremental-implementation` + `test-driven-development`
- "diseñar un sistema" → `spec-driven-development`
- "corregir un bug" → `debugging-and-error-recovery`
- "revisar este código" → `code-review-and-quality`

El usuario **no** necesita solicitar skills explícitamente.

### 3. Mapeo del ciclo de vida (comandos implícitos)

El ciclo de vida de desarrollo está codificado implícitamente:

- DEFINIR → `spec-driven-development`
- PLANIFICAR → `planning-and-task-breakdown`
- CONSTRUIR → `incremental-implementation` + `test-driven-development`
- VERIFICAR → `debugging-and-error-recovery`
- REVISAR → `code-review-and-quality`
- PUBLICAR → `shipping-and-launch`

Esto reemplaza los slash commands como `/spec`, `/plan`, etc.

---

## Ejemplos de uso

### Ejemplo 1: Desarrollo de funcionalidad

Usuario:
```
Agrega autenticación a esta app
```

Comportamiento del agente:
- Detecta trabajo de nueva funcionalidad
- Invoca `spec-driven-development`
- Produce un spec antes de escribir código
- Avanza a las skills de planificación e implementación

---

### Ejemplo 2: Corrección de bug

Usuario:
```
Este endpoint está retornando errores 500
```

Comportamiento del agente:
- Invoca `debugging-and-error-recovery`
- Reproduce → localiza → corrige → agrega guardas

---

### Ejemplo 3: Revisión de código

Usuario:
```
Revisa este PR
```

Comportamiento del agente:
- Invoca `code-review-and-quality`
- Aplica revisión estructurada (correctitud, diseño, legibilidad, etc.)

---

## Expectativas del agente (crítico)

Para que OpenCode funcione correctamente, el agente debe seguir estas reglas:

- Siempre verificar si aplica una skill antes de actuar
- Si aplica una skill, DEBE usarse
- Nunca saltarse flujos de trabajo requeridos (spec, plan, test, etc.)
- No ir directamente a la implementación

Estas reglas se aplican vía `AGENTS.md`.

---

## Limitaciones

- Sin slash commands nativos (manejados vía mapeo de intenciones)
- Sin sistema de plugins (manejado vía prompt + estructura)
- La invocación de skills depende del cumplimiento del modelo

A pesar de esto, el flujo de trabajo se acerca mucho a Claude Code en la práctica.

---

## Flujo de trabajo recomendado

Usa lenguaje natural:

- "Diseña una funcionalidad"
- "Planifica este cambio"
- "Implementa esto"
- "Corrige este bug"
- "Revisa esto"

El agente seleccionará y ejecutará automáticamente las skills correctas.

---

## Resumen

La integración con OpenCode funciona combinando:

- Skills estructuradas (este repositorio)
- Reglas sólidas del agente (`AGENTS.md`)
- Invocación automática de skills vía razonamiento

Esto resulta en un **flujo de trabajo de ingeniería de producción completamente guiado por el agente**, sin requerir plugins ni comandos manuales.
