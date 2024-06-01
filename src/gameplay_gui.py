import tkinter as tk
import main_gui as main
from PIL import Image, ImageTk


class Starsailor(main.MainWindow):
    def __init__(self):
        super().__init__()
        self.picture_as_label = None
        self.starsailor_pil_img = None
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
        self.starsailor_pil_img = Image.open("../pictures/coverphoto.jpg")
        self.starsailor_picture = ImageTk.PhotoImage(self.starsailor_pil_img)
        self.picture_as_label = tk.Label(self.active_frame, image=self.starsailor_picture)
        self.picture_as_label.grid(column=0, columnspan=9, row=3, rowspan=6)


test = Starsailor()
test.run_mainloop()
