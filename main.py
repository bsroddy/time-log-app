import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager

from class_structure import Activity, ActivityLog, LogEntry


class EnterActivityScreen(BoxLayout):
    pass

class ActivityLogScreen(BoxLayout):
    pass

class TitleScreen(BoxLayout):
    pass

def easy(n, *args):
    print n

class TimeLog(ScreenManager):
    def __init__(self, **kwargs):
        super(TimeLog, self).__init__(**kwargs)
        self.activity_log = ActivityLog()
        self.activity_list = []
        self.enter_activity_buttons = self.ids['enter_activity_buttons']
        self.displayed_activity_log = self.ids['activity_log']

    def add_activity_to_list(self, new_activity_name):
        for activity in self.activity_list:
            if activity.get_name() == new_activity_name:
                #Exits method.  The named activity is already in the list of activities.
                return

        self.activity_list.append(Activity(new_activity_name))

    def populate_enter_activity_buttons(self):
        for activity in self.activity_list:
            #To do: Add time handling (start and end time).
            new_button = Button(text = activity.get_name())

            new_button.bind(on_release=self.populate_displayed_activity_log)
            new_button.bind(on_release=self.clear_displayed_activity_log)
            new_button.bind(on_release = lambda *args: self.activity_log.add_log_entry(LogEntry(activity, start_time=0, end_time=0)))

            self.enter_activity_buttons.add_widget(new_button)

    def clear_enter_activity_buttons(self):
        self.enter_activity_buttons.clear_widgets()

    def populate_displayed_activity_log(self, *args):
        for log_entry in self.activity_log.get_log_entry_list():
            new_button = Button(text = log_entry.get_activity().get_name())
            self.displayed_activity_log.add_widget(new_button)

    def clear_displayed_activity_log(self, *args):
        self.displayed_activity_log.clear_widgets()

    def log_activity(self, activity):
        #To do: add time handling.
        self.activity_log.add_log_entry(log_entry = LogEntry(activity, start_time = 0, end_time = 0))






class TimeLogApp(App):
    """The main app."""
    def build(self):
        return TimeLog()

if __name__ == '__main__':
    TimeLogApp().run()