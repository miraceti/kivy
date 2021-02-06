from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class NoobWidget(BoxLayout):
    def updateText(self):
        self.ids.clicked.text="Has been clicked!"

class NoobApp(App):
    def build(self):
        return NoobWidget()
    
if __name__ == "__main__":
    NoobApp().run()