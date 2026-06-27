---
name: angular-frontend
description: Build Angular apps with standalone components, signals, typed reactive forms, and RxJS discipline. Enforces OnPush change detection, dependency injection patterns, accessibility (WCAG 2.1 AA), and Angular anti-pattern detection (manual subscriptions without teardown, logic in templates, any-typed forms). Use when building, reviewing, or refactoring Angular components, services, or state.
---

# Angular Frontend

## Overview
Angular gives you a lot of structure and a lot of ways to leak: a subscription without teardown, change detection running on every tick, business logic smeared across templates. This skill encodes the discipline a senior Angular engineer applies — standalone components, signals/OnPush for predictable rendering, typed forms, and RxJS that always completes — so apps stay fast and the framework's strengths (DI, typing) actually pay off. It maps directly to the enterprise patterns a Java/Spring background expects: DI, layered services, clear contracts.

Pair with `test-driven-development` (Jasmine/Karma or Vitest + Testing Library), `frontend-ui-engineering` (design system, a11y), and `source-driven-development` (confirm the installed Angular version — signals, standalone, and control flow `@if/@for` differ by major).

## When to Use
- Building or refactoring Angular standalone components, services, or state.
- Reviewing an Angular diff (change detection, subscriptions, forms, a11y).
- Diagnosing extra change-detection cycles or memory leaks from subscriptions.
- Deciding between signals, RxJS, and a store for state.

Confirm the installed Angular major before relying on any API (signals/`@if`/standalone are version-gated).

## Process

### 1. Standalone-first architecture
- New components/directives/pipes are `standalone: true`; import what they use directly. Avoid NgModules for new code unless the version requires them.
- One responsibility per component; presentational components take inputs and emit outputs, smart components wire services.

### 2. Change detection: OnPush + signals
- Set `changeDetection: ChangeDetectionStrategy.OnPush` on components by default.
- Prefer **signals** for component state; they integrate with OnPush and make derived state explicit (`computed`). Use `effect()` sparingly and only for side effects.
- Pass data down via typed `input()`/`@Input()`, up via `output()`/`@Output()`.

### 3. RxJS that always completes
- Every manual `subscribe` has a teardown. Prefer the `async` pipe in templates over manual subscription; when subscribing in code, use `takeUntilDestroyed()` (or a destroy subject).
- Compose with operators (`switchMap`, `combineLatest`); avoid nested subscribes. Use `switchMap` for cancellable request-per-input flows.

### 4. Dependency injection
- Inject via `inject()` or constructor; depend on abstractions for testability. Scope services with `providedIn: 'root'` unless they need a narrower lifecycle.
- Keep business logic in services, not components or templates.

### 5. Typed reactive forms
- Use strictly-typed reactive forms (`FormGroup<...>`, `NonNullableFormBuilder`); never `any`-typed controls.
- Validation lives in the form model; templates render state, they don't compute it.

### 6. Templates stay declarative
- No function calls doing real work in template bindings (they run every change detection). Move to signals/computed or memoized values.
- Use the new control flow (`@if`/`@for` with `track`) where available; `@for` always has `track`.

### 7. Accessibility (WCAG 2.1 AA)
- Semantic elements; labels for inputs; manage focus on route/dialog changes; keyboard operability; visible focus; color never the only signal.

### 8. Verify (see Verification).

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "I'll subscribe and unsubscribe later." | A subscription without teardown is a leak. Use the `async` pipe or `takeUntilDestroyed()`. |
| "Default change detection is fine." | Default CD runs on every event tick app-wide. OnPush + signals make rendering predictable and fast. |
| "A function in the template is convenient." | It re-runs every change-detection cycle. Use a signal/computed or precomputed value. |
| "Nested subscribes are easier to read." | They leak and race. Compose with `switchMap`/`combineLatest`. |
| "Untyped forms are quicker to write." | `any` forms lose the one thing Angular gives you — type safety. Use typed reactive forms. |
| "Business logic in the component is fine for now." | Logic belongs in injectable services (testable, reusable). Components wire, services decide. |
| "I'll add a11y later." | Cheapest at write time; retrofitting is a rewrite. |

## Red Flags — stop and reconsider
- A `.subscribe()` with no `takeUntilDestroyed`/destroy subject and no `async` pipe.
- A component without `OnPush` re-rendering on unrelated events.
- A method call inside a template binding that does computation or I/O.
- Nested `subscribe` blocks instead of higher-order operators.
- `FormControl` / `FormGroup` without generic types, or `any` in form models.
- Business logic living in a component or template instead of a service.
- `@for` without `track`.
- Interactive `div`/`span` without role/keyboard handling.

## Verification (evidence required to close)
- [ ] `source-driven-development` consulted for the installed Angular major (signals/standalone/control flow).
- [ ] Component/service tests pass, querying by role/label.
- [ ] Components are OnPush; signals/computed used for state and derivation.
- [ ] Every subscription has teardown (or uses the `async` pipe); no nested subscribes.
- [ ] Forms are strictly typed; validation in the model, not the template.
- [ ] Templates are declarative (no work in bindings); `@for` uses `track`.
- [ ] Business logic lives in injectable services.
- [ ] Accessibility pass: labels, alt, keyboard, visible focus, non-color signaling.
- [ ] `ng build` passes with no new warnings.
