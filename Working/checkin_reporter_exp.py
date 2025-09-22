import os
from datetime import datetime
import json

BASE_FILE = 'check_in.json'

# ----------- Helper Functions -------------

def load_list():
    """Load check-ins"""
    if os.path.exists(BASE_FILE):
        with open(BASE_FILE, "r") as file:
            return json.load(file)
    return []


def save_list(checks):
    """Saves check-ins"""
    with open(BASE_FILE,"w") as file:
        json.dump(checks, file, indent=4)
        
        
def add_list(checks):
    """Add new check-in"""
    name = input("Enter your name: ").strip()
    if name != "":
        day_input = datetime.now().strftime("%d-%m-%y")
        time_input = datetime.now().strftime("%H:%M:%S")
        
    checkin_dets ={
        "name" : name,
        "day": day_input,
        "time": time_input
    }
    
    checks.append(checkin_dets)
    save_list(checks)
    print("👍 Check-in successful!")
    
    
def view_list(checks):
    """View check-ins"""
    if not checks:
        print("No check-ins made yet...")
        return
        
    for i, chk in enumerate(checks, 1):
        print(f"{i}.{chk['name']} | {chk['day']} | {chk['time']}")
        
        
def filter_by_name_asc(checks):
    """filter by name in asc order"""
    if not checks:
        print("No check-ins made yet")
        return
    
    filtered = sorted(checks, key=lambda chk: chk['name'].lower())
    for i, chk in enumerate(filtered, 1):
        print(f"{i}.{chk['name']} | {chk['day']} | {chk['time']}")
        
        
def filter_by_time_latest(checks):
    """filter by time from latest"""
    if not checks:
        print("No check-ins made yet")
        return
    
    filtered = sorted(
        checks,
        key=lambda chk: datetime.strptime(chk['day'] + " " + chk['time'], "%d-%m-%y %H:%M:%S"),
        reverse=True 
    )
    for i, chk in enumerate(filtered, 1):
        print(f"{i}. {chk['day']} | {chk['time']} | {chk['name']}")
        
        
def clear_Json(checks):
    """clear check-ins"""
    if not checks:
        print("No check-ins yet...")
        return
        
    with open(BASE_FILE, "w") as file:
        json.dump([], file, indent=4)
        checks.clear()
        print("✅ Check-ins cleared!")
        
        
# ------------ main function ----------------

def main():
    
    check = load_list()
    
    while True:
        print("\n ==== Check-in tracker ===")
        print("1. Add new check-in")
        print("2. View all check-ins")
        print("3. Filter by name(Asc)")
        print("4. Filter by time(latest)")
        print("5. Clear check-ins")
        print("6. Exit")
        
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
            clear_Json(check)
        elif choice == "6":
            print("Goodbye...")
            break
        
        else:
            print("Invalid choice... try again")


if __name__ == "__main__":
    main()            