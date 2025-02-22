from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty

KV = '''
<MyCard@MDCard>:
    size_hint: None, None
    size: "200dp", "100dp"
    padding: "10dp"
    md_bg_color: root.bg_color
    MDLabel:
        text: root.text
        halign: "center"

<MainScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: "10dp"
        spacing: "10dp"
        ScrollView:
            GridLayout:
                id: grid
                cols: 1
                size_hint_y: None
                height: self.minimum_height
                row_default_height: '100dp'
                row_force_default: True
'''

class MyCard(MDCard):
    text = StringProperty("")
    bg_color = ListProperty([1, 1, 1, 1])

class MainScreen(BoxLayout):
    pass

class MyApp(MDApp):
    def build(self):
        # Charger le fichier KV et retourner l'instance de MainScreen
        Builder.load_string(KV)
        return MainScreen()

    def on_start(self):
        # Exemple simple de liste de dictionnaires avec des noms et des couleurs
        data = [
            {'text': f'Person {i}', 'bg_color': [0.5, 0.2, 0.8, 1] if i % 2 == 0 else [0.2, 0.8, 0.5, 1]}
            for i in range(10)
        ]

        # Accéder au GridLayout via self.root
        grid = self.root.ids.grid
        for item in data:
            card = MyCard(text=item['text'], bg_color=item['bg_color'])
            grid.add_widget(card)

if __name__ == '__main__':
    MyApp().run()
