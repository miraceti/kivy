from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout

from kivy_garden.matplotlib import FigureCanvasKivyAgg

import matplotlib.pyplot as plt
# define what we want to graph
x = [1,2,3,4,5]
y = [5,12,6,9,15]

plt.plot(x,y)
plt.ylabel("Y axes")
plt.xlabel("X axes")

KV='''
<Matty>
    BoxLayout:
        id: box
        size_hint_y: .8
        pos_hint: {"top": 1}
        
    BoxLayout:
        size_hint_y: .2
        TextInput:
            id: namer
            multiline: False

        Button:
            text: "Save It!"
            on_release: root.save_it()
'''
class Matty(FloatLayout):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)
        
        box = self.ids.box
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        
    def save_it(self):
        name = self.ids.namer.text
        if name:
            plt.savefig(name)
            

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style= "Dark"
        self.theme_cls.primary_palette = "BlueGray"
               
        Builder.load_string(KV)
        
        return Matty()
      
          
MainApp().run()