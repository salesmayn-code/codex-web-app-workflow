# Phase 001 Task Contract: Workflow Artifacts

- Parent phase: 001
- Status: accepted
- Attempt: 1 of 2
- Objective: Create the six immediately usable template artifacts and concise reusable brand UI guard required by the approved phase.
- Allowed files: `PRODUCT.template.md`, `DESIGN.template.md`, `ROADMAP.template.md`, `PHASE.template.md`, `TASK.template.md`, `DECISION.template.md`, `.agents/skills/brand-ui-guard/SKILL.md`
- Prohibited changes: All other files; do not alter `.codex`, documentation, GitHub workflow templates, scripts, package manifests, product code, or global configuration.
- Acceptance criteria: All six templates are structured, directly usable, and preserve approval/scope/evidence gates; the product and design templates support future project-specific content without creating a product or brand; the brand UI skill requires `DESIGN.md`, token use, anti-generic-pattern review, desktop/mobile inspection, and appropriate interaction-state verification.
- Verification commands: `git diff --check`; inspect every assigned file; run `python scripts/validate_template.py` if it is available when work completes.
- Required return format: outcome (`pass`, `fail`, or `blocked`); attempt number; files changed or inspected; commands and concise results; evidence paths/output; known limitations; blockers.

## Completion evidence

All six root templates and the brand UI guard were inspected. The final
repository validator passed with zero errors, all four project TOMLs parsed,
and Git's whitespace/conflict-marker check passed.
