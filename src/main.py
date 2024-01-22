# this is the file where the game will actually be done
import logging
from functions import dice
from functions import get_file
from functions import typing_effect
from functions import stats
from functions import text_regex

import time
import os

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug("start of file")
time.sleep(1)
# this is the fancy little intro screen
typing_effect("-"*90, .005)
print()
typing_effect("-"*90, .005)
print()
typing_effect("-"*90, .005)
typing_effect("""
             #####                       #####                                
            #     # #####   ##   #####  #     #   ##   # #       ####  #####  
            #         #    #  #  #    # #        #  #  # #      #    # #    # 
             #####    #   #    # #    #  #####  #    # # #      #    # #    # 
                  #   #   ###### #####        # ###### # #      #    # #####  
            #     #   #   #    # #   #  #     # #    # # #      #    # #   #  
             #####    #   #    # #    #  #####  #    # # ######  ####  #    # """.center(150," "), .005)
print("\n")
typing_effect("-"*90, .005)
print()
typing_effect("-"*90, .005)
print()
typing_effect("-"*90, .005)


