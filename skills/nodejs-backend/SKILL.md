---
name: nodejs-backend
description: Build Node.js services (Express/Fastify) with async/await discipline, layered architecture, and safe error propagation. Enforces input validation at boundaries, no blocking the event loop, structured error handling, and Node anti-pattern detection (unhandled rejections, callback/await mixing, secrets in code). Use when building, reviewing, or refactoring Node.js APIs, services, or workers.
---

# Node.js Backend

## Overview
Node's single-threaded event loop is fast until something blocks it, and forgiving until an unhandled rejection takes the process down. This skill encodes the discipline a senior Node engineer applies — async/await everywhere with real error handling, validation at the edges, thin controllers over a service layer — so the service stays responsive and failures are explicit rather than silent. The layered shape (route → service → repository) mirrors enterprise patterns a Spring background already knows.

Pair with `test-driven-development` (Vitest/Jest + supertest), `api-and-interface-design` (contract-first), `security-and-hardening` (OWASP, secrets), and `source-driven-development` (verify framework/runtime APIs against installed versions).

## When to Use
- Building or refactoring Node.js HTTP APIs (Express/Fastify), services, or workers.
- Reviewing a Node diff (async correctness, error handling, validation, layering).
- Diagnosing unhandled rejections, event-loop stalls, or memory growth.
- Structuring a service into layers.

## Process

### 1. Async/await, end to end
- Use `async/await` consistently; don't mix callbacks and promises in the same flow. Promisify legacy callback APIs at the boundary.
- Every `await` that can reject is inside a `try/catch` or handled by centralized error middleware. No floating promises.
- Run independent awaits with `Promise.all`; don't serialize what can be concurrent.

### 2. Don't block the event loop
- No synchronous CPU-heavy work (large JSON, crypto, sync fs) on the request path. Offload to worker threads, streams, or a queue.
- Stream large payloads instead of buffering them in memory.

### 3. Layered architecture
- Route/controller → service (business logic) → repository (data). Controllers are thin: validate, call a service, shape the response.
- No DB calls or business rules in route handlers; no HTTP concerns in services.

### 4. Validate at the boundary
- Validate and type every external input (body, query, params, headers) with a schema validator (Zod/Joi/valibot). Reject early with clear errors.
- Never trust client input; coerce and bound it before use.

### 5. Structured error handling
- Define an error taxonomy (e.g. `AppError` with status + code). Throw typed errors in services; translate to HTTP in one place (error middleware).
- Set `process.on('unhandledRejection')` / `uncaughtException` handlers for observability; never swallow errors silently.
- Return consistent error shapes; don't leak stack traces to clients.

### 6. Configuration and secrets
- Read config from environment (validated at startup); no secrets, tokens, or connection strings in code or committed `.env`.
- Fail fast on missing required config.

### 7. Resource lifecycle
- Pool DB connections; close them on shutdown. Handle `SIGTERM` for graceful shutdown (drain, then exit).

### 8. Verify (see Verification): integration tests with supertest, validation tests, no unhandled rejections.

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "I'll catch the rejection later." | A floating promise becomes an unhandled rejection that can crash the process. Handle every await. |
| "A little sync work won't hurt." | Sync CPU work blocks the whole event loop for every user. Offload or stream. |
| "Validation slows me down." | Unvalidated input is the root of most security and 500 bugs. Validate at the boundary, always. |
| "DB call straight in the route is fine." | It couples HTTP to data and is untestable. Route → service → repository. |
| "I'll put the API key in the code for now." | Secrets in code leak via git forever. Read from validated env. |
| "Mixing a callback in here is quicker." | Mixed callback/promise flows drop errors. Promisify at the edge, await consistently. |
| "Awaiting them one by one is clearer." | Independent awaits should be `Promise.all`. Serial awaits waste latency. |

## Red Flags — stop and reconsider
- An `async` call with no `try/catch` and no centralized error handler (floating promise).
- Synchronous CPU/fs/crypto work on the request path.
- DB queries or business rules inside a route handler.
- External input used without schema validation.
- `catch` blocks that swallow errors or log-and-continue silently.
- Secrets/connection strings hardcoded or in committed `.env`.
- Serial `await` chain over independent operations.
- No graceful shutdown / connection cleanup.

## Verification (evidence required to close)
- [ ] `source-driven-development` consulted for installed Node, Express/Fastify, and validator versions.
- [ ] Integration tests pass (supertest); validation and error-path tests included.
- [ ] All awaits handled; no floating promises; `unhandledRejection` handler present.
- [ ] No blocking work on the request path; large payloads streamed.
- [ ] Layering enforced: thin controllers, logic in services, data in repositories.
- [ ] Every external input validated at the boundary with a schema.
- [ ] Errors use a typed taxonomy, translated to HTTP in one place; no stack traces leaked.
- [ ] Secrets read from validated env; graceful shutdown handled.
- [ ] Build/lint passes with no new warnings.
