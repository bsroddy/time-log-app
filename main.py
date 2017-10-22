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

class TimeLog(ScreenManager):
    def __init__(self, **kwargs):
        super(TimeLog, self).__init__(**kwargs)
        self.activity_log = ActivityLog()
        self.activity_list = []
        self.enter_activity_buttons = self.ids['enter_activity_buttons']

    def add_activity_to_list(self, new_activity_name):
        for activity in self.activity_list:
            if activity.get_name() == new_activity_name:
                #Exits method.  The named activity is already in the list of activities.
                return

        self.activity_list.append(Activity(new_activity_name))

    def populate_enter_activity_buttons(self):
        for activity in self.activity_list:
            new_button = Button(text = activity.get_name())
            self.enter_activity_buttons.add_widget(new_button)

    def clear_enter_activity_buttons(self):
        self.enter_activity_buttons.clear_widgets()




class TimeLogApp(App):
    """The main app."""
    def build(self):
        return TimeLog()

if __name__ == '__main__':
    TimeLogApp().run()