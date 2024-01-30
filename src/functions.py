import sys
import time
import re


# ------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------Variables--------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------------
# ---------------------------------This is what gets and print the text files--------------------------------------
# -----------------------------------------------------------------------------------------------------------------


def get_file(file_path):
    file = open(file_path, "r")
    text = file.read()
    text = text.strip()
    file.close()
    return text


# -----------------------------------------------------------------------------------------------------------------
# ---------------------------------This is what types strings out -------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------


def typing_effect(string, wait_time):
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(wait_time)  # this controls the speed of the game


# -----------------------------------------------------------------------------------------------------------------
# ---------------------------------This is what prints out the stats ----------------------------------------------
# -----------------------------------------------------------------------------------------------------------------


def text_regex(text):
    alphabet_regex = re.compile("[a-zA-Z]+")
    mo = alphabet_regex.findall(text)
    return mo
    # will return a list of strings


def intro_screen(wait):
    # this is the fancy little intro screen
    typing_effect("-" * 110, wait)
    print()
    typing_effect("-" * 110, wait)
    print()
    typing_effect("-" * 110, wait)
    typing_effect("""
        *        #####                       #####                                           *
                #     # #####   ##   #####  #     #   ##   # #       ####  #####    *
       *        #         #    #  #  #    # #        #  #  # #      #    # #    #          
   *             #####    #   #    # #    #  #####  #    # # #      #    # #    #               *
                      #   #   ###### #####        # ###### # #      #    # #####         *
          *     #     #   #   #    # #   #  #     # #    # # #      #    # #   #            
                 #####    #   #    # #    #  #####  #    # # ######  ####  #    # """.center(110, " "), 0)
    print("\n")
    typing_effect("-" * 110, wait)
    print()
    typing_effect("-" * 110, wait)
    print()
    typing_effect("-" * 110, wait)
    time.sleep(.75)
    print()
    input("Press Enter to Continue...".center(110, " ") + "\n")
    print("\n")
    # todo un-comment this ^


def one_or_two():
    user_input = input("\n Enter [1] or [2]\n")
    if user_input == "1":
        return int(user_input)
    elif user_input == "2":
        return int(user_input)
    else:
        print("You must enter 1 or 2")
        one_or_two()
