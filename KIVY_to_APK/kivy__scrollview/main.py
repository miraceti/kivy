from kivymd.app import MDApp
from kivy.uix.floatlayout import floatlayout
from kivy.lang import Builder
from kivy.core.window import window

Window.size = 360, 640
class Layout_(floatlayout):
    pass

class Main(MDApp):
    def build(self):
        Builder.load_file("ui.kv")
        return Layout_()