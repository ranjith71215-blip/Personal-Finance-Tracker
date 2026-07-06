

import json
import csv
import os
import shutil
from datetime import datetime
from finance_tracker.expense import Expense

DATA_FILE = "data/expenses.json"
BACKUP_FOLDER = "data/backup"
EXPORT_FOLDER = "data/exports"


def save_expenses(expenses, filename=DATA_FILE):
    """Save a list of Expense objects to a JSON file."""
    try:
        # make sure the data folder exists
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        data = [e.to_dict() for e in expenses]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        return True
    except (IOError, OSError) as e:
        print(f"Error saving data: {e}")
        return False


def load_expenses(filename=DATA_FILE):
    """Load expenses from a JSON file. Returns a list of Expense objects."""
    if not os.path.exists(filename):
        print("No existing data file found. Starting fresh.")
        return []

    try:
        with open(filename, "r") as f:
            data = json.load(f)

        expenses = []
        for item in data:
            try:
                expenses.append(Expense.from_dict(item))
            except (ValueError, KeyError) as e:
                print(f"Skipping a bad entry in data file: {e}")

        return expenses

    except json.JSONDecodeError:
        print("Data file is corrupted or empty. Starting fresh.")
        return []
    except (IOError, OSError) as e:
        print(f"Error reading data file: {e}")
        return []


def backup_data(filename=DATA_FILE, backup_folder=BACKUP_FOLDER):
    """Make a timestamped copy of the data file in the backup folder."""
    if not os.path.exists(filename):
        print("No data file to back up yet.")
        return False

    try:
        os.makedirs(backup_folder, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"expenses_backup_{timestamp}.json"
        backup_path = os.path.join(backup_folder, backup_name)

        shutil.copy(filename, backup_path)
        print(f"Backup created: {backup_path}")
        return True
    except (IOError, OSError) as e:
        print(f"Error creating backup: {e}")
        return False


def list_backups(backup_folder=BACKUP_FOLDER):
    """Return a list of available backup files, most recent first."""
    if not os.path.exists(backup_folder):
        return []
    files = [f for f in os.listdir(backup_folder) if f.endswith(".json")]
    files.sort(reverse=True)
    return files


def restore_backup(backup_filename, backup_folder=BACKUP_FOLDER, filename=DATA_FILE):
    """Restore a backup file to be the main data file."""
    backup_path = os.path.join(backup_folder, backup_filename)
    if not os.path.exists(backup_path):
        print("That backup file does not exist.")
        return False

    try:
        shutil.copy(backup_path, filename)
        print("Backup restored successfully.")
        return True
    except (IOError, OSError) as e:
        print(f"Error restoring backup: {e}")
        return False


def export_to_csv(expenses, export_folder=EXPORT_FOLDER):
    """Export expenses to a CSV file. Returns the file path if successful."""
    if not expenses:
        print("No expenses to export.")
        return None

    try:
        os.makedirs(export_folder, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = os.path.join(export_folder, f"expenses_{timestamp}.csv")

        with open(filepath, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Category", "Amount", "Description"])
            for e in expenses:
                writer.writerow([e.date, e.category, e.amount, e.description])

        print(f"Data exported to: {filepath}")
        return filepath

    except (IOError, OSError) as e:
        print(f"Error exporting to CSV: {e}")
        return None


def import_from_csv(filepath):
    """Import expenses from a CSV file. Returns a list of Expense objects."""
    if not os.path.exists(filepath):
        print("CSV file not found.")
        return []

    imported = []
    try:
        with open(filepath, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    expense = Expense(
                        row["Date"],
                        row["Amount"],
                        row["Category"],
                        row.get("Description", "")
                    )
                    imported.append(expense)
                except (ValueError, KeyError) as e:
                    print(f"Skipping bad row in CSV: {e}")

        print(f"Imported {len(imported)} expenses from CSV.")
        return imported

    except (IOError, OSError) as e:
        print(f"Error reading CSV file: {e}")
        return []