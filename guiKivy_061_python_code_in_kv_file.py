from kivy_garden import mapview
from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):
    some_text = "Helllo World!"
    our_list =["John","Mary","Tina"]
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('kivy061.kv')

MainApp().run()
 
