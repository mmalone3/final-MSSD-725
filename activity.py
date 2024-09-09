
class Activity:
    def __init__(self, name, duration_minutes, activity_type):
        """
        Initialize an Activity object.

        Args:
            name (str): Name of the person performing the activity.
            duration_minutes (int): Duration of the activity in minutes.
            activity_type (str): Type of activity being performed.
        """
        self.name = name
        self.duration_minutes = duration_minutes
        self.activity_type = activity_type

    def display_activity(self):
        """
        Display the activity information.
        """
        print(f"Activity Type: {self.activity_type}")
        print(f"Duration: {self.duration_minutes} minutes")
        print(f"Name: {self.name}")

    def congratulate(self):
        """
        Print a congratulatory message for completing the activity.
        """
        print(f"Good job {self.name} for spending {self.duration_minutes} minutes on {self.activity_type}!")

# Example usage:
if __name__ == "__main__":
    # Static creation
    static_activity = Activity("Alice", 60, "Running")
    static_activity.display_activity()
    static_activity.congratulate()

    # Dynamic creation
    name = input("Enter your name: ")
    duration = int(input("Enter activity duration in minutes: "))
    activity_type = input("Enter activity type: ")

    dynamic_activity = Activity(name, duration, activity_type)
    dynamic_activity.display_activity()
    dynamic_activity.congratulate()
