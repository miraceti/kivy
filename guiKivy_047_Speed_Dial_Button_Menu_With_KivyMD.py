from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):
    #key=icon: value=text
    data = {
        "language-python": "Python",
        "language-ruby": "Ruby",
        "language-java": "Java",
        "language-javascript": "JS"
    }
    
    def callback(self, instance):
        lang=""
        if instance.icon == 'language-python':
            lang = "Python"
        elif instance.icon == 'language-javascript':
            lang = "JS"
        elif instance.icon == 'language-java':
            lang = "Java"
        elif instance.icon == 'language-ruby':
            lang = "Ruby"
            
        self.root.ids.my_label.text = f'you press {lang}'
    
    # open
    def open(self):
        self.root.ids.my_label.text = f'OPEN!'
        
    def close(self):
        self.root.ids.my_label.text = f'CLOSE!'
    
    def build(self):
        self.theme_cls.theme_style= "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('kivy047.kv')
    
    

MainApp().run()