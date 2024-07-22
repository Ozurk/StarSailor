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
from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
Builder.load_file("Starsailor.kv")


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

    def change_size(self, size: list, _duration):
        
        animation = Animation(size=size, duration=_duration)
        animation.start(self)




class StarsailorApp(App):
    def build(self):
        main_widget = Starsailor()
        return  main_widget
    


class Starsailor(GridLayout):
    name = StringProperty
    food = NumericProperty
    money = NumericProperty
    sanity = NumericProperty
    inventory: ListProperty


    def clear_active_frame(self, *args):
        self.ids.ActiveFrame.clear_widgets()
        self.ids.Bottom_Tool_Bar.clear_widgets()


    def create_new_game(self, *args):
        active_frame = self.ids.ActiveFrame
        self.food = 100
        self.money = 1000
        self.sanity = 85
        self.clear_active_frame()
        main_window = MainGameWindow()
        active_frame.add_widget(main_window)





class MainGameWindow(ScrollView):
    def on_touch_down(self, touch):
        ship = self.ids.ship
        ship.move_to(touch.pos[0] - (ship.width / 2), (touch.pos[1] - ship.height * 1.25), 1)
        return super().on_touch_down(touch)
    
    

      




if __name__ == '__main__':
    StarsailorApp().run()
