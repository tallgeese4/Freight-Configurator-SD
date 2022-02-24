
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.properties import ObjectProperty,NumericProperty,ListProperty
from kivy.uix.spinner import Spinner


kv=Builder.load_file("vwgraphics.kv")

class VWGraphics(FloatLayout):
	volume = ObjectProperty(None)
	density = ObjectProperty(None)
	weight = ObjectProperty(None)
	def spinner_clicked(self,value):
		self.ids.Density.text = value

	def lab(self):
		vol=500;
		self.volume.text = str(vol)


class Screen(App):
	def build(self):
		return VWGraphics()

if __name__ == "__main__":
    Screen().run()