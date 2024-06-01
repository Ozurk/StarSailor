import tkinter as tk
from PIL import Image, ImageTk

# todo player stats class
# todo player stats as a csv
food = 100
money = 1000
sanity = 75


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.create_window()

    def create_window(self):
        self.root.geometry('1000x600')
        self.root.title("Starsailor")
        self.tool_bar_widgets()
        self.canvas()

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

        help_button = tk.Button(tool_bar, bitmap="question", activebackground="#1F262A", bg="#B0C4DE", relief="raised",
                                borderwidth=5)
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

    def canvas(self):
        main_canvas_frame = tk.Frame(self.root)
        # todo make a big ol frame that covers everything but the toolbar
        canvas = tk.Canvas(main_canvas_frame, height=700, width=700)
        self.starsailor_image = Image.open("../pictures/coverphoto.gif")
        self.starsailor_photoimage = ImageTk.PhotoImage(self.starsailor_image)
        starsailor_img = canvas.create_image((100, 100), image=self.starsailor_photoimage, anchor=tk.NW)
        canvas.grid()

        main_canvas_frame.pack()

    def run_mainloop(self):
        self.root.mainloop()


main_window = MainWindow()
main_window.run_mainloop()


class Persistant_Functions():
    def __init__(self):
        pass

    def save_game(self):
        print("saved game!")
        pass
