from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.uix.recycleview import RecycleView
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, ListProperty
from kivy.uix.image import Image
import matplotlib.pyplot as plt
import io
from PIL import Image as PILImage

KV = '''
<MyCard@MDCard>:
    size_hint: None, None
    size: "200dp", "100dp"
    padding: "10dp"
    md_bg_color: root.bg_color
    MDLabel:
        text: root.text
        halign: "center"

<CardScreen>:
    name: 'card'
    BoxLayout:
        orientation: 'vertical'
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
        BoxLayout:
            size_hint_y: None
            height: "50dp"
            MDFloatingActionButton:
                icon: "arrow-left"
                on_release: app.root.current = 'graph'
            MDFloatingActionButton:
                icon: "arrow-right"
                on_release: app.root.current = 'card'

<GraphScreen>:
    name: 'graph'
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Graph Page"
            md_bg_color: app.theme_cls.primary_color
        BoxLayout:
            padding: "10dp"
            Image:
                id: graph
                source: ''
        BoxLayout:
            size_hint_y: None
            height: "50dp"
            MDFloatingActionButton:
                icon: "arrow-left"
                on_release: app.root.current = 'graph'
            MDFloatingActionButton:
                icon: "arrow-right"
                on_release: app.root.current = 'card'

<MainScreenManager>:
    CardScreen:
    GraphScreen:
'''

class MyCard(MDCard):
    text = StringProperty("")
    bg_color = ListProperty([1, 1, 1, 1])

class CardScreen(Screen):
    pass

class GraphScreen(Screen):
    pass

class MainScreenManager(ScreenManager):
    pass

class MyApp(MDApp):
    data = ListProperty()

    def build(self):
        Builder.load_string(KV)
        return MainScreenManager()

    def on_start(self):
        # Exemple de liste de dictionnaires avec des noms et des couleurs
        self.data = [
            {'text': f'Person {i}', 'bg_color': [0.5, 0.2, 0.8, 1] if i % 2 == 0 else [0.2, 0.8, 0.5, 1]}
            for i in range(6000)
        ]

        # Tracer le graphique sinus et l'afficher en tant qu'image
        self.plot_sinus_graph()

    def plot_sinus_graph(self):
        import numpy as np

        # Créer un graphique sinus
        fig, ax = plt.subplots()
        x = np.linspace(0, 2 * np.pi, 100)
        y = np.sin(x)
        ax.plot(x, y)
        ax.set_title('Sinus Graph')

        # Enregistrer le graphique dans un objet BytesIO
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)

        # Charger l'image avec PIL et l'afficher dans le widget Image
        pil_image = PILImage.open(buf)
        pil_image.save('graph.png')  # Sauvegarder l'image temporairement

        # Afficher l'image dans le widget Image
        graph_screen = self.root.get_screen('graph')
        graph_widget = graph_screen.ids.graph
        graph_widget.source = 'graph.png'
        graph_widget.reload()

if __name__ == '__main__':
    MyApp().run()
