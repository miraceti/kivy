from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.vkeyboard import VKeyboard
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        
        # define our layout
        layout = GridLayout(cols=1) 
        
        # define our VKeyboard
        keyboard = VKeyboard(on_key_up = self.key_up)
        
        self.label = Label(text="Type something!", font_size="20sp")
        
        layout.add_widget(self.label)
        layout.add_widget(keyboard)
        
        return layout
        
    def key_up(self, keyboard, keycode, *args):
        if isinstance(keycode, tuple):
            print(keycode)
            keycode = keycode[1]
                       
        # track what already in the label
        thing = self.label.text   
        
        # run some logics
        if thing == "Type something!":
            thing = ""
            
        # backspace
        if keycode =='backspace':
            thing = thing[:-1]
            keycode = ''
            
        # spacebar
        if keycode =='spacebar':
            keycode = " "
        
        # update label        #  
        self.label.text = f'{thing}{keycode}'
            

MainApp().run()
 
