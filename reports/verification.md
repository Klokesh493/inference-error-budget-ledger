# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -v
python3 budget_ledger.py sample_budget.csv
/rank ok 0.6
/classify exhausted 1.6
test_marks_exhausted_budget (test_budget_ledger.BudgetLedgerTest) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
````
