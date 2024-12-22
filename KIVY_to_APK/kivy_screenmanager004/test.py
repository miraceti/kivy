from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

KV = '''
<DEMO1>:
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0, 0.5, 0.8, 1  # Couleur bleu clair (RGBA)

        MDLabel:
            text: 'ECRAN1'
            halign: "center"
            pos_hint: {"center_y": .95, "center_x": .5}

        FloatLayout:
            id: table_ecran1

        MDBoxLayout:
            size_hint_y: 0.1
            padding: dp(10)
            spacing: dp(10)

            MDRaisedButton:
                text: "Ecran precedent"
                size_hint_x: 0.4
                on_release: root.manager.current = "DEMO3"

            MDRaisedButton:
                text: "Ecran suivant"
                size_hint_x: 0.4
                on_release: root.manager.current = "DEMO2"

<DEMO2>:
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0, 0.5, 0.8, 1  # Couleur bleu clair (RGBA)

        MDLabel:
            text: 'ECRAN2'
            halign: "center"
            pos_hint: {"center_y": .95, "center_x": .5}

        MDBoxLayout:
            size_hint_y: 0.1
            padding: dp(10)
            spacing: dp(10)

            MDRaisedButton:
                text: "Ecran precedent"
                size_hint_x: 0.4
                on_release: root.manager.current = "DEMO1"

            MDRaisedButton:
                text: "Ecran suivant"
                size_hint_x: 0.4
                on_release: root.manager.current = "DEMO3"

<DEMO3>:
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0, 0.5, 0.8, 1  # Couleur bleu clair (RGBA)

        MDLabel:
            text: 'ECRAN3'
            halign: "center"
            pos_hint: {"center_y": .95, "center_x": .5}

        MDBoxLayout:
            size_hint_y: 0.1
            padding: dp(10)
            spacing: dp(10)

            MDRaisedButton:
                text: "Ecran precedent"
                size_hint_x: 0.4
                on_release: root.manager.current = "DEMO2"

            MDRaisedButton:
                text: "Ecran suivant"
                size_hint_x: 0.4
                on_release: root.manager.current = "DEMO1"

'''

class DEMO1(Screen):
    def on_enter(self, *args):
        # Define Table
        self.table = MDDataTable(
            use_pagination=True,
            pos_hint={'center_x': 0.5, 'center_y': 0.8},
            size_hint=(0.9, 0.9),
            check=True,
            column_data=[
                ("First Name", dp(30)),
                ("Last Name", dp(30)),
                ("Email Address", dp(30),self.sort_on_email),
                ("Phone Number", dp(30))
            ],
            row_data=[
                ("1John", "Elder", "john@codemy.com", "(123) 456-7891"),
                ("2Mary", "Elder", "mary@codemy.com", "(123) 456-1123"),
                ("3Mary", "Elder", "mary@codemy.com", "(123) 456-1123"),
                ("4Mary", "Elder", "mary@codemy.com", "(123) 456-1123"),
                ("5Mary", "Elder", "mary@codemy.com", "(123) 456-1123"),
                ("6Mary", "Elder", "mary@codemy.com", "(123) 456-1123"),
                ("7Mary", "Elder", "mary@codemy.com", "(123) 456-1123"),
                ("8John", "Elder", "john@codemy.com", "(123) 456-7891"),
                ("9Mary", "Elder", "mary@codemy.com", "(123) 456-1123"),
                ("10Mary", "Elder", "mary@codemy.com", "(123) 456-1123"),
                ("11Mary", "Elder", "mary@codemy.com", "(123) 456-1123"),
                ("12Mary", "Elder", "mary@codemy.com", "(123) 456-1123"),
                ("13Mary", "Elder", "mary@codemy.com", "(123) 456-1123"),
                ("14Mary", "Elder", "mary@codemy.com", "(123) 456-1123"),
            ],
            sorted_on="Email Address",
            sorted_order="ASC",
            elevation=2,
        )
        self.ids.table_ecran1.bind(on_row_press=self.on_row_press)
        self.ids.table_ecran1.bind(on_check_press=self.on_check_press)
        self.ids.table_ecran1.add_widget(self.table)

    def on_row_press(self, instance_table, instance_row):
        '''Called when a table row is clicked.'''

        print(instance_table, instance_row)

    def on_check_press(self, instance_table, current_row):
        '''Called when the check box in the table row is checked.'''

        print(instance_table, current_row)

    def sort_on_email(self, data):
        return zip(
            *sorted(
                enumerate(data),
                key=lambda l: sum(
                    [
                        int(l[1][-2].split("@")[0]) * 60,
                        int(l[1][-2].split("@")[1]),
                    ]
                ),
            )
        )

    
class DEMO2(Screen):
    pass

class DEMO3(Screen):
    pass

class Main(MDApp):
    def build(self):
        Builder.load_string(KV)

        sm = ScreenManager()
        sm.add_widget(DEMO1(name="DEMO1"))
        sm.add_widget(DEMO2(name="DEMO2"))
        sm.add_widget(DEMO3(name="DEMO3"))

        return sm

Main().run()
