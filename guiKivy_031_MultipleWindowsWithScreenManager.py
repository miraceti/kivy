from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# define different screens
class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

# define our kv design file
kv = Builder.load_file('kivy031.kv')#methode 1 prefered"

class AwesomeApp(App):
    def build(self):
        return kv
    
if __name__ == '__main__':
    AwesomeApp().run()