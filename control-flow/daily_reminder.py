
# Step 1: Ask for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Step 2: Match case for priority and generate reminder message
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task."
    case "low":
        reminder = f"Note: '{task}' is a low priority task."
    case _:
        reminder = f"Reminder: '{task}' priority is not recognized, but it still needs to be completed."

# Step 3: Modify reminder based on time sensitivity
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."

    # Step 4: Output the final reminder
print(reminder)
