from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage


class CarouselApp(App):
    def build(self):
        carousel = Carousel(direction='right')
        for i in range(1,5):
            src = "D:\\eric\\PARTAGE\\images\\linux"+str(i)+".png" 
            image = AsyncImage(source=src, fit_mode="contain")
            carousel.add_widget(image)
        return carousel


CarouselApp().run()