---
name: daily-control
description: Run a local Markdown control loop for daily planning, evidence refresh, shutdown reflection, weekly review, setup, help, or source extension. Use when the user invokes Daily Control, asks what to do next in a Daily Control Context Root, or wants an Agent to maintain this planning-and-reflection context.
license: MIT. See LICENSE
metadata:
  version: "0.1.0"
---

# Daily Control

Guide the user through a local-first control loop. The Context Root is shared context, not application state; ordinary Agent reasoning performs the work.

## Resolve the route

Resolve one of the routes below. `/daily-control <route>` is the recommended explicit syntax; an equivalent natural-language request selects the same route.

- **help** or a bare `/daily-control` — follow [Help](#help) below without loading another reference.

- **setup** — read [`references/routes/setup.md`](references/routes/setup.md).
- **open** — read [`references/routes/open.md`](references/routes/open.md).
- **refresh** — read [`references/routes/refresh.md`](references/routes/refresh.md).
- **shutdown** — read [`references/routes/shutdown.md`](references/routes/shutdown.md).
- **weekly-review** — read [`references/routes/weekly-review.md`](references/routes/weekly-review.md).
- **extend** — read [`references/routes/extend.md`](references/routes/extend.md).

If the intent is ambiguous, ask one short question naming the likely routes.

## Help

For `help` or a bare invocation, show one-line descriptions of setup, open, refresh, shutdown, weekly-review, and extend. Do not write or run the suggested route.

If the current directory lacks either Context Root marker, recommend setup and explain that an existing root must be named directly; do not scan for one.

When both markers exist, read the Context Root `AGENTS.md`, preferences, today's Daily record when present, and Source Contracts. Recommend at most one next route from durable content rather than heading presence alone:

- No Daily record or no confirmed Open content: **open**.
- Confirmed Open, incomplete Shutdown, and at least one enabled Source whose current Evidence is not refreshed: **refresh**.
- Confirmed Open and no enabled Sources: **shutdown** when the user is ready; mention **extend** as optional.
- Current Evidence and incomplete Shutdown: **shutdown**.
- Completed Shutdown: state that today's loop is complete without recommending another route.

List weekly-review in the help text, but do not infer that it is due. Treat `context/now.md` only as supporting context; durable records decide the suggestion.

## Resolve the Context Root

For routes other than setup and help, accept the current working directory only when it contains both `AGENTS.md` and `context/contracts/daily.md`. Otherwise ask the user for the Context Root. Do not scan other directories or use a global registry.

For setup, the user may choose the current directory or name another target. The setup route establishes the markers.

## Invariants

- Keep every Daily Control write inside the confirmed Context Root.
- Read the Context Root `AGENTS.md` before changing context.
- Treat durable Daily, Weekly, Area, Project, Routine, and Evidence records as canonical. `context/now.md` is a rebuildable cache.
- Treat a configured `context/control-policy.md` as user-owned default constraints. Surface conflicts and let the user confirm a current-day override without silently changing the policy.
- Treat a root created before Control Policy support as unconfigured rather than blocking another route. Offer setup when the user wants to add the missing scaffold file.
- Let the user decide priorities, consequential constraints, interpretation, permissions, and final acceptance.
- Present factual Evidence separately from human interpretation.
- Read back every changed file before reporting completion. Report partial or blocked work exactly.

Finish when the selected route's completion criteria are satisfied; do not continue into another route unless the user asked for it.
