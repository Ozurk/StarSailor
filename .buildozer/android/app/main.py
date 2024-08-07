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
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.scrollview import ScrollView

Builder.load_file("Starsailor.kv")




class MainMenuTopButtons(BoxLayout):
    pass

class Boat(Image):
    def move_to(self, x_coord, y_coord, _duration):
        animation = Animation(x=x_coord, y=y_coord, duration=_duration)
        animation.start(self)


        

class Planet(Widget):
    def move_to(self, x_coord, y_coord, _duration):
        animation = Animation(x=x_coord, y=y_coord, duration=_duration)
        animation.start(self)

    def change_size(self, size, _duration):
        animation = Animation(size=size, duration=_duration)
        animation.start(self)


class Map(Screen):
    window_width = Window.width
    window_height = Window.height
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            # Convert touch position to the ship's parent coordinate space
            parent = self.ids.ship.parent
            touch_pos = parent.to_widget(*touch.pos)
            # Move the ship to the new position
            self.ids.ship.move_to(touch_pos[0], touch_pos[1], 1)
        return super().on_touch_down(touch)
    
class HForgeTopDown(Screen):
    window_width = Window.width
    window_height = Window.height


class HForgeFactory(Screen):
    pass

class LightWelder(Image):
    def on_touch_move(self, touch):
        animation = Animation(x=self.x + 20, y=self.y, duration=.2)
        animation.start(self)
        return super().on_touch_move(touch)
            
            
class Starsailor(ScreenManager):    
    name = StringProperty()
    food = NumericProperty(0)
    money = NumericProperty(0)
    sanity = NumericProperty(0)
    inventory = ListProperty([])
    ship = ObjectProperty(None)
    map = ObjectProperty(None)

    

    

class StartMenu(Screen):
    def create_new_game(self, *args):
        self.food = 100
        self.money = 1000
        self.sanity = 85
        self.ship = self.map.ids.ship
        self.add_widget(self.map)
        

class TopButtons(BoxLayout):
    pass


class StarsailorApp(App):
    def build(self):
        root = Starsailor()
        return root
        


if __name__ == '__main__':
    StarsailorApp().run()
