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
from kivy.uix.button import ButtonBehavior, Button

from kivy.lang import Builder



class StarsailorApp(App):
    def build(self):
        return Starsailor()


class Starsailor(GridLayout):
    def clear_active_frame(self):
        self.ids.ActiveFrame.clear_widgets()
        self.ids.Bottom_Tool_Bar.clear_widgets()

    def create_new_game(self):
        Player.food = 100
        Player.money = 1000
        Player.sanity = 85
        self.clear_active_frame()

        text_label = Label(text="Name")
        text_entry0 = TextInput()
        self.ids.ActiveFrame.add_widget(text_label)
        self.ids.ActiveFrame.add_widget(text_entry0)

        text_label1 = Label(text="Place")
        text_entry1 = TextInput()
        self.ids.ActiveFrame.add_widget(text_label1)
        self.ids.ActiveFrame.add_widget(text_entry1)

        button = Button(text="Save", background_color=(1, 0, 0, 1), on_release=self.ids.ActiveFrame.clear_widgets)
        self.ids.ActiveFrame.add_widget(button)


class Player(Widget):
    name = StringProperty
    food = NumericProperty
    money = NumericProperty
    sanity = NumericProperty


if __name__ == '__main__':
    StarsailorApp().run()
