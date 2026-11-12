# Inference Error Budget Ledger architecture

Calculates consumed inference error budget from request and failure counts.

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

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
