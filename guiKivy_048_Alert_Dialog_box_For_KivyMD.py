from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton

class MainApp(MDApp):
    dialog = None
    def build(self):
        self.theme_cls.theme_style= "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('kivy048.kv')
    
    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title = "Pretty good !",
                text = "this is just some text",
                buttons = [
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color, on_release= self.close_dialog
                        ),
                    MDRectangleFlatButton(
                        text="Yes it's good!", text_color=self.theme_cls.primary_color, on_release=self.neat_dialog
                        ),
                    ] ,                 
                )
             
        self.dialog.open()
        
    # close alert dialog by  the cancel button         # 
    def close_dialog(self, obj):
        self.dialog.dismiss()
    
    #close alert box 
    def neat_dialog(self, obj):
        self.dialog.dismiss()
        # change label text
        self.root.ids.my_label.text = "Yes it-s good "

MainApp().run()