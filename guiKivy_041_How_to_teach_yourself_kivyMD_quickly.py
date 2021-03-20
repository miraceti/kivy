from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.card import MDCardSwipe


# define our kv design file
Builder.load_file('kivy041.kv')#methode 1 prefered"

class MyLayout(Widget):
    pass
            
class AwesomeApp(MDApp):
    def build(self):
        return MyLayout()

    
if __name__ == '__main__':
    AwesomeApp().run()