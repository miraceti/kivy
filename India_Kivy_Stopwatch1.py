from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.clock import Clock

from time import strftime

#set the size of the app
Window.size = (500, 700)

Builder.load_file('stopwatch.kv')#methode 1 prefered"
            
class StopWatchApp(App):
    sw_seconds = 0
    sw_started = False
    
    def update_time(self, nap):
        if self.sw_started:
            self.sw_seconds += nap
            
        minutes, seconds = divmod(self.sw_seconds, 60)
        part_seconds = seconds*100%100
        
        self.root.ids.stopwatch.text= f'{int(minutes):02}:{int(seconds):02}.[size=40]{int(part_seconds):02}[/size]'
        
        self.root.ids.time.text = strftime('[b]%H[/b]:%M:%S')
    
    def on_start(self):
        Clock.schedule_interval(self.update_time,0)
        
    def start_stop(self):
        self.root.ids.start_stop.text= 'start' if self.sw_started else 'stop'
        
        self.sw_started = not self.sw_started
        
    def reset(self):
        if self.sw_started:
            self.root.ids.start_stop.text= 'start'
            self.sw_started= False 
            
        self.sw_seconds = 0
            
        
if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#4b5162')
    StopWatchApp().run()