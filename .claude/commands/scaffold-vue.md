---
description: Scaffold and implement a Vue component or feature following Vue conventions, accessibility, and TDD.
---

Invoke the agent-skills:vue-frontend skill, alongside agent-skills:frontend-ui-engineering, agent-skills:incremental-implementation, and agent-skills:test-driven-development.

`$ARGUMENTS` describes what to build (e.g. a component, page, or feature). If empty, ask what Vue artifact to scaffold and its acceptance criteria.

## Process
1. Confirm the installed Vue 3 version via agent-skills:source-driven-development before using version-gated APIs.
2. Decide the component boundary and where state should live (per vue-frontend).
3. Work in thin vertical slices: write a failing test (RED), implement the minimum (GREEN), run the suite, commit.
4. Apply the Vue red-flags and accessibility (WCAG 2.1 AA) checks from vue-frontend before marking done.
5. Close only with the vue-frontend Verification checklist satisfied.

Do not invent Vue APIs from memory — anchor every framework decision in official docs.
