from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

class DEMO1(Screen):
    pass

class DEMO2(Screen):
    pass

class Main(MDApp):
    def build(self):
        Builder.load_file("ui.kv")

        sm = ScreenManager()
        sm.add_widget(DEMO1(name = "DEMO1"))
        sm.add_widget(DEMO2(name = "DEMO2"))

        return sm
    
Main().run()