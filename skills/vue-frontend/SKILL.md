---
name: vue-frontend
description: Build Vue 3 apps with the Composition API, single-file components, and correct reactivity. Enforces Pinia state patterns, props/emits contracts, accessibility (WCAG 2.1 AA), and Vue anti-pattern detection (reactivity loss from destructuring, watcher overuse, prop mutation). Use when building, reviewing, or refactoring Vue components, composables, or Pinia stores.
---

# Vue Frontend

## Overview
Vue's reactivity is its superpower and its sharpest edge: destructure a `reactive` object or hand off a `.value` at the wrong moment and the UI silently stops updating — no error, just stale pixels. This skill encodes the Composition-API discipline a senior Vue engineer applies so reactivity stays intact, components own clear contracts, and state lives in composables/stores rather than smeared across watchers.

Pair with `test-driven-development` (Vue Test Utils / Vitest), `frontend-ui-engineering` (design system, a11y), and `source-driven-development` (confirm Vue 3.x / Pinia / Nuxt specifics against installed versions).

## When to Use
- Building or refactoring Vue 3 SFCs, composables, or Pinia stores.
- Reviewing a Vue diff (reactivity correctness, contracts, a11y).
- Diagnosing "the value changed but the template didn't update" bugs.
- Deciding between local `ref`, a composable, or a Pinia store.

Confirm the installed Vue/Pinia/Nuxt versions before relying on any specific API.

## Process

### 1. Composition API + `<script setup>` by default
- Use `<script setup>` for new components: less boilerplate, better type inference.
- One concern per composable. Extract reusable stateful logic into `useX()` composables that return refs and functions.

### 2. Choose the right reactivity primitive
- `ref()` for primitives and when you need a stable reference to pass around.
- `reactive()` for objects you won't destructure.
- `computed()` for anything derivable — never recompute manually in a watcher.
- Do **not** destructure a `reactive()` object or store without `toRefs()`/`storeToRefs()`; destructuring breaks reactivity.

### 3. Watchers are a last resort
- Prefer `computed` over `watch`. Use `watch`/`watchEffect` only for side effects (fetching on id change, syncing to localStorage), not for deriving values.
- Always consider the cleanup (`onWatcherCleanup` / returned stop) and `immediate`/`deep` cost.

### 4. Component contracts: typed props + explicit emits
- Declare `defineProps` with types and `defineEmits` for every event. The emits list is the component's public output contract.
- **Never mutate a prop.** Emit an event or use a local copy / `v-model` with a writable computed.
- Use `v-model` (with `defineModel` in 3.4+) for two-way binding instead of ad-hoc prop+event pairs.

### 5. State placement
- Local `ref` by default → composable when shared logic → **Pinia** store when shared across routes/components or server-derived.
- In Pinia, read state with `storeToRefs()` to keep reactivity; call actions directly. Keep stores small and domain-scoped.

### 6. Lists and rendering
- `v-for` always has a stable `:key` from data (not index for dynamic lists).
- Never combine `v-if` and `v-for` on the same element; filter via a `computed` instead.

### 7. Accessibility (WCAG 2.1 AA)
- Semantic elements first; labels for inputs; `alt` for images; manage focus on route/dialog changes.
- Keyboard-operable interactive elements; visible focus; color is never the only signal.

### 8. Verify (see Verification).

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "I'll destructure the store, it's cleaner." | Destructuring a reactive/store drops reactivity. Use `storeToRefs()` / `toRefs()`. |
| "A watcher is the obvious way to compute this." | If it's derivable, it's a `computed`. Watchers for derivation cause stale/echo bugs and extra runs. |
| "I just mutate the prop directly, it's faster." | Mutating props breaks one-way data flow and warns in dev. Emit or use a writable computed. |
| "`v-if` with `v-for` on one tag is fine." | Precedence pitfalls and wasted work. Filter with a computed, then `v-for`. |
| "Everything goes in one big store." | Giant stores become god-objects. Scope stores by domain. |
| "Index keys are fine." | Not for dynamic/reorderable lists — Vue's diff misbehaves. Use stable IDs. |
| "I'll add a11y later." | Cheapest at write time; retrofitting is a rewrite. |

## Red Flags — stop and reconsider
- `const { x } = reactive(obj)` or `const { x } = useStore()` without `toRefs`/`storeToRefs`.
- A `watch` whose body just assigns a value that could be a `computed`.
- Direct assignment to a `props.*` field.
- `v-if` and `v-for` on the same element.
- `:key="index"` on a list that filters/reorders/paginates.
- A composable that mutates global state instead of returning it.
- Interactive `div`/`span` without role/keyboard handling.

## Verification (evidence required to close)
- [ ] `source-driven-development` consulted for installed Vue 3.x / Pinia / Nuxt versions.
- [ ] Component/composable tests pass (Vue Test Utils / Vitest), querying by role/label.
- [ ] No reactivity-breaking destructuring; stores read via `storeToRefs()`.
- [ ] No watchers doing work a `computed` should; remaining watchers have clear side-effect purpose + cleanup.
- [ ] No prop mutation; two-way binding uses `v-model`/writable computed.
- [ ] `v-for` keys are stable; no `v-if`+`v-for` on the same element.
- [ ] Accessibility pass: labels, alt, keyboard, visible focus, non-color signaling.
- [ ] Build passes with no new warnings.
