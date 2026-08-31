#!/usr/bin/env python3
"""Validate the reusable Codex web-app workflow template.

This repository is a template rather than an application, so project-specific
PRODUCT.md and DESIGN.md files are optional.  The check validates the reusable
workflow contracts with Python's standard library only.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Iterable, Mapping

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python < 3.11 is unsupported.
    tomllib = None  # type: ignore[assignment]


ROOT_TEMPLATE_NAMES = (
    "PRODUCT.template.md",
    "DESIGN.template.md",
    "ROADMAP.template.md",
    "PHASE.template.md",
    "TASK.template.md",
    "DECISION.template.md",
)

REQUIRED_FILES = (
    "AGENTS.md",
    ".codex/config.toml",
    ".codex/agents/phase-owner.toml",
    ".codex/agents/implementation-worker.toml",
    ".codex/agents/quality-auditor.toml",
    ".agents/skills/brand-ui-guard/SKILL.md",
    "README.md",
    ".gitignore",
    "docs/VALIDATION.md",
    *ROOT_TEMPLATE_NAMES,
    "scripts/validate_template.py",
)

REQUIRED_CONFIG_KEYS = (
    "model",
    "model_reasoning_effort",
    "agents.enabled",
    "agents.max_concurrent_threads_per_session",
    "agents.default_subagent_model",
    "agents.default_subagent_reasoning_effort",
    "agents.interrupt_message",
)

AGENT_EXPECTATIONS: Mapping[str, Mapping[str, object]] = {
    ".codex/agents/phase-owner.toml": {
        "name": "phase_owner",
        "model": "gpt-5.6-terra",
        "sandbox_mode": "workspace-write",
    },
    ".codex/agents/implementation-worker.toml": {
        "name": "implementation_worker",
        "model": "gpt-5.6-luna",
        "sandbox_mode": "workspace-write",
    },
    ".codex/agents/quality-auditor.toml": {
        "name": "quality_auditor",
        "model": "gpt-5.6-luna",
        "sandbox_mode": "read-only",
    },
}

REQUIRED_GUARD_TERMS = (
    "design.md",
    "design token",
    "desktop",
    "mobile",
    "loading",
    "empty",
    "error",
    "hover",
    "focus",
    "disabled",
    "success",
    "gradient",
    "glassmorphism",
    "blob",
    "pill",
    "floating-card",
    "saas",
)

REQUIRED_README_TERMS = (
    "github template",
    "sol",
    "terra",
    "luna",
    "stitch",
    "copy",
    "global",
    "project-local",
    "approve",
    "phase",
)

REQUIRED_VALIDATION_TERMS = (
    "toml",
    "markdown",
    "frontmatter",
    "design",
    "optional",
    "manual",
    "git diff --check",
    "skill",
    "playwright",
)


class Reporter:
    """Collect errors and warnings while keeping command output readable."""

    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.successes: list[str] = []

    def ok(self, message: str) -> None:
        self.successes.append(message)
        print(f"[OK] {message}")

    def warn(self, message: str) -> None:
        self.warnings.append(message)
        print(f"[WARN] {message}")

    def error(self, message: str) -> None:
        self.errors.append(message)
        print(f"[ERROR] {message}")


def read_text(path: Path, reporter: Reporter) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        reporter.error(f"Missing required file: {path}")
    except (OSError, UnicodeError) as exc:
        reporter.error(f"Cannot read {path}: {exc}")
    return None


def get_nested(data: Mapping[str, object], dotted_key: str) -> object | None:
    current: object = data
    for segment in dotted_key.split("."):
        if not isinstance(current, Mapping) or segment not in current:
            return None
        current = current[segment]
    return current


def parse_toml(path: Path, reporter: Reporter) -> dict[str, object] | None:
    if tomllib is None:
        reporter.error("Python 3.11+ is required for standard-library TOML parsing")
        return None
    try:
        with path.open("rb") as handle:
            parsed = tomllib.load(handle)
    except FileNotFoundError:
        reporter.error(f"Missing required TOML file: {path}")
        return None
    except (OSError, tomllib.TOMLDecodeError) as exc:
        reporter.error(f"Invalid TOML in {path}: {exc}")
        return None
    if not isinstance(parsed, dict):
        reporter.error(f"TOML root must be a table: {path}")
        return None
    reporter.ok(f"Parsed TOML: {path}")
    return parsed


def validate_toml(root: Path, reporter: Reporter) -> None:
    config_path = root / ".codex/config.toml"
    config = parse_toml(config_path, reporter)
    if config is not None:
        for key in REQUIRED_CONFIG_KEYS:
            if get_nested(config, key) is None:
                reporter.error(f"{config_path} is missing required key: {key}")
        agents = get_nested(config, "agents")
        if isinstance(agents, Mapping):
            max_threads = agents.get("max_concurrent_threads_per_session")
            if not isinstance(max_threads, int) or isinstance(max_threads, bool) or max_threads < 1:
                reporter.error(
                    f"{config_path} agents.max_concurrent_threads_per_session must be a positive integer"
                )
        if get_nested(config, "agents.enabled") is not True:
            reporter.error(f"{config_path} must enable agents with agents.enabled = true")
        if get_nested(config, "model_reasoning_effort") != "xhigh":
            reporter.error(f"{config_path} must set model_reasoning_effort = xhigh")
        if get_nested(config, "agents.default_subagent_reasoning_effort") != "xhigh":
            reporter.error(
                f"{config_path} must set agents.default_subagent_reasoning_effort = xhigh"
            )

    for relative_path, expectations in AGENT_EXPECTATIONS.items():
        parsed = parse_toml(root / relative_path, reporter)
        if parsed is None:
            continue
        for key, expected in expectations.items():
            actual = get_nested(parsed, key)
            if actual != expected:
                reporter.error(
                    f"{relative_path} must set {key} = {expected!r}; found {actual!r}"
                )
        if parsed.get("model_reasoning_effort") != "xhigh":
            reporter.error(f"{relative_path} must set model_reasoning_effort = xhigh")
        instructions = parsed.get("developer_instructions")
        if not isinstance(instructions, str) or len(instructions.strip()) < 80:
            reporter.error(f"{relative_path} needs substantive developer_instructions")


def frontmatter(text: str) -> tuple[str | None, str]:
    """Return (frontmatter, body), accepting LF and CRLF Markdown."""

    normalized = text.replace("\r\n", "\n")
    if not normalized.startswith("---\n"):
        return None, normalized
    closing = normalized.find("\n---", 4)
    if closing < 0:
        return None, normalized
    end = closing + len("\n---")
    if end < len(normalized) and normalized[end] == "\n":
        end += 1
    return normalized[4:closing], normalized[end:]


def frontmatter_keys(header: str) -> set[str]:
    keys: set[str] = set()
    for line in header.splitlines():
        match = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):(?:\s|$)", line)
        if match:
            keys.add(match.group(1).lower())
    return keys


def validate_markdown_structure(root: Path, reporter: Reporter) -> None:
    for relative_name in ROOT_TEMPLATE_NAMES:
        path = root / relative_name
        text = read_text(path, reporter)
        if text is None:
            continue
        normalized = text.replace("\r\n", "\n")
        headings = re.findall(r"(?m)^#{1,6}\s+\S.+$", normalized)
        if not headings:
            reporter.error(f"{relative_name} must contain at least one Markdown heading")
        else:
            reporter.ok(f"Markdown headings found: {relative_name}")
        if not normalized.strip():
            reporter.error(f"{relative_name} must not be empty")

        if relative_name == "DESIGN.template.md":
            header, body = frontmatter(normalized)
            if header is None:
                reporter.error(
                    "DESIGN.template.md must begin with YAML frontmatter delimited by ---"
                )
            else:
                keys = frontmatter_keys(header)
                for key in ("version", "name", "description"):
                    if key not in keys:
                        reporter.error(
                            f"DESIGN.template.md frontmatter is missing top-level key: {key}"
                        )
                if not body.strip():
                    reporter.error("DESIGN.template.md needs Markdown guidance after frontmatter")
                else:
                    reporter.ok("DESIGN.template.md has YAML frontmatter and Markdown guidance")


def validate_required_paths(root: Path, reporter: Reporter) -> None:
    for relative_name in REQUIRED_FILES:
        path = root / relative_name
        if path.is_file():
            continue
        if not path.exists():
            reporter.error(f"Missing required path: {relative_name}")
        else:
            reporter.error(f"Required path is not a file: {relative_name}")


def validate_text_contract(
    root: Path,
    relative_name: str,
    required_terms: Iterable[str],
    reporter: Reporter,
) -> str | None:
    text = read_text(root / relative_name, reporter)
    if text is None:
        return None
    lowered = text.lower()
    missing = [term for term in required_terms if term.lower() not in lowered]
    if missing:
        reporter.error(f"{relative_name} is missing required references: {', '.join(missing)}")
    else:
        reporter.ok(f"Required guidance references found: {relative_name}")
    return text


def validate_skill(root: Path, reporter: Reporter) -> None:
    relative_name = ".agents/skills/brand-ui-guard/SKILL.md"
    text = validate_text_contract(root, relative_name, REQUIRED_GUARD_TERMS, reporter)
    if text is None:
        return
    header, body = frontmatter(text)
    if header is None:
        reporter.error(f"{relative_name} must begin with YAML frontmatter delimited by ---")
        return
    keys = frontmatter_keys(header)
    for key in ("name", "description"):
        if key not in keys:
            reporter.error(f"{relative_name} frontmatter is missing top-level key: {key}")
    if not body.strip():
        reporter.error(f"{relative_name} needs Markdown guidance after frontmatter")
    elif {"name", "description"}.issubset(keys):
        reporter.ok(f"{relative_name} has YAML frontmatter and Markdown guidance")


def validate_documentation(root: Path, reporter: Reporter) -> None:
    validate_text_contract(root, "README.md", REQUIRED_README_TERMS, reporter)
    validation_text = validate_text_contract(
        root, "docs/VALIDATION.md", REQUIRED_VALIDATION_TERMS, reporter
    )
    if validation_text is not None:
        lowered = validation_text.lower()
        has_design_lint_command = "designmd lint" in lowered or "design:lint" in lowered
        has_optional_manual = "optional" in lowered and "manual" in lowered
        if not has_design_lint_command:
            reporter.error("docs/VALIDATION.md must document a DESIGN.md lint command")
        if not has_optional_manual:
            reporter.error(
                "docs/VALIDATION.md must explicitly describe project-specific design linting as optional/manual"
            )


def validate_project_design(root: Path, reporter: Reporter) -> None:
    design_path = root / "DESIGN.md"
    product_path = root / "PRODUCT.md"
    if not design_path.exists():
        reporter.warn(
            "DESIGN.md is absent, which is valid for template state; project-specific design linting is an optional/manual prerequisite"
        )
    elif design_path.is_file():
        text = read_text(design_path, reporter)
        if text is not None:
            header, body = frontmatter(text)
            if header is None or not body.strip():
                reporter.error("DESIGN.md exists but lacks YAML frontmatter and Markdown guidance")
            else:
                reporter.ok("Optional project DESIGN.md has frontmatter and Markdown guidance")
    if not product_path.exists():
        reporter.warn("PRODUCT.md is absent, which is valid for a reusable template")


def validate(root: Path) -> int:
    reporter = Reporter()
    if not root.is_dir():
        reporter.error(f"Validation root is not a directory: {root}")
        return 1

    print(f"Validating Codex workflow template: {root}")
    validate_required_paths(root, reporter)
    validate_toml(root, reporter)
    validate_markdown_structure(root, reporter)
    validate_skill(root, reporter)
    validate_documentation(root, reporter)
    validate_project_design(root, reporter)

    print(
        f"Summary: {len(reporter.errors)} error(s), {len(reporter.warnings)} warning(s), "
        f"{len(reporter.successes)} successful check(s)"
    )
    if reporter.errors:
        print("Template validation failed.")
        return 1
    print("Template validation passed.")
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    default_root = Path(__file__).resolve().parents[1]
    parser.add_argument(
        "--root",
        type=Path,
        default=default_root,
        help="repository root to validate (default: the parent of scripts/)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    return validate(args.root.resolve())


if __name__ == "__main__":
    raise SystemExit(main())
