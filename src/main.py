# this is the file where the game will actually be done
import logging
from functions import *

import time
import os

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug("start of file")
time.sleep(1)

intro_screen()
print("\n")
input("Press Enter to Continue...".center(110, " ") + "\n")
os.system("cls")
time.sleep(1)

user_name = text_regex(input("What is Your Name?".center(110, " ") + "\n"))
logging.debug("the user's first name is " + user_name[0] + " and the Last name is " + user_name[1])
