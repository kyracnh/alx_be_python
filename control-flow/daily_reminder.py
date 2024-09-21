task = input("Enter your task for today: ")
priority = input("What is the priority of this task? (high, medium, low): ").lower()
time_bound = input("Is this task time-sensitive? (yes or no): ").lower()

match priority:
    case "high":
        reminder = f"Reminder: Your task '{task}' is of high priority."
    case "medium":
        reminder = f"Reminder: Your task '{task}' is of medium priority."
    case "low":
        reminder = f"Reminder: Your task '{task}' is of low priority."
    case _:
        reminder = f"Reminder: Your task '{task}' has an unrecognized priority level."

if time_bound == "yes":
    reminder += " It requires immediate attention today!"

print(reminder)
