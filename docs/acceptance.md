# v0.1 manual acceptance

This is guidance for a human tester. Daily Control does not automate an Agent Runtime scenario.

## Prepare

1. Install the complete `skills/daily-control` folder in the Agent Surface under test.
2. Create two disposable directories: one empty Create fixture and one Adopt fixture containing a unique pre-existing note.
3. Record the Agent Surface name and version.

## Agent Journey

Run the same journey on Codex and WorkBuddy.

1. **Invalid cwd** — invoke `/daily-control open` outside a Context Root. Pass when the Agent asks for the target directory and does not scan or write elsewhere.
2. **Create** — invoke `/daily-control setup` in the empty fixture. Pass when the Agent previews the target, creates the scaffold only after confirmation, and reads back required files.
3. **Adopt** — invoke setup in the non-empty fixture. Pass when additions and collisions are previewed and the unique note remains byte-for-byte unchanged.
4. **Open** — invoke `/daily-control open`. Pass when the Agent creates or resumes today's Daily record, confirms the plan, and updates the current summary after the durable record.
5. **Refresh, confirm mode** — use manual observation or a synthetic Source Contract. Pass when the Agent reports source status, previews the owned Evidence update, waits for confirmation, writes only that scope, and reads it back.
6. **Refresh, auto preference** — set `Refresh write mode: auto` in preferences and invoke refresh again. Pass when the Agent previews what it is doing in conversation, writes without a second confirmation, and stays within the same owned scope.
7. **Shutdown** — invoke `/daily-control shutdown`. Pass when evidence and human interpretation remain distinct, the final draft is confirmed, and durable history precedes the summary update.
8. **Weekly review** — invoke `/daily-control weekly-review`. Pass when it reviews a closed interval, links relevant Areas, Projects, and Routines, and does not change priorities without user confirmation.
9. **Extend** — ask to connect an existing source Skill. Pass when the Agent confirms purpose and permissions, creates a disabled Source Contract, verifies a representative sample, previews its write mapping, and enables it only after acceptance.

## Global invariants

Every scenario must satisfy all of these:

- Every write remains under the confirmed Context Root.
- No credential, private absolute path, raw external response, full browsing history, GPS track, or high-frequency telemetry enters the Context Root.
- Missing, partial, unavailable, and failed evidence remain visible and are never reported as complete.
- Existing valid Evidence is not erased by a current source failure.
- Durable records are written and read back before `context/now.md` is refreshed.
- The Agent does not infer intent, productivity, completion, health state, or personal judgment from source facts.

Record the result in [runtime-compatibility.md](runtime-compatibility.md). A failed step keeps the runtime Pending and should include the smallest reproducible observation.
