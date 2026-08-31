# Daily Control repository guidance

Keep Daily Control agent-native and local-first. The shipped product is a standalone Skill plus Markdown scaffold and optional Extensions, not an application runtime.

## Working rules

- Prefer the smallest documentation or contract change that satisfies the request.
- Keep runtime instructions inside `skills/daily-control/`; repository `docs/` must not be a runtime dependency of the installed Skill.
- Preserve Human Authority: consequential priorities, constraints, interpretations, permissions, and writes remain visible to the user.
- Do not add deterministic code without a concrete accepted need.
- Keep examples synthetic and exclude credentials, private paths, and personal data.

## Maintainer references

- Specs use the local Markdown tracker described in `docs/agents/issue-tracker.md`.
- Commodity implementations follow `docs/agents/buy-vs-build.md`.
