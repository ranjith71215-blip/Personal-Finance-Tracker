

from datetime import datetime


def monthly_report(expenses, manager, year, month):
    """Print a report for a given month and year."""
    month_expenses = manager.get_by_month(year, month)

    print(f"\n--- MONTHLY REPORT: {year}-{month:02d} ---")

    if not month_expenses:
        print("No expenses recorded for this month.")
        return

    total = manager.total_spent(month_expenses)
    print(f"Total expenses: {len(month_expenses)}")
    print(f"Total spent: Rs.{total:.2f}")
    print(f"Average per expense: Rs.{total / len(month_expenses):.2f}")

    print("\nExpenses this month:")
    for e in sorted(month_expenses, key=lambda x: x.date):
        print(f"  {e}")

    category_breakdown(month_expenses, manager)


def category_breakdown(expenses, manager):
    """Print a category-wise breakdown with a simple bar chart."""
    totals = manager.category_totals(expenses)

    if not totals:
        print("No data available for category breakdown.")
        return

    print("\n--- CATEGORY BREAKDOWN ---")
    grand_total = sum(totals.values())
    max_amount = max(totals.values())

    for category, amount in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        percent = (amount / grand_total) * 100 if grand_total else 0
        bar_length = int((amount / max_amount) * 30) if max_amount else 0
        bar = "#" * bar_length
        print(f"{category:<14} Rs.{amount:>8.2f} ({percent:5.1f}%) {bar}")


def show_statistics(manager):
    """Show overall stats: total spent, highest expense, most used category."""
    expenses = manager.get_all()

    if not expenses:
        print("No expenses recorded yet.")
        return

    total = manager.total_spent()
    highest = max(expenses, key=lambda e: e.amount)
    lowest = min(expenses, key=lambda e: e.amount)
    totals_by_cat = manager.category_totals()
    top_category = max(totals_by_cat, key=totals_by_cat.get)

    print("\n--- OVERALL STATISTICS ---")
    print(f"Total expenses recorded: {len(expenses)}")
    print(f"Total amount spent: Rs.{total:.2f}")
    print(f"Average expense: Rs.{total / len(expenses):.2f}")
    print(f"Highest expense: Rs.{highest.amount:.2f} ({highest.category} on {highest.date})")
    print(f"Lowest expense: Rs.{lowest.amount:.2f} ({lowest.category} on {lowest.date})")
    print(f"Most spent category: {top_category} (Rs.{totals_by_cat[top_category]:.2f})")


def trend_analysis(manager):
    """Show a simple month-by-month spending trend."""
    expenses = manager.get_all()
    if not expenses:
        print("No expenses to analyze.")
        return

    monthly_totals = {}
    for e in expenses:
        month_key = e.date[:7]  # "YYYY-MM"
        monthly_totals[month_key] = monthly_totals.get(month_key, 0) + e.amount

    print("\n--- SPENDING TREND (by month) ---")
    max_amount = max(monthly_totals.values())
    for month_key in sorted(monthly_totals.keys()):
        amount = monthly_totals[month_key]
        bar_length = int((amount / max_amount) * 30) if max_amount else 0
        bar = "#" * bar_length
        print(f"{month_key}  Rs.{amount:>8.2f}  {bar}")