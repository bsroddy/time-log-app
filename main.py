import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager

class EnterActivityScreen(BoxLayout):
    pass

class ActivityLogScreen(BoxLayout):
    pass

class TitleScreen(BoxLayout):
    pass

class ActivityLog(ScreenManager):
    pass


class ActivityLogApp(App):
    """The main app."""
    def build(self):
        return ActivityLog()

if __name__ == '__main__':
    ActivityLogApp().run()