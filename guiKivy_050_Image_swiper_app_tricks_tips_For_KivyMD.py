from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):
    
    def build(self):
        self.theme_cls.theme_style= "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('kivy050.kv')
    
    def on_swipe_left(self):
        self.root.ids.toolbar.title="you swipe left"
        print("you swipe left")
    
        
    def on_swipe_right(self):
        self.root.ids.toolbar.title="you swipe right"
        print("you swipe right")
    
MainApp().run()