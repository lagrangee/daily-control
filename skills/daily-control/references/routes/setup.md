# Setup route

Read [`../context-root.md`](../context-root.md), then establish one user-confirmed Context Root from the assets under `../../assets/scaffold/`.

## 1. Confirm target and mode

Use the current working directory when the user confirms it; otherwise ask for a target. Offer:

- **Create** for an empty or new directory.
- **Adopt** for a directory with existing content.

Complete when the target path and mode are explicit.

## 2. Inspect and preview

List existing target entries relevant to scaffold collisions. Show which scaffold files would be created, which existing files would be preserved, and which collisions need a merge decision. Do not write during this step.

In Adopt mode, preserve existing content. If an existing `AGENTS.md`, `README.md`, or matching contract needs Daily Control guidance, propose the smallest merge and obtain confirmation.

Complete when every collision has a user-approved resolution.

## 3. Create the scaffold

Copy or faithfully reproduce the scaffold assets only within the target. Always include templates and contracts; include the Fitness and Reading starter Area files only when the user selects them. Replace angle-bracket prompts only when the user has supplied the value; otherwise leave an explicit question in the instance.

Ask for stable preferences that materially affect the loop: locale, timezone, week start, selected Areas, privacy notes, and refresh write mode. Keep them as plain Markdown.

Complete when every required Context Root path exists and pre-existing content remains intact.

## 4. Read back

Read back `AGENTS.md`, preferences, the Daily and Evidence Contracts, and any merged file. Summarize the active Areas, write mode, and absence or presence of enabled Sources.

Complete when the readback matches the approved setup. Suggest `/daily-control open` as a next action without running it automatically.
