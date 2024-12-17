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


Builder.load_file("Starsailor.kv")


class Starsailor(BoxLayout):
    # root widget
    pass


class MainMenu(Screen):
    # start screen
    pass

class IntroScreen(Screen):
    # Intro_Screen
    pass

class Map(Screen):
    # Central Map
    pass


class StarsailorApp(App):
    def build(self):
        root = Starsailor()
        return root


if __name__ == '__main__':
    StarsailorApp().run()
