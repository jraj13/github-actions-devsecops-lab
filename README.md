# GitHub Actions DevSecOps Lab

A secure CI/CD reference implementation using **GitHub Actions**, **Python**, and automated security gates.

This project demonstrates how code quality, dependency security, secret detection, static analysis, testing, packaging, and artifact publishing can be combined into a single CI pipeline.

> This repository uses a small synthetic Python application for demonstration purposes. It does not contain employer or client source code.

## Pipeline Overview

```text
Developer Push / Pull Request
        │
        ▼
┌──────────────────────────────┐
│        GitHub Actions        │
├──────────────────────────────┤
│ Checkout repository          │
│ Install dependencies         │
│ Dependency vulnerability     │
│ Secret scanning              │
│ Static security analysis     │
│ Formatting                   │
│ Linting                      │
│ Unit tests                   │
│ Package build                │
│ Artifact upload              │
└──────────────────────────────┘
        │
        ▼
   Build succeeds
        or
   Security gate fails
```

## Security Controls

### Dependency Vulnerability Scanning

The pipeline uses `pip-audit` to identify known vulnerabilities in installed Python dependencies.

```bash
pip-audit
```

This represents a Software Composition Analysis (SCA) control.

### Secret Scanning

The pipeline uses `detect-secrets` to identify credentials, tokens, keys, and other secret-like values that may accidentally be committed.

```bash
detect-secrets scan --baseline .secrets.baseline
```

A baseline is committed to the repository so reviewed false positives can be tracked consistently.

### Static Application Security Testing

Bandit performs Python-focused static security analysis.

```bash
bandit -r src
```

This helps identify insecure coding patterns in application source code.

## Code Quality

Ruff is used for both formatting and linting.

```bash
ruff format --check .
ruff check .
```

Local formatting can be applied with:

```bash
ruff format .
```

## Automated Testing

The sample application is tested using pytest.

```bash
pytest -v
```

The test suite covers normal behavior and invalid input handling.

## Build and Artifact Publishing

After all quality and security checks pass, the project is packaged using Python's build tooling:

```bash
python -m build
```

This produces a source distribution and wheel under:

```text
dist/
```

GitHub Actions then uploads the build output as a workflow artifact.

This demonstrates separation between source validation and production of a deployable artifact.

## CI Workflow

The workflow runs on:

- Pushes to `main`
- Pushes to feature branches
- Pull requests targeting `main`
- Manual execution with `workflow_dispatch`

The pipeline follows a fail-fast security-gate model. A failed dependency audit, secret scan, SAST check, formatting check, lint check, or unit test causes the CI run to fail.

## Project Structure

```text
github-actions-devsecops-lab/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   └── secure_app/
│       ├── __init__.py
│       └── app.py
├── tests/
│   └── test_app.py
├── .secrets.baseline
├── pyproject.toml
└── README.md
```

## Local Development

Create and activate a virtual environment.

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
```

Run all local validation:

```powershell
ruff format .
ruff check .
pytest -v
pip-audit
detect-secrets scan --baseline .secrets.baseline
bandit -r src
python -m build
```

## DevSecOps Layers

This project intentionally separates different security responsibilities:

| Control | Tool | Purpose |
|---|---|---|
| Dependency Security | `pip-audit` | Detect vulnerable third-party packages |
| Secret Detection | `detect-secrets` | Detect accidentally committed credentials |
| SAST | `Bandit` | Detect insecure Python coding patterns |
| Code Quality | `Ruff` | Formatting and static lint checks |
| Testing | `pytest` | Validate expected application behavior |
| Build | `build` | Produce distributable Python artifacts |
| CI/CD | GitHub Actions | Automate quality and security gates |

These controls complement one another rather than replacing one another.

## Design Principles

- Security checks should run automatically.
- Security failures should block the pipeline.
- Quality and security controls should be reproducible locally.
- CI workflows should use least-privilege permissions.
- Build artifacts should only be produced after validation succeeds.
- Security controls should address different classes of risk.
- Public examples should use synthetic code and data.

## Technology Stack

**GitHub Actions | Python | DevSecOps | CI/CD | pip-audit | detect-secrets | Bandit | Ruff | pytest | Software Composition Analysis | SAST**

## Future Enhancements

Potential extensions include:

- GitHub CodeQL analysis
- SBOM generation
- Container image scanning
- Dependency review for pull requests
- Signed build artifacts
- OIDC-based cloud authentication
- Environment-specific deployment gates
- Reusable GitHub Actions workflows
- Branch protection and required status checks

## Purpose

This project is a public reference implementation demonstrating practical DevSecOps patterns for secure software delivery.

It focuses on the CI/CD and security architecture rather than application complexity.