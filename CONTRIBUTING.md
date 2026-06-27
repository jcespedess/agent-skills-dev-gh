# Contribuir a Agent Skills — Dev

¡Gracias por tu interés en contribuir! Este proyecto es una colección de skills de ingeniería de producción para agentes de IA, extendida con el stack del proyecto.

## Agregar una nueva skill

1. Crear un directorio en `skills/` con nombre en kebab-case
2. Agregar un `SKILL.md` siguiendo el formato de [docs/skill-anatomy.md](docs/skill-anatomy.md)
3. Incluir frontmatter YAML con los campos `name` y `description`
4. Asegurar que `description` comience con lo que hace la skill (tercera persona), seguido de una o más condiciones de disparo `Usar cuando`

### Bar de calidad para skills

Las skills deben ser:

- **Específicas** — Pasos accionables, no consejos vagos
- **Verificables** — Criterios de salida claros con requisitos de evidencia
- **Probadas en batalla** — Basadas en flujos de trabajo de ingeniería reales, no en ideales teóricos
- **Mínimas** — Solo el contenido necesario para guiar al agente correctamente

### Estructura

Toda nueva skill debe tener:

- `SKILL.md` en el directorio de la skill
- Frontmatter YAML con `name` y `description` válidos

Las nuevas skills deben seguir la anatomía estándar:

- **Overview** — Qué hace esta skill y por qué importa
- **When to Use** — Condiciones de activación
- **Process** — Flujo de trabajo paso a paso
- **Common Rationalizations** — Excusas que los agentes usan para saltarse pasos, con rebatimientos
- **Red Flags** — Señales de advertencia de que la skill se está aplicando incorrectamente
- **Verification** — Cómo confirmar que la skill se aplicó correctamente

Los campos de frontmatter son obligatorios. La anatomía de secciones es un patrón recomendado: títulos equivalentes como `How It Works`, `Workflow` o `Core Process` están bien cuando preservan la misma intención y hacen la skill fácil de seguir.

### Qué no hacer

- No duplicar contenido entre skills — referenciar otras skills en su lugar
- No agregar skills que sean consejos vagos en lugar de procesos accionables
- No crear archivos de soporte a menos que el contenido supere las 100 líneas
- No crear un directorio `scripts/` vacío solo para imitar otra skill — agregar `scripts/` solo cuando la skill incluye helpers ejecutables
- No poner material de referencia dentro de directorios de skills — usar `references/` en su lugar

## Agregar skills de stack extendido

Para agregar o modificar skills específicas del stack del proyecto (`angular-frontend`, `springboot-backend`, etc.):

1. Seguir la misma anatomía que las skills base
2. Evitar hardcodear versiones de APIs — delegar a `source-driven-development` para verificar la versión instalada
3. Documentar la skill en `STACK-EXTENSIONS.md` (tabla de skills y comandos)
4. Si corresponde, agregar o actualizar el comando scaffold en `.claude/commands/scaffold-*.md`

## Modificar skills existentes

- Mantener los cambios focalizados y mínimos
- Preservar la estructura y el tono existentes
- Verificar que el frontmatter YAML siga siendo válido tras las ediciones

## Testear hooks

El hook de inicio de sesión (`hooks/session-start.sh`) inyecta la meta-skill `using-agent-skills` en cada nueva sesión de Claude Code. Un test de regresión en `hooks/session-start-test.sh` valida el payload JSON del hook — tanto cuando `jq` está disponible como cuando no lo está.

Ejecutarlo antes de abrir cualquier PR que toque:

- `hooks/session-start.sh`
- `skills/using-agent-skills/SKILL.md` (el contenido de la meta-skill embebido por el hook)

```bash
bash hooks/session-start-test.sh
```

Salida esperada: `session-start JSON payload OK`. El script sale con código distinto de cero ante cualquier fallo de aserción.

### Reproducir el fallback sin jq

El hook degrada graciosamente a un payload de prioridad `INFO` cuando `jq` no está en `PATH`. Para ejercitar esa rama localmente:

```bash
JQ_DIR=$(dirname "$(command -v jq)")
PATH=$(echo "$PATH" | tr ':' '\n' | grep -v "^${JQ_DIR}$" | tr '\n' ':' | sed 's/:$//') \
  bash hooks/session-start-test.sh
```

## Validar skills

Antes de cualquier PR, correr el validador para asegurar que el frontmatter y las secciones obligatorias estén correctos:

```bash
node scripts/validate-skills.js
```

Salida esperada: `X skills checked — 0 error(s), 0 warning(s) — PASSED`

## Reportar problemas

Abrir un issue si encuentras:

- Una skill que da orientación incorrecta u obsoleta
- Cobertura faltante para un flujo de trabajo de ingeniería común
- Inconsistencias entre skills
- Una skill de stack extendido que no refleja la versión actual del framework

## Licencia

Al contribuir, aceptas que tus contribuciones serán licenciadas bajo la Licencia MIT.
