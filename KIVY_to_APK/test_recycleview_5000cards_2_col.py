from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.uix.recycleview import RecycleView
from kivy.uix.recyclegridlayout import RecycleGridLayout
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
    RecycleView:
        viewclass: 'MyCard'
        data: app.data
        RecycleGridLayout:
            cols: 2
            default_size: None, dp(100)
            default_size_hint: 1, None
            size_hint_y: None
            height: self.minimum_height
            spacing: dp(10)
'''

class MyCard(MDCard):
    text = StringProperty("")
    bg_color = ListProperty([1, 1, 1, 1])

class MainScreen(RecycleView):
    pass

class MyApp(MDApp):
    data = ListProperty()

    def build(self):
        # Charger le fichier KV et retourner l'instance de MainScreen
        Builder.load_string(KV)
        return MainScreen()

    def on_start(self):
        # Exemple de liste de dictionnaires avec des noms et des couleurs
        self.data = [
            {'text': f'Person {i}', 'bg_color': [0.5, 0.2, 0.8, 1] if i % 2 == 0 else [0.2, 0.8, 0.5, 1]}
            for i in range(6000)
        ]

if __name__ == '__main__':
    MyApp().run()
