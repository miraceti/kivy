from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
# from kivy.uix.slider import Slider

Builder.load_file('kivy026.kv')#methode 1 prefered"

class MyLayout(Widget):
    pass
         
class AwesomeApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    AwesomeApp().run()