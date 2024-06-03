import tkinter as tk
import os
import shelve
import time
from PIL import Image, ImageTk


def get_file(file_path):
    try:
        file = open(file_path, "r")
        text = file.read()
        text = text.strip()
        file.close()
        return text
    except UnicodeDecodeError:
        file = open(file_path, "r", encoding="utf-8")
        text = file.read()
        text = text.strip()
        file.close()
        return text


# todo player stats class
# todo player stats as a csv
food = 100
money = 1000
sanity = 75


class MainWindow:
    def __init__(self):
        self.food_label = None
        self.money_label = None
        self.sanity_label = None
        self.bottom_bar = None
        self.start_menu_frame = None
        self.root = tk.Tk()
        # self.root.resizable(width=False, height=False)
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x = (self.screen_width // 2) - (1000 // 2)
        self.game_shelve = None
        self.game_name_entry = None
        self.player_name_entry = None
        self.player_name = None
        self.stats = self.stats = {"food": 100,
                                   "money": 0,
                                   "sanity": 0,
                                   "Inventory": {},
                                   "Planets Visited": {"Heaven's Forge": False, "Twilight Isles": False,
                                                       "Acropolis": False, "Loamstone": False, "Ch'tak": False,
                                                       "Valdsafar": False, "Titiana": False, "B-IRS": False},
                                   "Critical Events": {"Talashandra": False, "Talashandra 2": False,
                                                       "Talashandra 3": False,
                                                       "Gas-Beings": False, "Turtles": False}}
        self.game_name = None
        self.original_image = None
        self.picture_as_label = None
        self.starsailor_img = None
        self.starsailor_picture = None
        self.create_window()

    def create_window(self):
        self.root.geometry(f'1000x750+{self.x}+0')
        self.root.title("Starsailor")
        self.tool_bar_widgets()
        self.start_menu_frame = tk.Frame()

    def tool_bar_widgets(self):
        tool_bar = tk.Frame(self.root)
        tool_bar.columnconfigure(0, weight=2)
        tool_bar.columnconfigure(1, weight=1)
        tool_bar.columnconfigure(2, weight=1)
        tool_bar.columnconfigure(3, weight=1)
        tool_bar.columnconfigure(4, weight=2)

        banner = tk.Label(tool_bar, text="Starsailor", bg='#2E294E', font=("Times New Roman", 30), fg='#B0C4DE')
        banner.grid(row=0, column=1, columnspan=3, sticky=tk.N + tk.EW)

        menu_button = tk.Menubutton(tool_bar, text="Menu", font=("Times New Roman", 15), relief="raised", borderwidth=5,
                                    activebackground="#2E294E", bg="#B0C4DE",
                                    activeforeground="#B0C4DE")
        menu_button.grid(column=4, row=0, sticky=tk.NSEW)

        menu = tk.Menu(menu_button, tearoff=0, borderwidth=2)
        menu_button["menu"] = menu
        menu.add_command(label="Save Game", activebackground="#1F262A", command=self.save_game)
        menu.add_command(label="Restart Game", activebackground="#1F262A")
        menu.add_command(label="Load Game", activebackground="#1F262A")

        def show_help():
            help_window = tk.Tk()
            help_message = tk.Message(help_window, text=get_file("../storyline/setup/Setup and Help"), fg="black")
            help_message.pack()
            help_window.geometry(f'500x500+{75 + self.x}+0')

            def close_help():
                help_window.destroy()

            close_button = tk.Button(help_window, text="close", bg="red", command=close_help)
            close_button.pack(anchor=tk.SE, side=tk.BOTTOM)

        help_button = tk.Button(tool_bar, bitmap="question", activebackground="#1F262A", bg="#B0C4DE", relief="raised",
                                borderwidth=5, command=show_help)
        help_button.grid(column=0, row=0, sticky=tk.NSEW)

        inventory_button = tk.Button(tool_bar, text="Inventory", borderwidth=3, relief='raised', bg="#BC4842")
        inventory_button.grid(column=0, row=1, sticky=tk.N + tk.EW)

        self.food_label = tk.Button(tool_bar, text=f"Food: {self.stats['food']}", justify="center",
                                    background="#469BAB")
        self.food_label.grid(column=1, row=1, sticky=tk.NSEW)

        self.money_label = tk.Button(tool_bar, text=f"Money: {self.stats['money']}", justify="center",
                                     background="#469BAB")
        self.money_label.grid(column=2, row=1, sticky=tk.NSEW)

        self.sanity_label = tk.Button(tool_bar, text=f"Sanity: {self.stats['sanity']}", justify="center",
                                      background="#469BAB")
        self.sanity_label.grid(column=3, row=1, sticky=tk.NSEW)

        passenger_button = tk.Button(tool_bar, text="Passengers", borderwidth=3, relief='raised', bg="#BC4842")
        passenger_button.grid(column=4, row=1, sticky=tk.N + tk.EW)
        tool_bar.pack(fill="x")

        self.bottom_bar = tk.Frame(self.root)
        self.bottom_bar.columnconfigure(0, weight=1)
        self.bottom_bar.columnconfigure(1, weight=1)
        return_to_ship_button = tk.Button(self.bottom_bar, text="Return to Ship", height=8, bg="#BC4842")
        return_to_ship_button.grid(column=0, row=0, sticky=tk.NSEW)

        return_to_chtak_button = tk.Button(self.bottom_bar, text="Return to Ch'tak", height=8, bg="#B0C4DE",
                                           font=("Times New Roman", 10))
        return_to_chtak_button.grid(column=1, row=0, sticky=tk.NSEW)

        self.bottom_bar.pack(fill="x", side=tk.BOTTOM)

    def initialise_new_game(self):
        self.player_name = self.player_name_entry.get()
        self.game_name = self.game_name_entry.get()
        print(os.getcwd())
        if not os.getcwd().endswith("Saved States"):
            os.chdir("..\\tables\\Saved States")
        os.mkdir(self.game_name)
        time.sleep(.5)
        os.chdir(f"{self.game_name}")
        self.game_shelve = shelve.open(self.game_name)
        self.game_shelve["player name"] = self.player_name
        self.stats = {"food": 100,
                      "money": 1000,
                      "sanity": 80,
                      "Inventory": {},
                      "Planets Visited": {"Heaven's Forge": False, "Twilight Isles": False,
                                          "Acropolis": False, "Loamstone": False, "Ch'tak": False,
                                          "Valdsafar": False, "Titiana": False, "B-IRS": False},
                      "Critical Events": {"Talashandra": False, "Talashandra 2": False, "Talashandra 3": False,
                                          "Gas-Beings": False, "Turtles": False}}
        os.chdir("../")
        # todo investigate the shelving system
        self.sanity_label.update_idletasks()
        self.food_label.update_idletasks()
        self.money_label.update_idletasks()

    def save_game(self):
        self.game_shelve["stats"] = self.stats

    def load_game(self):
        pass

    def run_mainloop(self):
        self.root.mainloop()

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


if __name__ == "__main__":
    main_window = MainWindow()
    main_window.run_mainloop()
