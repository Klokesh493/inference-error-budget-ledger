# Inference Error Budget Ledger walkthrough

## Business problem

Calculates consumed inference error budget from request and failure counts.

## Reproduce the workflow

Run `python3 budget_ledger.py sample_budget.csv` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
/rank ok 0.6
/classify exhausted 1.6
```

The sample supplies these fields. `endpoint`, `requests`, `failures`, `error_budget_pct`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
