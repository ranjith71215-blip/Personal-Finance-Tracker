import unittest
# --- CORRECTED: Capitalized 'Expense' to match expense.py ---
from finance_tracker.expense import Expense


class TestExpense(unittest.TestCase):

    def test_valid_expense(self):
        # a normal expense should be created without errors
        # --- CORRECTED ---
        e = Expense("2026-07-05", 100, "Food", "Lunch")
        self.assertEqual(e.date, "2026-07-05")
        self.assertEqual(e.amount, 100)
        self.assertEqual(e.category, "Food")
        self.assertEqual(e.description, "Lunch")

    def test_invalid_date_raises_error(self):
        # wrong date format should raise an error
        with self.assertRaises(ValueError):
            # --- CORRECTED ---
            Expense("05-07-2026", 100, "Food")

    def test_negative_amount_raises_error(self):
        # amount must be greater than 0
        with self.assertRaises(ValueError):
            # --- CORRECTED ---
            Expense("2026-07-05", -50, "Food")

    def test_zero_amount_raises_error(self):
        with self.assertRaises(ValueError):
            # --- CORRECTED ---
            Expense("2026-07-05", 0, "Food")

    def test_unknown_category_defaults_to_other(self):
        # category not in the list should become "Other"
        # --- CORRECTED ---
        e = Expense("2026-07-05", 100, "Randomcategory")
        self.assertEqual(e.category, "Other")

    def test_to_dict_and_from_dict(self):
        # converting to dict and back should give the same values
        # --- CORRECTED ---
        e = Expense("2026-07-05", 250.5, "Transport", "Bus fare")
        data = e.to_dict()
        # --- CORRECTED ---
        e2 = Expense.from_dict(data)

        self.assertEqual(e.date, e2.date)
        self.assertEqual(e.amount, e2.amount)
        self.assertEqual(e.category, e2.category)
        self.assertEqual(e.description, e2.description)


if __name__ == "__main__":
    unittest.main()