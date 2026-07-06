

import unittest
import os
from finance_tracker.expense import Expense
from finance_tracker import file_handler

TEST_FILE = "data/test_expenses.json"
TEST_EXPORT_FOLDER = "data/test_exports"


class TestFileHandler(unittest.TestCase):

    def setUp(self):
        # runs before every test - start with a clean slate
        self.expenses = [
            Expense("2026-07-01", 100, "Food", "Groceries"),
            Expense("2026-07-02", 50, "Transport", "Bus")
        ]

    def tearDown(self):
        # runs after every test - clean up test files
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)
        if os.path.exists(TEST_EXPORT_FOLDER):
            for f in os.listdir(TEST_EXPORT_FOLDER):
                os.remove(os.path.join(TEST_EXPORT_FOLDER, f))
            os.rmdir(TEST_EXPORT_FOLDER)

    def test_save_and_load_expenses(self):
        # save expenses then load them back and compare
        file_handler.save_expenses(self.expenses, TEST_FILE)
        loaded = file_handler.load_expenses(TEST_FILE)

        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0].category, "Food")
        self.assertEqual(loaded[1].amount, 50)

    def test_load_missing_file_returns_empty_list(self):
        # loading a file that doesn't exist should not crash
        loaded = file_handler.load_expenses("data/does_not_exist.json")
        self.assertEqual(loaded, [])

    def test_export_to_csv_creates_file(self):
        filepath = file_handler.export_to_csv(self.expenses, TEST_EXPORT_FOLDER)
        self.assertTrue(os.path.exists(filepath))

    def test_export_empty_list_returns_none(self):
        result = file_handler.export_to_csv([], TEST_EXPORT_FOLDER)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()