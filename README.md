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
