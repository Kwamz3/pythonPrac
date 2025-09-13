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
    with open(BASE_FILE, "w") as file:
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
    print("✅ Expense created successfully")
    
    
def view_expenses(expenses):
    """View all expenses"""
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    for i, exp in enumerate(expenses, 1):
        print(f"{i}.{exp['date']} | {exp['category']} | ${exp['amount']:.2f} | {exp['notes']}") 
        
        
def filter_by_category(expenses):
    """Filter expenses by category"""
    category = input("Enter category to filter by: ").strip()
    filtered = [exp for exp in expenses if exp['category'].lower() == category.lower()]
    
    if not filtered:
        print("No results found in this category")
        return
    
    for exp in filtered:
        print(f"{exp['date']} | {exp['category']} | ${exp['amount']:.2f} | {exp['notes']}")
        
        
def summary(expenses):
    """Show expense summary"""
    if not expenses:
        print("No summary to show")
        return
    
    total =  sum(exp["amount"] for exp in expenses)
    print(f"Total spent: ${total:.2f}")
    
    category_totals = {}
    for exp in expenses:
        category_totals[exp["category"]] = category_totals.get(["category"], 0) + exp["amount"]
        
    print("\n Spending by category: ")
    for category, amount in category_totals.items():
        print(f"- {category} : ${amount:.2f}")
        
        
# ----------------- Main Program --------------------

def main():
    expense = load_expenses()
    
    while True:
        print("\n === Personal Expense Tracker ===")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. Filter by category")
        print("4. Summary")
        print("5. Exit")
        
        choice = input("Enter your option: ").strip()
        
        if choice == "1":
            add_expenses(expense)
        elif choice == "2":
            view_expenses(expense)
        elif choice == "3":
            filter_by_category(expense)
        elif choice == "4":
            summary(expense)
        elif choice == "5":
            print("Goodbye...")
            break
        else:
            print("Invalid choice... please try again")
            
            
if __name__ == "__main__":
    main()