---
version: alpha
kind: design-system
name: "[Project name]"
description: "[One-sentence description of the approved visual identity]"
status: Draft
colors:
  canvas: "#ffffff"
  surface: "#f6f7f9"
  surface-raised: "#ffffff"
  text-primary: "#111827"
  text-muted: "#4b5563"
  text-inverse: "#ffffff"
  brand-primary: "#1f2937"
  brand-accent: "#0f766e"
  border: "#d1d5db"
  focus: "#2563eb"
  success: "#166534"
  warning: "#92400e"
  danger: "#b91c1c"
typography:
  display:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "4rem"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "-0.04em"
  heading:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "2rem"
    fontWeight: 650
    lineHeight: 1.15
    letterSpacing: "-0.02em"
  body:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "0.06em"
rounded:
  sm: "4px"
  md: "8px"
  lg: "14px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "24px"
  xl: "40px"
  2xl: "64px"
breakpoints:
  mobile: "0px"
  tablet: "768px"
  desktop: "1024px"
  wide: "1440px"
motion:
  fast: "120ms"
  standard: "200ms"
  emphasis: "320ms"
components:
  button-primary:
    backgroundColor: "{colors.brand-primary}"
    textColor: "{colors.text-inverse}"
    rounded: "{rounded.md}"
    padding: "12px 16px"
    focusRing: "{colors.focus}"
  button-secondary:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.text-primary}"
    borderColor: "{colors.border}"
    rounded: "{rounded.md}"
    padding: "12px 16px"
  input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.text-primary}"
    borderColor: "{colors.border}"
    rounded: "{rounded.sm}"
    padding: "12px"
  status-success:
    textColor: "{colors.success}"
    backgroundColor: "{colors.surface}"
---

# Design system

Copy this file to `DESIGN.md` only after a visual direction is selected. The YAML front matter is normative: implementation code must use these tokens or a documented semantic alias. The starter values are an accessible neutral baseline for tooling and must be replaced or explicitly approved as the project's visual direction before implementation.

## Approval metadata

- **Product brief:** [Link to `PRODUCT.md` and its approval evidence]
- **Direction selected:** [Name and link to the approved design direction]
- **Owner:** [Terra or named design owner]
- **Approver:** [Sol or product approver]
- **Status:** [Draft / Approved / Superseded]
- **Last reviewed:** [YYYY-MM-DD]

## Overview

Describe the visual idea in specific, testable language.

- **Audience fit:** [Why this visual language fits the users in `PRODUCT.md`]
- **Emotional effect:** [What the interface should make users feel]
- **Signature motif:** [One recognizable element and its permitted use]
- **Content density:** [Sparse, moderate or dense, with a concrete example]
- **Recognition test:** [How the interface remains identifiable without a logo]

## Colors

Explain the job of every color token, contrast expectations and where accent colors are permitted. Do not use accent colors decoratively throughout the interface. Record contrast evidence for normal text, large text, controls and non-text indicators.

## Typography

Explain the display versus functional type strategy, hierarchy, maximum line lengths, weight usage and numeral treatment for data-heavy interfaces. Name the loading and fallback behavior for every non-system font.

## Layout and responsive behavior

Define the content grid, maximum widths, page rhythm, sidebar behavior, mobile stacking, density rules and any intentional asymmetry. State the behavior at the `mobile`, `tablet`, `desktop` and `wide` breakpoints above, including overflow handling.

## Elevation and depth

Define whether depth comes from borders, shadows, contrast, layering or no elevation. Map each approved shadow or border treatment to a token; avoid one-off effects.

## Shapes

Define the shape language and when each radius is appropriate. State where square corners are required and where rounded elements are meaningful rather than decorative.

## Components and states

Specify buttons, inputs, cards, tables, navigation, dialogs, charts and status indicators. For each applicable component, describe default, hover, focus, active, disabled, loading, empty, error and success behavior, including text alternatives and keyboard behavior.

## Motion

Explain which transitions communicate hierarchy, state or feedback, using only the motion tokens above. Define reduced-motion behavior and avoid animation that delays task completion.

## Do

- Preserve the approved signature motif and information hierarchy.
- Use the YAML tokens consistently and add a token before adding a repeated visual value.
- Keep color, type and spacing choices legible at every approved breakpoint.
- Use realistic product content during visual review.
- Document intentional exceptions beside the affected component or decision record.

## Do not

- Use generic purple-blue gradients unless the approved direction explicitly requires them.
- Wrap every section in a floating card.
- Use excessive pills, glassmorphism or unrelated icons inside rounded squares.
- Add decorative blobs, noise or illustration without product meaning.
- Use vague copy such as “unlock,” “revolutionize” or “seamless” in interface content.
- Animate elements without communicating hierarchy, state or feedback.
- Copy a generic centered SaaS hero layout.

## Validation and evidence

- **Token/design lint command:** [Command and result]
- **Desktop screenshot:** [Path or link; viewport, for example 1440 × 900]
- **Tablet screenshot:** [Path or link; viewport, for example 768 × 1024]
- **Mobile screenshot:** [Path or link; viewport, for example 390 × 844]
- **Accessibility review:** [Contrast, focus and keyboard evidence]
- **State review:** [Routes/components and states inspected]
