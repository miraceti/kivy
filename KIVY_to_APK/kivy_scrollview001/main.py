from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = 360, 640
class Layout_(FloatLayout):
    pass

class Main(MDApp):
    def build(self):
        Builder.load_file("ui.kv")
        return Layout_()
    

Main().run()