from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style= "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('kivy045.kv')
    
    def presser(self):
        self.root.ids.my_label.text= "You pressesd it !!"

MainApp().run()