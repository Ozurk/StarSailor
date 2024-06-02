import tkinter as tk
import main_gui as main
from PIL import Image, ImageTk


class Starsailor(main.MainWindow):
    def __init__(self):
        super().__init__()
        self.original_image = None
        self.picture_as_label = None
        self.starsailor_img = None
        self.starsailor_picture = None
        self.start_active_frame()
        self.intro_screen()

    def start_active_frame(self):
        self.active_frame = tk.Frame(self.root, background="#001E24")
        self.active_frame.columnconfigure(1, weight=1)
        self.active_frame.columnconfigure(2, weight=1)
        self.active_frame.columnconfigure(3, weight=1)
        self.active_frame.columnconfigure(4, weight=1)
        self.active_frame.columnconfigure(5, weight=1)
        self.active_frame.columnconfigure(6, weight=1)
        self.active_frame.columnconfigure(7, weight=1)
        self.active_frame.columnconfigure(8, weight=1)
        self.active_frame.columnconfigure(9, weight=1)
        self.active_frame.rowconfigure(0, weight=1)
        self.active_frame.rowconfigure(1, weight=1)
        self.active_frame.rowconfigure(2, weight=1)
        self.active_frame.rowconfigure(3, weight=1)
        self.active_frame.rowconfigure(4, weight=1)
        self.active_frame.rowconfigure(5, weight=1)
        self.active_frame.rowconfigure(6, weight=1)
        self.active_frame.rowconfigure(7, weight=1)
        self.active_frame.rowconfigure(8, weight=1)
        self.active_frame.rowconfigure(9, weight=1)

        self.active_frame.pack(fill='x')

    def intro_screen(self):
        start_button = tk.Button(self.active_frame, text="Start")
        start_button.grid(column=0, columnspan=10, row=0, rowspan=2, sticky=tk.NSEW)

        load_button = tk.Button(self.active_frame, text="Load_Game")
        load_button.grid(column=0, columnspan=10, row=2, sticky=tk.NSEW)

        instructions_button = tk.Button(self.active_frame, text="Instructions")
        instructions_button.grid(column=0, columnspan=10, row=3, sticky=tk.NSEW)

        help_button = tk.Button(self.active_frame, text="Help")
        help_button.grid(column=0, columnspan=10, row=4, sticky=tk.NSEW)

        credits_button = tk.Button(self.active_frame, text="Credits")
        credits_button.grid(column=0, columnspan=10, row=5, sticky=tk.NSEW)

        self.original_image = Image.open("../pictures/coverphoto.gif")
        self.starsailor_img = self.original_image
        self.starsailor_picture = ImageTk.PhotoImage(self.starsailor_img)
        self.picture_as_label = tk.Label(self.active_frame, image=self.starsailor_picture)
        self.picture_as_label.grid(column=10, row=0, rowspan=9, sticky=tk.NSEW)
        self.active_frame.bind("<Configure>", self.resize_image)

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


test = Starsailor()
test.run_mainloop()
