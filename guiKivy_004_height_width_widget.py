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
        self.cols = 1
        
        self.row_force_default=True
        self.row_default_height = 120
        self.col_force_default= True
        self.col_default_width = 100
        
        #create a second grid layout
        self.top_grid = GridLayout(
            row_force_default=True, 
            row_default_height = 40,
            col_force_default= True,
            col_default_width = 100
            )
        self.top_grid.cols = 2
        
        
        
        
        #Add widget 
        self.top_grid.add_widget(Label(text="Name : "))
        #Add input box
        self.name = TextInput(multiline=True)
        self.top_grid.add_widget(self.name)
        
        #Add widget 
        self.top_grid.add_widget(Label(text="Favorite Pizza : "))
        #Add input box
        self.pizza = TextInput(multiline=False)
        self.top_grid.add_widget(self.pizza)
        
        #Add widget label
        self.top_grid.add_widget(Label(text="Favorite color : "))
        #Add input box
        self.color = TextInput(multiline=False)
        self.top_grid.add_widget(self.color)
        
        #add the new top_grid to our app
        self.add_widget(self.top_grid)
        
        
        #create the submit button
        self.submit = Button(text ="Submit",
                             font_size=32,
                             size_hint_y = None,
                             height = 50,
                             size_hint_x = None,
                             width = 200
                             )
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