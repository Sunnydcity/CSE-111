# Import necessary modules
import json
import datetime
from kivy.config import Config
from kivy.app import App  # Ensure App is imported here
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class PlannerScreen(BoxLayout):
    subject_input = ObjectProperty(None)
    time_input = ObjectProperty(None)
    schedule_display = ObjectProperty(None)
    schedule = {}

    def add_schedule(self):
        subject = self.subject_input.text.strip()
        time = self.time_input.text.strip()

        if not subject or not time:
            self.schedule_display.text = "Please enter both subject and time."
            return

        try:
            # Validate time format
            datetime.datetime.strptime(time, "%H:%M")
            if time in self.schedule:
                self.schedule_display.text = f"Time conflict: {time} is already scheduled."
                return

            self.schedule[time] = subject
            self.update_display()
            self.subject_input.text = ""
            self.time_input.text = ""
        except ValueError:
            self.schedule_display.text = "Invalid time format. Use HH:MM."

    def save_schedule(self):
        with open("schedule.json", "w") as file:
            json.dump(self.schedule, file)
        self.schedule_display.text = "Schedule saved successfully."

    def load_schedule(self):
        try:
            with open("schedule.json", "r") as file:
                self.schedule = json.load(file)
            self.update_display()
        except FileNotFoundError:
            self.schedule_display.text = "No saved schedule found."

    def update_display(self):
        display_text = "\n".join([f"{time}: {subject}" for time, subject in sorted(self.schedule.items())])
        self.schedule_display.text = display_text

class PlannerApp(App):
    def build(self):
        return PlannerScreen()

if __name__ == "__main__":
    PlannerApp().run()
