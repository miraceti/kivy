from kivy.app import App, Widget
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse
#from kivy.core.text import LabelBase, DEFAULT_FONT
#LabelBase.register(DEFAULT_FONT, 'NotoSansCJKjp-Regular.otf')


class MyWidget(Widget):
    evn = None

    def __init__(self, *args, **kwargs):
        Widget.__init__(self, *args, **kwargs)
        self.ellipse_pos_x = 200
        self.ellipse_pos_y = 200
        self.ellipse_pos = (self.ellipse_pos_x, self.ellipse_pos_y)
        self.ellipse_width = 200
        self.ellipse_height = 200
        self.ellipse_size = (self.ellipse_width, self.ellipse_height)
        self.move = 5
        self.evn = Clock.schedule_interval(self.update, 0.01)

    def update(self, dt):
        self.canvas.clear()
        with self.canvas:
            Color(rgb=(0, 255, 0))
            Ellipse(pos=self.ellipse_pos, size=self.ellipse_size)
            if self.ellipse_pos_x + self.ellipse_width >= self.width:
                self.move = -5
            elif self.ellipse_pos_y + self.ellipse_height >= self.height:
                self.move = -5
            elif self.ellipse_pos_x <= 0:
                self.move = +5
            self.ellipse_pos_x += self.move
            self.ellipse_pos_y += self.move
            self.ellipse_pos = (self.ellipse_pos_x, self.ellipse_pos_y)


class Sample4App(App):
    def build(self):
        return MyWidget()


Sample4App().run()
