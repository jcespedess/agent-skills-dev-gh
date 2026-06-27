---
description: Scaffold and implement a Angular component or feature following Angular conventions, accessibility, and TDD.
---

Invoke the agent-skills:angular-frontend skill, alongside agent-skills:frontend-ui-engineering, agent-skills:incremental-implementation, and agent-skills:test-driven-development.

`$ARGUMENTS` describes what to build (e.g. a component, page, or feature). If empty, ask what Angular artifact to scaffold and its acceptance criteria.

## Process
1. Confirm the installed Angular version via agent-skills:source-driven-development before using version-gated APIs.
2. Decide the component boundary and where state should live (per angular-frontend).
3. Work in thin vertical slices: write a failing test (RED), implement the minimum (GREEN), run the suite, commit.
4. Apply the Angular red-flags and accessibility (WCAG 2.1 AA) checks from angular-frontend before marking done.
5. Close only with the angular-frontend Verification checklist satisfied.

Do not invent Angular APIs from memory — anchor every framework decision in official docs.
