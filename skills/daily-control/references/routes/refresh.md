# Refresh route

Read the Context Root `AGENTS.md`, `context/preferences.md`, `context/contracts/evidence.md`, [`../evidence-contract.md`](../evidence-contract.md), and every Source Contract with `Enabled: yes`.

## 1. Select the window and sources

Use the current Daily record's local date unless the user names another window. State the enabled Source IDs. With no enabled Sources, ask whether to record manual observation or run extend; stop without reporting success.

Complete when the collection window and source set are explicit.

## 2. Collect factual results

For each enabled Source Contract, use only its declared method and permission scope. Normalize the result as complete, partial, unavailable, or failed. Keep facts, provenance, and diagnostics distinct.

Complete when every enabled source has a current status or an honestly reported access boundary.

## 3. Preview the owned update

Prepare the current Daily file's `## Evidence` section and any explicitly extension-owned artifacts. Preserve unrelated sections and last valid source facts when the current call fails, while showing the current status and original fact window.

Default to asking for confirmation. If preferences say `Refresh write mode: auto`, or the user explicitly requested automatic writing for this call, show a concise preview and proceed without a second confirmation.

Complete when the proposed writes, preserved content, and overall outcome are visible.

## 4. Write and read back

Write only the previewed owned scope. Read every changed artifact back and compare it with the proposal. Do not update `context/now.md` during an ordinary refresh.

Complete when readback matches. Report the overall complete, partial, or failed outcome and name every unavailable or failed Source.
