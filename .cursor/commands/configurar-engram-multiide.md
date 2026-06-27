---
name: /configurar-engram-multiide
id: configurar-engram-multiide
category: Workflow
description: Setup Engram F1–F5 en Cursor y/o Claude Code (skill configurar-engram-multiide)
---

# configurar-engram-multiide

Punto de entrada para **setup** de Engram en **Cursor y/o Claude Code**. Skill: **`@configurar-engram-multiide`**.

> **Solo Cursor:** usar **`@configurar-engram`** o **`/configurar-engram`** (skill más simple, misma cobertura Cursor).

## Paso 0 — IDE destino (obligatorio)

| Opción | Qué configura |
|--------|--------------|
| **Cursor** | F2-Cursor + rule `engram.mdc` |
| **Claude Code** | F2-CC + sección `## Engram` en `CLAUDE.md` |
| **Ambos** | F2-Cursor + F2-CC + ambos artefactos |

## Modos (inferir del chat o pedir al usuario)

| Modo | Fases | Frases típicas |
|------|-------|----------------|
| **A** (default) | F1 → F5 completo | «configura Engram en Claude Code», «configura Engram en Cursor y Claude Code» |
| **B** | F4 verificar | «verifica Engram», «health check engram» |
| **C** | F5 sync | «sync engram», «subir/bajar chunks» |
| **D** | F1 sistema | CLI no encontrado |
| **E** | F2-Cursor | solo MCP Cursor |
| **E-CC** | F2-CC | solo MCP Claude Code |
| **F** | F3 repo | solo config.json + rule/CLAUDE.md |
| **G** | Comenzar día | «comenzar el día», «iniciar sesión de trabajo» |
| **H** | Finalizar día | «finalizar el día», «cerrar sesión engram» |
| **I** | Consultar ID | «detalle memoria #N», «timeline engram» |

Sin argumento → preguntar **IDE destino** y luego **modo A**.

## Pasos (modo A)

1. Confirmar **IDE destino** (Cursor / Claude Code / Ambos).
2. Confirmar **`DEST_ROOT`** (ruta absoluta en multi-root).
3. Ejecutar checklist del IDE correspondiente (o ambos si «Ambos»).
4. Informe final unificado con filas N/A por IDE no configurado.
5. Commit de chunks **solo** si el usuario lo pide.

## Activación

`/configurar-engram-multiide`, `@configurar-engram-multiide`, «configura Engram en Claude Code», «configura Engram en Cursor y Claude Code».
