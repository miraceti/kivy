from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

#set the size of the app
# Window.size = (500, 700)


Builder.load_file('kivy015.kv')#methode 1 prefered"

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text="0"
        
class CalculatorApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    CalculatorApp().run()