# Daily Control Context Root

This directory is the user's private, local-first context. Read `context/preferences.md` and `context/now.md`, then load only the contracts and durable records relevant to the current request.

## Authority

The user decides priorities, important constraints, interpretation, permissions, and consequential changes. Draft those decisions visibly and obtain confirmation before recording them.

## Truth

Daily, Weekly, Area, Project, Routine, and Evidence records are canonical. `context/now.md` is a rebuildable routing cache; durable records win when they conflict.

## Writes

- Keep every Daily Control write inside this Context Root.
- Follow the owner and boundaries in `context/contracts/`.
- Preserve user-authored content outside the selected route's owned section.
- Write and read back durable records before updating `context/now.md`.
- Keep credentials and rich raw source data at the external source.
- Separate source-attributed facts from the user's interpretation.
