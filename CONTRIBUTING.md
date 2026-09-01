# Contributing

Daily Control accepts focused improvements to its standalone Skill, public documentation, scaffold, examples, and optional Extensions.

Before opening a change:

1. Keep the core agent-native and free of required application code.
2. Keep the installed Skill independent from repository-level `docs/` and `extensions/`.
3. Use synthetic fixtures; remove private paths, credentials, raw personal exports, and proprietary data.
4. State whether a runtime or source integration is reference-only or manually verified.
5. Follow the Extension acceptance criteria in [docs/extensions.md](docs/extensions.md) for adapter contributions.
6. Run the checks in [docs/acceptance.md](docs/acceptance.md) that match your change.

Changes that introduce executable code must name the concrete need, dependencies, permission boundary, and verification evidence.
