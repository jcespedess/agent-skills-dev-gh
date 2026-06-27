# Usar agent-skills con Antigravity CLI (agy)

El paquete `agent-skills` puede instalarse como plugin nativo en Antigravity CLI (`agy`), dándole al agente acceso a flujos de trabajo estructurados, personas y slash commands personalizados.

## Configuración

### Opción 1: Instalación como plugin nativo (Recomendado)

Antigravity CLI tiene un sistema de plugins de primera clase que registra skills, agentes y comandos personalizados.

**Instalar desde el repositorio remoto:**

```bash
agy plugin install https://github.com/addyosmani/agent-skills.git
```

**Instalar desde un clon local:**

```bash
git clone https://github.com/addyosmani/agent-skills.git
agy plugin install /path/to/agent-skills
```

Esto validará el plugin y lo instalará en tu directorio de configuración global de Antigravity (`~/.gemini/antigravity-cli/plugins/agent-skills/`).

### Opción 2: Importar desde Gemini CLI

Si ya instalaste `agent-skills` bajo tu instalación legacy de Gemini CLI, puedes importarlo directamente:

```bash
agy plugin import gemini
```

Una vez instalado, verifica el plugin activo:

```bash
agy plugin list
```

---

## Slash commands

El plugin registra 7 slash commands personalizados que mapean al ciclo de vida del desarrollo:

| Comando | Qué hace | Skill activada |
|---------|----------|----------------|
| `/spec` | Escribir un spec estructurado antes de escribir código | `spec-driven-development` |
| `/planning` | Descomponer el trabajo en tareas pequeñas y verificables | `planning-and-task-breakdown` |
| `/build` | Implementar la siguiente tarea de forma incremental | `incremental-implementation` |
| `/test` | Flujo TDD — rojo, verde, refactor | `test-driven-development` |
| `/review` | Revisión de código en cinco ejes | `code-review-and-quality` |
| `/code-simplify` | Reducir complejidad sin cambiar el comportamiento | `code-simplification` |
| `/ship` | Checklist de pre-lanzamiento con fan-out paralelo de personas | `shipping-and-launch` |

> **Nota:** Usa `/planning` en lugar de `/plan` para evitar conflictos con el comando interno de generación de planes de Antigravity.

---

## Skills y descubrimiento

Antigravity auto-descubre las skills dentro del directorio `skills/` del plugin.

- Antigravity hace coincidir las tareas e intenciones del usuario con las skills relevantes bajo demanda.
- Si una tarea coincide con una skill, el agente cargará la skill y te pedirá permiso antes de ejecutar.

---

## Verificación y validación

Para validar que tu plugin local está correctamente estructurado y contiene todas las skills, ejecuta:

```bash
agy plugin validate /path/to/agent-skills
```

---

## Cómo funciona

### 1. Activación de skills bajo demanda

Antigravity CLI auto-descubre los archivos `SKILL.md` en el directorio `skills/` del plugin instalado. Usando las descripciones de activación en el frontmatter de cada skill, el agente activa dinámicamente el flujo de trabajo apropiado cuando detecta la intención del desarrollador.

Por ejemplo, cuando le pides al agente:

- **Diseñar un nuevo sistema** → Sugerirá/activará `spec-driven-development`
- **Implementar una funcionalidad** → Activará `incremental-implementation` y `test-driven-development`
- **Corregir un bug** → Activará `debugging-and-error-recovery`

### 2. Personas de agentes especializados

El plugin registra definiciones de subagentes reutilizables desde el directorio `agents/`:

- `code-reviewer.md`
- `security-auditor.md`
- `test-engineer.md`

Puedes invocar estas personas directamente dentro de tu sesión o al delegar tareas usando subagentes.

---

## Configuración y personalización

### Reglas específicas del proyecto (AGENTS.md)

Para imponer cumplimiento estricto de skills (por ejemplo, requerir un spec o plan antes de escribir código), copia o enlaza `AGENTS.md` en la raíz de tu workspace. Antigravity CLI lee este archivo para alinear el comportamiento del agente y la fase de planificación con las convenciones de tu equipo.

### Modo sandbox

Si quieres ejecutar skills o scripts con permisos de terminal limitados (por seguridad al ejecutar tests de validación de terceros), inicia el CLI con:

```bash
agy --sandbox
```

---

## Consejos de uso

1. **Mantén los plugins actualizados:** Puedes actualizar el CLI o verificar versiones más nuevas del plugin con:
   ```bash
   agy update
   ```
2. **Revisa antes de ejecutar:** Cuando los agentes ejecuten tareas de refactorización complejas usando estas skills, usa `Ctrl+r` para entrar a la pantalla de **Artifact Review** y revisar, editar o aprobar el código antes de que sea commiteado.
3. **Controla los permisos:** Usa el flag `--dangerously-skip-permissions` solo en proyectos locales de confianza donde quieras omitir los prompts de aprobación manual de herramientas.
