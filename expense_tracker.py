import json
from datetime import datetime
import os

BASE_FILE = "expenses.json"

# -------------------- Helper functions --------------------

def load_expenses():
    """Loads expenses from Json File"""
    if os.path.exists(BASE_FILE):
        with open(BASE_FILE, "r") as file:
            return json.load(file)
    return []


def save_expenses(expenses):
    """Saves expenses to Json File"""
    with open(expenses, "w") as file:
        json.dump(expenses, file, indent=4)
        

def add_expenses(expenses):
    """Add a new expense"""
    date_input = input("Enter date (YYYY-MM-DD) or press enter for today: ").strip()
    if date_input == "":
        date_input = datetime.today().strftime("%y-%m-%d")
        
    category = input("Enter the category (Food, Transportation, Shoppng etc.): ").strip()
    amount = float(input("Enter amount: ").strip())
    notes = input("Enter notes(optional): ").strip()
    
    expense = {
        "date": date_input,
        "category": category,
        "amount": amount,
        "notes": notes
    }
    
    expenses.append(expense)
    save_expenses(expenses)
    print("✅Expense created successfully")
    
    
def view_expenses(expenses):
    """View all expenses"""
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    for i, exp in enumerate(expenses, 1):
        print(f"{i}.{exp['date']} | {exp['category']} | ${exp['amount']:.2f} | {exp['notes']}")
            
