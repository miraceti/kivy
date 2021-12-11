from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.videoplayer import VideoPlayer

class MainApp(MDApp):
    title = "Simple Video Player"
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        
        # create VideoPlayer instance
        player = VideoPlayer(source="videos/intro.mp4") 
        
        # Assign VideoPlayer state
        player.state = 'play'
        
        player.options = {'eos' : "loop"} #'pause' ; 'stop'
        
        player.allow_stretch = True
        
        # return player
        return player
        
MainApp().run()
 
