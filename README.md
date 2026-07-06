# Personal Finance Tracker

### Author

Ranjith kumar G

---

## Project Description

The Personal Finance Tracker is a Python-based console application that allows users to manage their daily expenses efficiently. Users can add, search, filter, view, and export expense records, generate monthly reports, track budgets, and back up their data, while storing information permanently using a JSON file.

This project demonstrates the use of Python fundamentals such as:

* Variables and Data Types
* Functions
* Conditional Statements (`if`, `elif`, `else`)
* Loops (`while`, `for`)
* Classes and Objects (OOP)
* File Handling (`JSON` and `CSV`)
* Input Validation
* Data Persistence
* Modular Programming
* Unit Testing (`unittest`)

---

## Features

### Expense Management

The system provides the following operations:

| Feature                  | Description                                              |
| ------------------------ | ---------------------------------------------------------|
| Add Expense               | Add a new expense with date, amount, category, description |
| View Expenses             | Display all saved expenses, sorted by date               |
| Search Expenses           | Search/filter by keyword, category, or amount range       |
| Monthly Report            | Generate a report for a specific month and year          |
| Category Breakdown        | View spending by category with a simple bar chart        |
| Set/Update Budget         | Set a monthly budget and track spending against it       |
| Export to CSV             | Export all expenses to a CSV file                         |
| Statistics                | View totals, highest/lowest expense, and spending trends  |
| Backup/Restore            | Create backups of data and restore from a previous backup |

### Input Validation

* Expense date must follow the `YYYY-MM-DD` format.
* Amount must be a positive number.
* Unknown categories automatically default to `"Other"`.
* Invalid inputs are handled gracefully with error messages.

### Data Persistence

* Expenses are stored in a JSON file (`data/expenses.json`).
* Data is automatically loaded when the program starts.
* Data is automatically saved after every new expense and on exit.
* Backups are stored in `data/backup/` with timestamped filenames.
* CSV exports are stored in `data/exports/`.

---

## Project Structure

```text
week4-finance-tracker/
│── finance_tracker/
│ ├── __init__.py
│ ├── main.py
│ ├── expense.py
│ ├── expense_manager.py
│ ├── file_handler.py
│ ├── reports.py
│ └── utils.py
│── data/
│ ├── expenses.json
│ ├── backup/
│ └── exports/
│── tests/
│ ├── test_expense.py
│ ├── test_file_handler.py
│ └── test_reports.py
│── requirements.txt
│── README.md
│── .gitignore
└── run.py
```

---

## How to Run

### Method 1: Run Normally

Open the terminal in VS Code and run:

```bash
python run.py
```

---

### Method 2: Run from Command Prompt

```bash
python run.py
```

The application will display the main menu and allow you to manage expenses interactively.

---

## Sample Menu

```text
========================================
              MAIN MENU
========================================
1. Add New Expense
2. View All Expenses
3. Search Expenses
4. Generate Monthly Report
5. View Category Breakdown
6. Set/Update Budget
7. Export Data to CSV
8. View Statistics
9. Backup/Restore Data
0. Exit
```

---

## Sample Data (data/expenses.json)

```json
[
    {
        "date": "2026-04-05",
        "amount": 1000.0,
        "category": "Transport",
        "description": "train"
    },
    {
        "date": "2026-05-01",
        "amount": 1500.0,
        "category": "Rent",
        "description": ""
    },
    {
        "date": "2026-06-05",
        "amount": 2000.0,
        "category": "Food",
        "description": "Lunch"
    },
]
```

---

## Sample Statistics Output

```text
--- OVERALL STATISTICS ---
Total expenses recorded: 3
Total amount spent: Rs.1950.00
Average expense: Rs.650.00
Highest expense: Rs.1200.00 (Rent on 2026-06-15)
Lowest expense: Rs.250.00 (Food on 2026-07-01)
Most spent category: Rent (Rs.1200.00)
```

---

## How to Run Tests

All test files are connected together in `run_tests.py`. To run all tests at once:

```bash
python run_tests.py
```

This runs tests for `expense.py`, `file_handler.py`, and `reports.py` together and prints the results in the terminal.

---

## Learning Outcomes

By completing this project, you will learn how to:

* Create and organize classes and functions
* Work with objects to represent structured data
* Validate user inputs for dates, amounts, and categories
* Read and write JSON files
* Export data to CSV format
* Implement CRUD-style operations for expenses
* Build menu-driven console applications
* Handle persistent data storage and backups
* Write basic unit tests using `unittest`
* Design modular Python programs across multiple files

---

## Optimization Techniques

* Modular file-based design (separate modules for expenses, file handling, reports, utils)
* Reusable validation functions
* Sorted lookups for faster reporting
* Automatic folder/file creation if missing
* Efficient filtering using list comprehensions
* Reduced code duplication through shared manager methods

---

## Technologies Used

* Python 3
* JSON
* CSV
* unittest
* Visual Studio Code (VS Code)

---

## Conclusion

This Personal Finance Tracker is a practical Python application that combines file handling, input validation, object-oriented programming, and reporting into a single project. It provides a strong foundation for developing more advanced applications such as database-driven budgeting tools, web-based expense trackers, and personal finance dashboards.