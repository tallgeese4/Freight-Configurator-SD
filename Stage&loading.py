import kivy
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.properties import ObjectProperty, NumericProperty, ListProperty
from kivy.uix.spinner import Spinner
from kivymd.uix.datatables import MDDataTable

from kivy.metrics import dp

Builder.load_file("loadgraphics.kv")


class LoadGraphics(MDApp):
    pass


if __name__ == "__main__":
    LoadGraphics().run()
