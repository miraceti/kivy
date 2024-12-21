from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

KV = '''
<DEMO>:
    Screen:
        name: "Ecran1"
        MDLabel:
            text: "Ecran 1"
            halign: "center"
        MDRaisedButton:
            text: "Aller a l'ecran 2"
            pos_hint: {"center_x": .5, "center_y": .4}
            on_release: root.current = "Ecran2"

    Screen:
        name: "Ecran2"
        MDLabel:
            text: "Ecran 2"
            halign: "center"
        MDRaisedButton:
            text: "Aller a l'ecran 1"
            pos_hint: {"center_x": .5, "center_y": .4}
            on_release: root.current = "Ecran1"
'''

class DEMO(ScreenManager):
    pass


class Main(MDApp):
    def build(self):
        #Builder.load_file("ui.kv") 
        Builder.load_string(KV)
        return DEMO()
    
Main().run()