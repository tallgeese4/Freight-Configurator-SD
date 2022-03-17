import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle, Color, Line
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivy.uix.screenmanager import Screen
import Volume_Weight

x = 800
y = 600

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', x)
Config.set('graphics', 'height', y)
Config.write()


class LoadGraphics(Screen):
    kv = Builder.load_file('loadgraphics.kv')
    screenbutton = ObjectProperty(None)
    
    def on_enter(self, *args):
        
        self.ids.screenbutton.background_color = (1, 0, 1, 1)
        Number, Volume, Weight, Density = Volume_Weight.VWGraphics().data()
        with self.canvas.before:
            Color(.66, .66, .66, .66)
            Rectangle(pos=(0, (y * .15)), size=((x * .5), (y * .45)))
            Color(0, 0, 0, 1)
            Line(points=[(0), (y * .45), (x * .5), (y * .45)], width=5)
            Line(points=[(0), (y * .30), (x * .5), (y * .3)], width=5)
        shelf = Label(text="Staging Shelf", font_size=30, size_hint=(.4, .4), pos_hint={'x': .04, 'y': .45})
        self.add_widget(shelf)

        with self.canvas.before:
            Color(.66, .66, .66, .66)
            Rectangle(pos=((x * .725), (y * .025)), size=((x * .2), (y * .8)))
        trailer = Label(text="Trailer", font_size=30, size_hint=(.4, .4), pos_hint={'x': .625, 'y': .65})
        self.add_widget(trailer)
        if (Volume != None and Weight != None and Density != None ):
            if Number>26:
                Number=26

            for i in range(1, Number+1):
                if i < 11:
                    Volume = Label(text=str(i), font_size=30, size_hint=(.04, .06),
                                   pos_hint={'x': ((i - 1) / 20), 'y': .5}, color=(0, 0, 0, 1))
                    with Volume.canvas.before:
                        Color(1, 1, 1, 1)
                        Rectangle(pos=((x * ((i - 1) / 20)), y * .5), size=((x * .04), (y * .06)))
                elif 11 <= i < 21:
                    Volume = Label(text=str(i), font_size=25, size_hint=(.04, .06),
                                   pos_hint={'x': ((i - 11) / 20), 'y': .35}, color=(0, 0, 0, 1))
                    with Volume.canvas.before:
                        Color(1, 1, 1, 1)
                        Rectangle(pos=((x * ((i - 11) / 20)), y * .35), size=((x * .04), (y * .06)))
                else:
                    Volume = Label(text=str(i), font_size=25, size_hint=(.04, .06),
                                   pos_hint={'x': ((i - 21) / 20), 'y': .2}, color=(0, 0, 0, 1))
                    with Volume.canvas.before:
                        Color(1, 1, 1, 1)
                        Rectangle(pos=((x * ((i - 21) / 20)), y * .2), size=((x * (.04)), (y * .06)))

                self.add_widget(Volume)




    def Loading_Sequence(self):
        pass
