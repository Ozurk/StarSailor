# this is the file where the game will actually be done
import logging
import functions
from storyline_functions import *


import time
import os

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug("start of file")


# this is rather self-explanatory
functions.intro_screen()
print("\n")
input("Press Enter to Continue".center(110, "-") + "\n")
os.system("cls")

intro()

while True:
    random_event()
