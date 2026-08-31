---
name: daily-control
description: Manage a local Markdown context through daily planning, evidence refresh, shutdown reflection, weekly review, setup, or source extension. Use when the user invokes Daily Control or asks an Agent to maintain this planning-and-reflection context.
---

# Daily Control

Guide the user through a local-first control loop. The Context Root is shared context, not application state; ordinary Agent reasoning performs the work.

## Resolve the route

Treat `/daily-control <route>` as the canonical invocation. Natural-language requests may select the same route.

- **setup** — read [`references/routes/setup.md`](references/routes/setup.md).
- **open** — read [`references/routes/open.md`](references/routes/open.md).
- **refresh** — read [`references/routes/refresh.md`](references/routes/refresh.md).
- **shutdown** — read [`references/routes/shutdown.md`](references/routes/shutdown.md).
- **weekly-review** — read [`references/routes/weekly-review.md`](references/routes/weekly-review.md).
- **extend** — read [`references/routes/extend.md`](references/routes/extend.md).

If the intent is ambiguous, ask one short question naming the likely routes.

## Resolve the Context Root

For routes other than setup, accept the current working directory only when it contains both `AGENTS.md` and `context/contracts/daily.md`. Otherwise ask the user for the Context Root. Do not scan other directories or use a global registry.

For setup, the user may choose the current directory or name another target. The setup route establishes the markers.

## Invariants

- Keep every Daily Control write inside the confirmed Context Root.
- Read the Context Root `AGENTS.md` before changing context.
- Treat durable Daily, Weekly, Area, Project, Routine, and Evidence records as canonical. `context/now.md` is a rebuildable cache.
- Let the user decide priorities, consequential constraints, interpretation, permissions, and final acceptance.
- Present factual Evidence separately from human interpretation.
- Read back every changed file before reporting completion. Report partial or blocked work exactly.

Finish when the selected route's completion criteria are satisfied; do not continue into another route unless the user asked for it.
