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
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.vector import Vector
import time 


Builder.load_file("Starsailor.kv")


class Boat(Image):
    def move_to(self, coordinates: list):
        for x in range(coordinates[0]):
            self.pos.x += 1
            time.sleep(.001)
        for x in range(coordinates[1]):
            self.pos.y += 1




class StarsailorApp(App):
    def build(self):
        self.root_widget = Starsailor()
        return self.root_widget
    


class Starsailor(GridLayout):
    name = StringProperty
    food = NumericProperty
    money = NumericProperty
    sanity = NumericProperty
    inventory: ListProperty
    text_entry0 = None



    def clear_active_frame(self, *args):
        self.ids.ActiveFrame.clear_widgets()
        self.ids.Bottom_Tool_Bar.clear_widgets()

    def create_new_game(self):
        self.food = 100
        self.money = 1000
        self.sanity = 85
        self.clear_active_frame()

        text_label = Label(text="Name")
        self.text_entry0 = TextInput(font_size=120)
        self.ids.ActiveFrame.add_widget(text_label)
        self.ids.ActiveFrame.add_widget(self.text_entry0)

        button = Button(text="Save", background_color=(1, 0, 0, 1), on_press=self.save_name_and_clear,
                        on_release=self.create_intro_screen)

        self.ids.ActiveFrame.add_widget(button)

    def save_name_and_clear(self, *args):
        self.name = self.text_entry0.text
        self.clear_active_frame()

    def create_intro_screen(self, *args):
        self.ids.ActiveFrame.add_widget(IntroScreen())

    def proceed_to_heavens_forge(self, *args):
        active_frame = self.ids['ActiveFrame']
        active_frame.clear_widgets()
        





class IntroScreen(BoxLayout):
    pass


class HeavensForge(FloatLayout):
    pass
        



if __name__ == '__main__':
    StarsailorApp().run()
