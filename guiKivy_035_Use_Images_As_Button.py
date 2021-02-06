from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

# define our kv design file
Builder.load_file('kivy035.kv')#methode 1 prefered"

class MyLayout(Widget):
    def hello_on(self):
        self.ids.my_label.text="You press the button"
        self.ids.my_image.source = 'images/login_pressed.png'
        
    def hello_off(self):
        self.ids.my_label.text="Hello World!"
        self.ids.my_image.source = 'images/login.png'

class AwesomeApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    AwesomeApp().run()