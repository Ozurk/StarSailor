from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.app import App
#:import utils kivy.utils


class Starsailor(GridLayout):
    pass


class StarsailorApp(App):
    def build(self):
        return Starsailor()


if __name__ == '__main__':
    StarsailorApp().run()