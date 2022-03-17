import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle, Color
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.config import Config
import Volume_Weight

x = 800
y = 600
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', x)
Config.set('graphics', 'height', y)
Config.write()





class RFIDGraphics(Screen):
    kv = Builder.load_file("rfidgraphics.kv")
    output=ObjectProperty(None)
    screenbutton = ObjectProperty(None)

    def on_enter(self, *args):
        self.ids.screenbutton.background_color = (1, 0, 1, 1)
        Number,Volume,Weight,Density=Volume_Weight.VWGraphics().data()
        if(Volume== None or Weight==None or Density==None):
            self.ids.output.text = "Redo Weight calculation"
        elif(Number>26):
            self.ids.output.text = "Pallets scanned exceed 26"
        else:
            self.ids.output.text=("Pallet: "+ str(Number)+"\nVolume: " + str(Volume)+"\nDensity: " + str(Density)+"\nWeight: " + str(Weight))

    def SubmitRFID(self):
        Number, Volume, Weight, Density = Volume_Weight.VWGraphics().data()
        if (Volume != None and Weight != None and Density != None):
            RFIDfile = open("RFIDOutput.txt", mode="w")
            RFIDfile.write("Pallet: "+ str(Number)+"\nVolume: " + str(Volume)+"\nDensity: " + str(Density)+"\nWeight: " + str(Weight))
            RFIDfile.close
