from kivy_garden import mapview
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy_garden.mapview import MapView

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('kivy060.kv')

MainApp().run()
 
