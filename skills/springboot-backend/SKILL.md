---
name: springboot-backend
description: Build Spring Boot services (Maven, Java 21, Spring Boot 3.5) with constructor injection, layered architecture, and JPA done right. Enforces transaction boundaries, DTO/entity separation, bean validation, and Spring anti-pattern detection (field injection, fat controllers, N+1 queries, entities as API payloads). No Gradle. Use when building, reviewing, or refactoring Spring Boot APIs, services, or persistence.
---

# Spring Boot Backend

## Overview
Spring Boot does a lot for you, which is exactly why the failure modes are subtle: field injection that hides dependencies, an `@Transactional` that doesn't fire because the call was internal, a lazy association that fans out into N+1 queries, an entity serialized straight to the API. This skill encodes the discipline a senior Spring engineer applies so the layered architecture stays clean, transactions are correct, and the persistence layer doesn't quietly melt under load.

**Stack assumption (referencia del proyecto):** Maven, Java 21, Spring Boot 3.5. **No Gradle.** Pair with `test-driven-development` (JUnit 5 + MockMvc + Testcontainers), `api-and-interface-design` (contract-first, DTOs), `security-and-hardening`, and `source-driven-development` (verify Spring APIs against the installed version).

## When to Use
- Building or refactoring Spring Boot controllers, services, or repositories.
- Reviewing a Spring diff (injection, transactions, DTO boundaries, query shape).
- Diagnosing N+1 queries, lazy-init exceptions, or transaction-not-applied bugs.
- Designing the layering and API payload contracts.

## Process

### 1. Constructor injection, always
- Inject dependencies via the constructor (final fields). Never field injection (`@Autowired` on fields) — it hides dependencies and breaks testability and immutability.
- Depend on interfaces where a seam is useful; keep beans single-responsibility.

### 2. Layered architecture
- Controller (`@RestController`) → Service (`@Service`, business logic + transactions) → Repository (`@Repository`/Spring Data).
- Controllers are thin: validate input, call a service, map to a response. No business logic or persistence in controllers.

### 3. DTOs at the boundary — never expose entities
- Accept and return **DTOs/records**, not JPA entities. Map explicitly (MapStruct or hand-mapped). Entities leaking into the API couples your schema to your contract and invites lazy-loading serialization bugs.
- Validate request DTOs with Bean Validation (`@Valid`, `@NotNull`, `@Size`...).

### 4. Transactions done right
- Put `@Transactional` on service methods, not controllers or repositories. Keep transactions short.
- Remember self-invocation doesn't trigger the proxy: an internal `this.method()` call won't start a new transaction. Mark read paths `@Transactional(readOnly = true)`.

### 5. JPA without N+1
- Default associations to `LAZY`; fetch what you need with `JOIN FETCH` / entity graphs, not by triggering lazy loads in a loop.
- Watch for the N+1 pattern (one query + one-per-row). Page large result sets; never load unbounded collections.
- Don't do queries inside loops; batch.

### 6. Error handling
- Centralize with `@RestControllerAdvice` / `@ExceptionHandler`; return consistent problem responses (RFC 7807 style). Don't leak stack traces or entity internals.
- Throw domain exceptions in services; translate to HTTP in the advice.

### 7. Configuration and secrets
- Externalize config (`application.yml` + profiles + env). No secrets in code or committed properties. Fail fast on missing required config.

### 8. Verify (see Verification): slice tests + integration tests with Testcontainers; assert query counts on hot paths.

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Field injection is less boilerplate." | It hides dependencies, blocks `final`, and complicates tests. Use constructor injection. |
| "I'll return the entity directly, it's faster." | Entities as payloads couple schema to API and trigger lazy-loading serialization bugs. Use DTOs. |
| "`@Transactional` on the controller is fine." | Transactions belong on service methods; on controllers they wrap too much and miss the boundary. |
| "The lazy association is convenient in the loop." | That's N+1. Use `JOIN FETCH`/entity graphs and assert query counts. |
| "Self-call into the @Transactional method works." | It doesn't — the proxy is bypassed. Move the method to another bean or restructure. |
| "I'll handle errors per-controller." | Scattered handling is inconsistent. Centralize with `@RestControllerAdvice`. |
| "Gradle would be quicker here." | Stack standard is Maven. Stay on Maven. |

## Red Flags — stop and reconsider
- `@Autowired` on a field instead of constructor injection.
- A JPA entity used as a `@RequestBody` or returned from a controller.
- `@Transactional` on a controller, or a `@Transactional` method called via `this.` from the same bean.
- A repository call inside a `for`/`stream` loop (N+1).
- `FetchType.EAGER` on collections, or unbounded `findAll()` on large tables.
- Business logic or persistence code inside a controller.
- Stack traces / entity internals returned to clients.
- Secrets in `application.properties`/`.yml` committed to git.
- A `build.gradle` appearing in the project.

## Verification (evidence required to close)
- [ ] `source-driven-development` consulted for Spring Boot 3.5 / Java 21 APIs.
- [ ] Tests pass: web slice (MockMvc) + integration with Testcontainers; query counts asserted on hot paths.
- [ ] Constructor injection throughout; no field `@Autowired`.
- [ ] Controllers are thin; DTOs/records at the boundary; entities never serialized to the API.
- [ ] `@Transactional` on services (readOnly where applicable); no proxy-bypassing self-calls.
- [ ] No N+1: associations LAZY, fetched via JOIN FETCH/entity graphs; no queries in loops.
- [ ] Errors centralized via `@RestControllerAdvice`; no leaked internals.
- [ ] Secrets externalized; build is Maven (Java 21), no Gradle.
- [ ] `mvn verify` passes.
