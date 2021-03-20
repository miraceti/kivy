from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

# define our kv design file
Builder.load_file('kivy039.kv')#methode 1 prefered"

class MyLayout(Widget):
    pass
            
class AwesomeApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    AwesomeApp().run()