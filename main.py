from kivy.app import App

from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput


class PushSenderApp(App):
    def build(self):
        return MainTab()


class MainTab(Widget):
    pass


if __name__ == '__main__':
    PushSenderApp().run()