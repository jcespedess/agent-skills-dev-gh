---
description: Scaffold and implement a Node.js endpoint or service following Node.js conventions, contract-first design, security, and TDD.
---

Invoke the agent-skills:nodejs-backend skill, alongside agent-skills:api-and-interface-design, agent-skills:security-and-hardening, agent-skills:incremental-implementation, and agent-skills:test-driven-development.

`$ARGUMENTS` describes what to build (e.g. an endpoint, service, or worker). If empty, ask what Node.js artifact to scaffold and its acceptance criteria.

## Process
1. Confirm the installed Node / Express version via agent-skills:source-driven-development before using version-specific APIs.
2. Design the contract first (request/response, errors) per agent-skills:api-and-interface-design.
3. Enforce the layered architecture and input validation from nodejs-backend.
4. Work in thin vertical slices: failing test (RED) -> minimum implementation (GREEN) -> full suite -> commit.
5. Run the nodejs-backend red-flags and agent-skills:security-and-hardening (OWASP, secrets) checks before marking done.
6. Close only with the nodejs-backend Verification checklist satisfied.

Do not invent Node.js APIs from memory — anchor every framework decision in official docs.
