# Usar agent-skills con Windsurf

## Configuración

### Reglas del proyecto

Windsurf usa `.windsurfrules` para instrucciones del agente específicas del proyecto:

```bash
cat /path/to/agent-skills/skills/test-driven-development/SKILL.md > .windsurfrules
echo "\n---\n" >> .windsurfrules
cat /path/to/agent-skills/skills/incremental-implementation/SKILL.md >> .windsurfrules
echo "\n---\n" >> .windsurfrules
cat /path/to/agent-skills/skills/code-review-and-quality/SKILL.md >> .windsurfrules
```

### Reglas globales

Para skills que quieres en todos los proyectos, agrégalas a las reglas globales de Windsurf:

1. Abre Windsurf → Settings → AI → Global Rules
2. Pega el contenido de tus skills más usadas

## Configuración recomendada

Mantén `.windsurfrules` enfocado en 2-3 skills esenciales para mantenerte dentro de los límites de contexto:

```
# .windsurfrules
# Skills esenciales de agent-skills para este proyecto

[Pegar test-driven-development SKILL.md]

---

[Pegar incremental-implementation SKILL.md]

---

[Pegar code-review-and-quality SKILL.md]
```

## Consejos de uso

1. **Sé selectivo** — El contexto de Windsurf es limitado. Elige las skills que cubran tus mayores brechas de calidad.
2. **Referencia en la conversación** — Pega contenido adicional de skills directamente en el chat cuando trabajes en fases específicas (por ejemplo, pega `security-and-hardening` al construir autenticación).
3. **Usa las referencias como checklists** — Pega `references/security-checklist.md` y pide a Windsurf que verifique cada ítem.
