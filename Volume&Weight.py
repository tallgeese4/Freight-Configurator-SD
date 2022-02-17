
import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.properties import ObjectProperty



class Graphics(FloatLayout):
	vol = ObjectProperty(None)

	def lab(self):
		volume=500;
		self.vol.text = str(volume)






class Screen(App):
	def build(self):
		return Builder.load_file("graphics.kv")

Screen().run()