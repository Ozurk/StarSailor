# this is the file where the game will actually be done
import logging
from functions import *
from storyline_functions import *


import time
import os

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug("start of file")
time.sleep(1)

# this is rather self-explanatory
intro_screen()
print("\n")
input("Press Enter to Continue".center(110, "-") + "\n")
os.system("cls")
print(os.getcwd())

intro()
choice = user_number_validation(input("\nenter 1 or 2"))
if choice == "1":
    chapter1a()
elif choice == "2":
    chapter1b()
else:
    time.sleep(2)
    os.system("cls")
    print("\nyou did not enter a 1 or 2\nI will pick for you")
    time.sleep(2)
    chapter1b()







