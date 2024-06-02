import tkinter as tk
import main_gui as main
from PIL import Image, ImageTk
import shelve
import os


class Starsailor(main.MainWindow):
    def __init__(self):
        super().__init__()
        self.stats = None
        self.game_name = None
        self.original_image = None
        self.picture_as_label = None
        self.starsailor_img = None
        self.starsailor_picture = None
        self.create_playable_window_frame()
        self.intro_screen()

    def create_playable_window_frame(self):
        self.start_menu_frame = tk.Frame(self.root, background="#001E24")
        self.start_menu_frame.columnconfigure(1, weight=1)
        self.start_menu_frame.columnconfigure(2, weight=1)
        self.start_menu_frame.columnconfigure(3, weight=1)
        self.start_menu_frame.columnconfigure(4, weight=1)
        self.start_menu_frame.columnconfigure(5, weight=1)
        self.start_menu_frame.columnconfigure(6, weight=1)
        self.start_menu_frame.columnconfigure(7, weight=1)
        self.start_menu_frame.columnconfigure(8, weight=1)
        self.start_menu_frame.columnconfigure(9, weight=1)
        self.start_menu_frame.rowconfigure(0, weight=1)
        self.start_menu_frame.rowconfigure(1, weight=1)
        self.start_menu_frame.rowconfigure(2, weight=1)
        self.start_menu_frame.rowconfigure(3, weight=1)
        self.start_menu_frame.rowconfigure(4, weight=1)
        self.start_menu_frame.rowconfigure(5, weight=1)
        self.start_menu_frame.rowconfigure(6, weight=1)
        self.start_menu_frame.rowconfigure(7, weight=1)
        self.start_menu_frame.rowconfigure(8, weight=1)
        self.start_menu_frame.rowconfigure(9, weight=1)

        self.start_menu_frame.pack(fill='x')

    def intro_screen(self):
        def new_game():
            self.start_menu_frame.destroy()
            new_game_frame = tk.Frame(self.root)
            new_game_frame.columnconfigure(0, weight=1)
            new_game_frame.columnconfigure(1, weight=1)
            new_game_frame.columnconfigure(2, weight=1)
            new_game_frame.columnconfigure(3, weight=1)
            new_game_frame.columnconfigure(4, weight=1)
            new_game_label = tk.Label(new_game_frame, text="New Game", background="#1F262A", foreground="#B0C4DE")
            new_game_label.grid(column=0, columnspan=5, row=0, sticky=tk.NSEW)
            player_name_entry_label = tk.Label(new_game_frame, text="Player Name")
            player_name_entry_label.grid(column=0, row=1)
            player_name = tk.Entry(new_game_frame)
            player_name.grid(column=1, columnspan=3, row=1, sticky=tk.NSEW)
            game_name = tk.Entry(new_game_frame)
            game_name_entry_label = tk.Label(new_game_frame, text="Game Name")
            game_name_entry_label.grid(column=0, row=2)
            game_name.grid(column=1, columnspan=3, row=2, sticky=tk.NSEW)
            new_game_button = tk.Button(new_game_frame, text="New Game", bg='green',
                                        command=Live_Game.initialise_new_game())
            new_game_button.grid(column=3, row=4, sticky=tk.NSEW)
            new_game_frame.pack(fill="x")

        new_game_button = tk.Button(self.start_menu_frame, text="New Game", command=new_game)
        new_game_button.grid(column=0, columnspan=10, row=0, rowspan=2, sticky=tk.NSEW)

        load_button = tk.Button(self.start_menu_frame, text="Load_Game")
        load_button.grid(column=0, columnspan=10, row=2, sticky=tk.NSEW)

        instructions_button = tk.Button(self.start_menu_frame, text="Instructions")
        instructions_button.grid(column=0, columnspan=10, row=3, sticky=tk.NSEW)

        help_button = tk.Button(self.start_menu_frame, text="Help")
        help_button.grid(column=0, columnspan=10, row=4, sticky=tk.NSEW)

        credits_button = tk.Button(self.start_menu_frame, text="Credits")
        credits_button.grid(column=0, columnspan=10, row=5, sticky=tk.NSEW)

        self.original_image = Image.open("../../pictures/coverphoto.gif")
        self.starsailor_img = self.original_image
        self.starsailor_picture = ImageTk.PhotoImage(self.starsailor_img)
        self.picture_as_label = tk.Label(self.start_menu_frame, image=self.starsailor_picture)
        self.picture_as_label.grid(column=10, row=0, rowspan=9, sticky=tk.NSEW)
        self.start_menu_frame.bind("<Configure>", self.resize_image)

    def resize_image(self, event):

        og_width, og_height = self.original_image.size
        aspect_ratio = og_width / og_height
        new_height = event.height
        new_width = event.width * (new_height / og_height)
        if (new_width / new_height) > aspect_ratio:
            new_width = int(new_height * aspect_ratio)
        else:
            new_height = int(new_width / aspect_ratio)
        resized_image = self.original_image.resize((new_width, new_height),
                                                   Image.Resampling.LANCZOS)
        self.starsailor_img = ImageTk.PhotoImage(resized_image)
        self.picture_as_label.config(image=self.starsailor_img)


class Live_Game(Starsailor):
    def __init__(self):
        super().__init__()
        self.stats = None
        self.game_name = None
        self.player_name = None

    def initialise_new_game(self, game_name, player_name):
        os.chdir("src/tables/Saved States")
        self.game_name = shelve.open(str(game_name))
        self.game_name["player name"] = str(player_name)
        self.player_name = player_name
        self.stats = {"food": 100,
                      "money": 1000,
                      "sanity": 80,
                      "Inventory": {},
                      "Planets Visited": {"Heaven's Forge": False, "Twilight Isles": False,
                                          "Acropolis": False, "Loamstone": False, "Ch'tak": False,
                                          "Valdsafar": False, "Titiana": False, "B-IRS": False},
                      "Critical Events": {"Talashandra": False, "Talashandra 2": False, "Talashandra 3": False,
                                          "Gas-Beings": False, "Turtles": False}}


test = Starsailor()
test.run_mainloop()
