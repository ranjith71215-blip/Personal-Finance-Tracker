

from datetime import datetime

CATEGORIES = ["Food", "Transport", "Rent", ]


class Expense:
    def __init__(self, date, amount, category, description=""):
        # basic validation done here, nothing too fancy
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format")

        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")

        category = category.strip().title()
        if category not in CATEGORIES:
            category = "Other"

        self.date = date
        self.amount = round(amount, 2)
        self.category = category
        self.description = description.strip()

    def to_dict(self):
        # used when saving to JSON
        return {
            "date": self.date,
            "amount": self.amount,
            "category": self.category,
            "description": self.description
        }

    @staticmethod
    def from_dict(data):
        # used when loading from JSON
        return Expense(data["date"], data["amount"], data["category"], data.get("description", ""))

    def __str__(self):
        return f"{self.date} | {self.category:<12} | Rs.{self.amount:>8.2f} | {self.description}"