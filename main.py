from kivy.app import App

from kivy.uix.dropdown import DropDown
from kivy.uix.tabbedpanel import TabbedPanel


class PushSenderApp(App):
    def build(self):
        return MainWindow()


class MainWindow(TabbedPanel):
    pass


class ApplicationsNamesDropDown(DropDown):
    pass


if __name__ == '__main__':
    PushSenderApp().run()