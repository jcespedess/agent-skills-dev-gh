# Usar agent-skills con Cursor

## Configuración

### Opción 1: Directorio de reglas (Recomendado)

Cursor soporta un directorio `.cursor/rules/` para reglas específicas del proyecto:

```bash
mkdir -p .cursor/rules

cp /path/to/agent-skills/skills/test-driven-development/SKILL.md .cursor/rules/test-driven-development.md
cp /path/to/agent-skills/skills/code-review-and-quality/SKILL.md .cursor/rules/code-review-and-quality.md
cp /path/to/agent-skills/skills/incremental-implementation/SKILL.md .cursor/rules/incremental-implementation.md
```

Las reglas en este directorio se cargan automáticamente en el contexto de Cursor.

### Opción 2: Archivo .cursorrules

Crea un archivo `.cursorrules` en la raíz del proyecto con las skills esenciales incluidas:

```bash
cat /path/to/agent-skills/skills/test-driven-development/SKILL.md > .cursorrules
echo "\n---\n" >> .cursorrules
cat /path/to/agent-skills/skills/code-review-and-quality/SKILL.md >> .cursorrules
```

## Configuración recomendada

### Skills esenciales (cargar siempre)

Agrega estas a `.cursor/rules/`:

1. `test-driven-development.md` — Flujo TDD y patrón Prove-It
2. `code-review-and-quality.md` — Revisión en cinco ejes
3. `incremental-implementation.md` — Construir en slices pequeños y verificables

### Skills por fase (cargar según demanda)

Para trabajo en fases específicas, crea archivos de reglas adicionales según sea necesario:

- `spec-development.md` -> `spec-driven-development/SKILL.md`
- `frontend-ui.md` -> `frontend-ui-engineering/SKILL.md`
- `security.md` -> `security-and-hardening/SKILL.md`
- `performance.md` -> `performance-optimization/SKILL.md`

Agrégalas a `.cursor/rules/` cuando trabajes en tareas relevantes y retíralas al terminar para gestionar los límites de contexto.

## Consejos de uso

1. **No cargues todas las skills a la vez** — Cursor tiene límites de contexto. Carga 2-3 skills esenciales como reglas y agrega las específicas de cada fase según se necesite.
2. **Referencia las skills explícitamente** — Indica a Cursor "Follow the test-driven-development rules for this change" para asegurarte de que lea las reglas cargadas.
3. **Usa agentes para revisión** — Copia el contenido de `agents/code-reviewer.md` y pide a Cursor que revise el diff con ese framework.
4. **Carga referencias según demanda** — Cuando trabajes en rendimiento, agrega `performance.md` a `.cursor/rules/` o pega el contenido del checklist directamente.
