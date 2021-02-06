from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

# define our kv design file
Builder.load_file('kivy032.kv')#methode 1 prefered"

class MyLayout(Widget):
    def spinner_clicked(self, value):
        self.ids.click_label.text = f'you Selected : {value}'

class AwesomeApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    AwesomeApp().run()