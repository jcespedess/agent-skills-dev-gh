---
description: Scaffold and implement a Google ADK agent or multi-agent pipeline following ADK orchestration patterns, state contracts, and TDD.
---

Invoke the agent-skills:python-google-adk skill, alongside agent-skills:python-backend, agent-skills:api-and-interface-design, agent-skills:incremental-implementation, and agent-skills:test-driven-development.

`$ARGUMENTS` describes the agent or pipeline to build. If empty, ask what ADK artifact to scaffold (single agent, sequential/parallel/loop pipeline, or tool) and its acceptance criteria.

## Process
1. Verify the installed `google-adk` version via agent-skills:source-driven-development (ADK 2.0 changed orchestration — graph workflows).
2. Choose orchestration deterministically: Sequential/Parallel/Loop for known flows; LlmAgent only for genuine reasoning-based routing.
3. Define agent contracts: focused instructions, minimal tools, `output_key` for data that downstream agents consume via `{key}`.
4. Build tools as typed, documented functions that validate inputs and return structured results.
5. Work in slices: test each tool in isolation, then the pipeline end-to-end with `InMemorySessionService` (RED -> GREEN -> commit).
6. If deploying, wrap behind FastAPI per agent-skills:api-and-interface-design (validation, no hardcoded secrets).
7. Close only with the python-google-adk Verification checklist satisfied.
