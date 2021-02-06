from kivy.uix.screenmanager import Screen

from kivymd.toast import toast
from kivymd.uix.button import MDFloatingActionButtonSpeedDial


class KitchenSinkStackButtons(Screen):
    already_create_buttons = False

    def on_enter(self, *args):
        if not self.already_create_buttons:

            def callback(instance_button):
                toast(instance_button.icon)

            button_speed_dial = MDFloatingActionButtonSpeedDial()
            button_speed_dial.rotation_root_button = True
            button_speed_dial.data = {
                "language-python": "Python",
                "language-php": "PHP",
                "language-cpp": "C++",
            }
            button_speed_dial.callback = callback
            self.add_widget(button_speed_dial)
            self.already_create_buttons = True
