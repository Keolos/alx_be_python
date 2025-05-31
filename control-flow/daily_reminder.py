# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case to generate base reminder message based on priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Task priority '{priority}' is not recognized."

# Modify the reminder message based on whether the task is time-bound
if priority in ["high", "medium", "low"]:
    if time_bound == "yes":
        # Append urgency message for time-sensitive tasks
        reminder += " that requires immediate attention today!"
    else:
        # Append different message if not time-bound
        if priority == "low":
            reminder += ". Consider completing it when you have free time."
        else:
            reminder += "."

# Print the customized reminder that includes task, priority, and urgency info
print(reminder)

