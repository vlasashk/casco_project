from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.properties import ObjectProperty, StringProperty


class FirstWindow(Screen):
    def set_male(self):
        pol = "male"
        print(pol)
        return pol

    def set_female(self):
        pol = "female"
        print(pol)
        return pol


class SecondWindow(Screen):
    vozrast = ObjectProperty(None)

    def vozrast_read(self):
        print(self.ids)
        text = self.vozrast.text
        vozrast = int(text)
        print(vozrast)
        return vozrast


class ThirdWindow(Screen):
    stazh = ObjectProperty(None)

    def stazh_read(self):
        print(self.ids)
        text = self.stazh.text
        stazh = int(text)
        print(stazh)
        return stazh


class FourthWindow(Screen):
    def checkbox_click(self, instance, value, car):
        App.get_running_app().avto = car


class FifthWindow(Screen):
    def set_yes(self):
        avarii = "was"
        print(avarii)
        return avarii

    def set_no(self):
        avarii = "wasn't"
        print(avarii)
        return avarii


class SixthWindow(Screen):
    def raschet_tarifa(self, avto, pol, vozrast, stazh, avarii, tip_strahovaniya):
        koeff_car_DTP = None
        koeff_car_ugon = None
        koeff_pol_DTP = None
        koeff_pol_ugon = None
        koeff_avarii = None
        koeff_vozr_stazh = None

        # Авто до 800 тыс
        low = [
            "Chevrolet NIVA",
            "Datsun on-DO",
            "Lada 4x4",
            "Lada Granta",
            "Lada Kalina",
            "Lada Largus",
            "Lada Vesta",
            "Lada X-Ray",
            "Renault Logan",
            "Renault Sandero",
        ]
        # Авто от 800 тыс до 1,6 млн
        mid = [
            "Hyundai Creta",
            "Nissan Qashqai",
            "Renault Duster",
            "Renault Kaptur",
            "VW Polo",
            "Skoda Rapid",
            "KIA Rio",
            "Hyundai Solaris",
        ]
        # Авто от 1,6 млн
        prem = [
            "KIA Sportage",
            "Mazda CX-5",
            "Nissan X-Trail",
            "Skoda Octavia A7",
            "Toyota Camry",
            "Toyota RAV 4",
            "VW Tiguan",
        ]
        tariff_DTP = 18000
        tarif_ugon = 7000

        if avto in low:
            koeff_car_DTP = 0.73
            koeff_car_ugon = 0.95
        elif avto in mid:
            koeff_car_DTP = 1
            koeff_car_ugon = 0.83
        elif avto in prem:
            koeff_car_DTP = 1.6
            koeff_car_ugon = 1.45
        else:
            return print("Ошибка класса авто ", avto)

        if pol == "male":
            koeff_pol_DTP = 1.15
            koeff_pol_ugon = 0.97
        elif pol == "female":
            koeff_pol_DTP = 0.8
            koeff_pol_ugon = 1.05
        else:
            return print("Ошибка пола", pol)

        if avarii == "was":
            koeff_avarii = 1.24
        elif avarii == "wasn't":
            koeff_avarii = 0.75
        else:
            return print("Ошибка аварий ", avarii)

        if (
            ((vozrast <= 21) & (stazh == 0))
            | ((38 <= vozrast <= 50) & (stazh == 3))
            | ((vozrast >= 51) & (4 <= stazh <= 5))
        ):
            koeff_vozr_stazh = 1.9

        elif (28 <= vozrast <= 37) & (stazh == 1):
            koeff_vozr_stazh = 1.8

        elif (
            ((vozrast <= 21) & (stazh == 2))
            | ((vozrast >= 50) & (stazh == 3))
            | ((28 <= vozrast <= 37) & (stazh == 3))
        ):
            koeff_vozr_stazh = 1.7

        elif (vozrast <= 21) & (stazh == 1):
            koeff_vozr_stazh = 1.6

        elif (
            ((vozrast <= 21) & (stazh == 3))
            | ((22 <= vozrast <= 27) & (stazh == 1))
            | ((vozrast >= 51) & ((6 <= stazh <= 10) | (stazh >= 25)))
            | ((vozrast >= 51) & (stazh == 0))
        ):
            koeff_vozr_stazh = 1.5

        elif ((38 <= vozrast <= 50) & (0 <= stazh <= 1)) | (
            (vozrast >= 51) & (stazh == 1)
        ):
            koeff_vozr_stazh = 1.4

        elif (
            ((22 <= vozrast <= 27) & ((stazh == 0) | (stazh == 3)))
            | ((28 <= vozrast <= 37) & (6 <= stazh <= 10))
            | ((38 <= vozrast <= 50) & (stazh == 2))
            | ((vozrast >= 51) & (stazh == 2))
        ):
            koeff_vozr_stazh = 1.3

        elif ((22 <= vozrast <= 27) & (6 <= stazh <= 10)) | (
            (38 <= vozrast <= 50) & (4 <= stazh <= 5)
        ):
            koeff_vozr_stazh = 1.2

        elif ((28 <= vozrast <= 37) & ((4 <= stazh <= 5) | (18 <= stazh <= 24))) | (
            (38 <= vozrast <= 50) & ((6 <= stazh <= 17) | (stazh >= 25))
        ):
            koeff_vozr_stazh = 1.15

        elif ((22 <= vozrast <= 27) & ((stazh == 2) | (4 <= stazh <= 5))) | (
            (28 <= vozrast <= 37) & (11 <= stazh <= 17)
        ):
            koeff_vozr_stazh = 1.1

        elif ((28 <= vozrast <= 37) & (stazh == 2)) | (
            (38 <= vozrast <= 50) & (18 <= stazh <= 24)
        ):
            koeff_vozr_stazh = 1

        elif ((28 <= vozrast <= 37) & (stazh == 0)) | (
            (vozrast >= 51) & ((11 <= stazh <= 24))
        ):
            koeff_vozr_stazh = 0.9

        else:
            return print("Ошибка возраста и стажа ", vozrast, " ", stazh)

        final_tarif = (
            tariff_DTP * koeff_avarii * koeff_pol_DTP * koeff_vozr_stazh * koeff_car_DTP
        )

        if tip_strahovaniya == "partial":
            print(round(final_tarif))
            return round(final_tarif)
        elif tip_strahovaniya == "full":
            final_tarif_full = (
                final_tarif + tarif_ugon * koeff_car_ugon * koeff_pol_ugon
            )
            print(round(final_tarif_full))
            return round(final_tarif_full)
        else:
            return print("Ошибка типа страхования ", tip_strahovaniya)

    def set_full(self):
        tip_strahovaniya = "full"
        print(tip_strahovaniya)
        return tip_strahovaniya

    def set_partial(self):
        tip_strahovaniya = "partial"
        print(tip_strahovaniya)
        return tip_strahovaniya

    def set_text_final(self):
        text = str(App.get_running_app().raschet_tarifa) + " ₽"
        self.manager.get_screen("seventh").labelText = text


class SeventhWindow(Screen):
    labelText = StringProperty("My label")


class WindowManager(ScreenManager):
    pass


Config.set("graphics", "width", "900")
Config.set("graphics", "height", "600")
Config.set("graphics", "resizable", False)

kv = Builder.load_file("calculator.kv")


class Calculator(App):
    avto = None
    pol = None
    vozrast = None
    stazh = None
    avarii = None
    tip_strahovaniya = None
    tip_strahovaniya = None
    raschet_tarifa = None

    def build(self):
        Window.clearcolor = (255, 179, 105, 1)
        return kv


if __name__ == "__main__":
    Calculator().run()
