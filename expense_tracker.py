import json
from datetime import datetime
import os

BASE_FILE = "expenses.json"

# ----- Backend functions -----
def load_expenses():
    """Loads expenses from the JSON file"""
    if os.path.exists(BASE_FILE):
        with open(BASE_FILE, "r") as file:
            return json.load(file)
    return []   

def save_expenses(expenses):
    """Save expenses to the JSON file""" 
    with open(BASE_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    """Add new expense"""
    date_input = input("Enter date (YYY-MM-DD) or press Enter for today: ").strip()
    if date_input == "":
        date_input = datetime.today().strftime("%Y-%m-%d")
    
    category = input("Enter category(Food, Shopping, Transport, etc. ): ").strip()
    amount = float(input("Enter amount: ").strip())
    notes = input("Enter notes (optional): ").strip()
    
    expense = {
        "date: ": date_input,
        "category": category,
        "amount": amount,
        "notes": notes
    }
    
    expenses.append(expense)
    save_expenses(expenses)
    print("✅ Expense added successfully!")
        
                


# ----- Main Program -----
def main():
    expenses = load_expenses()
    
    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. Filter by category")
        print("4. Summary")
        print("5. Exit")
        
        choice = input("Choose an option").strip()
        
        if choice == "1":
            add_expense(expenses)