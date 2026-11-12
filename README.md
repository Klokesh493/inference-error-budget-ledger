# Inference Error Budget Ledger

Calculates consumed inference error budget from request and failure counts.

Focus: AI/ML platform SLO tracking.

Built as a small, runnable Python project with clear input, output, sample data, and tests.

## Run

```bash
python3 budget_ledger.py sample_budget.csv
```

## Verify

```bash
python3 -m unittest discover . -v
```

## Local verification

Run `make verify` with Make and Python 3 installed. The target runs the documented sample through the project CLI. It also runs the existing Python unit tests.

## Business problem

Inference error counts have different consequences at different request volumes. Teams need to compare failures against the allowed budget.

## Project walkthrough

```mermaid
flowchart LR
    A["Request and failure totals"]
    B["Divide failures by allowed failures"]
    C["Compare consumption to 0.75 and 1"]
    D["Watch or exhausted"]
    E["OK below 0.75"]
    A --> B --> C
    C --> D
    C --> E
```

[Architecture and data flow](docs/ARCHITECTURE.md) · [Business problem, demo, and verification](docs/CASE_STUDY.md)

## Run the project

### Local setup

Run `make verify` with Python 3 and Make installed.

### CLI usage

```sh
python3 budget_ledger.py sample_budget.csv
```

### Replay usage

Run `make replay` to replay the checked-in inputs. The runner compares stdout with the baseline, reports differences, and exits nonzero on regression.

[Replay cases](examples/replay-manifest.json) · [Generated report](reports/replay.md) · [Rule implementation](docs/RULES.md)

### Run tests

[Verification report](reports/verification.md) · [Business problem, sample behavior, and limitations](docs/CASE_STUDY.md)


### Limitations

The verification report covers the bundled local examples. See the [case study](docs/CASE_STUDY.md) for project-specific assumptions and operating limits.
