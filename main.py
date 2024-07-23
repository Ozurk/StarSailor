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
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.lang import Builder
from kivy.vector import Vector
from kivy.uix.scrollview import ScrollView

Builder.load_file("Starsailor.kv")

class MoveButtons(BoxLayout):

    def scroll_up(self):
        MainGameWindow.scroll_up(MainGameWindow)

    def scroll_down(self):
        MainGameWindow.scroll_down(MainGameWindow)
        


class MainMenuTopButtons(BoxLayout):
    pass

class Boat(Image):
    def move_to(self, x_coord, y_coord, _duration):
        animation = Animation(x=x_coord, y=y_coord, duration=_duration)
        animation.start(self)

    def change_size(self, _height, _width, _duration):
        animation = Animation(height=_height, width=_width, duration=_duration)
        animation.start(self)
        

class Planet(Widget):
    def move_to(self, x_coord, y_coord, _duration):
        animation = Animation(x=x_coord, y=y_coord, duration=_duration)
        animation.start(self)

    def change_size(self, size, _duration):
        animation = Animation(size=size, duration=_duration)
        animation.start(self)


class MainGameWindow(ScrollView):
    ship = ObjectProperty(None)
    
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            parent = self.ship.parent
            touch_pos = parent.to_widget(*touch.pos)
            self.ship.move_to(touch_pos[0], touch_pos[1], 1)
            return True
        return super().on_touch_down(touch)
    
    def scroll_up(self):
        self.scroll_y = min(self.scroll_y + 0.1, 1)

    def scroll_down(self):
        self.scroll_y = max(self.scroll_y - 0.1, 0)


class Starsailor(GridLayout):
    name = StringProperty()
    food = NumericProperty(0)
    money = NumericProperty(0)
    sanity = NumericProperty(0)
    inventory = ListProperty([])

    def clear_active_frame(self, *args):
        self.ids.ActiveFrame.clear_widgets()
        self.ids.Bottom_Tool_Bar.clear_widgets()
        self.ids.Bottom_Tool_Bar.add_widget(MoveButtons())

    def create_new_game(self, *args):
        active_frame = self.ids.ActiveFrame
        self.food = 100
        self.money = 1000
        self.sanity = 85
        self.clear_active_frame()
        main_window = MainGameWindow()
        active_frame.add_widget(main_window)


class StarsailorApp(App):
    def build(self):
        return Starsailor()


if __name__ == '__main__':
    StarsailorApp().run()
