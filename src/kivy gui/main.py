from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivy.properties import DictProperty
from kivy.properties import NumericProperty
from kivy.uix.button import ButtonBehavior


class StarsailorApp(App):
    def build(self):
        return Starsailor()


class Starsailor(GridLayout):
    def create_new_game(self):
        NewGameScreen()
        Player.food = 100
        Player.money = 1000
        Player.sanity = 85



class PersistentFrame(GridLayout):
    pass

class NewGameScreen(BoxLayout):
    pass





class Player(Widget):
    name = StringProperty
    food = NumericProperty
    money = NumericProperty
    sanity = NumericProperty





if __name__ == '__main__':
    StarsailorApp().run()
