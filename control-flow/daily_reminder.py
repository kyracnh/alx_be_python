task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task. This task requires immediate attention today!")
        else :
            print(f"Note: '{task}' is a high priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task. This task requires immediate attention today!")
        else :
            print(f"Note: '{task}' is a high priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task. This task requires immediate attention today!")
        else :
            print(f"Note: '{task}' is a high priority task. Consider completing it when you have free time.")
    case _:
        print(f"Reminder: '{task}' priority is not recognized, but it still needs to be completed.")
