

import importlib
from datetime import datetime


def _load_module(preferred_name, fallback_name):
    try:
        return importlib.import_module(preferred_name)
    except (ImportError, ModuleNotFoundError):
        return importlib.import_module(fallback_name)


expense_manager_module = _load_module("finance_tracker.expense_manager", "expense_manager")
ExpenseManager = expense_manager_module.ExpenseManager

expense_module = _load_module("finance_tracker.expense", "expense")
Expense = expense_module.Expense
CATEGORIES = expense_module.CATEGORIES

file_handler = _load_module("finance_tracker.file_handler", "file_handler")
reports = _load_module("finance_tracker.reports", "reports")
utils = _load_module("finance_tracker.utils", "utils")


class FinanceTracker:
    def __init__(self):
        self.manager = ExpenseManager()
        # load existing data when app starts
        loaded = file_handler.load_expenses()
        self.manager.load_expenses(loaded)
        self.budget = utils.load_budget()

    def run(self):
        print("=" * 60)
        print("          PERSONAL FINANCE TRACKER")
        print("=" * 60)

        while True:
            print("\n" + "=" * 40)
            print("              MAIN MENU")
            print("=" * 40)
            print("1. Add New Expense")
            print("2. View All Expenses")
            print("3. Search Expenses")
            print("4. Generate Monthly Report")
            print("5. View Category Breakdown")
            print("6. Set/Update Budget")
            print("7. Export Data to CSV")
            print("8. View Statistics")
            print("9. Backup/Restore Data")
            print("0. Exit")
            print("=" * 40)

            choice = input("\nEnter your choice (0-9): ").strip()

            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.search_expenses()
            elif choice == "4":
                self.generate_monthly_report()
            elif choice == "5":
                self.view_category_breakdown()
            elif choice == "6":
                self.set_budget()
            elif choice == "7":
                self.export_data()
            elif choice == "8":
                self.view_statistics()
            elif choice == "9":
                self.backup_restore()
            elif choice == "0":
                self.save_and_exit()
                break
            else:
                print("Invalid choice! Please enter 0-9.")

    def save_and_exit(self):
        file_handler.save_expenses(self.manager.get_all())
        print("\n" + "=" * 60)
        print("Data saved. Thank you for using Personal Finance Tracker!")
        print("=" * 60)

    def add_expense(self):
        print("\n--- ADD NEW EXPENSE ---")
        date = utils.get_valid_date()
        amount = utils.get_valid_amount()
        category = utils.get_valid_category(CATEGORIES)
        description = input("Description (optional): ").strip()

        try:
            self.manager.add_expense(date, amount, category, description)
            file_handler.save_expenses(self.manager.get_all())
            print("Expense added successfully!")
        except ValueError as e:
            print(f"Could not add expense: {e}")

    def view_expenses(self):
        print("\n--- ALL EXPENSES ---")
        expenses = self.manager.get_all()
        if not expenses:
            print("No expenses recorded yet.")
            return

        for i, e in enumerate(expenses, start=1):
            print(f"{i}. {e}")
        print(f"\nTotal: Rs.{self.manager.total_spent():.2f}")

    def search_expenses(self):
        print("\n--- SEARCH EXPENSES ---")
        print("Leave any field blank to skip that filter.")

        keyword = input("Keyword in description: ").strip()
        category = input("Category (e.g. Food, Transport): ").strip()
        min_input = input("Minimum amount: ").strip()
        max_input = input("Maximum amount: ").strip()

        min_amount = float(min_input) if min_input else None
        max_amount = float(max_input) if max_input else None

        results = self.manager.search(
            keyword=keyword,
            category=category,
            min_amount=min_amount,
            max_amount=max_amount
        )

        if not results:
            print("No matching expenses found.")
            return

        print(f"\nFound {len(results)} matching expense(s):")
        for i, e in enumerate(results, start=1):
            print(f"{i}. {e}")
        print(f"\nTotal of results: Rs.{self.manager.total_spent(results):.2f}")

    def generate_monthly_report(self):
        year_input = input("Enter year (e.g. 2026): ").strip()
        month_input = input("Enter month (1-12): ").strip()

        try:
            year = int(year_input)
            month = int(month_input)
            if not (1 <= month <= 12):
                raise ValueError
        except ValueError:
            print("Invalid year or month.")
            return

        reports.monthly_report(self.manager.get_all(), self.manager, year, month)

    def view_category_breakdown(self):
        reports.category_breakdown(self.manager.get_all(), self.manager)

    def set_budget(self):
        print("\n--- SET/UPDATE BUDGET ---")
        print(f"Current monthly budget: Rs.{self.budget:.2f}")
        amount = utils.get_valid_amount("Enter new monthly budget: ")
        self.budget = amount
        utils.save_budget(amount)

        # check current month spending against new budget
        now = datetime.now()
        month_expenses = self.manager.get_by_month(now.year, now.month)
        spent = self.manager.total_spent(month_expenses)

        print(f"Budget updated to Rs.{amount:.2f}")
        if spent > amount:
            print(f"Warning: You have already spent Rs.{spent:.2f} this month, over budget!")
        else:
            print(f"You have spent Rs.{spent:.2f} of your budget so far this month.")

    def export_data(self):
        print("\n--- EXPORT DATA ---")
        expenses = self.manager.get_all()
        file_handler.export_to_csv(expenses)

    def view_statistics(self):
        reports.show_statistics(self.manager)
        reports.trend_analysis(self.manager)

    def backup_restore(self):
        print("\n--- BACKUP/RESTORE ---")
        print("1. Create Backup")
        print("2. Restore from Backup")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            file_handler.backup_data()
        elif choice == "2":
            backups = file_handler.list_backups()
            if not backups:
                print("No backups available.")
                return
            print("Available backups:")
            for i, b in enumerate(backups, start=1):
                print(f"{i}. {b}")
            selection = input("Enter backup number to restore: ").strip()
            if selection.isdigit() and 1 <= int(selection) <= len(backups):
                file_handler.restore_backup(backups[int(selection) - 1])
                # reload data after restore
                loaded = file_handler.load_expenses()
                self.manager.load_expenses(loaded)
            else:
                print("Invalid selection.")
        else:
            print("Invalid choice.")


def main():
    tracker = FinanceTracker()
    tracker.run()


if __name__ == "__main__":
    main()