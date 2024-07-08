from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivy.properties import DictProperty
from kivy.properties import NumericProperty
from kivy.uix.button import ButtonBehavior

from kivy.lang import Builder

Builder.load_file("Starsailor.kv")


class StarsailorApp(App):
    def build(self):
        return Starsailor()


class Starsailor(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.main_frame = self.ids.ActiveFrame
        self.bottom_tool_bar = self.ids.Bottom_Tool_Bar

    def clear_active_frame(self):
        self.bottom_tool_bar.clear_widgets()
        self.main_frame.clear_widgets()

    def create_new_game(self):
        Player.food = 100
        Player.money = 1000
        Player.sanity = 85
        self.clear_active_frame()
        text_label = Label(text="Name")
        text_entry0 = TextInput()
        self.add_widget(text_label)
        self.add_widget(text_entry0)





class Player(Widget):
    name = StringProperty
    food = NumericProperty
    money = NumericProperty
    sanity = NumericProperty


if __name__ == '__main__':
    StarsailorApp().run()
