from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.core.window import Window

KV = '''
<Layout_>
    ScrollView:
        size: self.size
        GridLayout:
            size_hint_y: None
            height: self.minimum_height
            width: self.minimum_width
            cols: 2
            spacing: "20dp"
            padding: "20dp"

            MDCard:
                orientation: "vertical"
                padding: "8dp"
                size_hint: 1, None
                height: "210dp"
                elevation: 5
                border_radius: 20
                radius: [15]
            MDCard:
                orientation: "vertical"
                padding: "8dp"
                size_hint: 1, None
                height: "210dp"
                elevation: 5
                border_radius: 20
                radius: [15]
            MDCard:
                orientation: "vertical"
                padding: "8dp"
                size_hint: 1, None
                height: "210dp"
                elevation: 5
                border_radius: 20
                radius: [15]
            MDCard:
                orientation: "vertical"
                padding: "8dp"
                size_hint: 1, None
                height: "210dp"
                elevation: 5
                border_radius: 20
                radius: [15]
            MDCard:
                orientation: "vertical"
                padding: "8dp"
                size_hint: 1, None
                height: "210dp"
                elevation: 5
                border_radius: 20
                radius: [15]
            MDCard:
                orientation: "vertical"
                padding: "8dp"
                size_hint: 1, None
                height: "210dp"
                elevation: 5
                border_radius: 20
                radius: [15]
            MDCard:
                orientation: "vertical"
                padding: "8dp"
                size_hint: 1, None
                height: "210dp"
                elevation: 5
                border_radius: 20
                radius: [15]
            MDCard:
                orientation: "vertical"
                padding: "8dp"
                size_hint: 1, None
                height: "210dp"
                elevation: 5
                border_radius: 20
                radius: [15]
            MDCard:
                orientation: "vertical"
                padding: "8dp"
                size_hint: 1, None
                height: "210dp"
                elevation: 5
                border_radius: 20
                radius: [15]
            MDCard:
                orientation: "vertical"
                padding: "8dp"
                size_hint: 1, None
                height: "210dp"
                elevation: 5
                border_radius: 20
                radius: [15]
                               
'''

Window.size = 360, 640
class Layout_(FloatLayout):
    pass

class Main(MDApp):
    def build(self):
        #Builder.load_file("ui.kv")
        Builder.load_string(KV)
        return Layout_()
    

Main().run()