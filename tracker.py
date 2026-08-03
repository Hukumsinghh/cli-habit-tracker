import json
import os
from datetime import datetime

DATA_FILE = 'habits.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def add_habit(data):
    habit = input("Enter a new habit to track: ").strip()
    if habit and habit not in data:
        data[habit] = {"streak": 0, "last_completed": None}
        print(f"Success: '{habit}' added to your tracker. Time to get 1% better!")
    else:
        print("Habit already exists or invalid input.")

def complete_habit(data):
    print("\n--- Your Habits ---")
    for i, habit in enumerate(data.keys(), 1):
        print(f"{i}. {habit} (Current Streak: {data[habit]['streak']} days)")
    
    choice = input("\nEnter the name of the habit you completed today: ").strip()
    
    if choice in data:
        today = datetime.now().strftime("%Y-%m-%d")
        if data[choice]["last_completed"] == today:
            print("You already completed this habit today. Great job!")
            return
            
        data[choice]["streak"] += 1
        data[choice]["last_completed"] = today
        print(f"Awesome! Your streak for '{choice}' is now {data[choice]['streak']} days.")
    else:
        print("Habit not found.")

def main():
    data = load_data()
    while True:
        print("\n=== Daily Habit Tracker ===")
        print("1. Add a new habit")
        print("2. Mark habit as complete")
        print("3. View all streaks")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            add_habit(data)
        elif choice == '2':
            complete_habit(data)
        elif choice == '3':
            print("\n--- Current Streaks ---")
            for habit, info in data.items():
                print(f"• {habit}: {info['streak']} days")
        elif choice == '4':
            save_data(data)
            print("Progress saved. See you tomorrow!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()