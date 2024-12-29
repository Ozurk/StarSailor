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
            inventory.width = self.width
            inventory.disabled = False
        else:  # If currently visible
            inventory.opacity = 0
            inventory.width = 0
    


class MainMenu(Screen):
    # start screen
    pass

class IntroScreen(Screen):
    intro = """As the captain of the Starbound Skiff, a ship unlike any other—crafted from starlight and wood—you’ve always been the guardian of the seas and skies.
But disaster struck when your loyal companion, Astra the sea turtle, was taken by the nefarious Tideforged, a shadowy entity that thrives in the darkest depths.
With Astra gone, the balance of the ocean is unraveling. Whispers from the waves reveal that Astra is being held captive in a hidden underwater stronghold,
guarded by riddles, traps, and creatures born of the Tideforged’s wickedness.
Your mission is clear: navigate treacherous waters, decode ancient maps, and harness the magic of the seas to find Astra.
 But reaching her won’t be enough. To save your friend, you must face the Tideforged and restore harmony to the waters.
Will your courage and wit be enough to save Astra and uncover the secrets of the ocean’s depths? The tides wait for no one, Captain."""

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
            boat.y += 15
            boat.source = 'pictures/Boats/boat_in_motion_up.png'
            scroll_distance = scrollview.convert_distance_to_scroll(0, 15)
            scrollview.scroll_y = scrollview.scroll_y + scroll_distance[1]

        elif direction == 'down':
            boat.y -= 15
            boat.source = 'pictures/Boats/boat_in_motion_down.png'
            scroll_distance = scrollview.convert_distance_to_scroll(0, -15)
            scrollview.scroll_y = scrollview.scroll_y + scroll_distance[1]

        elif direction == 'left':
            boat.source = 'pictures/Boats/boat_in_motion_left.png'
            boat.x -= 15
            scroll_distance = scrollview.convert_distance_to_scroll(-15, 0)
            scrollview.scroll_x = scrollview.scroll_x + scroll_distance[0]

        elif direction == 'right':
            boat.source = 'pictures/Boats/boat_in_motion.png'
            boat.x += 15   
            scrollview.convert_distance_to_scroll(15, 0)
            scroll_distance = scrollview.convert_distance_to_scroll(15, 0)
            scrollview.scroll_x = scrollview.scroll_x + scroll_distance[0]
        print(boat.pos)
        



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
    
    dialog = """
A Overclocked Lightwelder runs red hot steam whistling off its rotund metallic frame.

It's voice box drones out to you:

I have overseen this forge for millennia and time has taken its toll on me.

These rusty joints once shined with a coat of star paint but has since peeled off over the many centuries in this immense heat, 

and without its protective properties, I fear for my imminent dissolution.

I fear the last can of starpaint was used up decades ago, should you find some. I will bestow upon you a pallet of hardlight.

---This will surely be invaluable in the exploration of more distant skies---"""

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
    
    dialog = """
You have arrived at Ch'tak
------------------------------------------------------------------------------------------------------------------------
Ch'tak is a frigid wetland of icefloes and fetid swamps.
The mire teems with flora and fauna that will devour any ill equipped expedition.
The mud and frostbite form a grim synergy, as the former has claimed as many boots as the latter has feet.
Fruits unique to the Deep Bog pollinate the air with thick spores that cling to the insides of ones' lungs and slowly suffocate you as they grow into barbed hairy tufts.
Exotic parasites attracted to both heat and light swarm the air and waters, their buzzing perennial as the stench of decay pervading the muck.
Anything that could survive here would certainly be robust, and probably a predatory.
So imagine your surprise when you find a hospitable settlement marked in the ship's database of Imperial starcharts.
It appears to be an abandoned outpost of the Empire, now colonized by an indigenous tribe of plant-based lifeforms.
The rusty military base as been reclaimed by nature, and its new inhabitants have crafted a treetop village out of its overgrown skeleton.
Gourdlike yurts hang from the canopy, intrinsically linked by a bridge network as numerous and complex as a hyphae system.
You dock upon a weathered landing pad, next to a parapet that has been repurposed into a garden.
You are greeted by a being with the appearance of a dandelion on two legs woven out of reeds. It shakes its head, and makes a number of obscure gestures you cannot interpret.
It knows no language you can understand, let alone a mouth to speak with, but it clearly means you no harm and soon waddles off.
You call after it but it ignores you completely.
As you enter into the village, you have similar luck with all you come across."""

class TwilightIslesLanding(Screen):
    pass


class Showroom(Screen):
    def add_xyclon_to_inventory(self):
        app = App.get_running_app()
        inventory = app.root.ids.Inventory_Grid
        # The item which needs to be put into inventory
        # this is the Image widget
        item = Image(source="pictures/valdstafar/showroom/Xclon-3.png")
        if "Xyclont" not in inventory.ids:
            inventory.add_widget(item)
            # change id here.
            inventory.ids["Xyclon"] = item  # Add the item to the ids dictionary
            xyclon_widget = self.ids.Xyclon
            if xyclon_widget.parent:
                xyclon_widget.parent.remove_widget(xyclon_widget)


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
    def add_machine_to_inventory(self):
        app = App.get_running_app()
        inventory = app.root.ids.Inventory_Grid
        # The item which needs to be put into inventory
        # this is the Image widget
        item = Image(source="pictures/valdstafar/showroom/machine.png")
        if "Machine" not in inventory.ids:
            inventory.add_widget(item)
            # change id here.
            inventory.ids["Machine"] = item  # Add the item to the ids dictionary
            machine_widget = self.ids.Machine
            if machine_widget.parent:
                machine_widget.parent.remove_widget(machine_widget)


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
        
    dialog = """"An amber mushroom man lounges, eight feet tall even in a sitting position,
as thick as a tree trunk, draped in finery of deepest sapphire
and cradling a blade of shimmering Starglass between his rooted arms and legs.
Sharp, fierce periwinkle pupils betray droopy eyelids beneath the brim his golden cap.
The camaraderie of the court drowns out as your mind fills "
                      "with a voice as fierce as sunlight and rich as honey:
On a journey, it is as important to know where you are, as it is to know where you are going.

Altough I can not tell you where you will find your friend,

---This Universal Positioning System [UPS] informs you of where you are---"""


    
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
        

class Navigator(Screen):
    def add_goggles_to_inventory(self):
        app = App.get_running_app()
        print(app.root.ids)
        inventory = app.root.ids.Inventory_Grid
        goggles = Image(source='pictures/twilight_isles/goggles.png')
        print(inventory.ids)
        if "Goggles" not in inventory.ids:
            inventory.add_widget(goggles)
            inventory.ids.Goggles = goggles
    
    dialog = """"Captain! A moment, if you will?"
a chipper young woman aks you. You turn and are surprised to find yourself face to face with what appears to be a mummy.
The whole right side of her face as well as most of her body are tightly wound in bandages, and a long lined aviator's jacket drapes easily from her shoulders.
The left side of her face reveals a friendly smile of charming, crooked teeth and a pupil that shines with silver light.
"Listen Cap, someone round here's gonna go gossipping to you bout me anyways, so I figure ye ought to hear it from me first.
I was a navigator on the 'Lady Jenny'.
A damn fine navigator, for a damn fine ship. But the crew...

Have you ever heard of Siren-Suns? They weave the most wondrous light and their warmth is seductive. Our captain set a
course that neared one's orbit, and equipped us with safety gear to protect our heads and hearts as we passed. But one
foolish sailor hadn't properly fastened his goggles, and the sun's allure influenced him instantly. Possessed, he began
ripping goggles off the faces of his fellows, and a mutiny of sun smitten supplicants multiplied across the ship. They
commandeered the Jenny. They flung ol' captain off the side. I tried to fight, but was pinned back by the lot of em as
they took the helm and steered us toward oblivion.

I shielded my gaze against its whispering rays, while they blinded themselves staring into that blazing beauty. The
reverie broke when their eyes began to bubble, but by then we didn't have much longer before the rest of our selves
followed suite. I blindly reached for the helm and veered us off course. I remember nary after that. These turtle
priests found us. They specialize in the the treatment of star ailments. Wrapped me up good here. Rest of my boys was
cooked, and consigned to the skies.

I took these googles from the dead deck-hand, s'pose he don't need em' anymore. 

-- Take them, you will need them if you insist on venturing into the negitive x coords---"""


class Turtle(Screen):
    dialog = """Here is a map with the coordinates to a the secret portal"""
    
    def add_map_to_inventory(self):
        app = App.get_running_app()
        print(app.root.ids)
        inventory = app.root.ids.Inventory_Grid
        map = Image(source='pictures/twilight_isles/turtles/map.png')
        print(inventory.ids)
        if "Map" not in inventory.ids:
            inventory.add_widget(map)
            inventory.ids.Map = map


class WormHoleLanding(Screen):
    dialog = 'Welcome to the wormhole launch site'
    

    def attempt_wormhole_travel(self):
        app = App.get_running_app()
        map_screen = app.root.ids.ScreenManager.get_screen("Map")
        boat = map_screen.ids.Boat
        screenmanager = app.root.ids.ScreenManager
        hardlight = app.root.ids.Inventory_Grid.ids.get("Hardlight")
        goggles = app.root.ids.Inventory_Grid.ids.get("Goggles")
        print(app.root.ids.ScreenManager.current)
        fail_screen = screenmanager.get_screen('FailureScreen')
        fail_label = fail_screen.ids.FailureLabel

        # Set failure texts
        if hardlight is None:
            screenmanager.current = 'FailureScreen'
            fail_label.text = "Your Ship was destroyed through 'Spaghetification'"
        elif goggles is None:
            pass
        elif not 245 < boat.x < 445 and -550 < boat.y < - 350:
            pass
        else:
            app.root.ids.ScreenManager.current = 'SuccessScreen'


    def add_map_to_inventory(self):
        app = App.get_running_app()
        print(app.root.ids)
        inventory = app.root.ids.Inventory_Grid
        map = Image(source='pictures/twilight_isles/turtles/map.png')
        print(inventory.ids)
        if "Map" not in inventory.ids:
            inventory.add_widget(map)
            inventory.ids.Map = map



class FailureScreen(Screen):
    pass

class SuccessScreen(Screen):
    pass

class StarsailorApp(App):
    def build(self):
        root = Starsailor()
        self.root = root
        return root


if __name__ == '__main__':
    StarsailorApp().run()



