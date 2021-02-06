from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder


Builder.load_file('kivy028.kv')#methode 1 prefered"

class MyLayout(Widget):
    checks=[]
    def checkbox_click(self, instance, value, topping):
        print(instance)
        if value == True:
            MyLayout.checks.append(topping)
            tops = ''
            for x in MyLayout.checks:
                tops = f'{tops} {x}'
            self.ids.output_label.text=f'tu as choisis :{tops}'
        else:
            MyLayout.checks.remove(topping)
            tops = ''
            for x in MyLayout.checks:
                tops = f'{tops} {x}'
            self.ids.output_label.text=f'tu as choisis :{tops}'
         
class AwesomeApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    AwesomeApp().run()