import time
import datetime


class Activity():
    """An activity that the user engages in and logs."""

    def __init__(self, name):
        """Initialize with name (string) attribute."""
        self.name = name

    def update_name(self, new_name):
        """Takes str. Update name (string) attribute."""
        self.name = new_name

    def get_name(self):
        """Return name (string) attribute."""
        return self.name


class Time():
    """A time, hour (24-hour format) and minute."""
    #Fated to be wrapper class for built-in Python datetime or time module.

    def __init__(self, hour, minute):
        """Initialize with hour (int) and minute (int) attributes.  Hour variable is in 24-hour format."""
        self.hour = hour
        self.minute = minute

    def update_hour(self, new_hour):
        """Takes int. Update hour (int) attribute."""
        self.hour = new_hour

    def get_hour(self):
        """Return hour (int) attribute."""
        return self.hour

    def update_minute(self, new_minute):
        """Takes int. Update minute (int) attribute."""
        self.minute = new_minute

    def get_minute(self):
        """Return minute (int) attribute."""
        return self.minute


class LogEntry():
    """An entry into the day's activities, including the beginning and ending times."""

    def __init__(self, activity, start_time, end_time):
        """Initialize with activity (Activity), start_time (Time), and end_time (Time) attributes."""
        self.activity = activity
        self.start_time = start_time
        self.end_time = end_time

    def update_activity(self, new_activity):
        """Takes Activity. Update activity (Activity) attribute."""
        self.activity = new_activity

    def get_activity(self):
        """Return activity (Activity) attribute."""
        return self.activity

    def update_start_time(self, new_start_time):
        """Takes Time. Update start_time (Time) attribute."""
        self.start_time = new_start_time

    def get_start_time(self):
        """Return start_time (Time) attribute."""
        return self.start_time

    def update_end_time(self, new_end_time):
        """Takes Time. Update end_time (Time) attribute."""
        self.end_time = new_end_time

    def get_end_time(self):
        """Return end_time (Time) attribute."""
        return self.end_time


class Date():
    def __init__(self, month, day, year):
        """Initialize with month (int), day (int), and year (int) attributes."""
        self.month = month
        self.day = day
        self.year = year

    def update_month(self, new_month):
        """Takes int. Update month (int) attribute."""
        self.month = new_month

    def get_month(self):
        """Return month (int) attribute."""
        return self.month

    def update_day(self, new_day):
        """Takes int. Update day (int) attribute."""
        self.day = new_day

    def get_day(self):
        """Return day (int) attribute."""
        return self.day

    def update_year(self, new_year):
        """Takes int. Update year (int) attribute."""
        self.year = new_year

    def get_year(self):
        """Return year (int) attribute."""
        return self.year


class ActivityLog():
    """A list of activities logged on a particular date."""

    def __init__(self, date=None):
        """Initialize with log_entry_list (list of LogEntry) attribute and optional date attribute."""
        self.log_entry_list = []
        self.date = date

    def get_log_entry_list(self):
        """Returns list of LogEntry's."""
        return self.log_entry_list

    def add_log_entry(self, log_entry):
        """Takes LogEntry. Adds an entry to the activity log."""
        self.log_entry_list.append(log_entry)

    def clear_log_entry_list(self):
        """Clears the list of LogEntry's."""
        del self.log_entry_list[:]

    def get_date(self):
        """Returns this ActivityLog's Date--the date on which its activities took place."""
        return self.date

    def set_date(self, new_date):
        """Sets this ActivityLog's Date."""
        self.date = new_date


class HistoricalDay():
    """The record of a past day's activities."""

    def __init__(self, activity_log, day_of_the_week=None):
        """Initialize with log_entry_list (list of LogEntry) attribute and optional day_of_the_week attribute."""
        self.activity_log = activity_log
        self.day_of_the_week = day_of_the_week

    def get_activity_log(self):
        """Returns activity_log."""
        return self.activity_log

    def set_activity_log(self, new_activity_log):
        """Sets activity log."""
        self.activity_log = new_activity_log

    def get_day_of_the_week(self):
        """Returns day of the week."""
        return self.day_of_the_week

    def set_day_of_the_week(self, new_day_of_the_week):
        """Sets day_of_the_week."""
        self.day_of_the_week = new_day_of_the_week


class HistoricalMonth():
    """The records of a month of HistoricalDays."""

    def __init__(self, list_of_days, month_of_the_year=None):
        """Initialize with list_of_days (list of HistoricalDay) attribute and optional month_of_the_year attribute."""
        self.list_of_days = list_of_days
        self.month_of_the_year = month_of_the_year

    def get_list_of_days(self):
        """Returns list_of_days."""
        return self.list_of_days

    def set_list_of_days(self, new_list_of_days):
        """Sets list_of_days."""
        self.list_of_days = new_list_of_days

    def get_month_of_the_year(self):
        """Returns month_of_the_year."""
        return self.month_of_the_year

    def set_month_of_the_year(self, new_month_of_the_year):
        """Sets month_of_the_year."""
        self.month_of_the_year = new_month_of_the_year


class HistoricalYear():
    """The records of a month of HistoricalDays."""

    def __init__(self, list_of_months, year_number=None):
        """Initialize with list_of_months (list of HistoricalMonth) attribute and optional year_number attribute."""
        self.list_of_months = list_of_months
        self.year_number = year_number

    def get_list_of_months(self):
        """Returns list_of_months."""
        return self.list_of_months

    def set_list_of_months(self, new_list_of_months):
        """Sets list_of_months."""
        self.list_of_months = new_list_of_months

    def get_year_number(self):
        """Returns year_number."""
        return self.year_number

    def set_year_number(self, new_year_number):
        """Sets year_number."""
        self.year_number = new_year_number


class HistoricalCalendar():
    """The records of a month of HistoricalDays."""

    def __init__(self, list_of_years):
        """Initialize with list_of_years (list of HistoricalYear)."""
        self.list_of_years = list_of_years

    def get_list_of_years(self):
        """Returns list_of_years."""
        return self.list_of_years

    def set_list_of_years(self, new_list_of_years):
        """Sets list_of_years."""
        self.list_of_years = new_list_of_years