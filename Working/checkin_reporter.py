import json
from datetime import datetime
import os

BASE_FILE = "check_in.json"

# --------------------- Helper functions -------------------

def load_list():
    """Loads check-in list"""
    if os.path.exists(BASE_FILE):
        with open(BASE_FILE, "r") as file:
            return json.load(file)
    return []


def save_list(checks):
    """Saves current checks"""
    with open(BASE_FILE, "w") as file:
        json.dump(checks, file, indent=4)
 
    
def checkin_list(checks):
    """Add new check-ins"""
    name = input("Enter your name: ").strip()
    if name != "":
        day_input = datetime.now().strftime("%d-%m-%y")
        time_input = datetime.now().strftime("%H:%M:%S")
    
    checkin_details = {
        "name" : name,
        "day" : day_input,
        "time" : time_input
    }
    
    checks.append(checkin_details)
    save_list(checks)
    print("👍 Check-in success")
    

def view_list(checks):
    """View check-in list"""
    if not checks:
        print("No check-ins made yet")
        return
    
    for i, chk in enumerate(checks, 1):
        print(f"{i}.{chk['name']} | {chk['day']} | {chk['time']}")
        
        
# def filter_by_name_asc(checks):
#     """Filter by the names in ascending order"""
#     filtered = [chk for chk in expenses if ]


# ------------------ Main Program ------------------------

def main():
    check = load_list()
    
    while True:
        print("\n === Check-in Tracker ===")
        print("1. Check in")
        print("2. View Checks")
        print("3. Exit")
        
        choice = input("Enter your option: ").strip()
        
        if choice == "1":
            checkin_list(check)
        elif choice == "2":
            view_list(check)
        elif choice == "3":
            print("Goodbye...")
            break
        else:
            print("Invalid choice... try again")
            
if __name__ == "__main__":
    main()