# Sample Python application demonstrating 
# How to create PageLayout in Kivy 

import kivy 

# base Class of your App inherits from the App class. 
# app:always refers to the instance of your application 
from kivy.app import App 

# The PageLayout class is used to create
# a simple multi-page layout,
# in a way that allows easy flipping from
# one page to another using borders.
from kivy.uix.pagelayout import PageLayout

# creates the button in kivy 
# if not imported shows the error 
from kivy.uix.button import Button

class PageLayout(PageLayout):
	"""
	Define class PageLayout here
	"""

	def __init__(self):
		
		# The super function in Python can be
		# used to gain access to inherited methods
		# which is either from a parent or sibling class.
		super(PageLayout, self).__init__()

		# creating buttons on different pages
		btn1 = Button(text ='Page 1')
		
		btn2 = Button(text ='Page 2')

		btn3 = Button(text ='Page 3')

		# adding button on the screen
		# by add widget method
		self.add_widget(btn1)

		self.add_widget(btn2)

		self.add_widget(btn3)


# creating the App class
class Page_LayoutApp(App):
	"""
	App class here
	"""

	def build(self):
		"""
		build function here
		"""
		return PageLayout()


# Run the App
if __name__ == '__main__':
	Page_LayoutApp().run()
