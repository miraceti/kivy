from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

from kivy.uix.floatlayout import FloatLayout
# from kivy_garden.matplotlib import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

# from urllib.request import urlopen
# import json
import requests
# import datetime
version= " (v010)"
##########################################
#code de recuperation des données externes
urlexo_pllist = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+distinct+pl_name,disc_year,sy_dist,discoverymethod,pl_bmasse,pl_rade\
+from+ps+&format=json"
response = requests.get(urlexo_pllist)
data_pllist = response.json()
#######################
#### ECRAN1
#######################
data_nbpl = list({(item['pl_name']) for item in data_pllist})
nb_exoplanets= len(data_nbpl)

# Regrouper par 'pl_name' et garder les valeurs maximales pour les autres colonnes
aggregated_data = {}
for row in data_pllist:
    pl_name = row['pl_name']
    if pl_name not in aggregated_data:
        aggregated_data[pl_name] = row
    else:
        for key in row:
            if key != 'pl_name' and row[key] is not None:
                # Conserver la valeur maximale pour les autres colonnes
                aggregated_data[pl_name][key] = max(aggregated_data[pl_name][key], row[key]) if aggregated_data[pl_name][key] is not None else row[key]

# Convertir en une liste de tuples pour MDDataTable
data_table_tuple = [
    (row['pl_name'], row['disc_year'], row['sy_dist'], row['discoverymethod'], row['pl_bmasse'], row['pl_rade'])
    for row in aggregated_data.values()
]
#######################

#######################
### ECRAN2
#######################
#cle associés
keys = ["pl_name","disc_year","sy_dist","discoverymethod","pl_bmasse","pl_rade"]

#conversion en liste de dict
data_table_dict = [dict(zip(keys, tpl)) for tpl in data_table_tuple]

#######################

#######################
### ECRAN3
#######################
#extraction des tuples (pl_name, disc_year) sans doublons
unique_data = list(set(map(lambda x: (x['pl_name'], x['disc_year']), data_table_dict)))

#creation du comptage par année
from collections import Counter
#comptage decouverte par annee
discovery_counts = Counter(item['disc_year'] for item in data_table_dict)
#tri par annee
sorted_discovery_counts = sorted(discovery_counts.items())

#separation resultat en 2 listes
liste_annee, liste_nb = zip(*sorted_discovery_counts)

liste_annee = list(liste_annee)
liste_nb = list(liste_nb)

#tracer graphique
plt.figure(3, figsize=(10,6))
plt.plot(liste_annee, liste_nb, marker='o', linestyle='-', color='b', label='Nombre par année')
plt.title("Nombre d'exoplanètes par année")
plt.xlabel("Année")
plt.ylabel("Nombre")
plt.grid(True)
plt.legend()
# plt.show()


#######################
### ECRAN4
#######################
# plt.figure(4)
# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100

# plt.scatter('a', 'b', c='c', s='d', data=data)
# plt.xlabel('entry a')
# plt.ylabel('entry b')
# # plt.show()

#extraire les données
x = [item['disc_year'] for item in data_table_dict] #année de decouverte : X
y = [item['pl_bmasse'] for item in data_table_dict] #masse de la planete : Y
methods = [item['discoverymethod'] for item in data_table_dict]#methode de decouverte

#taille des points
size = 100

#palette de couleurs
unique_methods = list(set(methods))
colors = {method: plt.cm.tab10(i) for i, method in enumerate(unique_methods)}

#tracer graph
plt.figure(4, figsize=(10,6))

for method in unique_methods:
    #filtrage data par methodes
    x_vals = [x[i] for i in range(len(x)) if methods[i]== method]
    y_vals = [y[i] for i in range(len(y)) if methods[i]== method]
    plt.scatter(x_vals, y_vals, s=size, color=colors[method], label=method, alpha=0.7, edgecolors='w')

#ajout detail graph
plt.title("Masse de la planete VS Année de découverte", fontsize=16)
plt.xlabel("Année de découverte (disc_year)", fontsize=14)
plt.ylabel("Masse de la planete (pl_bmasse)", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)

#legende
plt.legend(title="Méthodes de découvertes", fontsize=12, loc='center left', bbox_to_anchor=(1, 0.5))

#ajuster l'epacement
plt.tight_layout()

#######################
### ECRAN5
#######################

#pie
# plt.style.use('dark_background')
# labels = 'Frogs', 'Hogs', 'Dogs', 'logs'
# sizes = [15, 30, 45, 10]
# fig, ax = plt.subplots()
# ax.pie(sizes, labels=labels)


#########
#comptage des ocurence
discovery_methods = [item['discoverymethod'] for item in data_table_dict]
method_counts = Counter(discovery_methods)

#preparation données
labels = list(method_counts.keys())
counts = list(method_counts.values())

#palette de couleurs pour les barres
colors = plt.cm.Paired.colors[:len(labels)]

#tracage
plt.figure(5, figsize=(10,6))
plt.bar(labels, counts, color=colors, edgecolor='black')
plt.title("Répartition  des méthodes de découverte", fontsize=16)
plt.xlabel("Méthodes de découverte", fontsize=14)
plt.ylabel("nombre d'éléments", fontsize=14)
plt.xticks(rotation=45 , fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()


fig_num=plt.gcf().number
print(fig_num)
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
                on_release: root.manager.current = "DEMO5"

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
        md_bg_color: 1, 0.01, 0.01, 0.8  # Couleur rouge clair (RGBA)
        #rgba(81, 4, 80, 0.8)

        FloatLayout:
            MDLabel:
                text: 'ECRAN2'
                halign: "center"
                pos_hint: {"center_y": .95}  # Remonter le texte vers le haut

            FloatLayout:
                ScrollView:
                    siwidth: root.width
                    size_hint_y: None
                    height: root.height-60
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
                            md_bg_color: 0.1, 0.6, 0.8, 1 #couleur de fond : bleu clair
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

            BoxLayout:
                id: box3
                size_hint_y: .8
                pos_hint: {"center_y": .5}  # Remonter la table
                #pos_hint: {"top": 1}

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
                on_release: root.manager.current = "DEMO4"

<DEMO4>:
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.9, 0.9, 0.1, 0.8  # Couleur vert clair (RGBA)

        FloatLayout:
            MDLabel:
                text: 'ECRAN4'
                halign: "center"
                pos_hint: {"center_y": .95}  # Remonter le texte vers le haut

            BoxLayout:
                id: box4
                size_hint_y: .8
                pos_hint: {"center_y": .5}  # Remonter la table
                #pos_hint: {"top": 1}

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
                on_release: root.manager.current = "DEMO5"

<DEMO5>:
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.9, 0.1, 0.9, 0.8  # Couleur vert clair (RGBA)

        FloatLayout:
            MDLabel:
                text: 'ECRAN5'
                halign: "center"
                pos_hint: {"center_y": .95}  # Remonter le texte vers le haut

            BoxLayout:
                id: box5
                size_hint_y: .8
                pos_hint: {"center_y": .5}  # Remonter la table
                #pos_hint: {"top": 1}

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
                on_release: root.manager.current = "DEMO4"

            MDRaisedButton:
                text: "Ecran suivant"
                size_hint_x: 0.4
                md_bg_color: 0, 0, 0.5, 1  # Bleu foncé (RGBA)
                text_color: 1, 1, 1, 1  # Blanc
                font_name: "Roboto-Bold"  # Police en gras
                on_release: root.manager.current = "DEMO6"

<DEMO6>:
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.9, 0.1, 0.9, 0.8  # Couleur vert clair (RGBA)

        FloatLayout:
            MDLabel:
                text: 'ECRAN6'
                halign: "center"
                pos_hint: {"center_y": .95}  # Remonter le texte vers le haut

            BoxLayout:
                id: box6
                size_hint_y: .8
                pos_hint: {"center_y": .5}  # Remonter la table
                #pos_hint: {"top": 1}

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
                on_release: root.manager.current = "DEMO5"

            MDRaisedButton:
                text: "Ecran suivant"
                size_hint_x: 0.4
                md_bg_color: 0, 0, 0.5, 1  # Bleu foncé (RGBA)
                text_color: 1, 1, 1, 1  # Blanc
                font_name: "Roboto-Bold"  # Police en gras
                on_release: root.manager.current = "DEMO7"

<DEMO7>:
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.9, 0.1, 0.9, 0.8  # Couleur vert clair (RGBA)

        FloatLayout:
            MDLabel:
                text: 'ECRAN7'
                halign: "center"
                pos_hint: {"center_y": .95}  # Remonter le texte vers le haut

            BoxLayout:
                id: box7
                size_hint_y: .8
                pos_hint: {"center_y": .5}  # Remonter la table
                #pos_hint: {"top": 1}

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
                on_release: root.manager.current = "DEMO6"

            MDRaisedButton:
                text: "Ecran suivant"
                size_hint_x: 0.4
                md_bg_color: 0, 0, 0.5, 1  # Bleu foncé (RGBA)
                text_color: 1, 1, 1, 1  # Blanc
                font_name: "Roboto-Bold"  # Police en gras
                on_release: root.manager.current = "DEMO8"

<DEMO8>:
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.9, 0.1, 0.9, 0.8  # Couleur vert clair (RGBA)

        FloatLayout:
            MDLabel:
                text: 'ECRAN8'
                halign: "center"
                pos_hint: {"center_y": .95}  # Remonter le texte vers le haut

            BoxLayout:
                id: box8
                size_hint_y: .8
                pos_hint: {"center_y": .5}  # Remonter la table
                #pos_hint: {"top": 1}

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
                on_release: root.manager.current = "DEMO7"

            MDRaisedButton:
                text: "Ecran suivant"
                size_hint_x: 0.4
                md_bg_color: 0, 0, 0.5, 1  # Bleu foncé (RGBA)
                text_color: 1, 1, 1, 1  # Blanc
                font_name: "Roboto-Bold"  # Police en gras
                on_release: root.manager.current = "DEMO9"

<DEMO9>:
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.9, 0.1, 0.9, 0.8  # Couleur vert clair (RGBA)

        FloatLayout:
            MDLabel:
                text: 'ECRAN9'
                halign: "center"
                pos_hint: {"center_y": .95}  # Remonter le texte vers le haut

            BoxLayout:
                id: box9
                size_hint_y: .8
                pos_hint: {"center_y": .5}  # Remonter la table
                #pos_hint: {"top": 1}

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
                on_release: root.manager.current = "DEMO8"

            MDRaisedButton:
                text: "Ecran suivant"
                size_hint_x: 0.4
                md_bg_color: 0, 0, 0.5, 1  # Bleu foncé (RGBA)
                text_color: 1, 1, 1, 1  # Blanc
                font_name: "Roboto-Bold"  # Police en gras
                on_release: root.manager.current = "DEMO10"


<DEMO10>:
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.9, 0.1, 0.9, 0.8  # Couleur vert clair (RGBA)

        FloatLayout:
            MDLabel:
                text: 'ECRAN10'
                halign: "center"
                pos_hint: {"center_y": .95}  # Remonter le texte vers le haut

            BoxLayout:
                id: box10
                size_hint_y: .8
                pos_hint: {"center_y": .5}  # Remonter la table
                #pos_hint: {"top": 1}

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
                on_release: root.manager.current = "DEMO9"

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

        # Regrouper par 'pl_name' et garder les valeurs maximales pour les autres colonnes
        # aggregated_data = {}
        # for row in data_pllist:
        #     pl_name = row['pl_name']
        #     if pl_name not in aggregated_data:
        #         aggregated_data[pl_name] = row
        #     else:
        #         for key in row:
        #             if key != 'pl_name' and row[key] is not None:
        #                 # Conserver la valeur maximale pour les autres colonnes
        #                 aggregated_data[pl_name][key] = max(aggregated_data[pl_name][key], row[key]) if aggregated_data[pl_name][key] is not None else row[key]

        # # Convertir en une liste de tuples pour MDDataTable
        # data_table = [
        #     (row['pl_name'], row['disc_year'], row['sy_dist'], row['discoverymethod'], row['pl_bmasse'], row['pl_rade'])
        #     for row in aggregated_data.values()
        # ]

        self.ids.label_ecran1.text = f"Nb exoplanètes à ce jour {version} : [color=ff0000][b][size=80]{nb_exoplanets}[/size][/b][/color] "  # Mettre à jour le texte de l'étiquette
        # Define Table
        self.table = MDDataTable(
            use_pagination=True,
            pos_hint={'center_x': 0.5, 'center_y': 0.5},  # Centrer la table
            size_hint=(0.9, None),  # Largeur fixe et hauteur dynamique
            height=dp(8 * 48 + 56),  # 5 lignes * 48dp + 56dp pour l'en-tête
            check=True,

            column_data=[
                ("pl_name", dp(30),self.sort_on_pl_name),
                ("disc_year", dp(30)),
                ("sy_dist", dp(30)),
                ("discoverymethod", dp(30)),
                ("pl_bmasse", dp(30)),
                ("pl_rade", dp(30))
            ],
            row_data=data_table_tuple,
            sorted_on="pl_name",
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

    def sort_on_pl_name(self, data):
        """    Fonction de tri personnalisée pour la colonne PL_NAME.    """
        # Trier les données par la 3ème colonne (index 2)
        sorted_data = sorted(data, key=lambda row: row[2])  
        # Extraire les indices et les données triées
        sorted_indices = [i for i in range(len(sorted_data))]
        return sorted_indices, sorted_data
    
class DEMO2(Screen):
    def on_enter(self, *args):
        # Filtrer les planètes avec une distance valide (non None)
        valid_planets = [planet for planet in data_table_dict if planet.get('sy_dist') is not None]
        
        # Trier les planètes par distance
        sorted_planets = sorted(valid_planets, key=lambda x: x['sy_dist'])
        
        # Sélectionner les 10 plus proches
        closest_planets = sorted_planets[:10]
        # Liste des IDs des cartes
        card_ids = [
            'cart1_text', 'cart2_text', 'cart3_text', 'cart4_text', 'cart5_text',
            'cart6_text', 'cart7_text', 'cart8_text', 'cart9_text', 'cart10_text'
        ]

        # Mettre à jour les cartes avec les données des planètes
        for i, planet in enumerate(closest_planets):
            pl_name = planet.get('pl_name', 'Unknown')
            sy_dist = planet.get('sy_dist', 'Unknown')
            pl_rade = planet.get('pl_rade', 'Unknown')
            pl_bmasse = planet.get('pl_bmasse', 'Unknown')
            discoverymethod = planet.get('discoverymethod', 'Unknown')
            # Mettre à jour le texte de la carte
            self.ids[card_ids[i]].text = f"Nom: {pl_name}\nDistance: {sy_dist:.2f} Parsecs\nRayon: {str(pl_rade)} Kms\nMasse: {str(pl_bmasse)} Terre\nMethode: {discoverymethod}"

class DEMO3(Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)
        
        box = self.ids.box3
        # box.add_widget(FigureCanvasKivyAgg(plt.figure(3)))
        
    # def save_it(self):
    #     name = self.ids.namer.text
    #     if name:
    #         plt.savefig(name)

class DEMO4(Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)
        
        box = self.ids.box4
        # box.add_widget(FigureCanvasKivyAgg(plt.figure(4)))
        
    # def save_it(self):
    #     name = self.ids.namer.text
    #     if name:
    #         plt.savefig(name)

class DEMO5(Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)
        
        box = self.ids.box5
        # box.add_widget(FigureCanvasKivyAgg(plt.figure(5)))
        
    # def save_it(self):
    #     name = self.ids.namer.text
    #     if name:
    #         plt.savefig(name)

class DEMO6(Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)
        
        box = self.ids.box6
        # box.add_widget(FigureCanvasKivyAgg(plt.figure(5)))
        
    # def save_it(self):
    #     name = self.ids.namer.text
    #     if name:
    #         plt.savefig(name)

class DEMO7(Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)
        
        box = self.ids.box7
        # box.add_widget(FigureCanvasKivyAgg(plt.figure(5)))
        
    # def save_it(self):
    #     name = self.ids.namer.text
    #     if name:
    #         plt.savefig(name)

class DEMO8(Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)
        
        box = self.ids.box8
        # box.add_widget(FigureCanvasKivyAgg(plt.figure(5)))
        
    # def save_it(self):
    #     name = self.ids.namer.text
    #     if name:
    #         plt.savefig(name)

class DEMO9(Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)
        
        box = self.ids.box9
        # box.add_widget(FigureCanvasKivyAgg(plt.figure(5)))
        
    # def save_it(self):
    #     name = self.ids.namer.text
    #     if name:
    #         plt.savefig(name)

class DEMO10(Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)
        
        box = self.ids.box10
        # box.add_widget(FigureCanvasKivyAgg(plt.figure(5)))
        
    # def save_it(self):
    #     name = self.ids.namer.text
    #     if name:
    #         plt.savefig(name)


class Main(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        #self.icon = "imagesatellite1.png"
        Builder.load_string(KV)

        sm = ScreenManager()
        sm.add_widget(DEMO1(name="DEMO1"))
        sm.add_widget(DEMO2(name="DEMO2"))
        sm.add_widget(DEMO3(name="DEMO3"))
        sm.add_widget(DEMO4(name="DEMO4"))
        sm.add_widget(DEMO5(name="DEMO5"))
        sm.add_widget(DEMO6(name="DEMO6"))
        sm.add_widget(DEMO7(name="DEMO7"))
        sm.add_widget(DEMO8(name="DEMO8"))
        sm.add_widget(DEMO9(name="DEMO9"))
        sm.add_widget(DEMO10(name="DEMO10"))

        return sm

Main().run()