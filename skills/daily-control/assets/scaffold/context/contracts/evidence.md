# Evidence Contract

Refresh reads only Source Contracts in `context/contracts/sources/` with `Enabled: yes`.

Each result records Source ID, Capability, window, status, minimal facts, provenance, and safe diagnostics. Status is `complete`, `partial`, `unavailable`, or `failed`; a complete check may contain no matching facts.

Refresh owns the current Daily file's `## Evidence` section and artifacts explicitly named by a Source Contract. It stores lightweight projections, not credentials or raw source exports, and does not infer intent, productivity, completion, diagnosis, or personal judgment.
