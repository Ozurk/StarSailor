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


Builder.load_file("Starsailor.kv")


class Starsailor(BoxLayout):
    money = NumericProperty(0)

class MainMenu(Screen):
    # start screen
    pass

class IntroScreen(Screen):
    # Intro_Screen
    pass

class Map(Screen):
    # Central Map
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

    def add_hardlight_to_inventory(self):
        app = App.get_running_app()
        inventory = app.root.ids.Inventory_Grid
        hardlight = Image(source="pictures/heavens_forge/the factory/hardlight.png")
        if "Hardlight" not in inventory.ids:
            inventory.add_widget(hardlight)
            inventory.ids.Hardlight = hardlight


class ChtakLanding(Screen):
    pass

class TwilightIslesLanding(Screen):
    pass


class Showroom(Screen):
    def add_starpaint_to_inventory(self):
        app = App.get_running_app()
        inventory = app.root.ids.Inventory_Grid
        # The item which needs to be put into inventory
        # this is the Image widget
        item = Image(source="pictures/valdstafar/showroom/starpaint.png")
        if "Starpaint" not in inventory.ids:
            inventory.add_widget(item)
            # change id here. This would surely have been a great time for abstraction
            inventory.ids.Starpaint = item

class ValdstafarLanding(Screen):
    pass

class EndLanding(Screen):
    pass

































class StarsailorApp(App):
    def build(self):
        root = Starsailor()
        self.root = root
        return root


if __name__ == '__main__':
    StarsailorApp().run()
