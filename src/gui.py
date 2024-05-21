import tkinter as tk

# todo player stats class
# todo player stats as a csv
food = 100


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.create_window()

    def create_window(self):
        self.root.geometry('1000x700')
        self.root.title("Starsailor")
        self.tool_bar_widgets()

    def tool_bar_widgets(self):
        tool_bar = tk.Frame(self.root)
        index = 0
        for columns in range(6):
            tool_bar.columnconfigure(index, weight=1)
            index += 1
        banner = tk.Label(tool_bar, text="STARSAILOR", bg='navy', font=("Times New Roman", 20), fg='yellow')
        banner.grid(row=0, column=1, columnspan=4, sticky=tk.N + tk.EW)

        save_button = tk.Button(tool_bar, text="Save")
        save_button.grid(column=5, row=0, sticky=tk.NSEW)

        help_button = tk.Button(tool_bar, bitmap="question")
        help_button.grid(column=0, row=0, sticky=tk.NSEW)

        inventory_button = tk.Button(tool_bar, text="Inventory")
        inventory_button.grid(column=0, row=1, sticky=tk.N+tk.EW)

        food_button = tk.Button(tool_bar, text="Food", font=("Times New Roman", 10))
        food_button.grid(column=1, row=1, sticky=tk.N + tk.EW)

        money_button = tk.Button(tool_bar, text="Money", font=("Times New Roman", 10))
        money_button.grid(column=2, row=1, sticky=tk.N + tk.EW)

        sanity_button = tk.Button(tool_bar, text="Sanity", font=("Times New Roman", 10))
        sanity_button.grid(column=3, row=1, sticky=tk.N + tk.EW)

        sanity_button = tk.Button(tool_bar, text="Sanity", font=("Times New Roman", 10))
        sanity_button.grid(column=4, columnspan=5, row=1, sticky=tk.N + tk.EW)

        tool_bar.pack(fill="x")

    def run_mainloop(self):
        self.root.mainloop()


main_window = MainWindow()
main_window.run_mainloop()
