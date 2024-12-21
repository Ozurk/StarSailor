from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle
from kivy.app import App
from kivy.properties import StringProperty, NumericProperty, ListProperty, ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition, SwapTransition
from kivy.uix.scrollview import ScrollView
from kivy.uix.relativelayout import RelativeLayout


Builder.load_file("Starsailor.kv")


class Starsailor(BoxLayout):
    money = NumericProperty(0)

class MainMenu(Screen):
    # start screen
    pass

class IntroScreen(Screen):
    # Intro_Screen
    pass

class Map(Screen):
    # Central Map
    pass

class Inventory(BoxLayout):
    pass


class HeavensForgeLanding(Screen):
    pass

class Factory(Screen):
    pass

class LightWelder(Screen):
    pass


class ChtakLanding(Screen):
    pass

class TwilightIslesLanding(Screen):
    pass

class Valstafarlanding(Screen):
    pass

class EndLanding(Screen):
    pass

































class StarsailorApp(App):
    def build(self):
        root = Starsailor()
        self.root = root
        return root


if __name__ == '__main__':
    StarsailorApp().run()
