from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window


Builder.load_file('update_label.kv')#methode 1 prefered"

class MyLayout(Widget):
    def press(self):
        #create variables
        name = self.ids.name_input.text
        print(name)
        #update the label
        self.ids.name_label.text = f'Hello {name} !'
        
        #clear input box
        self.ids.name_input.text = ""
        

class AwesomeApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    AwesomeApp().run()