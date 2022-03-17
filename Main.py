import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
import Volume_Weight
import RFID
import Stage_Loading


class WindowManager(ScreenManager):
    pass


sm = WindowManager()

screens = [Volume_Weight.VWGraphics(name="Volume_Weight"), RFID.RFIDGraphics(name="RFID"),
           Stage_Loading.LoadGraphics(name="stage_loading")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "Volume_Weight"



class TruckLoading(App):
    def build(self):
        return sm




if __name__ == '__main__':
    TruckLoading = TruckLoading()
    TruckLoading.run()
