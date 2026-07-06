

import json
import os
from datetime import datetime

BUDGET_FILE = "data/budget.json"


def get_valid_date(prompt="Enter date (YYYY-MM-DD): "):
    """Keep asking until user enters a valid date."""
    while True:
        date_str = input(prompt).strip()
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD (e.g. 2026-07-05).")


def get_valid_amount(prompt="Enter amount: "):
    """Keep asking until user enters a valid positive number."""
    while True:
        value = input(prompt).strip()
        try:
            amount = float(value)
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            return amount
        except ValueError:
            print("Please enter a valid number.")


def get_valid_category(categories, prompt="Choose a category number: "):
    """Show category options and let user pick by number."""
    print("Categories:")
    for i, cat in enumerate(categories, start=1):
        print(f"  {i}. {cat}")

    while True:
        choice = input(prompt).strip()
        if choice.isdigit() and 1 <= int(choice) <= len(categories):
            return categories[int(choice) - 1]
        print("Invalid choice, try again.")


def load_budget():
    """Load monthly budget value from file. Returns 0 if not set."""
    if not os.path.exists(BUDGET_FILE):
        return 0
    try:
        with open(BUDGET_FILE, "r") as f:
            data = json.load(f)
            return data.get("monthly_budget", 0)
    except (json.JSONDecodeError, IOError):
        return 0


def save_budget(amount):
    """Save the monthly budget value to file."""
    try:
        os.makedirs(os.path.dirname(BUDGET_FILE), exist_ok=True)
        with open(BUDGET_FILE, "w") as f:
            json.dump({"monthly_budget": amount}, f, indent=4)
        return True
    except (IOError, OSError) as e:
        print(f"Error saving budget: {e}")
        return False