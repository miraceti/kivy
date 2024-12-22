from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

# from urllib.request import urlopen
# import json
import requests
# import datetime
version= " (v014g)"
##########################################
#code de recuperation des données externes
#######################
urlexo1 = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+count(pl_name)+as+nbe+from+ps+where+default_flag=1&format=json"
print(urlexo1)
# data = json.loads(urlopen(urlexo1).read().decode("utf-8"))
response = requests.get(urlexo1)
data = response.json()
# # print(data)
data0=data[0]
# # print(data0)
nb_exoplanets= data0['nbe']
# print(nb_exoplanets)
# ######################
# now = datetime.date.today()
# y0 = now.year
# print(y0)
# nb_exoplanets = 5100
############################################################
#########################################

KV = '''
<DEMO1>:
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0, 0.5, 0.8, 1  # Couleur bleu clair (RGBA)

        FloatLayout:
            MDLabel:
                id: label_ecran1  # Ajoutez un identifiant pour l'étiquette
                text: 'ECRAN1'
                halign: "center"
                markup: True  # Permet l'utilisation des balises de formatage
                pos_hint: {"center_y": .95}  # Remonter le texte vers le haut

            FloatLayout:
                id: table_ecran1
                pos_hint: {"center_y": .5}  # Remonter la table

        MDBoxLayout:
            size_hint_y: 0.1
            padding: dp(10)
            spacing: dp(10)

            MDRaisedButton:
                text: "Ecran precedent"
                size_hint_x: 0.4
                md_bg_color: 0.2, 0.2, 0.2, 1  # Gris foncé (RGBA)
                text_color: 1, 1, 1, 1  # Blanc
                font_name: "Roboto-Bold"  # Police en gras
                on_release: root.manager.current = "DEMO3"

            MDRaisedButton:
                text: "Ecran suivant"
                size_hint_x: 0.4
                md_bg_color: 0, 0, 0.5, 1  # Bleu foncé (RGBA)
                text_color: 1, 1, 1, 1  # Blanc
                font_name: "Roboto-Bold"  # Police en gras
                on_release: root.manager.current = "DEMO2"

<DEMO2>:
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.30, 0.01, 0.31, 0.8  # Couleur rouge clair (RGBA)
        #rgba(81, 4, 80, 0.8)

        FloatLayout:
            MDLabel:
                text: 'ECRAN2'
                halign: "center"
                pos_hint: {"center_y": .95}  # Remonter le texte vers le haut

        MDBoxLayout:
            size_hint_y: 0.1
            padding: dp(10)
            spacing: dp(10)

            MDRaisedButton:
                text: "Ecran precedent"
                size_hint_x: 0.4
                md_bg_color: 0.2, 0.2, 0.2, 1  # Gris foncé (RGBA)
                text_color: 1, 1, 1, 1  # Blanc
                font_name: "Roboto-Bold"  # Police en gras
                on_release: root.manager.current = "DEMO1"

            MDRaisedButton:
                text: "Ecran suivant"
                size_hint_x: 0.4
                md_bg_color: 0, 0, 0.5, 1  # Bleu foncé (RGBA)
                text_color: 1, 1, 1, 1  # Blanc
                font_name: "Roboto-Bold"  # Police en gras
                on_release: root.manager.current = "DEMO3"

<DEMO3>:
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.1, 0.9, 0.1, 0.8  # Couleur vert clair (RGBA)

        FloatLayout:
            MDLabel:
                text: 'ECRAN3'
                halign: "center"
                pos_hint: {"center_y": .95}  # Remonter le texte vers le haut

        MDBoxLayout:
            size_hint_y: 0.1
            padding: dp(10)
            spacing: dp(10)

            MDRaisedButton:
                text: "Ecran precedent"
                size_hint_x: 0.4
                md_bg_color: 0.2, 0.2, 0.2, 1  # Gris foncé (RGBA)
                text_color: 1, 1, 1, 1  # Blanc
                font_name: "Roboto-Bold"  # Police en gras
                on_release: root.manager.current = "DEMO2"

            MDRaisedButton:
                text: "Ecran suivant"
                size_hint_x: 0.4
                md_bg_color: 0, 0, 0.5, 1  # Bleu foncé (RGBA)
                text_color: 1, 1, 1, 1  # Blanc
                font_name: "Roboto-Bold"  # Police en gras
                on_release: root.manager.current = "DEMO1"

'''

class DEMO1(Screen):
    def on_enter(self, *args):
        # Mettre à jour le texte de l'étiquette

        self.ids.label_ecran1.text = f"Nombre d'exoplanètes dé&couvertes à ce jour : [color=ff0000][b][size=30]{nb_exoplanets}[/size][/b][/color] "  # Mettre à jour le texte de l'étiquette
        # Define Table
        self.table = MDDataTable(
            use_pagination=True,
            pos_hint={'center_x': 0.5, 'center_y': 0.5},  # Centrer la table
            size_hint=(0.9, None),  # Largeur fixe et hauteur dynamique
            height=dp(8 * 48 + 56),  # 5 lignes * 48dp + 56dp pour l'en-tête
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
        """    Fonction de tri personnalisée pour la colonne Email Address.    """
        # Trier les données par la 3ème colonne (index 2)
        sorted_data = sorted(data, key=lambda row: row[2])  
        # Extraire les indices et les données triées
        sorted_indices = [i for i in range(len(sorted_data))]
        return sorted_indices, sorted_data
    
class DEMO2(Screen):
    pass

class DEMO3(Screen):
    pass

class Main(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        Builder.load_string(KV)

        sm = ScreenManager()
        sm.add_widget(DEMO1(name="DEMO1"))
        sm.add_widget(DEMO2(name="DEMO2"))
        sm.add_widget(DEMO3(name="DEMO3"))

        return sm

Main().run()
