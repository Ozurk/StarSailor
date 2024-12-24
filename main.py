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
from kivy.clock import Clock
Builder.load_file("Starsailor.kv")


class Starsailor(BoxLayout):
    money = NumericProperty(0)

    def toggle_inventory(self):
        # Access the inventory widget
        app = App.get_running_app()
        inventory = app.root.ids.Inventory

        # Toggle visibility
        if inventory.opacity == 0:  # If currently hidden
            inventory.opacity = 1
            inventory.width = 0
            inventory.disabled = False
        else:  # If currently visible
            inventory.opacity = 0
            inventory.width = self.width / 2
            inventory.disabled = True


class MainMenu(Screen):
    # start screen
    pass

class IntroScreen(Screen):
    # Intro_Screen
    pass

class Map(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.moving_boat_event = None  # Event for continuous movement

    def start_moving_boat(self, direction):
        """Start moving the boat in the given direction."""
        if self.moving_boat_event is None:
            self.moving_boat_event = Clock.schedule_interval(
                lambda dt: self.move_boat(direction), 0.05
            )

    def move_boat(self, direction):
        """Move the boat in the specified direction."""
        scrollview = self.ids.Scrollview
        layout = self.ids.MapImage

        boat = self.ids.Boat  # Reference to the boat widget
        if direction == 'up':
            boat.y += 15  # Adjust the increment as needed
            boat.source = 'pictures/Boats/boat_in_motion_up.png'
        elif direction == 'down':
            boat.y -= 15
            boat.source = 'pictures/Boats/boat_in_motion_down.png'
        elif direction == 'left':
            boat.source = 'pictures/Boats/boat_in_motion_left.png'
            boat.x -= 15
        elif direction == 'right':
            boat.source = 'pictures/Boats/boat_in_motion.png'
            boat.x += 15

        scrollview.scroll_x = (boat.x + boat.width / 2 - scrollview.width / 2) / layout.width * 2
        scrollview.scroll_y = (boat.y + boat.height / 2 - scrollview.height / 2) / layout.height * 2

    def stop_moving_boat(self):
        boat = self.ids.Boat  # Reference to the boat widget
        """Stop moving the boat."""
        if self.moving_boat_event is not None:
            self.moving_boat_event.cancel()
            self.moving_boat_event = None
            if boat.source == "pictures/Boats/boat_in_motion.png":
                boat.source = 'pictures/Boats/boat.png'
            elif boat.source == 'pictures/Boats/boat_in_motion_left.png':
                boat.source = 'pictures/Boats/boat_left.png'
            elif boat.source == 'pictures/Boats/boat_in_motion_up.png':
                boat.source = 'pictures/Boats/boat_up.png'
            elif boat.source == 'pictures/Boats/boat_in_motion_down.png':
                boat.source = 'pictures/Boats/boat_down.png'
                

class Boat(Image):
    pass

class Inventory(BoxLayout):
    pass


class HeavensForgeLanding(Screen):
    pass

class Factory(Screen):
    pass

class LightWelder(Screen):
    
    dialog = """A Overclocked Lightwelder runs red hot steam whistling off its rotund metallic frame. It's voice box
            drones out to you.I have overseen this forge for millennia and time has taken its toll on me.
            These rusty joints once shined with a coat of star paint but has since peeled off over the many centuries in this immense heat, 
            and without its protective properties, I fear for my imminent dissolution. I fear the last can of starpaint was used up decades ago, should you find some. I will bestow upon 
            you a pallet of hardlight. This will surely be invaluable in the exploration of more distant skies."""

    success = "Thank you very much. Here is your hardlight"


    def trade_starpaint(self):
        app = App.get_running_app()
        inventory = app.root.ids.Inventory_Grid
        if 'Starpaint' in inventory.ids:
            starpaint = inventory.ids.Starpaint
            inventory.remove_widget(starpaint)
            self.ids.LightWelderDialog.text = self.success
            self.add_hardlight_to_inventory()



    def add_hardlight_to_inventory(self):
        app = App.get_running_app()
        inventory = app.root.ids.Inventory_Grid
        hardlight = Image(source="pictures/heavens_forge/the factory/hardlight.png")
        print(inventory.ids)
        if "Hardlight" not in inventory.ids:
            inventory.add_widget(hardlight)
            inventory.ids.Hardlight = hardlight


class ChtakLanding(Screen):
    pass

class TwilightIslesLanding(Screen):
    pass


class Showroom(Screen):
    pass


class DisplayCase(Screen):
    def add_starpaint_to_inventory(self):
        app = App.get_running_app()
        inventory = app.root.ids.Inventory_Grid
        # The item which needs to be put into inventory
        # this is the Image widget
        item = Image(source="pictures/valdstafar/showroom/starpaint.png")
        if "Starpaint" not in inventory.ids:
            inventory.add_widget(item)
            # change id here.
            inventory.ids["Starpaint"] = item  # Add the item to the ids dictionary
            starpaint_widget = self.ids.StarPaint
            if starpaint_widget.parent:
                starpaint_widget.parent.remove_widget(starpaint_widget)


class ValdstafarLanding(Screen):
    pass

class EndLanding(Screen):
    pass

class Experience(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update_compass_coordinates, 0.1)

    def update_compass_coordinates(self, dt):
        """Update Compass coordinates with Boat's current position."""
        app = App.get_running_app()
        map_screen = app.root.ids.ScreenManager.get_screen("Map")  # Ensure correct id
        boat = map_screen.ids.Boat  # Get the Boat instance
        compass = app.root.ids.Inventory_Grid.ids.get("Compass")

        if compass:
            compass.x_coords = boat.x
            compass.y_coords = boat.y



    
    def add_compass_to_inventory(self):
        app = App.get_running_app()
        print(app.root.ids)
        inventory = app.root.ids.Inventory_Grid
        map = app.root.ids.ScreenManager.get_screen("Map")
        boat = map.ids.Boat
        ups = Compass(x_coords=boat.x, y_coords=boat.y)
        print(inventory.ids)
        if "Compass" not in inventory.ids:
            inventory.add_widget(ups)
            inventory.ids.Compass = ups

class Compass(BoxLayout):
    x_coords = NumericProperty(0)
    y_coords = NumericProperty(0)
    pass
        


























class StarsailorApp(App):
    def build(self):
        root = Starsailor()
        self.root = root
        return root


if __name__ == '__main__':
    StarsailorApp().run()
