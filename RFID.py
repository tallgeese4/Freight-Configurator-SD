import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.properties import ObjectProperty,NumericProperty,ListProperty
from kivy.uix.spinner import Spinner

kv=Builder.load_file("rfidgraphics.kv")

class RFIDGraphics(FloatLayout):
	pass



class Screen(App):
	def build(self):
		return RFIDGraphics()

if __name__ == "__main__":
    Screen().run()