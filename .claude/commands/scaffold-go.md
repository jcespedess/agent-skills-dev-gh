---
description: Scaffold and implement a Go endpoint or service following Go conventions, contract-first design, security, and TDD.
---

Invoke the agent-skills:go-backend skill, alongside agent-skills:api-and-interface-design, agent-skills:security-and-hardening, agent-skills:incremental-implementation, and agent-skills:test-driven-development.

`$ARGUMENTS` describes what to build (e.g. an endpoint, service, or worker). If empty, ask what Go artifact to scaffold and its acceptance criteria.

## Process
1. Confirm the installed Go version via agent-skills:source-driven-development before using version-specific APIs.
2. Design the contract first (request/response, errors) per agent-skills:api-and-interface-design.
3. Enforce the layered architecture and input validation from go-backend.
4. Work in thin vertical slices: failing test (RED) -> minimum implementation (GREEN) -> full suite -> commit.
5. Run the go-backend red-flags and agent-skills:security-and-hardening (OWASP, secrets) checks before marking done.
6. Close only with the go-backend Verification checklist satisfied.

Do not invent Go APIs from memory — anchor every framework decision in official docs.
