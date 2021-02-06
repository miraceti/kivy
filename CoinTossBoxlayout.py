from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

# Builder.load_file('cointoss.kv')#methode 1 prefered"

class CoinTossBoxLayout(BoxLayout):
    def choice(self, guess):
        output = "you clicked the " + guess + " button!"
        self.ids.result.text = output
        
class CoinTossApp(App):
    def build(self):
        return CoinTossBoxLayout()
    
if __name__ == "__main__":
    CoinTossApp().run()