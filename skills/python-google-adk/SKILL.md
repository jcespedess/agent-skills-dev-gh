---
name: python-google-adk
description: Build multi-agent systems with the Google Agent Development Kit (ADK) — Agent/Runner architecture, shared session state, sequential/parallel/loop workflow agents, function tools, and FastAPI deployment. Enforces deterministic-vs-LLM orchestration boundaries, state contracts via output_key, and ADK anti-pattern detection. Use when building, reviewing, or debugging Google ADK agents, runners, tools, or agent pipelines in Python.
---

# Python — Google ADK

## Overview
Google's Agent Development Kit (ADK) gives you LLM agents and a set of deterministic **workflow agents** (Sequential, Parallel, Loop) that orchestrate them. The most common failure is blurring the two: asking an LLM to "coordinate" what a `SequentialAgent` should run deterministically, or passing data between steps with ad-hoc globals instead of shared session state. This skill encodes the architecture so pipelines are deterministic where they should be, state flows through explicit contracts, and tools are clean Python functions.

> **Version note:** ADK moves fast — **ADK Python 2.0 GA** introduced graph workflows and collaborative agents. Always run `source-driven-development` against the installed `google-adk` version before relying on any signature below; treat the APIs here as architectural patterns, not pinned contracts.

Pair with `python-backend` (general Python discipline), `api-and-interface-design` (the FastAPI surface), `test-driven-development`, and `source-driven-development`.

## When to Use
- Building or refactoring ADK agents, runners, tools, or multi-agent pipelines.
- Deciding between an LLM agent and a deterministic workflow agent.
- Wiring agents into a FastAPI service for deployment.
- Debugging state that doesn't flow between agents, or non-deterministic orchestration.

## Core architecture (the mental model)
- **Agent / LlmAgent** — the "brain": `name`, `model`, `instruction`, `tools`, optional `output_key`.
- **Workflow agents** — deterministic orchestrators, *not* LLM-driven:
  - `SequentialAgent` — runs sub-agents in fixed order (a pipeline).
  - `ParallelAgent` — runs sub-agents concurrently against the same input.
  - `LoopAgent` — repeats sub-agents until a condition/max iterations.
- **Runner** — the execution engine: `Runner(agent=..., app_name=..., session_service=...)`.
- **SessionService** — conversation memory + shared state (`InMemorySessionService` for dev).
- **Tools** — plain Python functions (or `FunctionTool` / `LongRunningFunctionTool`); `AgentTool` exposes an agent as a tool.
- **Shared state** — the bus between agents: an agent writes its result to `output_key`; downstream agents read it by templating `{key}` in their instruction or via `tool_context.state`.

## Process

### 1. Choose orchestration: deterministic vs LLM-driven
- Fixed order of steps → `SequentialAgent`. Independent fan-out → `ParallelAgent`. Iterate until done → `LoopAgent`.
- Use an `LlmAgent` to *decide* only when the routing genuinely needs reasoning. Don't ask an LLM to sequence steps you already know the order of.

### 2. Define agents with explicit contracts
- Each `LlmAgent` has a focused `instruction`, the minimal `tools` it needs, and an `output_key` if a later step consumes its output.
- Downstream agents declare their inputs by referencing `{previous_output_key}` in their instruction — that reference *is* the contract.

### 3. Tools are clean, typed, documented functions
- Tool functions have type hints and a docstring (the LLM reads it to decide usage). Return structured dicts, not free text, when the result feeds logic.
- Validate inputs inside the tool; never trust the model to pass well-formed args.
- Use `LongRunningFunctionTool` for slow/async operations so the runner isn't blocked.

### 4. State and sessions
- Pass data between agents through session state (`output_key` → `{key}`), never through module globals or closures.
- Use `InMemorySessionService` for tests/dev; swap to a persistent service for production. Keep `app_name`/`user_id`/`session_id` consistent across `create_session` and `run`.

### 5. Run via the Runner (async-first)
- Build `types.Content(role="user", parts=[types.Part(text=...)])`, call `runner.run_async(user_id, session_id, new_message=content)`, iterate events, act on `event.is_final_response()`.
- Prefer `run_async` and `await`; only use the sync `run` for simple scripts.

### 6. Deploy behind FastAPI
- Use ADK's FastAPI integration (`get_fast_api_app`) to expose agents as endpoints, or wrap a `Runner` in your own route. Keep the agent definitions importable and side-effect-free at module load.
- Apply `python-backend` + `api-and-interface-design` to the HTTP surface (validation, error semantics, no secrets in code).

### 7. Verify (see Verification): tools unit-tested in isolation; pipeline tested with `InMemorySessionService`; state contracts asserted.

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "I'll let an LlmAgent coordinate the steps." | If the order is known, that's a `SequentialAgent` — deterministic, cheaper, testable. Don't pay an LLM to sequence. |
| "I'll pass data between agents with a global var." | State belongs in session (`output_key` → `{key}`). Globals break concurrency, sessions, and tests. |
| "The tool docstring/types are optional." | The model uses the signature and docstring to call the tool. Vague tools = wrong calls. |
| "One giant agent with all the tools is simpler." | A god-agent is unsteerable and untestable. Decompose into focused agents with clear contracts. |
| "I'll use the sync `run` everywhere." | ADK is async-first; blocking calls stall the runner. Use `run_async` and long-running tools for slow work. |
| "I memorized the ADK API." | ADK 2.0 changed orchestration (graph workflows). Verify against the installed version via source-driven-development. |
| "I'll skip validating tool inputs." | The model can pass malformed args. Validate at the tool boundary like any untrusted input. |

## Red Flags — stop and reconsider
- An `LlmAgent` whose instruction is "call A, then B, then C" instead of a `SequentialAgent`.
- Data passed between agents via module-level globals or closures rather than session state.
- A tool function with no type hints / docstring, or returning unstructured text that feeds logic.
- Inconsistent `app_name`/`user_id`/`session_id` between session creation and `run`.
- A single agent holding every tool in the system.
- Blocking I/O inside a tool without `LongRunningFunctionTool` / async.
- ADK API usage written from memory without a version check.
- Secrets/API keys hardcoded in agent or tool definitions.

## Verification (evidence required to close)
- [ ] `source-driven-development` consulted for the installed `google-adk` version (orchestration + tool APIs).
- [ ] Orchestration uses the right agent type (Sequential/Parallel/Loop vs LlmAgent for genuine routing).
- [ ] Inter-agent data flows through session state (`output_key` → `{key}`), no globals.
- [ ] Tools have type hints + docstrings, validate inputs, and return structured results; slow ops use long-running/async tools.
- [ ] Pipeline tested end-to-end with `InMemorySessionService`; tools unit-tested in isolation; state contracts asserted.
- [ ] FastAPI surface follows `api-and-interface-design` (validation, error semantics, no hardcoded secrets).
- [ ] App imports cleanly with no side effects at module load; `pytest` green.
