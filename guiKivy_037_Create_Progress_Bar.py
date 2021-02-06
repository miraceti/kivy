from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

# define our kv design file
Builder.load_file('kivy037.kv')#methode 1 prefered"

class MyLayout(Widget):
    def press_it(self):
        current = self.ids.my_progress_bar.value
        if current == 1:
            current = 0
            self.ids.my_progress_bar.value = current
            self.ids.my_label.text = f'{int(current*100)}% Progress'
        else:
            current += .25
            self.ids.my_progress_bar.value = current
            self.ids.my_label.text = f'{int(current*100)}% Progress'

class AwesomeApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    AwesomeApp().run()