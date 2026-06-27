---
name: react-frontend
description: Build React UIs with hooks, component composition, and disciplined state management. Enforces accessibility (WCAG 2.1 AA), Suspense and error boundaries, stable keys, and React anti-pattern detection (prop drilling, effect misuse, derived state stored in state). Use when building, reviewing, or refactoring React components, custom hooks, or app architecture.
---

# React Frontend

## Overview
React rewards a few disciplines and punishes their absence quietly: state that lives at the wrong level, effects that run when they shouldn't, and re-renders nobody asked for. This skill encodes the decisions a senior React engineer makes by reflex so the agent doesn't ship code that "works" in the demo but leaks renders, breaks on the second click, or fails a screen reader.

Pair this skill with `test-driven-development` (React Testing Library), `frontend-ui-engineering` (design system, accessibility), and `source-driven-development` (verify API against the installed React version — hooks rules and Suspense semantics change across majors).

## When to Use
- Building or refactoring React components, pages, or custom hooks.
- Reviewing a React diff (composition, state placement, effect correctness, a11y).
- Deciding where state should live or how to share it.
- Diagnosing extra re-renders, stale closures, or "it renders twice" bugs.

Do **not** invent framework specifics from memory — confirm the installed React version first (hooks, `use`, Suspense, Server Components differ by major).

## Process

### 1. Decide the component boundary first
- One responsibility per component. If you're describing it with "and", split it.
- Prefer composition (`children`, slots) over configuration props that pile up boolean flags.
- Keep components presentational where possible; push data fetching and side effects to the edges (hooks, route loaders).

### 2. Place state at the lowest common ancestor
- Local state (`useState`/`useReducer`) by default. Lift only when two siblings must share.
- Reach for Context only for genuinely cross-cutting state (theme, auth, locale). Context is not a state manager — it re-renders every consumer on change.
- External store (Zustand/Redux/TanStack Query) when state is server-derived, shared widely, or needs caching. Server state ≠ client state: use a query library for the former.

### 3. Derive, don't duplicate
- Anything computable from props/state is computed during render, not stored in state and synced with an effect.
- `useMemo`/`useCallback` only after measuring, or when a referential identity is a dependency. Premature memoization is noise.

### 4. Use effects only for synchronization with the outside world
- An effect is for subscriptions, DOM measurement, network on mount — not for transforming props into state, and not as an event handler.
- Every effect declares a complete dependency array and a cleanup. If you can't write the cleanup, question the effect.
- Event-driven logic goes in event handlers, not effects.

### 5. Stable keys and predictable lists
- Keys are stable IDs from the data, never array index for dynamic/reorderable lists.
- Extract list items into their own component so each row memoizes independently.

### 6. Accessibility (WCAG 2.1 AA)
- Semantic elements first (`button`, `nav`, `label`); `div` + `onClick` is a last resort and needs `role` + keyboard handling.
- Every input has an associated `label`; every image has `alt`; focus is visible and managed on route/modal changes.
- Interactive controls are keyboard-operable; color is never the only signal.

### 7. Resilience
- Wrap async/lazy boundaries in `<Suspense>` with a fallback and an error boundary above them.
- Handle loading, empty, and error states explicitly — three states, not one happy path.

### 8. Verify (see Verification)
- Component tests with React Testing Library (query by role/label, not test IDs); accessibility check; a render-count sanity pass for hot paths.

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "I'll store the computed value in state to avoid recomputing." | Derived state in state is the #1 source of sync bugs. Compute during render; memoize only if measured hot. |
| "An effect is the easiest way to update X when Y changes." | If Y changes from an event, do it in the handler. Effects for prop→state sync cause cascades and double-renders. |
| "Index keys are fine, the list doesn't reorder." | Until it does, or items are inserted/removed. Use stable IDs; the cost of a real key is zero. |
| "Context is simpler than a store." | Context re-renders every consumer on any change. For frequently-updated shared state it's slower and harder to reason about. |
| "I'll add aria later." | Semantics are cheapest at write time. Retrofitting a11y onto `div` soup is a rewrite. |
| "useCallback everywhere can't hurt." | It adds allocation and dependency surface. Memoize for a reason, not by default. |
| "It works, the second render is harmless." | A second render often signals a state/effect smell that becomes a bug under concurrency. |

## Red Flags — stop and reconsider
- `useState` + `useEffect` pair whose only job is to copy/transform a prop into state.
- An effect with an empty or incomplete dependency array silencing the linter.
- `key={index}` on a list that can reorder, filter, or paginate.
- A component that both fetches data and renders complex UI and manages form state.
- `div`/`span` with `onClick` and no keyboard handler or `role`.
- A Context provider wrapping the whole app for state that changes on every keystroke.
- `dangerouslySetInnerHTML` with non-sanitized input.

## Verification (evidence required to close)
- [ ] `source-driven-development` consulted for the installed React major (hooks/Suspense/`use` semantics).
- [ ] Component tests pass, querying by role/label (RTL), covering loading/empty/error states.
- [ ] No derived-state-in-state and no prop→state sync effects remain.
- [ ] All effects have complete deps + cleanup; event logic lives in handlers.
- [ ] Lists use stable keys; hot lists have memoized item components.
- [ ] Accessibility pass: labels, alt text, keyboard operability, visible focus, non-color signaling.
- [ ] Render-count sanity check on the changed hot path (no unexpected cascades).
- [ ] Build passes with no new warnings.
