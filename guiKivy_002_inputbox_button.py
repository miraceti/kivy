import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    #initialize infinite keywords
    def __init__(self, **kwargs):
        #call the grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)
        
        #set the columns
        self.cols = 2
        
        #Add widget 
        self.add_widget(Label(text="Name : "))
        #Add input box
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)
        
        #Add widget 
        self.add_widget(Label(text="Favorite Pizza : "))
        #Add input box
        self.pizza = TextInput(multiline=False)
        self.add_widget(self.pizza)
        
        #Add widget label
        self.add_widget(Label(text="Favorite color : "))
        #Add input box
        self.color = TextInput(multiline=False)
        self.add_widget(self.color)
        
        #create the submit button
        self.submit = Button(text ="Submit", font_size=32)
        #bind button
        self.submit.bind(on_press = self.press)
        self.add_widget(self.submit)
        
    def press(self,instance):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text
        
        # print(f'Hello {name}, you like {pizza} pizza and your favorite color is {color}!')
        #print to the scree
        self.add_widget(Label(text=f'Hello {name}, you like {pizza} pizza and your favorite color is {color}!'))
        
        # clear the input boxes after click
        self.name.text=""
        self.pizza.text=""
        self.color.text=""
        
        

class MyApp(App):
    def build(self):
        # return Label(text="hello My World !", font_size=72)
        return MyGridLayout()
    

if __name__ == '__main__':
    MyApp().run()