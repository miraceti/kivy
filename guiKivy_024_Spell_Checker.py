from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.spelling import Spelling

Builder.load_file('kivy024.kv')#methode 1 prefered"

class MyLayout(Widget):
    def press(self):
        #creation d'une instance de Spelling
        s = Spelling()
        
        #select a language
        s.select_language('en_US')
        
        #pour voir les options de language
        print(s.list_languages())
        
        #grab word from textbox
        word = self.ids.word_input.text
        
        options = s.suggest(word)
        
        x = ""
        for item in options:
            x = f'{x} {item}'
        
        #update the label
        self.ids.word_label.text = f'{x}'#f'Suggestions : {options}' # str(option)
         
class AwesomeApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    AwesomeApp().run()