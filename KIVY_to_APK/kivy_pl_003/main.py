## Sample Python application demonstrating the 
## working of PageLayout in Kivy using .kv file 

##################################################
# import kivy module 
import kivy 

# base Class of your App inherits from the App class. 
# app:always refers to the instance of your application 
from kivy.app import App

# this restrict the kivy version i.e 
# below this kivy version you cannot 
# use the app or software 
kivy.require('1.9.0')

# The PageLayout class is used to create
# a simple multi-page layout,
# in a way that allows easy flipping from
# one page to another using borders.
from kivy.uix.pagelayout import PageLayout

# creating the root widget used in .kv file 
class PageLayout(PageLayout):
	pass

# creating the App class in which name 
#.kv file is to be named PageLayout.kv 
class PageLayoutApp(App): 
	# defining build() 
	def build(self): 
		# returning the instance of root class 
		return PageLayout() 

# creating object of PageLayoutApp() class
plApp = PageLayoutApp()

# run the class
plApp.run()
