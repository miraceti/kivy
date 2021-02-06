from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

#set the size of the app
Window.size = (500, 700)


Builder.load_file('kivy016.kv')#methode 1 prefered"

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text="0"
        
    def button_press(self, button):
        #creation d'une variable qui contient la valeur de la zone texte
        prior = self.ids.calc_input.text
        
        #check si 0 est present
        if prior == "0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'
            
    #creation de la fonction d'addition
    def add(self):
        #creation d'une variable qui contient la valeur de la zone texte
        prior = self.ids.calc_input.text
        #ajouter le signe + a la textbox
        self.ids.calc_input.text = f'{prior}+'
       
    #creation de la fonction de soustraction
    def subtract(self):
        #creation d'une variable qui contient la valeur de la zone texte
        prior = self.ids.calc_input.text
        #ajouter le signe + a la textbox
        self.ids.calc_input.text = f'{prior}-'

    #creation de la fonction de multiplication
    def multiply(self):
        #creation d'une variable qui contient la valeur de la zone texte
        prior = self.ids.calc_input.text
        #ajouter le signe + a la textbox
        self.ids.calc_input.text = f'{prior}*'
        
    #creation de la fonction de division
    def divide(self):
        #creation d'une variable qui contient la valeur de la zone texte
        prior = self.ids.calc_input.text
        #ajouter le signe + a la textbox
        self.ids.calc_input.text = f'{prior}/'
    
    #creation de la fonction de calcul    
    def equals(self):
        #creation d'une variable qui contient la valeur de la zone texte
        prior = self.ids.calc_input.text
        
        #addition
        if "+" in prior:
            num_list = prior.split("+")
            answer = 0
            #on boucle sur la liste des nombre
            for number in num_list:
                answer = answer + int(number)
            #print the answer in the textbox
            self.ids.calc_input.text = str(answer)
        
class CalculatorApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    CalculatorApp().run()