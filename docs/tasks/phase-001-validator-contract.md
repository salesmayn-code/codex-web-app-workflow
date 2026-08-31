# Phase 001 Task Contract: Template Validator

- Parent phase: 001
- Status: accepted after phase-wide dependency correction
- Attempt: 2 of 2
- Objective: Implement a dependency-free local validator for the reusable repository template.
- Allowed files: `scripts/validate_template.py`
- Prohibited changes: All other files; do not alter project documentation, templates, `.codex`, `.agents/skills`, package manifests, product code, or global configuration.
- Acceptance criteria: The script runs with the repository's available Python interpreter and checks required paths, TOML parsing, required TOML keys, Markdown/frontmatter structure where required, the brand UI guard's required rules, documentation command references, and flags absent project-specific design linting as an explicitly optional/manual prerequisite. It exits nonzero for violations and zero for the completed template. It must use only the Python standard library.
- Verification commands: `python scripts/validate_template.py`; a negative self-test using a safely temporary copy or controlled input only if implemented without modifying shared artifacts; `git diff --check`.
- Required return format: outcome (`pass`, `fail`, or `blocked`); attempt number; files changed or inspected; commands and concise results; evidence paths/output; known limitations; blockers.

## Completion evidence

The worker completed the standard-library validator. Its second attempt was
blocked while aligning sibling documentation/skill wording, so Sol applied
those escalated sibling corrections. The final validator completed with zero
errors, two expected template-state warnings, and fifteen successful checks;
the negative-root self-test exited nonzero as intended.
