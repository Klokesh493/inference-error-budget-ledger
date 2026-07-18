import unittest

from budget_ledger import status


class BudgetLedgerTest(unittest.TestCase):
    def test_marks_exhausted_budget(self):
        row = {"endpoint": "/classify", "requests": "50000", "failures": "40", "error_budget_pct": "0.05"}
        self.assertEqual(status(row), "exhausted")


if __name__ == "__main__":
    unittest.main()
