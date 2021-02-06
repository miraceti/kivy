from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.animation import Animation

# define our kv design file
Builder.load_file('kivy036.kv')#methode 1 prefered"

class MyLayout(Widget):
    def animate_it(self, widget, *args):
        #define animation
        animate = Animation(background_color=(0, 0, 1, 1),
                            duration = 1,
                            # opacity = 0
                            )
        #do 2nd animation
        # animate += Animation(opacity=0, duration= .5) 
        animate += Animation(size_hint = (1,1)) 
        animate += Animation(size_hint = (.5,.5)) 
        animate += Animation(pos_hint = {"center_x" : 0.1}) 
        animate += Animation(pos_hint = {"center_x" : 0.5}) 
        
        animate.start(widget)
        
        #create a calllback
        animate.bind(on_complete = self.my_callback)
        
    def my_callback(self, *args):
        self.ids.my_label.text = " Wow! Look At That!"

class AwesomeApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    AwesomeApp().run()