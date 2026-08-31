# Privacy and data boundaries

Daily Control is local-first, but local storage alone does not guarantee privacy. The Agent and every enabled source still have their own access and transmission boundaries.

## Context Root boundary

- The Agent uses only the user-confirmed Context Root for Daily Control writes.
- Setup in Adopt mode preserves existing content and previews collisions.
- Source permissions are explicit in a plain Markdown Source Contract.
- Credentials remain in the source's approved secret store or Agent Surface, never in the Context Root.

## Minimal evidence

Daily Control stores the smallest useful projection: factual summary, source status, time window, and provenance. The external source remains canonical for rich detail.

Do not place raw API responses, complete computer histories, full Screen Time exports, raw reading archives, FIT files, high-frequency health telemetry, or GPS tracks in a Daily record. Link or name the source instead.

## Interpretation boundary

Evidence can report observable facts such as a recorded workout, an application duration, or a reading session. The user supplies meaning. The Agent must not turn those facts into claims about intent, productivity, quality, completion, diagnosis, or moral judgment.
