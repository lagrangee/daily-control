# Maintainer smoke checklist

Use the relevant checks after changing the standalone Skill, scaffold, or route contracts. This checklist catches observable regressions; it is not a runtime certification program.

## Prepare

1. Install the complete `skills/daily-control` folder in an Agent Surface.
2. Create two disposable directories: one empty Create fixture and one Adopt fixture containing a unique pre-existing note.
3. Use synthetic content and keep every fixture outside the repository.

## Agent journey

1. **Bare help, invalid cwd** — invoke `/daily-control` outside a Context Root. Pass when the Agent shows the routes, recommends setup, and does not scan or write.
2. **Create** — invoke `/daily-control setup` in the empty fixture. Pass when the Agent previews the target, creates the scaffold only after confirmation, includes an unconfigured Control Policy, and reads back required files.
3. **Adopt** — invoke setup in the non-empty fixture. Pass when additions and collisions are previewed and the unique note remains byte-for-byte unchanged.
4. **Bare help, valid root** — invoke `/daily-control`. Pass when the Agent reads today's durable state, makes at most one supported next-route suggestion, and does not execute it.
5. **Open with policy** — configure one Control Policy field, then invoke open with a conflicting request. Pass when the Agent names the conflict and records only a confirmed current-day override without changing the policy.
6. **Refresh, confirm mode** — use manual observation or a synthetic Source Contract. Pass when the Agent reports source status, previews the owned Evidence update, waits for confirmation, writes only that scope, and reads it back.
7. **Refresh, auto preference** — set `Refresh write mode: auto` in preferences and invoke refresh again. Pass when the Agent previews what it is doing in conversation, writes without a second confirmation, and stays within the same owned scope.
8. **Shutdown** — invoke shutdown. Pass when Evidence and human interpretation remain distinct, the final draft is confirmed, and durable history precedes the summary update.
9. **Weekly review** — invoke weekly-review. Pass when it reviews a closed interval, links relevant Areas, Projects, and Routines, and applies a proposed Control Policy or priority change only after separate confirmation.
10. **Extend** — ask to connect an existing source Skill. Pass when the Agent confirms purpose and permissions, creates a disabled Source Contract, verifies a representative sample, previews its write mapping, and enables it only after acceptance.

## Global invariants

Every exercised scenario must satisfy all of these:

- Every write remains under the confirmed Context Root.
- No credential, private absolute path, raw external response, full browsing history, GPS track, or high-frequency telemetry enters the Context Root.
- Missing, partial, unavailable, and failed Evidence remain visible and are never reported as complete.
- Existing valid Evidence is not erased by a current source failure.
- Durable records are written and read back before `context/now.md` is refreshed.
- The Agent does not infer intent, productivity, completion, health state, or personal judgment from source facts.
- Help is read-only and never executes its suggested route.

Record a reproducible failure in the issue or pull request that fixes it. Run only the scenarios touched by an ordinary change; run the complete checklist before a tagged release.
