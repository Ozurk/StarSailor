# this is the file where the game will actually be done
import logging
from functions import *

import time
import os

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug("start of file")
time.sleep(1)

# this is rather self-explanatory
intro_screen()
print("\n")
os.system("cls")
time.sleep(1)
print(os.getcwd())
typing_effect(get_file(r"\storyline\intro"))

