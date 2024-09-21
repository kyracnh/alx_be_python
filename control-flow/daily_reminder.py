task = input("Enter your task: ")

# Prompt for the task's priority level (high, medium, low)
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-sensitive (yes or no)
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder message
reminder = f"Reminder: '{task}' is a "

# Process the task using Match Case based on the priority
match priority:
    case "high":
        reminder += "high priority task"
    case "medium":
        reminder += "medium priority task"
    case "low":
        reminder += "low priority task"
    case _:
        reminder += "task with an unrecognized priority level"

# Check if the task is time-sensitive
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Provide the customized reminder
print(reminder)
