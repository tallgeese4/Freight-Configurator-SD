from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle, Color
from kivy.properties import ObjectProperty
from kivy.uix.spinner import Spinner
from kivy.config import Config
import csv

x = 800
y = 600
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', x)
Config.set('graphics', 'height', y)
Config.write()

class Graphics(FloatLayout):
    global Density_Var
    global Volume_Var
    global Weight_Var
    global Pallet_Number
    global start
    global filename

    Density_Var = None
    Volume_Var=None
    Weight_Var=None
    Pallet_Number=None
    filename=None
    start=0

    volume = ObjectProperty(None)
    density = ObjectProperty(None)
    weight = ObjectProperty(None)
    status = ObjectProperty(None)

    def spinner_clicked(self, value):

        global Density_Var
        global Volume_Var
        global Weight_Var
        global start
        global csvfile

        self.ids.density.text = value
        if value!="":
            Density_Var = float(value.split(" ")[0])
        if start == 1:
            if (Volume_Var != None):
                self.ids.volume.text = str(Volume_Var)+" ft^3"
                self.Weightmethod()
                self.ids.weight.text = str(round(Weight_Var,3))+ " lbs"

    def VolumeReading(self):
        global Volume_Var
        file1 = open("volume.txt", "r")
        Volume_Var = float(file1.readline())
        file1.close()

    def Weightmethod(self):
        global Density_Var
        global Weight_Var
        global Volume_Var

        if Density_Var != None:
            Weight_Var = Volume_Var * Density_Var


    def Scan(self):
        global Volume_Var
        global Pallet_Number
        if start == 1:
            self.ids.density.text = ""
            self.ids.weight.text = ""
            Pallet_Number=+1
            self.VolumeReading()
            if (Volume_Var != None):
                self.ids.volume.text = str(Volume_Var)+" cm^3"

    def SubmitData(self):
        global start
        global Density_Var
        global Volume_Var
        global Weight_Var
        global Pallet_Number
        global filename
        if start==1:
            with open(filename, 'a',newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow([str(Pallet_Number),str(Volume_Var),str(Density_Var),str(Weight_Var)])


    def Status(self):
        global start
        global filename
        global Pallet_Number
        global csvfile
        if start==0:
            start = 1
            self.ids.status.background_color=(0,1,0,1)
            Pallet_Number=0
            filename = "Bill_of_Laden.csv"
            with open(filename, 'w',newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(["Pallet","Volume","Density","Weight"])
                csvwriter.writerow(["", "cm^3", "g/cm^3", "lbs"])
        elif start==1:
            start =0
            self.ids.status.background_color=(1,0,0,1)
            Pallet_Number=None
            csvfile.close()








kv = Builder.load_file("graphics.kv")
class TruckLoading(App):
    def build(self):
        return Graphics()

if __name__ == '__main__':
    TruckLoading = TruckLoading()
    TruckLoading.run()
