import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle, Color
from kivy.properties import ObjectProperty
from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import Screen
from kivy.config import Config

x = 800
y = 600
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', x)
Config.set('graphics', 'height', y)
Config.write()

kv = Builder.load_file("vwgraphics.kv")
i = 0
start = 0
index = 0
Weight_array=[0]
Number_array=[None]


class VWGraphics(Screen):
    global Den
    volume = ObjectProperty(None)
    density = ObjectProperty(None)
    weight = ObjectProperty(None)
    screenbutton=ObjectProperty(None)
    Den = None

    def on_enter(self, *args):
        global i
        self.ids.screenbutton.background_color=(1, 0, 1, 1)
        i = 0

    def spinner_clicked(self, value):
        global Den
        global start
        self.ids.density.text = value
        Den = int(value)
        if start != 0:
            Volume = VWGraphics().VolumeReading()
            if (Volume != None):
                self.ids.volume.text = str(Volume)
                Weight = self.Weightmethod(Volume)
                self.ids.weight.text = str(Weight)

    def VolumeReading(self):
        file1 = open("volume.txt", "r")
        vol = file1.readline()
        file1.close()
        return int(vol)

    def Weightmethod(self, Volume):
        global Den
        Weight = None

        if Den != None:
            Weight = Volume * int(Den)
        return Weight

    def Start(self):
        Volume = int(VWGraphics().VolumeReading())
        Density = Den
        global start
        start = 1
        if (Volume != None):
            self.ids.volume.text = str(Volume)
        if (Density != None and Volume != None):
            Weight = self.Weightmethod(Volume)
            self.ids.weight.text = str(Weight)

    def SubmitData(self):
        global i
        global start
        i = 1
        if start == 1:
            self.PalletNumber()

            Number, Volume, Weight, Density = self.data()
            if (Volume != None and Weight != None and Density != None):
                self.Weight_Sorting(Weight,Number)

        start = 0
        return Weight_array,Number_array

    def clearData(self):
        global i
        i = 0
    def PalletNumber(self):
        global index
        Number, Volume, Weight, Density = self.data()

        if i==1:
            if start == 1:
                if ((Volume != None and Weight != None and Density != None)):
                    index = index + 1

    def Weight_Sorting(self, Weight, Number):
        global Number_array, Weight_array
        place = None
        for i in range(0, Number):
            if (Weight_array[0] < Weight):
                Weight_array.insert(0, Weight)
                place=0
                break

            elif (Weight_array[i] >= Weight and Weight_array[i + 1] < Weight):
                Weight_array.insert(i+1 , Weight)
                place = i
                break
            elif (Weight_array[24] > Weight):
                Weight_array[25] = Weight
                place = 25
                break
        Number_array.insert(place, Number)
        return Weight_array,Number_array

    def data(self):
        global index
        global Den
        global start
        Volume = None
        Weight = None
        Density = None
        Number = index

        if i == 1:
            Volume = self.VolumeReading()
            Weight = self.Weightmethod(Volume)
            Density = str(Den)

        return Number, Volume, Weight, Density
