import os
from datetime import datetime
import json

BASE_FILE = 'check_ins.json'

# ---------------- Helper Functions ----------------

def load_list():
    """Loads check-in list"""
    if os.path.exists(BASE_FILE):
        with open(BASE_FILE, "r") as file:
            return json.load(file)
    return[]


def save_list(checks):
    """Save check-in list"""
    with open(BASE_FILE, "w") as file:
        json.dump(checks, file, indent=4)
        

def add_list(checks):
    """Add new check-in"""
    name = input("Enter your name: ").strip()
    if name != "":
        day_input = datetime.now().strftime("%d-%m-%y")
        time_input = datetime.now().strftime("%H:%M:%S")
        
    checkin_details = {
        "name": name,
        "day": day_input,
        "time": time_input
    }
    
    checks.append(checkin_details)
    save_list(checks)
    print("👍 Check-in successful!")
    
    
def view_list(checks):
    """View check-in lists"""
    if not checks:
        print("No check-ins made yet")
        
    for i, chk in enumerate(checks, 1):
        print(f"{i}.{chk['name']} | {chk['day']} | {chk['time']}")
        
        
def filter_by_name_asc(checks):
    """Filter by name and display in ascending order"""
    filtered = sorted(checks, key=lambda chk: chk['name'].lower())
    for i, chk in enumerate(filtered, 1):
        print(f'{i}.{chk['name']} | {chk['day']} | {chk['time']}')
        
        
def filter_by_time_latest(checks):
    """Filter by time and display from the latest"""
    filtered = sorted(checks, key=lambda chk: chk(['day'], ['time']))
    for i, chk in enumerate(filtered, 1):
        print(f"{i}.{chk['name']} | {chk['day']} | {chk['time']}")


def clear_json(checks):
    """Clear check-in Json"""
    with open(BASE_FILE, "w") as file:
        json.dump([], file, indent=4)
        checks.clear()
    print("Check-in data has been cleared.")
        
        
        
# ------------------- Main function -----------------

def main():
    
    check = load_list()
    
    while True:
        print("\n === Check-in Monitor ===")
        print("1. Add new Check-in")
        print("2. View all Check-ins")
        print("3. Filter by name(ASC)")
        print("4. Filter by time(latest)")
        print("5. Clear check-ins")
        print("6. Goodbye")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_list(check)
        elif choice == "2":
            view_list(check)
        elif choice == "3":
            filter_by_name_asc(check)
        elif choice == "4":
            filter_by_time_latest(check)
        elif choice == "5":
            clear_json(check)
        elif choice == "6":
            print("Goodbye...")
            break
        else:
            print("Invalid choice! try again...")
            
if __name__ == "__main__":
    main()