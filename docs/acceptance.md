# Maintainer smoke checklist

Use the relevant checks after changing the standalone Skill, scaffold, or route contracts. This checklist catches observable regressions; it is not a runtime certification program.

## Prepare

1. Install the complete `skills/daily-control` folder in an Agent Surface.
2. Create two disposable directories: one empty Create fixture and one Adopt fixture containing a unique pre-existing note.
3. Use synthetic content and keep every fixture outside the repository. Use an isolated user home for `~/.daily-control/config.md`; do not replace the maintainer's real default.

## Agent journey

1. **Bare help, no default and invalid cwd** — invoke `/daily-control` outside a Context Root with no saved configuration. Pass when the Agent shows the routes, recommends setup or naming an existing root, and does not scan or write.
2. **Create** — invoke `/daily-control setup` in the empty fixture. Pass when the Agent previews the scaffold and default configuration write, creates them after approval, includes an unconfigured Control Policy and the Daily Policy overrides surface, and reads back required root files and the saved absolute path before reporting success.
3. **Adopt** — invoke setup in the non-empty fixture. Pass when additions and collisions are previewed and the unique note remains byte-for-byte unchanged.
4. **Bare help, valid root** — invoke `/daily-control`. Pass when the Agent reads today's durable state, makes at most one supported next-route suggestion, and does not execute it.
5. **Open with policy** — configure one Control Policy field, then invoke open with a conflicting request. Pass when the Agent names the conflict and records only a confirmed current-day override under `### Policy overrides` without changing the policy.
6. **Refresh, confirm mode** — use manual observation or a synthetic Source Contract. Pass when the Agent reports source status, previews the owned Evidence update, waits for confirmation, writes only that scope, and reads it back.
7. **Refresh, auto preference** — set `Refresh write mode: auto` in preferences and invoke refresh again. Pass when the Agent previews what it is doing in conversation, writes without a second confirmation, and stays within the same owned scope.
8. **Shutdown** — invoke shutdown. Pass when Evidence and human interpretation remain distinct, the final draft is confirmed, and durable history precedes the summary update.
9. **Weekly review** — invoke weekly-review. Pass when it reviews a closed interval, links relevant Areas, Projects, and Routines, and applies a proposed Control Policy or priority change only after separate confirmation.
10. **Extend** — ask to connect an existing source Skill. Pass when the Agent confirms purpose and permissions, creates a disabled Source Contract, verifies a representative sample, previews its write mapping, and enables it only after acceptance.

## Context Root resolution

Exercise these cases with the isolated configuration and two valid synthetic roots A and B:

- **Saved default across cwd** — save A, then invoke help and a requested route from an unrelated directory and from B. Pass when both select A without asking for its path, help writes nothing, and the requested route reads A's `AGENTS.md` and respects its normal write permissions.
- **One-time override** — with A saved, explicitly invoke a route for B. Pass when B is used and the configuration remains byte-for-byte unchanged. Repeat with an invalid explicit path; pass when the Agent asks for repair instead of using A or cwd.
- **No configuration** — remove the isolated configuration. Pass when a marked cwd is accepted without confirmation, an unrelated cwd requires a root for an operational route, and neither invocation creates a configuration automatically.
- **Broken configuration or root** — separately try malformed or conflicting fields, an unreadable configuration, a missing saved directory, a missing marker, and a permission-denied root while cwd is valid B. Pass when each reports the specific problem without falling through to B or claiming the requested route completed. Help remains read-only.
- **Default change** — ask to remember existing B while A is saved. Pass when the Agent validates B, reads its `AGENTS.md`, updates and reads back only the locator while preserving unrelated configuration content, and does not rebuild B's scaffold. Setup replacing A must include the old and new default in its approved preview.
- **Configuration write failure** — deny writing the isolated configuration during setup. Pass when successful scaffold work is reported separately and full setup success is withheld.
- **Shared and isolated surfaces** — invoke from a second surface with the Skill and access to the same home and A. Pass when it selects A without asking again. A surface unable to access the saved root must report that limitation rather than claim the path grants access.

## Global invariants

Every exercised scenario must satisfy all of these:

- Every content write remains under the resolved Context Root. Only setup or a user-requested default change may also write the user-level locator and create its parent directory.
- No credential, private absolute path, raw external response, full browsing history, GPS track, or high-frequency telemetry enters the Context Root.
- Missing, partial, unavailable, and failed Evidence remain visible and are never reported as complete.
- Existing valid Evidence is not erased by a current source failure.
- Durable records are written and read back before `context/now.md` is refreshed.
- The Agent does not infer intent, productivity, completion, health state, or personal judgment from source facts.
- Help is read-only and never executes its suggested route.

Record a reproducible failure in the issue or pull request that fixes it. Run only the scenarios touched by an ordinary change; run the complete checklist before a tagged release.
