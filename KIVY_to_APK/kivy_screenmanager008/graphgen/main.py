import matplotlib

from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.utils import get_color_from_hex

from kivy_garden.matplotlib import FigureCanvasKivy, NavigationToolbar2Kivy, FigureCanvasKivyAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from kivy.properties import NumericProperty

Builder.load_file("layout.kv")


fig, ax = plt.subplots()

canvas = fig.canvas

import numpy as np
from numpy import sin,cos,tan

class Home(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # self.bx = self.ids.bx
        # self.nav = NavigationToolbar2Kivy(canvas)
        
        # self.bx.add_widget(self.nav.actionbar)
        # self.bx.add_widget(canvas)
        # self.w_action_bar = self.nav.actionbar = ActionBar(pos_hint={'top': 1.0}, background_color = get_color_from_hex('#F05F40'))
        
    
    def gnrt_graph(self):
        try:
            self.fn = self.ids.fn
            self.first_value_of_x = self.ids.first_value
            self.final_value_of_x = self.ids.final_value
            self.nmbr_parts = self.ids.nmbrs_parts

            first_value = int(self.first_value_of_x.text)
            final_value = int(self.final_value_of_x.text)
            nmbr_parts = int(self.nmbr_parts.text)

            print(first_value, final_value, nmbr_parts)

            x = np.linspace(first_value, final_value, nmbr_parts)
            y = eval(self.fn.text)
            
            print(y)

            plt.plot(x, y)
            plt.grid()
            # fig, ax = plt.subplots()
            canvas = FigureCanvasKivyAgg(plt.gcf())
            self.bx = self.ids.bx
            self.nav = NavigationToolbar2Kivy(canvas)
            
            self.bx.add_widget(self.nav.actionbar)
            self.bx.add_widget(canvas)
        except Exception:
            pass
        
class Main(MDApp):
    def build(self):
        # sm =  ScreenManager()
        # sm.add_widget(EquationScreen(name = "eqn"))
        # sm.add_widget(GraphScreen(name = "graph"))
        self.icon = "/home/sharif/Desktop/Projects/graph_calculator/icon.png"
        return Home()


if __name__ == "__main__":
    Main().run()