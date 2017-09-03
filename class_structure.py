import time
import datetime

class Activity():
    """A basic activity that the user engages in."""

    def __init__(self, name):
        """Initialize with name (string) attribute."""
        self.name = name

    def update_name(self, new_name):
        """Update name (string) attribute."""
        self.name = new_name

    def get_name(self):
        """Return name (string) attribute."""
        return self.name

class Time():
    def __init__(self, hour, minute):
        """Initialize with hour (int) and minute (int) attributes.  Hour var is in 24-hour format."""
        self.hour = hour
        self.minute = minute

    def update_hour(self, new_hour):
        """Update hour (int) attribute."""
        self.hour = new_hour

    def get_hour(self):
        """Return hour (int) attribute."""
        return self.hour

    def update_minute(self, new_minute):
        """Update minute (int) attribute."""
        self.minute = new_minute

    def get_minute(self):
        """Return minute (int) attribute."""
        return self.minute



class Scheduled_Activity():
    """A basic activity that the user engages in."""

    def __init__(self, activity, start_time, end_time):
        """Initialize with activity (activity), start_time (time), and end_time (time) attributes."""
        self.activity = activity
        self.start_time = start_time
        self.end_time = end_time

    def update_activity(self, new_activity):
        """Update activity (activity) attribute."""
        self.activity = new_activity

    def update_start_time(self, new_start_time):
        """Update start_time (time) attribute."""
        self.start_time = new_start_time

    def update_end_time(self, new_end_time):
        """Update end_time (time) attribute."""
        self.end_time = new_end_time




print time.localtime(time.time()).tm_hour,":",time.localtime(time.time()).tm_min