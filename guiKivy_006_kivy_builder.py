import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('whatever.kv')#methode 1 prefered"
# Builder.load_string(""" coller le fichier kv               """) #methode 2

class MyGridLayout(Widget):

    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)

   
    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text
        
        # print(f'Hello {name}, you like {pizza} pizza and your favorite color is {color}!')
        #print to the scree
        # self.add_widget(Label(text=f'Hello {name}, you like {pizza} pizza and your favorite color is {color}!'))
        print(f'Hello {name}, you like {pizza} pizza and your favorite color is {color}!')
        
        # clear the input boxes after click
        self.name.text=""
        self.pizza.text=""
        self.color.text=""

class AwesomeApp(App):
    def build(self):
        # return Label(text="hello My World !", font_size=72)
        return MyGridLayout()
    

if __name__ == '__main__':
    AwesomeApp().run()