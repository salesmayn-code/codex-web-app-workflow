---
name: brand-ui-guard
description: Apply the approved DESIGN.md contract to frontend, styling and visual-review work.
---

# Brand UI guard

Use this skill for any frontend, styling, design-system, screenshot or visual-review task.

## Before implementation

- Read the complete `DESIGN.md` and the relevant phase/task contract.
- If `DESIGN.md` is missing, invalid, unapproved or contradictory, stop and report a blocker; do not invent a visual system.
- Identify the tokens, component rules, responsive breakpoints, motion guidance and forbidden patterns that apply to the changed flow.

## During implementation

- Use every declared design token for color, typography, spacing, radius, elevation and motion. Propose a `DESIGN.md` change when a needed token is missing; do not create a second token system in component code.
- Preserve the approved hierarchy, density and signature motif with realistic product content.
- Keep semantics, labels, keyboard behavior and visible focus intact. Respect reduced-motion preferences.
- Flag and remove generic AI patterns unless the approved design explicitly calls for them: excessive gradients, glassmorphism, meaningless blobs, excessive pills, floating-card layouts, unrelated icons in rounded squares and generic centered SaaS composition.

## Verification

- Inspect the changed flow at desktop and mobile viewports; record viewport sizes and screenshot paths.
- Check overflow, responsive hierarchy, contrast, typography, focus visibility, console errors and touch/keyboard usability.
- Verify applicable default, hover, focus, active, disabled, loading, empty, error and success states.
- Compare the rendered result with `DESIGN.md`, and return file- or route-specific findings and evidence. Automated checks do not replace rendered inspection.
