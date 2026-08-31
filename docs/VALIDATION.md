# Repository validation

These checks validate the reusable workflow files. Run them from the repository
root. The template does not prescribe a package manager or contain a product
runtime, so application commands such as lint, type checking, tests, and a
production build are run after the template is instantiated and its package
scripts are defined.

## Required baseline checks

### Automated template validation

Run the repository's dependency-free structural check with Python 3.11 or
newer:

```text
python scripts/validate_template.py
```

It checks the required tree, TOML syntax and role values, Markdown/frontmatter
structure, brand UI skill metadata and guardrails, and the required README and
validation guidance. Missing project-specific `PRODUCT.md` and `DESIGN.md`
files are expected warnings while this repository remains a template. Any
reported error produces a nonzero exit code.

### Git whitespace errors

Run this before every phase handoff:

```text
git diff --check
```

An empty result and exit code `0` mean that Git found no whitespace errors.

### TOML syntax

Python 3.11 or newer includes the standard-library TOML parser:

```text
python -c "import tomllib; from pathlib import Path; files=sorted(Path('.codex').rglob('*.toml')); assert files, 'No .codex TOML files found'; [tomllib.loads(p.read_text(encoding='utf-8')) for p in files]; print(f'Validated {len(files)} TOML files')"
```

For Python 3.10 or older, run the equivalent command with `tomli` after
installing it in the active development environment:

```text
python -m pip install tomli
python -c "import tomli; from pathlib import Path; files=sorted(Path('.codex').rglob('*.toml')); assert files, 'No .codex TOML files found'; [tomli.loads(p.read_text(encoding='utf-8')) for p in files]; print(f'Validated {len(files)} TOML files')"
```

### Markdown and frontmatter

Use the Markdown formatter/linter to catch malformed Markdown and common
style errors:

```text
npx --yes prettier@3 --check "**/*.md"
npx --yes markdownlint-cli2 "**/*.md"
```

The following PowerShell check validates frontmatter delimiters for Markdown
files that opt into frontmatter. It does not change files and does not require
an external YAML package:

```powershell
$errors = @()
Get-ChildItem -Path . -Recurse -Filter *.md -File | ForEach-Object {
  $lines = Get-Content -LiteralPath $_.FullName
  if ($lines.Count -gt 0 -and $lines[0] -eq '---') {
    $closing = $lines | Select-Object -Skip 1 | Where-Object { $_ -eq '---' }
    if (-not $closing) { $errors += "$($_.FullName): missing closing frontmatter delimiter" }
  }
}
if ($errors.Count -gt 0) { $errors | Write-Error; exit 1 }
'Markdown frontmatter delimiters are valid.'
```

### DESIGN.md linting

The reusable repository intentionally has no live `DESIGN.md`. After an
application copies `DESIGN.template.md` to `DESIGN.md`, selects a visual
direction, and replaces or approves every starter token, run Google's DESIGN.md
linter:

```text
npx -p @google/design.md designmd lint DESIGN.md
```

If the derived application installs `@google/design.md` as a development
dependency, run the project-installed alternative:

```text
designmd lint DESIGN.md
```

Expose the latter as a package script such as `design:lint` and include it in
the application's quality gate. On Windows, use the `designmd` executable alias
shown above.

Also run the Markdown checks against the design contract explicitly:

```text
npx --yes markdownlint-cli2 DESIGN.md DESIGN.template.md
```

These commands require package-registry access and are therefore documented
manual/project checks, not prerequisites for validating this dependency-free
template. Markdown linting is supplemental; it does not validate the DESIGN.md
token contract. No linter replaces human review of tokens, hierarchy, density,
responsive rules, or the approved signature motif. The design contract must be
read before frontend implementation.

### Skill validation

Confirm that the reusable UI guard skill exists and is readable:

```powershell
$skill = '.agents/skills/brand-ui-guard/SKILL.md'
if (-not (Test-Path -LiteralPath $skill -PathType Leaf)) { throw "Missing $skill" }
$content = Get-Content -LiteralPath $skill -Raw
if ([string]::IsNullOrWhiteSpace($content)) { throw "$skill is empty" }
if ($content -notmatch 'DESIGN\.md') { throw "$skill does not reference DESIGN.md" }
'Brand UI guard skill is present and non-empty.'
```

The phase owner must also inspect the skill's actual instructions for design
token usage, rejected generic UI patterns, state coverage, and desktop/mobile
visual verification.

## Optional browser and visual checks

For an instantiated application that includes Playwright tests and a valid
`playwright.config.*`, run:

```text
npx playwright test
```

If browsers are not installed in the environment, install them according to
the project's approved setup process before running the tests. Store or link
the resulting screenshots and reports in the phase evidence. At minimum,
review each changed flow at one desktop and one mobile viewport, and record the
viewport sizes. Check keyboard focus, overflow, responsive layout, console
errors, and applicable loading, empty, error, hover, active, disabled, and
success states.

## Application quality gate

The derived application should run every command defined by its package
scripts and phase contract, typically:

```text
npm run lint
npx tsc --noEmit
npm test
npm run build
```

Use the project's actual package-manager scripts when names differ. Report an
unavailable command instead of claiming it passed. Manual setup such as
Stitch MCP authentication is recorded as a prerequisite, not as a successful
automated check.
