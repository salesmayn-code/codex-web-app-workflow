---
kind: task-contract
version: "1.0"
task: "[001]"
name: "[Task name]"
status: Pending
attempt: 0
maximum_attempts: 2
parent_phase: "[PHASE-NNN]"
owner: "[implementation_worker or quality_auditor]"
assigned_by: "[phase_owner]"
---

# Task [001] — [Task name]

Copy this file to `docs/tasks/[NNN]-[short-name].md`. The phase owner fills the contract before delegation and owns the attempt counter and final status. A worker may edit only the allowed files.

## Objective

State one bounded implementation, investigation, test or audit outcome with a clear definition of done.

## Allowed files

- `[path/to/owned/file]`
- `[path/to/owned/test-or-evidence-file]`

## Prohibited changes

- [Files, routes, configuration, package manifests, migrations or design tokens outside this task]
- [Unrelated behavior or dependency changes]

## Acceptance criteria

- [ ] [Observable result]
- [ ] [Required scope and ownership result]
- [ ] [Error, accessibility or responsive result when applicable]

## Dependencies

- **Inputs:** [Approved files, prior task output or decision record]
- **Blocked by:** [Task or external dependency, or “none”]
- **Coordination required:** [Shared-file owner, or “none”]

## Required verification

- `[command]` — [Expected result]
- `[command]` — [Expected result]
- [For UI work: desktop/mobile viewport and interaction-state checks]

## Attempt history

The phase owner records every attempt. Attempt 1 is the initial implementation. Attempt 2 is allowed only after file-specific rejection reasons are recorded. A second failure is escalated; it is not retried or reassigned as a disguised third attempt.

| Attempt | Date | Scope/result | Rejection reason or correction | Evidence | Reviewer |
| ---: | --- | --- | --- | --- | --- |
| 1 | YYYY-MM-DD | [Result] | [None or concrete reason] | [Path/output] | [Name] |
| 2 | YYYY-MM-DD | [Result] | [None or concrete reason] | [Path/output] | [Name] |

## Completion report

Completed by the worker, then reviewed by the phase owner.

- **Outcome:** [Pass / Fail / Blocked]
- **Attempt:** [1 or 2]
- **Files changed or inspected:** [Explicit list]
- **Verification:** [Each command, result and relevant output/evidence path]
- **Design/UX evidence:** [DESIGN.md sections, viewports and states when applicable]
- **Known limitations:** [Concrete limitations]
- **Blocker and recommended next action:** [Cause and recommendation, or “none”]
