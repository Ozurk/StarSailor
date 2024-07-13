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
from kivy.properties import ListProperty


# from kivy.lang import Builder


class StarsailorApp(App):
    def build(self):
        return Starsailor()


class Starsailor(GridLayout):
    text_entry0 = None
    def clear_active_frame(self, *args):
        self.ids.ActiveFrame.clear_widgets()
        self.ids.Bottom_Tool_Bar.clear_widgets()

    def create_new_game(self):
        Player.food = 100
        Player.money = 1000
        Player.sanity = 85
        self.clear_active_frame()

        text_label = Label(text="Name")
        self.text_entry0 = TextInput()
        self.ids.ActiveFrame.add_widget(text_label)
        self.ids.ActiveFrame.add_widget(self.text_entry0)

        button = Button(text="Save", background_color=(1, 0, 0, 1), on_press=self.save_name_and_clear,
                        on_release=self.create_main_game_window)

        self.ids.ActiveFrame.add_widget(button)

    def save_name_and_clear(self, *args):
        Player.name = self.text_entry0.text
        self.clear_active_frame()


    def create_main_game_window(self, *args):
        active_frame = self.ids.ActiveFrame
        label = Label(text=f"Hello, {Player.name}", color=(1, 0, 0, 1), font_size=100)
        active_frame.add_widget(label)


class Player(Widget):
    name = StringProperty
    food = NumericProperty
    money = NumericProperty
    sanity = NumericProperty
    inventory: ListProperty


if __name__ == '__main__':
    StarsailorApp().run()
