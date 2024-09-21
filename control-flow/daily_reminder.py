task = str(input("Enter your task:"))
priority = str(input("Priority (high/medium/low):"))
time_bound = str(input("Is it time-bound? (yes/no):"))

match priority:
    case "high":
        reminder = f"Your task '{task}' is of high priority."
    case "medium":
        reminder = f"Your task '{task}' is of medium priority."
    case "low":
        reminder = f"Your task '{task}' is of low priority."
    case _:
        reminder = f"Your task '{task}' has an unrecognized priority level."
if time_bound == "yes":
    reminder += " It requires immediate attention today!"

print(reminder)
