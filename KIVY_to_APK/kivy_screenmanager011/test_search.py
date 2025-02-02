from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

KV = """
BoxLayout:
    orientation: "vertical"

    # Barre du haut
    BoxLayout:
        size_hint_y: 0.1
        Button:
            text: "Menu"
        
        Label:
            text: "Titre de l'App"
            color: 1, 1, 1, 1
            canvas.before:
                Color:
                    rgba: 0, 1, 1, 1  # Fond rouge clair
                Rectangle:
                    pos: self.pos
                    size: self.size

        Button:
            text: "Profil"

    # ScrollView contenant la liste des enregistrements
    ScrollView:
        size_hint_y: 0.7
        GridLayout:
            id: record_list
            cols: 1
            size_hint_y: None
            height: self.minimum_height  # Ajuste la hauteur automatiquement

    # Barre du bas avec la recherche
    BoxLayout:
        size_hint_y: 0.2
        TextInput:
            id: search_input
            hint_text: "Rechercher..."
            size_hint_x: 0.8
            multiline: False
            on_text: app.filter_records(self.text)  # Filtrer en temps réel
        Button:
            text: "🔍"
            size_hint_x: 0.2
            on_press: app.filter_records(search_input.text)  # Filtrer au clic
"""

class MyApp(App):
    def build(self):
        self.root = Builder.load_string(KV)

        # Liste complète des enregistrements (simulée)
        self.all_records = [
            "Alice - 01","Bob - 02","Charlie - 03","David - 04","Emma - 05","Fiona - 06","George - 07","Hannah - 08","Ian - 09","Jack - 10",
            "Alice - 01","Bob - 02","Charlie - 03","David - 04","Emma - 05","Fiona - 06","George - 07","Hannah - 08","Ian - 09","Jack - 10",
            "Alice - 01","Bob - 02","Charlie - 03","David - 04","Emma - 05","Fiona - 06","George - 07","Hannah - 08","Ian - 09","Jack - 10",
            "Alice - 01","Bob - 02","Charlie - 03","David - 04","Emma - 05","Fiona - 06","George - 07","Hannah - 08","Ian - 09","Jack - 10",
        ]

        # Afficher la liste au démarrage
        self.filter_records("")

        return self.root

    def filter_records(self, query):
        """Filtre les enregistrements et les affiche dans le ScrollView"""
        record_list = self.root.ids.record_list
        record_list.clear_widgets()  # Efface les anciens résultats

        # Filtrage des enregistrements (insensible à la casse)
        filtered = [r for r in self.all_records if query.lower() in r.lower()]

        # Si aucun résultat, afficher "Aucun résultat trouvé"
        if not filtered:
            record_list.add_widget(
                Label(
                    text="Aucun résultat trouvé",
                    size_hint_y=None,
                    height=40,
                    color=(1, 0, 0, 1),  # Rouge
                    bold=True
                )
            )
            return

        # Ajouter les résultats filtrés sous forme de boutons cliquables
        for record in filtered:
            btn = Button(
                text=record,
                size_hint_y=None,
                height=50,
                on_press=self.on_record_selected  # Appel de la fonction quand on clique
            )
            record_list.add_widget(btn)

    def on_record_selected(self, instance):
        """Action lorsqu'un enregistrement est cliqué"""
        print(f"Enregistrement sélectionné : {instance.text}")  # Affichage console
        # Tu peux ici ouvrir un détail, afficher une popup, etc.

if __name__ == "__main__":
    MyApp().run()
