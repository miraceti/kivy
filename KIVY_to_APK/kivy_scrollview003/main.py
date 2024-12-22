from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.core.window import Window

KV = '''
<Layout_>
    ScrollView:
        siwidth: root.width
        size_hint_y: None
        height: root.height
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
                MDLabel:
                    id: cart1_text
                    text: "ici1"
                    halign:"center"
            MDCard:
                orientation: "vertical"
                padding: "8dp"
                size_hint: 1, None
                height: "210dp"
                elevation: 5
                border_radius: 20
                radius: [15]
                MDLabel:
                    id: cart2_text
                    text: "ici2"
            MDCard:
                orientation: "vertical"
                padding: "8dp"
                size_hint: 1, None
                height: "210dp"
                elevation: 5
                border_radius: 20
                radius: [15]
                MDLabel:
                    id: cart3_text
                    text: "ici3"
            MDCard:
                orientation: "vertical"
                padding: "8dp"
                size_hint: 1, None
                height: "210dp"
                elevation: 5
                border_radius: 20
                radius: [15]
                MDLabel:
                    id: cart4_text
                    text: "ici4"
            MDCard:
                orientation: "vertical"
                padding: "8dp"
                size_hint: 1, None
                height: "210dp"
                elevation: 5
                border_radius: 20
                radius: [15]
                MDLabel:
                    id: cart5_text
                    text: "ici5"
            MDCard:
                orientation: "vertical"
                padding: "8dp"
                size_hint: 1, None
                height: "210dp"
                elevation: 5
                border_radius: 20
                radius: [15]
                MDLabel:
                    id: cart6_text
                    text: "ici6"
            MDCard:
                orientation: "vertical"
                padding: "8dp"
                size_hint: 1, None
                height: "210dp"
                elevation: 5
                border_radius: 20
                radius: [15]
                MDLabel:
                    id: cart7_text
                    text: "ici7"
            MDCard:
                orientation: "vertical"
                padding: "8dp"
                size_hint: 1, None
                height: "210dp"
                elevation: 5
                border_radius: 20
                radius: [15]
                MDLabel:
                    id: cart8_text
                    text: "ici8"
            MDCard:
                orientation: "vertical"
                padding: "8dp"
                size_hint: 1, None
                height: "210dp"
                elevation: 5
                border_radius: 20
                radius: [15]
                MDLabel:
                    id: cart9_text
                    text: "ici9"
            MDCard:
                orientation: "vertical"
                padding: "8dp"
                size_hint: 1, None
                height: "210dp"
                elevation: 5
                border_radius: 20
                radius: [15]
                MDLabel:
                    id: cart10_text
                    text: "ici10"
                               
'''

Window.size = 360, 640
class Layout_(FloatLayout):
    pass

class Main(MDApp):
    def build(self):
        #Builder.load_file("ui.kv")
        Builder.load_string(KV)
        
        return Layout_()
    
    def on_start(self):
        cart2_text_var2="pas la"
        name=self.root.ids.cart2_text.text
        print(name)
        self.root.ids.cart2_text.text=cart2_text_var2

        return super().on_start()

Main().run()