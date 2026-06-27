---
description: Scaffold and implement a Spring Boot endpoint or service following Spring Boot conventions, contract-first design, security, and TDD.
---

Invoke the agent-skills:springboot-backend skill, alongside agent-skills:api-and-interface-design, agent-skills:security-and-hardening, agent-skills:incremental-implementation, and agent-skills:test-driven-development.

`$ARGUMENTS` describes what to build (e.g. an endpoint, service, or worker). If empty, ask what Spring Boot artifact to scaffold and its acceptance criteria.

## Process
1. Confirm the installed Spring Boot 3.5 / Java 21 version via agent-skills:source-driven-development before using version-specific APIs.
2. Design the contract first (request/response, errors) per agent-skills:api-and-interface-design.
3. Enforce the layered architecture and input validation from springboot-backend.
4. Work in thin vertical slices: failing test (RED) -> minimum implementation (GREEN) -> full suite -> commit.
5. Run the springboot-backend red-flags and agent-skills:security-and-hardening (OWASP, secrets) checks before marking done.
6. Close only with the springboot-backend Verification checklist satisfied.

Do not invent Spring Boot APIs from memory — anchor every framework decision in official docs.
