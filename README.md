# Agent Skills — Dev

**Skills de ingeniería de producción para agentes de IA.**

Las skills codifican los flujos de trabajo, gates de calidad y buenas prácticas que los ingenieros senior aplican al construir software. Están empaquetadas para que los agentes de IA las sigan de forma consistente en cada fase del desarrollo.

> Fork de [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) extendido con skills y comandos específicos del stack del proyecto. Ver [STACK-EXTENSIONS.md](STACK-EXTENSIONS.md) para el detalle de las extensiones.

```
  DEFINIR         PLANIFICAR     CONSTRUIR      VERIFICAR      REVISAR         PUBLICAR
 ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐
 │ Idea │ ───▶ │ Spec │ ───▶ │ Code │ ───▶ │ Test │ ───▶ │  QA  │ ───▶ │  Go  │
 │Refine│      │  PRD │      │ Impl │      │Debug │      │ Gate │      │ Live │
 └──────┘      └──────┘      └──────┘      └──────┘      └──────┘      └──────┘
  /spec          /plan          /build        /test         /review       /ship
```

---

## Comandos

7 slash commands que mapean al ciclo de vida del desarrollo. Cada uno activa las skills correctas automáticamente.

| Qué estás haciendo | Comando | Principio clave |
|--------------------|---------|-----------------|
| Definir qué construir | `/spec` | Spec antes que código |
| Planificar cómo construirlo | `/plan` | Tareas pequeñas y atómicas |
| Construir incrementalmente | `/build` | Un slice a la vez |
| Demostrar que funciona | `/test` | Los tests son la prueba |
| Revisar antes de mergear | `/review` | Mejorar la salud del código |
| Simplificar el código | `/code-simplify` | Claridad sobre ingenio |
| Publicar a producción | `/ship` | Más rápido es más seguro |

¿Querés menos pasos manuales una vez que existe el spec? **`/build auto`** genera el plan e implementa cada tarea en un único paso aprobado — aprobás el plan una vez y luego corre de forma autónoma. Elimina la intervención humana *entre* tareas, no la verificación: cada tarea sigue siendo conducida por tests y commiteada individualmente, y se pausa ante fallos o pasos riesgosos.

Las skills también se activan automáticamente según lo que estés haciendo — diseñar una API dispara `api-and-interface-design`, construir UI dispara `frontend-ui-engineering`, y así sucesivamente.

### Comandos scaffold — stack extendido

| Comando | Stack | Compone |
|---------|-------|---------|
| `/scaffold-angular` | Angular | angular-frontend + frontend-ui-engineering + incremental + tdd |
| `/scaffold-react` | React | react-frontend + frontend-ui-engineering + incremental + tdd |
| `/scaffold-vue` | Vue | vue-frontend + frontend-ui-engineering + incremental + tdd |
| `/scaffold-node` | Node.js | nodejs-backend + api-and-interface-design + security + incremental + tdd |
| `/scaffold-springboot` | Spring Boot | springboot-backend + api-and-interface-design + security + incremental + tdd |
| `/scaffold-python` | Python/FastAPI | python-backend + api-and-interface-design + security + incremental + tdd |
| `/scaffold-go` | Go | go-backend + api-and-interface-design + security + incremental + tdd |
| `/scaffold-adk` | Google ADK | python-google-adk + python-backend + api-and-interface-design + incremental + tdd |

---

## Inicio rápido

<details>
<summary><b>Claude Code (recomendado)</b></summary>

**Instalación desde marketplace:**

```
/plugin marketplace add addyosmani/agent-skills
/plugin install agent-skills@addy-agent-skills
```

> **¿Errores SSH?** El marketplace clona repos vía SSH. Si no tenés claves SSH configuradas en GitHub, usá la URL HTTPS completa:
> ```bash
> /plugin marketplace add https://github.com/addyosmani/agent-skills.git
> /plugin install agent-skills@addy-agent-skills
> ```

**Local / desarrollo:**

```bash
git clone https://github.com/TU_USUARIO/agent-skills-dev-gh.git
claude --plugin-dir /ruta/a/agent-skills-dev-gh
```

</details>

<details>
<summary><b>Cursor</b></summary>

Copiá cualquier `SKILL.md` en `.cursor/rules/`, o referenciá el directorio `skills/` completo. Ver [docs/cursor-setup.md](docs/cursor-setup.md).

</details>

<details>
<summary><b>Antigravity CLI</b></summary>

Instalá como plugin nativo para skills, subagentes y slash commands. Ver [docs/antigravity-setup.md](docs/antigravity-setup.md).

```bash
agy plugin install https://github.com/TU_USUARIO/agent-skills-dev-gh.git
```

</details>

<details>
<summary><b>Gemini CLI</b></summary>

Instalá como skills nativas para auto-descubrimiento, o agregá al `GEMINI.md` para contexto persistente. Ver [docs/gemini-cli-setup.md](docs/gemini-cli-setup.md).

```bash
gemini skills install ./agent-skills-dev-gh/skills/
```

</details>

<details>
<summary><b>Windsurf</b></summary>

Agregá el contenido de las skills a tu configuración de reglas de Windsurf. Ver [docs/windsurf-setup.md](docs/windsurf-setup.md).

</details>

<details>
<summary><b>OpenCode</b></summary>

Usa ejecución de skills basada en agentes vía AGENTS.md y la herramienta `skill`. Ver [docs/opencode-setup.md](docs/opencode-setup.md).

</details>

<details>
<summary><b>GitHub Copilot</b></summary>

Usá las definiciones de agentes de `agents/` como personas de Copilot y el contenido de skills en `.github/copilot-instructions.md`. Ver [docs/copilot-setup.md](docs/copilot-setup.md).

</details>

<details>
<summary><b>Kiro IDE & CLI</b></summary>

Las skills para Kiro se ubican en `.kiro/skills/` y pueden almacenarse a nivel de proyecto o global. Kiro también soporta Agents.md. Ver docs de Kiro en https://kiro.dev/docs/skills/

</details>

<details>
<summary><b>Codex / Otros agentes</b></summary>

Las skills son Markdown puro — funcionan con cualquier agente que acepte system prompts o archivos de instrucciones. Ver [docs/getting-started.md](docs/getting-started.md).

</details>

---

## Las 32 skills

Los comandos anteriores son puntos de entrada. El pack incluye 32 skills en total — 24 del ciclo de vida base más 8 extensiones del stack extendido. Cada skill es un flujo de trabajo estructurado con pasos, gates de verificación y tablas anti-racionalización.

### Meta — Descubrir qué skill aplica

| Skill | Qué hace | Cuándo usarla |
|-------|----------|---------------|
| [using-agent-skills](skills/using-agent-skills/SKILL.md) | Mapea el trabajo entrante a la skill correcta y define reglas operativas compartidas | Al iniciar una sesión o decidir qué skill aplica |

### Definir — Clarificar qué construir

| Skill | Qué hace | Cuándo usarla |
|-------|----------|---------------|
| [interview-me](skills/interview-me/SKILL.md) | Entrevista de una pregunta a la vez que extrae lo que el usuario realmente quiere, hasta ~95% de confianza | El pedido es poco específico, o el usuario dice "entrevístame" |
| [idea-refine](skills/idea-refine/SKILL.md) | Pensamiento divergente/convergente estructurado para convertir ideas vagas en propuestas concretas | Tenés un concepto rough que necesita exploración |
| [spec-driven-development](skills/spec-driven-development/SKILL.md) | Escribir un PRD cubriendo objetivos, comandos, estructura, estilo de código, testing y límites antes de cualquier código | Iniciando un proyecto, feature o cambio significativo |

### Planificar — Descomponer

| Skill | Qué hace | Cuándo usarla |
|-------|----------|---------------|
| [planning-and-task-breakdown](skills/planning-and-task-breakdown/SKILL.md) | Descomponer specs en tareas pequeñas y verificables con criterios de aceptación y ordenamiento de dependencias | Tenés un spec y necesitás unidades implementables |

### Construir — Escribir el código

| Skill | Qué hace | Cuándo usarla |
|-------|----------|---------------|
| [incremental-implementation](skills/incremental-implementation/SKILL.md) | Slices verticales delgados — implementar, testear, verificar, commitear. Feature flags, defaults seguros, cambios con rollback | Cualquier cambio que toque más de un archivo |
| [test-driven-development](skills/test-driven-development/SKILL.md) | Red-Green-Refactor, pirámide de tests (80/15/5), tamaños de test, DAMP sobre DRY, Regla de Beyoncé, testing en browser | Implementando lógica, corrigiendo bugs o cambiando comportamiento |
| [context-engineering](skills/context-engineering/SKILL.md) | Darle al agente la información correcta en el momento correcto — rules files, empaquetado de contexto, integraciones MCP | Al iniciar una sesión, cambiar de tarea o cuando cae la calidad del output |
| [source-driven-development](skills/source-driven-development/SKILL.md) | Basar cada decisión de framework en documentación oficial — verificar, citar fuentes, marcar lo no verificado | Querés código autorizado con fuentes citadas para cualquier framework |
| [doubt-driven-development](skills/doubt-driven-development/SKILL.md) | Revisión adversarial en contexto fresco de cada decisión no trivial — CLAIM → EXTRACT → DOUBT → RECONCILE → STOP | El riesgo es alto (producción, seguridad, irreversible) o el código es desconocido |
| [frontend-ui-engineering](skills/frontend-ui-engineering/SKILL.md) | Arquitectura de componentes, design systems, gestión de estado, diseño responsivo, accesibilidad WCAG 2.1 AA | Construyendo o modificando interfaces de usuario |
| [api-and-interface-design](skills/api-and-interface-design/SKILL.md) | Diseño contract-first, Ley de Hyrum, Regla de Una Versión, semántica de errores, validación de límites | Diseñando APIs, límites de módulos o interfaces públicas |

### Stack extendido — Frontend

| Skill | Qué hace | Cuándo usarla |
|-------|----------|---------------|
| [angular-frontend](skills/angular-frontend/SKILL.md) | Standalone components, signals, OnPush, typed reactive forms, RxJS discipline, WCAG 2.1 AA | Construyendo o refactorizando Angular |
| [react-frontend](skills/react-frontend/SKILL.md) | Hooks, gestión de estado, composición de componentes, accesibilidad | Construyendo o refactorizando React |
| [vue-frontend](skills/vue-frontend/SKILL.md) | Composition API, Pinia, Vue Router, accesibilidad | Construyendo o refactorizando Vue |

### Stack extendido — Backend

| Skill | Qué hace | Cuándo usarla |
|-------|----------|---------------|
| [nodejs-backend](skills/nodejs-backend/SKILL.md) | Express/Fastify, validación, seguridad, testing con Jest/Vitest | Construyendo servicios Node.js |
| [springboot-backend](skills/springboot-backend/SKILL.md) | Java 21, Maven, Spring Boot 3.5, @RestController/@Service/@Repository, Bean Validation, JUnit 5 | Construyendo servicios Spring Boot |
| [python-backend](skills/python-backend/SKILL.md) | FastAPI/Django, Pydantic, pytest, async, seguridad | Construyendo servicios Python (sin ADK) |
| [go-backend](skills/go-backend/SKILL.md) | Idiomatic Go, interfaces, testing, seguridad | Construyendo servicios Go |
| [python-google-adk](skills/python-google-adk/SKILL.md) | ADK 2.0, Agent/Runner, SequentialAgent, ParallelAgent, LoopAgent, session state, FastAPI deploy | Construyendo pipelines multi-agente con Google ADK |

### Verificar — Demostrar que funciona

| Skill | Qué hace | Cuándo usarla |
|-------|----------|---------------|
| [browser-testing-with-devtools](skills/browser-testing-with-devtools/SKILL.md) | Chrome DevTools MCP para datos de runtime — inspección DOM, logs de consola, trazas de red, profiling de rendimiento | Construyendo o depurando algo que corre en un browser |
| [debugging-and-error-recovery](skills/debugging-and-error-recovery/SKILL.md) | Triage de cinco pasos: reproducir, localizar, reducir, corregir, guardar. Regla stop-the-line, fallbacks seguros | Los tests fallan, el build se rompe o el comportamiento es inesperado |

### Revisar — Gates de calidad antes del merge

| Skill | Qué hace | Cuándo usarla |
|-------|----------|---------------|
| [code-review-and-quality](skills/code-review-and-quality/SKILL.md) | Revisión en cinco ejes, tamaño de cambio (~100 líneas), etiquetas de severidad (Nit/Opcional/FYI), normas de velocidad | Antes de mergear cualquier cambio |
| [code-simplification](skills/code-simplification/SKILL.md) | Valla de Chesterton, Regla de 500, reducir complejidad preservando el comportamiento exacto | El código funciona pero es más difícil de leer o mantener de lo necesario |
| [security-and-hardening](skills/security-and-hardening/SKILL.md) | Prevención OWASP Top 10, patrones de auth, gestión de secretos, auditoría de dependencias, sistema de tres niveles | Manejando input de usuario, auth, almacenamiento de datos o integraciones externas |
| [performance-optimization](skills/performance-optimization/SKILL.md) | Enfoque measure-first — objetivos de Core Web Vitals, flujos de profiling, análisis de bundle, detección de anti-patrones | Existen requisitos de rendimiento o sospechás regresiones |

### Publicar — Deploy con confianza

| Skill | Qué hace | Cuándo usarla |
|-------|----------|---------------|
| [git-workflow-and-versioning](skills/git-workflow-and-versioning/SKILL.md) | Desarrollo trunk-based, commits atómicos, tamaño de cambio (~100 líneas), el patrón commit-as-save-point | Haciendo cualquier cambio de código (siempre) |
| [ci-cd-and-automation](skills/ci-cd-and-automation/SKILL.md) | Shift Left, Faster is Safer, feature flags, pipelines de quality gate, loops de feedback ante fallos | Configurando o modificando pipelines de build y deploy |
| [deprecation-and-migration](skills/deprecation-and-migration/SKILL.md) | Mentalidad código-como-pasivo, deprecación compulsoria vs. consultiva, patrones de migración, eliminación de código zombie | Removiendo sistemas viejos, migrando usuarios o discontinuando features |
| [documentation-and-adrs](skills/documentation-and-adrs/SKILL.md) | Architecture Decision Records, docs de API, estándares de documentación inline — documentar el *por qué* | Tomando decisiones arquitectónicas, cambiando APIs o publicando features |
| [observability-and-instrumentation](skills/observability-and-instrumentation/SKILL.md) | Logging estructurado, métricas RED, tracing OpenTelemetry, alertas basadas en síntomas — instrumentar mientras construís | Agregando telemetría, o publicando algo que corra en producción |
| [shipping-and-launch](skills/shipping-and-launch/SKILL.md) | Checklists de pre-lanzamiento, ciclo de vida de feature flags, rollouts graduales, procedimientos de rollback, setup de monitoreo | Preparándose para hacer deploy a producción |

---

## Personas de agentes

Personas especialistas preconfiguradas para revisiones focalizadas:

| Agente | Rol | Perspectiva |
|--------|-----|-------------|
| [code-reviewer](agents/code-reviewer.md) | Senior Staff Engineer | Revisión de código en cinco ejes con el estándar "¿lo aprobaría un staff engineer?" |
| [test-engineer](agents/test-engineer.md) | Especialista QA | Estrategia de testing, análisis de cobertura y el patrón Prove-It |
| [security-auditor](agents/security-auditor.md) | Ingeniero de Seguridad | Detección de vulnerabilidades, modelado de amenazas, evaluación OWASP |
| [web-performance-auditor](agents/web-performance-auditor.md) | Ingeniero de Rendimiento Web | Auditoría de Core Web Vitals con modos Quick/Deep y regla de honestidad de métricas; ejecutar con `/webperf` |

---

## Checklists de referencia

Material de consulta rápida que las skills cargan cuando lo necesitan:

| Referencia | Cubre |
|-----------|-------|
| [testing-patterns.md](references/testing-patterns.md) | Estructura de tests, naming, mocking, ejemplos React/API/E2E, anti-patrones |
| [security-checklist.md](references/security-checklist.md) | Chequeos pre-commit, auth, validación de input, headers, CORS, OWASP Top 10 |
| [performance-checklist.md](references/performance-checklist.md) | Objetivos Core Web Vitals, checklists frontend/backend, comandos de medición |
| [accessibility-checklist.md](references/accessibility-checklist.md) | Navegación por teclado, lectores de pantalla, diseño visual, ARIA, herramientas de testing |

---

## Cómo funcionan las skills

Cada skill sigue una anatomía consistente:

```
┌─────────────────────────────────────────────────┐
│  SKILL.md                                       │
│                                                 │
│  ┌─ Frontmatter ─────────────────────────────┐  │
│  │ name: nombre-en-minusculas-con-guiones    │  │
│  │ description: Guía a los agentes en [tarea]│  │
│  │              Usar cuando…                 │  │
│  └───────────────────────────────────────────┘  │
│  Overview         → Qué hace esta skill         │
│  When to Use      → Condiciones de activación   │
│  Process          → Flujo de trabajo paso a paso│
│  Rationalizations → Excusas + rebatimientos     │
│  Red Flags        → Señales de que algo va mal  │
│  Verification     → Requisitos de evidencia     │
└─────────────────────────────────────────────────┘
```

**Decisiones de diseño clave:**

- **Proceso, no prosa.** Las skills son flujos de trabajo que los agentes siguen, no docs de referencia que leen. Cada una tiene pasos, checkpoints y criterios de salida.
- **Anti-racionalización.** Cada skill incluye una tabla de excusas comunes que los agentes usan para saltarse pasos (ej. "agrego los tests después") con contraargumentos documentados.
- **La verificación no es negociable.** Cada skill termina con requisitos de evidencia — tests pasando, output del build, datos de runtime. "Parece correcto" nunca es suficiente.
- **Disclosure progresivo.** El `SKILL.md` es el punto de entrada. Las referencias de soporte se cargan solo cuando se necesitan, manteniendo el uso de tokens mínimo.

---

## Estructura del proyecto

```
agent-skills-dev-gh/
├── skills/                            # 32 skills (24 base + 8 stack extendido)
│   ├── interview-me/                  #   Definir
│   ├── idea-refine/                   #   Definir
│   ├── spec-driven-development/       #   Definir
│   ├── planning-and-task-breakdown/   #   Planificar
│   ├── incremental-implementation/    #   Construir
│   ├── context-engineering/           #   Construir
│   ├── source-driven-development/     #   Construir
│   ├── doubt-driven-development/      #   Construir
│   ├── frontend-ui-engineering/       #   Construir
│   ├── test-driven-development/       #   Construir
│   ├── api-and-interface-design/      #   Construir
│   ├── angular-frontend/              #   Construir — stack extendido
│   ├── react-frontend/                #   Construir — stack extendido
│   ├── vue-frontend/                  #   Construir — stack extendido
│   ├── nodejs-backend/                #   Construir — stack extendido
│   ├── springboot-backend/            #   Construir — stack extendido
│   ├── python-backend/                #   Construir — stack extendido
│   ├── go-backend/                    #   Construir — stack extendido
│   ├── python-google-adk/             #   Construir — stack extendido
│   ├── browser-testing-with-devtools/ #   Verificar
│   ├── debugging-and-error-recovery/  #   Verificar
│   ├── code-review-and-quality/       #   Revisar
│   ├── code-simplification/           #   Revisar
│   ├── security-and-hardening/        #   Revisar
│   ├── performance-optimization/      #   Revisar
│   ├── git-workflow-and-versioning/   #   Publicar
│   ├── ci-cd-and-automation/          #   Publicar
│   ├── deprecation-and-migration/     #   Publicar
│   ├── documentation-and-adrs/        #   Publicar
│   ├── observability-and-instrumentation/ # Publicar
│   ├── shipping-and-launch/           #   Publicar
│   └── using-agent-skills/            #   Meta: cómo usar este pack
├── agents/                            # 4 personas especialistas
├── references/                        # 5 checklists de referencia
├── hooks/                             # Hooks de ciclo de sesión
├── .claude/commands/                  # 17 slash commands (Claude Code)
├── .gemini/commands/                  # 7 slash commands (Gemini CLI)
├── commands/                          # 8 slash commands (Antigravity CLI)
├── .cursor/                           # MCP Engram + rule engram.mdc
├── .engram/                           # Config memoria persistente
├── plugin.json                        # Manifest Antigravity
├── STACK-EXTENSIONS.md                     # Detalle extensiones stack extendido
└── docs/                              # Guías de setup por herramienta
```

---

## Por qué Agent Skills

Los agentes de IA de código eligen por defecto el camino más corto — lo que frecuentemente significa saltarse specs, tests, revisiones de seguridad y las prácticas que hacen confiable al software. Agent Skills le da a los agentes flujos de trabajo estructurados que imponen la misma disciplina que los ingenieros senior aplican al código de producción.

Cada skill codifica juicio de ingeniería ganado con esfuerzo: *cuándo* escribir un spec, *qué* testear, *cómo* revisar y *cuándo* publicar. No son prompts genéricos — son el tipo de flujos de trabajo opinados y orientados a proceso que separan el trabajo de calidad de producción del trabajo de calidad de prototipo.

Las skills incorporan buenas prácticas de la cultura de ingeniería de Google — incluyendo conceptos de [Software Engineering at Google](https://abseil.io/resources/swe-book) y la [guía de prácticas de ingeniería](https://google.github.io/eng-practices/) de Google. Encontrarás la Ley de Hyrum en diseño de APIs, la Regla de Beyoncé y la pirámide de tests en testing, normas de tamaño de cambio y velocidad de revisión en code review, la Valla de Chesterton en simplificación, desarrollo trunk-based en flujo git, Shift Left y feature flags en CI/CD, y una skill dedicada a deprecación que trata el código como un pasivo.

---

## Contribuir

Las skills deben ser **específicas** (pasos accionables, no consejos vagos), **verificables** (criterios de salida claros con requisitos de evidencia), **probadas en batalla** (basadas en flujos de trabajo reales) y **mínimas** (solo lo necesario para guiar al agente).

Ver [docs/skill-anatomy.md](docs/skill-anatomy.md) para la especificación de formato y [CONTRIBUTING.es.md](CONTRIBUTING.es.md) para las guías de contribución.

---

## Licencia

MIT — usá estas skills en tus proyectos, equipos y herramientas.
