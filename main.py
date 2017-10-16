import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.config import Config

class EnterActivityScreen(BoxLayout):
    pass


class enter_activity_screenApp(App):
    """The main app."""
    def build(self):
        return EnterActivityScreen()

if __name__ == '__main__':
    enter_activity_screenApp().run()