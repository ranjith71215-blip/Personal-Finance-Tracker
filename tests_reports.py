

import unittest
from finance_tracker.expense_manager import ExpenseManager


class TestReports(unittest.TestCase):

    def setUp(self):
        # add some sample expenses before each test
        self.manager = ExpenseManager()
        self.manager.add_expense("2026-07-01", 100, "Food", "Groceries")
        self.manager.add_expense("2026-07-05", 200, "Transport", "Cab")
        self.manager.add_expense("2026-06-15", 50, "Food", "Snacks")

    def test_total_spent(self):
        total = self.manager.total_spent()
        self.assertEqual(total, 350)

    def test_category_totals(self):
        totals = self.manager.category_totals()
        self.assertEqual(totals["Food"], 150)
        self.assertEqual(totals["Transport"], 200)

    def test_get_by_month(self):
        july_expenses = self.manager.get_by_month(2026, 7)
        self.assertEqual(len(july_expenses), 2)

        june_expenses = self.manager.get_by_month(2026, 6)
        self.assertEqual(len(june_expenses), 1)

    def test_search_by_category(self):
        results = self.manager.search(category="Food")
        self.assertEqual(len(results), 2)

    def test_search_by_amount_range(self):
        results = self.manager.search(min_amount=100, max_amount=200)
        self.assertEqual(len(results), 2)


if __name__ == "__main__":
    unittest.main()