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

Resolve the Context Root using the rules below. If no root is available, show the routes and recommend setup or naming an existing root. If a selected path or saved configuration is invalid or inaccessible, explain what needs repair. Keep help read-only in both cases.

When a root is resolved, read its `AGENTS.md`, preferences, today's Daily record when present, and Source Contracts. Recommend at most one next route from durable content rather than heading presence alone:

- No Daily record or no confirmed Open content: **open**.
- Confirmed Open, incomplete Shutdown, and at least one enabled Source whose current Evidence is not refreshed: **refresh**.
- Confirmed Open and no enabled Sources: **shutdown** when the user is ready; mention **extend** as optional.
- Current Evidence and incomplete Shutdown: **shutdown**.
- Completed Shutdown: state that today's loop is complete without recommending another route.

List weekly-review in the help text, but do not infer that it is due. Treat `context/now.md` only as supporting context; durable records decide the suggestion.

## Resolve the Context Root

For every route except setup, resolve in this order and stop at the first selected path:

1. A Context Root explicitly named by the user for this invocation.
2. The `Context Root` field in `~/.daily-control/config.md`.
3. The current working directory, only when no saved configuration exists and it contains both `AGENTS.md` and `context/contracts/daily.md`.

Validate that the selected directory is accessible and contains both markers, then use it without asking the user to confirm it again. An invalid explicit path, unreadable or malformed configuration, or invalid saved root requires repair or an explicit replacement; do not silently fall through to cwd or scan other directories. If no root is available, ask for one (help only explains the options). Ordinary invocations, including explicit one-time overrides, leave the saved default unchanged.

The user-level configuration is plain Markdown with exactly one `Context Root: /absolute/path` field. `~` means the current user's home; store the root as an absolute path. It is a locator, not planning state. For setup or a user-requested change to the saved default, read [`references/context-root.md`](references/context-root.md#saved-default). Sharing it across Agent Surfaces requires the same home, an available Skill, and access to the configuration and root; the saved path does not grant filesystem permissions.

Setup establishes or adopts the user-selected root and saves the default through its route.

## Invariants

- Keep every Daily Control content write inside the resolved Context Root. The sole outside-root exception is `~/.daily-control/config.md` during setup or a user-requested default change.
- Read the Context Root `AGENTS.md` before changing context.
- Treat durable Daily, Weekly, Area, Project, Routine, and Evidence records as canonical. `context/now.md` is a rebuildable cache.
- Treat a configured `context/control-policy.md` as user-owned default constraints. Surface conflicts and let the user confirm a current-day override without silently changing the policy.
- Treat a root created before Control Policy support as unconfigured rather than blocking another route. Offer setup when the user wants to add the missing scaffold file.
- Let the user decide priorities, consequential constraints, interpretation, permissions, and final acceptance.
- Present factual Evidence separately from human interpretation.
- Read back every changed file before reporting completion. Report partial or blocked work exactly.

Finish when the selected route's completion criteria are satisfied; do not continue into another route unless the user asked for it.
