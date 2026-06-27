---
name: python-backend
description: Build Python services (FastAPI/Django) with type hints, layered architecture, and explicit error handling. Enforces input validation with Pydantic/schemas, dependency injection, async correctness, and Python anti-pattern detection (bare excepts, mutable default args, blocking calls in async, secrets in code). Use when building, reviewing, or refactoring Python APIs, services, or workers (non-ADK).
---

# Python Backend

## Overview
Python lets you ship fast and lets you ship landmines just as fast: a bare `except` that hides the real failure, a mutable default argument shared across calls, a blocking call inside an `async def` that stalls the event loop. This skill encodes the discipline a senior Python engineer applies — type hints everywhere, validation at the edges, a clean service layer, errors that surface — so the service is correct and maintainable.

> For **Google ADK / multi-agent** work, use `python-google-adk` instead (or alongside) — this skill covers general Python web/service backends.

Pair with `test-driven-development` (pytest), `api-and-interface-design` (contract-first), `security-and-hardening`, and `source-driven-development` (verify framework APIs against installed versions).

## When to Use
- Building or refactoring Python HTTP APIs (FastAPI/Django/Flask), services, or workers.
- Reviewing a Python diff (typing, validation, error handling, async correctness, layering).
- Diagnosing event-loop stalls in async code, or silent failures from broad excepts.
- Structuring a service into layers.

## Process

### 1. Type hints and explicit contracts
- Type-hint public functions, parameters, and returns. Run a type checker (mypy/pyright) in CI.
- Prefer dataclasses / Pydantic models for structured data over loose dicts.

### 2. Validate at the boundary
- Validate every external input with Pydantic (FastAPI) or serializers (Django/DRF). Reject early with clear, structured errors.
- Coerce and bound input; never trust client-supplied values downstream.

### 3. Layered architecture
- Router/view → service (business logic) → repository/data access. Views are thin: validate, call a service, shape the response.
- No ORM queries or business rules in views; no HTTP concerns in services.

### 4. Async correctness (when async)
- In `async def`, never call blocking I/O (sync DB drivers, `requests`, `time.sleep`, heavy CPU). Use async clients or run blocking work in a thread/executor.
- Run independent awaits concurrently (`asyncio.gather`); don't serialize what can be parallel.

### 5. Explicit error handling
- No bare `except:` and no `except Exception` that swallows. Catch specific exceptions; let unexpected ones propagate to a central handler.
- Define a domain error taxonomy; translate to HTTP in one place (FastAPI exception handlers / DRF). Don't leak tracebacks to clients.

### 6. Avoid the classic footguns
- No mutable default arguments (`def f(x=[])`) — use `None` and create inside.
- Be explicit about `None`; use `Optional[...]` and guard. Prefer pure functions for logic.

### 7. Configuration and secrets
- Read config from environment via a settings object (Pydantic `BaseSettings`), validated at startup. No secrets in code or committed `.env`. Fail fast on missing config.

### 8. Verify (see Verification): pytest (unit + API via TestClient), type check clean, no blocking calls in async.

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "A broad `except` keeps it from crashing." | It hides the real error and ships corrupt state. Catch specific exceptions; let the rest propagate. |
| "Type hints are optional." | They are the cheapest bug-catcher and contract you have. Hint public surfaces and check in CI. |
| "`requests` inside async is fine for now." | It blocks the event loop for every request. Use an async client or an executor. |
| "Validation can come later." | Unvalidated input is the root of security and 500 bugs. Validate at the boundary. |
| "`def f(items=[])` is convenient." | The default is shared across calls — a classic state-leak bug. Use `None`. |
| "ORM call in the view is quick." | Couples HTTP to data, untestable. View → service → repository. |
| "I'll hardcode the key for testing." | Secrets in code leak via git. Read from validated settings/env. |

## Red Flags — stop and reconsider
- `except:` / `except Exception:` that logs-and-continues or passes.
- Blocking I/O (`requests`, sync DB, `time.sleep`, heavy CPU) inside `async def`.
- External input used without Pydantic/serializer validation.
- Mutable default argument (`=[]`, `={}`).
- ORM queries or business rules inside a view/router.
- Missing type hints on public functions; no type checker in CI.
- Secrets/connection strings hardcoded or in committed `.env`.
- Serial `await`s over independent operations.

## Verification (evidence required to close)
- [ ] `source-driven-development` consulted for installed Python, FastAPI/Django versions.
- [ ] pytest passes (unit + API via TestClient/test client); validation and error paths covered.
- [ ] Type checker (mypy/pyright) clean on public surfaces.
- [ ] Every external input validated at the boundary; structured errors returned.
- [ ] No bare/broad excepts swallowing errors; domain errors translated to HTTP centrally.
- [ ] In async code: no blocking calls; independent awaits use `asyncio.gather`.
- [ ] No mutable default args; layering enforced (thin views, logic in services).
- [ ] Secrets from validated settings/env; no tracebacks leaked to clients.
