# Inference Error Budget Ledger architecture

Calculates consumed inference error budget from request and failure counts.

```mermaid
flowchart LR
    N0["sample_budget.csv"]
    N1["budget_ledger.py"]
    N2["consumed / status"]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
