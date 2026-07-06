

from datetime import datetime
from finance_tracker.expense import Expense


class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, date, amount, category, description=""):
        new_expense = Expense(date, amount, category, description)
        self.expenses.append(new_expense)
        return new_expense

    def remove_expense(self, index):
        if index < 0 or index >= len(self.expenses):
            raise IndexError("That expense number does not exist")
        return self.expenses.pop(index)

    def get_all(self):
        # returns expenses sorted by date, oldest first
        return sorted(self.expenses, key=lambda e: e.date)

    def search(self, keyword="", category="", min_amount=None, max_amount=None):
        """
        Search expenses by keyword in description, category name,
        and/or amount range. All filters are optional.
        """
        results = self.expenses

        if keyword:
            keyword = keyword.lower()
            results = [e for e in results if keyword in e.description.lower()]

        if category:
            category = category.strip().title()
            results = [e for e in results if e.category == category]

        if min_amount is not None:
            results = [e for e in results if e.amount >= min_amount]

        if max_amount is not None:
            results = [e for e in results if e.amount <= max_amount]

        return sorted(results, key=lambda e: e.date)

    def get_by_month(self, year, month):
        matched = []
        for e in self.expenses:
            e_date = datetime.strptime(e.date, "%Y-%m-%d")
            if e_date.year == year and e_date.month == month:
                matched.append(e)
        return matched

    def total_spent(self, expense_list=None):
        if expense_list is None:
            expense_list = self.expenses
        return round(sum(e.amount for e in expense_list), 2)

    def category_totals(self, expense_list=None):
        if expense_list is None:
            expense_list = self.expenses
        totals = {}
        for e in expense_list:
            totals[e.category] = totals.get(e.category, 0) + e.amount
        return {k: round(v, 2) for k, v in totals.items()}

    def load_expenses(self, expense_list):
        self.expenses = expense_list

    def clear_all(self):
        self.expenses = []