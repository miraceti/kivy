from kivy.app import App 
from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen 
# Create both screens. Please note the root.manager.current: this is how # you can control the ScreenManager from kv. Each screen has by default a # property manager that gives you the instance of the ScreenManager used. 
Builder.load_string("""
<MenuScreen>:     
    BoxLayout:         
        Button:             
            text: 'First Button on Menu'             
            on_press: root.manager.current = 'settings'         
        Button:             
            text: 'Second Button on Menu' 
            
<SettingsScreen>:     
    BoxLayout:         
        Button:             
            text: 'First Button on Settings'             
            on_press: root.manager.current = 'menu'         
        Button:             
            text: 'Second Button on Settings' 
                    """) 
# Declare both screens 
class MenuScreen(Screen):     
    pass 
class SettingsScreen(Screen):     
    pass 
# Create the screen manager 
sm = ScreenManager() 
sm.add_widget(MenuScreen(name='menu')) 
sm.add_widget(SettingsScreen(name='settings'))
    
    
class TestApp(App):     
    def build(self):         
        return sm 
    
if __name__ == '__main__':     
    TestApp().run()