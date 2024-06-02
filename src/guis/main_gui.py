import tkinter as tk
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
        self.bottom_bar = None
        self.start_menu_frame = None
        self.root = tk.Tk()
        # self.root.resizable(width=False, height=False)
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x = (self.screen_width // 2) - (1000 // 2)
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
        menu.add_command(label="Save Game", activebackground="#1F262A")
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

        food_label = tk.Button(tool_bar, text=f"Food: {food}", justify="center", background="#469BAB")
        food_label.grid(column=1, row=1, sticky=tk.NSEW)

        money_label = tk.Button(tool_bar, text=f"Money: {money}", justify="center", background="#469BAB")
        money_label.grid(column=2, row=1, sticky=tk.NSEW)

        sanity_label = tk.Button(tool_bar, text=f"Sanity: {sanity}", justify="center", background="#469BAB")
        sanity_label.grid(column=3, row=1, sticky=tk.NSEW)

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

    def run_mainloop(self):
        self.root.mainloop()


if __name__ == "__main__":
    main_window = MainWindow()
    main_window.run_mainloop()
