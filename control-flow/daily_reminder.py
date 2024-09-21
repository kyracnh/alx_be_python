task = input("Enter your task: ")

# Prompt for the task's priority level
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-sensitive
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Provide customized reminder using Match Case and conditional statements
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Reminder: '{task}' has an unrecognized priority level"

# Modify the reminder based on time sensitivity
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# The print statement now explicitly starts with "Reminder:"
print(f"{reminder}")
