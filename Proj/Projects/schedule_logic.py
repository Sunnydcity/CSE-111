import json

# Save schedule to a JSON file
def save_schedule(schedule, filename="schedule.json"):
    with open(filename, "w") as file:
        json.dump(schedule, file)

# Load schedule from a JSON file
def load_schedule(filename="schedule.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Create a schedule dictionary
def create_schedule(subjects, times):
    return {time: subject for subject, time in zip(subjects, times)}

# Validate schedule to ensure no overlap
def validate_schedule(subjects, times):
    time_objects = [datetime.datetime.strptime(time, "%H:%M") for time in times]
    time_objects.sort()
    for i in range(1, len(time_objects)):
        if time_objects[i] == time_objects[i - 1]:
            return False
    return True
