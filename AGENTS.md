# Project Operating Rules

## Purpose and scope

This repository is a reusable workflow template for web applications. It does not authorize building a product until the architect has an approved product brief, design direction, and numbered phase contract.

## Source-of-truth order

When instructions conflict, apply them in this order:

1. The user's latest explicit instruction.
2. The active numbered phase file.
3. `PRODUCT.md` for product behavior and scope.
4. `DESIGN.md` for visual behavior and tokens.
5. Repository conventions, validation scripts, and tests.
6. These operating rules.

Do not silently resolve a material contradiction. Stop the affected task, state the conflicting sources, and escalate it to the parent agent or architect.

## Agent hierarchy

The primary project thread is the Sol architect. Sol owns requirements, architecture, phase order, user approvals, and final acceptance.

For each approved numbered phase:

1. Sol spawns exactly one `phase_owner` (Terra) for that phase.
2. Terra reads the complete phase contract and relevant project documents before changing files.
3. Terra breaks the phase into bounded, named tasks with acceptance criteria and verification commands.
4. Terra explicitly delegates suitable tasks to Luna `implementation_worker` or `quality_auditor` agents.
5. Terra reviews the combined diff and the workers' evidence.
6. Terra reports only accepted work, or an explicit rejection/blocker, to Sol.

Do not start a later phase without Sol's approval. Do not delegate by implication: every delegated task must state its objective, allowed files, prohibited changes, required checks, attempt number, and required return format.

## Task contracts, ownership, and parallel work

Create or update a task contract before assigning implementation. Each contract must record its parent phase, status, attempt count, objective, allowed files, prohibited changes, acceptance criteria, verification commands, and completion evidence.

Parallelize only read-only investigation, testing, and independent implementation. Before parallel write work, assign explicit and non-overlapping file ownership. Do not run parallel write tasks when they touch the same files; depend on unfinished output; or alter shared configuration, routes, package manifests, database migrations, or central design tokens. The phase owner coordinates any change in those shared areas.

Workers may edit only their allocated files. If completing a task requires another file, report a blocker to Terra; do not expand scope unilaterally.

## Retry and escalation policy

Each delegated task receives at most two implementation attempts. Terra, not the worker, records the attempt number and task status.

On attempt 1, the worker implements the bounded task, runs its required verification, and returns evidence. If Terra rejects it, Terra supplies file-specific rejection reasons and may authorize one corrective attempt.

If attempt 2 fails, do not retry or reassign the task as a disguised third attempt. Escalate to Sol with the attempted changes, verification output, failure or blocker, affected files, and a recommended next action.

## Frontend and brand rules

`DESIGN.md` is the canonical visual contract. Before any frontend or visual change, read it and any relevant installed design or brand UI skill. If `DESIGN.md` is required by the phase but absent, invalid, or conflicts with the requested work, report a blocker rather than inventing a visual system.

For UI work:

- Use declared design tokens for color, spacing, radius, shadow, typography, and motion; do not introduce arbitrary visual values when a token exists.
- Propose a `DESIGN.md` update when a required token is missing; do not create a second design system in component files.
- Preserve the approved hierarchy, density, signature motif, component rules, and responsive guidance.
- Reject generic AI patterns unless expressly approved by the design contract: excessive gradients, glassmorphism, meaningless blobs, excessive pills, floating-card layouts, and generic centered SaaS composition.
- Use real or realistic product content for visual review.
- Implement and verify applicable default, hover, focus, active, disabled, loading, empty, error, and success states.

A visual phase is incomplete until the changed user-facing flows are rendered and inspected at desktop and mobile sizes. Capture or link the reviewed screenshots and report viewport sizes.

## Quality gate

Before accepting a phase, Terra must inspect the actual diff and independently evaluate worker evidence. Run the applicable project commands for:

- Linting.
- Type checking.
- Relevant automated tests.
- Production build.
- `DESIGN.md` validation for visual work.
- Browser or screenshot verification for user-facing work.

Check accessibility, responsive behavior, interaction states, console errors, focus visibility, overflow, and scope adherence. Passing commands alone do not prove visual correctness. Do not claim a check passed without its command and result; if a command is unavailable, report why and the substitute evidence or remaining risk.

## Completion reports

Every worker report must contain: outcome (`pass`, `fail`, or `blocked`); attempt number; files changed or inspected; commands run and concise results; evidence paths or relevant output; known limitations; and blockers. Terra's phase report must additionally state the phase status (`accepted`, `rejected`, or `blocked`), completed objectives, actual changed-file list, verification evidence, design screenshots when applicable, out-of-scope findings, and remaining risks.
