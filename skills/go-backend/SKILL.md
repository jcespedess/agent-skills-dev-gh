---
name: go-backend
description: Build Go services with idiomatic error handling, safe concurrency, and context propagation. Enforces wrapped errors (%w, errors.Is/As), goroutine lifecycle discipline, table-driven tests, and Go anti-pattern detection (goroutine leaks, ignored errors, naked returns, premature interfaces). Use when building, reviewing, or refactoring Go APIs, services, workers, or CLIs.
---

# Go Backend

## Overview
Go is small on purpose: the language won't stop you from leaking a goroutine, swallowing an error, or sharing memory without a lock. Correctness comes from discipline, not from the compiler. This skill encodes the habits a senior Go engineer applies so services handle errors explicitly, goroutines have owners and exits, and `context` actually cancels work.

Pair with `test-driven-development` (table-driven tests, the race detector), `api-and-interface-design` (contract-first handlers), and `source-driven-development` (verify stdlib/module APIs against the installed Go version).

## When to Use
- Building or refactoring Go HTTP/gRPC services, workers, or CLIs.
- Reviewing a Go diff (error handling, concurrency safety, context, tests).
- Diagnosing goroutine leaks, data races, or deadlocks.
- Designing package boundaries and interfaces.

## Process

### 1. Errors are values — handle every one
- Check and handle (or deliberately wrap) every returned `error`. Never `_ = err`.
- Wrap with context using `fmt.Errorf("doing X: %w", err)` so the chain is inspectable.
- Compare with `errors.Is` (sentinels) and `errors.As` (typed errors), never string matching.
- Define sentinel errors (`var ErrNotFound = errors.New(...)`) at package boundaries for callers to branch on.
- Return errors; reserve `panic` for truly unrecoverable, programmer-error states.

### 2. Concurrency: every goroutine has an owner and an exit
- Before launching a goroutine, answer: who waits for it, and how does it stop?
- Propagate `context.Context` as the first parameter through call chains; select on `ctx.Done()` in loops and blocking sends/receives.
- Use `sync.WaitGroup` / `errgroup` to await goroutines; never fire-and-forget unbounded.
- Channels: the sender closes, never the receiver. Size buffers deliberately. Avoid sharing memory — communicate, or guard with `sync.Mutex` when shared state is unavoidable.
- Always run tests with `-race` for concurrent code.

### 3. Context discipline
- `ctx` is the first arg, never stored in a struct. Don't pass `nil` — use `context.TODO()` if genuinely unknown.
- Set deadlines/timeouts on outbound calls; honor cancellation in long loops.
- Never put request-scoped business data in `context.Value` beyond cross-cutting metadata (trace IDs, auth).

### 4. Interfaces: accept interfaces, return structs — when proven
- Define interfaces at the consumer, not the producer, and only when there are multiple implementations or a test seam is needed. Don't pre-abstract.
- Keep interfaces small (1–3 methods). `io.Reader`-sized, not god-interfaces.

### 5. Package and API shape
- Package names are short, lowercase, no stutter (`http.Client`, not `http.HTTPClient`).
- Exported surface is minimal; zero values are useful where possible.
- Constructors return concrete types; validate inputs at the boundary.

### 6. Resource lifecycle
- `defer` Close/Unlock right after acquire; check `Close` errors where they matter (writers).
- No leaked file handles, rows, or response bodies (`defer resp.Body.Close()`).

### 7. Verify (see Verification): table-driven tests + `-race` + `go vet`.

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "I'll handle this error later / it can't happen." | Unchecked errors are how Go programs corrupt silently. Handle or wrap every one. |
| "A quick `go func()` for the background work." | A goroutine without an owner and an exit is a leak waiting for production. Define both first. |
| "I'll add the interface now so it's flexible." | Premature interfaces add indirection with no caller. Add at the consumer when a second impl exists. |
| "Comparing the error string is fine." | Brittle; breaks on wrapping/rewording. Use `errors.Is`/`errors.As`. |
| "Storing ctx in the struct is convenient." | It breaks cancellation semantics and lifetimes. Pass it per-call as the first arg. |
| "The race detector is too slow to run." | A data race is undefined behavior. Run `-race` on concurrent paths, always. |
| "Naked return keeps it short." | Named-return + naked `return` hides what's returned and ships subtle bugs. Be explicit. |

## Red Flags — stop and reconsider
- `_ = err` or a returned error never checked.
- `go func(){...}()` with no `WaitGroup`/`errgroup`/cancellation.
- A channel closed by the receiver, or an unbounded buffered channel as a queue.
- `context.Context` stored as a struct field, or `nil` context passed.
- An interface with one implementation defined next to that implementation.
- Missing `defer resp.Body.Close()` / `defer rows.Close()`.
- Error compared via `strings.Contains(err.Error(), ...)`.
- Shared map/slice written from multiple goroutines without a mutex.

## Verification (evidence required to close)
- [ ] `source-driven-development` consulted for the installed Go version and module APIs.
- [ ] Table-driven tests pass; concurrent code tested with `go test -race`.
- [ ] `go vet` clean; no unchecked errors (errors handled or wrapped with `%w`).
- [ ] Every goroutine has a defined owner and exit path; channels closed by the sender.
- [ ] `context` flows as first arg with deadlines on outbound calls; no ctx in structs.
- [ ] Interfaces live at the consumer and are minimal; no premature abstraction.
- [ ] Resources closed via `defer`; no leaked bodies/rows/handles.
- [ ] `go build ./...` passes.
