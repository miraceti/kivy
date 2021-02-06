from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

#set the size of the app
Window.size = (500, 700)


Builder.load_file('kivy020.kv')#methode 1 prefered"

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text="0"
        
    def button_press(self, button):
        #creation d'une variable qui contient la valeur de la zone texte
        prior = self.ids.calc_input.text
        
        #test erreur en premier
        if "Erreur" in prior:
            prior = ''
        
        #check si 0 est present
        if prior == "0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'
    
    #creation de la fonction de suppression du dernier chiffre
    def remove(self):
        #creation d'une variable qui contient la valeur de la zone texte
        prior = self.ids.calc_input.text
        #suppression du dernier caractere de prior
        prior = prior[:-1]
        self.ids.calc_input.text = prior
    
    
    #signe positif ou negatif
    def pos_neg(self):
        #creation d'une variable qui contient la valeur de la zone texte
        prior = self.ids.calc_input.text
        #check du signe moins "-"
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-","")}'
        else:
            self.ids.calc_input.text = f'-{prior}'
            
            
    #creation de la fonction decimal
    def dot(self):
        #creation d'une variable qui contient la valeur de la zone texte
        prior = self.ids.calc_input.text
        num_list = prior.split("+")
                
        if "+" in prior and "." not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior
        
        elif "." in prior:
            pass
        else:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior
        
        
            
    #creation de la fonction d'addition
    def math_sign(self,sign):
        #creation d'une variable qui contient la valeur de la zone texte
        prior = self.ids.calc_input.text
        #ajouter le signe + a la textbox
        self.ids.calc_input.text = f'{prior}{sign}'
       
       
    #creation de la fonction de calcul    
    def equals(self):
        #creation d'une variable qui contient la valeur de la zone texte
        prior = self.ids.calc_input.text
        #capture des erreurs
        try:
            #evaluate the math from the textbox (string)
            answer = eval(prior)
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "Erreur"
        
        '''
        #addition
        if "+" in prior:
            num_list = prior.split("+")
            answer = 0.0
            #on boucle sur la liste des nombre
            for number in num_list:
                answer = answer + float(number)
            #print the answer in the textbox
            self.ids.calc_input.text = str(answer)
        '''
class CalculatorApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    CalculatorApp().run()