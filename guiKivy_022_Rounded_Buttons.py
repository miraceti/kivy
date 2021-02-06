from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

#set the size of the app
Window.size = (500, 700)

Builder.load_file('kivy022.kv')#methode 1 prefered"

class MyLayout(Widget):
    pass
         

class AwesomeApp(App):
    def build(self):
        Window.clearcolor= (1,1,1,1)
        return MyLayout()
    
if __name__ == '__main__':
    AwesomeApp().run()