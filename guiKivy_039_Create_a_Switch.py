from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

# define our kv design file
Builder.load_file('kivy039.kv')#methode 1 prefered"

class MyLayout(Widget):
    def switch_click(self, switchObject, switchValue):
        print(switchValue)
        print(switchObject)
        if (switchValue):
            self.ids.my_label.text = "You clicked the switch On! "
        else:
            self.ids.my_label.text = "You clicked the switch Off! "
            # self.ids.my_switch.disabled = True
            
class AwesomeApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    AwesomeApp().run()